# --- 2.1 函数定义与参数 ---

def calculate_area(width, height=10):
    """
    计算矩形面积
    :param width: 宽度 (必选参数)
    :param height: 高度 (默认参数)
    :return: 面积
    """
    return width * height


# --- 2.2 异常处理 ---
def safe_divide(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误: 除数不能为零")
    except TypeError:
        print("错误: 参数类型错误")
    else:
        print("计算成功，无异常")
    finally:
        print("运算结束清理工作")
    return result

# --- 2.3 Python lambda（匿名函数） ---
# lambda 语法格式：
#
# lambda arguments: expression
# lambda是 Python 的关键字，用于定义 lambda 函数。
# arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
# expression 是一个表达式，用于计算并返回函数的结果。

square = lambda x: x * x  # 定义一个匿名函数计算平方
height = lambda x: x+2  # 定义一个匿名函数计算高度


def main():
    """主函数"""
    # 调用 calculate_area
    area = calculate_area(5)
    print(f"矩形面积: {area}")
    
    print("\n--- 异常处理测试 ---")
    # 调用 safe_divide
    result = safe_divide(10, 0)
    print(f"结果: {result}")
    
    # 调用 lambda 函数
    print("\n--- Lambda 函数测试 ---")
    print(f"5 的平方: {square(5)}")
    print(f"高度增加 2 后: {height(5)}")


if __name__ == "__main__":
    main()
 

    