def write_file(file_name, file_content):
    our_file = open(f'{file_name}.txt', mode='w', encoding= 'utf-8' )
    our_file.write(file_content)
    pass

def append_file(file_name, append_content):
    our_file = open(f'{file_name}.txt', mode='a', encoding= 'utf-8' )
    our_file.write(append_content)
    pass

def read_file(file_name):
    our_file = open(f'{file_name}.txt', mode='r', encoding= 'utf-8' )
    return our_file.read()
    
