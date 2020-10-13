# Chapter 13 - Dictionaries

---

Strings and lists are ordered data structures, which entails that they can be indexed. Not all data is naturally ordered, which is why Python offers dictionaries as a way to structure unordered data.

---

## Basics of dictionaries

Dictionaries are *unordered* collections of elements. To identify an element, you have to know the element's "key".

Basically, dictionaries store "key-value pairs". Any immutable data type can function as a key. A very common type to use as key is the string.

You create dictionaries using curly brackets (`{}`), similar to how you create lists using square brackets. An empty dictionary you create by assigning `{}` to a variable. You can create a dictionary with contents by describing every element of the dictionary between the curly brackets using the syntax `<key>:<value>`, and commas between the elements.

Here a dictionary `fruitbasket` is created, that contains three key-value pairs, namely the key "apple" with value 3, the key "banana" with value 5, and the key "cherry" with value 50.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
```

To access the value belonging to a specific key, you use the same syntax as you would use for a list, except that you write the key in the place where you would write the index for a list.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket["banana"] )
```

    5
    

You can use a `for` loop to traverse a dictionary. The variable in the `for` loop gets access to all the keys.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }

def traverse_dictionary(dictionary):
    content = ""
    for key in dictionary:
        print( key, ':', dictionary[key] )

traverse_dictionary(fruitbasket)
```

    apple : 3
    banana : 5
    cherry : 50
    

Trying to access a dictionary element using a key that is not available in the dictionary will lead to a runtime error. However, adding a new element to a dictionary you can do by simply assigning a value to the dictionary item identified by the new key. For instance, adding a "mango" to the fruitbasket you can do as follows:


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket )
fruitbasket["mango"] = 1
print( fruitbasket )
```

    {'apple': 3, 'banana': 5, 'cherry': 50}
    {'apple': 3, 'banana': 5, 'cherry': 50, 'mango': 1}
    

Overwriting a dictionary item works in exactly the same way as creating a new dictionary item: you just assign a value to it.

You can delete an item from a dictionary using the `del` keyword, just as you do with lists. 


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket )
del fruitbasket["banana"]
print( fruitbasket )
```

    {'apple': 3, 'banana': 5, 'cherry': 50}
    {'apple': 3, 'cherry': 50}
    

You can determine the number of key-value pairs in a dictionary by using the `len()` function.

By the way, do you understand how the ordering of a dictionary works when looking at the display of a dictionary? Think about it.

The answer is: there is no ordering: dictionaries are unordered. In principle one cannot tell what ordering you see on your screen when you run the code above, because it might differ between computers, operating systems, and versions of Python. There is a certain structure to the ordering of the items, but nothing that you can predict. By adding enough items, the ordering might even suddenly change completely.

Since dictionaries are unordered, many of the concepts that are applicable to lists, do not work on dictionaries. For instance, you cannot refer to "slices" of a dictionary, and neither can you "sort" or "reverse" a dictionary. So dictionaries are quite limited, but they do have their uses.

---

## Dictionary methods

This section describes the dictionary methods that are most often used.

### `copy()`

Just like lists, if you assign a variable that contains a dictionary to another variable, you are not creating a copy of the dictionary; you are actually creating an alias (if you do not remember what an alias is, see the previous chapter). You cannot use the trick which is used for lists to create a copy, as it uses a slice-syntax, and dictionaries do not support slices. Therefore, there is a method `copy()` that returns a copy of a dictionary.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
fruitbasketalias = fruitbasket
fruitbasketcopy = fruitbasket.copy()

print( id( fruitbasket ) )
print( id( fruitbasketalias ) )
print( id( fruitbasketcopy ) )
```

    2209308352960
    2209308352960
    2209308352768
    

Note that this method makes a shallow copy of the dictionary (see the previous chapter if you do not remember the difference between shallow and deep copies). If you want to make a deep copy, use the `deepcopy()` function from the `copy` module.

### `keys()`, `values()`, and `items()`

The method `keys()` provides an iterator that lists all the keys of a dictionary. The method `values()` provides an iterator that lists all the values of a dictionary. The method `items()` provides an iterator that lists all the key-value pairs of a dictionary as tuples.

I specifically say that these methods returns an iterator and not a list. If you want to turn them into lists, you have to use list casting (see the previous chapter).


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( list( fruitbasket.keys() ) )
print( list( fruitbasket.values() ) )
print( list( fruitbasket.items() ) )
```

    ['apple', 'banana', 'cherry']
    [3, 5, 50]
    [('apple', 3), ('banana', 5), ('cherry', 50)]
    

At this point you might be wondering when you can use an iterator. You mainly use iterators for `for` loops (though you can also use them as arguments for the functions `max()`, `min()` and `sum()`).


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }
for key in fruitbasket.keys():
    print( key, ':', fruitbasket[key] )
    
print( sum( fruitbasket.values() ) )
```

    apple : 3
    banana : 5
    cherry : 50
    durian : 0
    mango : 2
    60
    

Since this code provides an unpredictable order for the keys, you might want to sort them before looping over them. Since `keys()` does not provide a list, it cannot be sorted directly, but you can turn the result into a list using list casting. After doing that, you can sort.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }
keylist = list( fruitbasket.keys() )
keylist.sort()
for key in keylist:
    print( key, ':', fruitbasket[key] )
```

    apple : 3
    banana : 5
    cherry : 50
    durian : 0
    mango : 2
    

You cannot apply the `sort()` method to the list casting, i.e., `keylist = list( fruitbasket.key() ).sort()` does not work. You must first create the list, then sort it. Neither can you write `for key in keylist.sort()`, as the `sort()` method has no return value.

If you wonder why Python seems to prefer iterators instead of lists: the answer is that iterators are more general and use much less memory. They are "lazy" methods, as they only provide an item when it is requested.

### `get()`

The `get()` method can be used to get a value from a dictionary even when you do not know if the key for which you seek the value exists. You call the `get()` method with the key you are looking for, and it will return the corresponding value when the key exists in the dictionary, or the special value `None` when the key does not exist in the dictionary. If you want to return a specific value instead of `None` if the key does not exist, you can add that value as a second argument to the method.


```python
fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }


def keyvalue_exists(fruitbasket, item): 
    apple = fruitbasket.get( item )
    output = ""
    if apple:
        return (item + " is in the basket" )
    else:
        return( "no "+ item + " in the basket")
        
print(keyvalue_exists(fruitbasket, "apple"))
print(keyvalue_exists(fruitbasket, "orange"))

banana = fruitbasket.get( "banana", 0 )
print( "number of bananas in the basket:", banana )

strawberry = fruitbasket.get( "strawberry", 0 )
print( "number of strawberries in the basket:", strawberry )
```

    apple is in the basket
    no orange in the basket
    number of bananas in the basket: 5
    number of strawberries in the basket: 0
    

Study the example above closely, as what it demonstrates about the `get()` method is very useful. Suppose that you store a collection of items with corresponding quantities, for instance, the contents of a fruit basket with the keys being the names of the fruits and the values being the quantities. When you query the fruitbasket dictionary using the `get()` method with a second parameter zero, you can look for any fruit in the basket without the need to check first if the fruit exists in the basket, because if you ask for a fruit that is not there, the `get()` method returns zero, which is exactly what you want to hear.

### Practice

**Exercise**: The code block below contains a list of words. Build a dictionary that contains all these words as keys, and how often they occur as values. Then print the words with their quantities.


```python
# Word counts.
wordlist = ["apple","durian","banana","durian","apple","cherry","cherry","mango","apple",
            "apple","cherry","durian","banana","apple","apple","apple","apple","banana","apple"]

def word_dictionary_list(word_list):
    dict = {}
    for element in wordlist:
        count = wordlist.count(element)
        dict[element] = count
    return dict #a dictionary with words as key, and their frequency in word_list as value

print(word_dictionary_list(wordlist))
```

    {'apple': 9, 'durian': 3, 'banana': 3, 'cherry': 3, 'mango': 1}
    

**Exercise**: The code block below contains a string that is a list of words, separated by commas. Build a dictionary that contains all these words as keys, and how often they occur as values. Then print the words with their quantities.


```python
# More word counts.
csv = "apple,durian,banana,durian,apple,cherry,cherry,mango,apple," + \
      "apple,cherry,durian,banana,apple,apple,apple,apple,banana,apple"
    
def word_dictionary_csv(word_text):
    word_split = word_text.split(',')
    word_dict = {}
    for elm in word_split:
        word_dict[elm] = word_split.count(elm)
    return word_dict #a dictionary with words as key, and their frequency in word_text as value

print(word_dictionary_csv(csv))
```

    {'apple': 9, 'durian': 3, 'banana': 3, 'cherry': 3, 'mango': 1}
    

**Exercise**: The code block below contains a very small dictionary that contains the translations of English words to Dutch. Write a function that uses this dictionary to return a word-for-word translation of the given sentence. A word for which you cannot find a translation, you can leave "as is". The dictionary is supposed to be used case-insensitively, but your translation may consist of all lower case words. Remove punctuations from the translation.


```python
# Translation
english_dutch = { "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal",
    "saw":"zaag", "first":"eerst", "performance":"optreden",
    "of":"van", "a":"een", "new":"nieuw", "symphony":"symphonie",
    "by":"bij", "one":"een", "world":"wereld", "leading":"leidend",
    "modern":"modern", "composer":"componist", "composers":"componisten",
    "two":"twee", "shed":"schuur", "sheds":"schuren" }

def translate(english_text):
    eng_lower = english_text.lower()
    eng_split = eng_lower.split()
    eng_trans = ''
    for elm in eng_split:
        elm_adj = []
        for char in elm:
            if char < "a" or char > "z":
                elm_adj.append(' ')
            else:
                elm_adj.append(char)
        new_elm = ''.join(elm_adj)
        for word in new_elm.split():
            dutch_word = english_dutch.get(word, 0)
            if dutch_word == 0:
                dutch_word = word
            eng_trans +=  ' ' + dutch_word
    return eng_trans.strip() #a word-by-word translation of english_text to dutch 

sentence = "Last week The Royal Festival Hall saw the first performance of \
a new symphony by one of the world's leading modern composers, Arthur \"Two-Sheds\" Jackson."
print(translate(sentence))
```

    laatst week de koninklijk feest hal zaag de eerst optreden van een nieuw symphonie bij een van de wereld s leidend modern componisten arthur twee schuren jackson
    

---

## Keys

As I said, any immutable data type can be a dictionary key. This means that strings, integers, and floats can all be used as keys. This can occasionally be useful. 

A very straightforward example of tuples being useful as keys is a dictionary in which you want to store information associated with points in two-dimensional space (a discussion of which was given in the chapter on tuples). There is no good way in which you can store the identification of a point in a single number or string. It is not impossible (for instance, you could store the number-pair as their string-representations, concatenated with a comma in between) but it becomes ambiguous and convoluted (for instance, the string-keys "`2,3`", "`2, 3`", "`+2,+3`", and "`02,03`" would all be representing the same tuple).

---

## Storing complicated values

Until now I only considered the case in which a dictionary stores a single value of a simple data type. However, it is possible to store much more complex values in dictionaries. Values can be arbitrary Python objects. For example, you can store a list with each key. Below a dictionary is used to store the students who are following a course. The course is identified by its course number, while the students are identified by their student numbers.


```python
courses = {
    '880254':['u123456', 'u383213', 'u234178'], 
    '822177':['u123456', 'u223416', 'u234178'], 
    '822164':['u123456', 'u223416', 'u383213', 'u234178']}

for c in courses:
    print( c )
    for s in courses[c]:
        print( s, end=" " )
    print()
```

    880254
    u123456 u383213 u234178 
    822177
    u123456 u223416 u234178 
    822164
    u123456 u223416 u383213 u234178 
    

Suppose that we do not only want to store the student numbers for a course number, but also the name of the course, the ECTS value of the course, and for each student number also the grade. You can do that (for example) by storing the value for a course number as a dictionary, with three keys, namely "name", "ects", and "students". The value for "name" is the course name as a string, the value for "ects" is the ECTS as an integer, and the value for "students" is another dictionary, which contains student numbers as keys and grades as values.


```python
courses = {
    '880254': 
    { "name":"Research Skills Data Processing", "ects":3, 
      "students":{'u123456':8, 'u383213':7.5, 'u234178':6} }, 
    '822177': 
    { "name":"Understanding Intelligence", "ects":6,
     "students":{'u123456':5, 'u223416':7, 'u234178':9} }, 
    '822164': 
    { "name":"Computer Games", "ects":6,
     "students":{'u123456':7.5, 'u223416':9, 'u383213':6, 'u234178':4} } }

for c in courses:
    print( "{}: {} ({})".format( c, courses[c]["name"], courses[c]["ects"] ) )
    for s in courses[c]["students"]:
        print( "{}: {}".format( s, courses[c]["students"][s] ) )
    print()
```

    880254: Research Skills Data Processing (3)
    u123456: 8
    u383213: 7.5
    u234178: 6
    
    822177: Understanding Intelligence (6)
    u123456: 5
    u223416: 7
    u234178: 9
    
    822164: Computer Games (6)
    u123456: 7.5
    u223416: 9
    u383213: 6
    u234178: 4
    
    

Data structures can become a lot more complex than this if you want. However, if you are really considering designing Python programs for data structures like this, you should at least investigate object orientation first and probably do a separate course on databases.

---

## Lookup speed

Lists and dictionaries are the two most-used data structures in Python. While often it is clear when you should use which data structure, it is helpful if you know a little bit about how Python processes these data structures in case you have a choice.

Suppose that we read a large bunch of numbers from a file. The numbers are all different and can be anything. We later need to compare the numbers on another list to the numbers that we read from the file.

Should we use a list or a dictionary to store the numbers that we read from the file? Since they are just numbers, without extra data, a list seems to be the best option. There is, however, a problem if you use a list here. Check out the following code, in which a list of 10000 numbers is created, and after that some code checks for 10000 different numbers whether they are on the list (which none of them are).


```python
from datetime import datetime


def duration_check_numbers_in_list():
    numlist = []

    for i in range( 10000 ):
        numlist.append( i )

    start = datetime.now()

    count = 0
    for i in range( 10000, 20000 ):
        if i in numlist:
            count += 1

    end = datetime.now()
    return( "{}.{} seconds needed to find {} numbers".format( 
            (end - start).seconds, (end - start).microseconds,count ) )
print(duration_check_numbers_in_list())
```

    1.58199 seconds needed to find 0 numbers
    

Here is the code for doing the same thing with a dictionary, where we simply store the value 1 with each number.


```python
from datetime import datetime

def duration_check_numbers_in_dictionary():
    numdict = {}

    for i in range( 10000 ):
        numdict[i] = 1

    start = datetime.now()

    count = 0
    for i in range( 10000, 20000 ):
        if i in numdict:
            count += 1

    end = datetime.now()

    return( "{}.{} seconds needed to find {} numbers".format( 
            (end - start).seconds, (end - start).microseconds,count ) )
print(duration_check_numbers_in_dictionary())
```

    0.0 seconds needed to find 0 numbers
    

You will notice that for a dictionary, the code gives an answer almost immediately, while for a list it takes quite some time for the code to provide an answer. 

The reason is that I use the `in` operator to check whether a number is in the list, or in the dictionary. For a list this means that Python searches through the list, sequentially, until it reaches the number or reaches the end of the list. In this case, it means that Python checks 10000 times 10000 numbers (as it cannot find any of them), which is 100 million numbers.

For a dictionary, the process of finding a key is much faster. Python can quickly decide whether or not a key is in a dictionary. Usually, the checking of just a handful of numbers suffices. Therefore, the code is much, much faster for a dictionary.

You might think that a couple of seconds for the list search is still negligible, but the search time increases quadratically with the size of the data. Depending on the problem, using a dictionary might be highly preferable over using a list.

On the other hand, lists take less memory than dictionaries, and if you can directly access a list item via its index, lists are faster than dictionaries. For instance, in the problem above, if the list is sorted you can find numbers on it in a smarter way than using the `in` operator (checking about 14 indices would suffice) -- in that case, a list may be faster again.

From this, you should remember that a list is fast if you can access its elements directly via their index, while a dictionary is a much better choice if the main way to find something is by scanning items. The `in` operator seems easy and reads well, but if you use it to seek something in a long list, you better think again.

---

## What you learned

In this chapter, you learned about:

- Dictionaries
- Dictionary keys and values
- Dictionary methods `copy()`, `keys()`, `values()`, `items()`, and `get()`
- Complicated dictionaries
- Speed differences between lists and dictionaries

---

## Excercises

### Exercise 13.1

Write a program that takes the text in the code block, splits it into words (where everything that is not a letter is considered a word boundary), and case-insensitively builds a dictionary that stores for every word how often it occurs in the text. Then print all the words with their quantities in alphabetical order.


```python
# Word counting.
text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

word_list = text.lower().split()
#print(word_list)

word_list.sort()
#print(word_list)

word_dict = {}
for word in word_list:
    #print(f'word = {word}')
    chars = list(word)
    #print(chars)
    for c in chars:
        if ord(c) < ord("a") or ord(c) > ord("z"):
            chars.remove(c)
    adj_word = ''.join(chars)
    #print(f'adj_word = {adj_word}')
    count = text.lower().count(adj_word)
    word_dict[adj_word] = count
    
print(word_dict)
```

    {'a': 9, 'and': 1, 'as': 4, 'chuck': 9, 'could': 3, 'he': 3, 'how': 1, 'if': 2, 'much': 3, 'wood': 7, 'woodchuck': 4, 'would': 4}
    

### Exercise 13.2

Write a functions that reads the contents of an input file, splits it into words (where everything that is not a letter is considered a word boundary), and case-insensitively builds and returns a dictionary that stores for every word how often it occurs in the text.  Write another function that takes such a dictionary as a parameter, and prints all its words with their quantities in alphabetical order. The second function does not return anything.



```python
# Counting words in pc_woodchuck.txt.
def count_words(input_file):
    fp = open(input_file)
    buffer = fp.readlines()
    text = ' '.join(buffer)
    word_list = text.lower().split()
    #print(word_list)

    word_dict = {}
    for word in word_list:
        #print(f'word = {word}')
        chars = list(word)
        #print(chars)
        for c in chars:
            if ord(c) < ord("a") or ord(c) > ord("z"):
                chars.remove(c)
        adj_word = ''.join(chars)
        #print(f'adj_word = {adj_word}')
        count = text.lower().count(adj_word)
        word_dict[adj_word] = count
    return word_dict #a dictionary with words as key and their frequency in input_file as value

def print_words(word_dict):
    #prints words and frequencies in word_dict in alphabetical order
    word_list = list(word_dict.keys())
    word_list.sort()
    #print(word_list)
    for word in word_list:
        print(f'{word}: {word_dict[word]}')
    return

print_words(count_words( "pc_woodchuck.txt"))
#count_words( "pc_woodchuck.txt")
```

    a: 9
    and: 1
    as: 4
    chuck: 9
    could: 3
    he: 3
    how: 1
    if: 2
    much: 3
    wood: 7
    woodchuck: 4
    would: 4
    

### Exercise 13.3

The code block below shows a list of movies. For each movie it also shows a list of ratings. Convert this code in such a way that it stores all this data in one dictionary, then use the dictionary to print the average rating for each movie, rounded to one decimal.


```python
# Movie ratings.
movies = ["Monty Python and the Holy Grail", 
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

grail_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5,8 ]
brian_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]
life_ratings = [ 7, 6, 5 ]
different_ratings = [ 6, 5, 6, 6 ]

movie_dict = {}
rating_list = [grail_ratings, brian_ratings, life_ratings, different_ratings]
for i in range(len(movies)):
    movie = movies[i]
    movie_dict[movie] = rating_list[i]
#print(movie_dict)

for m in movie_dict:
    #print(m)
    #print(movie_dict[m])
    ratings = movie_dict[m]
    total = 0
    for r in ratings:
        total += r
    avg = total / len(ratings)
    avg = round(avg,1)
    print(f'{m}: {avg}')
```

    Monty Python and the Holy Grail: 7.9
    Monty Python's Life of Brian: 6.8
    Monty Python's Meaning of Life: 6.0
    And Now For Something Completely Different: 5.8
    

### Exercise 13.4

A library contains books. Books have a writer, identified by last name and first name. Books also have a title. Books also have a location number that identifies where they can be found in the library. Librarians want to be able to locate a specific book if they know writer and title, and they want to be able to list all the books that they have of a specific writer. What data structure would you use to store the books? 


```python
# Data structure
book1 = {"title": "Title1", "writer": "First1 Last1", "location": "Number1"}
book2 = {"title": "Title2", "writer": "First2 Last2", "location": "Number2"}
book3 = {"title": "Title3", "writer": "First2 Last2", "location": "Number3"}
book4 = {"title": "Title4", "writer": "First1 Last1", "location": "Number4"}
book5 = {"title": "Title5", "writer": "First5 Last5", "location": "Number5"}
book6 = {"title": "Title6", "writer": "First1 Last6", "location": "Number6"}
lib_books = {"book1": book1, "book2": book2, "book3": book3, "book4": book4, "book5": book5, "book6": book6}
lib_books
```




    {'book1': {'title': 'Title1', 'writer': 'First1 Last1', 'location': 'Number1'},
     'book2': {'title': 'Title2', 'writer': 'First2 Last2', 'location': 'Number2'},
     'book3': {'title': 'Title3', 'writer': 'First2 Last2', 'location': 'Number3'},
     'book4': {'title': 'Title4', 'writer': 'First1 Last1', 'location': 'Number4'},
     'book5': {'title': 'Title5', 'writer': 'First5 Last5', 'location': 'Number5'},
     'book6': {'title': 'Title6', 'writer': 'First1 Last6', 'location': 'Number6'}}




```python
# Function to locate book based on writer and title
def locate_book(writer, title):
    results = ''
    for b in lib_books:
        #print(b)
        if lib_books[b]["writer"] == writer and lib_books[b]["title"] == title:
            #print(lib_books[b])
            results = lib_books[b]["location"]
    return results
locate_book("First2 Last2", "Title3")
```




    'Number3'




```python
# Function to list books from writer
def list_books_by_writer(writer):
    results = {}
    for b in lib_books:
        #print(b)
        if lib_books[b]["writer"] == writer:
            #print(lib_books[b])
            results[b] = {"title": lib_books[b]["title"], "writer": lib_books[b]["writer"], "location": lib_books[b]["location"]}
    return results
#list_books_by_writer("First1 Last6")
list_books_by_writer("First2 Last2")
```




    {'book2': {'title': 'Title2', 'writer': 'First2 Last2', 'location': 'Number2'},
     'book3': {'title': 'Title3', 'writer': 'First2 Last2', 'location': 'Number3'}}



---

## Python 2

In Python 2, the methods `keys()`, `values()`, and `items()` return lists instead of iterators.

Python 2 also supports a method `has_key()` that you can use to check if a certain key is in a dictionary, but this method has been removed from Python 3.

---

End of Chapter 13.
