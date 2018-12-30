0_docker_command.rst

vim 설치
 * http://blog.hemapresso.com/?p=715

docker run -it ubuntu /bin/bash

apt-get update
apt-get install vim

docker ps -a

docker commit c06b9adb389d ubuntu_my  <--- 이미지 저장 명령

docker run -it ubuntu_my /bin/bash

get-started
 * https://docs.docker.com/get-started/part2/#requirementstxt


 
-----------------
conda create -n tf pip python=3.5
pip install --upgrade pip

activate tf

conda  activate tf in docker
chmod -R 755 ./tf/*

(tf) root@b514cb0e9e9a:/opt/conda# ls                   
tf
(tf) root@b514cb0e9e9a:/opt/conda# chmod -R 755 ./bin/* 

cd /opt/conda/envs
activate tf

conda install -c conda-forge keras

(tf) root@b514cb0e9e9a:/opt/conda/envs# activate tf   
(tf) root@b514cb0e9e9a:/opt/conda/envs#               

================================================
docker run hello-world
powershell
docker pull continuumio/miniconda3

docker run -i -t continuumio/miniconda3 /bin/bash
python3 -c "print(3*5)"

exit

docker ps -a

bbf4eec6c91d

docker commit bbf4eec6c91d mlearn:init  <--- 이미지 저장 명령
docker images

docker run -i -t mlearn:init /bin/bash

docker attach 977abd71790d     <-- 다시 콘솔로 들어 간다

docker start 1807abd8a0cc   <-- exit 로 중지한 컨테이너 start
docker attach 977abd71790d <-- 콘솔로 들어 간다

호스트 os 홈폴더 마운트하기
docker run -i -t -v C:\Users\kusun\my_dir:/my_dir  continuumio/miniconda3 /bin/bash

* $HOME:$HOME 은 윈도우의 경우 	c:\Users\사용자이름
* kusun 밑에 쓸데 없는 폴더가 많다.
docker run -i -t -v $HOME:$HOME  continuumio/miniconda3 /bin/bash  <--안됨
C:\Users\kusun\my_dirvim

(base) root@b514cb0e9e9a:/# cd /my_dir
(base) root@b514cb0e9e9a:/my_dir# ls
1111.txt

docker start b514cb0e9e9a
docker attach b514cb0e9e9a
docker commit b514cb0e9e9a mlearn:init 
docker stop 

https://brunch.co.kr/@hopeless/10

docker ps      동작중인 컨테이너
docker ps -a    정지된 컨테이너

컨테이너 삭제
docker rm 컨테이너id
docker images
docker rmi <image id>   image 삭제
--------------------

# jep
C:\ProgramData\Anaconda3\envs\TF\python.exe setup.py build
C:\ProgramData\Anaconda3\envs\TF\python.exe setup.py install
