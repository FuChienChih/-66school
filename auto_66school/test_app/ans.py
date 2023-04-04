def sum_of_values():
    values = []
    sum_ = 0
    str_ = ""
    n = int(input("你將輸入n個正整數"))
    for i in range(n):
        value = int(input(f"第{i+1}個正整數"))
        sum_ += value
        values.append(value)
        str_ = str_ + str(value) + "+"
    print(str_[:-1] + "=" + str(sum(values)))
