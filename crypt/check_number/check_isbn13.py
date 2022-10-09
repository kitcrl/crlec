print(' ISBN 13자리 검증 ');
isbn_n = input(' ISBN 12자리 : ');
check_n = [1,3,1,3,1,3,1,3,1,3,1,3];
isbn = 0;

for i in range(len(isbn_n)):
    isbn += (int(check_n[i])*int(isbn_n[i]));

x13 = 10-(isbn%10);

print(' 검증 결과 ');
print( x13 );
