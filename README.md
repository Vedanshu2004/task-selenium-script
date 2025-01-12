Overview:

This project is a web application that retrieves and displays the top 5 trending topics from Twitter, along with the current date, time, and the server's IP address. The application is built using Flask for the web framework, Selenium for web scraping, and MongoDB for storing the trending topics.

Features:

Home Page: Displays a button to fetch the latest trending topics.
Fetch Trending Topics: Retrieves the top 5 trending topics from Twitter.
Display Information: Shows the trending topics, current date and time, and server IP address.
Store in MongoDB: Saves the fetched trending topics along with the timestamp in a MongoDB database.
Dependencies:

To run this project, ensure you have the following dependencies installed:

Flask: A lightweight WSGI web application framework in Python.
Selenium: A tool for automating web browsers.
MongoDB: A NoSQL database for storing trending topics.
pymongo: A Python driver for MongoDB.
chromedriver: A WebDriver for Chrome, required for Selenium to control the browser.
Installation:

Set Up MongoDB:

Install MongoDB on your system or use a cloud-based MongoDB service.
Create a database named trending_topics_db and a collection named trends.
Install Python Dependencies:

bash
Copy code
pip install Flask selenium pymongo
Download ChromeDriver:

Download the appropriate version of ChromeDriver for your system from the official site.
Ensure that chromedriver.exe is in your system's PATH or specify its path in the selenium_script.py file.
Usage:

Run the Flask Application:

bash
Copy code
python app.py
Access the Application:

Open a web browser and navigate to http://127.0.0.1:5000/.
Click the "Click here to run the script" button to fetch and display the trending topics.
File Structure:

Copy code
project/
│
├── app.py
├── selenium_script.py
└── templates/
    └── index.html
File Descriptions:

app.py: The main Flask application that defines routes and handles requests.
selenium_script.py: Contains the function fetch_trending_topics() that uses Selenium to scrape Twitter for trending topics.
templates/index.html: The HTML template for the home page, which includes a button to fetch trending topics and a section to display the results.
Note:

Ensure that your system has the necessary permissions to run Selenium and access the internet. If you encounter issues with ChromeDriver, verify that it is compatible with your version of Google Chrome. Additionally, ensure that the chromedriver.exe path is correctly specified in the selenium_script.py file.

For a detailed walkthrough on collecting tweets into MongoDB using Python, you can refer to this YouTube tutorial.

By following these steps, you should be able to set up and run the Twitter Trending Topics Fetcher application successfully.
