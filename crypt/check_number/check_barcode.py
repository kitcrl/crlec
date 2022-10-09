print(' 바코드 검증 ');
barcode_n = input(' 바코드 12자리 : ');
barcode = 0;

for i in range(len(barcode_n)): # i :  0 ~ 11
    if ( i%2 == 0 ) :
        barcode += int(barcode_n[i]);
    else :
        barcode += 3*int(barcode_n[i]);

x13 = (10-barcode)%10;
print( x13 );
