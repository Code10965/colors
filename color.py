# get the user input from index site and turn it into a variable
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
print("Content-Type: text/html")
print()   
print("<TITLE>CGI script output</TITLE>")
color_selected = str(form["color"].value)

# convert variable into a standard format
color_selected_strip = color_selected.lower().strip().replace(" ","")

# creating a list from the color file
filename = "colors.txt"

with open(filename) as file_object:
   lines = file_object.readlines()
color_set = ''
for line in lines:
   line = line.lower().strip().replace(" ", "")
   color_set += line
   
# check if selected color is in this list
if color_selected_strip in color_set:

# combine html code with exchangable variable input (python-code) in one statement
   print("""
      <!DOCTYPE html>
      <center>
      <h2>Yiiihaaa!!!</h2>
      <h1 style="color:
      """)   
   print(color_selected) 
   print("""";>""")  
   print(f"{color_selected.title()} ")
   print("""
      </h1>
      <h2>is a very beautiful color.</h2>
      </center>
      </html>
      """)  

# close if-else condition
else:
   print("""
      <!DOCTYPE html>
      <center>
      <h2>This is not a color. Try again, please.
      <br>
      </h2>
      </center>
      </html>
      """)  

# build a return button to move back to index 
   print("""
      <div style = "text-align: center";>
      <form action="http://localhost:8000/">
      <button type="back">back</button>
      </form>
      </div>
      """)


