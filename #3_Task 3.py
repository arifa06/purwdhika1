def odd_even():
    x = [1,3,2,2,1,5,1,24,12,124,12,21,32,15]
    
    odd = [1,1,1,3,5,15,21]
    odd.sort()

    even = [2,2,12,24,32,124]
    even.reverse()

    print('sort_odd_even('+str(x)+')')
    print(odd+even)

odd_even()