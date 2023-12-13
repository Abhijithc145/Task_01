# user_management

Here we can run django project in two ways

Step 1:
        python3 -m venv venv 
       source venv/bin/activate
       Here we are useing  database is sqllite
       Here you can run strightly use below commands

       python3 manage.py makemigration
       python3 manage.py migrate
       python3 manage.py run-server


step2:
        IF you need to change the database go to common/configs/local.cfg add your postgres sql data
       And run 
       
       Make run-local
