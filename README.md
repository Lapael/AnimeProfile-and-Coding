# AnimeProfile-and-Coding

## 개요
- 애니 프사와 코딩 스킬 간의 상관관계 분석

## 데이터셋
- leetcode(`https://leetcode.com/`) 랭킹 페이지 크롤링
- 사용자 랭킹, 프로필 사진 URL, 대회 참여 횟수
- google cloud vision api를 통해 프로필 사진 labeling
- label들에 애니 관련 keyword(Anime, Animation, Animated cartoon, Cartoon)에 해당되는 수 만큼 저장
- rankings / contests / ani_num 형식의 csv 작성
- rankings : 랭킹
- contest : 대회 참여 횟수
- ani_num : 애니 키워드 수 (높을수록 더욱 씹덕일 확률 높을듯)

## 분석
### Cell 1:
- 데이터 불러오기
- 데이터 수 출력 - 119,623
- ani_group 생성 : non-anime, anime 구분용
- ani_type 생성 : basic(기본 프사), normal(일반 프사), anime 구분용

### Cell 2:
- 전체 데이터셋을 n등분 한 뒤
- 상위 1분할, 상위 2분할, 상위 3분할, ..., 상위 n분할의 애니프사 비율 도식화
- -> 상위권일수록 애니프사 비율이 큼

### Cell 3:
- anime와 non-anime의 rankings, contests 전체 평균 비교
- -> 애니프사 그룹은 일반프사 그룹보다 평균 등수가 약 22,000등 높음
- -> 애니프사 그룹은 일반프사 그룹보다 평균 대회 참여 횟수가 약 4번 많음

### Cell 4:
- anime와 non-anime의 rankings, contests 분할별 평균 비교
- -> 애니프사 그룹은 일반프사 그룹보다 평균 등수가 높음, 상위권일수록 격차가 큼
- -> 애니프사 그룹은 일반프사 그룹보다 평균 대회 참여 횟수가 높음, 상위권일수록 격차가 큼

### Cell 5:
- ani_num에 따른 랭킹 비교 - 최소제곱선
- -> ani_num이 클수록 평균 등수가 높음
- -> 추가로 일반프사는 고르게 분포된 반면, 애니프사는 랭킹의 양 극단에 유독 많이 분포한다는 것을 알 수 있음
