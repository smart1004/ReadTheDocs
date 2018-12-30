
Docker_TensorFlow
Docker Image for TensorFlow/Keras

https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html

https://www.youtube.com/watch?v=_Lo-5SZDDEc


https://hub.docker.com/r/heatonresearch/jupyter-python-r/

docker pull heatonresearch/jupyter-python-r

https://github.com/jeffheaton/t81_558_deep_learning


 * docker run -it --rm -p 8888:8888 -v C:\Users\kusun\my_dir:/root/mount/ heatonresearch/jupyter-python-r:latest
 * 아래는 jupyter가 뜬다
 * http://127.0.0.1:8888/?token=1ff150656a6d03523d344892753403e1a55884741495bd1a

http://(1d47440b6cc1 or 127.0.0.1):8888/?token=1ff150656a6d03523d344892753403e1a55884741495bd1a


docker run -it --rm -p 8888:8888 -v [local folder]:/root/mount/ heatonresearch/jupyter-python-r:latest



호스트 os 홈폴더 마운트하기
docker run -i -t -v C:\Users\kusun\my_dir:/my_dir  continuumio/miniconda3 /bin/bash

