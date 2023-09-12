# Url Shortner project
A simple url shortner app built with django and Python v3.7 and above

### Setup
Update the System
```bash
sudo apt-get update
```
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/et3858/url_shortner_project.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Download django usig pip
```bash
sudo apt install python3-pip -y
```
```bash
pip install django
```
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python3 manage.py migrate
```

One last step and then our App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple App. Start the server by following command

```bash
python3 manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000 for the App.

If you are working with a remote server (like an AWS EC2 instance or others), change the localhost IP for the public IP of your server.

Happy Coding
