import streamlit as st
import pandas as pd
import plotly.express as px
import ast

# 1. Page Configuration
st.set_page_config(page_title="Job Market Analyzer", page_icon="📊", layout="wide")

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_job_data.csv")

    # Because saving to CSV turns lists into strings
    def parse_skills(skill_str):
        try:
            return ast.literal_eval(skill_str)
        except:
            return []

    df['skills_list'] = df['skills_list'].apply(parse_skills)
    return df

df = load_data()

# 3. Dashboard Header
st.title("📊 Job Market Data Analyzer")
st.markdown("Explore salaries, demand, and required skills for Data Professionals.")
st.divider()

# 4. Sidebar for User Filters
st.sidebar.header("Filter the Data")

# Get unique seniority levels, drop NaNs, and add an "All" option
seniority_options = ["All"] + list(df['seniority_level'].dropna().unique())
selected_seniority = st.sidebar.selectbox("Select Seniority Level", seniority_options)

# Apply the filter
if selected_seniority != "All":
    filtered_df = df[df['seniority_level'] == selected_seniority]
else:
    filtered_df = df

# 5. Top-Level KPIs (Key Performance Indicators)
col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs Analyzed", len(filtered_df))
col2.metric("Average Salary", f"${filtered_df['avg_salary'].mean():,.0f}")
col3.metric("Highest Salary", f"${filtered_df['max_salary'].max():,.0f}")

st.divider()

# 6. Main Charts Area
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Top 10 In-Demand Skills")
    # Explode and count
    exploded = filtered_df.explode('skills_list')
    top_skills = exploded['skills_list'].value_counts().head(10).reset_index()
    top_skills.columns = ['Skill', 'Count']

    # Plotly Bar Chart
    fig_skills = px.bar(top_skills, x='Count', y='Skill', orientation='h',
                        color='Count', color_continuous_scale='Viridis')
    fig_skills.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_skills, use_container_width=True)

with col_chart2:
    st.subheader("Salary Distribution by Seniority")
    # Plotly Box Plot
    fig_salary = px.box(df, x='avg_salary', y='seniority_level', color='seniority_level')
    st.plotly_chart(fig_salary, use_container_width=True)
