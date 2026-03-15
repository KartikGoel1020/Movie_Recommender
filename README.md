**🎬 Movie Recommender System**

A simple and interactive **Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.
# 🎬 Movie Recommender System

A simple and interactive **Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.
The application suggests movies similar to the one selected by the user and displays their posters using the **TMDB API**.

This project demonstrates how **content-based filtering** and **cosine similarity** can be used to build a recommendation engine for movies.

---

# 🚀 Live Application

You can try the live web application here:

**Live Demo:**
[https://kartikgoel1020-movie-recommender.streamlit.app](https://kartikgoel1020-movie-recommenderappapp-nzy3ehbe3nhxsk3ryfpfvm.streamlit.app/)

---

# 📌 Project Overview

Recommendation systems are widely used by platforms such as **Netflix, Amazon, and Spotify** to help users discover content they might enjoy.

In this project, a **content-based recommendation approach** is used.
Instead of relying on user ratings, the system analyzes the **similarity between movie attributes** such as genres, keywords, cast, and overview to recommend similar movies.

When a user selects a movie, the system identifies movies that share similar characteristics and suggests the **top 5 most relevant movies**.

---

# ✨ Features

* Interactive **web interface** built with Streamlit
* Recommends **top 5 similar movies**
* Displays **movie posters using TMDB API**
* Uses **machine learning similarity algorithms**
* Fast and lightweight application
* Deployed online using **Streamlit Cloud**

---

# 🧠 How the Recommendation System Works

The recommendation engine follows these steps:

### 1. Data Preparation

The movie dataset is processed to combine important attributes such as:

* Genres
* Keywords
* Cast
* Crew
* Movie overview

These attributes are merged into a single **tags column**.

---

### 2. Text Vectorization

Machine learning models cannot understand raw text.
Therefore, the movie tags are converted into **numerical vectors** using:

**CountVectorizer**

This converts words into a structured numerical representation.

---

### 3. Similarity Calculation

After converting the text into vectors, we calculate similarity using:

**Cosine Similarity**

Cosine similarity measures the **angle between two vectors** to determine how similar they are.

Movies with similar tags will have a **higher similarity score**.

---

### 4. Generating Recommendations

When a user selects a movie:

1. The system finds that movie in the dataset.
2. It checks the similarity scores with all other movies.
3. Movies are sorted by similarity.
4. The **top 5 most similar movies** are returned.

---

# 🛠 Technologies Used

This project was built using the following tools and technologies:

**Programming Language**

* Python

**Libraries**

* Pandas
* Scikit-learn
* NumPy
* Requests
* Pickle

**Framework**

* Streamlit

**External API**

* TMDB (The Movie Database API) for movie posters

**Deployment**

* Streamlit Cloud
* GitHub

---

# 📂 Project Structure

```text
Movie_Recommender
│
├── app.py                # Main Streamlit application
├── movie_dict.pkl        # Processed movie dataset
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

# 🔑 API Configuration

This project uses the **TMDB API** to fetch movie posters.

The API key is stored securely using **Streamlit Secrets** to prevent exposing it in the code.

Example configuration:

```toml
tmdb_api_key = "YOUR_API_KEY"
```

---

# 📊 Learning Outcomes

Through this project, the following concepts were explored:

* Content-based recommendation systems
* Natural language processing for movie metadata
* Text vectorization using CountVectorizer
* Cosine similarity for recommendation engines
* Building data applications using Streamlit
* Deploying machine learning applications on the cloud

---

# 🚀 Future Improvements

Some possible improvements for the project include:

* Adding **search functionality**
* Improving recommendation accuracy using **TF-IDF**
* Adding **movie ratings and popularity filters**
* Implementing **hybrid recommendation systems**
* Adding **user authentication**
* Enhancing UI/UX design

---

# 👨‍💻 Author

**Kartik Goel**

MBA – Business Analytics
Parul University (in association with KPMG)

---

# ⭐ Acknowledgment

This project was created as part of learning **machine learning applications and deployment using Streamlit**.

It demonstrates how recommendation systems work and how they can be deployed as interactive web applications.

---

If you found this project helpful or interesting, feel free to ⭐ the repository.
