# 03_Operators_Keywords_Variables


#========================================================= Operators ==============================================================
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	Name	Example	
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y   #the floor division // rounds the result down to the nearest whole number
x=17
y=3
print(x//y)  # 5


# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	
# =	        x = 5	x = 5	
# +=	x += 3   	x = x + 3	
# -=	x -= 3  	x = x - 3	
# *=	x *= 3	    x = x * 3	
# /=	x /= 3	    x = x / 3	
# %=	x %= 3	    x = x % 3	
# //=	x //= 3	    x = x // 3	
# **=	x **= 3	    x = x ** 3
#  Python does not support ++ (increment) or -- (decrement) operators like C, C++, or Java. Instead, you have to use += or -=.
# Why Doesn’t Python Support ++ or --?
# Python emphasizes readability and clarity. The ++ and -- operators are known to cause confusion in languages like C and C++. Instead, Python encourages explicit updates using += 1 or -= 1.

# Let me know if you have more questions! 🚀


# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y
# In Python, comparison operators return Boolean values

# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

x=5
y=5
print(id(x))
print(id(y))
print(x is y)

# Memory Allocation in Python
### **How Python Allocates Memory to Different Data Types**
# Python handles memory management automatically using **dynamic memory allocation** and **garbage collection**. The memory allocation depends on the data type and is managed by the **Python Memory Manager**.

# ---

# ## **1. Memory Allocation in Python**
# Python memory is divided into two main parts:
# ### **1.1 Stack Memory (for small and local objects)**
# - Stores **function calls, local variables, and references** to objects.
# - Works in a **Last In, First Out (LIFO)** manner.
# - Automatically freed when a function ends.

# ### **1.2 Heap Memory (for large objects and dynamic data)**
# - Stores **actual objects** (lists, dictionaries, class instances, etc.).
# - Python dynamically allocates memory in the **heap**.
# - Objects remain in memory until the **Garbage Collector** removes unused ones.

# ---

# ## **2. Memory Allocation for Different Data Types**
# Python handles memory allocation differently for **immutable** and **mutable** objects.

# ### **2.1 Immutable Objects (Integers, Strings, Tuples, Floats)**
# - **Stored in a special memory pool for efficiency** (like integer caching).
# - Example:
#   ```python
#   a = 10  # Allocated in memory pool
#   b = 10  # Same memory reference as 'a'
#   print(id(a), id(b))  # Same memory location
#   ```
#   - Python **reuses small integer objects** (`-5 to 256`) to save memory.
#   - Strings are also stored efficiently using **string interning**.

# ---

# ### **2.2 Mutable Objects (Lists, Dictionaries, Sets, Custom Objects)**
# - Stored in **heap memory**.
# - Each variable gets a new memory location.
# - Example:
#   ```python
#   list1 = [1, 2, 3]
#   list2 = [1, 2, 3]
#   print(id(list1), id(list2))  # Different memory locations
#   ```

# ---

# ## **3. Reference Counting & Garbage Collection**
# Python tracks the number of references to an object using **reference counting**.
# - If the count reaches **zero**, the **Garbage Collector** automatically frees the memory.

# ### **Example of Reference Counting**
# ```python
# import sys

# a = [1, 2, 3]
# b = a  # Another reference to the same list
# print(sys.getrefcount(a))  # Output: 3 (a, b, and getrefcount reference it)
# del a
# print(sys.getrefcount(b))  # Output: 2
# ```

# ---

# ## **4. Python’s Garbage Collector (GC)**
# Python has an **automatic garbage collector** that removes unused objects to free memory.
# - Uses **Reference Counting** + **Generational GC** (objects grouped into Young, Middle-aged, Old generations).
# - You can manually trigger garbage collection:
#   ```python
#   import gc
#   gc.collect()
#   ```

# ---

# ## **Conclusion**
# 1. **Small immutable objects** (integers, strings) → **Memory pool (stack memory)**
# 2. **Mutable objects** (lists, dictionaries) → **Heap memory**
# 3. **Reference counting & Garbage Collector** manage memory automatically.
# 4. **Python optimizes memory** by caching small integers and using string interning.


# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

x="abdullah"
y="ab" in x
print(y)  #true

# Operator	Description	Example	
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers

# Operator Precedence
# Operator precedence describes the order in which operations are performed.
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description	
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR

# ===================================================================================================================================


#=================================================== Keywords ======================================================================
# Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:
# Keyword	Description
# and	A logical operator
# as	To create an alias
# assert	For debugging
# break	To break out of a loop
# class	To define a class
# continue	To continue to the next iteration of a loop
# def	To define a function
# del	To delete an object
# elif	Used in conditional statements, same as else if
# else	Used in conditional statements
# except	Used with exceptions, what to do when an exception occurs
# False	Boolean value, result of comparison operations
# finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	To create a for loop
# from	To import specific parts of a module
# global	To declare a global variable
# if	To make a conditional statement
# import	To import a module
# in	To check if a value is present in a list, tuple, etc.
# is	To test if two variables are equal
# lambda	To create an anonymous function
# None	Represents a null value
# nonlocal	To declare a non-local variable
# not	A logical operator
# or	A logical operator
# pass	A null statement, a statement that will do nothing
# raise	To raise an exception
# return	To exit a function and return a value
# True	Boolean value, result of comparison operations
# try	To make a try...except statement
# while	To create a while loop
# with	Used to simplify exception handling
# yield	To return a list of values from a generator

# ================================================ Variable ========================================================================
# Variables are containers for storing data values.
# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Variables are case sensitive :   a and A are different

 
#Completed