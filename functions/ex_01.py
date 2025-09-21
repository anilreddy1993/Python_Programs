
# def test(a,b,*ag,**agw):
#     print(a,b,ag)



# test(1,2,g=22,h =44)


# def test(a, b, *ag,t=6,y, **agw):
#     print("a:", a)
#     print("b:", b)
#     print("ag (extra positional):", ag)
#     print("agw (extra keyword):", agw)

# test(1, 2, 3, 4, g=22, h=44)


# r = range(5)
# print(r)


# we have o find maximun of number in 3 numbers

# def mx(a,b,c,/):
#     r = max(a,b,c)
#     return r

# print(mx(12,144,33))


# calsculate the sipmle interest s = ptr/100 p is prinicial amount which we tooh t means time period how many years and ra maens rate of interest


# def sim(*,p,t,r):
#     s = (p*t*r)/100
#     return s

# print(sim(p = 30000,t = 5,r = 7.4))

# filter unique number in list


# def un(*args):
#     r = set(args)
#     l = sorted(r)
#     return l

# print(un(1,4,5,6,7,8,6,5,4,55,77,88,55))


# return function

# def outer():
#     def inner(n):
#         print(f'welcome {n}')

#     return inner

# f = outer()
# f("kennedy")
#-----------------------Closure function-----------------------------------------
# def get_counter():
#     ''' closure function contains nested function,
#     return function,
#     inner function can access the variables of outer function
#     '''
#     count = 0
#     def counter():
#         nonlocal count
#         count+=1
#         return count
#     return counter


# f = get_counter()
# print(f(),f(),f(),f())


'''
#-------------------------decorator-----------------------
#ex:1
def decorator(func):
    def wrapper():
        print("Before the function runs")
        func()  # call the original function
        print("After the function runs")
    return wrapper

def say_hello():
    print("Hello!")

# Apply decorator manually
decorated = decorator(say_hello)
decorated()

#ex:02
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

#ex:03  (When Python sees @decorator, it does:

#say_hello = decorator(say_hello))

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 5))


#real world ex
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(x, y):
    return x * y

print(multiply(4, 3))


#ex 05
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            print("Access denied!")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    print(f"Welcome {user['name']}!")

user1 = {"name": "Kishore", "logged_in": True}
user2 = {"name": "Raj", "logged_in": False}

view_profile(user1)  # ✅ allowed
view_profile(user2)  # ❌ denied


# ex :06
def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                print("Function call limit reached!")
                return None
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(max_calls=2)
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()  # blocked

#--------------------------------------------
import time

def delay(seconds=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds} second(s) before running {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(seconds=2)
def greet(name):
    print(f"Hello, {name}!")

greet("Kishore")
#--------------------------
# ------------------
import time

def retry(times=3):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(1)
            print("All attempts failed.")
        return wrapper
    return actual_decorator

@retry(times=3)
def risky_division(x, y):
    return x / y

print(risky_division(10, 2))  # works
print(risky_division(10, 0))  # will retry 3 times


def test(fun):
    def tester():
        print('-'*20)
        fun()
        print('-'*20)
    return tester

@test
def wish():
    print('Welcome')

# w = test(wish)
# print(w())

wish()

'''
#--------------------------lambda functions------------------------------





