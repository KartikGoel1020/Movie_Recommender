# 🎬 Movie Recommender System

A simple and interactive **Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.
The application recommends movies similar to the one selected by the user and displays their posters using the **TMDB API**.

This project demonstrates how **content-based filtering** and **cosine similarity** can be used to build a recommendation engine similar to those used by platforms like **Netflix and Amazon**.

---

# 🚀 Live Application

You can try the live application here:

👉 **Live Demo**
https://kartikgoel1020-movie-recommenderappapp-nzy3ehbe3nhxsk3ryfpfvm.streamlit.app/

---

# 📌 Project Overview

Recommendation systems help users discover content they might enjoy by analyzing similarities between items.

In this project, a **content-based recommendation approach** is used. Instead of relying on user ratings, the system analyzes the **similarity between movie attributes** such as genres, keywords, cast, and overview to recommend similar movies.

When a user selects a movie, the system identifies movies that share similar characteristics and recommends the **top 5 most relevant movies**.

---

# ✨ Features

* Recommend **Top 5 similar movies**
* Displays **movie posters using TMDB API**
* Interactive **Streamlit web interface**
* Fast recommendation using **Cosine Similarity**
* Lightweight and easy-to-use application
* Deployed online using **Streamlit Cloud**

---

# 🧠 How the Recommendation System Works

The recommendation engine follows these steps:

### 1. Data Processing

Movie metadata such as **genres, keywords, cast, and overview** are combined to create a single column called **tags**.

---

### 2. Text Vectorization

The textual data is converted into numerical format using **CountVectorizer** from Scikit-Learn.

This converts words into a vector representation that machine learning algorithms can process.

---

### 3. Similarity Calculation

The system calculates similarity between movies using **Cosine Similarity**.

Movies with similar tags have **higher similarity scores**, meaning they share similar characteristics.

---

### 4. Recommendation Generation

When a user selects a movie:

1. The movie index is identified.
2. Similarity scores with all other movies are calculated.
3. Movies are sorted based on similarity.
4. The **Top 5 most similar movies** are recommended.

---

# 🛠 Technologies Used

**Programming Language**

* Python

**Libraries**

* Pandas
* NumPy
* Scikit-learn
* Requests
* Pickle

**Framework**

* Streamlit

**External API**

* TMDB API (for fetching movie posters)

**Deployment**

* Streamlit Cloud
* GitHub

---

# 📂 Project Structure

```
Movie_Recommender
│
├── app.py
├── movie_dict.pkl
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project Locally

If you want to run this project on your system:

### Clone the repository

```
git clone https://github.com/KartikGoel1020/Movie_Recommender.git
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run the Streamlit app

```
streamlit run app.py
```

The application will open in your browser.

---

# 🔑 API Configuration

This project uses the **TMDB API** to fetch movie posters.

The API key is stored securely using **Streamlit Secrets**.

Example configuration:

```
tmdb_api_key = "YOUR_API_KEY"
```

---

# 📊 Learning Outcomes

Through this project, the following concepts were explored:

* Content-based recommendation systems
* Text vectorization using CountVectorizer
* Cosine similarity for recommendation engines
* Building interactive data apps using Streamlit
* Deploying machine learning applications to the cloud

---

# 🚀 Future Improvements

Potential improvements include:

* Adding **search functionality**
* Improving recommendations using **TF-IDF**
* Adding **movie ratings and popularity filters**
* Creating a **hybrid recommendation system**
* Improving UI design

---

# 👨‍💻 Author

**Kartik Goel**

MBA – Business Analytics
Parul University (in association with KPMG)

---

⭐ If you found this project interesting, consider starring the repository.
