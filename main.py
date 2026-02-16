#lab 1, lab task 1
# num=int(input("enter a number:"));
# reverse=0;
# while(num!=0):
#     digit=num%10;
#     reverse=reverse*10+digit;
#     num=num//10;
# print("reverse of the number is: ",reverse);

#lab 1, lab task 2
# n=int (input("how many numbers you want to enter: "));
# even_sum=0;
# odd_sum=0;
# for i in range(n):
#     num=int(input("enter a number: "));
#     if(num%2==0):
#         even_sum+=num;
#     else:
#         odd_sum+=num;
# print("sum of even numbers is: ",even_sum);
# print("sum of odd numbers is: ",odd_sum);

#lab 1, lab task 3
# terms=int(input("how many terms you want to print: "));
# first=0;
# second=1;
# print("fibonacci series: ",end="");
# for i in range(terms):
#     print(first,end=" ");
#     next=first+second;
#     first=second;
#     second=next;

#lab 1, lab task 4
# mars=int(input("enter your marks:"));
# def grade(marks):
#     if (marks<50):
#         print("grade: F");
#     elif (marks>=50 and marks<60):
#         print("grade: D");
#     elif (marks>=60 and marks<70):
#         print("grade: C");
#     elif (marks>=70 and marks<80):
#         print("grade: B");
#     elif (marks>=80 and marks<90):
#         print("grade: A");
#     elif(marks>=90 and marks<=100):
#         print("grade: A+");
#     else:
#         print("invalid marks");
# grade(mars);    

#lab 1, lab task 5
# number=int(input("enter a number: "));
# factorial=1;
# if number<0:
#     print("factorial does not exist for negative numbers");
# elif number==0:
#     print("factorial of 0 is 1");       
# else:   
#     for i in range(1,number+1):
#         factorial*=i;
#     print("factorial of ",number," is ",factorial);

