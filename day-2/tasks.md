## Python Programming Practice Questions

### Level 1 — Variables and Basic Data Types

1. **Personal Information**
   Write a Python program to create variables for your name, age, city, and college. Display all the information.

2. **Student Information**
   Create variables to store a student's:
   - Name
   - Roll number
   - Age
   - Department
   - Percentage

   Display the information in a readable format.

3. **Employee Information**
   Create variables for employee name, employee ID, salary, and department. Print all the details.

4. **Change Variable Value**
   Create a variable `age = 20`. Change its value to `21` and print the value before and after changing it.

5. **Multiple Assignment**
   Create three variables `a`, `b`, and `c` and assign them the values `10`, `20`, and `30` in a single statement. Print them.

6. **Same Value Assignment**
   Create three variables `x`, `y`, and `z` and assign `100` to all three variables using a single statement.

---

## Level 2 — Data Types

7. **Display Data Types**
   Create variables containing an integer, float, string, Boolean, and `None`. Print the value and data type of each variable.

8. **Student Marks**
   Create variables for:

   ```text
   Student Name
   English Marks
   Maths Marks
   Science Marks
   ```

   Print all values along with their data types.

9. **Product Information**
   Create variables for:

   ```text
   Product Name
   Price
   Quantity
   Available
   ```

   Display the values and their data types.

10. **Type Checking Program**
    Create four variables:

    ```python
    a = 25
    b = 25.5
    c = "25"
    d = True
    ```

    Use `type()` to display the data type of each variable.

---

## Level 3 — Type Conversion

11. **Convert String to Integer**
    Create:

    ```python
    age = "21"
    ```

    Convert it into an integer and add `5` to it.

12. **Convert String to Float**
    Create:

    ```python
    price = "99.50"
    ```

    Convert it into a float and add `50.50`.

13. **Convert Number to String**
    Create an integer variable containing a roll number. Convert it into a string and display its type before and after conversion.

14. **User Age Program**
    Take the user's age as input, convert it into an integer, and display their age after 5 years.

15. **Simple Calculator**
    Take two numbers from the user, convert them to integers, and display:
    - Addition
    - Subtraction
    - Multiplication
    - Division

---

## Level 4 — Arithmetic Operators

16. **Basic Calculator**
    Create two variables:

    ```python
    a = 20
    b = 6
    ```

    Write a program to calculate:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Floor division
    - Modulus
    - Power

17. **Rectangle Calculator**
    Store the length and width of a rectangle in variables. Calculate:
    - Area
    - Perimeter

18. **Circle Calculator**
    Create a constant `PI = 3.14159`. Take the radius of a circle and calculate its area.

19. **Student Marks**
    Store marks of five subjects and calculate:
    - Total marks
    - Average marks

20. **Shopping Bill**
    Store the price and quantity of a product. Calculate the total bill.

21. **Salary Calculation**
    Store an employee's basic salary. Calculate the salary after adding a bonus of ₹5,000.

22. **Temperature Conversion**
    Store a temperature in Celsius and convert it into Fahrenheit.

---

## Level 5 — Assignment Operators

23. **Update Bank Balance**
    Create:

    ```python
    balance = 10000
    ```

    Add ₹2,000, subtract ₹1,500, and multiply the remaining balance by 2 using assignment operators.

24. **Shopping Quantity**
    Create:

    ```python
    quantity = 5
    ```

    Increase the quantity by 3, then decrease it by 2 using assignment operators.

25. **Score Update**
    Create:

    ```python
    score = 50
    ```

    Add 10, subtract 5, and multiply the result by 2 using `+=`, `-=`, and `*=`.

---

## Level 6 — Comparison Operators

26. **Age Comparison**
    Take the user's age and check whether the age is greater than or equal to 18.

27. **Marks Comparison**
    Take marks from the user and check whether the marks are greater than or equal to 40.

28. **Two Numbers**
    Take two numbers from the user and display the results of:
    - Equal
    - Not equal
    - Greater than
    - Less than
    - Greater than or equal to
    - Less than or equal to

29. **Maximum of Two Numbers**
    Take two numbers and use comparison operators to determine which number is greater.

30. **Password Length Concept**
    Store a number representing password length and check whether it is greater than or equal to 8.

---

## Level 7 — Logical Operators

31. **Student Eligibility**
    A student is eligible for admission if:
    - Age is at least 18
    - Marks are at least 50

    Write a program using `and`.

32. **Scholarship Eligibility**
    A student gets a scholarship if:
    - Marks are at least 80 **OR**
    - Attendance is at least 90%

    Write a program using `or`.

33. **Driving Eligibility**
    Take the user's age and check whether they are eligible to drive if their age is 18 or above.

34. **Login Condition**
    Create two Boolean variables:

    ```python
    username_correct
    password_correct
    ```

    Display whether the user can log in using `and`.

35. **Movie Ticket Eligibility**
    A person can watch a movie if their age is 18 or above **and** they have a valid ticket.

---

## Level 8 — Membership Operators

36. **Fruit Search**
    Create a list:

    ```python
    fruits = ["apple", "banana", "mango", "orange"]
    ```

    Ask the user for a fruit name and check whether it exists in the list.

37. **Language Search**
    Create a list of programming languages and check whether `"Python"` exists in the list.

38. **Student Name Search**
    Create a list of five student names. Ask the user to enter a name and check whether the student exists in the list.

39. **Character Search**
    Store a word in a variable. Ask the user for a character and check whether that character exists in the word.

---

## Level 9 — Identity Operators

40. **Compare Two Lists**
    Write a program:

    ```python
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    ```

    Use both `is` and `==` to compare `a` with `b` and `a` with `c`.

41. **Identity Demonstration**
    Create two variables that refer to the same list and another list containing the same values. Demonstrate the difference between `is` and `==`.

---

# Level 10 — Real-World Mini Programs

42. **Student Result Calculator**
    Write a program that takes marks for five subjects and calculates:
    - Total
    - Average
    - Whether the student scored at least 40 in the average

43. **Shopping Bill Calculator**
    Take:
    - Product price
    - Quantity

    Calculate the total bill and check whether the bill is greater than ₹1,000.

44. **Simple ATM Program**
    Create:

    ```python
    balance = 10000
    withdrawal = 3000
    ```

    Calculate the remaining balance and check whether the remaining balance is greater than ₹5,000.

45. **Employee Salary Calculator**
    Take basic salary and bonus as inputs. Calculate the final salary and check whether the final salary is greater than ₹50,000.

46. **Student Admission Check**
    Take age and percentage as input. A student is eligible if:

    ```text
    age >= 18 AND percentage >= 50
    ```

    Display the result.

47. **Product Availability**
    Create a list of available products. Ask the user for a product name and check whether it is available using `in`.

48. **Number Analysis**
    Take a number from the user and display:
    - Whether it is greater than 100
    - Whether it is equal to 100
    - Whether it is less than 100
    - Its square
    - Its remainder when divided by 2

49. **Age Category Program**
    Take a person's age and use comparison and logical operators to check:
    - Whether they are an adult
    - Whether they are eligible for driving at age 18+

    _(Do not use `if` yet; simply display the Boolean results.)_

50. **Complete Beginner Challenge**
    Write a program that asks the user for:
    - Name
    - Age
    - Marks
    - Favorite fruit

    Then:
    1. Convert age and marks to appropriate numeric types.
    2. Display all information.
    3. Display the data types.
    4. Check whether marks are at least 40.
    5. Check whether the favorite fruit exists in a predefined fruit list.
    6. Display all Boolean results.
