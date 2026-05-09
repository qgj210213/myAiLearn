# 周3：深度学习基础（PyTorch 快速实践）

重点学习：神经网络基础、反向传播、PyTorch 张量/模型/训练循环、GPU 基本使用。

必学要点：
- 先建立深度学习训练的基本流程意识：数据进入模型、计算损失、反向传播、更新参数。
- 掌握 PyTorch 的核心使用方式：会写简单模型，会组织数据，会完成基础训练循环。
- 能处理训练中的常见问题：模型不收敛、loss 不下降、过拟合、学习率不合适。

必做小项目（3–7 天）：
- 无必做项目（专注 PyTorch 小模型练习）

工作要点：
- 能写出简单训练脚本并解释每步
- 熟悉 PyTorch 调试常见问题（梯度消失/爆炸）

## 周3 详细要学习内容（表格）

| 主题 | 详细要学习的内容 | 必须掌握 | 进阶 / 备注 |
|---|---|---:|---|
| 深度学习基础 | 神经网络、前向传播、损失函数、反向传播 | 能说清训练一轮模型发生了什么 | 数学推导不用一开始学太深 |
| Tensor 基础 | tensor 创建、shape、dtype、device、基础运算 | 能处理输入输出张量 | 广播机制可边用边学 |
| 数据加载 | Dataset、DataLoader、batch、shuffle | 能把数据封装为可训练输入 | 多进程加载属于进阶 |
| 模型定义 | nn.Module、Linear、Activation、Sequential | 能搭一个简单 MLP/CNN | 自定义复杂模块可后学 |
| 训练循环 | forward、loss.backward、optimizer.step、zero_grad | 能独立写训练与验证循环 | 混合精度训练是进阶 |
| 优化器与调参 | SGD、Adam、学习率、batch size、epoch | 知道哪些参数最影响训练结果 | scheduler 可进阶 |
| 保存与推理 | model.save/load、eval 模式、inference | 能保存模型并做预测 | TorchScript/ONNX 可进阶 |
| 调试与可复现 | 随机种子、日志、loss 曲线、过拟合小样本测试 | 能定位训练流程基本问题 | WandB/TensorBoard 可后补 |

---

## 每日/每项练习建议
- Day 1：熟悉 Tensor 基础操作，写几个 shape 变换练习。
- Day 2：用 Dataset 和 DataLoader 封装一个小数据集。
- Day 3：写一个最简单的分类模型并跑通训练循环。
- Day 4：尝试调整学习率、batch size，观察 loss 和效果变化。
- Day 5：补上模型保存、加载和推理代码，整理为完整训练脚本。

---

速学资源（选一）： PyTorch 教程、fast.ai 入门课程

小贴士：从小模型起步，先保证训练流程正确，再谈结构和调参。
