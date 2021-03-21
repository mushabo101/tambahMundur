while True:
    def tambahMundur(x,y):
            try:
                reversedx = 0
                reversedy = 0
                hasilreversed = 0 
                while x > 0 :#perulangan untuk reversed nilai x
                    reminder = x % 10
                    reversedx = (reversedx *10 ) + reminder
                    x = x // 10
                while y > 0 : #perulangan untuk reversed nilai y
                    reminder = y % 10
                    reversedy = (reversedy *10 ) + reminder
                    y = y // 10
            
                hasil = reversedx + reversedy #hasil reversed nilai x + y
                while hasil > 0 : #perulangan untuk hasil
                    reminder = hasil % 10
                    hasilreversed = (hasilreversed *10 ) + reminder
                    hasil = hasil // 10
                return hasilreversed #hasil yang disimpan 
            except ValueError:
                return 'Invalid Input'
               

    x = int(input('Masukkan angka 1 : '))
    y = int(input('Masukkan angka 2 : '))
    print(tambahMundur(x,y))

    



            