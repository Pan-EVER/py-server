## 目录结构说明
```
fastapi_project/
├── app/                      # 主应用代码
│   ├── __init__.py           # 初始化文件
│   ├── main.py               # FastAPI 应用入口
│   ├── api/                  # API 路由
│   │   ├── __init__.py
│   │   ├── v1/               # API 版本 1
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/    # 各个端点的路由
│   │   │   │   ├── items.py
│   │   │   │   ├── users.py
│   │   │   └── routers.py    # 路由聚合
│   ├── core/                 # 核心配置和工具
│   │   ├── __init__.py
│   │   ├── config.py         # 配置文件
│   │   ├── security.py       # 认证和授权
│   │   └── utils.py          # 工具函数
│   ├── models/               # 数据模型
│   │   ├── __init__.py
│   │   ├── item.py           # 项目模型
│   │   └── user.py           # 用户模型
│   ├── schemas/              # Pydantic 模型（请求/响应模型）
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   ├── services/             # 业务逻辑
│   │   ├── __init__.py
│   │   ├── item_service.py
│   │   └── user_service.py
│   ├── db/                   # 数据库相关
│   │   ├── __init__.py
│   │   ├── base.py           # 数据库基类
│   │   ├── session.py        # 数据库会话
│   │   └── repositories/     # 数据库操作
│   │       ├── __init__.py
│   │       ├── item_repo.py
│   │       └── user_repo.py
│   └── tests/                # 单元测试
│       ├── __init__.py
│       ├── test_items.py
│       └── test_users.py
├── requirements.txt          # 项目依赖
├── .env                      # 环境变量
├── .gitignore                # Git 忽略文件
├── README.md                 # 项目说明
└── run.py                    # 启动脚本

## Features

- RESTful API endpoints for CRUD operations
- MySQL database integration using SQLAlchemy ORM
- Pydantic data validation
- Environment variables configuration
- Automatic API documentation
- Modular project structure

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create `.env` file with your database credentials:
   ```env
   DATABASE_URL=mysql+pymysql://user:password@localhost:3306/dbname
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

### Users API Endpoints

- `POST /users/` - Create new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user
```
