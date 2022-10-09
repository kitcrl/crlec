print(' [신용카드번호 검사숫자 계산] ');
card_n = input(' 신용카드번호 앞 15자리를 입력하세요 : ');
check_n = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2];
card = 0;
h = 0;
#h = (위 card_n = input 에서 입력한 15개의 숫자 중, 홀수번째에 있는 숫자 중에서 5 이상인 숫자의 개수) 
for i in range(len(card_n)):
    if ( i%2 == 0 ):
        if ( int(card_n[i]) >= 5 ) :
            h += 1;

for i in range(len(check_n)): 
    card += int(card_n[i])*int(check_n[i]);

x16 = (10-(card+h)%10)%10;

print(' 입력하신 신용카드번호의 끝자리는 다음과 같습니다 ');
print( x16 );
