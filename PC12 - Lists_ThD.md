# Chapter 12 - Lists

-------------------------------

Lists are ordered collections of data items. They are a highly flexible data structure, that you will find many uses for.

---

## List basics

A list is a collection of elements.

The elements of a list are *ordered*. Because they are ordered, you can access each of the elements of a list using an index, just like you can access the characters of a string.

In Python, lists are recognizable from the fact that they enclose their elements in square brackets (`[]`). You can get the number of elements in a list by using the `len()` function. You can use a `for` loop to traverse the elements of a list. You can mix data types in a list. You can apply the `max()`, `min()` and `sum()` functions to a list. You can test for the existence of an element in a list using the `in` operator (or for the non-existence by using `not in`).


```python
fruitlist = ["apple", "banana", "cherry", 27, 3.14]

print( len( fruitlist ) )

for element in fruitlist:
    print( element )
print( fruitlist[2] )

print() # remember; print() results in an empty line, and comments explain your code

numlist = [314, 315, 642, 246, 129, 999]
print( max( numlist ) )
print( min( numlist ) )
print( sum( numlist ) )
print( 100 in numlist )
print( 999 in numlist )
```

    5
    apple
    banana
    cherry
    27
    3.14
    cherry
    
    999
    129
    2645
    False
    True
    

**Exercise**: Write a `while` loop to print the elements of a list.


```python
# Traversing a list using while.
fruitlist = ["apple", "banana", "cherry ", "durian", "orange"]

i = 0
while i < len(fruitlist):
    print(fruitlist[i])
    i += 1
```

    apple
    banana
    cherry 
    durian
    orange
    

---

## Lists are mutable

Because lists are mutable, you can change the contents of a list.

To overwrite an element of a list, you can assign a new value to it.


```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[2] = "strawberry"
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian', 'orange']
    ['apple', 'banana', 'strawberry', 'durian', 'orange']
    

You can also overwrite list slices by assigning a new list to the slice. The slice you remove need not be of equal length to the new list you insert.


```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:3] = ["raspberry", "elderberry", "strawberry", "blueberry"]
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian', 'orange']
    ['apple', 'raspberry', 'elderberry', 'strawberry', 'blueberry', 'durian', 'orange']
    

You can insert new elements into a list by assigning them to an zero-sized slice.


```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:1] = ["raspberry", "elderberry", "strawberry", "blueberry"]
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian', 'orange']
    ['apple', 'raspberry', 'elderberry', 'strawberry', 'blueberry', 'banana', 'cherry', 'durian', 'orange']
    

You can delete elements from a list by assigning an empty list to a slice.


```python
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist )
fruitlist[1:3] = []
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian', 'orange']
    ['apple', 'durian', 'orange']
    

Using slices and assignments, you can adapt a list in any way that you like. However, it is easier to change lists using methods. There are many helpful methods available, which I am going to discuss below.

**Exercise**: Change the list in the code block below by turning every word in the list into a word consisting of only capitals. At this point in the notebook, the way to do that is by using a while loop that uses a variable `i` that starts at 0 and runs up to `len(fruitlist)-1`. This is an index for all the elements of `fruitlist`, which you can change by simply assigning a new value to them. 


```python
# Making capital fruits.
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]

i = 0
while i < len(fruitlist):
    fruitlist[i] = fruitlist[i].upper()
    i += 1
print(fruitlist)    
```

    ['APPLE', 'BANANA', 'CHERRY', 'DURIAN', 'ORANGE']
    

---

## Lists and operators

Lists support the use of the operators `+` and `*`. These operators work similar as to how they work for strings. 

You can add two lists together with the `+` operator, the result of which is a list which contains the elements of both lists involved. Of course, you have to assign the result to a variable to store it.

You can multiply a list by an integer to create a list that contains the elements of the original list, repeated as often as the number indicates. This can be a fast approach to create a list with all equal elements.


```python
fruitlist = ["apple", "banana"] + ["cherry", "durian"]
print( fruitlist )

def multiply_list_by_ten(itemlist):
    return itemlist * 10
    
print(multiply_list_by_ten([0]))
print(multiply_list_by_ten(fruitlist))
```

    ['apple', 'banana', 'cherry', 'durian']
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ['apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian', 'apple', 'banana', 'cherry', 'durian']
    

Note: With the `+` you can add a list to another list, but you cannot add a new element to a list, unless you turn that new element into a list with a single element by putting two square brackets around it. If you try to add something to a list that is not a list, Python will try to interpret it as a list -- if it can do that (which it can, for instance, for a string, which it can consider a list of characters); it will then still do the addition but the result will not be what you want. For instance, the code below tries to add a "cherry" to a list, but only the second addition actually does what is intended.


```python
def add_to_list(fruitlist, item):
    fruitlist += item
    return fruitlist

print(add_to_list(["apple", "banana"], "cherry"))
print(add_to_list(["apple", "banana"], ["cherry"]))
```

    ['apple', 'banana', 'c', 'h', 'e', 'r', 'r', 'y']
    ['apple', 'banana', 'cherry']
    

---

## List methods

Python supports many methods to change lists or get information from them. You do not need to import a module to use them. Since they are methods, you call them using the syntax `<list>.<method>()`.

**Important!** Lists are mutable and these methods actually *change* the list! It is not as you are used to with string methods, where the methods create a new string, and return it, while the original string remains. Most list methods have an irrevocable effect on the list they work on. Usually they have no return value, and you do not need one either, as the purpose of the methods is to change the list.

### `append()`

`append()` attaches an item at the end of a list. You call the method with the item you wish to add as argument.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.append( "orange" )
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian']
    ['apple', 'banana', 'cherry', 'durian', 'orange']
    

An alternative for using the `append()` method is to add a list with one new element to the existing list with a `+`, and assign the resulting list to the original list variable. However, the `append()` method is preferable as it is more readable. `<list>.append(<element>)` is equivalent to `<list>[len(<list>):] = [<element>]`, or simply `<list> += [<element>]`.

### `extend()`

`extend()` makes a list longer by appending the elements of another list at the end. You call the method with the list of which you want to add the elements as argument.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.extend( ["raspberry", "elderberry", "strawberry", "blueberry"] )
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian']
    ['apple', 'banana', 'cherry', 'durian', 'raspberry', 'elderberry', 'strawberry', 'blueberry']
    

Just as with the `append()` method, you can extend an existing list with a new list by simply using the `+` operator, and assigning the result to the original list variable. And just as with the `append()` method, using the `extend()` method is preferable. `<list>.extend(<addlist>)` is equivalent to `<list>[len(<list>):] = <addlist>`.

### `insert()`

`insert()` allows you to insert an element at a specific position in a list. It is called with two arguments, the first being the index of the location where you wish to insert the new element, and the second the new element itself. To insert an element at the front of the list, you can use index 0. When using this, keep in mind that the index of the elements after your insertion change!


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.insert( 2, "orange" )
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian']
    ['apple', 'banana', 'orange', 'cherry', 'durian']
    

`<list>.insert(<index>,<element>)` is equivalent to `<list>[<index>:<index>] = [<element>]`.

### `remove()`

`remove()` allows you to remove an element from a list. The element you wish to remove is given as argument. If the element occurs in the list multiple times, only the first occurrence will be removed. If you try to remove an element that is not on the list, a runtime error is generated. 


```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist )
fruitlist.remove( "banana" )
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'banana', 'durian']
    ['apple', 'cherry', 'banana', 'durian']
    

### `pop()`

Like `remove()`, `pop()` removes an element from the list, but does so by index. It has one optional argument, which is the index of the element that you wish to remove. If you do not provide that argument, `pop()` removes the last element from the list. If the index is beyond the boundaries of the list, `pop()` generates a runtime error.

A major difference with `remove()` is that `pop()` actually has a return value, namely the element that gets removed. This allows you to quickly process all the elements of a list, while emptying the list at the same time.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
print( fruitlist.pop() )
print( fruitlist )
print( fruitlist.pop( 0 ) )
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'durian']
    durian
    ['apple', 'banana', 'cherry']
    apple
    ['banana', 'cherry']
    

### `del`

`del` is neither a method nor a function, but since it is often metioned in one breath with `remove()` and `pop()`, I place it here. `del` is a keyword that allows you to delete a list element, or list slice, by index. It is similar to `pop()` in functionality, but does not have a return value. Also, `pop()` cannot be used on slices. To use `del`, use the statement `del <list>[<index>]` or `del <list>[<index1>:<index2>]`.


```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist )
del fruitlist[3] 
print( fruitlist )
```

    ['apple', 'banana', 'cherry', 'banana', 'durian']
    ['apple', 'banana', 'cherry', 'durian']
    

### `index()`

`index()` returns the index of the first occurrence on the list of the element that is given to `index()` as argument. A runtime error is generated if the element is not found on the list.


```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist.index( "banana" ) )
```

    1
    

### `count()`

`count()` returns an integer that indicates how often the element that is passed to it as an argument occurs in the list.


```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist.count( "banana" ) )
```

    2
    

### ``sort()``

`sort()` sorts the elements of the list, from low to high. If the elements of the list are strings, it does an alphabetical sort. If the elements are numbers, it does a numeric sort. If the elements are mixed, it generates a runtime error, unless certain arguments are given.


```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort()
print( fruitlist )

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort()
print( numlist )
```

    ['apple', 'banana', 'banana', 'blueberry', 'cherry', 'durian', 'raspberry', 'strawberry']
    [129, 246, 314, 315, 642, 999]
    

To do a reverse sort, you can add an argument `reverse=<boolean>`.


```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( reverse=True )
print( fruitlist )
```

    ['strawberry', 'raspberry', 'durian', 'cherry', 'blueberry', 'banana', 'banana', 'apple']
    

Another argument that you can give `sort()` is a key. You have to provide this argument as `<list>.sort( key=<key> )`, whereby `<key>` is a function that takes one argument (the element that is to be sorted) and returns a value that is used as key. A typical use for the `key` argument is if you want to sort a list of strings, but want to do the sorting case-insensitively. So as key you want to use the elements, but in lower case, i.e., you want to apply the function `str.lower()` to the element. You call the sort as in the following example:


```python
fruitlist = ["apple", "Strawberry", "banana", "raspberry", "CHERRY", "banana", "durian", "blueberry"]
fruitlist.sort() 
print( fruitlist )
fruitlist.sort( key=str.lower ) # case-insensitive sort
print( fruitlist )
```

    ['CHERRY', 'Strawberry', 'apple', 'banana', 'banana', 'blueberry', 'durian', 'raspberry']
    ['apple', 'banana', 'banana', 'blueberry', 'CHERRY', 'durian', 'raspberry', 'Strawberry']
    

Note that for the key argument, you do not place parentheses after the function name. This is not a function call, it is an argument that tells Python which function to use to generate the key.

You can write your own function to be used as key. For example, in the code below, `numlist` is sorted with the last digit of each number as the most important digit, followed by the middle digit:


```python
def revertdigits( element ):
    return (element%10)*100 + (int( element/10 )%10)*10 + int( element/100 )

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort( key=revertdigits )
print( numlist )
```

    [642, 314, 315, 246, 129, 999]
    

Here is another example, that sorts a list of strings by string length, followed by alphabetical order:


```python
def len_alphabetical( element ):
    return len( element ), element 

fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=len_alphabetical )
print( fruitlist )
```

    ['apple', 'banana', 'banana', 'cherry', 'durian', 'blueberry', 'raspberry', 'strawberry']
    

At this point we can give a typical example of the use of "anonymous functions". Using an anonymous function to specify the key for the `sort()` method keeps the code for the key next to where you call the `sort()`, instead of elsewhere in the program. This may improve readability.


```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=lambda x: (len(x),x) )
print( fruitlist )
```

    ['apple', 'banana', 'banana', 'cherry', 'durian', 'blueberry', 'raspberry', 'strawberry']
    

### `reverse()`

`reverse()` simply reverses the elements of the list.


```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.reverse()
print( fruitlist )
```

    ['blueberry', 'durian', 'banana', 'cherry', 'raspberry', 'banana', 'strawberry', 'apple']
    

### Practice

**Exercise**: Sort a list of numbers using their absolute values.


```python
# Sorting with absolute values.
numlist = [-10, -7, -3, -2, 0, 1, 2, 5, 7, 8, 10]
numlist.sort(key=lambda x: abs(x))
print(numlist)
```

    [0, 1, -2, 2, -3, 5, -7, 7, 8, -10, 10]
    

**Exercise**: Count how often each letter occurs in a string (case-insensitively). You can ignore every character that is not a letter. Of course, you should not introduce 26 variables to do this; instead, use a list of 26 items that all start at zero. Print the resulting counts. As index for the list you can use `ord(letter) - ord("a")`, where letter is a lower case letter (the `ord()` function is explained in the strings chapter).


```python
# Letter counting.
text = """Now, it's quite simple to defend yourself against a man armed
with a banana. First of all you force him to drop the banana; then, 
second, you eat the banana, thus disarming him. You have now rendered 
him helpless."""

abc_count_list = [0]*26
#print(abc)
for c in text:
    index = ord(c.lower()) - ord("a")
    #print(f'index = {index} - {index >= 26 or index < 0}')
    if index >= 26 or index < 0:
        #print(f'c = {c} - order = {ord(c.lower())} - count = 0')
        continue
    else:
        #print(f'c = {c} - order = {ord(c.lower())} - count = {abc_count_list[index]}')
        abc_count_list[index] = abc_count_list[index] + 1 
        #print(f'count = {abc_count_list[index]}')
        
    #print('--------------------------------------------')

for i in range(len(abc_count_list)):
    #print(f'i = {i} - {i % 4}')
    if i % 5 == 4:
        print(f'{abc_count_list[i]:{2}} {chr(ord("a")+i)}')        
    else:
        print(f'{abc_count_list[i]:{2}} {chr(ord("a")+i)}', end = ' | ')
```

    19 a |  3 b |  2 c |  8 d | 18 e
     5 f |  2 g | 10 h | 11 i |  0 j
     0 k |  6 l |  7 m | 15 n | 12 o
     3 p |  1 q |  8 r | 10 s | 12 t
     6 u |  1 v |  3 w |  0 x |  4 y
     0 z | 


```python
# Letter counting.
text = """Now, it's quite simple to defend yourself against a man armed
with a banana. First of all you force him to drop the banana; then, 
second, you eat the banana, thus disarming him. You have now rendered 
him helpless."""

# Version 2:
abc_count_list = [0]*26
#print(abc_count_list)
start = ord("a")
#print(f'start = {start}')

for i in range(len(abc_count_list)):
    #print(f'i = {i} - ord = {i + start} - char = {chr(i + start)}')
    count = text.count(chr(i + start))
    #print(f'count = {count}')
    #print('--------------------------------')
    if (i) % 5 == 4:
        print(f'{count:{2}} {chr(i + start)}')        
    else:
        print(f'{count:{2}} {chr(i + start)}', end = ' | ')
```

    19 a |  3 b |  2 c |  8 d | 18 e
     4 f |  2 g | 10 h | 11 i |  0 j
     0 k |  6 l |  7 m | 14 n | 12 o
     3 p |  1 q |  8 r | 10 s | 12 t
     6 u |  1 v |  3 w |  0 x |  3 y
     0 z | 

---

## Aliasing

If you assign a variable that contains a list to another variable, you might expect that you create a copy of the list in the second variable. But you are not doing that. You are actually creating an *alias* for the list, i.e., a new variable that is referring to the same list. This means that the new variable can be treated as a list, but any change that you make to the list it refers to, is visible in the original list variable, and vice versa. They are not different lists.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
print( fruitlist )
print( newfruitlist )
newfruitlist[2] = "orange"
print( fruitlist )
print( newfruitlist )
```

    ['apple', 'banana', 'cherry', 'durian']
    ['apple', 'banana', 'cherry', 'durian']
    ['apple', 'banana', 'orange', 'durian']
    ['apple', 'banana', 'orange', 'durian']
    

Every variable in Python has an identification number. You can see it with the `id()` function. The ID number indicates which memory spot the variable refers to. For an alias of a list, the ID is the same as for the original list.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
print( id( fruitlist ) )
print( id( newfruitlist ) )
```

    1714861209152
    1714861209152
    

If you want to create a copy of a list, you can do so using a little trick. Instead of using `<newlist> = <oldlist>`, you use the command `<newlist> = <oldlist>[:]`.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( id( fruitlist ) )
print( id( newfruitlist ) )
print( id( verynewfruitlist ) )

fruitlist[2] = "orange"
print( fruitlist )
print( newfruitlist )
print( verynewfruitlist )
```

    1714861389952
    1714861389952
    1714862332608
    ['apple', 'banana', 'orange', 'durian']
    ['apple', 'banana', 'orange', 'durian']
    ['apple', 'banana', 'cherry', 'durian']
    

### `is`

The keyword `is` is introduced to compare the identities of two variables.


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( fruitlist is newfruitlist )
print( fruitlist is verynewfruitlist )
print( newfruitlist is verynewfruitlist )
```

    True
    False
    False
    

As you can see, the keyword `is` manages to determine that `fruitlist` and `newfruitlist` are aliases, but that `verynewfruitlist` is not the same list. If you compare them with the `==` operator, the results are not the same as comparing them with `is`:


```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( fruitlist == newfruitlist )
print( fruitlist == verynewfruitlist )
print( newfruitlist == verynewfruitlist )
```

    True
    True
    True
    

The `==` operator actually compares the contents of the lists, so it returns `True` for all comparisons. For data types for which `==` is not defined, it executes an identity comparison, but for lists it has been defined as a comparison of the contents.

### Shallow vs. deep copies

If (some of) the items of your list are lists themselves (or other mutable data structures which are introduced in the next chapters), copying the list using the `<newlist> = <oldlist>[:]` syntax may give problems. The reason is that such a copy is a "shallow copy", which means that it copies each of the elements of the list with a regular assignment, which entails that the items in the list that are lists themselves become aliases of the items on the original list.


```python
numlist = [ 1, 2, [3, 4] ]
copylist = numlist[:]

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

    [5, 2, [6, 4]]
    [1, 2, [6, 4]]
    

In the code above, you can see that the assignment `numlist[0] = 5` only has an effect on `numlist`, as `copylist` contains a copy of numlist. However, since this is a shallow copy, the assignment to `numlist[2][0]` has an effect on both lists, as the sublist `[3, 4]` is stored in `copylist` as an alias.

If you want to create a "deep copy" of a list (i.e., a copy that also contains true copies of all mutable substructures of the list, which in turn contain true copies of all their mutable substructures, etcetera), then you can use the `copy` module for that. The `deepcopy()` function from the copy module allows you to create deep copies of any mutable data structure.


```python
from copy import deepcopy

numlist = [ 1, 2, [3, 4] ]
copylist = deepcopy( numlist )

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

    [5, 2, [6, 4]]
    [1, 2, [3, 4]]
    

Note that the `copy` module also contains a function `copy()` that makes shallow copies. If you wonder why that function is included as you can easily create shallow copies of lists with the `<newlist> = <oldlist>[:]` command: the `copy` module not only works for lists, but for any mutable data structure. Not for all such data structures there exist shortcuts to create shallow copies. 

### Passing lists as arguments

When you pass a list as an argument to a function, this is a "pass by reference". The parameter that the function has access to will be an alias for the list that you pass. This means that a function that you pass a list to, can actually change the contents of the list.

This is important, so I repeat it: when you pass a mutable data structure to a function, this is a "pass by reference", meaning that the data structure is passed as an alias and the function can change the contents of the data structure.

You have to know whether a function that you pass a list to will or will not change the list. If you do not want the function to change the list, and you do not know if it will, you best pass a deep copy of the list to the function.


```python
def changelist( x ):
    if len( x ) > 0:
        x[0] = "CHANGE!"
        
fruitlist = ["apple", "banana", "cherry", "durian"]
changelist( fruitlist )
print( fruitlist )
```

    ['CHANGE!', 'banana', 'cherry', 'durian']
    

The reason that a list is "passed by reference" and not "by value" is that technically, every argument that is passed to a function must be stored in the computer in a specific block of memory that is part of the processor. This is called the "stack", and it is pretty limited in size. Since lists can be really long, allowing a program to place a list on the stack would cause all kinds of annoying runtime errors. In Python, as in most other programming languages, for the most part only basic data types (such as integers, floats, and strings) are passed by value.

Some languages, such as Matlab, prefer to copy the list in memory, which prevents this kind of behavior. However, Matlab is nearly famous for running out of memory while doing relatively simple things.

---

## Nested lists

The elements of a list may be lists themselves (which also may contains lists, etcetera). This is a good way to create a matrix in a program. For instance, you can create a Tic-Tac-Toe board, where a dash (`-`) represents an empty cell, as follows:


```python
board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
```

The first row of the board is represented by `board[0]`, the second row by `board[1]`, and the third row by `board[2]`. If you want to access the first cell of the first row, that is `board[0][0]`, the second cell is `board[0][1]` and the third cell is `board[0][2]`.

For example, the following code places an "X" in the middle of the board, and an "O" in the upper right corner. It also displays the board in a nice way (with markers for rows and columns around it).


```python
def display_board( b ):
    print( "  1 2 3" )
    for row in range( 3 ):
        print( row+1, end=" ")
        for col in range( 3 ):
            print( b[row][col], end=" " )
        print()
           
board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
board[1][1] = "X"
board[0][2] = "O"
display_board( board )
```

      1 2 3
    1 - - O 
    2 - X - 
    3 - - - 
    

---

## List casting

You can type cast a sequence of elements to a list using the `list()` function.


```python
t1 = ( "apple", "banana", "cherry" )
print( t1 )
print( type( t1 ) )
fruitlist = list( t1 )
print( fruitlist )
print( type( fruitlist ) )
```

    ('apple', 'banana', 'cherry')
    <class 'tuple'>
    ['apple', 'banana', 'cherry']
    <class 'list'>
    

This is sometimes necessary, in particular when you have an "iterator" available and you want to use the elements in a list format. An iterator is a function that generates a sequence. An example of an iterator that I already discussed is the `range()` function. The `range()` function generates a sequence of numbers. If you want to use these numbers as a list, you can use list casting.

Also, note that t1 is a 'tuple', which is a very flexile (and complex to use) way to store list-like data. If you can use a list, use a list.


```python
numlist = range( 1, 11 )
print( numlist )
numlist = list( range( 1, 11 ) )
print( numlist )
```

    range(1, 11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

You can turn a string into a list of its characters by using a list casting on the string.

---

## List comprehensions

List comprehensions are a concise way to create lists. They are typical for Python, but you do not find them in many other programming languages. They are not actually needed, as you can use functions to achieve the same effect, but as they are often used in examples (especially by people who want to show off their Python abilities to create short statements that have extensive effects), but it is prudent to discuss them.

Suppose that you want to create a list consisting of the squares of the numbers 1 to 25. A function that creates such a list is:


```python
def squareslist():
    squares = []
    for i in range( 1, 26 ):
        squares.append( i*i )
    return squares

sl = squareslist()
print( sl )
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]
    

In Python, you can create that list with one single statement, namely as follows:


```python
sl = [ x*x for x in range( 1, 26 )]
print( sl )
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]
    

Now suppose that you want to create this list, but want to leave out (for some reason) the squares of any numbers that end in 5. That would add at least two lines to the function above, but with list comprehensions you can still do it with that single line:


```python
sl = [ x*x for x in range( 1, 26 ) if x%10 != 5]
print( sl )
```

    [1, 4, 9, 16, 36, 49, 64, 81, 100, 121, 144, 169, 196, 256, 289, 324, 361, 400, 441, 484, 529, 576]
    

A list comprehension consists of an expression in square brackets, followed by a `for` clause, followed by zero or more `for` and/or `if` clauses. The result is a list that contains the elements that result from evaluating the expression for the combination of the `for` and `if` clauses.

The results can become quite complex. For instance, here is a list comprehension that creates a list of tuples with three integers between 1 and 4, whereby the three integers are all different:


```python
triplelist = [ (x,y,z) for x in range( 1, 5 ) for y in range( 1, 5 ) for z in range( 1, 5 ) 
              if x != y if x != z if y != z]
print( triplelist )
```

    [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 1, 2), (3, 1, 4), (3, 2, 1), (3, 2, 4), (3, 4, 1), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)]
    

If you find list comprehensions hard to use, remember that there is absolutely no reason to use them except for keeping code concise, and that keeping code readable and understandable is far more important than keeping it concise. If you find list comprehensions more intuitive, keep in mind not everybody does so!

---

## What you learned

In this chapter, you learned about:

- Lists
- Mutability of lists
- Using `+` and `*` with lists
- List methods `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, and `reverse()`
- `del` with lists
- Aliasing
- The keyword `is`
- Creating list copies
- Creating deep copies of lists using `deepcopy()`
- Using lists as arguments
- Nested lists
- List casting
- List comprehensions

-------------

## Exercises

### Exercise 12.1

A playing card consists of a suit ("Hearts", "Spades", "Clubs", or "Diamonds") and a value ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"). Write a function that creates and returns a list of all possible playing cards, which is a deck. Then create a function that shuffles the deck, producing a random order.


```python
#Creating a deck.
def make_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    cards = []
    for s in suits:
        #print(f's = {s}')
        for v in values:
            #print(f'v = {v}')
            card = v + ' ' + s
            #print(f'card = {card}')
            cards.append(card)
            #print(f'cards = {cards}')
            #print('---------------')
        #print('=====================')
    return cards #a list that represents a deck
deck = make_deck()
print(deck)
```

    ['Ace Hearts', '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts', 'Jack Hearts', 'Queen Hearts', 'King Hearts', 'Ace Spades', '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 'Jack Spades', 'Queen Spades', 'King Spades', 'Ace Clubs', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'Jack Clubs', 'Queen Clubs', 'King Clubs', 'Ace Diamonds', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'Jack Diamonds', 'Queen Diamonds', 'King Diamonds']
    


```python
from random import seed, randint

# Shuffling a deck.
## Version 1:
def shuffle_deck(deck):
    seed(52)
    for i in range(len(deck)):
        #print(f'i = {i}')
        j = randint(0,len(deck))
        #print(f'j = {j}')
        #print(f'deck[i] = {deck[i]}')
        #print(f'deck[j] = {deck[j]}')
        card1 = deck[i]
        card2 = deck[j]        
        deck[i] = card2
        deck[j] = card1
        #print(f'deck[i] = {deck[i]}')
        #print(f'deck[j] = {deck[j]}')
        #print('----------------------------------')
    return deck #shuffle the deck in a random order
deck1 = make_deck()
print(shuffle_deck(deck1))
```

    ['9 Spades', '4 Hearts', '10 Clubs', '7 Clubs', '6 Hearts', 'King Clubs', 'Ace Clubs', '6 Spades', '6 Diamonds', '7 Diamonds', 'King Spades', '10 Hearts', '7 Hearts', '10 Spades', '2 Clubs', 'Ace Spades', '5 Spades', '4 Clubs', '9 Clubs', 'Queen Spades', '2 Spades', '4 Spades', '2 Diamonds', '3 Diamonds', 'Queen Clubs', '3 Hearts', '8 Clubs', '3 Clubs', '3 Spades', '8 Hearts', '6 Clubs', '2 Hearts', 'Jack Diamonds', 'Queen Hearts', '5 Diamonds', 'Ace Hearts', 'Jack Clubs', 'King Diamonds', 'Jack Spades', 'Ace Diamonds', '7 Spades', '4 Diamonds', '10 Diamonds', '8 Diamonds', '9 Hearts', 'Queen Diamonds', '8 Spades', '5 Hearts', '5 Clubs', '9 Diamonds', 'Jack Hearts', 'King Hearts']
    


```python
from random import seed, shuffle

# Shuffling a deck.
## Version 2:
def shuffle_deck(deck):    
    seed(52)
    shuffle(deck)
    return deck #shuffle the deck in a random order
deck2 = make_deck()
print(shuffle_deck(deck2))
```

    ['Ace Diamonds', '3 Diamonds', '8 Clubs', 'King Spades', '7 Spades', '10 Hearts', '10 Diamonds', '5 Hearts', '4 Spades', '4 Diamonds', '2 Spades', '7 Hearts', '9 Spades', 'King Diamonds', '10 Clubs', '2 Diamonds', '6 Spades', '9 Diamonds', 'King Hearts', '2 Hearts', 'Queen Diamonds', 'Ace Spades', 'Jack Diamonds', '2 Clubs', '5 Diamonds', '8 Spades', '8 Hearts', '6 Clubs', '4 Clubs', '6 Hearts', 'Jack Clubs', '3 Spades', 'Queen Clubs', 'King Clubs', 'Queen Spades', '9 Clubs', '6 Diamonds', 'Ace Hearts', '3 Clubs', '10 Spades', 'Queen Hearts', '7 Diamonds', 'Jack Hearts', '9 Hearts', '3 Hearts', 'Ace Clubs', 'Jack Spades', '5 Clubs', '7 Clubs', '8 Diamonds', '4 Hearts', '5 Spades']
    

### Exercise 12.2

Count how often each letter occurs in a string (case-insensitively). You can ignore every character that is not a letter. Print the letters with their counts, in order from highest count to lowest count.


```python
# Letter counting.
def print_letter_counts(text):
    #count and print how many times each letter appears in text
    abc = [chr(x) for x in range(ord("a"), ord("z")+1)]
    abc.sort(key=lambda x: -text.count(x))
    result_list = []
    for char in abc:
        char_count = str(text.count(char)) + ' ' + char
        result_list.append(char_count)
    return result_list

text = '=-abcdefsssssssghijklm,"nopqrsttuvtwxy.abcdefgfhijklmabcdabbavwxyvwxyvwxyvwxyvwxyvwxyxyxyxyxyxyxyxyxxxxxxxx'
print_letter_counts(text)
```




    ['22 x',
     '14 y',
     '8 s',
     '7 v',
     '7 w',
     '5 a',
     '5 b',
     '3 c',
     '3 d',
     '3 f',
     '3 t',
     '2 e',
     '2 g',
     '2 h',
     '2 i',
     '2 j',
     '2 k',
     '2 l',
     '2 m',
     '1 n',
     '1 o',
     '1 p',
     '1 q',
     '1 r',
     '1 u',
     '0 z']



### Exercise 12.3

The sieve of Eratosthenes is a method to find all prime numbers between 1 and a given number using a list. This works as follows: Fill the list with the sequence of numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime. Now loop over the list. Find the next number on the list that is not zero, which, at the start, is the number 2. Now set all multiples of this number to zero. Then find the next number on the list that is not zero, which is 3. Set all multiples of this number to zero. Then the next number, which is 5 (because 4 has already been set to zero), and do the same thing again. Process all the numbers of the list in this way. When you have finished, the only numbers left on the list are primes. Use this method to determine all the primes between 1 and 100.


```python
# Eratosthenes.
def eratosthenes(max_number):
    full_list = list(range(1, max_number+1))
    #print(full_list)
    
    prime_list = []
    full_list[0] = 0
    
    for i in full_list:
        #print(f'i = {i}')
        if i == 0:
            #print('+++++++++++++++++++++++++++++++++')
            continue
        else:
            non0 = i
            prime_list.append(non0)
            #print(f'non0 = {non0}')
            #print(f'prime_list = {prime_list}')
            #print(f'remain_list = {full_list[i:max_number]}')
            #print(f'full_list = {full_list}')
            for j in range(i,max_number):
                #print(f'  j = {j}')
                #print(f'  full_list[j] = {full_list[j]}')
                if full_list[j] % i == 0 and full_list[j] != 0:
                    full_list[j] = 0
                    #print(f'  #################################    changed full_list[j] = {full_list[j]}')
                #print(f'  {full_list}')
                #print('===================================')
        #print('*****************************')
    return prime_list #a list of prime numbers lower than max_number, using the Eratosthenes technique.

print(eratosthenes(100))
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    

### Exercise 12.4

Write a function that receives a list with numbers and returns this list without numbers higher or equal than 10. For instance, for the list `[1, 1, 32, 3, 5, 8, 10, 13, 21, 34, 55, 89]` the resulting list is `[1,1,3,5,8]`.


```python
def remove_numbers_higher_than_ten(numbers):
    new_list = numbers.copy()
    for element in numbers:
        #print(f'element = {element}')
        if element >= 10:
            new_list.remove(element)
    return new_list #a list without number higher or equal than 10

numbers = [1, 1, 32, 3, 5, 8, 10, 13, 21, 34, 55, -89, 1, 1, 32, 3, 5, 8, -10]
print(remove_numbers_higher_than_ten(numbers))
```

    [1, 1, 3, 5, 8, -89, 1, 1, 3, 5, 8, -10]
    

---

## Python 2

In Python 2, sorting a mixed list does not give a runtime error. The `sort()` function also supports an argument `cmp=<function>`, that allows you to specify a function that does the comparison between two elements. This function is no longer supported in Python 3, but you can use the `key` parameter for the same purpose. In the Python module `functools` a function `cmp_to_key()` is found that turns the old-style `cmp` specification into the new-style `key` specification.

In Python 2, the `range()` function produces an actual list, and you do not need list casting to turn the result of it into one.

--------

End of Chapter 12. 
