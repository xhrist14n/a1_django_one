python manage.py collectstatic
rm ./djangoone/*.pyc
rm ./home/*.pyc
clear
git add . -f
git commit -am "project django"
git push origin master