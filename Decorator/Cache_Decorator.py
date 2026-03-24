# cache_decorator
def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            print(f"Cache hit for arguments {args}")
            return cached_results[args]
        else:
            print(f"Cache miss for arguments {args}")
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper

# 使用装饰器装饰一个函数
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 调用被装饰的函数
if __name__ == "__main__":
    print("Fibonacci of 10:", fibonacci(10))  # 第一次计算，缓存未命中
    print("Fibonacci of 10 again:", fibonacci(10))  # 第二次计算，缓存命中
    print("Fibonacci of 9:", fibonacci(9))  # 第一次计算，缓存未命中
    print("Fibonacci of 9 again:", fibonacci(9))  # 第二次计算，缓存命中