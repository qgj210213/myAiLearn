from pathlib import Path
import datetime

OUT = Path(__file__).parent / 'AUTO_DOC.md'

content = f"""# 自动生成：requirements.txt 与生成 Markdown 方法（简要）

生成时间：{datetime.datetime.now().isoformat()}

## requirements.txt 的作用

- 列出项目依赖，便于通过 `pip install -r requirements.txt` 还原环境。
- 通过 `pip freeze > requirements.txt` 导出当前环境依赖（建议在虚拟环境中运行）。

## 在 `py_env` 目录生成 Markdown 的示例方法

1. 手动创建 `*.md` 文件
2. 使用脚本（本脚本即为示例）
3. Jupyter nbconvert： `jupyter nbconvert --to markdown notebook.ipynb --output-dir=py_env`
4. Pandoc： `pandoc input.docx -t markdown -o py_env/from_docx.md`
5. 使用模板引擎（Jinja2）渲染

此文件由 `gen_md.py` 自动生成。
"""

OUT.write_text(content, encoding='utf-8')
print(f'生成: {OUT}')

