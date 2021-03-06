To make absolutely sure that the file object gets closed, you should call the
close() function as it is considered good programming practice. When the Python
program/script is running, it leaves the files open, if close() is not called
with a few exceptions. What we also learn here is that file objects use up
system resources which shouldn't be used anymore when the file operations are
already done, as this would be considered bad practice and a waste of system
resources while the code is running. So in most cases, Python takes care of
closing the file objects properly by itself, however, use the close() method in
combination with open(). There is no reason not to use it.
