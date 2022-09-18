file_name = 'python/chapter9/chapter10/the music master.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'sorry the file'+file_name+'does not exist.'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('the file'+file_name+'has about '+str(num_words)+' words.')
