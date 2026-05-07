#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python 基础语法和数据结构示例
演示变量、控制结构、循环和常用数据结构的使用
"""


def demo_basic_syntax():
    """演示基础语法"""
    print("=== 1.1 基础语法 ===\n")
    
    # 变量定义与动态类型
    name = "Python学习"
    age = 2026 - 1991  # 表达式计算
    print(f"名称: {name}")
    print(f"年龄: {age}")
    
    # 控制结构
    if age > 30:
        status = "Mature"
    else:
        status = "Young"
    print(f"状态: {status}")
    
    # 循环语句
    print("\n循环演示:")
    for i in range(3):
        print(f"  循环第 {i+1} 次")


def demo_list():
    """演示列表操作"""
    print("\n=== List (列表): 有序可变 ===")
    
    my_list = [1, 2, 3]
    print(f"初始列表: {my_list}")
    
    my_list.append(4)       # 末尾添加
    print(f"添加4后: {my_list}")
    
    my_list[0] = 99         # 修改元素
    print(f"修改第一个元素: {my_list}")
    
    removed_val = my_list.pop() # 弹出末尾元素
    print(f"弹出元素 {removed_val} 后: {my_list}")


def demo_tuple():
    """演示元组操作"""
    print("\n=== Tuple (元组): 有序不可变 ===")
    
    my_tuple = (10, 20, 30)
    print(f"元组: {my_tuple}")
    
    # my_tuple[0] = 5  # 会报错，不可修改
    print("注意: 元组不可修改")
    
    x, y, z = my_tuple      # 解包
    print(f"解包后: x={x}, y={y}, z={z}")


def demo_set():
    """演示集合操作"""
    print("\n=== Set (集合): 无序不重复 ===")
    
    list_with_dup = [1, 1, 2, 3]
    print(f"原始列表(有重复): {list_with_dup}")
    
    my_set = set(list_with_dup)  # 结果 {1, 2, 3}
    print(f"转换为集合(去重): {my_set}")
    
    other_set = {2, 3, 4}
    print(f"另一个集合: {other_set}")
    print(f"交集: {my_set & other_set}")  # 交集: {2, 3}
    print(f"并集: {my_set | other_set}")
    print(f"差集: {my_set - other_set}")


def demo_dict():
    """演示字典操作"""
    print("\n=== Dict (字典): 键值对 ===")
    
    person = {"name": "Alice", "age": 25}
    print(f"初始字典: {person}")
    
    person["city"] = "New York"  # 增加键值对
    print(f"添加城市后: {person}")
    
    # 安全获取，不存在返回默认值
    job = person.get("job", "Unemployed")
    print(f"职业(使用默认值): {job}")
    
    # 遍历字典
    print("\n遍历字典:")
    for key, value in person.items():
        print(f"  {key}: {value}")


def main():
    """主函数 - 执行所有演示"""
    print("=" * 50)
    print("Python 基础语法和数据结构演示")
    print("=" * 50)
    
    demo_basic_syntax()
    demo_list()
    demo_tuple()
    demo_set()
    demo_dict()
    
    print("\n" + "=" * 50)
    print("演示完成!")
    print("=" * 50)


if __name__ == "__main__":
    main()