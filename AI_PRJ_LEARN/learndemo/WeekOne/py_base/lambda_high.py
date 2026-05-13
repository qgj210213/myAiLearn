"""
高阶函数（Higher-Order Function, HOF）
    满足以下至少一条的函数即为高阶函数：
    1) 接收别的函数作为参数（例如 sorted 的 key、map/filter 的第一个参数）；
    2) 返回一个函数（例如工厂函数、偏应用）。

lambda（匿名函数）
    语法：lambda 参数: 表达式
    适合「极短、只做一件事」的可调用对象；复杂逻辑请用 def 具名函数，便于阅读与调试。

本文件用同一套高阶函数，分别演示「传入具名 def」与「传入 lambda」的差异与取舍。
"""

import io
import sys
from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


# --- 高阶函数 1：把「规则」交给调用方 ---
def map_with(items: Iterable[T], rule: Callable[[T], R]) -> List[R]:
    """
    对序列中每个元素应用 rule，返回新列表。
    rule 可以是具名函数，也可以是 lambda，只要「接受一个参数并返回一个值」即可。
    """
    return [rule(x) for x in items]


# --- 高阶函数 2：返回一个函数（闭包）---
def make_scaler(factor: float) -> Callable[[float], float]:
    """返回函数 g(x) = x * factor。调用方拿到的是「已经绑定了 factor 的新函数」。"""

    def scale(x: float) -> float:
        return x * factor

    return scale


def _configure_stdout_utf8() -> None:
    """避免 Windows 默认 cp932 控制台打印中文时报 UnicodeEncodeError。"""
    buf = getattr(sys.stdout, "buffer", None)
    if buf is None:
        return
    try:
        sys.stdout = io.TextIOWrapper(buf, encoding="utf-8", errors="replace", line_buffering=True)
    except (AttributeError, OSError, ValueError):
        pass


def main() -> None:
    nums = [1, 2, 3, 4, 5]

    print("=== 1. map_with: 具名函数 vs lambda ===\n")

    # 不使用 lambda：逻辑稍长或会复用时，用 def 更清晰，栈追踪里也有函数名
    def to_square(n: int) -> int:
        return n * n

    print("传入具名函数 to_square:", map_with(nums, to_square))

    # 使用 lambda：就地表达「对每个元素平方」，一眼能看出规则，无需单独起名
    print("传入 lambda x: x * x:  ", map_with(nums, lambda x: x * x))

    # 对比：把「加 10」写成具名函数 vs lambda，效果相同，取舍在可读性与复用
    def add_ten(n: int) -> int:
        return n + 10

    print("传入具名函数 add_ten: ", map_with(nums, add_ten))
    print("传入 lambda x: x + 10:", map_with(nums, lambda x: x + 10))

    print("\n--- 小结 ---")
    print("相同点：二者都是「可调用对象」，高阶函数不关心名字，只关心签名是否匹配。")
    print("不同点：lambda 适合单行、一次性；def 适合命名、复用、调试与写文档字符串。")

    print("\n=== 2. make_scaler: 返回函数的工厂 (高阶函数) ===\n")

    double = make_scaler(2.0)
    half = make_scaler(0.5)
    print("double(3) =", double(3))
    print("half(8)  =", half(8))

    # 若只想临时用一次，也可以不显式保存返回的函数，而用 lambda 包一层（示意）
    # 注意：这里演示的是「把 lambda 当作返回值」与上面「把 lambda 当参数」是两种常见用法
    immediate = (lambda f, x: f(x))(make_scaler(3.0), 4.0)
    print("一次性调用 (lambda 包一层):", immediate)

    print("\n=== 3. sorted 的 key: 库自带的高阶函数 ===\n")
    words = ["pear", "apple", "kiwi"]
    print("按长度排序（lambda）:", sorted(words, key=lambda w: len(w)))
    print("按字典序排序（默认）:", sorted(words))


if __name__ == "__main__":
    _configure_stdout_utf8()
    main()
