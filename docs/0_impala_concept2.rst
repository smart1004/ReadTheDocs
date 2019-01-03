
0_impala_in_python.rst
impala in python

http://ryufree.tistory.com/220

임팔라는 하둡상에서 맵-리듀스(Map-Reduce)를 이용하지 않고 SQL(Standard Query Language)을 처리하는 기능을 내장한 제품입니다
임팔라는 하둡 위에 동작하는 질의 엔진

아파치 임팔라(Impala)
임팔라는 H베이스(HBase)나 맵-리듀스 같은 별도 계층을 거치지 않고 HDFS(Hadoop Distributed File System)와 직접 통신을 합니다. 
그리고 하이브처럼 ‘하이브쿼리언어(HiveQL)’를 사용합니다.
클라우데라는 임팔라와 하이브의 최대 차이를 성능으로 꼽습니다. 
하이브는 자바로 만들어졌지만 임팔라는 C++ 기반으로 만들어졌으며, 별도의 실행엔진을 사용하므로 맵-리듀스 프로그래밍을 할 필요가 없습니다.
임팔라는 맵-리듀스와는 달리 쿼리(Query)를 아주 낮은 지연속도로 처리할 수 있다고 합니다. 
맵-리듀스에 있는 ‘셔플링(Shuffling)’ 단계를 거치지 않아 테이블간의 조인(Join) 작업도 반드시 맵-리듀스 처럼 다대다 커뮤니케이션을 요구하지 않습니다.

https://kr.cloudera.com/products/open-source/apache-hadoop/impala.html
http://ryufree.tistory.com/220


Hadoop에 설치되는 유일하고 진정한 대화형 분석 솔루션으로써, 다른 솔루션과 비교하여 더욱 우수한 성능을 발휘합니다. 
대규모 병렬 처리(MPP) 엔진으로 설계된 Impala는 동시성이 높은 워크로드를 지원하여 기업 전체의 비즈니스 분석 전문가에게 
광범위한 액세스를 통해 가장 빠른 시간에 통찰 정보를 제공합니다.


클라우데라 임팔라는 H베이스(HBase)나 맵리듀스같은 별도 계층을 거치지 않고 HDFS와 직접통신한다
