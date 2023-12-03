# Multi-Modal-Search-Engine
# Multimodal Search
Multimodal Search Engine

This is a prototype to create an intelligent search engine, ”Yaaay”, formultiple modalities that scores the probability which leads to a relevant page. It proposes a multi-modalsearch engine based on the Okapi BM25 model for the retrieval and ranking for the cricket dataset. This system is designed, developed and is available through a web application

In the project directory:

1. `Front End - React Based Code`

```
Under yaaay-ui

Installation

$ npm install

Running the application - Runs the app in the development mode.
Open http://localhost:3000 to view it in the browser.

$ npm start

Testing the application - Launches the test runner in the interactive watch mode

$ npm test

```


2. `For running Backend - BM25 enabled custom Flask API`

```
Under yaaay-backend

Installation - 

$ pip install rank_bm25

Running the application - Runs the application on the development server
Open http://172.16.7.138:5000/ to view the API response in the browser. 

$ python mock.py

```

3. `Integration with Backend`

Under yaaay-ui, 

3. 1. `For connecting to BM25 enabled custom Flask API` 

```

The API call is made from UI fetching data from file: useCustomSearch.js
`http://172.16.7.138:5000/result?q=${term}`

```

3. 2. `For connecting to Google APIs`

```

In key.js, we have configured the API_KEY = "AIzaSyCK9VkNmSiSUu-s9VUaH9VIBnIbqISjlqQ";
The API call is made from UI fetching data from file: useGoogleSearch.js
`https://www.googleapis.com/customsearch/v1?key=${API_KEY}&cx=${CONTEXT_KEY}&q=${term}`

```


