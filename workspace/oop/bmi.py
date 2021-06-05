'''   고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만   '''

class Bmi(object):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        index = self.weight / self.height **2 * 10000 # **2은 제곱 cm와 m의 차이 반영
        if index >= 35:
            bmi = "고도비만"
        elif index >=30:
            bmi = "중도비만"
        elif index >=23:
            bmi = "경도비만"
        elif index >= 18.5:
            bmi = "정상"
        else:
            bmi = "저체중"
        return bmi

    @staticmethod
    def main():
        while 1:
            menu = input('0-종료 1-bmi \n 입력 : ')
            if menu == '0':
                break
            elif menu == '1':
                height = int(input('키 : '))
                weight = int(input('몸무게 : '))
                bmi = Bmi(height, weight) #bmi를 인스턴스(객체)라고 한다.
                print(bmi.get_bmi())
            else:
                print('잘못된 접근')
                continue

Bmi.main()
