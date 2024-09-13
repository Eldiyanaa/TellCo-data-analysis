# TellCo Telecom Data Insights
## Project Overview
This project aims to analyze TellCo's telecommunications dataset to gain insights into user behavior, engagement, and satisfaction. The goal is to inform business strategies and identify potential growth opportunities, helping determine if TellCo is a viable investment for stakeholders.

## Business Need
TellCo's investors specialize in acquiring undervalued telecom companies. By understanding user behaviors and network performance, this project seeks to uncover strategies for improving profitability and customer satisfaction, making TellCo a more attractive investment opportunity.

## Data Description
- **Source:** Monthly aggregation of xDR (data records) from TellCo's users.
- **Attributes:** Data includes session details such as duration, data usage, handset models, and application types.
- **Database:** Data is stored in a PostgreSQL schema.
## Project Objectives
**1. User Overview:**

- Analyze the most popular handsets and manufacturers.
- Study user behavior in relation to various applications.
- Handle missing values, outliers, and data inconsistencies.

**2. User Engagement Analysis:**

- Track key metrics such as session duration and data usage.
- Segment users into different groups using k-means clustering to identify customer profiles and engagement levels.

**3. Experience Analytics:**

- Analyze network performance, device characteristics, and session quality.
- Perform clustering on user experience metrics to identify issues affecting customer satisfaction.

**4. Satisfaction Analysis:**

- Assign scores for user engagement and experience.
- Build a regression model to predict customer satisfaction based on engagement and network experience metrics.
## Tools & Technologies
- **Data Processing & Analysis:** Python (pandas, numpy)
- **Machine Learning:** scikit-learn (clustering, regression modeling)
- **Visualization:** matplotlib, seaborn
- **Database Management:** PostgreSQL
- **Dashboard:** Streamlit for interactive data exploration
- **Containerization:** Docker
- **Continuous Integration:** GitHub Actions
## Setup Instructions
### Clone the Repository
```
git clone git@github.com:nebiyu-ethio/tellco-data-insights.git
```
```
cd tellco-data-insights
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Run the Project
- **Data Analysis:** Execute scripts for data preprocessing, clustering, and regression analysis.
- **Interactive Dashboard:** Run the Streamlit app for interactive exploration of TellCo’s telecom data.
```
streamlit run dashboard.py
```
## Project Deliverables
- **Data Analysis:** Insights into customer behavior and network performance.
- **Clustering Models:** Segmented customer profiles based on engagement and experience.
- **Predictive Models:** A regression model predicting customer satisfaction.
- **Interactive Dashboard:** A user-friendly interface for exploring TellCo's data.
## License
This project is licensed under the MIT License.
