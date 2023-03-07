
Python工程


## 安装依赖

python install pip

pip install -r requirements.txt

pip list

## 持久化

持久化对象创建表

python manage.py migrate

创建默认用户表超级用户

python manage.py createsuperuser

## 启动django服务

cd mysite

python manage.py runserver 8081

## 测试脚本运行

执行poll应用下测试脚本

manage.py test polls

## 封装模块库

### 打包

切换到项目根目录

python setup.py sdist

dist目录内生成 *-*.tar.gz文件

### 安装

切换到*-*.tar.gz所在目录

python -m pip install --user polls-0.1.tar.gz

解压tar.gz tar -cvxf polls-0.1.tar.gz

进入polls-0.1目录，执行脚本

python setup.py install

### 卸载

python -m pip uninstall polls
