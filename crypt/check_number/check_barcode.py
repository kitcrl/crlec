print(' 바코드 검증 ');
#barcode_n = input(' 바코드 12자리 : ');
#barcode_n = [9,7,9,1,1,9,2,2,2,3,7,8];
barcode_n = [2,1,0,0,0,0,0,2,0,2,2,9];
barcode = 0;

for i in range(len(barcode_n)): # i :  0 ~ 11
    if ( i%2 == 0 ) :
        barcode += 3*int(barcode_n[i]);
    else :
        barcode += int(barcode_n[i]);

x13 = (10-barcode)%10;
print( x13 );
