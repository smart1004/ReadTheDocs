Docker_TensorFlow
Docker Image for TensorFlow/Keras

docker windows tutorial
 * https://docs.docker.com/docker-for-windows/


한글 docker 
 * https://www.slideshare.net/iFunFactory/docker-linux-linux-66590915

docker-guide
 * https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html


https://dev-ops-notes.com/docker/howto-run-jupiter-keras-tensorflow-pandas-sklearn-and-matplotlib-docker-container/


http://taewan.kim/post/python_env_for_machine_learning/
> docker pull taewanme/pyml:0.1.07
> docker images --all
docker run -itd -p 8888:8888 -p 6006:6006   -v C:\Users\kusun\my_dir:/root/ipython   --name pyml  taewanme/pyml:0.1.07

암호는 Welcome1  이다

docker container ls
docker container stop 30bffb99790f

https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
https://www.youtube.com/watch?v=_Lo-5SZDDEc


https://hub.docker.com/r/heatonresearch/jupyter-python-r/

docker pull heatonresearch/jupyter-python-r

https://github.com/jeffheaton/t81_558_deep_learning


 * docker run -it --rm -p 8888:8888 -v C:\Users\kusun\my_dir:/root/mount/ heatonresearch/jupyter-python-r:latest
 * 아래d는 jupyter가 뜬다
 * http://127.0.0.1:8888/?token=1ff150656a6d03523d344892753403e1a55884741495bd1a


docker run -it --rm -p 8888:8888 -v [local folder]:/root/mount/ heatonresearch/jupyter-python-r:latest

호스트 os 홈폴더 마운트하기
docker run -i -t -v C:\Users\kusun\my_dir:/my_dir  continuumio/miniconda3 /bin/bash
