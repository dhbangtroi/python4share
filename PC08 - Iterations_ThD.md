# Chapter 8 - Iterations


-------------------------------

Computers do not get bored. If you want the computer to repeat a certain task hundreds of thousands of times, it does not protest. Humans hate too much repetition. Therefore, repetitious tasks should be performed by computers. All programming languages support repetitions. The general class of programming constructs that allow the definition of repetitions are called "iterations". A term which is even more common for such tasks is "loops".

This chapter explains all you need to know about loops in Python. Make sure you take your time for this chapter, and work on it until you understand it completely. Loops are such a basic concept in programming that you need to understand them in all their details. Each and every chapter after this one needs loops.

---

## `while` loop

Suppose you want to print the first five multiples of number 23. With the material from the previous chapter, you would program that as follows:


```python
print(1 * 23)
print(2 * 23)
print(3 * 23)
print(4 * 23)
print(5 * 23)
```

But what if we want you to print the first 500 multiples? Are you going to create a block of code of more than 500 lines long? Surely there must be an easier way to do this?

Of course there is. You can use a loop to do this. 

The first loop you will learn about is the `while` loop. A `while` statement is quite similar to an `if` statement. The syntax is:

    while <boolean expression>:
        <statements>

Just like an `if` statement, the `while` statement tests a boolean expression, and if the expression evaluates to `True`, it executes the code block below it. However, contrary to the `if` statement, once the code block has finished, the code "loops" back to the boolean expression to test it again. If it still evaluates to `True`, the code block below it gets executed once more. And after it has finished, it loops back again, and again, and again...

Note: if the boolean expression immediately evaluates to `False`, then the code block below the `while` is skipped completely, just like with an `if` statement.

### `while` loop, first example

Let's take a simple example: we want to write a function that prints numbers 1 to 5. With a `while` loop, that can be done as follows:


```python
def print_one_to_five():
    num = 1
    while num <= 5:
        print( num )
        num += 1
    print( "Done" )
    
print_one_to_five()
```

It is crucial that you understand this code, so let's discuss it step by step.

The first line of the function initializes a variable `num`. This is the variable that the code will print, so it is initialized to `1`, as `1` is the first value that must be printed.

Then the `while` loop starts. The boolean expression says `num <= 5`. Since `num` is `1`, and `1` is actually smaller than (or equal to) `5`, the boolean expression evaluates to `True`. Therefore, the code block below the `while` gets executed.

The first line of the code block below the `while` prints the value of `num`, which is `1`. The second line adds `1` to the value of `num`, which makes `num` hold the value `2`. Then the code loops back to the boolean expression (i.e., the last line of the code, the printing of "Done", is not executed as it is not part of the loop and the loop has not finished yet).

Since `num` is `2`, the boolean expression still evaluates to `True`. The code block gets executed once more. `2` is displayed, `num` gets the value `3`, and the code loops back to the boolean expression.

Since `num` is `3`, the boolean expression still evaluates to `True`. The code block gets executed once more. `3` is displayed, `num` gets the value `4`, and the code loops back to the boolean expression.

Since `num` is `4`, the boolean expression still evaluates to `True`. The code block gets executed once more. `4` is displayed, `num` gets the value `5`, and the code loops back to the boolean expression.

Since `num` is `5`, the boolean expression still evaluates to `True` (because `5 <= 5`). The code block gets executed once more. `5` is displayed, `num` gets the value `6`, and the code loops back to the boolean expression.

Since `num` is `6`, the boolean expression now evaluates to `False` (because `6` is bigger than `5`). Therefore, the code block gets skipped, and the code continues with the first line below the code block, which is the last line of the code. The word `Done` is printed, and the code ends.

**Exercise**: Change the code above so that the function prints the numbers 1, 3, 5, 7, and 9.


```python
def print_odds_one_to_nine():
    num = 1
    while num <= 9:
        print( num )
        num += 2
    print( "Done" )
    
print_odds_one_to_nine()
```

    1
    3
    5
    7
    9
    Done
    

### `while` loop, second example

If you understand the first example, you probably also understand how to print the first five multiples of 23. This is implemented as follows:


```python
def print_multiples_of_23():
    count = 1
    while count <= 5:
        print( count*23 )
        count += 1
    print( "Done" )

print_multiples_of_23()
```

    23
    46
    69
    92
    115
    Done
    

Study this code closely. variable `count` is used to count how often the code has gone through the loop. Since the loop must be done five times, `count` is started at `1` and the boolean expression for the loop continues until `count` is higher than `5`. Thus, in the loop `count` gets increased by `1` at the end of every cycle through the loop.

We can also write the function as follows:


```python
def print_multiples_of_23():
    count = 0
    while count < 5:
        count += 1
        print( count*23 )
    print( "Done" )

print_multiples_of_23()
```

    23
    46
    69
    92
    115
    Done
    

You may wonder why `count` is started at `0` and the boolean expression checks if `count < 5`. Why not start `count` at `1` and check if `count <= 5`? The reason is convention: programmers are used to start indices at `0`, and if they count, they count "up to but not including". When you continue with programming, you will find that most code sticks to this convention. Most standard programming constructs that use indices or count things apply this convention too. Therefore it is a good idea to get used to this convention, as it makes code easier to read.

Note: The variable `count` is what programmers call a "throw-away variable". Its only purpose is to count how often the loop has been cycled through, and it has no real meaning before or after the loop. Programmers often choose a single-character variable name for such a variable, usually `i` or `j`. In this example we chose the name `count` because it is illustrative of what the variable does for the code, but a single-character name for this variable would have been acceptable.

**Exercise**: Change the code block above so that the function also prints the total and the average of the five numbers.


```python
def print_total_avg_multiples_of_23():
    count = 0
    total = 0
    while count < 5:
        #print(count)
        count += 1
        total += count*23
        print( count*23 )
        #print(total)
    print('Total =', total)
    print('Average =', total/count)
    print( 'Done' )

print_total_avg_multiples_of_23()
```

    23
    46
    69
    92
    115
    Total = 345
    Average = 69.0
    Done
    

### Endless loops

The code below is supposed to start at number 1, and add up numbers, until it encounters a number that, when squared, is dividable by 1000. The code contains an error, though. See if you can spot it (without running the code!).


```python
number = 1
total = 0
while (number * number) % 1000 != 0:
    total += number
print( "Total is", total )
```

The heading of this subsection gave away the answer, of course: this code contains a loop that never terminates. If you run it, it looks like the program "hangs", i.e., sits there and does nothing. It is not doing nothing, it is actually highly active, but it is in a neverending addition. `number` starts at `1`, and is never increased in the loop, so the boolean expression will always be `True`. This is called an "endless loop", and it is the single one great danger in using `while` loops.

If you did run this code, you can go the the "Kernel" menu and choose "Interrupt". If you ran the code without modifications, you will have to do that. 

If you did not spot that this is an example of an endless loop, you might have seen what happened if we had written code that prints something in the loop. Unfortunately, browsers tend not to handle notebooks that print a lot of stuff well, and you would probably need a reboot of your computer, or at least the shutdown of the browser via a task manager, to resolve the problem. 

Since every programmer writes endless loops by accident now and again, it is good practice when you program a loop to immediately add a statement to a loop that makes a change that is tested in the boolean expression, so that you do not forget about it.

Should you still write an endless loop and have trouble interrupting the kernel, if you are on the notebook server the instructor can shut down your kernel for you.

**Exercise**: Fix the code above so that it no longer is an endless loop.

### `while` loop practice exercises

You should now practice a bit with simple `while` loops.

**Exercise**: In the code block below, write a countdown function. It takes an integer parameter `count`, and counts down to zero, printing each number it encounters (e.g. 10, 9, 8, ...). It does not print `0`, instead it prints "Blast off!". The function does not return anything.


```python
def print_count_down(count):
    #print stuff
    while count > 0:
        print(count)
        count -= 1
    print('Blast off!')
print_count_down(3)
```

    3
    2
    1
    Blast off!
    

**Exercise**: The factorial of a positive integer is that integer, multiplied by all positive integers that are lower (excluding zero). You write the factorial as the number with an exclamation mark after it. E.g., the factorial of 5 is `5! = 5 * 4 * 3 * 2 * 1 = 120`. Write a function that calculates the factorial of its (integer) parameter. Test your function for different parameter values, but do not use very large numbers as factorials grow exponentially. Hint: to do this with a `while` loop, you need at least one more variable.


```python
def factorial(number):
    result = number
    while number > 1:
        result = result * (number - 1)
        number -= 1
    return result #factorial of number

print(factorial(16))
```

    20922789888000
    

---

## `for` loop

An alternative way of implementing loops is by using a `for` loop. `for` loops tends to be easier and safer to use than `while` loops, but cannot be applied to all iteration problems. `while` loops are more general. In other words, everything that a `for` loop can do, a `while` loop can do too, but not the other way around.

The syntax of a `for` loop is as follows:

    for <variable> in <collection>:
        <statements>

A `for` loop gets presented with a collection of items, and it will process these items, in order, one by one. Every cycle through the loop will put one item in the variable given next to the `for`, and can then be used in the code block under the `for`. The variable does *not* need to exist before the `for` loop is encountered. If it does, it gets overwritten. It is a real variable, by the way, in the sense that it still exists after the loop has finished. It will contain the last value that it got assigned during the processing of the loop.

At this point you might wonder what a "collection" is. There are many different kinds of collections in Python, and in this section we will introduce a few. In later chapters collections will be discussed in more detail.

### `for` loop with strings

The only collection introduced until now is the string. A string is a collection of characters, e.g., the string "banana" is a collection of the characters "b", "a", "n", "a", "n", and "a", in that specific order. The following code loops through each of these letters:


```python
for letter in "banana":
    print( letter )
print( "Done" )
```

    b
    a
    n
    a
    n
    a
    Done
    

While this code is fairly trivial, let's go through it step by step.

When the `for` loop is encountered, Python takes the first member of the collection (here, the first letter in the string "banana", which is "b") and puts it into the variable `letter`. It then executes the code block below `for`. The code block contains only one statement, which is the printing of `letter`. So the program prints "b", and then loops back to the `for`. 

Python then takes the next letter, which is an "a", and it executes the code block with `letter` being an "a". It then repeats this process for each of the remaining letters.

Once all the letters have been used, the `for` loop ends, and Python executes the last line of the code, which is the printing of the word "Done".

To be absolutely clear: In a `for` loop you do *not* have to write code that explicitly increases some kind of variable that then grabs the next letter, or something like that. The `for` statement handles that automatically: every time it is looped back to, it takes the next item from the collection. 

### `for` loop using a variable as collection

In the code above, the literal string "banana" was used as the collection, but it could also be a variable that contains a string. For instance, the following code introduces a function that prints every letter in its string parameter:


```python
def print_letters(text):
    for letter in text:
        print( letter )
    print( "Done" )
    
print_letters("banana")
print_letters("apple")
```

    b
    a
    n
    a
    n
    a
    Done
    a
    p
    p
    l
    e
    Done
    

You might wonder if this isn't dangerous. What happens if the programmer changes the contents of the variable `text` *in* the loop's code block? Let's try that out:


```python
def print_letters(text):
    for letter in text:
        print( letter )
        if letter == "n":
            text = "orange"    
    print( "Done" )
    
print_letters("banana")
```

    b
    a
    n
    a
    n
    a
    Done
    

As you can see when you run this code, changing the contents of the variable `text` in the loop has *no effect* on the loop's processing. The sequence of characters that the loop processes is only constituted once, when the `for` loop is first entered. This is a great feature of `for` loops, because it means they are *guaranteed* to end. No `for` loops are endless! 

Note that there is a conditional statement in the loop above. There is nothing that stops you from putting conditions in the code block for a loop. There is also nothing against putting loops in the code block for a condition, or even putting loops inside loops (more on that last option follows later in this chapter). As long as you stick to the syntactic requirements, you can use conditional statements and loops wherever you can write Python statements. 

### `for` loop using a range of numbers

Python offers a `range()` function that generates a collection of sequential numbers, which is often used for `for` loops. The simplest call to `range()` has one parameter, which is a number. It will generate all integers, starting at zero, up to but not including the parameter.


```python
for x in range( 10 ):
    print( x )
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

`range()` can get multiple parameters. If you give two parameters, then the first will be the starting number (default is zero), while the second will be the "up to but not including" number. If you give three parameters, the third will be a step size (default is `1`). You can choose a negative step size if you want to count down. With a negative step size, make sure that the starting number is higher than the number that you want to count up to (or down to, in this case).


```python
for x in range( 1, 11, 2 ):
    print( x )
```

    1
    3
    5
    7
    9
    

**Exercise:** Change the three parameters above to observe their effect, until you fully understand the `range()` function.


```python
for x in range( 11, 1, -2 ):
    print( x )
```

    11
    9
    7
    5
    3
    

**Exercise:** Write a function that, using the `for` loop and `range()` function, takes two integer parameters `a` and `b`, and prints multiples of 3 starting at `a` and counting down to `b`.


```python
def print_multiple3(a,b):
    #print multiples of 3, starting at a and counting down to b
    for x in range(a,b-1,-1):
        if x % 3 == 0:
            print(x)
print_multiple3(16,1)            
```

    15
    12
    9
    6
    3
    

### `for` loop with manual collections

If you want to use a `for` loop to cycle through items in a collection that you create manually, you can do so by listing all your items between parentheses. This defines a "tuple" for the items of your collection. Tuples will be discussed later.


```python
for x in ( 10, 100, 1000, 10000 ):
    print( x )
```

    10
    100
    1000
    10000
    

Or:


```python
for x in ( "apple", "pear", "orange", "banana", "mango", "cherry" ):
    print( x )
```

    apple
    pear
    orange
    banana
    mango
    cherry
    

Your collection can even consist of mixed types.

### Practice with `for` loops

To get strong grips on how to use `for` loops, do the following exercises.

**Exercise**: You already created a function with a `while` loop that printed the first five multiples of 23. Create another code for this task, but now use a `for` loop.


```python
# first five multiples of 23.
def print_multiples_of_23():
    for i in range(1,6):
        print( i*23 )
    print( "Done" )

print_multiples_of_23()
```

    23
    46
    69
    92
    115
    Done
    

**Exercise**: Create a countdown function that starts at a certain count, and counts down to zero. Instead of zero, print "Blast off!". Use a `for` loop. 


```python
# Count down with for loop.
def print_count_down(count):
    for count in range(count,0,-1):
        print(count)
    print('Blast off!')
print_count_down(13)
```

    13
    12
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Blast off!
    

---

## Loop control statements

There are three extra statements that help you control the flow in a loop. They are `else`, `break`, and `continue`.

### `else`

Just like with an `if` statement, you can add an `else` statement to the end of a `while` or `for` loop. The code block for the `else` is executed whenever the loop ends, i.e., when the boolean expression for the `while` loop evaluates to `False`, or when the last item of the collection of the `for` loop is processed.

Here is an example of using the `else` clause for a `while` loop:


```python
def count_up(i):
    while i < 5:
        print( i )
        i += 1
    else:
        print( "The loop ends, i is now", i )
    print( "Done" )
    
count_up(1)
```

    1
    2
    3
    4
    The loop ends, i is now 5
    Done
    

And here is an example of using `else` for a `for` loop:


```python
def print_fruits():
    for fruit in ( "apple", "orange", "strawberry" ):
        print( fruit )
    else:
        print( "The loop ends, fruit is now", fruit )
    print( "Done" )   
    
print_fruits()
```

### `break`

The `break` statement allows you to prematurely break out of a loop. I.e., when Python encounters the `break` statement, it will no longer process the remainder of the code block for the loop, and will not loop back to the boolean expression. It will simply continue with the first statement after the loop's code block.

To see why this is useful, here follows an interesting exercise. We are looking for the first positive number under 10000 that is both a multiple of 9 and 21. We can write a function to do that for us:


```python
i = 1
while i <= 10000:
    if i%9 == 0 and i%21 == 0:
        break
    i += 1

print (i, "is our solution.")
```

In this example we see the `break` statement used to good effect. Since we have no idea which number we are looking for, we are just going to check a whole bunch of numbers. we let a counter `i` run up to `10000`. We might find the answer at any point, and when we do, we `break` out of the loop, because further testing of numbers no longer serves a purpose.


Interestingly, `break` in a program functions similarly to `return` in a function. We can write the above code as a function and replace `break` with `return`, with the same effect:


```python
def joint_multiple():
    i = 1
    while i <= 10000:
        if i%9 == 0 and i%21 == 0:
            return i
        i += 1

print (joint_multiple(), "is our solution.")
```

Or even better, we can pass the values 9 and 21 to the function as parameters, and make it more general-purpose:


```python
def joint_multiple(a,b):
    i = 1
    while i <= 10000:
        if i%a == 0 and i%b == 0:
            return i
        i += 1

print (joint_multiple(9,21), "is our solution.")
```

The `break` statement also works for `for` loops. But it cannot be used outside a loop. It is only defined for loops. Note that when a `break` statement is encountered, and the loop also has an `else` clause, the code block for the `else` will *not* be executed.

The following code checks a list of grades for a student. As long as all grades are 5.5 or higher, the student passes. When one or more grades are lower than 5.5, the student fails. The grades are in a collection that is given to a `for` loop.


```python
for grade in ( 8, 7.5, 9, 6, 6, 6, 5.5, 7, 5, 8, 7, 7.5 ):
    if grade < 5.5:
        print( "The student fails!" )
        break
else:
    print( "The student passes!" )
```

    The student fails!
    

**Exercise**: Remove the 5 from the list of grades and notice that the student now passes. Study this code carefully until you understand it.


```python
for grade in ( 8, 7.5, 9, 6, 6, 6, 5.5, 7, 8, 7, 7.5 ):
    if grade < 5.5:
        print( "The student fails!" )
        break
else:
    print( "The student passes!" )
```

    The student passes!
    

### `continue`

When the `continue` statement is encountered in the code block of a loop, the current cycle ends immediately and the code loops back to the start of the loop. For a `while` loop, that means that the boolean expression is evaluated again. For a `for` loop, that means that the next item is taken from the collection and processed.

The following code prints all numbers between 1 and 100 that cannot be divided by 2 or 3, do not end in a 7 or 9, and do not consist of two equal digits.


```python
for num in range( 1, 101 ):
    if num%2 == 0:
        continue
    if num%3 == 0:
        continue
    if num%10 == 7:
        continue
    if num%10 == 9:
        continue
    if num > 9:
        if num%10 == int( num / 10 ):
            continue
    print( num )
```

Alternatively, you could have created one big boolean expression for an `if` statement, but that would become unreadable quickly. Still, just like `break` statements, `continue` statements can always be avoided if you really want to, but they do help keeping code understandable.

Note that `continue` statements, just like `break` statements, can only be used inside loops.

Be very, very careful when using a `continue` in a `while` loop. Most `while` loops use a number that restricts the number of cycles through the loop. Usually such a number is increased at the bottom of the code block for the loop. A `continue` statement would loop back to the boolean expression immediately, without increasing the number, and thus such a `continue` could easily cause an endless loop. I.e.:

    i = 0
    while i < 10:
        if i == 5:
            continue
        i += 1

causes an endless loop!

**Exercise**: Write a program that processes a collection of numbers using a `for` loop. The program should end immediately, printing only the word "Done", when a zero is encountered (use a `break` for this). Negative numbers should be ignored (use a `continue` for this). If no zero is encountered, the program should display the sum of all numbers (do this in an `else` clause). Always display "Done" at the end of the program.


```python
total = 0
for num in ( 12, 4, 3, 33, -2, -5, 0, 7, 22, 4):
    #print('num =', num)
    # Write your code here
    if num == 0:
        #print('num == 0', num == 0, count)
        break
    if num < 0:
        #print('num < 0', num < 0, count)
        continue
    else:
        total += num
else:
    print(total)
print('Done')
```

    85
    Done
    

With the numbers provided, the program should display only "Done". If you remove the zero, it should display 85 (and "Done").

Now write a function that does the same; that is, it receives a collection of numbers and processes them as described above:


```python
def process_numbers(numbers):
    total = 0
    for num in numbers:
        #print('num =', num)
        # Write your code here
        if num == 0:
            #print('zero')
            exec = 0
            #print('exec =', exec)
            break
        if num < 0:
            #print('negative')
            exec = -1
            #print('exec =', exec)
            continue
        else:
            total += num
            exec = 1
            #print('else')
            #print('exec =', exec)
            #print('count =', count)
        #print('-----------------')
    if exec == 1:
        x = str(total) + '\n' + 'Done'
    else:
        x = 'Done'
    return x
print(process_numbers(( 12, 4, 3, 33, -2, -5, 7, 22, 4 )))
```

    85
    Done
    

-------

## Nested loops

You can put a loop inside another loop. 

That is a simple statement, but it is one of the hardest concepts for students to wrap their minds around.

Let's first look at an example of a double-nested loop, i.e., a loop which contains one other loop. Usually programmers talk about an "outer loop" and an "inner loop". The inner loop is part of the code block for the outer loop.


```python
for i in range( 3 ):
    print( "Entering the outer loop for i =", i )
    for j in range( 3 ):
        print( "    Entering the inner loop for j =", j )
        print( "    ", i, ",", j)
        print( "    Leaving the inner loop for j =", j )
    print( "Leaving the outer loop for i =", i )
```

Study this code and its output until you fully understand it!

The code first gives `i` the value `0`, and then lets `j` take on the values `0`, `1`, and `2`. It then gives `i` the value `1`, and then lets `j` take on the values `0`, `1`, and `2`. Finally, it gives `i` the value `2`, and then lets `j` take on the values `0`, `1`, and `2`. So this code runs through all possible pairs of `(i,j)` with `i` and `j` being `0`, `1`, or `2`.

Notice how variables for the outer loop are also accessible by the inner loop. `i` exists in both the outer and the inner loop.

Suppose that you want to write a function tat prints all pairs `(i,j)` where `i` and `j` can take on the values `0` to `maximum`, but `j` must be higher than `i`. The function takes `maximum` as a parameter:


```python
def print_pairs(maximum):
    for i in range( maximum ):
        for j in range( i+1, maximum ):
            print( "    ", i, ",", j)
            
print_pairs(4)
```

         0 , 1
         0 , 2
         0 , 3
         1 , 2
         1 , 3
         2 , 3
    

See how the value of `i` is used to set the range for `j`?

**Exercise**: Write a function that prints all pairs `(i,j)` where `i` and `j` can take on the values `0` to `maximum`, but they cannot be equal.


```python
def print_nonequal_pairs(maximum):
    #print pairs
    for i in range( maximum ):
        for j in range( maximum ):
            if i == j:
                continue
            else:
                print( "    ", i, ",", j)
                
print_nonequal_pairs(3)
```

         0 , 1
         0 , 2
         1 , 0
         1 , 2
         2 , 0
         2 , 1
    

You can, of course, also nest `while` loops, or mix  nesting `for` loops with `while` loops.

You should be aware that when you use a `break` or `continue` in an inner loop, it will only `break` out of the inner loop or `continue` with the inner loop, respectively. There is no command that you can give in an inner loop that breaks out of both the inner and outer loop immediately.

Once you understand double-nested loops, it should come as no surpise that you can also triple-nest loops, quadruple-nest loops, or go even deeper. However, in practice seldom see
a nesting deeper than triple-nested.


```python
for i in range( 3 ):
    for j in range( 3 ):
        for k in range( 3 ):
            print( i, ",", j, ",", k)
```

    0 , 0 , 0
    0 , 0 , 1
    0 , 0 , 2
    0 , 1 , 0
    0 , 1 , 1
    0 , 1 , 2
    0 , 2 , 0
    0 , 2 , 1
    0 , 2 , 2
    1 , 0 , 0
    1 , 0 , 1
    1 , 0 , 2
    1 , 1 , 0
    1 , 1 , 1
    1 , 1 , 2
    1 , 2 , 0
    1 , 2 , 1
    1 , 2 , 2
    2 , 0 , 0
    2 , 0 , 1
    2 , 0 , 2
    2 , 1 , 0
    2 , 1 , 1
    2 , 1 , 2
    2 , 2 , 0
    2 , 2 , 1
    2 , 2 , 2
    

---

## Being smart about loops

To complete this chapter, we discuss a few strategies on loop design.

### Processing data items one by one

Usually, when a loop is applied, you are working through a long series of data items. Each cycle through the loop will process one of those data items. You then often need to remember something about the data items that you have processed so far, for which you need extra variables. You have to be smart in thinking about such variables.

Take the following example: we need a function that takes ten integer parameters, and returns the largest (or smallest). Since you will have to process all the numbers, you have to think about a loop, and in particular, a loop wherein you have only one of the numbers available each cycle through the loop (but you will see them all before the loop ends). You must now think about variables that you can use to remember something each cycle through the loop, that allows you to determine, at the end, which number was the largest or the smallest. Which variables do you need?

The answer, which comes easy to anyone who has been doing some programming, is that you need to remember, each cycle through the loop, which is the largest or smallest number *until now*. That means that every cycle through the loop you compare the new number with the variables in which you retain the largest or smallest, and replace them with the new number if that is appropriate. 

You will have to find good initial values for these variables. The largest and smallest need an appropriate value. The best solution in this case is to fill them with the first number, as that number is both the largest and the smallest at that point.

---

## On designing algorithms

At this point in the course, you will often run into exercises and coding problems for which you are unsure how to solve them. The example of finding the largest or smallest number in a collection is such a problem, and you saw a solution for that. Such a solution approach is called an "algorithm". But how do you design such algorithms?

What you have to do in such a situation is sit back, leave the keyboard alone, and think "How would I solve this problem as a human?" Try to write down what you would do if you would do it by hand. It does not matter if what you would do is a very boring task that you would never *want* to do by hand -- you have a computer to do the boring things for you.

Once you have figured out what you would do, then try to think about how you would translate that to code. Because basically, that is what you need to tell the computer: the steps that you as a human would take to get to a solution. If you really cannot think of any way that you as a human would use to solve a problem, then you won't be able to tell the computer how to do it for you.

---

## What you learned

In this chapter, you learned about:

- What loops are
- `while` loops
- `for` loops
- Endless loops
- Loop control via `else`, `break`, and `continue`
- Nested loops

-------

## Exercises

Since loops are incredibly important and students often have problems with them, we provide a number of exercises here and recommend that you do them all. You will learn a lot.

### Exercise 8.1

Write a function that prints a multiplication table for digits 1 to 10. A multiplication table for the numbers 1 to `num = 3` looks as follows:

`. |  1  2  3`<br>
`------------`<br>
`1 |  1  2  3`<br>
`2 |  2  4  6`<br>
`3 |  3  6  9`

So the labels on the rows are multiplied by the labels on the columns, and the result is shown in the cell that is on that row/column combination. 


```python
def print_multiplication_table(num):
    # Multiplication table.
    for i in range(1,num+1):
        if i == 1:
            result = ' ' + str(i) + ' |'
            header = ' . |'
        elif i < 10 and i > 1: 
            result = ' ' + str(i) + ' |'
        else:
            result = str(i) + ' |'
        #print('i =', i)
        #print('result =', result)
        for j in range(1,num+1):
            #print('j =', j)
            if i*j < 10:
                result = result + '   ' + str(i * j)
                header = header + '   ' + str(i * j)
            elif i*j > 99:
                result = result + ' ' + str(i * j)
                header = header + ' ' + str(i * j)
            else:
                result = result + '  ' + str(i * j)
                header = header + '  ' + str(i * j)
            #print('result =', result)
        result = result + '\n'
        if i == 1:
            print(header)
            print('-' * len(header))    
            print(result)
        else :
            print(result)
    #print(result)        
print_multiplication_table(10)            
```

     . |   1   2   3   4   5   6   7   8   9  10
    --------------------------------------------
     1 |   1   2   3   4   5   6   7   8   9  10
    
     2 |   2   4   6   8  10  12  14  16  18  20
    
     3 |   3   6   9  12  15  18  21  24  27  30
    
     4 |   4   8  12  16  20  24  28  32  36  40
    
     5 |   5  10  15  20  25  30  35  40  45  50
    
     6 |   6  12  18  24  30  36  42  48  54  60
    
     7 |   7  14  21  28  35  42  49  56  63  70
    
     8 |   8  16  24  32  40  48  56  64  72  80
    
     9 |   9  18  27  36  45  54  63  72  81  90
    
    10 |  10  20  30  40  50  60  70  80  90 100
    
    

### Exercise 8.2

If you did the previous exercise with a `while` loop, then do it again with a `for` loop. If you did it with a `for` loop, then do it again with a `while` loop. If you did not use a loop at all, you should be ashamed of yourself.


```python
def print_multiplication_table(num):
    # Multiplication table.
    i = 1
    while i <= num:
        if i == 1:
            result = ' ' + str(i) + ' |'
            header = ' . |'
        elif i < 10 and i > 1: 
            result = ' ' + str(i) + ' |'
        else:
            result = str(i) + ' |'
        #print('i =', i)
        #print('result =', result)
        j = 1
        while j <= num:
            #print('j =', j)
            if i*j < 10:
                result = result + '   ' + str(i * j)
                header = header + '   ' + str(i * j)
            elif i*j > 99:
                result = result + ' ' + str(i * j)
                header = header + ' ' + str(i * j)
            else:
                result = result + '  ' + str(i * j)
                header = header + '  ' + str(i * j)
            #print('result =', result)
            j += 1
        result = result + '\n'
        if i == 1:
            print(header)
            print('-' * len(header))    
            print(result)
        else :
            print(result)
        i += 1
    #print(result)        
print_multiplication_table(10)        
```

     . |   1   2   3   4   5   6   7   8   9  10
    --------------------------------------------
     1 |   1   2   3   4   5   6   7   8   9  10
    
     2 |   2   4   6   8  10  12  14  16  18  20
    
     3 |   3   6   9  12  15  18  21  24  27  30
    
     4 |   4   8  12  16  20  24  28  32  36  40
    
     5 |   5  10  15  20  25  30  35  40  45  50
    
     6 |   6  12  18  24  30  36  42  48  54  60
    
     7 |   7  14  21  28  35  42  49  56  63  70
    
     8 |   8  16  24  32  40  48  56  64  72  80
    
     9 |   9  18  27  36  45  54  63  72  81  90
    
    10 |  10  20  30  40  50  60  70  80  90 100
    
    

### Exercise 8.3

Write and test three functions that return the largest, the smallest, and the number of dividables by 3 in a given collection of numbers. Use the algorithm described earlier in this chapter.


```python
def largest(number_collection):
    for i in number_collection:
        max = i
        for j in number_collection:
            if j >= max:
                max = j
    return max #the largest number in number_collection

def smallest(number_collection):
    for i in number_collection:
        min = i
        for j in number_collection:
            if j <= min:
                min = j
    return min #the smallest number in number_collection

def dividables_by3(number_collection):
    count = 0
    for i in number_collection:
        if i % 3 == 0:
            count +=1            
    return count #the number of dividables by 3 in number_collection

numbers = (2, 821, 19, 23, 1, 10, 817, 5, 61)
print(largest(numbers))
print(smallest(numbers))
print(dividables_by3(numbers))
```

    821
    1
    0
    

### Exercise 8.4

"99 bottles of beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows: "99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall." The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Write a function that generates and prints all the verses of the song (though you might start a bit lower, for instance with 10 bottles). Make sure that your loop is not endless, and that you use the proper inflection for the word "bottle".


```python
def bottle_song(bottles):
    #print the song lyrics
    song = ""
    for i in range(bottles, 0, -1):
        x = i
        x -= 1
        if i > 2:
            lrc = str(i) + " bottles of beer on the wall, " \
            + str(i) + " bottles of beer. Take one down, pass it around, " \
            + str(x) + " bottles of beer on the wall."
        elif i == 2:
            lrc = str(i) + " bottles of beer on the wall, " \
            + str(i) + " bottles of beer. Take one down, pass it around, " \
            + str(x) + " bottle of beer on the wall."
        else:
            lrc = str(i) + " bottle of beer on the wall, " \
            + str(i) + " bottle of beer. Take one down, pass it around, " \
            + str(x) + " bottle of beer on the wall."
        song = song + '\n' + lrc
    return song
print(bottle_song(10))        
```

    
    10 bottles of beer on the wall, 10 bottles of beer. Take one down, pass it around, 9 bottles of beer on the wall.
    9 bottles of beer on the wall, 9 bottles of beer. Take one down, pass it around, 8 bottles of beer on the wall.
    8 bottles of beer on the wall, 8 bottles of beer. Take one down, pass it around, 7 bottles of beer on the wall.
    7 bottles of beer on the wall, 7 bottles of beer. Take one down, pass it around, 6 bottles of beer on the wall.
    6 bottles of beer on the wall, 6 bottles of beer. Take one down, pass it around, 5 bottles of beer on the wall.
    5 bottles of beer on the wall, 5 bottles of beer. Take one down, pass it around, 4 bottles of beer on the wall.
    4 bottles of beer on the wall, 4 bottles of beer. Take one down, pass it around, 3 bottles of beer on the wall.
    3 bottles of beer on the wall, 3 bottles of beer. Take one down, pass it around, 2 bottles of beer on the wall.
    2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall.
    1 bottle of beer on the wall, 1 bottle of beer. Take one down, pass it around, 0 bottle of beer on the wall.
    

### Exercise 8.5

The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a function that calculates and prints the Fibonacci sequence until the numbers get higher than a `maximum`.


```python
def print_fibonacci(maximum):
    # print Fibonacci seri
    i = 0
    x = 0
    while True:
        if i < 2:
            total = 1
            x = 1
        else:
            total += x
            x = total - x
            if total > maximum:
                break
        i += 1
        print(total, end = ", ")
print_fibonacci(95)
```

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 

### Exercise 8.6

A prime number is a positive integer that is dividable by exactly two different numbers, namely 1 and itself. The lowest (and only even) prime number is 2. The first 10 prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29. Write a function that returns `True` if its parameter is a prime number, and `False` otherwise. Hint: In a loop where you test the possible dividers of the number, you can conclude that the number is not prime as soon as you encounter a number other than 1 or the number itself that divides it. However, you can *only* conclude that it actually *is* prime after you have tested all possible dividers.


```python
def isPrime(number):
    for num in (2,3,5,7):
        #print(number)
        #print(num)
        #print(number % num == 0)
        if (number == num):
            #print('if')
            return True
            break
        elif (number % num == 0) or (number == 1):
            #print('elif')
            return False
            break
    else:
        #print('else')
        return True
    #return result #True if number is prime, False otherwise
isPrime(6)
```

    elif
    




    False



### Exercise 8.7

Write a function that prints all integers between the parameters `a` and `b` that can be written as the sum of two squares. Produce output in the form of `z = x**2 + y**2`, e.g., `58 = 3**2 + 7**2`. If a number occurs on the list with multiple *different* ways of writing it as the sum of two squares, that is acceptable. 


```python
def print_sum_squares(a,b):
    # print sum of two squares.
    for i in range(a,b):
        for j in range(i,b):
            x = i**2
            y = j**2
            check = x + y
            #print(x)
            #print(y)
            #print(check)
            #print('--------')
            if check <= b and x != y:
                text = str(check) +  ' = ' + str(i) + '**2 + ' + str(j) + '**2'
                print(text)
        #else:
         #   text = 'No integer in range (' + str(a) + ',' + str(b) + ') satisfies the condition!'
print_sum_squares(1,50)
```

    5 = 1**2 + 2**2
    10 = 1**2 + 3**2
    17 = 1**2 + 4**2
    26 = 1**2 + 5**2
    37 = 1**2 + 6**2
    50 = 1**2 + 7**2
    13 = 2**2 + 3**2
    20 = 2**2 + 4**2
    29 = 2**2 + 5**2
    40 = 2**2 + 6**2
    25 = 3**2 + 4**2
    34 = 3**2 + 5**2
    45 = 3**2 + 6**2
    41 = 4**2 + 5**2
    

### Exercise 8.8

A, B, C, and D are all different digits. The number DCBA is equal to 4 times the number ABCD. What are the digits? Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero. Use a quadruple-nested loop.


```python
# Solve 4*ABCD == DCBA.
for d in range(1,10):
    for c in range(0,10):
        if d == c:
            continue
        for b in range(0,10):  
            if b == d or b == c:
                continue
            for a in range(1,10):
                if a == b or a == c or a == d:
                    continue
                x = 1000 * a + 100 * b + 10 * c + d
                y = 1000 * d + 100 * c + 10 * b + a
                if 4 * x == y:
                    print('ABCD =', x)
                    print('DCBA =', y)
else:
    print('Done!')
```

    ABCD = 2178
    DCBA = 8712
    Done!
    

---

## Python 2

In Python 3, the `range()` function is an iterator. This entails that it needs very little memory space: it only retains the last number generated, the step size, and the limit that it should reach. In Python 2 `range()` is implemented differently: it produces all the numbers of the range in memory at once. This means that a statement like `range(1000000000)` in Python 2 requires so much memory that it may very well crash the program. In Python 3, such issues do not exist. In Python 2 it is therefore recommended not to use `range()` for more than 10,000 numbers or so, while in Python 3 no restrictions exist.

---

End of Chapter 8. 
