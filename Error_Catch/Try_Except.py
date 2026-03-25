# 除法函数，捕获除0错误以及类型错误
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return f"The result of {a} divided by {b} is: {result}"
    finally:
        print("Division operation attempted.")

# 测试除法函数
print(divide(10, 2))  # 正常除法
print(divide(10, 0))  # 除0错误
print(divide(10, "a"))  # 类型错误