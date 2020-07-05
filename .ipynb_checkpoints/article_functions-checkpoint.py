import statistics as stat

def read_article(name):
    try:
        with open('article.txt', 'r') as f:
            read_data = f.read()
    except FileNotFoundError:
         print("There is no file with name")
    return read_data

def count_int_and_letters(read_data):
    numbers = []
    letters = 0
    for letter in read_data:
        try:
            num = float(int(letter))
            numbers.append(num)
            mean = stat.mean(numbers)
        except  ValueError:
            letters += 1
    print(f'Среднее значение {mean:.3}')
    print(f'Общее количество букв {letters}')
            
            
        
        
    