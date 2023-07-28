# build_files.sh
# pip install pipenv

# pipenv install
pip install --upgrade pip
pip install -r requirements.txt
echo "=================================================="
echo `python3 --version`
echo "=================================================="
# make migrations
# python3.11 manage.py migrate 
# python3.11 manage.py collectstatic