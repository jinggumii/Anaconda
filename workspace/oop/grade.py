
class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avg())

        if score >= 90:
            grade = 'A'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade

    @staticmethod
    def main():

        while 1:
            menu = input('0-종료 1-학점')
            if menu == '0':
                break
            elif menu == '1':
                kor = int(input('국어 : '))
                eng = int(input('영어 : '))
                math = int(input('수학 : '))
                grade = Grade(kor, eng, math)
                print(f'학점 : {grade.get_grade()}')
            else:
                print('이상 접근')
                continue

Grade.main()