import os
if __name__=="_main_":
    print("This is a GitHub tutorial")
def is_prime(n):
    # Số nguyên tố phải lớn hơn 1
    if n <= 1:
        return False
    # 2 và 3 là số nguyên tố
    if n <= 3:
        return True
    # Loại bỏ các số chia hết cho 2 hoặc 3 để tăng tốc
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Kiểm tra các số từ 5 đến căn bậc hai của n
    # Các số nguyên tố (ngoại trừ 2, 3) luôn có dạng 6k ± 1
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

# Ví dụ sử dụng:
number = 17
if is_prime(number):
    print(f"{number} là số nguyên tố")
else:
    print(f"{number} không phải là số nguyên tố")

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # Chọn phần tử chốt
    left = [x for x in arr if x < pivot]   # Các số nhỏ hơn pivot
    middle = [x for x in arr if x == pivot] # Các số bằng pivot
    right = [x for x in arr if x > pivot]  # Các số lớn hơn pivot
    
    return sort_array(left) + middle + sort_array(right)

# Sử dụng
my_list = [64, 34, 25, 12, 22, 11, 90]
print(sort_array(my_list))