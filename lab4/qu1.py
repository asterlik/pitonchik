def create_file_reader(filename):
    file = open(filename, 'r', encoding='utf-8')
    
    def read_next_line():
        line = file.readline()
        if line:
            return line.rstrip('\n') 
        else:
            file.close()
            return None 
    
    return read_next_line

if __name__ == "__main__":
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("привет, это первая строка\nа это вторая строка\nи наконец третья")
    

    get_line = create_file_reader('test.txt')
    
    print(get_line())  
    print(get_line())  
    print(get_line()) 