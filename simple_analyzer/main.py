with open("/Users/merigasparan/git/simple_analyzer/config/config.txt", "r") as f:
    int_val = f.readline().split('=', 1)[1][:-1]
    seq_len = f.readline().split('=', 1)[1][:-1]
    print(int_val)
    print(seq_len)