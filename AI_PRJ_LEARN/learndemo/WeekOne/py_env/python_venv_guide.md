# Python `venv` 使用指南

## 一、在 Windows（PowerShell）中如何创建 `venv` 并安装依赖

### 1) 进入项目目录

```powershell
cd d:\qgjWork\rakuten\copilotWork\AiWork\myAiLearn\AI_PRJ_LEARN
```

### 2) 创建虚拟环境（建议放项目根目录）

```powershell
py -3 -m venv .venv
```

### 3) 激活虚拟环境

```powershell
.\.venv\Scripts\Activate.ps1
```

如果提示脚本被禁止执行（ExecutionPolicy），在**当前窗口临时放开**：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4) 升级 `pip`（推荐）

```powershell
python -m pip install -U pip
```

### 5) 安装依赖

如果项目有 `requirements.txt`：

```powershell
pip install -r requirements.txt
```

如果没有 `requirements.txt`，按需安装包：

```powershell
pip install <package-name>
```

### 6) 验证是否在虚拟环境中

```powershell
python -c "import sys; print(sys.executable)"
```

输出路径中包含 `.venv` 即表示生效。

### 7) 退出虚拟环境

```powershell
deactivate
```

---

## 二、这些操作一般用在哪些地方

1. **项目开发与学习**  
   每个 Python 项目依赖不同，用 `venv` 可以让项目之间互不影响。

2. **避免污染系统环境**  
   不把依赖装到全局 Python，降低环境冲突风险。

3. **团队协作与可复现**  
   通过 `requirements.txt` 或 `pyproject.toml`，新环境可快速复现依赖。

4. **多 Python 版本并存**  
   不同项目可以使用不同解释器版本。

5. **CI/CD 与部署场景**  
   常见流程就是：创建环境 -> 安装依赖 -> 测试/运行。

6. **使用第三方库时**  
   一旦项目需要第三方包，建议默认使用 `venv`。

---

## 三、简短建议

- 学习脚本若只用标准库，可不强制使用 `venv`。  
- 只要涉及第三方依赖，建议始终先建 `.venv`。  
- 仓库建议固定一个依赖文件（如 `requirements.txt`）方便协作。
