
============
0_scalable keras deep learning rest api
============

get_Model, load model in memory, 동영상 
 * https://www.youtube.com/watch?v=XgzxH6G-ufA

최신판   
https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/   

https://www.pyimagesearch.com/2018/01/29/scalable-keras-deep-learning-rest-api/   


**** 아주 좋은 자료이다.
https://www.pyimagesearch.com/2018/01/29/scalable-keras-deep-learning-rest-api/

https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html
Caveat: We are assuming you are using the default Flask server that is single threaded. If you deploy to a multi-threaded server you could be in a situation where you are still loading multiple models in memory even when using the "more correct" method discussed earlier in this post. If you intend on using a dedicated server such as Apache or nginx you should consider making your pipeline more scalable, as discussed here.


keras rest api model preload

use python keras model in java

https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html

use python keras model in java

https://towardsdatascience.com/deploying-keras-deep-learning-models-with-java-62d80464f34a

https://towardsdatascience.com/deploying-keras-deep-learning-models-with-java-62d80464f34a


https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2


★
how-to-keep-a-keras-model-loaded-into-memory-and-use-it

https://stackoverflow.com/questions/52937256/how-to-keep-a-keras-model-loaded-into-memory-and-use-it-when-needed

https://github.com/Ares513/DetectingTrollsApi/blob/master/api.py
