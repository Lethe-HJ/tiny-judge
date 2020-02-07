from judge.judge import Judge 

class Solution:
    __name__ = "Solution"

    def __call__(self):
        return self.decompressRLElist
        
    def decompressRLElist(self, nums):
        pass

class Solution1(Solution):
    '''
    ִ����ʱ :112 ms, ������ Python3 �ύ�л�����8.20%���û�
    �ڴ����� :13.3 MB, ������ Python3 �ύ�л�����100.00%���û�

    ���� �½��б�������, �б�ϲ�Ч�ʵ�
    '''
    __name__ = "Solution1"

    def decompressRLElist(self, nums):
        out = []
        if nums == []:
            return out
        for i in range(len(nums)):    
            num = nums[i]
            if i%2==0:
                freq = num
            else:
                out.extend([num]*freq)
        return out

class Solution2((Solution)):
    '''
    ִ����ʱ :76 ms, ������ Python3 �ύ�л�����37.27%���û�
    �ڴ����� :13.3 MB, ������ Python3 �ύ�л�����100.00%���û�
    '''
    __name__ = "Solution2"

    def decompressRLElist(self, nums):
        out = []
        if nums == []:
            return out
        for i in range(len(nums)):    
            num = nums[i]
            if i%2==0:
                freq = num
            else:
                while freq:
                    out.append(num)
                    freq = freq - 1
        return out


class Solution3((Solution)):
    '''
    ִ����ʱ :72 ms, ������ Python3 �ύ�л�����57.39%���û�
    �ڴ����� :13.4 MB, ������ Python3 �ύ�л�����100.00%���û�
    '''
    __name__ = "Solution3"

    def decompressRLElist(self, nums):
            max_index = len(nums) - 1
            out = []
            i = 0
            while i <= max_index:
                first = nums[i]
                second = nums[i+1]
                while first:
                    out.append(second)
                    first = first - 1
                i = i + 2
            return out

class Solution4((Solution)):
    '''
    ִ����ʱ :68 ms, ������ Python3 �ύ�л�����71.30%���û�
    �ڴ����� :13.3 MB, ������ Python3 �ύ�л�����100.00%���û�
    '''
    
    __name__ = "Solution4"
    
    def decompressRLElist(self, nums):
        out = []
        for i in range(0, len(nums), 2):    
            first = nums[i]
            second = nums[i+1]
            while first:
                out.append(second)
                first = first - 1
        return out


class Solution5((Solution)):
    '''
    ִ����ʱ :60 ms, ������ Python3 �ύ�л�����83.73%���û�
    �ڴ����� :13.4 MB, ������ Python3 �ύ�л�����100.00%���û�
    '''
    __name__ = "Solution5"

    def decompressRLElist(self, nums):
        out = []
        nums = nums.__iter__()
        nums_len = nums.__length_hint__()
        while nums_len:
            first = nums.__next__()
            second = nums.__next__()
            while first:
                out.append(second)
                first = first - 1
            nums_len = nums_len - 2
        return out


class Solution6(Solution):
    
    __name__ = "Solution6"

    def decompressRLElist(self, nums):
        out = []
        nums = nums.__iter__()
        for _ in range(0, nums.__length_hint__(), 2):
            first = nums.__next__()
            second = nums.__next__()
            while first:
                out.append(second)
                first = first - 1
        return out

test_li = [
    
    ([1,2,3,4], [2,4,4,4]),
    ([1,2,1000,4], [2]),
]

[test_li[1][1].append(4) for i in range(1000)]

object_li = [Solution1, Solution2, Solution3, Solution4, Solution5, Solution6]

the_judge = Judge(test_li, times_b=20)
[the_judge(object_i()(), object_i.__name__) for object_i in object_li]