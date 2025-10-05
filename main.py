def bad_function(param1, param2):
    """函数有很多空格问题"""
    x = param1 + param2
    y = x * 2
    print(f"Result: {y}")
    return y


class BadClass:
    def __init__(self, name):
        self.name = name

    def method_with_issues(self, value):
        if value > 10:
            print("Value is large")
        elif value < 0:
            print("Value is negative")
        # 一个超长的行被合理拆分
        result = (
            value
            * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679  # noqa: E501
        )
        return result


def another_bad_function():
    list1 = [1, 2, 3, 4, 5]
    for i in list1:
        if i % 2 == 0:
            print(i)

    # 缺少空行
    def inner_function():
        pass

    return inner_function


# 运算符周围空格问题
a = 1 + 2
b = a * 3
c = b / 4

# 导入后应该有两个空行但这里只有一个


def trailing_whitespace():
    return "这行末尾有空格"


if __name__ == "__main__":
    obj = BadClass("test")
    obj.method_with_issues(15)
    bad_function(1, 2)
    another_bad_function()
    print("Done")
