# 这是一个有风格问题的Python文件
def   hello_world (  ) :   # 函数名和括号间有多余空格
  print( "Hello, World!" )  # 缩进不一致，且字符串括号内有空格

def calculate_sum (a,b): # 参数间缺少空格，函数名后有多余空格
    result = a+b # 运算符周围缺少空格
    # 下面是一个超长的行，肯定会触发flake8的line too long错误
    print(f"The sum of {a} and {b} is {result}. This is a very long line that definitely exceeds the 79 characters limit set by PEP8.")
    return result

if __name__ == "__main__"：
    hello_world()
    calculate_sum(1,2)
