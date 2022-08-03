#printing the sum of five consecutive payments in a list
def largest_sum(payments):
    i = 0
    largest = payments[i] + payments[i + 1] + payments[i + 3] + payments[i + 4] + payments[i + 5]
    consecutive5 = f"{payments[i]} + {payments[i + 1]} + {payments[i + 2]} + {payments[i + 3]} + {payments[i + 4]}"
    n = len(payments)
    if n > 5:
        for i in range(n - 5):
            new_largest = payments[i + 1] + payments[i + 2] + payments[i + 3] + payments[i + 4] + payments[i + 5]
            if new_largest > largest:
                largest = new_largest
                consecutive5 = f"{payments[i + 1]} + {payments[i + 2]} + {payments[i + 3]} + {payments[i + 4]} + {payments[i + 5]}"
        print(consecutive5)
        print(largest)


payments = [1, 2, 3, 4, 75, 6, 7, 8, 9, 2]
print(largest_sum(payments))
