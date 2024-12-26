# GDGoC Hongik 프로젝트 트랙 3기 미션 코스

안녕하세요, GDGoC Hongik Organizer 이혁입니다.

지난 [2주차 README](README_week2.md)는 옮겨놓았으니 추후 참고 부탁드려요. 2번째 미션도 잘 마무리하셨나요? 지난 번에는 코드보다는 개념을 배우는게 많아서 약간은 지루하셨을 수도 있을 거 같아요.

이번 주차도 역시 여태까지 배우고 정리한 내용을 발전시켜서 진행할 예정이에요. 마지막 미션까지 화이팅합시다!

> **안내 사항**
>
> - 최하단에 기재된 [폴더 구조](#폴더-구조) 형식에 맞춰서 파일을 만들어주세요.
> - 레포지토리를 Fork한 이후, 최대한 빠른 시일 내에 PR을 올려주세요. 이후 Push를 진행해도 되니 운영진이 미션 진행 여부를 확인할 수 있도록 해주세요.
> - 레포지토리는 무조건 Public으로 Fork해주세요. Private으로만 진행하면 운영진이 과제 피드백에 어려움을 겪을 수 있어요.
> - 이번 주에 배우는 내용들도 블로그에 꼭 회고록과 함께 정리해주시고, 해당 링크를 제출해주세요.
> - [GitHub 과제 제출 가이드라인](https://www.gdschongik.com/project-track/3/guide/github)을 준수하여 진행해주세요.

## [메인 미션] API를 실제로 구현해보자.

> **학습 목표**
>
> - Django REST framework를 통해 API 명세의 API들을 구현할 수 있다.

2주차 미션으로 진행했던 API 명세를 기반으로 실제 API를 구현해봐요. 아래 미션 내용을 참고하여 실제로 어떻게 프론트엔드와 소통할 수 있을지를 확인해요.

[Django를 이용한 회원 관리 API 구현 명세](django_api_specification.md)

## 폴더 구조

```bash
.
├── README.md
└── mission_course
    ├── manage.py
    └── mission
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
# 미션을 수행하기 위해 필요한 파일을 자유롭게 추가해주세요.

# 가상 환경을 모두 올리지 않도록 주의해주세요.
```
