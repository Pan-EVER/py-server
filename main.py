from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()



app = FastAPI(docs_url=None)  # 禁用默认的 Swagger UI

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 自定义 Swagger UI 页面
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Docs",
        swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui/swagger-ui.css",
    )

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# 定义一个带参数的路由
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}