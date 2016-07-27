# ---- The basics of text files ----- # 

# 'r' means read-only
file_for_reading = open('reading_file.txt', 'r')

# 'w' is write - will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append - for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# this closes your files when you're done
file_for_writing.close()


# b/c its easy to forget to close your files, you should always use them in a with block, at the end of which they will be closed automatically:
with open(filename,'r') as f:
  data = function_that_gets_data_from(f)

# at this point f has already been closed, so don't try to use it
process(data)

# if you need to read a whole text file:
#     - iterate over the lines of the file using for:

starts_with_hash = 0

with open('input.txt','r') as f: 
  for line in file:                                                 # look at each line in the file
    if re.match("^#",line):                                         # use a regex to see if it starts with '#'
      starts_with_hash += 1                                         # if it does, add 1 to the count


