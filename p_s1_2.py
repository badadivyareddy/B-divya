print("");
num = input(" ");
if num == 'x':
    exit();
else:
    number = int(num);
    if number == 0:
        print("\nFactorial of 0 is 1");
    elif number < 0:
        print("\nFactorial of negative numbers doesn't exist..!!");
    else:
        fact = 1;
        for i in range(1, number+1):
            fact = fact*i;
        print("\nFactorial of", number, "is", fact);
