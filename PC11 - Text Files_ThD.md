# Chapter 11 - Text Files

---

One of the most important uses of Python for data processing is the reading, changing, and writing of text files. Data is often stored in text files, because text files can be easily transferred between different programs. There are multiple standardized formats for text files, such as "comma-separated values" (CSV) files. Python supports particular text file formats through modules, some of which will be discussed later. This chapter focusses on opening, reading, writing, and closing of any text file, regardless of format. 

---

## Flat text files

When programmers refer to "text files" or "flat text files", they mean files in which all characters are meant to be read as regular characters, like you would type on a keyboard. For instance, Python program files are flat text files, as are HTML files. Word processor documents, however, are not flat text files, and neither are images. If you want to know whether a file is a text file or not, you can try to open it in a text editor (such as the editor for the IDLE environment, which comes with Python). If you see only readable text, the file is likely to be a text file. Otherwise, it is a so-called "binary file".

Text files consist of lines of text. At the end of a line, there is a "newline" symbol, which in Python is the character "`\n`". Different operating systems use slightly different ways of storing this character in a text file: some Windows programs store it as "carriage return", as well as "line feed" ("`\r\n`", sometimes thought as a leftover from old typewriters), while on Linux it is always stored as a single "`\n`". As long as you access a file from Python as a regular text file, Python will convert the characters that it reads to the standard "`\n`", and vice versa when it writes. So you do not usually need to worry about such differences (except when you need to transfer text files between operating systems).

However; if you open a file in other editors, such as notepad, sometimes it does not properly understand the end-of-line characters, and shows everything on one line.

### File handles and pointers

When you work with a file in a program, you have to open the file. Opening a file provides a so-called "file handle". A file handle can be seen as an access point to the file. It contains a "pointer" that indicates a particular place in the file. That pointer is used when you read from or write to the file. For instance, when you read from the file, it starts reading at the pointer, and moves the pointer forward in the file.

When you open a file, the pointer is placed at a particular spot in the file, depending on how you opened the file. If you opened the file for reading only, the pointer is placed at the start of the file. The same is true when you open the file for both reading and writing. If you open the file for "appending" (i.e., to place new data at the file's end), the file pointer is positioned at the end of the file. Lastly, if you open a file for writing only, actually the file is completely emptied and the file pointer is placed at the start of the, now empty, file. To create a new file (i.e., a file with a name that does not exist yet), you open it for "writing only".

After opening the file, the file handle is the only access point for the file. All actions you perform on the file, you perform as methods for the file handle.

Note that any operating system only allows a limited number of files to be open simultaneously. Therefore you should close files that you no longer need to work with.

### Moving the file pointer

The file pointer, that indicates where in a file you are working, is moved automatically. For instance, when you read 10 characters from a file, the file pointer indicates which is the first of those 10 characters, and, while reading, moves up 10 characters, so that its new position is 10 characters further in the file than before. When you deal with text files, the automatic movements of the file pointer are exactly what you want. You *can* position the file pointer manually using specific methods, but such methods are, in general, only used when dealing with binary files. 

### Buffering

When you make changes to files, these often are not stored in the files immediately. Instead, the operating system "buffers" the changes in memory, and "flushes" the buffers to the actual files when it sees a need for that. You can force the flushing of the buffers by closing a file. Buffers are also flushed when your program ends normally.

However, when your program crashes (for instance because of a runtime error), buffers might not be flushed, and your files will not be updated to the point where the crash took place. So you cannot take the file contents into account when trying to debug a program.

### File processing programs

Most programs that deal with text files follow a process that, in a loop, reads contents of a file, processes those contents in some way, then writes the contents to another file. For instance, a program might read lines from a text file, and for each line sort the words, then write the sorted words to another text file. This is hardly any different from a program that asks the user the provide, in a loop, a line of text, then sorts the words in the line, and displays them using the `print()` function. 

However, it tends to be experienced as more complicated.

When you provide input to a program manually, and see it displaying outputs, you always know more or less what lines of your code Python is processing, and you can make up tests on the fly. If you work with files, you have to prepare your files beforehand, then run the program and wait until it finishes before you can examine the contents of the output files. 

While working with files might give a sense of lack of control, during development of the program you can always include `print()` statements to get an insight in what the program is doing. For instance, when it reads a line, you can print that line, and when it writes a line, you can also print that line. That way, your insight in the inner workings of the program is no different regardless whether you use manual inputs and screen outputs, or file inputs and outputs.

---

## Reading text files

To read the contents of a file, you must first open it, then read the contents, then close it.

### Opening a file using `open()`

To open a file, you use the `open()` function. 

The `open()` function gets two arguments, of which the second one is optional. The first argument is the name of the file. If the file is not in the current directory, you have to include the complete path to the file so that Python can find it. The second argument is the "mode". The mode indicates how you want to treat the file. The default mode (which is picked when you do not supply the second argument) is opening the file as a text file for reading only. How you set other modes is discussed later.

The `open()` function returns a file handle, which you use for all the remaining functionalities.

Rather than writing "`<handle> = open( <filename> )`", you will often see Python programs that write this as "`open( <filename> ) as <handle>`". These two ways of writing code are equivalent. I myself prefer the first, as that is the way it is done in most programming languages. However, the second method has an advantage that I discuss below, when talking about closing a file.

### Reading a file using `read()`

The simplest way to read the contents of a file is using the `read()` method, without arguments, on the file handle. This returns a string that contains the complete contents of the file. `read()` can get an argument, but that's only used for binary files.

Reading from a file moves the file pointer to right after the part of the file that was read. This means that if you use the `read()` method without arguments, the file pointer is moved to the end of the file. This entails that if you would try to `read()` from it a second time, nothing would be read, as there is nothing to be read after the spot where the file pointer is.

### Closing a file using `close()`

To close a file, you use the `close()` method on the file handle. Every file that you open, you should close at some point in your program. This is especially true in these notebooks, as each notebook page is considered to be one complete program; this means that if you do not close a file, it remains open even after the bit of code that you executed ends.

If everything that you need to do with a file is done in a single block, you can write this block as follows:

    with open( <filename> ) as <handle>:
        <statements>
        
This syntactic construction has the advantage that the file will be closed automatically after the block `<statements>` ends, so you do not need to include an explicit `close()` call. This construction is typically Python; you do not see it in many other programming languages.

### Displaying the contents of a file

Now the first few functions and methods for dealing with text files have been introduced, I can show some code that reads the contents of a file.


```python

def display_contents_file(file_name):
    with open( file_name ) as fp:
        buffer = fp.read()
    print( buffer )
    
display_contents_file("pc_rose.txt")
```

    'Tis but thy name that is my enemy.
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? That which we call a rose
    By any other name would smell as sweet.
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name;
    And for that name, which is no part of thee,
    Take all myself.
    
    

This code assumes that a file is available with the name "`pc_rose.txt`". Such a file should be included with these notebooks, so it should work. If it is not, you get a runtime error. How to deal with such errors will be explained in the next chapter.

**Exercise**: In the code above, change the file name "`pc_rose.txt`" to something that does not exist. Run the program and observe the error that you get.

**Exercise**: In the code above, change the file name to "`pc_woodchuck.txt`". Run the program and observe the output. Note: several more files with names "`pc_<something>.txt`" are included, but some of these contain lots of text (in particular the ones in the subfolder `pcdata`). Best not try to read the other ones (for now).


```python
def display_contents_file(file_name):
    with open( file_name ) as fp:
        buffer = fp.read()
    print( buffer )
    
display_contents_file("pc_rose2.txt")
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-1-d5fb8f718b43> in <module>
          4     print( buffer )
          5 
    ----> 6 display_contents_file("pc_rose2.txt")
    

    <ipython-input-1-d5fb8f718b43> in display_contents_file(file_name)
          1 def display_contents_file(file_name):
    ----> 2     with open( file_name ) as fp:
          3         buffer = fp.read()
          4     print( buffer )
          5 
    

    FileNotFoundError: [Errno 2] No such file or directory: 'pc_rose2.txt'



```python
def display_contents_file(file_name):
    with open( file_name ) as fp:
        buffer = fp.read()
    print( buffer )
    
display_contents_file("pc_woodchuck.txt")
```

    How much wood would a woodchuck chuck
    If a woodchuck could chuck wood?
    He would chuck, he would, as much as he could,
    And chuck as much as a woodchuck would
    If a woodchuck could chuck wood.
    
    

### Reading lines using `readline()`

To read a text file line by line, you can use the `readline()` method. The `readline()` method reads characters starting at the file pointer up to and including the next newline character, and returns them as a string. You can recognize that you have reached the end of the file by the fact that no characters are read anymore, i.e., the string that is returned is empty.


```python
def display_contents_file2(file_name):
    fp = open( file_name )
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        print( buffer )
    fp.close()
display_contents_file2("pc_rose.txt")
```

    'Tis but thy name that is my enemy.
    
    Thou art thyself, though not a Montague.
    
    What's Montague? it is nor hand, nor foot,
    
    Nor arm, nor face, nor any other part
    
    Belonging to a man. O, be some other name!
    
    What's in a name? That which we call a rose
    
    By any other name would smell as sweet.
    
    So Romeo would, were he not Romeo call'd,
    
    Retain that dear perfection which he owes
    
    Without that title. Romeo, doff thy name;
    
    And for that name, which is no part of thee,
    
    Take all myself.
    
    

Notice that the output of the code above has an empty line between each of the lines displayed. Where is that extra line coming from? Think about it.

The extra line is there because the `readline()` method returns a string of the characters read, up to and *including* the newline character. So when the `buffer` is printed, it prints a newline character too. And since the `print()` function *also* moves to a new line after it is executed, there is an empty line printed after each line of text.

**Exercise**: In the code block below, write code that reads the lines from "`pc_rose.txt`", and displays only those lines that contain the word "name".


```python
# Printing lines with "name".
def display_contents_file2(file_name):
    fp = open( file_name )
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        if 'name' in buffer:
            print( buffer )
    fp.close()
display_contents_file2("pc_rose.txt")
```

    'Tis but thy name that is my enemy.
    
    Belonging to a man. O, be some other name!
    
    What's in a name? That which we call a rose
    
    By any other name would smell as sweet.
    
    Without that title. Romeo, doff thy name;
    
    And for that name, which is no part of thee,
    
    

### Reading lines using `readlines()`

A collary to the `readline()` method is the `readlines()` method. `readlines()` reads all the lines in the file, and returns them as a list of strings. The strings include the newline characters.


```python
def display_contents_file3(file_name):
    fp = open( file_name)
    buffer = fp.readlines()
    for line in buffer:
        print( line, end="" )
    fp.close()
    
display_contents_file3("pc_rose.txt")
```

    'Tis but thy name that is my enemy.
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? That which we call a rose
    By any other name would smell as sweet.
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name;
    And for that name, which is no part of thee,
    Take all myself.
    

Note that the output of the code above does not have the empty lines between the lines of text, as the `print()` function includes the "`end=""`" argument, which entails that `print()` itself does not go to the next line after printing.

### When to use which file-reading method

Both the `read()` and `readlines()` method read a whole file at once. Obviously, for small files this is acceptable, but for long files you might not have enough memory to store the file contents efficiently. In such circumstances (or when you do not know the file size), you should read a file line by line with the `readline()` method.

It is often a good idea, during code development, to process only the first few lines of a file. That way you limit the amount of time that the program needs to process a file, and limit its output, which makes debugging easier. For instance, the code below process the first 10 lines of one of the longer files.


```python
def display_contents_file4(file_name):
    fp = open(file_name)
    count = 0
    while count < 10:
        buffer = fp.readline()
        if buffer == "":
            break
        print( buffer, end="" )
        count += 1
    fp.close()
    
display_contents_file4( "pc_amontillado.txt")
```

    THE CASK OF AMONTILLADO.
    
    THE thousand injuries of Fortunato I had borne as I best could; but
    when he ventured upon insult, I vowed revenge. You, who so well know the
    nature of my soul, will not suppose, however, that I gave utterance to
    a threat. _At length_ I would be avenged; this was a point definitively
    settled--but the very definitiveness with which it was resolved,
    precluded the idea of risk. I must not only punish, but punish with
    impunity. A wrong is unredressed when retribution overtakes its
    redresser. It is equally unredressed when the avenger fails to make
    

Once the program is finished and debugged, I can remove the references to `count` and change the loop to `while True`, to process the whole file.

**Exercise**: Start by copying the code above in the code block below. Then adapt it to count how often the word "fortunato" (with any capitalization) occurs in the text as a whole. Print only the number of occurrences of that word. If you do it correctly, you find the answer is 14 (it occurs 3 times in the first 20 lines).


```python
# Counting "fortunato".
def display_contents_file4(file_name):
    fp = open(file_name)
    count = 0
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        if 'fortunato' in buffer.lower():
            #print(count)
            #print( buffer, end="" )
            count += 1
    fp.close()
    return count
    
display_contents_file4( "pc_amontillado.txt")
```




    14



---

## Writing text files

Writing a text file is similar to reading. You open the file, write to it, and close it.

### Opening a file for writing

To open a file for writing, and writing only, you give the value "`w`" as the second argument to the `open()` function. If the file does not exist yet, it will create it. If it does exist, it will delete its contents.

Let me repeat that: **when you open a file for writing and it already exists, its contents are deleted**! There is no warning message saying "are you sure?" The file is simply emptied. So you have to be very, very careful when opening a file for writing. Usually I ask students to write their programs in such a way that they first check if a file exists before opening it for writing, and give an error message when it already exists. Functions for checking if a file exists are discussed later in this chapter.

### Writing using `write()`

To write something to a text file, you use the `write()` method with as argument a string that you want to write to the file. The example code below writes ten lines (`line1` to `line10`) to a file. It then opens the file, reads the contents, and displays them. Run the code and see what happens.


```python
fp = open( "pc_writetest.tmp", "w" )
counter = 0
while counter < 10:
    counter += 1
    text = "line" + str(counter)
    fp.write( text )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )
```

    line1line2line3line4line5line6line7line8line9line10
    

If you did what was asked, you have noticed that all the text is in the file, but it all is on one line. There are no newlines in between. The reason is that you have to explicitly write newline characters when you want newlines in your file. 

**Exercise**: Change the code above so that every line of text is on a separate line in the file that you write.

### Writing using `writelines()`

You can write a list of strings at once, by using the `writelines()` method that gets the list as argument. Each of the strings in the list must end in a newline character if you want those newline characters in the output file. `writelines()` is the opposite of `readlines()`; if you use the list that `readlines()` returns as argument for `writelines()`, the contents of the output file will be exactly the same as the contents of the input file.

Note that there is no `writeline()` method. `writeline()` would be exactly the same method as `write()`, so it is not needed.

### Practice

**Exercise**: In the code block below, write a program that reads the contents of "`pc_rose.txt`", and writes exactly the same contents to the file "`pc_writetest.tmp`". Then open the file "`pc_writetest.tmp`" and display the contents. You can easily construct this program by cobbling together some of the code given above. 


```python
# Copying pc_rose.txt
fp = open( "pc_rose.txt")
buffer = fp.read()
fp.close()
print('buffer')
print( buffer )

fp = open( "pc_writetest.tmp", "w" )
fp.write( buffer )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer2 = fp.read()
print('buffer2')
print( buffer2 )
```

    buffer
    'Tis but thy name that is my enemy.
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? That which we call a rose
    By any other name would smell as sweet.
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name;
    And for that name, which is no part of thee,
    Take all myself.
    
    buffer2
    'Tis but thy name that is my enemy.
    Thou art thyself, though not a Montague.
    What's Montague? it is nor hand, nor foot,
    Nor arm, nor face, nor any other part
    Belonging to a man. O, be some other name!
    What's in a name? That which we call a rose
    By any other name would smell as sweet.
    So Romeo would, were he not Romeo call'd,
    Retain that dear perfection which he owes
    Without that title. Romeo, doff thy name;
    And for that name, which is no part of thee,
    Take all myself.
    
    

---

## Appending to text files

"Appending" refers to writing at the end of an existing file. When you open a file for appending, the contents are not erased, but the file pointer is placed at the end of the file, where you can then write new data. You open a file in "append" mode by using "`a`" as the mode argument when opening the file.

The code below first displays the contents of "`pc_writetest.tmp`". It then appends ten new lines (`line11` to `line20`) to the file. Finally, it displays the contents of the new file. The function below is slightly better-structured than before, using a constant for the filename that is repeated three times in the program, and using a function to display the file contents as this functionality is needed twice.


```python
def display_contents( filename ):
    fp = open( filename )
    print( fp.read() )
    fp.close()

def write_and_append(filename):
    fp = open( filename, "a" )
    counter = 10
    while counter < 20:
        counter += 1
        text = 'line' + str(counter) + '\n'
        fp.write( text )
    fp.close()

file_name = "pc_writetest.tmp"

display_contents( file_name )
write_and_append( file_name )
display_contents( file_name )

```

    line1line2line3line4line5line6line7line8line9line10
    line1line2line3line4line5line6line7line8line9line10line11
    line12
    line13
    line14
    line15
    line16
    line17
    line18
    line19
    line20
    
    

---

## `os.path` methods

At this point you know everything you need to handle text files in Python. However, there are several handy functions that make your life easier when dealing with files. These are collected in the `os.path` module. As per usual, we will not list all of them, but the ones that you will use the most. These are not part of the official syllabus of the course.

In these functions, the term "path" refers to a filename or a directory name, complete with parent directories (and drive letter). The parent directories (and drive letter) do not *need* to be there explicitly, but even if they are not, implicitly they still are as each file and each directory is located in a particular place in the file system.

### `exists()`

The function `exists()` gets a path as argument, and returns `True` if that path exists, and `False` if it does not.


```python
from os.path import exists

def check_if_path_exists(file_name):
    if exists(file_name ):
        return( file_name + " exists" )
    else:
        return( file_name + " does not exist" )

print(check_if_path_exists("pc_rose.txt"))
print(check_if_path_exists("pc_tulip.txt"))

```

    pc_rose.txt exists
    pc_tulip.txt does not exist
    

### `isfile()`

`isfile()` tests if the path that is supplied as argument is a file. If it is, it returns `True`. If it is not, it returns `False`. If the path does not exist, the function also returns `False`.


```python
from os.path import isfile

def check_if_file_exists(file_name):
    if isfile( file_name ):
        return( file_name + " is a file" )
    else:
        return( file_name + " is not a file" )
    
print(check_if_file_exists("pc_rose.txt"))
```

    pc_rose.txt is a file
    

### `isdir()`

`isdir()` tests if the path that is supplied as argument is a directory. If it is, it returns `True`. If it is not, it returns `False`. If the path does not exist, the function also returns `False`.


```python
from os.path import isdir

def check_if_path_is_dir(file_name):
    if isdir( file_name):
        print( file_name + " Rose is a directory" )
    else:
        print(file_name + " is not a directory" )
check_if_path_is_dir("pc_rose.txt")
```

    pc_rose.txt is not a directory
    

### `join()`

`join()` takes one or more parts of a path as argument, and concatenates them reasonably intelligently to a legal name for a path. This means that it will add and remove slashes as needed. `join()` is particularly handy in combination with `listdir()`. 

The reason that `join()` is handy with `listdir()`, is that `listdir()` results in a list of file names that do not include the directory names. Usually, when you ask for a list of file names, you intend to open them at some point. But to open a file that is not in the current directory, you need to know the complete path name that leads to the file. When you apply `listdir()`, you know where you are looking for files, so you know the elements of the path name. To construct the complete path name for each file, you need to concatenate the elements of the path name to the file name. Rather than trying to decide where you need to add slashes, and which kind of slashes they need to be, you can leave all of that to the `join()` function.

The code below looks for all the files in the `pcdata` directory, and lists them including their complete path name. See how `join()` is used to construct that path name from the current directory, the `pcdata` directory, and the file name.


```python
from os import listdir, getcwd
from os.path import join

def display_contents_dir(directory):
    filelist = listdir( directory )
    for name in filelist:
        pathname = join( getcwd(), directory, name )
        print( pathname )
        
display_contents_dir("pcdata")
```

    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_bohemia.txt
    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_jeeves.txt
    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_woodchuck.txt
    

### `basename()`

`basename()` extracts the filename from a path, and returns it. 


```python
from os.path import basename

print( basename( "/System/Home/readme.txt" ) )
```

    readme.txt
    

### `dirname()`

`dirname()` extracts the directory name from a path, and returns it.


```python
from os.path import dirname

print( dirname( "/System/Home/readme.txt" ) )
```

    /System/Home
    

### `getsize()`

`getsize()` gets the size of the file that is supplied as argument, and returns it as an integer. The file must exist, otherwise you get a runtime error.


```python
from os.path import getsize

numbytes = getsize( "pc_rose.txt" )
print( numbytes )
```

    485
    

**Exercise**: In the code block below, write some code that adds up the sizes of all the files in the `pcdata` directory, and prints the result.


```python
# Add up file size.
from os import listdir, getcwd
from os.path import join, getsize

def add_up_size(directory):
    numbytes = 0
    filelist = listdir( directory )
    for name in filelist:
        pathname = join( getcwd(), directory, name )
        print( pathname )
        numbytes += getsize( pathname )
        print(getsize( pathname ))
    return numbytes
add_up_size("pcdata")
```

    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_bohemia.txt
    47605
    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_jeeves.txt
    37239
    E:\THIENDHB_GOOGLEDRIVE\MASTER TILBURG\DATA PROCESSING\NOTEBOOKS\pcdata\pc_woodchuck.txt
    195
    




    85039



---

## File encoding

Text files use an "encoding", i.e., a system that prescribes how characters in the files are supposed to be interpreted. This encoding may differ between operating systems. You can see the preferred encoding that your system uses with a call to `sys.getfilesystemencoding()`.


```python
from sys import getfilesystemencoding

print( getfilesystemencoding() )
```

    utf-8
    

If you read a text file which uses a different encoding than your file system prefers, you may get a `UnicodeDecodeError`. Whether or not you get this error for a particular file, is related to your operating system. An annoying consequence of that is that when you port Python code that reads a file to another system, a file that could be read by your code previously may cause your code to crash after the port.

An easy way to get around this problem is by adding an extra parameter when opening a file, which indicates the encoding mechanism that you want to use when reading the file. You do this by adding a parameter "`encoding=<encodingname>`", where `<encodingname>` is a string that can have a variety of values, for which some typical ones are:

    ascii       7-bits encoding, supports characters with values in the range 00-7F
    latin-1     8-bits encoding, supports characters with values in the range 00-FF
    mbcs        2-byte encoding, that is currently getting replaced by UTF-8
    utf-8       variable bytes encoding

Typically, text files are created with `ascii` or `latin-1` encoding. Since `ascii` is incorporated in `latin-1`, you can safely open any text file by specifying `latin-1` as encoding. It is possible that for the characters beyond the `ascii` range, you get different characters than the person who created the file wanted you to see -- that depends on the encoding mechanism that your file system uses. But at least the `UnicodeDecodeError` is avoided.

Note that while `utf-8` supports a much wider range of characters than `latin-1`, you may still get the `UnicodeDecodeError` when you read a text file that uses `latin-1` encoding on a system that uses `utf-8` encoding, as `utf-8` has no corresponding characters with values in the range 80-FF.

For example, the following code opens a file that has been created with `latin-1` encoding. This will give an exception on a system that uses `utf-8` as default encoding:


```python
def exemption_handling(file_name):
    fp = open( file_name )
    try:
        buffer = fp.readlines()
        output = ""
        for i in range(7):
            output += buffer[i]
        return(output)
    except UnicodeDecodeError:
        print( "A UnicodeDecodeError occurred" )
    finally:
        fp.close()
        
print(exemption_handling("pc_erlkonig.txt"))
```

    Erlkönig
    J.W. Goethe
    
    Wer reitet so spät durch Nacht und Wind?
    Es ist der Vater mit seinem Kind;
    Er hat den Knaben wohl in dem Arm,
    Er faßt ihn sicher, er hält ihn warm.
    
    

You can resolve this by simply specifying `latin-1` as encoding mechanism:


```python
def exemption_handling(file_name):
 
    fp = open( file_name, encoding="latin-1" )
    try:
        output = ""
        buffer = fp.readlines()
        for i in range(7):
            output += buffer[i]
        return output
    except UnicodeDecodeError:
        print( "A UnicodeDecodeError occurred" )
    finally:
        fp.close()
        
print(exemption_handling("pc_erlkonig.txt"))
```

    Erlkönig
    J.W. Goethe
    
    Wer reitet so spät durch Nacht und Wind?
    Es ist der Vater mit seinem Kind;
    Er hat den Knaben wohl in dem Arm,
    Er faßt ihn sicher, er hält ihn warm.
    
    

**Exercise**: If you change the encoding mechanism for this file to `utf-8`, it will enforce the `UnicodeDecodeError` as it contains characters with numbers in the range 80-FF. Try this.

If you want to see which special characters are supported with values in the range 80-FF on your system, run the code below. The numerical value of a character in the table can be derived by calculating `16*row+col`, whereby `row` and `col` are the hexadecimal row and column number, respectively. I do not display the characters in the range 80-9F, as these are normally not filled in.


```python
def exemption_handling(file_name):
 
    fp = open( file_name, encoding="utf-8" )
    try:
        output = ""
        buffer = fp.readlines()
        for i in range(7):
            output += buffer[i]
        return output
    except UnicodeDecodeError:
        print( "A UnicodeDecodeError occurred" )
    finally:
        fp.close()
        
print(exemption_handling("pc_erlkonig.txt"))
```

    A UnicodeDecodeError occurred
    None
    


```python
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 10, 16 ):
    print( chr( ord( 'A' )+i-10 ), end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

     0 1 2 3 4 5 6 7 8 9 A B C D E F
    A   ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ­ ® ¯
    B ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿
    C À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï
    D Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß
    E à á â ã ä å æ ç è é ê ë ì í î ï
    F ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ
    

---

## What you learned

In this chapter, you learned about:

- Text files
- File pointers
- Opening and closing files with `open()` and `close()`
- Reading files with `read()`, `readline()`, and `readlines()`
- Writing files with `write()` and `writelines()`
- Appending to files
- `os.path` methods `exists()`, `isfile()`, `isdir()`, `join()`, `basename()`, `dirname()`, and `getsize()`
- Dealing with text files with different encoding mechanisms

---

## Exercises

### Exercise 11.1

Write a function that receives the name of an input and an output text file as two strings. The function reads the contents of the input file, reverses each of the lines, and writes the reversed lines to the output file. The function does not return anything. You can use "`pc_rose.txt`" as a sample file to test your function:



```python
def reverse_lines(input_file, output_file):
    #reverse the lines in input_file, and write them to output_file
    # Open and read file
    fp = open( input_file )  
    buffer = fp.readlines()
    #for line in buffer:
        #print(line, end = '')
    #print('-----------------------')
    #print(f'len(buffer) = {len(buffer)}')
    #print('-----------------------')
    
    # Create reversed content
    reverse = ''
    for i in range(len(buffer)-1,0,-1):
        reverse += buffer[i]
        #print(buffer[i], end = '')
    #print('========================')
    fp.close()
    
    # Write file
    fp = open( output_file, "w" )
    fp.write( reverse )
    fp.close()
    return
reverse_lines("pc_rose.txt", "pc_writetest.txt")
```

### Exercise 11.2

Write a function that receives the name of an input and an output text file as two strings. The function reads the contents of the input file, counts the number of words in each line, and writes this number to the output file in a new line. The function does not return anything. You can use "`pc_rose.txt`" as a sample file to test your function:



```python
# Counting words line by line.
def count_line_words(input_file, output_file):
    #counts words in each line in input_file, and writes them to output_file
    # Open and read file
    fp = open( input_file )  
    buffer = fp.readlines()
    
    #print('-----------------------')
    #print(f'len(buffer) = {len(buffer)}')
    #print('-----------------------')   
        
    # Count words of each line
    count = ''
    for line in buffer:
        #print(line, end = '')
        count += str(len(line)-1) + '\n'
        #print(len(line)-1)

    #print('========================')
    fp.close()
    
    # Write file
    fp = open( output_file, "w" )
    fp.write( count )
    fp.close()
    return
    
count_line_words("pc_rose.txt", "pc_writetest2.txt")
```

### Exercise 11.3

In this directory you find a file `pc_bohemia.txt`. Write a program that processes the contents of this file, line by line. It creates an output file in the current working directory called `pc_bohemia.tmp`, which has the same contents as `pc_bohemia.txt`, except that all the vowels are removed (case-insensitively). At the end, display how many characters you read, and how many characters you wrote. If you want to check the contents of `pc_bohemia.tmp`, you can either open it in a text editor, or display the first 10 lines or so at the end of your program.


```python
# Removing vowels.
def remove_vowels(input_file, output_file):
    #removes vowels from each line in input_file, and writes them to output_file

    count = 0
    in_count = 0
    out_count = 0
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    text = ''
    fp = open(input_file)
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        in_count += len(buffer)
        #print(buffer, end = '')
        #print(f'len(buffer) = {len(buffer)}')
        #print(f'in_count = {in_count}')
        for i in vowels:
            if i in buffer:
                buffer = buffer.replace(i, '')
        out_count += len(buffer)
        #print('----------------')
        #print(buffer, end = '')
        #print(f'len(buffer) = {len(buffer)}')
        #print(f'out_count = {out_count}')
        text += buffer
        count += 1
        #print('*****************************')
    #print(text)
    print(f'in_count = {in_count}')
    print(f'out_count = {out_count}')
    fp.close()
    
    fp = open(output_file, 'w')
    fp.write(text)
    fp.close()
    return
    
remove_vowels("pc_bohemia.txt", "pc_bohemia.tmp")
```

    in_count = 46478
    out_count = 32840
    

### Exercise 11.4

Read the file with the names of the politicians.txt. Create two lists: One with the first names, and one with the last names. Return both two lists.


```python
def names_politicians(ifile):
    fp = open(ifile + ".txt")
    buffer = fp.readlines()
    first = ''
    last = ''
    for line in buffer:
        first += line.split()[0].strip() + ','
        last += line.split()[1].strip() + ','
    fp.close()
    return (first, last)

names_politicians("politicians")
```




    ('Xi,Vladimir,Donald,Angela,Jeff,Pope,Bill,Mohammed,Narendra,Larry,Jerome,Emmanuel,Mark,Theresa,Li,Warren,Ali,Mario,Jamie,Carlos,Jack,Christine,Doug,Tim,Elon,Benjamin,Ma,Larry,Akio,John,Antonio,Mukesh,Jean-Claude,Darren,Sergey,Kim,Charles,Shinzo,Rupert,Satya,Jim,Stephen,Khalifa,Haruhiko,Abdel,Li,Lloyd,Recep,Bob,Michel,Michael,Wang,Mary,Moon,Masayoshi,Bernard,Justin,Robin,Michael,Hui,Lee,Bashar,John,Enrique,Ken,Aliko,Mike,Qamar,Rodrigo,Abigail,Reed,Robert,Abu,Joko,Gianni,',
     'Jinping,Putin,Trump,Merkel,Bezos,Francis,Gates,Saud,Modi,Page,Powell,Macron,Zuckerberg,May,Keqiang,Buffett,Khamenei,Draghi,Dimon,Slim,Ma,Lagarde,McMillon,Cook,Musk,Netanyahu,Huateng,Fink,Toyoda,Flannery,Guterres,Ambani,Juncker,Woods,Brin,Jong-un,Koch,Abe,Murdoch,Nadella,Yong-Kim,Schwarzman,Al-Nahyan,Kuroda,el-Sisi,Ka-shing,Blankfein,Erdogan,Iger,Temer,Bloomberg,Jianlin,Barra,Jae-in,Son,Arnault,Trudeau,Li,Dell,Yan,Loong,al-Assad,Roberts,Nieto,Griffin,Dangote,Pence,Javed-Bajwa,Duterte,Johnson,Hastings,Mueller,al-Baghdadi,Widodo,Infantino,')



### Exercise 11.5

Read the file with the names of the politicians.txt. Save the names in a new text file (politicians_new.txt) after adding a column to each name indicating the total length of the name


```python
def length_names(ifile):
    fp = open(ifile + ".txt")
    buffer = fp.readlines()
    text = ''
    for line in buffer:
        length = len(line)
        text += line.replace('\n','') + ',' + str(length) + '\n'
    fp.close()
    
    fp = open(ifile + '_new.txt', 'w')
    fp.write(text)
    fp.close()
    return

length_names("politicians")
```

---

End of Chapter 11. 
