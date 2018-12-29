
============
0_flask sklearn model
============

--------
machine-learning-models-api-python
--------
 #. https://www.datacamp.com/community/tutorials/machine-learning-models-api-python   
 
--------
flask
-------- 
 #. http://flask.pocoo.org/docs/1.0/deploying/#deployment   
 
 #. https://winterj.me/flask-release/

#. http://flask.pocoo.org/docs/1.0/deploying/uwsgi/#starting-your-app-with-uwsgi
 
이제 기본적으로 development 환경에서 서버가 멀티스레드로 동작한다. 그에 맞춰 문서에서 by default serves only one request at a time 이라는 문구가 삭제되었다. 로컬 머신에서 테스트해 본 결과 동시에 128개의 요청도 처리 가능했지만 어디까지나 개발 환경에서 편의성이 좋아진 것으로 프로덕션 환경에서 app.run()은 추천하지 않는다. [#2529]



https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa   

https://loads.pickle.me.uk/2016/04/04/deploying-a-scikit-learn-classifier-to-production/

https://www.analyticsvidhya.com/blog/2017/09/machine-learning-models-as-apis-using-flask/

http://queirozf.com/entries/example-project-template-serve-a-scikit-learn-model-via-a-flask-api

https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa

https://www.wintellect.com/creating-machine-learning-web-api-flask/

https://github.com/amirziai/sklearnflask/


https://www.toptal.com/python/python-machine-learning-flask-example

