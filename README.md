# 📊 Job Market Data Analyzer

![Dashboard Preview](<img width="1915" height="991" alt="image" src="https://github.com/user-attachments/assets/3b191c2e-ef20-4a15-b8e9-3e59d698d1d9" />
<img width="1915" height="991" alt="image" src="https://github.com/user-attachments/assets/3b191c2e-ef20-4a15-b8e9-3e59d698d1d9" />
)

## 🚀 Project Overview

The **Job Market Data Analyzer** is an interactive, end-to-end data application designed to extract actionable insights from raw job posting data. It provides a comprehensive look into salaries, required tech stacks, and demand for data professionals across different seniority levels.

This project showcases a complete data pipeline: from messy, unstructured CSV data to a fully clean, optimized dataset, ultimately visualized through an interactive Streamlit dashboard.

**Live Demo:** [Insert Link to your Streamlit App]

## 🛠️ Tech Stack & Skills Demonstrated

* **Languages:** Python
* **Data Processing & ETL:** Pandas, NumPy, AST (Abstract Syntax Trees for parsing complex strings)
* **Data Visualization:** Plotly (Interactive charts), Seaborn, Matplotlib
* **Frontend/Web App:** Streamlit
* **Key Skills:** Exploratory Data Analysis (EDA), Data Cleaning, Outlier Handling, Pipeline Architecture

## 💡 Key Features

1. **Interactive Salary Analysis:** Boxplot distributions highlighting the actual earning potential and ranges across Junior, Mid, Senior, and Lead roles.
2. **Dynamic Skill Extraction:** Programmatic parsing of unstructured skill lists to identify and rank the Top 10 most in-demand technologies (e.g., Python, SQL, AWS).
3. **Data Filtering:** Real-time dashboard updates based on user-selected criteria, allowing for granular exploration of the job market.
4. **Outlier Mitigation:** Built-in logic to handle data entry errors (e.g., multi-million dollar salary anomalies) to ensure accurate statistical representation.

## 📂 Repository Structure

```text
job-market-analyzer/
│
├── data/                      <- (Ignored in Git) Raw and processed datasets
├── notebooks/                 <- Jupyter notebooks for EDA and cleaning logic
│   └── 01_EDA_and_cleaning.ipynb
├── app/                       <- Streamlit application code
│   └── main.py
├── requirements.txt           <- Project dependencies
└── README.md                  <- Project documentation
```

## ⚙️ How to Run Locally

1. **Clone the repository:**

``` bash
git clone [https://github.com/Z1KO-ai/job-market-analyzer.git](https://github.com/Z1KO-ai/job-market-analyzer.git)
cd job-market-analyzer
```

1. **Install dependencies:**

``` bash
pip install -r requirements.txt
```

1. **Add the data:**

Download the raw job market dataset from Kaggle.

Place it in a folder named data/raw/ at the root of the project.

Run the Jupyter Notebook in notebooks/ to clean the data and generate the processed file.

1. **Add the data:**

``` bash
streamlit run app/main.py
```

## 👨‍💻 About the Author

**Zack**
I specialize in Data Analysis with a strong focus on database development, data processing, and extracting actionable insights. I am currently expanding my expertise into Data Engineering to build robust, automated data pipelines and optimized architectures.

* GitHub: [@Z1KO-ai](https://github.com/ZackDev10/)
