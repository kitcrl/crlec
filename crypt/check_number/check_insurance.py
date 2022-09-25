print(' 건강보험등록번호 검증 ');
insura_n = input(' 번호 10자리 : ');
insura = 0;

check_n = [3,5,7,9,3,5,7,9,3,5];


for i in range(len(check_n)):
    insura += int(insura_n[i]);

r = insura%11;

x11 = (11-r)%10;

print(' 검증 결과 ');
print( x11 );
