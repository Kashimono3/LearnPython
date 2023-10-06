-- Tạo cơ sở dữ liệu
CREATE DATABASE QuanLyTruyXuat;
GO

-- Sử dụng cơ sở dữ liệu
USE QuanLyTruyXuat;
GO
CREATE TABLE users  (
    ID INT PRIMARY KEY,
    username NVARCHAR(255),
    password NVARCHAR(255),   
);
GO

INSERT INTO users (ID, username, password)
VALUES (1, 'admin', 'admin');



-- Tạo bảng "Loại cây"
CREATE TABLE Plants_and_Livestock (
     id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255),
    category NVARCHAR(255),
    planting_date DATE,
    location NVARCHAR(255),
	name_image NVARCHAR(255),
    image VARBINARY(MAX)
);
GO
select *from Plants_and_Livestock
DROP TABLE Plants_and_Livestock

