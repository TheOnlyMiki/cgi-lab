#!/usr/bin/env python3

import os

import cgi
import cgitb
from http.cookies import SimpleCookie
import secret
from templates import *

cgitb.enable()

fs = cgi.FieldStorage()
username = fs.getfirst( "username" )
password = fs.getfirst( "password" )

check = ( username == secret.username and password == secret.password )

sc = SimpleCookie( os.environ[ 'HTTP_COOKIE' ] )
sc_username = ''
sc_password = ''

if sc.get( 'username' ): sc_username = sc.get( 'username' ).value
if sc.get( 'password' ): sc_password = sc.get( 'password' ).value

cookie = ( sc_username == secret.username and sc_password == secret.password )

if cookie == True:
    username = sc_username
    password = sc_password

print( "Content-Type: text/html" )

if check == True:
    print( f"Set-Cookie: username={ username }" )
    print( f"Set-Cookie: password={ password }" )

if not username and not password:
    print( login_page() )
elif username == secret.username and password == secret.password:
    print( secret_page( username, password ) )
else:
    print( after_login_incorrect() )
