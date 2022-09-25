print(' 주민등록번호 검증 ');
jumin_a = input(' 주민등록번호 앞자리 : ');
jumin_b = input(' 주민등록번호 뒷자리 : ');

jumin_n = jumin_a + jumin_b;
check_n = [2,3,4,5,6,7,8,9,2,3,4,5];
jumin = 0;

for i in range(len(check_n)): # i :  0 ~ 11
    jumin += int(jumin_n[i])*int(check_n[i]);

r = jumin%11;
x13 = (11-r)%10;

print(' 검증 결과 ');
print( x13 );
