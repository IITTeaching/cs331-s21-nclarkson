import urllib
import requests
import queue
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    btxt = urllib.request.urlopen(book_url).read().decode()
    bascii = btxt.encode('ascii','replace')
    return bascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = radix_sort()
    proper = sorted(book_to_words())
    arr = []
    for i in range(len(lst)):
        arr.append(lst[i].decode("ascii"))
    return arr

def itemsToQueues(words,k,maxlen):
    temp = [None] * 256
    for i in range(0,256):
        temp[i] = []
    for j in range(0,len(words)):
        pos = get_pos(words[j], k, maxlen)
        temp[pos].append(words[j])
    return temp

def get_pos(word, k, max):
    pos = max - k - 1
    if pos >= len(word):
        return 0
    else:
        return word[pos]

def queuesToArray(queues,numWords):
    words = [ [] for i in range(numWords) ]
    ind = 0
    for i in range(0, len(queues)):
        cur = queues[i]
        while len(cur) > 0:
            words[ind] = cur.pop(0)
            ind += 1
    return words

def radix_sort():
    lw = calc_lenest_word()
    words = book_to_words()
    for i in range(0,lw):
        words = queuesToArray(itemsToQueues(words,i,lw),len(words))
    return words

def calc_lenest_word():
    max = 1
    lst = book_to_words()
    for i in lst:
        if(len(i) > max):
            max = len(i)
    return max

################################################################################
# TEST CASES
################################################################################

def test_book():
    arr = []
    w = book_to_words()
    for i in range(len(book_to_words())):
        arr.append(w[i].decode("ascii"))
    arr = sorted(arr)
    lst = radix_a_book()
    n = 0
    for i in range(len(arr)):
        if not arr[i]==lst[i]:
            print("Python Sort")
            print(arr[i])
            print()
            print("Radix Sort")
            print(lst[i])
            raise Exception
        n+=1
        print("Correct Comparisons = " + str(n))
    return True


def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_book]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
