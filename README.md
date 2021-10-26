# Getting Started

##  Heroku URL

https://cryptic-ridge-00861.herokuapp.com/

## About this Project

This project is a spotify player that takes in a song and artist information from SPOTIFY's API and returns a random song each time the page is accessed. The same page allows the user to access song information including lyrics from the Genius API.


## Installation

To run this program you need to have:

* pip install -r requirement.txt


Files and folders needed:

* app.py
* Folder: templates
  
   * File in folder:
  
        * index.html
        * login.html
        * signup.html
        * dashboard.html
  
* Folder: static
  
    * File in folder:
        * style.css
        * signin.css
        * starter-template.css
        * dashboard.css

Extra files needed:

* requirements.txt
* Procfile
* .env (to store your APIs)
* .gitignore (to hide .env with APIs)
  
## How it works

1. Install all the necessary plugins and create all your files, import everything needed in app.py.
2. Generate your own API keys for Spotify and Genius. Reference these documents: 
   * https://docs.genius.com/#/getting-started-h1 
  
   * https://developer.spotify.com/documentation/web-api/quick-start/

3. Plugin your API keys to the .env file. Example:
   
   * export SPOTIPY_CLIENT_ID=<"Your API key">
   * export SPOTIPY_CLIENT_SECRET=<"Your API key">
   * export GENIUS_ACCESS_TOKEN=<"Your API KEY">

4. Enter the different artists Spotify URIs you want to get a random top    song from in app.py file in the url section. Example: 

    * artist_uri = <'spotify:artist:36QJpDe2go2KgaRleHCDTp'>

    Reference these link for more infomation on spotipy and lyricsgenius:
   
   *  https://spotipy.readthedocs.io/en/2.19.0/
  
   *  https://lyricsgenius.readthedocs.io/en/master/index.html

5. Before you run the code enter source .env in bash terminal.

6. Run the code, you should get a link to a local web address in the terminal. Follow that link in your web brower and a page should appear with a artist name, song title, song cover art, and a link to a genius page with the songs lyrics.

7. You can edit the layout of the page with index.html and style.css files.
8.  You can deploy the the code to heroku if you want to make the  webpage public. Reference this document:

    * https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
  
## Technical issues / Problems
Technical issues: 

* Lyrics not loading on webpage
    * I solved this issue by fixing my html code by adding a hyperlink and using w3schools as a resource https://www.w3schools.com/html/html_links.asp
* App deployed in heroku but error on my heroku webpage
    * I solved this by adding a Procfile to the file and putting (web: python app.py) in the file
* Connect and create new user with Flask-SQLAlchemy 
    * I solved this by added some code like add row to db db.session.add(new_user). Or save data to db db.session.commit()
* Management State of user with Flask-Login
    * I solved this by adding a @login_required, If the user tries to access it without being logged in, it will be logged out.
* Logout session
    * I solved by using Flask-Login
Problems:

*  Lyrics for the song sometimes are not avaiable on genius
   *  I could of fixed this by including a print out the the lyrics for songs that don't have lyrics on genius
* I could of had a bigger selection of artist
  * I could have fixed this by just adding more artist uris to the program




   

    
