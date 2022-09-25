print(' 운전면허번호 검증 ');
drive_n = input(' 번호 8자리 : ');
drive = 0;

for i in range(len(drive_n)):
    drive += ((10-(i+1))*int(drive_n[i]))%10;

x10 = drive%10;

print(' 검증 결과 ');
print( x10 );
