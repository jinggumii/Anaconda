class Calculator(object):

    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    ''' 일반 메소드에서 정의한 기능을 호출해서 실제 연산하는 메소드 : 스태틱메소드 '''
    @staticmethod
    def main():
        while 1:
            menu = input('\n0-Exit 1-Calculate\n')
            if menu == '0':
                break
            elif menu == '1':
                first = int(input('첫 번째 수 : '))
                second = int(input('두 번째 수 : '))
                calc = Calculator(first, second)
                print(f'{calc.first} +  {calc.second} = {calc.add()}')
                print(f'{calc.first} -  {calc.second} = {calc.sub()}')
                print(f'{calc.first} *  {calc.second} = {calc.mul()}')
                print(f'{calc.first} /  {calc.second} = {calc.div()}')
            else:
                print('잘못 선택')

if __name__ == '__main__':
    Calculator.main()
