print(' 여권번호 검증 ');
passport_n = input(' 여권번호 6자리 : ');
check_n = [7,3,1,7,3,1];
passport = 0;

for i in range(len(check_n)): # i :  0 ~ 11
    passport += int(passport_n[i])*int(check_n[i]);

x7 = passport%10;

print(' 검증 결과 ');
print( x7 );
