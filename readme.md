# Trading Platform 📈

The **Trading Platform** is an innovative Django-based web application that brings trading view functionality to your fingertips! 💼💹 Dive into the exciting world of trading, analyze market data, and make informed decisions with ease. This readme will guide you through the installation and running of the application. Let's get started! 🚀

## Requirements 📋

To embark on this trading adventure, make sure you have the following requirements in place:

- Python 🐍
- Django 🌐
- Celery 🌟
- RabbitMQ 🐇

Before proceeding, ensure that you have these prerequisites installed on your system.

## Installation ⚙️

To set up the Trading Platform, follow these simple steps:

1. Install RabbitMQ 🐇 based on your operating system. It will play a vital role in the functioning of our application.

2. Install the Python dependencies by gracefully running the following command: 📥
   ```
   pip3 install -r requirements.txt
   ```

## Running the Application 🏃‍♀️

To ignite the Trading Platform's engine, follow these illuminating steps:

### Setting up the Database 💾

Prepare the database for action by running this command: 🛠️

```
python manage.py migrate
```

### Starting the Project 🚀

Launch the project and let it soar by executing this command: 🚀

```
python3 manage.py runserver
```

### Running Celery Processes ⚙️

The Trading Platform powers up with the help of mighty Celery! ⚡ Depending on your operating system, follow the instructions below to unleash the magic of Celery!

**For Linux/MacOS:** 🐧🍎
Execute this enchanting command to synchronize the realms of Celery's worker and beat processes: 🌟

```
celery -A trading_platform worker --loglevel=info --beat
```

**For Windows:** 🪟
Invoke two separate command prompt windows, each dedicated to a heroic Celery process. Kindly enter the following commands:

1️⃣ Start the worker:

```
celery -A trading_platform worker --loglevel=info
```

2️⃣ Start the beat:

```
celery -A trading_platform beat --loglevel=info
```

Rise above the horizon of possibilities! ✨✨ As the Trading Platform and Celery processes thrive, open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to bask in the marvels of the Trading Platform.

Remember to keep the RabbitMQ server live before commencing this glorious journey. It will ensure seamless task processing and job scheduling.

Should you require further assistance or seek enlightenment, dive into the extensive documentation or reach out to our dedicated support team. We're here to elevate your trading experience! 🚀💼

Happy Trading! 📈📉 Feel the thrill of the market and make your mark! 💪💰
