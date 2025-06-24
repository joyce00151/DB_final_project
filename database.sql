-- 创建 Room 表
CREATE TABLE Room (
    id INTEGER PRIMARY KEY,
    address TEXT,
    area DOUBLE
);

-- 创建 User 表
CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    room_id INTEGER,
    FOREIGN KEY (room_id) REFERENCES Room(id)
);

-- 创建 Device 表
CREATE TABLE Device (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    room_id INTEGER,
    FOREIGN KEY (room_id) REFERENCES Room(id)
);

-- 创建 DeviceUsage 表
CREATE TABLE DeviceUsage (
    id INTEGER PRIMARY KEY,
    device_id INTEGER,
    user_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES Device(id),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

-- 创建 SecurityEvent 表
CREATE TABLE SecurityEvent (
    id INTEGER PRIMARY KEY,
    device_id INTEGER,
    timestamp TIMESTAMP,
    description TEXT,
    FOREIGN KEY (device_id) REFERENCES Device(id)
);

-- 创建 Feedback 表
CREATE TABLE Feedback (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    content TEXT,
    submitted_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

-- 创建 DeviceRelation 表
CREATE TABLE DeviceRelation (
    id INTEGER PRIMARY KEY,
    device1_id INTEGER,
    device2_id INTEGER,
    frequency INTEGER,
    FOREIGN KEY (device1_id) REFERENCES Device(id),
    FOREIGN KEY (device2_id) REFERENCES Device(id)
);
