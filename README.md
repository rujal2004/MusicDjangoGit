#  Django Music App
A web-based music platform built using Django. Users can browse, search, and play music tracks from an online collection. Built to demonstrate Django’s full-stack capabilities with models, views, templates, and media handling.
##  Features

  Browse and play music tracks
  
  Search songs by title or artist
  
  Upload new songs (admin only)

  Donload songs
  
  Django admin panel for content management
  
  Responsive frontend with templates

## Tech Stack

 **Framework**: Django (Python)
 
 **Frontend**: HTML, CSS, Bootstrap (Django templates)
 
 **Database**: SQLite (accessed and managed via Django Admin Panel)
 
 **Media Handling**: Django Static & Media Files
 
 **Admin Interface**: Django’s built-in Admin Panel for uploading and managing music
 
  **Deployment**: Render 

# Installation
   ### 1. Clone the repository
           git clone https://github.com/rujal2004/django-music-app.git
           cd django-music-app
  ## 2.  Create virtual environment
        python -m venv venv
        venv\Scripts\activate
  ## 3.   Install dependencies
         pip install -r requirements.txt
  ## 4. Apply migrations
        python manage.py makemigrations
        python manage.py migrate
  ## 5.  Run the server
         python manage.py runserver


# Future Improvements
Add user registration and playlists

Add comments/likes per track

Integrate with Spotify/Youtube Music APIs

Improve music player UI with JS animations

# Author
 Rujal Gupta


         
