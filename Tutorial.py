import time  # time 모듈 도입

print("튜도리얼을 시작하겠습니다.")
time.sleep(1)
print()
print("당신은 수비입니다.")
time.sleep(0.8)
print()
print("타자에게 던질 세자리 수를 입력해 보겠습니다.")
print("세자리 수를 던질 때는 1~9 중에서 서로 다른 세 수를 선택해야 합니다.")

while True:    #투수의 역할을 연습하기 위한 것으로 '3 6 5'를 입력하게 되면 while문을 빠져나감.
    tutorial_pitch=input('3 6 5를 입력하세요 : ')
    if tutorial_pitch=='3 6 5':
        break

print("타자에게 365를 던졌습니다.")
time.sleep(0.7)
print()
print("타자가 일루타를 쳤습니다.")
time.sleep(1)
print()
print("수비를 해보겠습니다.")
time.sleep(0.7)
print()
print("당신이 던진 세자리수와 타자가 예측한 세자라수의 오차는 얼마일지 예측해봅시다.")
print()

while True:     #수비 연습을 하기 위한 것으로 '87'을 입력하게 되면 while문을 빠져나감.
    tutorial_defense=input("87을 입력해주세요 : ")
    if tutorial_defense=='87':
        break

print()        
time.sleep(0.7)        
print("OUT")        
print("수비를 성공하였습니다.")
time.sleep(0.7)
print()
print("당신이 예측한 오차와 실제 오차의 차이가 50 이하일 경우 수비 성공,\n100 초과일 경우 수비 실패,\n그 사이일 경우 다시 한 번 예측기회가 주어집니다.")
time.sleep(0.7)   
print()
print("3개의 아웃을 잡아내면 공수가 교대됩니다.")
time.sleep(1)
print()
print()
print("이번에는 공격을 연습해보겠습니다.")
time.sleep(0.7)
print()
print("상대편 투수가 세자리수를 던졌습니다.")
print("상대편 투수가 던진 세자리수의 각 자릿수 합은 9입니다.")
time.sleep(0.2)
print("어떤 수일지 예측해볼까요?")
time.sleep(0.7)
print()
print("타자도 마찬가지로 1~9 중에서 세 숫자를 골라야 합니다.")
print("투수가 던진 공의 합을 맞출 필요가 없으니 전략적으로 활용하세요!"

while True:    #타자 역할을 연습하기 위한 것으로 '5,1,3'을 입력하면 while문을 빠져나감.
    tutorial_attack=input("5,1,3을 입력해주세요 : ")
    if tutorial_attack=='5,1,3':
        break

print()        
time.sleep(0.7)        
print("HomeRun!")
time.sleep(0.7)
print("축하합니다. 홈런입니다.")
time.sleep(1)
print()
print("당신은 이제 게임을 할 준비를 마치셨습니다.")
time.sleep(0.7)
print("튜토리얼을 종료하고 게임을 시작하세요!")

