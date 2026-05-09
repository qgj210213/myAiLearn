# 周4：Transformer + prompt（Hugging Face 快速上手）

重点学习：Transformer 原理（注意力机制）、tokenization、使用 Hugging Face 加载模型与简单微调、prompt 设计基础。

必学要点：
- 先理解大模型应用最常用的几个环节：文本如何被切分、模型如何接收输入、输出为什么会变化。
- 会直接使用 Hugging Face 完成基础推理，知道模型、tokenizer、prompt 三者怎么配合。
- 掌握 prompt 的基本写法：任务描述清晰、输入输出格式明确、示例数量适中。

必做小项目（3–7 天）：
- 相关项目：RAG 问答系统、Multi-step Agent（详见 PROJECTS.md，关联周：Week4, Week5, Week7）

工作要点：
- 能解释 attention 的基本作用
- 熟悉 HF 推理代码与 prompt 示例

## 周4 详细要学习内容（表格）

| 主题 | 详细要学习的内容 | 必须掌握 | 进阶 / 备注 |
|---|---|---:|---|
| Transformer 基础 | self-attention、encoder/decoder、上下文建模 | 知道 Transformer 为什么适合文本任务 | 数学公式细节可后补 |
| Tokenizer | 分词、token id、padding、truncation、decode | 能正确处理输入文本和输出结果 | BPE/SentencePiece 原理可进阶 |
| Hugging Face 基础 | AutoTokenizer、AutoModel、pipeline、model config | 能快速加载模型并做推理 | model hub 管理可后补 |
| Prompt 工程 | 指令式 prompt、few-shot、格式约束、角色设定 | 能写出稳定、清晰、可复现的 prompt | prompt 自动优化属于进阶 |
| 推理实践 | 文本生成参数、temperature、top_p、max_tokens | 知道参数如何影响输出 | 采样策略深入可进阶 |
| 简单微调认知 | SFT、LoRA、PEFT 基础概念 | 知道什么时候该微调，什么时候直接 prompt 就够 | 真正训练可放后面 |
| 输出评估 | 准确性、稳定性、幻觉、格式一致性 | 能对大模型输出做简单判断 | 自动评测框架可后补 |

---

## 每日/每项练习建议
- Day 1：理解 tokenizer 和 token id，观察同一句话在不同模型下的切分结果。
- Day 2：用 Hugging Face 加载一个小模型，完成基础文本生成。
- Day 3：写 3 组不同 prompt，对比输出效果和稳定性。
- Day 4：尝试 few-shot prompt，观察示例数量对结果的影响。
- Day 5：整理一个固定输入/输出格式的推理脚本，方便后续接 RAG 或 Agent。

---

速学资源（选一）： Hugging Face 文档、CS224n 重要片段

小贴士：把 prompt 模板、参数设置和示例输入输出都写进 README。
