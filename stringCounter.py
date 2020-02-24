def am_counter(string, substring):
    string = string.lower()
    a = string.split(' ')
    print( a.count(substring))

am_counter('am i in amsterdam', 'am')
