# 周7：Agent 核心（planner/tool/memory，做个多步 agent）

重点学习：Agent 架构（Planner/Executor/Tool/Memory）、多步决策流程、工具调用与权限限制、长期/短期记忆策略。

必学要点：
- 先把 Agent 理解成“会规划、会调用工具、会记住上下文的 AI 工作流”，不要一开始就把它想得太复杂。
- 掌握 Agent 的最小闭环：输入任务、规划步骤、调用工具、观察结果、继续执行。
- 建立安全和边界意识：工具能做什么、不能做什么，失败时怎么回退，结果怎么记录。

必做小项目（3–7 天）：
- 相关项目：Multi-step Agent（详见 PROJECTS.md，关联周：Week4, Week5, Week7）

工作要点：
- 能说明 agent 的安全控制与回退策略
- 能描述 memory 与 tool 的交互流程

## 周7 详细要学习内容（表格）

| 主题 | 详细要学习的内容 | 必须掌握 | 进阶 / 备注 |
|---|---|---:|---|
| Agent 基础概念 | Planner、Executor、Tool、Memory、Observation | 能讲清 Agent 和普通问答系统的区别 | 多 Agent 协作可进阶 |
| 执行流程 | 任务拆解、步骤执行、结果观察、循环终止条件 | 能设计一个多步流程 | 自适应规划属于进阶 |
| Tool 设计 | 搜索、计算器、数据库、外部 API 工具接入 | 能封装至少 2 类工具并调用 | 工具权限系统可进阶 |
| Memory 设计 | 短期上下文、长期记忆、RAG 结合方式 | 能说明什么时候读历史、什么时候查知识库 | 记忆压缩属于进阶 |
| Prompt 与控制 | planner prompt、tool use prompt、输出结构约束 | 能让 Agent 输出稳定步骤 | 自反思/self-reflection 可进阶 |
| 安全与回退 | 权限限制、超时控制、失败重试、人工接管 | 能设计基础安全边界 | 审计系统可进阶 |
| 日志与调试 | 记录每一步输入、决策、工具输出、最终结果 | 能复盘 Agent 为什么做错 | 可视化 trace 可后补 |

---

## 每日/每项练习建议
- Day 1：画出一个最小 Agent 流程图，明确 planner、tool、memory 的职责。
- Day 2：实现一个固定步骤的 deterministic agent。
- Day 3：接入 1 到 2 个工具，比如搜索或计算器。
- Day 4：加入短期记忆或 RAG 检索，让 Agent 能利用历史信息。
- Day 5：补上失败回退、日志记录和输出结构约束。

---

速学资源（选一）： LangChain 教程、Ray/Agent 案例

小贴士：先做稳定的单 Agent，再考虑更复杂的自动规划或多 Agent 协作。
