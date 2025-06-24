-- 房间
INSERT INTO Room VALUES (1, '123 Smart Ave', 85.0);
INSERT INTO Room VALUES (2, '456 AI Blvd', 95.5);
INSERT INTO Room VALUES (3, '789 IoT Street', 60.0);
INSERT INTO Room VALUES (4, '101 Tech Park', 120.0);
INSERT INTO Room VALUES (5, '202 Future Lane', 75.0);
INSERT INTO Room VALUES (6, '303 Innovation Dr', 88.0);

-- 用户
INSERT INTO User VALUES (1, 'Alice', 'alice@example.com', '123456789', 1);
INSERT INTO User VALUES (2, 'Bob', 'bob@example.com', '987654321', 2);
INSERT INTO User VALUES (3, 'Charlie', 'charlie@example.com', '555555555', 3);
INSERT INTO User VALUES (4, 'Diana', 'diana@example.com', '666666666', 2);
INSERT INTO User VALUES (5, 'Eve', 'eve@example.com', '777777777', 4);
INSERT INTO User VALUES (6, 'Frank', 'frank@example.com', '888888888', 5);
INSERT INTO User VALUES (7, 'Grace', 'grace@example.com', '999999999', 6);
INSERT INTO User VALUES (8, 'Henry', 'henry@example.com', '111111111', 4);
INSERT INTO User VALUES (9, 'Ivy', 'ivy@example.com', '222222222', 5);
INSERT INTO User VALUES (10, 'Jack', 'jack@example.com', '333333333', 6);

-- 设备
INSERT INTO Device VALUES (1, 'Smart Light', 'Lighting', 1);
INSERT INTO Device VALUES (2, 'Smart Lock', 'Security', 1);
INSERT INTO Device VALUES (3, 'Smart TV', 'Entertainment', 2);
INSERT INTO Device VALUES (4, 'Smart AC', 'HVAC', 3);
INSERT INTO Device VALUES (5, 'Smart Speaker', 'Entertainment', 2);
INSERT INTO Device VALUES (6, 'Smart Refrigerator', 'Appliance', 4);
INSERT INTO Device VALUES (7, 'Smart Oven', 'Appliance', 4);
INSERT INTO Device VALUES (8, 'Smart Curtains', 'Lighting', 5);
INSERT INTO Device VALUES (9, 'Smart Heater', 'HVAC', 6);
INSERT INTO Device VALUES (10, 'Smart Vacuum', 'Cleaning', 5);

-- 使用记录
INSERT INTO DeviceUsage VALUES (1, 1, 1, '2025-06-01 08:00:00', '2025-06-01 10:00:00');
INSERT INTO DeviceUsage VALUES (2, 3, 2, '2025-06-01 19:00:00', '2025-06-01 20:30:00');
INSERT INTO DeviceUsage VALUES (3, 2, 1, '2025-06-02 10:00:00', '2025-06-02 11:00:00');
INSERT INTO DeviceUsage VALUES (4, 5, 4, '2025-06-02 14:00:00', '2025-06-02 18:00:00');
INSERT INTO DeviceUsage VALUES (5, 4, 3, '2025-06-03 13:00:00', '2025-06-03 15:30:00');
INSERT INTO DeviceUsage VALUES (6, 1, 4, '2025-06-04 07:00:00', '2025-06-04 09:00:00');
INSERT INTO DeviceUsage VALUES (7, 3, 2, '2025-06-04 19:00:00', '2025-06-04 21:00:00');
INSERT INTO DeviceUsage VALUES (8, 6, 5, '2025-06-05 09:00:00', '2025-06-05 09:30:00');
INSERT INTO DeviceUsage VALUES (9, 7, 5, '2025-06-05 18:00:00', '2025-06-05 19:00:00');
INSERT INTO DeviceUsage VALUES (10, 8, 6, '2025-06-06 07:00:00', '2025-06-06 08:30:00');
INSERT INTO DeviceUsage VALUES (11, 9, 7, '2025-06-06 20:00:00', '2025-06-06 22:00:00');
INSERT INTO DeviceUsage VALUES (12, 10, 6, '2025-06-07 14:00:00', '2025-06-07 15:00:00');
INSERT INTO DeviceUsage VALUES (13, 1, 8, '2025-06-07 06:00:00', '2025-06-07 07:30:00');
INSERT INTO DeviceUsage VALUES (14, 3, 9, '2025-06-07 19:00:00', '2025-06-07 21:00:00');
INSERT INTO DeviceUsage VALUES (15, 2, 10, '2025-06-08 01:00:00', '2025-06-08 02:00:00');
INSERT INTO DeviceUsage VALUES (16, 5, 8, '2025-06-08 15:00:00', '2025-06-08 17:00:00');
INSERT INTO DeviceUsage VALUES (17, 9, 7, '2025-06-09 06:30:00', '2025-06-09 08:00:00');
INSERT INTO DeviceUsage VALUES (18, 4, 10, '2025-06-09 21:00:00', '2025-06-09 22:30:00');
INSERT INTO DeviceUsage VALUES (19, 7, 5, '2025-06-10 18:00:00', '2025-06-10 19:30:00');

-- 安防事件
INSERT INTO SecurityEvent VALUES (1, 2, '2025-06-02 01:23:00', 'Unauthorized entry detected');
INSERT INTO SecurityEvent VALUES (2, 2, '2025-06-04 03:45:00', 'Door left open too long');
INSERT INTO SecurityEvent VALUES (3, 2, '2025-06-05 02:00:00', 'Multiple failed unlock attempts');
INSERT INTO SecurityEvent VALUES (4, 2, '2025-06-06 02:30:00', 'Suspicious motion detected');
INSERT INTO SecurityEvent VALUES (5, 10, '2025-06-07 04:00:00', 'Device offline alert');
INSERT INTO SecurityEvent VALUES (6, 2, '2025-06-08 01:15:00', 'Multiple failed unlock attempts');
INSERT INTO SecurityEvent VALUES (7, 9, '2025-06-09 23:45:00', 'Heater malfunction detected');

-- 用户反馈
INSERT INTO Feedback VALUES (1, 1, 'TV not working properly.', '2025-06-03 15:00:00');
INSERT INTO Feedback VALUES (2, 2, 'Door lock delayed response.', '2025-06-03 16:45:00');
INSERT INTO Feedback VALUES (3, 3, 'Air conditioner too loud.', '2025-06-04 10:30:00');
INSERT INTO Feedback VALUES (4, 4, 'Speaker volume fluctuates.', '2025-06-04 20:00:00');
INSERT INTO Feedback VALUES (5, 5, 'Refrigerator temperature too high.', '2025-06-06 10:00:00');
INSERT INTO Feedback VALUES (6, 6, 'Oven preheat taking too long.', '2025-06-06 20:30:00');
INSERT INTO Feedback VALUES (7, 7, 'Curtains open too slowly.', '2025-06-07 08:15:00');
INSERT INTO Feedback VALUES (8, 8, 'Heater making noise.', '2025-06-09 22:00:00');
INSERT INTO Feedback VALUES (9, 9, 'Vacuum missed spots.', '2025-06-10 16:00:00');
INSERT INTO Feedback VALUES (10, 10, 'Lock occasionally unresponsive.', '2025-06-10 18:30:00');

-- 设备关系
INSERT INTO DeviceRelation VALUES (1, 1, 2, 5);
INSERT INTO DeviceRelation VALUES (2, 2, 3, 2);
INSERT INTO DeviceRelation VALUES (3, 3, 5, 3);
INSERT INTO DeviceRelation VALUES (4, 1, 5, 1);
INSERT INTO DeviceRelation VALUES (5, 6, 7, 4);
INSERT INTO DeviceRelation VALUES (6, 8, 10, 3);
INSERT INTO DeviceRelation VALUES (7, 9, 4, 2);
INSERT INTO DeviceRelation VALUES (8, 5, 1, 2);
INSERT INTO DeviceRelation VALUES (9, 3, 10, 1);
INSERT INTO DeviceRelation VALUES (10, 7, 2, 3);




