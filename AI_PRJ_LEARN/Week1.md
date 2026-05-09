# 周1：Python + Git（工程习惯、HTTP/JSON）

重点学习：Python 基础语法、数据结构、虚拟环境、pip、Git 基本操作、HTTP/JSON、Flask/FastAPI 快速入门。

必学要点：
- 先打牢 Python 开发基础：能独立写脚本，完成文件处理、JSON 解析、异常处理和基础面向对象开发。
- 掌握最基本的工程协作能力：会搭建虚拟环境、管理依赖、使用 Git 完成分支开发与代码提交。
- 建立接口与服务意识：理解 HTTP/JSON，能调用 API，也能用 FastAPI 或 Flask 封装一个简单服务。
- 养成工程习惯：会调试、会写基础测试、能写清 README 和项目运行说明。

必做小项目（3–7 天）：
- 相关项目：部署演示（详见 PROJECTS.md，关联：Week1, Week6, Week8）

工作要点：
- 能说明为何选择 FastAPI/Flask 和如何在工程中处理错误与异常
- 熟悉 requests、Git 操作流程，并能写出可复现的部署步骤
- 能展示项目架构、日志/监控设计与故障排查思路

## 周1 详细要学习内容（表格）

| 主题 | 详细要学习的内容 | 必须掌握 | 进阶 / 备注 |
|---|---|---:|---|
| Python 基础 | 语法、数据结构（list/dict/set/tuple）、函数、类、列表推导、上下文管理器 | 能用 Python 写清晰脚本、理解迭代器/生成器、异常处理 | 类型提示 (typing)、async/await（进阶） |
| 开发环境 | venv/virtualenv、pip、requirements.txt、依赖安装与管理 | 能创建虚拟环境并复现依赖安装流程 | poetry / conda（进阶） |
| Git & GitHub | commit、branch、merge、PR、解决冲突、基本 GitHub 流程 | 能完成分支开发、发起并处理 PR、写良好 commit message | rebase、CI 集成（进阶） |
| HTTP/JSON & API | REST 概念、HTTP 方法/状态码、JSON 编解码、requests 使用 | 能调用第三方 API、解析 JSON、处理错误 | 异步请求 aiohttp、GraphQL（进阶） |
| Web 框架基础 | Flask 或 FastAPI：路由、请求参数、返回 JSON、简单部署 | 能把脚本封装成可被调用的 HTTP 服务 | FastAPI 的依赖注入、类型声明、uvicorn 部署（进阶） |
| 调试与测试 | logging、pdb、pytest 基本用法、断言、测试组织 | 能写单元测试并运行、能定位常见错误 | Mock、集成测试、测试覆盖率（进阶） |
| 编码规范 & 工程习惯 | black/flake8、README、文档、注释、代码结构 | 保持可读代码、写运行说明与演示步骤 | pre-commit、CI lint 检查（进阶） |
| 工具链 | VSCode 使用、命令行基础、Docker 入门（Dockerfile） | 能用 IDE 调试、构建并运行 Docker 镜像 | docker-compose、Kubernetes 概念（进阶） |

---

## 每日/每项练习建议
- Day 1–2: Python 小脚本练习（文件处理、JSON 处理、HTTP 请求）
- Day 3–4: 用 Flask/FastAPI 写一个简单的“健康检查 + echo API”并容器化
- Day 5: 用 Git 完成分支合并与 PR 流程，把代码推到 GitHub 并写好 README
- 持续：把练习放到一个 repo，写清复现步骤，录一段 2 分钟 Demo

---

小贴士：项目要能 demo（README + POST 请求），代码放 GitHub 并写清复现步骤。
