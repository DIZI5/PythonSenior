def max(num1, num2):
  if num1 > num2:
    num = num1
  else:
    num = num2
    
  print(num)
  return num

# ________________________________

def len(string):
    count = 0
    arr = string.split()
    for word in arr:
        count = count + 1
    return count
    
# ________________________________


def mean(num1, num2, num3):
    return int((num1 + num2 + num3) / 3)


# ________________________________

def monthByNum(num):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[num - 1]