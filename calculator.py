def add(a, b):
    """返回两个数的和"""
    # 添加类型检查
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("两个参数都必须是数字")
    return a + b
