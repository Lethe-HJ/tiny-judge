import time
import traceback

def time_calc(func):
    def run(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost = (end - start)
        # print(f"all tests cost {cost}s")
        return cost
    return run


class Judge:
    
    __instance = None  #　单例模式的单例识别

    def __new__(cls, test_li, times_a=1000, times_b=10, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, test_li, times_a=1000, times_b=10):
        self.test_li = test_li
        self.times_a = times_a
        self.times_b = times_b
        self.time_li = []  
        print(f"times_a:{self.times_a} times_b:{self.times_b}")
        print("name       status  avg    min    max")
    
    def __call__(self, f, name):
        # self.time_cacul(self.test)
        try:
            for _ in range(self.times_b):
                self.time_li.append(self.test(self.times_a, f))
        except AssertionError as e:
            print(e.args[0])
            return False
        max_time = "{:0>5.2f}".format(max(self.time_li) * 100)
        min_time = "{:0>5.2f}".format(min(self.time_li) * 100)
        avg_time = "{:0>5.2f}".format(sum(self.time_li)/len(self.time_li) * 100)
        print(f"{name}  sucess  {avg_time}  {min_time}  {max_time}")


    @time_calc
    def test(self, times, f):
        for (inputs,outs) in self.test_li:
            try:
                answer = f(inputs)
                assert answer == outs
                for _ in range(times):
                    f(inputs)
            except AssertionError:
                raise AssertionError(f"Failure, Input is {inputs}, your answer is {answer},but {outs} expected")
            except Exception:
                traceback.print_exc()
                return False
        return True
    
    