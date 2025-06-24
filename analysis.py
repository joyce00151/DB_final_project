import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

conn = duckdb.connect('C:/Users/Lenovo/Desktop/3B/database/Final Project/smart_home_project/duck.db')

output_dir = "report_output"
os.makedirs(output_dir, exist_ok=True)

def save_plot(df, kind, x, y, title, filename):
    ax = df.plot(kind=kind, x=x, y=y, title=title, legend=False)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

def save_heatmap(pivot_df, title, filename):
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot_df, annot=True, cmap='YlGnBu')
    plt.title(title)
    plt.tight_layout()
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

# 1. 每个用户设备使用总时长
def plot_user_total_usage():
    query = """
    SELECT 
        u.name AS user_name,
        SUM(extract('epoch' FROM (end_time - start_time)))/3600.0 AS total_hours
    FROM DeviceUsage du
    JOIN User u ON du.user_id = u.id
    GROUP BY u.name
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'user_name', 'total_hours', '每个用户使用设备总时长', 'user_total_usage.png')

# 2. 不同户型设备使用总时长
def plot_usage_by_room_size():
    query = """
    SELECT 
        CASE 
            WHEN r.area < 70 THEN '小户型'
            WHEN r.area BETWEEN 70 AND 90 THEN '中户型'
            ELSE '大户型'
        END AS room_size,
        SUM(extract('epoch' FROM (end_time - start_time)))/3600.0 AS total_usage_hours
    FROM DeviceUsage du
    JOIN User u ON du.user_id = u.id
    JOIN Room r ON u.room_id = r.id
    GROUP BY room_size
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'room_size', 'total_usage_hours', '不同户型设备使用总时长', 'room_usage.png')

# 3. 设备共用频率热力图
def plot_device_correlation():
    query = """
    SELECT 
        d1.name AS device1,
        d2.name AS device2,
        dr.frequency
    FROM DeviceRelation dr
    JOIN Device d1 ON dr.device1_id = d1.id
    JOIN Device d2 ON dr.device2_id = d2.id
    """
    df = conn.execute(query).fetchdf()
    pivot = df.pivot(index='device1', columns='device2', values='frequency').fillna(0)
    return save_heatmap(pivot, '设备共用频率热力图', 'device_correlation.png')

# 4. 用户活跃度排行（设备使用次数）
def plot_user_activity_rank():
    query = """
    SELECT 
        u.name AS user_name,
        COUNT(*) AS usage_count
    FROM DeviceUsage du
    JOIN User u ON du.user_id = u.id
    GROUP BY u.name
    ORDER BY usage_count DESC
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'user_name', 'usage_count', '用户活跃度排行', 'user_activity.png')

# 5. 最常触发安防事件的设备
def plot_security_event_top_devices():
    query = """
    SELECT 
        d.name AS device_name,
        COUNT(*) AS event_count
    FROM SecurityEvent se
    JOIN Device d ON se.device_id = d.id
    GROUP BY d.name
    ORDER BY event_count DESC
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'device_name', 'event_count', '最常触发安防事件的设备', 'security_top_devices.png')

# 6. 不同户型安防事件数量
def plot_security_event_by_area():
    query = """
    SELECT 
        CASE 
            WHEN r.area < 70 THEN '小户型'
            WHEN r.area BETWEEN 70 AND 90 THEN '中户型'
            ELSE '大户型'
        END AS room_size,
        COUNT(se.id) AS event_count
    FROM SecurityEvent se
    JOIN Device d ON se.device_id = d.id
    JOIN Room r ON d.room_id = r.id
    GROUP BY room_size
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'room_size', 'event_count', '不同户型安防事件数量', 'security_by_area.png')

# 新增1：设备类型使用时长分布
def plot_usage_by_device_type():
    query = """
    SELECT 
        d.type AS device_type,
        SUM(extract('epoch' FROM (end_time - start_time)))/3600.0 AS total_hours
    FROM DeviceUsage du
    JOIN Device d ON du.device_id = d.id
    GROUP BY d.type
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'device_type', 'total_hours', '不同设备类型使用总时长', 'usage_by_device_type.png')

# 新增2：用户反馈数量统计
def plot_feedback_count_per_user():
    query = """
    SELECT 
        u.name AS user_name,
        COUNT(f.id) AS feedback_count
    FROM Feedback f
    JOIN User u ON f.user_id = u.id
    GROUP BY u.name
    ORDER BY feedback_count DESC
    """
    df = conn.execute(query).fetchdf()
    return save_plot(df, 'bar', 'user_name', 'feedback_count', '用户反馈次数统计', 'feedback_count.png')

# 新增3：设备使用时间段热力图（小时 vs 设备）
def plot_device_usage_hour_heatmap():
    query = """
    SELECT 
        d.name AS device_name,
        EXTRACT(hour FROM du.start_time) AS usage_hour,
        COUNT(*) AS usage_count
    FROM DeviceUsage du
    JOIN Device d ON du.device_id = d.id
    GROUP BY device_name, usage_hour
    """
    df = conn.execute(query).fetchdf()
    pivot = df.pivot(index='device_name', columns='usage_hour', values='usage_count').fillna(0)
    return save_heatmap(pivot, '设备使用时间段热力图（小时）', 'device_usage_hour_heatmap.png')

# 新增4：设备使用时长与房间面积分段的关系（按设备类型细分）
def plot_usage_by_area_and_device_type():
    query = """
    SELECT 
        CASE 
            WHEN r.area < 70 THEN '小户型'
            WHEN r.area BETWEEN 70 AND 90 THEN '中户型'
            ELSE '大户型'
        END AS room_size,
        d.type AS device_type,
        SUM(extract('epoch' FROM (end_time - start_time)))/3600.0 AS total_hours
    FROM DeviceUsage du
    JOIN User u ON du.user_id = u.id
    JOIN Room r ON u.room_id = r.id
    JOIN Device d ON du.device_id = d.id
    GROUP BY room_size, d.type
    ORDER BY room_size, d.type
    """
    df = conn.execute(query).fetchdf()
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='room_size', y='total_hours', hue='device_type')
    plt.title('不同户型与设备类型使用时长关系')
    plt.xlabel('户型大小')
    plt.ylabel('使用时长（小时）')
    plt.tight_layout()
    filename = os.path.join(output_dir, 'usage_by_area_and_device_type.png')
    plt.savefig(filename)
    plt.close()
    return filename

# 新增5：简单分析设备共用时的用户使用情况（基于关系和使用次数）
def plot_device_relation_user_usage():
    query = """
    SELECT 
        d1.name AS device1,
        d2.name AS device2,
        dr.frequency,
        COUNT(DISTINCT du.user_id) AS user_count
    FROM DeviceRelation dr
    JOIN Device d1 ON dr.device1_id = d1.id
    JOIN Device d2 ON dr.device2_id = d2.id
    LEFT JOIN DeviceUsage du ON du.device_id IN (dr.device1_id, dr.device2_id)
    GROUP BY d1.name, d2.name, dr.frequency
    """
    df = conn.execute(query).fetchdf()
    if df.empty:
        return None
    df['label'] = df.apply(lambda r: f"{r.device1} & {r.device2}", axis=1)
    return save_plot(df, 'bar', 'label', 'user_count', '设备关联的用户覆盖数量', 'device_relation_user_usage.png')

def generate_html_report(image_paths_and_titles):
    html_path = os.path.join(output_dir, "report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>智能家居分析报告</title></head><body>")
        f.write("<h1>📊 智能家居系统数据分析报告</h1>")
        for img_path, title in image_paths_and_titles:
            if img_path is None:
                continue
            f.write(f"<h2>{title}</h2>\n")
            f.write(f"<img src='{os.path.basename(img_path)}' width='800'/><hr>\n")
        f.write("</body></html>")
    abs_path = os.path.abspath(html_path)
    print(f"✅ 分析报告已生成：{abs_path}")

def main():
    results = []
    results.append((plot_user_total_usage(), '每个用户使用设备总时长'))
    results.append((plot_usage_by_room_size(), '不同户型设备使用总时长'))
    results.append((plot_device_correlation(), '设备共用频率热力图'))
    results.append((plot_user_activity_rank(), '用户活跃度排行'))
    results.append((plot_security_event_top_devices(), '最常触发安防事件的设备'))
    results.append((plot_security_event_by_area(), '不同户型安防事件数量'))
    results.append((plot_usage_by_device_type(), '不同设备类型使用总时长'))
    results.append((plot_feedback_count_per_user(), '用户反馈次数统计'))
    results.append((plot_device_usage_hour_heatmap(), '设备使用时间段热力图'))
    results.append((plot_usage_by_area_and_device_type(), '不同户型与设备类型使用时长关系'))
    results.append((plot_device_relation_user_usage(), '设备关联的用户覆盖数量'))
    
    generate_html_report(results)

if __name__ == "__main__":
    main()





