def digital_root(n):
    while n > 10:
        str_n = list(str(n))
        int_list = [int(n) for n in str_n]
        n = 0    
        for i in range( len(int_list)):
            n = n + int_list[i]
            i+=1
    else:    
        print(n)


digital_root(2516)  