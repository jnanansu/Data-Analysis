# Function
def operation(A,B, op):
    if op == "sum":
        return A+B
    if op == "prod":
        return A*B
    if op == "minus":
        return A - B
    if op == "div":
        return A/B

# Define Main function
if __name__ == '__main__':
    print(operation(2,5,"div"))
