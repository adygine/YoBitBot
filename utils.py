def generate_as_file(name='noname.txt', include=''):
    with open(name,'w') as file:
        file.write(include)