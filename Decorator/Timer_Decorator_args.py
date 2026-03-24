import time

# 装饰器工厂：一个带参数的装饰器需要一个外层函数来接受参数，并返回一个装饰器函数。
def timer(unit="seconds"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()  # 记录开始时间
            result = func(*args, **kwargs)  # 执行被装饰的函数
            end = time.time()  # 记录结束时间
            elapsed_time = end - start  # 计算执行时间
            if unit == "milliseconds":
                elapsed_time *= 1000  # 转换为毫秒
            print(f"Function {func.__name__} executed in {elapsed_time:.4f} {unit}")  # 输出执行时间
            return result  # 返回被装饰函数的结果
        return wrapper
    return decorator

# 使用装饰器工厂创建一个装饰器，指定时间单位为毫秒
@timer(unit="milliseconds")
def product(a, b):
    time.sleep(1)  # 模拟一个耗时操作
    return a * b

# 不指定时间单位，默认使用秒
@timer()
def divide(a, b):
    time.sleep(0.5)  # 模拟一个耗时操作
    return a / b

# 调用被装饰的函数
if __name__ == "__main__":
    print("Product of 3 and 5:", product(3, 5))  # 调用被装饰的乘法函数
    print("Division of 10 by 2:", divide(10, 2))  # 调用被装饰的除法函数