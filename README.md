# MSA로 구현한 중고거래 사이트
## 💻Function
1. 검색(ELK)
2. 로그인/회원가입
3. 댓글
4. 거래

- - - -
## 💡Role
> 1. JWT 토큰을 이용한 로그인, 회원가입 구현  
> 2. 용도(삽입,삭제,수정,조회)에 따라 Database 분리  
> 3. Kafka를 사용해 분리된 Database간 동기화  
> 4. 매물 관련 Kafka, Zookeeper, MySQL 서버 Docker를 사용해 어떤 환경에서든 운영   

- - - -
## 🖥Tech Stack
￼![기술스택](https://user-images.githubusercontent.com/57867611/116672094-ba64ce80-a9dc-11eb-966f-631e25dbd8d5.png)

1.  Django Framework: MSA로 서비스를 설계할 때 장고와 FLASK 중 어떤 프레임워크를 사용할지 고민했으나, 개발 기간이 짧아 익숙하고 바로 개발에 들어갈 수 있는 장고를 선택했다. 하지만 개발을 계속하면서 FLASK보다 장고에서 API를 구현하는데 어렵다는 것을 느꼈다. 다음 MSA로 서비스를 구현할 때는 FLASK 또는 Java Spring을 사용할 것이다.

2. MySQL: 처음에 개발할 때는 MariaDB를 사용해 데이터베이스를 구축했으나, Date의 입력형식이 MariaDB에서는 오류가 발생하고 MySQL에서는 문제가 없었다. 개발 초기라 교체하는데 무리가 없었지만, 만약 개발이 어느정도 진행된 상태에서 이런 상황이 발생했다면 개발 일정에 큰 차질이 생겼을 것이다. 앞으로는 개발에 들어가기전 필요한 기술에 대한 조사를 철저히 해야겠다고 느꼈다.

3. Github: 4명의 팀원들과 프로젝트의 변경사항을 관리하고, 프로젝트 병합을 위해 Github을 사용했다.  각자 맡은 모듈(기능)을 구현하고 완벽하게 동작할 경우에 브랜치(모듈명으로 작성)로 올려, 개발 중간중간 모듈들을 합쳐 나아갔다.

4. Kafka: 용도에 따라 데이터베이스를 분리하고 데이터베이스간 동기화를 위해 Kafka를 사용했다. 동기화를 통해 데이터베이스를 분리함으로써, 기존에 하나의 DB로의 접근을 용도에 따라 접근하는 DB를 다르게해 MSA 취지에 맞도록 모듈-DB를 구현할 수 있었다. 아직 Broker, Group 등 Kafka의 여러 기능을 사용해 보지는 못했지만, 공부해 서버 로그를 수집하고, 분석하는 모듈에 Kafka를 사용해 구현할 것이다.

5. Docker: 각 모듈들을 각자의 로컬환경(Window, Mac)에서 개발하고 AWS에서 전체 모듈이 운영되도록 개발하기 위해 도커를 사용했다. 기존에 이미지가 있을 경우는 Docker Hub의 이미지를 사용하고, 이미지를 없을 경우 직접 도커 이미지를 만들었다. 또한 이미지를 생성한 뒤 여러 모듈을 한번에 동작시키기 위해 Docker-Compose 파일을 작성해 운영의 편의성을 더했다.
[Docker-compose] (https://github.com/ShinhyeongPark/MSA-project/blob/main/data/docker-compose.yaml)

- - - -
## 📁PIP List
1. bycrypt:
: 비밀번호를 원본 상태로 저장할 경우 보안상 매우 취약하다. 이를 보완하기 위해 비밀번호를 해시화(암호화)를 위한 라이브러리

2. djangorestframework : 회원정보와 매물정보를 위한 REST API 서버를 구축하기 위한 라이브러리

3. djangorestframework-jwt: 로그인을 통해 발급되는 토큰을 생성하고, 이 토큰을 통해 페이지를 이동을 위한 접근을 판단하는 기능을 구현

4. elasticsearch: 검색 모듈에 사용되는 elasticsearch과 장고의 파이썬을 연결하기 위해 필요한 라이브러리

- - - -
## ⚙️시스템 구성도
![시스템구성도](https://user-images.githubusercontent.com/57867611/116672145-cbaddb00-a9dc-11eb-91cd-c6d7911f5c4d.png)
- Consul을 통해 각 서비스간 통신을 하게 해주고, 각 서비스의 위치(IP)를 찾는 용도로 사용했다.
- 각 서비스를 포트별로 운영하고, 각 데이터베이스에는 API를 통해 접근한다.
- 매물 데이터베이스 같은 경우에는 Kafka를 사용해 동기화하고, 만약 한쪽에 이상이 있을 경우 다른 한쪽에서 운영하게 함으로써 오류로 인한 서버 정지에 대비한다.
- 모듈, Consul, Database, Kafa를 도커로 운영한다. 
- - - -
## 📚요구사항 분석
[요구사항 분석서] (https://github.com/ShinhyeongPark/MSA-project/blob/main/data/요구사항분석서.pdf)
- - - -
## ✏️API 설계
[API설계] (https://github.com/ShinhyeongPark/MSA-project/blob/main/data/API설계.pdf)
- - - -
## 📌ERD
![ERD](https://user-images.githubusercontent.com/57867611/116672171-d4061600-a9dc-11eb-9519-fb0a77f2f7b7.png)
[테이블설계] (https://github.com/ShinhyeongPark/MSA-project/blob/main/data/Table설계.pdf)