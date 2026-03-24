import time

# 类装饰器：一个类装饰器是一个实现了 __call__ 方法的类，这个方法接受一个函数作为参数，并返回一个新的函数。
class Timer:
    def __init__(self, unit="seconds"):
        self.unit = unit  # 初始化装饰器，接受一个参数来指定时间单位

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()  # 记录开始时间
            result = func(*args, **kwargs)  # 执行被装饰的函数
            end = time.time()  # 记录结束时间
            elapsed_time = end - start  # 计算执行时间
            if self.unit == "milliseconds":
                elapsed_time *= 1000  # 转换为毫秒
            print(f"Function {func.__name__} executed in {elapsed_time:.4f} {self.unit}")  # 输出执行时间
            return result  # 返回被装饰函数的结果
        return wrapper

# 使用类装饰器装饰一个函数，指定时间单位为毫秒
@Timer(unit="milliseconds")
def power(a, b):
    time.sleep(1)  # 模拟一个耗时操作
    return a ** b

# 调用被装饰的函数
if __name__ == "__main__":
    print("Power of 2 to the 3:", power(2, 3))  # 调用被装饰的幂函数