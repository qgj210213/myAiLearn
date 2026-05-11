# Python 推导式
# Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

# Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。

# 在使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性。

# Python 支持各种数据结构的推导式：

# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式
# 元组(tuple)推导式

# 列表推导式
# 列表推导式格式为：

# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list]

# 或者 

# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：

numbers = range(10)
# 基础推导式：生成平方数
squares = [x**2 for x in numbers]
# 带条件的推导式：仅偶数的平方
even_squares = [x**2 for x in numbers if x % 2 == 0]
# 嵌套推导式：矩阵展平
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(f"平方: {squares}")
print(f"偶数平方: {even_squares}")
print(f"矩阵展平: {flattened}")
# if __name__ == "__main__":
#     main()
    
