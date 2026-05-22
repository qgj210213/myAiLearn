# learndemo WeekOne 学习总结

---

## 1. `venv` 和依赖安装

`venv` 的作用是给每个项目单独隔离 Python 环境，避免不同项目的包版本冲突。

```powershell
# 进入项目目录
cd d:\qgjWork\rakuten\copilotWork\AiWork\myAiLearn\AI_PRJ_LEARN

# 创建虚拟环境
py -3 -m venv .venv

# 激活虚拟环境
.\.venv\Scripts\Activate.ps1

# 升级 pip
python -m pip install -U pip

# 安装依赖
pip install -r requirements.txt
```

---

## 2. `requirements.txt` 的作用

它是**依赖清单**，记录项目需要安装哪些第三方包和版本。

常见内容：

```txt
fastapi==0.115.0
uvicorn==0.30.6
requests==2.32.3
pytest==8.3.2
```

作用：
- 让别人一键复现环境
- 方便部署和 CI 安装
- 防止"我电脑能跑，你电脑不能跑"

安装方式：

```powershell
pip install -r requirements.txt
```

---

## 3. GET / POST 和常见状态码

### GET
- 用来**获取数据**
- 参数常放在 URL 里

```
GET /users?id=1
```

### POST
- 用来**提交数据**
- 常用于新增、登录、提交表单

```
POST /users
{
  "name": "Tom",
  "age": 18
}
```

### 常见状态码

| 状态码 | 含义 | 场景 |
|---|---|---|
| 200 | 成功 | 请求正常返回 |
| 201 | 已创建 | 新增数据成功 |
| 400 | 请求错误 | 参数不合法 |
| 401 | 未认证 | 没登录 |
| 403 | 无权限 | 有身份但没权限 |
| 404 | 未找到 | 路由或资源不存在 |
| 500 | 服务器错误 | 后端异常 |

---

## 4. `requests` 调用接口

```python
import requests

# GET
resp = requests.get("https://api.example.com/users", params={"id": 1})
print(resp.status_code)
print(resp.json())

# POST
data = {"name": "Tom", "age": 18}
resp = requests.post("https://api.example.com/users", json=data)
print(resp.status_code)
print(resp.json())
```

常用点：
- `params=`：拼到 URL 上
- `json=`：自动按 JSON 发送请求体
- `resp.json()`：把响应内容转成 Python 对象

---

## 5. 解析和构造 JSON 数据

### JSON → Python

```python
import json

text = '{"name": "Tom", "age": 18}'
obj = json.loads(text)
print(obj["name"])
```

### Python → JSON

```python
import json

data = {"name": "Tom", "age": 18}
text = json.dumps(data, ensure_ascii=False, indent=2)
print(text)
```

### 文件读写 JSON

```python
import json

data = {"name": "Tom"}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
```

---

## 6. 用 FastAPI 或 Flask 写简单接口

### FastAPI 示例

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.post("/echo")
def echo(data: dict):
    return {"you_send": data}
```

启动：

```powershell
uvicorn main:app --reload
```

### Flask 示例

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/hello")
def hello():
    return jsonify({"message": "hello"})

@app.post("/echo")
def echo():
    data = request.get_json()
    return jsonify({"you_send": data})
```

---

## 7. 基础测试和日志

### 测试

用 `pytest` 做最基础的单元测试：

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
```

运行：

```powershell
pytest
```

### 日志

比 `print()` 更适合正式项目：

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("service started")
logger.error("something went wrong")
```

---

## 8. README 中写清运行步骤

README 至少要写清：

1. 环境要求
2. 创建虚拟环境
3. 安装依赖
4. 启动服务
5. 如何测试接口

示例：

```md
## Run

1. 创建虚拟环境
   py -3 -m venv .venv

2. 激活环境
   .\.venv\Scripts\Activate.ps1

3. 安装依赖
   pip install -r requirements.txt

4. 启动服务
   uvicorn main:app --reload
```

---

## 9. 一句话总结

WeekOne 的核心就是：**会搭环境、会装依赖、会调接口、会处理 JSON、会写简单 API、会做基础测试和日志，并且能把运行方式写清楚。**
