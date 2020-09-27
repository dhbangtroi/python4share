# Chapter 10 - Strings

---

Until now, most examples and exercises have been using numbers. Typical students for whom this course is intended  start wondering by this time if programming is just for number manipulation. In daily life, it is far more commonplace to deal with textual information. So are they ever going to learn how to deal with text?

The reason that dealing with text was postponed until this point, is that dealing with numbers is simply easier than dealing with text. But in the present chapter, the first steps are taken to learn to manipulate textual information.

Text, in programming languages, is dealt with in the form of strings. This chapter is on the details of strings, and on readily-available functions to juggle them.

---

## Recapsulation of string discussions until now

In Chapter 4, strings were quickly introduced. The brief discussion in that chapter ended with the statement that a string is a text, enclosed by either single or double quotes, which might be of any length, including zero. The chapter also explained that you can concatenate two strings using `+`, and that you can create a string that is the repetition of a shorter string by using `*`. For example:


```python
s1 = "apple"
s2 = 'banana'

def print_variations(s1,s2):
    print( s1 )
    print( s2 )
    print( s1 + s2 )
    print( 3 * s1 )
    print( s2 * 3 )
    print( 2 * s1 + 2 * s2 )
    
print_variations(s1,s2)
```

    apple
    banana
    applebanana
    appleappleapple
    bananabananabanana
    appleapplebananabanana
    

You also learned how to get the length of a string using the `len()` function. String comparisons were explained in Chapter 7, in particular the fact that the comparison operators compare strings using alphabetical rules, whereby capitals are always lower in the alphabet than lower case letters. This will be explained more in-depth in the present chapter. Chapter 7 also explained how the `in` operator can be used to test the presence of characters or substrings in strings.

Chapter 8 explained how you can use a `for` loop to traverse all the characters in a string, and Chapter 9 introduced the `format()` function to format strings.



```python
word1 = "orange"
word2 = "banana"

def shared_letters(s1,s2):
    for letter in s1:
        if letter in s2:
            return( s1 + " and " + s2 + " share the letter " + letter )

print(shared_letters(word1,word2))
```

    orange and banana share the letter a
    

---

## Multi-line strings

Strings in Python may span across multiple lines. This can be useful when you have a very long string, or when you want to format the output of the string in a certain way. Multi-line strings can be achieved in two ways:

1. With single or double quotes, and an indication that the remainder of the string continues on the next line with a backslash.
2. With triple single or double quotes.

I first demonstrate how this works when you use the regular string enclosure with one double or single quote at each end of the string:


```python
longString = "I'm fed up with being treated like sheep. \
What's the point of going abroad if you're just another \
tourist carted around in buses surrounded by sweaty \
mindless oafs from Kettering and Coventry in their \
cloth caps and their cardigans and their transistor \
radios and their Sunday Mirrors, complaining about \
the tea - 'Oh they don't make it properly here, do they, \
not like at home' - and stopping at Majorcan bodegas \
selling fish and chips and Watney's Red Barrel and \
calamaris and two veg and sitting in their cotton frocks \
squirting Timothy White's suncream all over their puffy \
raw swollen purulent flesh 'cos they 'overdid it on the first day.'"
print( longString )
```

    I'm fed up with being treated like sheep. What's the point of going abroad if you're just another tourist carted around in buses surrounded by sweaty mindless oafs from Kettering and Coventry in their cloth caps and their cardigans and their transistor radios and their Sunday Mirrors, complaining about the tea - 'Oh they don't make it properly here, do they, not like at home' - and stopping at Majorcan bodegas selling fish and chips and Watney's Red Barrel and calamaris and two veg and sitting in their cotton frocks squirting Timothy White's suncream all over their puffy raw swollen purulent flesh 'cos they 'overdid it on the first day.'
    

As you can see, Python now interprets this example as a single line of text. The backslash (`\`) can actually be included after any Python statement to indicate that it continues on the next line, and it can be quite useful for that, for instance when you write long calculations.

The recommended way to write multi-line strings in Python is, however, to use triple double or single quotes. I indicated earlier that you can use those to write multi-line comments. Such comments are basically large strings in the middle of your Python program, which do nothing as they are not assigned to a variable.

Here is an example of a long string with triple double quotes:


```python
longString = """And being herded into endless Hotel Miramars and Bellevueses 
and Continentales with their modern international luxury 
roomettes and draught Red Barrel and swimming pools full 
of fat German businessmen pretending they're acrobats forming 
pyramids and frightening the children and barging into queues 
and if you're not at your table spot on seven you miss the 
bowl of Campbell's Cream of Mushroom soup, the first item on 
the menu of International Cuisine, and every Thursday night 
the hotel has a bloody cabaret in the bar, featuring a tiny 
emaciated dago with nine-inch hips and some bloated fat tart 
with her hair brylcreemed down and a big arse presenting 
Flamenco for Foreigners."""
print( longString )
```

    And being herded into endless Hotel Miramars and Bellevueses 
    and Continentales with their modern international luxury 
    roomettes and draught Red Barrel and swimming pools full 
    of fat German businessmen pretending they're acrobats forming 
    pyramids and frightening the children and barging into queues 
    and if you're not at your table spot on seven you miss the 
    bowl of Campbell's Cream of Mushroom soup, the first item on 
    the menu of International Cuisine, and every Thursday night 
    the hotel has a bloody cabaret in the bar, featuring a tiny 
    emaciated dago with nine-inch hips and some bloated fat tart 
    with her hair brylcreemed down and a big arse presenting 
    Flamenco for Foreigners.
    

The interesting difference between these two examples is that in the first example, the string was interpreted as one long, continuous series of characters, while in the second example the different lines are all printed on different lines on the output. The reason that this happens is that there is an invisible character included at the end of each line in the second example that indicates that Python should move to the next line before continuing. This is the so-called "newline" character, and you can actually insert it explicitly into a string, using the code "`\n`". So this code should not be read as two characters, the backslash and the "n", but as a single newline character. By using it, you can ensure that you print the output on multiple lines, even if you use the backslash to indicate the continuation of the string, as was done in the first example. For example:


```python
longstring = "And then some adenoidal typists from Birmingham with flabby\n\
white legs and diarrhoea trying to pick up hairy bandy-legged\n\
wop waiters called Manuel and once a week there's an excursion\n\
to the local Roman Ruins to buy cherryade and melted ice cream\n\
and bleeding Watney's Red Barrel and one evening you visit the\n\
so called typical restaurant with local colour and atmosphere\n\
and you sit next to a party from Rhyl who keep singing\n\
'Torremolinos, torremolinos' and complaining about the food -\n\
'It's so greasy here, isn't it?' - and you get cornered by some\n\
drunken greengrocer from Luton with an Instamatic camera and\n\
Dr. Scholl sandals and last Tuesday's Daily Express and he\n\
drones on and on and on about how Mr. Smith should be running\n\
this country and how many languages Enoch Powell can speak and\n\
then he throws up over the Cuba Libres."
print( longstring )
```

    And then some adenoidal typists from Birmingham with flabby
    white legs and diarrhoea trying to pick up hairy bandy-legged
    wop waiters called Manuel and once a week there's an excursion
    to the local Roman Ruins to buy cherryade and melted ice cream
    and bleeding Watney's Red Barrel and one evening you visit the
    so called typical restaurant with local colour and atmosphere
    and you sit next to a party from Rhyl who keep singing
    'Torremolinos, torremolinos' and complaining about the food -
    'It's so greasy here, isn't it?' - and you get cornered by some
    drunken greengrocer from Luton with an Instamatic camera and
    Dr. Scholl sandals and last Tuesday's Daily Express and he
    drones on and on and on about how Mr. Smith should be running
    this country and how many languages Enoch Powell can speak and
    then he throws up over the Cuba Libres.
    

This means that if you do not want automatic newline characters inserted into a multi-line string, you have to use the first approach, with the backslash at the end of the line. If you are okay with newline characters in your multi-line string, the second approach is probably the easiest to read.

---

## Escape sequences

"`\n`" is a so-called "escape sequence". An escape sequence is a string character written as a backslash followed by a code, which can be one or multiple characters. Python interprets escape sequences in a string as a special character; a control character.


```python
word1 = "orange"
word2 = "banana"

def add_newline_between_words(word1,word2):
    new_line = word1 + "\n" + word2
    return(new_line)
    
print(add_newline_between_words(word1,word2))
```

    orange
    banana
    

Besides the newline character there are more special characters "`\'`" and "`\"`", which can be used to place a single respectively double quote in a string, regardless of what characters surround the string. I also mentioned that you can use "`\\`" to insert a "real" backslash in a string. 

There are a few more "backslash sequences" which lead to a special character. Most of these are archaic and you do not need to worry about them. The one I want to mention are "`\t`" which represents a single tabulation (also known as the 'tab').


```python
def place_word_between_single_quotes(w1):
    new_line = '\'' + word1 + '\''
    return(new_line)
print(place_word_between_single_quotes(word1))

def place_word_between_double_quotes(w1):
    new_line = '\"' + word1 + '\"'
    return(new_line)
print(place_word_between_double_quotes(word1))
```

    'orange'
    "orange"
    

Extra information for students who want to know more, but not necessary for this course:

There is another character "`\xnn`" whereby `nn` stands for two hexadecimal digits, which represents the character with hexadecimal number `nn`. For example, "`\x20`" is the character expressed by the hexadecimal number `20`, which is the same as the decimal number `32`, which is the space (this will be explained later in this chapter).

In case you never learned about hexadecimal counting: hexadecimals use a numbering scheme that uses 16 different digits. We use ten (`0` to `9`), binary uses two (`0` to `1`), and hexidecimal then uses `0` to `9` and then continues from `A` to `F`. A direct translation from hexadecimals to decimals turns `A` into `10`, `B` into `11`, etcetera. In decimal counting, the value of a multi-digit number is found by multiplying the digits by increasing powers of `10`, from right to left, e.g., the number `1426` is `6 + 2*10 + 4*100 + 1*1000`. For hexadecimal numbers you do the same thing, but multiply by powers of `16`, e.g., the hexadecimal number `4AF2` is `2 + 15*16 + 10*256 + 4*4096`. Programmers tend to like hexadecimal numbers, as computers work with bytes as the smallest unit of memory storage, and a byte can store 256 different values, i.e., any byte value can be expressed by a hexadecimal number of two digits. 

---

## Accessing characters of a string

As I showed several times before, a string is a collection of characters in a specific order. You can access the individual characters of a string using indices.

### String indices

Each symbol in a string has a position, this position can be referred to by the index number of the position. The index numbers start at 0 and then increase to the length of the string. The following table shows the word "orange" in the first row and the indices for each letter in the second and third rows:

&nbsp;&nbsp;__`  o  r  a  n  g  e`__<br>
&nbsp;&nbsp;`  0  1  2  3  4  5`<br>
` -6 -5 -4 -3 -2 -1`

As you can see, you can use positive indices, which start at the first letter of the string and increase until the end of the string is reached, or negative indices, which start with -1 for the last letter of the string and decrease until the first letter of the string is reached.

As the length of a string `s` is `len(s)`, the last letter of the string has index `len(s)-1`. With negative indices, the first letter of the string has index `-len(s)`.

If a string is stored in a variable, the individual letters of the string can be accessed by the variable name and the index of the requested letter between square brackets (`[]`) next to it.


```python
fruit = "orange"

def print_indices(fruit,n):
    print(fruit[n])
print_indices(fruit,1 ) 
print_indices( fruit,2 ) 
print_indices( fruit,4 )
print_indices( fruit,-1 )
print_indices( fruit,-6 )
print_indices( fruit,-3 )
```

    r
    a
    g
    e
    o
    n
    

You can also use variables as indices, and even calculations or function calls. You must make sure, however, that calculations result in integers, because you cannot use floats as indices (think about this; what's at `fruit[2.9]`?. Below are some examples, most of which are so convoluted that implementation of these would be rare, at best. But they show what is possible.


```python
from math import sqrt

fruit = "orange"
x = 3

print_indices( fruit,3-2 )
print_indices( fruit,int( sqrt( 4 ) ))
print_indices( fruit,2**2)
print_indices( fruit,int( (x-len( fruit ))/3 ))
print_indices( fruit,-len( fruit ))
print_indices( fruit,-x )
```

    r
    a
    g
    e
    o
    n
    

In principle, you can also use an index with the actual string rather than a variable that contains it, e.g., `"orange"[2]` is the letter "a". For obvious reasons no one ever does that, though.

Besides using single indices you can also access a substring (also called a "slice") from a string by using two numbers between the square brackets with a colon (`:`) in between. The first of these numbers is the index where the substring starts, the second where it ends. The substring does *not* include the letter at the second index. By leaving out the left number you indicate that the substring starts at the beginning of the string (i.e., at index 0). By leaving out the right number you indicate that the substring ranges up to and includes the last character of the string.

If you try to access a character using an index that is beyond the reaches of a string, you get a runtime error ("index out of bounds"). For a range of indices to access substrings such limitations do not exist; you can use numbers that are outside the bounds of the string.


```python
fruit = "orange"
print( fruit[:] )
print( fruit[0:] )
print( fruit[:6] )
print( fruit[:100] )
print( fruit[:len( fruit )] )
print( fruit[1:-1] )
print( fruit[2], fruit[1:6] )
```

    orange
    orange
    orange
    orange
    orange
    rang
    a range
    

### Traversing strings

I already explained how you can traverse the characters of a string using a `for` loop:


```python
fruit = 'apple'

def traverse_characters(word):
    new_word = ""
    for char in word:
        new_word += ( char + ' - ' )
    return new_word
print(traverse_characters(fruit))
```

    a - p - p - l - e - 
    


Now you know about indices, you probably realize you can also use those to traverse the characters of a string:


```python
fruit = 'apple'

def traverse_characters2(word):
    new_word = ""
    for i in range( 0, len( word ) ):
        new_word += word[i] + " - "
    return new_word
    
def traverse_characters3(word):
    new_word = ""
    i = 0
    while i < len( word ):
        new_word += word[i] + " - "
        i += 1
    return new_word
print(traverse_characters2(fruit)+"\n"+traverse_characters3(fruit))
```

    a - p - p - l - e - 
    a - p - p - l - e - 
    

If you just want to traverse the individual characters of a string, the first method, using `for <character> in <string>:`, is by far the most elegant and readable. However, occasionally you have to solve problems in which you might prefer one of the other methods.

**Exercise**: Write code that for a string prints the indices of all of its vowels (`a`, `e`, `i`, `o`, and `u`). This can be done with a `for` loop or a `while` loop.


```python
# Vowel indices.
s = "And now for something completely different"
vowels = ('a', 'e', 'i', 'o', 'u')

for i in range(len(s)):
    if s[i].lower() in vowels:
        print(i)
```

    0
    5
    9
    13
    15
    18
    23
    27
    29
    34
    37
    39
    

**Exercise**: Write code that uses two strings. For each character in the first string that has exactly the same character at the same index in the second string, you print the character and the index. Watch out that you do not get an "index out of bounds" runtime error.


```python
# Similar characters at similar indices.
s1 = "The Holy Grail"
s2 = "Life of Brian"

if len(s1) <= len(s2):
    length = len(s1)
else:
    length = len(s2)
    
for i in range(length):
    if s1[i] == s2[i]:
            print(i, '-', s1[i])
```

    5 - o
    11 - a
    

**Exercise**: Write a function that takes a string as argument, and creates a new string that is a copy of the argument, except that every non-letter is replaced by a space (e.g., "`ph@t l00t`" is changed to "`ph t l  t`"). To write such a function, you will start with an empty string, and traverse the characters of the argument one by one. When you encounter a character that is acceptable, you add it to the new string. When it is not acceptable, you add a space to the new string. Note that you can check whether a character is acceptable by simple comparisons, e.g., any lower case letter can be found using the test `if ch >= 'a' and ch <= 'z':`. 


```python
# String cleaning function.
def clean_str(text):
    word = ''
    for c in range(len(text)):
        if text[c] >= 'a' and text[c] <= 'z':
            word += text[c]
            #print(text[c], end = '')            
        else:
            word += ' '
            #print(' ', end = '')
    return word
clean_str('pink@ is number 0ne')
```




    'pink  is number  ne'



### Extended slices

Slices (substrings) in python can take a third argument, which is the step size (or "stride") that is taken between indices. It is similar to the third argument for the `range()` function. The format for slices then becomes `<string>[<begin>:<end>:<step>]`. By default the step size is 1.

The most common use for the step size is to use a negative step size in order to create a reversed version of a string.


```python
fruit = "banana"
print( fruit[::2] )
print( fruit[1::2] )
print( fruit[::-1] ) 
print( fruit[::-2] ) 
```

    bnn
    aaa
    ananab
    aaa
    

Reversing a string using `[::-1]` is conceptually similar to traversing the string from the last character to the beginning of the string using backward steps of size 1.


```python
fruit = "banana"
for i in range( 5, -1, -1 ):
    print( fruit[i] )
```

    a
    n
    a
    n
    a
    b
    

---

## Strings are immutable

A core property of strings is that they are *immutable*. This means that they cannot be changed. For instance, you cannot change a character of a string by assigning a new value to it. As a demonstration, the following code leads to a runtime error if you try to run it:


```python
fruit = "oringe"
fruit[2] = "a"
print( fruit )
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-17-ea72f4b13ed0> in <module>
          1 fruit = "oringe"
    ----> 2 fruit[2] = "a"
          3 print( fruit )
    

    TypeError: 'str' object does not support item assignment


If you want to make a change to a string, you have to create a new string that contains the change; you can then assign the new string to the existing variable if you want. For instance:


```python
fruit = "oringe"
fruit = fruit[:2] + "a" + fruit[3:]
print( fruit )
```

    orange
    

The reasons for why strings are immutable are beyond the scope of this course. Just remember that if you want to modify a string you need to overwrite the entire string, and you cannot modify individual indices.

---

## `string` methods

There is a collection of methods that are designed to operate on strings. All of these methods are applied to a string to perform some operation. Since strings are immutable, they *never change* the string they work on, but they always `return` a changed version of the string.

Like the `format()` method introduced in Chapter 8, all these methods are called as `<string>.<method>()`, i.e., you have to write the string that they work on before the method call, with a period in between. You will encounter this more often, and why this is implemented in this way will be explained later in the course, in the chapters about object orientation.

Most of these methods are not part of a specific module, but can be called without importing them. There is a `string` module that contains specific constants and methods that can be used in your programs, but the methods I discuss here can all be used without importing the `string` module.

### `strip()`

`strip()` removes from a string leading and trailing spaces, including leading and trailing newlines and other characters that may be viewed as spaces. There are no parameters. See the following example (the string is bordered by [ and ] to show the effect):


```python
s = "    And now for something completely different\n     "
print( "["+s+"]" )
s = s.strip()
print( "["+s+"]" )
```

    [    And now for something completely different
         ]
    [And now for something completely different]
    

### `upper()` and `lower()`

`upper()` creates a version of a string of which all letters are capitals. `lower()` is equivalent, but uses only lower case letters. Neither method uses parameters.


```python
s = "The Meaning of Life"
print( s )
print( s.upper() )
print( s.lower() )
```

    The Meaning of Life
    THE MEANING OF LIFE
    the meaning of life
    

### `find()`

`find()` can be used to search in a string for the starting index of a particular substring. As parameters it gets the substring, and optionally a starting index to search from, and an ending index. It returns the lowest index where the substring starts, or `-1` if the substring is not found.


```python
s = "Humpty Dumpty sat on the wall"
print( s.find( "sat" ) )
print( s.find( "t" ) )
print( s.find( "t", 12 ) )
print( s.find( "q" ) )
```

    14
    4
    16
    -1
    

### `replace()`

`replace()` replaces all occurrences of a substring with another substring. As parameters it gets the substring to look for, and the substring to replace it with. Optionally, it gets a parameter that indicates the maximum number of replacements to be made. 

I must stress again that strings are immutable, so the `replace()` function is not actually changing the string. It returns a new string that is a copy of the string with the replacements made.


```python
s = ' Humpty Dumpty sat on the wall '
print( s.replace( 'sat on', 'fell off' ) )
```

     Humpty Dumpty fell off the wall 
    

### `split()`

`split()` splits a string up in words, based on a given character or substring which is used as separator. The separator is given as the parameter, and if no separator is given, the white space is used, i.e., you split a string in the actual words (though punctuation attached to words is considered part of the words). If there are multiple occurrences of the separator next to each other, the extra ones are ignored (i.e., with the white space as separator, it does not matter if there is a single white space between two words, or multiple).

The result of this split is a so-called "list" of strings. Lists are discussed in a coming chapter. However, note that if you want to access the separate words, you can use the `for <word> in <list>:` construction.


```python
s = 'Humpty Dumpty sat on the wall'
wordlist = s.split()
for word in wordlist:
    print( word )
```

    Humpty
    Dumpty
    sat
    on
    the
    wall
    

A very useful property of splitting is that we can decode some basic file formats. For example, a comma separated value (CSV) file is a very simple format, of which the basic setup is that each line consists of values that are separated by a comma. These values can be split from each other using the `split()` method. (Note: In actuality it will be a bit more convoluted as there might be commas in the fields that are stored in the CSV file, so it depends a bit on the contents of the file whether this simple approach will work. More on CSV files will be said in a much later chapter in the course, where file formats are discussed.)


```python
csv = "2016,September,28,Data Processing,Tilburg University,Tilburg"
values = csv.split( ',' )
for value in values:
    print( value )
```

    2016
    September
    28
    Data Processing
    Tilburg University
    Tilburg
    

### `join()`

`join()` is the opposite of `split()`. `join()` joins a list of words together, separated by a specific separator. This sounds like it would be a method of lists, but for historic reasons it is defined as a string method. Since all string methods are called with the format `<string>.<method>()`, there must be a string in front of the call to `join()`. That string is the separator that you want to use, while the parameter of the method is the list that you want to join together. The return value, as always, is the resulting string. In the following example, note the notation of each of these steps:


```python
s = "Humpty;Dumpty;sat;on;the;wall"
print ( s )
wordlist = s.split( ';' )
print ( wordlist )
s = " ".join( wordlist )
print( s )
```

    Humpty;Dumpty;sat;on;the;wall
    ['Humpty', 'Dumpty', 'sat', 'on', 'the', 'wall']
    Humpty Dumpty sat on the wall
    

### Practice

**Exercise**: In the code below you are given a string that contains a spelling error, namely the word "vox" instead of "fox". Replace all occurrences of this spelling error with the correct spelling. Hint: use `replace()`.


```python
# Replace vox with fox
text = """The quick, brown vox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. 
Junk MTV quiz graced by vox whelps. Bawds jog, flick quartz, vex nymphs. 
Waltz, bad nymph, for quick jigs vex! Vox nymphs grab quick-jived waltz. 
Brick quiz whangs jumpy veldt vox."""

new_text = text.replace("vox", "fox")
print(new_text)
```

    The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. 
    Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. 
    Waltz, bad nymph, for quick jigs vex! Vox nymphs grab quick-jived waltz. 
    Brick quiz whangs jumpy veldt fox.
    

**Exercise**: In the code below you are given a string that contains an at-sign (`@`). Display the contents of the string up to, but not including, this at-sign. Hint: use `find()`.


```python
text = """Nobody expects the Spanish
Inquisition!@ In fact, those who do
expect the Spanish Inquisition..."""

print(text[:text.find('@')])
```

    Nobody expects the Spanish
    Inquisition!
    

**Exercise**: Write a program that prints a "cleaned" version of all the words in a string. Everything that is not a letter should be removed and be considered a separator. All the letters should be lower case. For example, the string "I'm sorry, sir." should produce four words, namely "i", "m", "sorry", and "sir". You can use the function for string cleaning which you wrote as an exercise above.


```python
# Cleaned words.
def clean_split_str(text):
    word = ''
    text = text.lower()
    for c in range(len(text)):
        if text[c] >= 'a' and text[c] <= 'z':
            word += text[c]  
        else:
            word += ' '
    return word.split()
clean_split_str('pink@\'s beauty is number 0ne,indeed.')
```




    ['pink', 's', 'beauty', 'is', 'number', 'ne', 'indeed']



---

## Character encoding

All systems use a particular way of encoding characters. The basic encoding that (almost) every system supports is the standard ASCII code. This is a 7-bits code, which can represent 128 different characters. Several of these (in particular those with the lowest-numbered encodings) are control characters that have a special function. Most of these special functions are only useful for archaic computer systems, but the tabulation, newline, and backspace characters are found amongst them. If you only use characters on a standard US keyboard, you are limited to ASCII characters.

Nowadays, many systems use Unicode. Unicode supports far more characters. There are different formats for storing characters in Unicode. The best-known is `UTF-8`, which uses one byte for each of the ASCII characters, but multiple bytes for all the other characters (a byte is a group of 8 bits, whereby each bit contains either a 1 or a zero). Other Unicode encodings use multiple bytes to store any character. Python, be default, works with UTF-8, which means that it also supports regular ASCII encodings.

### ASCII

Below you can see the ASCII table. Not all characters are included; some characters are control characters; when used with a backslash, these become 'escape sequences', and lead to special behaviour. These have the numbers zero to 31, and 127. 32 is the space. I also display the hexadecimal code for each character next to the decimal code. (If you wonder why I even bother listing those hexadecimal codes: they become relevant in a much later chapter.)

` DC HX      DC HX      DC HX      DC HX      DC HX      DC HX`<br>
`` 32 20      48 30 0    64 40 @    80 50 P    96 60 `   112 70 p``<br>
` 33 21 !    49 31 1    65 41 A    81 51 Q    97 61 a   113 71 q`<br>
` 34 22 "    50 32 2    66 42 B    82 52 R    98 62 b   114 72 r`<br>
` 35 23 #    51 33 3    67 43 C    83 53 S    99 63 c   115 73 s`<br>
` 36 24 $    52 34 4    68 44 D    84 54 T   100 64 d   116 74 t`<br>
` 37 25 %    53 35 5    69 45 E    85 55 U   101 65 e   117 75 u`<br>
` 38 26 &    54 36 6    70 46 F    86 56 V   102 66 f   118 76 v`<br>
` 39 27 '    55 37 7    71 47 G    87 57 W   103 67 g   119 77 w`<br>
` 40 28 (    56 38 8    72 48 H    88 58 X   104 68 h   120 78 x`<br>
` 41 29 )    57 39 9    73 49 I    89 59 Y   105 69 i   121 79 y`<br>
` 42 2A *    58 3A :    74 4A J    90 5A Z   106 6A j   122 7A z`<br>
` 43 2B +    59 3B ;    75 4B K    91 5B [   107 6B k   123 7B {`<br>
` 44 2C ,    60 3C <    76 4C L    92 5C \   108 6C l   124 7C |`<br>
` 45 2D -    61 3D =    77 4D M    93 5D ]   109 6D m   125 7D }`<br>
` 46 2E .    62 3E >    78 4E N    94 5E ^   110 6E n   126 7E ~`<br>
` 47 2F /    63 3F ?    79 4F O    95 5F _   111 6F o`

As you can see, each character has a number attached to it. To find out what a character's number is in a Python program, you can use the `ord()` function. For instance, `ord("A")` return the number of "A", which, as you can see, is 65. The counterpart of the `ord()` function is the `chr()` function. `chr()` gets a number as argument, and returns the character that belongs to that number. For instance, `chr(65)` is the letter "A".

A comparison of strings which use only these characters use the numbers of the characters to determine which string is "smaller". For instance, the string "orange" is smaller than the string "ordinal", because the first character that differs between them is the third one, which is "a" for "orange" and "d" for "ordinal", and since the number for "a" is lower than the number for "d", the string "orange" is considered to be smaller than the string "ordinal". This is, basically, an alphabetic comparison. If characters occur in a string that are not letters, you can check in the ASCII table which is considered lower. Notice how all the digits are lower than letters.


```python
print( ord( 'A' ) )
print( ord( 'a' ) )
print( chr( 65 ) )
print( chr( 97 ) )
print( "orange" < "ordinal" )
```

    65
    97
    A
    a
    True
    

You can use these numbers that are associated with characters to do all kinds of calculations. For instance, if I want to know which the twelfth letter after "g" is, I can calculate that as follows:


```python
print( "The 12th letter after g is", chr( ord( "g" )+12 ) )
```

    The 12th letter after g is s
    

For another example of what you can do with character codes, here is a program that generates the ASCII table as a matrix:


```python
print( ' ', end='' )
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 2, 8 ):
    print( i, end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

      0 1 2 3 4 5 6 7 8 9 A B C D E F
    2   ! " # $ % & ' ( ) * + , - . /
    3 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
    4 @ A B C D E F G H I J K L M N O
    5 P Q R S T U V W X Y Z [ \ ] ^ _
    6 ` a b c d e f g h i j k l m n o
    7 p q r s t u v w x y z { | } ~ 
    

Note that I highly prefer you using the `ord()` and `chr()` functions if you want to juggle character encoding. If you want to refer to the character code of the letter "A", do not write `65`, but write `ord("A")` instead. `65` is only meaningful to people who know ASCII encodings from memory, and your programs should be meaningful to anybody. Moreover, while ASCII is a widely-used standard, there are still computers out there which use different encoding mechanisms, in which the code for "A" is not necessarily 65 (I am looking at you, IBM).

### UTF-8

Python supports Unicode, in particular the most common Unicode encoding scheme UTF-8. This means that you can use all kinds of "weird" characters. I explained that in the naming of functions and variables you can use "letters", which you probably assumed meant "A" to "Z" and "a" to "z". The funny thing is that it depends on the language codes of your computer what is considered a letter. For instance, if your computer tells Python that the language is German, then you can also use characters with umlauts. I strongly discourage using such letters in variable and function names, by the way. Not only are they hard to type, but they also make your program less portable.

In UTF-8, the regular characters which you find on a keyboard are represented in strings exactly as you would expect. However, "special" characters can be incorporated too, but look quite different. Since Python supports UTF-8, you have to be careful when you copy texts from, for instance, a word processor document. Word processors have the disturbing habit of changing characters into other characters, like turning straight quotes into round quotes. If you copy such round quotes into your program, Python will accept the characters, but will not interpret them as, for instance, string boundaries.

If you want to display Unicode characters, you can do so by using Unicode encodings. You have to know the UTF-8 number of the character that you want to display. If you know that, you can use a code `\uxxxx`, where `xxxx` is a hexadecimal number, to incorporate a Unicode character in a string. For example, the code below displays the capitals of the Greek alphabet:


```python
alpha = "\u0391"
for i in range( 25 ):
    print( chr( ord( alpha )+i ), end=" " )
```

    Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ ΢ Σ Τ Υ Φ Χ Ψ Ω 

(There is one weird character in this display, between the Rho and the Sigma, which is `\u03A2`, which is empty.) 

In general, you will not need to worry too much about character encodings. I recommend that you restrict yourself to ASCII whenever possible. In cases where you have to deal with Unicode characters, things usually work correctly automatically, since the standard Python functionalities support Unicode. Occasionally I have run into translation problems from Unicode to ASCII, in particular where files were concerned. It will be a while before you run into problems like that.

---

## What you learned

In this chapter, you learned about:

- Strings
- Multi-line strings
- Accessing string characters with positive and negative indices
- Slices
- Immutability of strings
- String methods `strip()`, `upper()`, `lower()`, `find()`, `replace()`, `split()`, and `join()`
- Escape sequences
- ASCII and UTF-8 encodings

----------

## Exercises

### Exercise 10.1

Count how many of each vowel (`a`, `e`, `i`, `o`, `u`) there are in the text string in the next cell, and print the count for each vowel with a single formatted string. Remember that vowels can be both lower and uppercase.


```python
# Counting vowels.
text = """And Saint Attila raised the hand grenade up on high,
saying, "O Lord, bless this thy hand grenade, that with it
thou mayst blow thine enemies to tiny bits, in thy mercy." 
And the Lord did grin. And the people did feast upon the lambs, 
and sloths, and carp, and anchovies, and orangutans, and 
breakfast cereals, and fruit bats, and large chu..."""

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for x in text:
    if x.lower() == 'a':
        count_a += 1
    elif x.lower() == 'e':
        count_e += 1
    elif x.lower() == 'i':
        count_i += 1
    elif x.lower() == 'o':
        count_o += 1
    elif x.lower() == 'u':
        count_u += 1
else:
    print(f'{count_a} a, {count_e} e, {count_i} i, {count_o} o, {count_u} u.')
```

    32 a, 23 e, 18 i, 12 o, 6 u.
    

### Exercise 10.2

The text string in the next cell contains several words which are enclosed by square brackets (`[` and `]`). Scan the string and print out all words which are between square brackets. For example, if the text string would be "`[a]n example[ string]`", you are expected to print out "`a string`".


```python
# Distilling text.

# Version 1
text = """The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. 
Junk MTV quiz graced by fox whelps. [Never gonna ] Bawds jog, flick quartz, vex nymphs. 
[give you up\n] Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. 
Brick quiz whangs jumpy veldt fox. [Never ] Bright vixens jump; [gonna let ] dozy fowl 
quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Charged 
[you down\n] fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven 
jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs! "Now fax quiz Jack!" 
my brave ghost pled. [Never ] Five quacking zephyrs jolt my wax bed. [gonna ] Flummoxed 
by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. [run around ] 
A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick 
brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! 
[and desert you] Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed 
by MTV for luck. A wizard’s job is to vex chumps quickly in fog. Watch "Jeopardy!", 
Alex Trebek's fun TV quiz game."""

str_start = text.find('[') + 1
str_stop = text.find(']')

while str_stop < len(text) and str_stop > str_start:
    #print(f'{str_start} - {str_stop}')
    print(f'{text[str_start:str_stop]}', end = '')
    
    str_start = text.find('[', str_start + 1) + 1
    str_stop = text.find(']', str_stop + 1)
    #print(f'{str_start} - {str_stop}')
    #print('---------------------------------')
```


```python
# Version 2 (from Hoda)
text = """The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. 
Junk MTV quiz graced by fox whelps. [Never gonna ] Bawds jog, flick quartz, vex nymphs. 
[give you up\n] Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. 
Brick quiz whangs jumpy veldt fox. [Never ] Bright vixens jump; [gonna let ] dozy fowl 
quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Charged 
[you down\n] fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven 
jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs! "Now fax quiz Jack!" 
my brave ghost pled. [Never ] Five quacking zephyrs jolt my wax bed. [gonna ] Flummoxed 
by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. [run around ] 
A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick 
brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! 
[and desert you] Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed 
by MTV for luck. A wizard’s job is to vex chumps quickly in fog. Watch "Jeopardy!", 
Alex Trebek's fun TV quiz game."""

splitted = text.split('[')

for w in splitted:
    if w.find(']') > 0:
        print(w[:w.find(']')], end = '')    
```

    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you

### Exercise 10.3

Print a line of all the capital letters "A" to "Z". Below it, print a line of the letters that are 13 positions in the alphabet away from the letters that are above them. E.g., below the "A" you print an "N", below the "B" you print an "O", etcetera. You have to consider the alphabet to be circular, i.e., after the "Z", it loops back to the "A" again.


```python
# ROTR-13.
text1 = ''
text2 = ''

start = ord('A')
stop = ord('Z')
nrange = stop - start + 1

for i in range(0, nrange):
    ord = start+i
    new_ord = ord+13
    text1 += ' ' + chr(start+i)
    #print(f'i = {i} | {start+i}-{chr(start+i)} | {start+i+13}-{chr(start+i+13)} | {start+i+13-nrange}-{chr(start+i+13-nrange)}')       
    if new_ord > stop:
        new_ord = new_ord-nrange
    text2 += ' ' + chr(new_ord)     
print(text1)
print(text2)
```

     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
     N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
    

### Exercise 10.4

In the text below, count how often the word "wood" occurs (using program code, of course). Capitals and lower case letters may both be used, and you have to consider that the word "wood" should be a separate word, and not part of another word. Hint: If you did the exercises from this chapter, you already developed a function that "cleans" a text. Combining that function with the `split()` function more or less solves the problem for you.


```python
# Counting wood.
text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def clean_split_str(text):
    word = ''
    text = text.lower()
    for c in range(len(text)):
        if text[c] >= 'a' and text[c] <= 'z':
            word += text[c]  
        else:
            word += ' '
    return word.split()
cleaned = clean_split_str(text)

count = 0
for i in range(len(cleaned)):
    if cleaned[i] == 'wood':
        count += 1
print(count)    
```

    3
    

### Exercise 10.5

Write a program that takes a string and produces a new string that contains the exact characters that the first string contains, but in order of their ASCII-codes. For instance, the string "Hello, world!" should be turned into " !,Hdellloorw". This is relatively easy to do with list functions, which will be introduced in a future chapter, but for now try to do it with string manipulation functions alone.


```python
# String sorting.
text = "Hello, world!"

# Version 1
result = 'H'
min = ord(result)
max = ord(result)
for c in text[1:]:
    #print(f'c = {c} - ord(c) = {ord(c)} - min = {min} - max = {max}')
    check_pos = result.find(c)
    #print(f'check_pos = {check_pos}')
    
    if ord(c) >= max:
        max = ord(c)
    if ord(c) <= min:
        min = ord(c)
    #print(f'min = {min} - max = {max}')    

    if ord(c) == max:
        #print('case 1')
        result = result + c
    elif ord(c) == min:
        #print('case 2')
        result = c + result
    elif check_pos > 0:
        #print('case 3')
        result = result[:check_pos+1] + c + result[check_pos+1:]
    else:
        #print('case 4')
        #print(f'c = {c} - ord(c) = {ord(c)} - min = {min} - max = {max}')
        #print(f'check_pos = {check_pos}')
        count = -1
        for x in result:
            if ord(c) > ord(x):
                count += 1
            #print(f'ord(x) = {ord(x)} - count = {count}')
        #else:
            #print(f'count = {count}')
        result = result[:count+1] + c + result[count+1:]
        #print(f'result = {result}')
        #print('++++++++++++++++++++')
print(result)    
```

     !,Hdellloorw
    


```python
# String sorting.
text = "Hello, world!"

# Version 2
result = ''
for c in text:
    #print(f'c = {c}')
    count = 0
    for x in result:
     #   print(f'x = {x}')
      #  print(f'ord(c) = {ord(c)} - ord(x) = {ord(x)}')
        if ord(c) >= ord(x):            
            count += 1
       #     print(f'count = {count}')
    else:   
        #print(f'count = {count}')
        #print(f'result[:count] = {result[:count]}')
        #print(f'result[count:] = {result[count:]}')
        result = result[:count] + c + result[count:] 
    #print(f'result = {result}')
    #print('++++++++++++++++++++')
print(result) 
```

     !,Hdellloorw
    

### Exercise 10.6

Typical autocorrect functions are the following: (1) if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case; (2) if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed; (3) if a sentence starts with a lower-case letter, that letter is turned into a capital; (4) if a word consists entirely of capitals, except for the first letter which is lower case, then the case of the letters in the word is reversed; and (5) if the sentence contains the name of a day (in English) which does not start with a capital, the first letter is turned into a capital. Write a function that takes a sentence as a parameter and returns its auto-corrected version.


```python
# Autocorrect.
def check_capital(char):
    if char >= 'A' and char <= 'Z':
        return True
    else:
        return False
    
def autocorrect(sentence):
    check = sentence.split()
    result = sentence

    # Rule 1 - Lower the 2nd letter in XXx: 
    for x in check:
 
        if check_capital(x[0]) and check_capital(x[1]) and not check_capital(x[2]):
            x2 = x.replace(x[1],x[1].lower())
            result = result.replace(x, x2)
        else:
            result = result
    #print(f'Rule 1 = {result}')
    
    # Rule 2 - Remove the duplicated word:        
    for x in check:
        x1 = x + ' ' + x
        result = result.replace(x1, x)
    #print(f'Rule 2 = {result}')
    
    # Rule 3 - Capitalize the 1st letter at beginning:
    if not check_capital(result[0]):
        result = result[0].upper() + result[1:]
    else:
        result = result   
    #print(f'Rule 3 = {result}')
    
    # Rule 4 - Reverse case for words if beginning with lower and then all upper case:
    for x in check:
        count_cap = 0
        for c in x:
            if check_capital(c):
                count_cap += 1
        #print(f'{len(x) - count_cap == 1} - x = {x} - count_cap = {count_cap}')
        if len(x) - count_cap == 1 and not check_capital(x[0]):
            x2 = x[0].upper() + x[1:].lower()
            #print(x2)
            #print(x)
            result = result.replace(x, x2)
            #print(f'result = {result}')
        else:
            result = result
    #print(f'Rule 4 = {result}')
    
    # Rule 5 - Capitalize 1st letter of English day:
    wdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    for x in check:
        if x in wdays:
            x2 = x[0].upper() + x[1:]
            result = result.replace(x, x2)
        else:
            result = result
    return result #autocorrected version of sentence

sentence = "as it turned out our chance meeting with REverend aRTHUR BElling was \
was to change our whole way of life, and every sunday we'd hurry along to St lOONY up the Cream BUn and Jam."
print(autocorrect(sentence))
```

    As it turned out our chance meeting with Reverend Arthur Belling was to change our whole way of life, and every Sunday we'd hurry along to St Loony up the Cream Bun and Jam.
    

---

## Python 2

In Python 2, the string manipulation methods listed above were part of the `string` module, and were generally called by importing the module and then writing `string.<method>()`. Such calls are no longer supported by Python 3.

Python 2 was not yet supporting Unicode natively, while Python 3 does. Python 3 strings are Unicode strings. You will not notice the difference as long as strings are ASCII, but Python 2 strings might get into troubles when Unicode characters are inserted into the strings. Python 3 also supports Unicode characters in identifiers such as variable names, while Python 2 does not. It is not recommended that you do use non-ASCII characters in identifiers, though.

---

End of Chapter 10.
