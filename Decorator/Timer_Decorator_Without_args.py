import time

# 定义一个装饰器函数，用于计算函数的执行时间
def timer(func):
    def wapper(*args, **kwargs):
        start = time.time()  # 记录开始时间
        result = func(*args, **kwargs) # 执行被装饰的
        end = time.time()  # 记录结束时间
        print(f"Function {func.__name__} executed in {end - start:.4f} seconds")  # 输出执行时间
        return result  # 返回被装饰函数的结果
    return wapper

# 使用装饰器装饰一个函数 @ 语法糖
@timer
def product(a, b):
    time.sleep(1)  # 模拟一个耗时操作
    return a * b

# 手动使用装饰器装饰一个函数
def sum(a, b):
    time.sleep(0.5)  # 模拟一个耗时操作
    return a + b

sum = timer(sum)  # 手动把函数传给装饰器装饰

# 调用被装饰的函数
if __name__ == "__main__":
    print("Product of 3 and 5:", product(3, 5))  # 调用被装饰的乘法函数
    print("Sum of 3 and 5:", sum(3, 5))  # 调用被装饰的加法函数