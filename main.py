'''

클래스 명 : main.py 

설명 : 깃허브 테스트 일환으로 git fork, commit, pull request에 대해 스터디합니다.

작성일 : 2022.02.24

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
- Student class가 필요합니다
    - 생성자에는 이름이 들어가야 합니다.
    - hello() 함수가 있으며 실행할 시, 이름이 출력됩니다.
- Teacher class가 필요합니다.
    - 생성자에는 영어 이름이 들어가야합니다.
    - hi() 함수가 있으며 실행할 시, 이름이 출력되야합니다.

Fixme > 
- 테스트 입니다.
'''


from Teacher import Teacher


if __name__ == "__main__":
    print("test")
    teacher = Teacher("mingyu")
    teacher.hi()