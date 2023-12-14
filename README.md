# user_management

Here we can run django project in two ways

Step 1:
        ]
       Here we are useing  database is sqllite
       Here you can run strightly use below commands

       python3 -m venv venv 
       source venv/bin/activate
       pip install -r requirements.txt
       python3 manage.py makemigration
       python3 manage.py migrate
       python3 manage.py run-server


       or
       python3 -m venv venv 
       source venv/bin/activate
       make run-local1


step2:
        IF you need to change the database go to common/configs/local.cfg add your (postgres) database path way
        
        Use this commond   "make run-local"

       
