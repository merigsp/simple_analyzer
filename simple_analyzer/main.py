from analyzer import Analyzer 
import random
import time

with open("/Users/merigasparan/git/simple_analyzer/config/config.txt", "r") as f:
    int_val = int(f.readline().split('=', 1)[1][:-1])
    seq_len = int(f.readline().split('=', 1)[1])
    print(int_val)
    print(seq_len)
    
print("Starting Analyzer program…")
analyzer = Analyzer()
while True:
    r = random.randint(1,100)
    analyzer.add_number(r)
    if len(analyzer.my_list) > seq_len:
        analyzer.my_list.pop(0)
    print("Even count:", analyzer.even_count())
    print("Odd count:", analyzer.odd_count())
    print("Highest:", analyzer.highest_number())
    print("Increasing pairs:", analyzer.increasing_pairs())
    print()
    current_sec = time.localtime().tm_sec
    if len(analyzer.my_list) >= seq_len and current_sec == 0:
        print("Conditions met! Ending loop.")
        break
    time.sleep(int_val)
    