# Django-worked-tutorial-with-explanations

  Terminal in Atom: conda create --name mysite python=3.7.3
  conda activate mysite
  source ~/.virtualenvs/djangodev/bin/activate
  pip install django
  django-admin startproject bezushchak_test

  git clone https://github.com/[!YourGitHubName!]/django.git
  pip install -e /Users/[Your Directory]/Desktop/Python_Intro/mysite/django
  cd /Users/[Your Directory]/Desktop/Python_Intro/mysite/django/tests
  pip install -r requirements/py3.txt
  cd /Users/[Your Directory]/Desktop/Python_Intro/mysite/
  python3 manage.py runserver
  ###Follow the http###
  press cntr+C
  ls
  python3 manage.py startapp polls
  
after:
source ~/.virtualenvs/djangodev/bin/activate
cd /Users/[Your Directory]/Desktop/Python_Intro/mysite/
python3 manage.py runserver

!!!!NEW PROJECT!!!!
conda create —-name bezushchak_test python=3.7.3
source activate bezushchak_test
(create folder)
cd bezushchak_test

pip install django
django-admin startproject bezushchak_test
django-admin startapp my_app

DJANGO CHANNELS!!!!
source ~/.virtualenvs/djangodev/bin/activate
cd /Users/Lexis/Desktop/Python_Intro/src
pip3 install django
pip3 install channels_redis
brew services start redis
python3 manage.py runserver
