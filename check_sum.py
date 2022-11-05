def check_sum(*args):
    sum_num = sum(*args)
    if sum_num < 50:
        print("not enough")
    else:
        print("verification passed")


nums = list(map(int, input().split()))

check_sum(nums)