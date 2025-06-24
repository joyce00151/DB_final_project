from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import duckdb
from typing import List, Optional
import os

app = FastAPI(title="Smart Home Management API")
DB_PATH = 'C:/Users/Lenovo/Desktop/3B/database/Final Project/smart_home_project/duck.db'

# 数据模型定义
class User(BaseModel):
    user_id: Optional[int]
    name: str
    age: int
    house_size: float

class Room(BaseModel):
    room_id: Optional[int]
    name: str
    user_id: int

class Device(BaseModel):
    device_id: Optional[int]
    name: str
    device_type: str
    room_id: int

class DeviceUsage(BaseModel):
    usage_id: Optional[int]
    device_id: int
    user_id: int
    timestamp: str
    duration: int  # 使用时长（分钟）

class SecurityEvent(BaseModel):
    event_id: Optional[int]
    room_id: int
    user_id: int
    event_type: str
    timestamp: str

class Feedback(BaseModel):
    feedback_id: Optional[int]
    user_id: int
    device_id: int
    comment: str
    timestamp: str

# 数据库连接方法
def get_db():
    return duckdb.connect(DB_PATH)

# ---------------------------- 用户 CRUD ----------------------------
@app.post("/users/", response_model=User)
def create_user(user: User):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO User (name, age, house_size) VALUES (?, ?, ?) RETURNING *;",
        (user.name, user.age, user.house_size)
    ).fetchone()
    return User(user_id=result[0], name=result[1], age=result[2], house_size=result[3])

@app.get("/users/", response_model=List[User])
def read_users():
    conn = get_db()
    rows = conn.execute("SELECT * FROM User").fetchall()
    return [User(user_id=r[0], name=r[1], age=r[2], house_size=r[3]) for r in rows]

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    conn = get_db()
    result = conn.execute(
        "UPDATE User SET name=?, age=?, house_size=? WHERE user_id=? RETURNING *;",
        (user.name, user.age, user.house_size, user_id)
    ).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return User(user_id=result[0], name=result[1], age=result[2], house_size=result[3])

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    result = conn.execute("DELETE FROM User WHERE user_id=?;", (user_id,))
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# ---------------------------- 房间 CRUD ----------------------------
@app.post("/rooms/", response_model=Room)
def create_room(room: Room):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO Room (name, user_id) VALUES (?, ?) RETURNING *;",
        (room.name, room.user_id)
    ).fetchone()
    return Room(room_id=result[0], name=result[1], user_id=result[2])

@app.get("/rooms/", response_model=List[Room])
def read_rooms():
    conn = get_db()
    rows = conn.execute("SELECT * FROM Room").fetchall()
    return [Room(room_id=r[0], name=r[1], user_id=r[2]) for r in rows]

# ---------------------------- 设备 CRUD ----------------------------
@app.post("/devices/", response_model=Device)
def create_device(device: Device):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO Device (name, device_type, room_id) VALUES (?, ?, ?) RETURNING *;",
        (device.name, device.device_type, device.room_id)
    ).fetchone()
    return Device(device_id=result[0], name=result[1], device_type=result[2], room_id=result[3])

@app.get("/devices/", response_model=List[Device])
def read_devices():
    conn = get_db()
    rows = conn.execute("SELECT * FROM Device").fetchall()
    return [Device(device_id=r[0], name=r[1], device_type=r[2], room_id=r[3]) for r in rows]

# ---------------------------- 使用记录 CRUD ----------------------------
@app.post("/usages/", response_model=DeviceUsage)
def create_usage(usage: DeviceUsage):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO DeviceUsage (device_id, user_id, timestamp, duration) VALUES (?, ?, ?, ?) RETURNING *;",
        (usage.device_id, usage.user_id, usage.timestamp, usage.duration)
    ).fetchone()
    return DeviceUsage(
        usage_id=result[0], device_id=result[1], user_id=result[2], timestamp=result[3], duration=result[4]
    )

@app.get("/usages/", response_model=List[DeviceUsage])
def read_usages():
    conn = get_db()
    rows = conn.execute("SELECT * FROM DeviceUsage").fetchall()
    return [DeviceUsage(
        usage_id=r[0], device_id=r[1], user_id=r[2], timestamp=r[3], duration=r[4]
    ) for r in rows]

# ---------------------------- 安防事件 CRUD ----------------------------
@app.post("/security_events/", response_model=SecurityEvent)
def create_event(event: SecurityEvent):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO SecurityEvent (room_id, user_id, event_type, timestamp) VALUES (?, ?, ?, ?) RETURNING *;",
        (event.room_id, event.user_id, event.event_type, event.timestamp)
    ).fetchone()
    return SecurityEvent(
        event_id=result[0], room_id=result[1], user_id=result[2], event_type=result[3], timestamp=result[4]
    )

@app.get("/security_events/", response_model=List[SecurityEvent])
def read_events():
    conn = get_db()
    rows = conn.execute("SELECT * FROM SecurityEvent").fetchall()
    return [SecurityEvent(
        event_id=r[0], room_id=r[1], user_id=r[2], event_type=r[3], timestamp=r[4]
    ) for r in rows]

# ---------------------------- 用户反馈 CRUD ----------------------------
@app.post("/feedbacks/", response_model=Feedback)
def create_feedback(feedback: Feedback):
    conn = get_db()
    result = conn.execute(
        "INSERT INTO Feedback (user_id, device_id, comment, timestamp) VALUES (?, ?, ?, ?) RETURNING *;",
        (feedback.user_id, feedback.device_id, feedback.comment, feedback.timestamp)
    ).fetchone()
    return Feedback(
        feedback_id=result[0], user_id=result[1], device_id=result[2], comment=result[3], timestamp=result[4]
    )

@app.get("/feedbacks/", response_model=List[Feedback])
def read_feedbacks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM Feedback").fetchall()
    return [Feedback(
        feedback_id=r[0], user_id=r[1], device_id=r[2], comment=r[3], timestamp=r[4]
    ) for r in rows]










