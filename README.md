# 2024fastAPI
fastAPI를 이용한 붓꽃분류시스템, 영화추천시스템 / 2024 3-1 캡스톤프로젝트2

<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
<!--   https://simpleicons.org/
  <img src="https://img.shields.io/badge/[아이콘 검색]-[색상코드]?style=for-the-badge&logo=[아이콘 검색]&logoColor=white"> -->

  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>


# 붓꽃분류 시스템 
### 결과물
<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/5ae541ca-338e-4b70-a22c-01304796af0c" width="600" height="300"/>

최종적으로 위와 같이 각각의 값들을 입력한 후 '붓꽃 종류 예측하기' 버튼을 클릭하면 각각 붓꽃들의 예측 값을 알려주고 파이차트를 통해 효과적으로 시각화하여 표현하는 사이트를 제작하였다


<details>
<summary>개발환경</summary>

annotated-types==0.6.0  
anyio==4.3.0  
click==8.1.7  
colorama==0.4.6  
exceptiongroup==1.2.0  
fastapi==0.110.0  
h11==0.14.0  
idna==3.6  
joblib==1.3.2  
numpy==1.26.4  
pandas==2.2.1  
pydantic==2.6.3  
pydantic_core==2.16.3  
python-dateutil==2.9.0.post0  
pytz==2024.1  
scikit-learn==1.4.1.post1  
scipy==1.12.0  
six==1.16.0  
sniffio==1.3.1  
starlette==0.36.3  
threadpoolctl==3.3.0  
typing_extensions==4.10.0  
tzdata==2024.1  
uvicorn==0.27.1  
</details>




# 영화추천시스템

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/974420eb-e1c3-461b-9e03-7e3568107eb3" width="700" height="350"/>


위 사진은 사이트에 최초 접속하였을때의 화면이다.
사용자가 어떤 영화를 좋아할 지 모르기에 랜덤한 영화 10가지를 보여주도록 설정해두었다.

---

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/5d608637-e54c-4f4d-945f-c983636a4897" width="700" height="350"/>

위 사이트는 포스터를 클릭하면 imdb의 사이트로 이동하게 된다.
포스터를 클릭 할 수 있다는 것을 알려주기 위해 상호작용을 추가하여 마우스를 포스터위에 올렸을때 마우스의 모양을 변화시키고 포스터의 밝기를 높여 클릭이 가능하다는것을 표현했다.

---

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/cb61a623-c217-4f8f-b9f4-1c41b8da1e90" width="700" height="350"/>

imdb에서 제공하는 장르들을 모두 기입하여 원하는 장르의 영화 10가지를 추천 받을 수 있도록 기능을 구현하였다.

---

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/bb216054-a665-4a78-9641-0b3a14744b51" width="700" height="350"/>

위 기능에서 장르를 선택하면 사진과 같이 장르 추천 영화 10가지가 출력된다.

---

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/e9558425-ae24-4d61-b680-8cded9263a73" width="700" height="350"/>

영화 id를 기입하면 해당 영화에 기반한 영화 10가지를 출력해준다.

---

<img src="https://github.com/smallbrowndog/2024fastAPI/assets/136410944/2cb18cea-1f1b-42f4-adcb-1fef88e5b50f" width="700" height="350"/>

영화 id와 해당 영화의 평점을 위 형식으로 기입하면 해당 영화와 평점에 기반한 영화 10가지를 출력해준다.
해당 기능은 정확히 동작하지 않아 보완이 필요할 것 같다.

---

<details>
<summary>개발환경</summary>

annotated-types==0.6.0  
anyio==4.3.0  
certifi==2024.2.2  
charset-normalizer==3.3.2  
click==8.1.7  
colorama==0.4.6  
exceptiongroup==1.2.0  
fastapi==0.110.0  
h11==0.14.0  
idna==3.6  
implicit==0.7.2  
numpy==1.26.4  
pandas==2.2.1  
pydantic==2.6.4  
pydantic_core==2.16.3  
python-dateutil==2.9.0.post0  
pytz==2024.1  
requests==2.31.0  
resolver==0.2.1  
scipy==1.12.0  
six==1.16.0  
sniffio==1.3.1  
starlette==0.36.3  
threadpoolctl==3.4.0  
tqdm==4.66.2  
typing_extensions==4.10.0  
tzdata==2024.1  
urllib3==2.2.1  
uvicorn==0.28.1  
</details>


