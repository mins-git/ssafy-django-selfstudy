# PJT 회원제 커뮤니티 게시판 구현

### 오늘 pjt 를 통해 배운 내용

1. API 요청 흐름 이해
    - API 요청의 전체적인 흐름을 실제 구현을 통해 직접 확인하고 이해할 수 있었습니다.

2. 쿼리 최적화 기법
    - prefetch_related()를 사용하여 ManyToManyField의 데이터를 효율적으로 로드하는 방법을 학습했습니다.
    - 불필요한 데이터베이스 쿼리를 줄이는 방법에 대해 고민하고 실제로 적용해 보았습니다.


3. 성능 고려사항
    - 작은 규모의 프로젝트에서도 데이터베이스 쿼리 최적화의 중요성을 인식했습니다.
    - board.like_users.all()과 같은 메서드 호출이 성능에 미치는 영향을 분석했습니다.

4. 코드 리팩토링
    - 기존 코드를 유지하면서도 성능을 개선하는 방법을 고민하고 적용했습니다.
    - set()을 활용하여 데이터 처리 효율성을 높이는 방법을 익혔습니다.

5. 문제 해결 능력 향상
    - 성능 문제를 인식하고, 해결 방안을 고민하여 실제로 적용하는 과정을 경험했습니다.
    - 기술적 고민을 논리적으로 정리하고 표현하는 능력을 기를 수 있었습니다.


## A. ManyToManyField가 적용된 views에서 M:N 참조 시 쿼리 최적화에 대한 고민

* 주요 과제: `boards/views.py`의 `likes` 함수 구현 과정에서 발생한 성능 최적화 고민

* 구체적 상황: 특정 게시물(`board`)에 좋아요를 누른 `User`들을 조회할 때, `board.like_users.all()`의 사용이 잠재적인 성능 문제를 야기할 수 있다는 인식

* 최적화 목표: `board.like_users.all()` 대신 더 효율적인 쿼리 방법을 모색하여 데이터베이스 접근 최소화 및 전체 성능 향상


* 결과 : `prefetch_related('like_users')를 사용함.`
  

  * 기억해볼 부분

    ```python
    # 기존 코드
    def likes(request, board_pk):
    board = Board.objects.get(pk=board_pk)

    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('boards:detail', board_pk)
    ```

  * 고민한 부분
    - 위 코드에서 board.like_users.all()를 사용하게 되면, 호출 시마다 데이터베이스에 쿼리가 실행될 것이라 생각하게 됨. 결과적으로 불필요한 쿼리 요청을 반복적으로 사용할 수 있지 않을까에 대한 고민을 하게 됨.
    - ManyToManyField를 사용하는 데 있어 board.like_users.all()이 성능 면에서 적절한 코드인지에 대한 고민을 함.

  * 고민 및 해결 방법

    * 고민:
        - ManyToManyField의 데이터를 불러오는 과정에서 성능 문제가 발생할 수 있다는 점을 인식함.
        - likes 함수에서 board.like_users.all()을 호출할 때, ManyToMany 관계에서는 관련된 데이터를 불러오기 위해 여러 쿼리가 발생할 수 있음.
        - like_users.all()을 호출할 때마다 데이터베이스에 쿼리가 실행되어, 불필요한 쿼리 요청이 반복적으로 수행되는 성능 저하 문제가 발생할 수 있을 것이라 생각함.
    * 해결 방법:

        - 쿼리 최적화: prefetch_related를 사용하여 ManyToManyField의 데이터를 미리 로드하고, 필요한 시점에만 쿼리를 수행하도록 최적화함. 이는 board.like_users를 참조할 때 발생할 수 있는 성능 문제를 해결할 수 있음.
        - prefetch_related()를 사용하여 ManyToManyField의 데이터를 미리 불러와, 이후 board.like_users를 참조할 때 추가적인 쿼리 요청을 줄임. 이 방법은 필요한 데이터를 한 번에 메모리로 불러와 이후의 반복적인 데이터베이스 쿼리를 방지함. 결과적으로 성능이 크게 향상되고, 참조 과정에서 고민하던 부분도 해결됨.
        - 코드 간소화: 기존 코드를 유지하면서도 조건을 명확히 하고, 참조가 제대로 이루어지도록 작성함.

  * 작은 프로젝트에서도 쿼리 문제가 발생할 수 있다고 생각한 이유:

    - Django에서 ManyToManyField는 내부적으로 중간 테이블을 사용하여 두 테이블 간의 관계를 처리함. 이 과정에서 관련 데이터를 불러오기 위해 여러 개의 쿼리가 발생할 수 있음을 인식함.
    - 비교적 작은 규모의 프로젝트라 하더라도, 관계형 데이터베이스에서는 특정 필드나 관계를 참조할 때마다 매번 데이터베이스에 쿼리를 요청하게 되면 성능 문제가 나타날 수 있다는 점을 고려함. 특히 board.like_users.all()처럼 반복적으로 같은 데이터를 요청하는 경우, 이런 성능 저하가 더 두드러지게 나타날 수 있다고 판단함.
    - 결과적으로, 쿼리 최적화 없이 이런 참조를 처리하면 작은 프로젝트에서도 불필요한 쿼리 비용이 쌓여 성능 이슈로 이어질 수 있다고 판단하여 코드를 수정 및 보완함.

  * 해결한 코드
    ```python
    def likes(request, board_pk):
    board = Board.objects.prefetch_related('like_users').get(pk=board_pk)
    
    # like_users를 set으로 변환
    liked_users = set(board.like_users.values_list('id', flat=True))
    
    if request.user.id in liked_users:
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('boards:detail', board_pk)
    ```

 * 핵심 내용 최종 정리:

    1. ManyToManyField 사용 시 발생할 수 있는 성능 문제 인식:
        - board.like_users.all() 호출 시 매번 데이터베이스 쿼리 발생 
        - 불필요한 쿼리 반복으로 인한 성능 저하 우려

    2. 쿼리 최적화 방법:
        - prefetch_related('like_users') 사용하여 관련 데이터 미리 로드
        -    중복 쿼리 감소 및 성능 향상

    3. 코드 개선:
        - Board.objects.prefetch_related('like_users').get(pk=board_pk) 사용
        - set()을 활용하여 liked_users 효율적으로 처리


    4. 작은 프로젝트에서도 쿼리 최적화의 중요성 인식

  * `Models.py` like_users 코드
  ```python
  class Board(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  ``` 
------


# 오늘 후기
- 오늘 프로젝트를 통해 Django의 ManyToManyField 사용과 관련된 중요한 성능 최적화 기법을 배웠다. 데이터베이스 쿼리 최적화의 중요성을 인식해본 첫날이다.
- prefetch_related를 활용한 쿼리 최적화는 향후 더 큰 규모의 프로젝트에서도 유용하게 적용될 수 있는 중요한 기술일것 같다.
- 앞으로도 계속해서 새로운 기술과 최적화 방법에 대한 세심한 접근과 고민을 바탕으로 더욱 효율적이고 견고한 애플리케이션을 개발해보는 목표 생성 해보게 됨.

### 참고 사이트
* [Django ManyToManyField Documentation](https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ManyToManyField)
* TIL Database M:N 공부내용 참고
