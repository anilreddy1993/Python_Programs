# coursera practice questions

# number = 5 # Initialize the variable
# while number<=16 # Complete the while loop condition
#     print(number, end=" ")
#     number+=5
#     break # Increment the variable

# # Should print 15 10 5 

# number = 15  # Start from 15
# while number >= 5:  # Continue until we reach 5
#     print(number, end=" ")
#     number -= 5


# def count_numbers(first, last):
#   # Loop through the numbers from first to last 
#   x = first
#   while x <= last:
#     print(x)

# for outer_loop in range(2, 6+1):
#     for inner_loop in range(outer_loop):
#         if inner_loop % 2 == 0:
#             print(inner_loop)

# for sum in range(5):
#     sum += sum
#     print(sum)


def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for i in range(1,maximum+1,2): 
        # if i %3 ==0:

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
           return_string +=str(i)+" "

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(___): 
         # Complete the inner loop range
        for y in range(___):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)


def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            ___ # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            ___ # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:  # Count down while start is >= stop
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1  # Decrement start
    else:
        return_string = "Counting up: "
        while start <= stop:  # Count up while start is <= stop
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1  # Increment start
    return return_string


# Test cases
print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))   # Should be "Counting down: 2,1"
print(counter(5, 5))   # Should be "Counting up: 5"





