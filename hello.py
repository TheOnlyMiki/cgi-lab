#!/usr/bin/env python3

import os
import cgi
import cgitb

cgitb.enable()

print( os.environ )

print( "Content-Type: text/html" )

if "QUERY_STRING" in os.environ: print( f"<p>QUERY_STRING={ os.environ[ 'QUERY_STRING' ] }</p>" )
if "HTTP_USER_AGENT" in os.environ: print( f"<p>BROWSER={ os.environ[ 'HTTP_USER_AGENT' ] }</p>" )

print( """<html>
            <body>""" )
print( "<ul>" )

print( f"key = value" )
for parameter in os.environ[ 'QUERY_STRING' ].split( '&' ):
    name, value = parameter.split( '=' )
    print( f"<li><em>{ name }</em> = { value }</li>" )
    
print("</ul>")

print("""</body>
    </html>""")
