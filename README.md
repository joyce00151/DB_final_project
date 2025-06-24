# DB_final_project
设计一个智能家居系统，使用fastapi或类似框架提供API管理智能家居，包括但不限于使用纪录、用户信息、安防事件、用户反馈等数据。 
# 主要文件结构如下：
```txt
smart_home_project/
├── main.py                 # FastAPI 主应用入口
├── database.sql            # 原生 SQL 建表脚本
├── populate_data.sql    # 插入模拟数据的 SQL 脚本
├── analysis.py             # 数据分析与可视化脚本
├── duck.db                 # DuckDB 数据库文件
```
# 各文件功能说明如下：
```txt
main.py：Python 脚本，FastAPI 应用的主入口，提供统一的 RESTful API 接口。
database.sql：SQL 脚本，包含原始建表语句，定义系统所用数据库的表结构。
populate_data.sql：SQL 脚本，用于插入模拟测试数据。
analysis.py：Python 脚本，实现对数据库中数据的统计分析与图表生成，输出静态 HTML 报告。
duck.db：DuckDB 数据库文件，由系统运行时自动创建与更新，存储所有数据表与内容。
```
