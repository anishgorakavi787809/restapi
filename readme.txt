How to use this program:

1. Download Python(python.org)
2. Download postgresql(https://www.postgresql.org/download/windows/)
3. open command line
4. type following above:
pip3 install psycopg2
pip3 install Flask
pip3 install Flask-RESTful
pip3 install google
pip3 install beautifulsoup4

5. go to line 13 in app.py in rest side
6. change #YOUR USERNAME to your postgres username
7.  change #YOUR PASSWORD to your own password
8. change #YOUR DATABASE to your own database
9. go to client-side app.py
10. Do the same thing like above
11. go back to rest-side and change "smtp.gmail.com",587 in 20  to "#Your email smtp",#port
12. open terminal or command line and type cd <Your path>/rest-side
13. type, 

If windows:
    python app.py
elif mac or linux:
    python3 app.py
14.
then type cd..

15.

If you wanna test rest:
use postman