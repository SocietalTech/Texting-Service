# Texting Service

These instructions assume that you're using Ubuntu or similar, although they can obviously be modified depending on the OS that you're on.

Steps to install on local machine:
- Go to project's directory using command: **cd /path/to/project**
- Create virtual environment using command: **virtualenv venv**
- Activate it using command: **source venv/bin/activate**
- Install Python dependencies using command: **pip install -r requirements.txt**
- Run migrations using command: **python manage.py migrate**
- Create superuser using command: **python manage.py createsuperuser**
  - Note: this superuser will be used for login purposes for the web form.
 
Steps to run on local machine:
- Get Twilio TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN from Twilio account.
- Set environment variables:
  - **TWILIO_ACCOUNT_SID**
  - **TWILIO_AUTH_TOKEN**
  - **SECRET_KEY** (if applicable)
- To run project on local machine, use command: **python manage.py runserver**
- Install Ngrok and run it using command: **./ngrok http 5000**
- Copy the URL generated by ngrok and put this url with amending in Twilio's active number
  - E.G. suppose the URL generated is http://6c697313.ngrok.io, then you need to add extra parameters to this URL and the actual URL would be http://6c697313.ngrok.io/category/sms
- Use this URL to go to web form: http://localhost:8000/admin/login/?next=/admin/category/category
- Use credentials which you created while creating superuser for login purposes.
