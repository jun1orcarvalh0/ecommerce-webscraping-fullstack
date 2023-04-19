# :technologist::shopping: E-commerce Web Scraping

## :page_with_curl: About
The e-commerce web scraping app is a full stack web application that allows users to scrape e-commerce websites for product data. The app was built using a combination of front-end and back-end technologies.

## :man_technologist: Technologies

* React: a JavaScript library for building user interfaces
* Next.js: a framework for building server-side rendered React applications
* TypeScript: a statically typed superset of JavaScript
* Tailwind CSS: a utility-first CSS framework
* Context API: a built-in state management solution for React
* Axios: a promise-based HTTP client for the browser and Node.js
* Python: a high-level programming language
* FastAPI: a modern, fast (high-performance) web framework for building APIs with Python
* Requests: a Python library for making HTTP requests
* BeautifulSoup4: a Python library for parsing HTML and XML documents
* MongoDB Atlas: a fully managed cloud database service for MongoDB

## :book: Technology Stack
Front-end
The front-end of the app was built using React and Next.js. React is a popular JavaScript library for building user interfaces, and Next.js is a framework for building server-side rendered React applications. The front-end was built with TypeScript to ensure type safety and improve code maintainability. Tailwind CSS was used to style the app, and Context API was used as a built-in state management solution for React. Axios was used to make HTTP requests from the browser.

Back-end
The back-end of the app was built using Python and FastAPI. Python is a high-level programming language that is widely used for web development, scientific computing, and data analysis. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It provides automatic validation of request parameters, serialization of response data, and built-in support for async programming. The app uses FastAPI to handle HTTP requests from the front-end and perform web scraping of e-commerce websites. Requests is used to make HTTP requests to the e-commerce websites, and BeautifulSoup4 is used to parse the HTML documents and extract the relevant product data.

MongoDB Atlas is used as the cloud database for the app. MongoDB Atlas is a fully managed cloud database service for MongoDB, which provides high availability, automatic scaling, and enterprise-grade security. The app uses MongoDB Atlas to store the scraped product data and make it available for analysis and visualization.

## :warning: Warning
Please note that the e-commerce web scraping app is designed for a production environment and utilizes MongoDB Atlas as its database for storing the scraped product data. While this database has been used for demonstration purposes, it is important to create your own database when developing on the project.


## :hammer_and_wrench: How to run the project

### 1 - Clone the repository
```sh
git clone git@github.com:jun1orcarvalh0/ecommerce-webscraping-fullstack.git
```

### 2 - Enter the project folder
```sh
cd ecommerce-webscraping-fullstack
```

### 3 - Enter in app folder
```sh
cd app
```

### 4 - Enter in front-end folder
```sh
cd front-end
```

### 5 - In the front-end folder, install the dependencies and run the application

Installing the dependencies:
```sh
npm install
```

OBS: There is a file called .env.example, you must change it to ".env" and set your API's Url

Running the application:
```sh
npm run dev
```

### 4 - Enter in back-end folder:
```sh
cd ..
```

```sh
cd back-end
```

### 5 - In the back-end folder, install the dependencies and run the application:

Creation of virtual environment
```sh
python3 -m venv .venv
```

Enter in virtual environment:
```sh
source .venv/bin/activate
```

Installing the dependencies:
```sh
pip install -r requirements.txt 
```

OBS: There is a file called .env.example, you must change it to ".env" and set your API's Url

Running the application:
```sh
uvicorn main:app --reload
```
