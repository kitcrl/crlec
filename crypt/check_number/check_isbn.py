print(' ISBN 검증 ');
isbn_n = input(' ISBN 12자리 : ');
isbn = 0;

for i in range(len(isbn_n)):
    isbn += ((i+1)*int(isbn_n[i]))%11;

x10 = isbn%11;

print(' 검증 결과 ');
if ( x10 == 10 ) :
    print('X');
else:
    print( x10 );
