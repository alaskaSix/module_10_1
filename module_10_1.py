from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_1 = datetime.now()
time_re1 = time_1 - time_start1
print(time_re1)

time_start2 = datetime.now()
thr_1 = Thread(target=write_words, args=(10, "example5.txt"))
thr_2 = Thread(target=write_words, args=(30, "example6.txt"))
thr_3 = Thread(target=write_words, args=(200, "example7.txt"))
thr_4 = Thread(target=write_words, args=(100, "example8.txt"))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_2 = datetime.now()
time_re2 = time_2 - time_start2
print(time_re2)