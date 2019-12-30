import time

attempt = 3


# 请求重试装饰器
def request_retry():
    def decorator(func):
        def wrapper(*args, **kw):
            att = 0
            error = ''
            while att < attempt:
                try:
                    return func(*args, **kw)
                except Exception as e:
                    att += 1
                    error = e
            raise error

        return wrapper

    return decorator


# 统计程序耗时
def take_time():
    def decorator(func):
        def wrapper(*args, **kw):
            print('#' * 50)
            start_time = time.time()
            result = func(*args, **kw)
            end_time = time.time()
            print('程序总共耗时：%s' % (end_time - start_time))
            print('#' * 50)
            return result

        return wrapper

    return decorator
