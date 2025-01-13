目录结构说明
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
```