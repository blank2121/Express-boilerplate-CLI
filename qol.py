import typer
import os

app = typer.Typer()

@app.command(name="express-app")
def express_setup(typescript: bool):
    '''makes express app with get and post routes'''
    script = '''const express = require("express"); 
const app = express();

app.set('view engine', /*enter a view engine, ejs is already installed*/);

app.get("/", (req, res) => {
    //put code in here

    //send file
    res.sendFile(/*file dir here*/);
});

app.post("/", (req, res) => {
    res.json({/*json data here*/})
});

app.listen(/*port*/);'''


    os.system("npm init -y")
    os.system("npm i express.js")
    os.system("npm install ejs")
    os.system("mkdir src")
    
    if typescript:
        with open("./src/index.ts", "w+") as f:
            f.write(script)
    else:
        with open("./src/index.js", "w+") as f:
            f.write(script)

@app.command(name="express-web-host")
def express_html(typescript: bool):
    '''makes express app to host website'''

    os.system("npm init -y")
    os.system("npm i express.js")
    os.system("npm i path.js")
    os.system("npm i ejs")
    os.system("mkdir src")
    os.system("mkdir static")
    os.system("mkdir views")
    os.mkdir("./views/styles/")
    
    with open("./views/styles/style.css", "w+") as f:
        f.write("""* {
    padding: 0;
    margin: 0;
}

h1 {
    color: blue;
}""")

    with open("./views/home.html", "w+") as f:
        content = '''<!--
this is an example file of where your html file(s) will be.
this also shows how you should link your css files.
also make sure to use the static file for images and other things
that will be static i.e. photos
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link rel="stylesheet" href="./styles/style.css">
    
</head>
<body>
    <h1>Example Thing</h1>
</body>
</html>'''
        f.write(content)

    if typescript:
        with open("./src/index.ts", "w+") as f:
            content='''const express = require('express');
const path = require('path');

const app = express();

//note do not type a slash at the end of the path
const dir = "/*enter directory to project file here*/";


app.use(express.static(path.join(dir + "/views")))

//setting a view engine is optional if you just use sendFile but it doesn't hurt to have it
app.set('view engine', /*set a default view engine. "ejs" is preinstalled*/);


app.get("/", (req, res) => {
    //anytime you do sendFile, make sure you start with (dir + "/views/"+ <your html file in /views/>)
    res.sendFile(dir + "/views/" + "home.html");
});

app.listen(/*port*/);'''
            f.write(content)
    else:
        with open("./src/index.js", "w+") as f:
            content = '''const express = require('express');
const path = require('path');

const app = express();

//note do not type a slash at the end of the path
const dir = "/*enter directory to project file here*/";


app.use(express.static(path.join(dir + "/views")))

//setting a view engine is optional if you just use sendFile but it doesn't hurt to have it
app.set('view engine', /*set a default view engine. "ejs" is preinstalled*/);


app.get("/", (req, res) => {
    //anytime you do sendFile, make sure you start with (dir + "/views/"+ <your html file in /views/>)
    res.sendFile(dir + "/views/" + "home.html");
});

app.listen(/*port*/);'''
            f.write(content)

if __name__ == '__main__':
    print("\n")
    app()
