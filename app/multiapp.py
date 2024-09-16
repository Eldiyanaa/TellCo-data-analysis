import streamlit as st
from app.user_engagement_analysis import app as engagement_app
from app.user_experience_analysis import app as experience_app
from app.user_satisfaction_analysis import app as satisfaction_app

class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({"title": title, "function": func})

    def run(self):
        app = st.sidebar.selectbox("Select Analysis", self.app, format_func=lambda app: app['title'])
        app['function']()

# Create the app
multi_app = MultiApp()

# Add all your apps here
multi_app.add_app("User Engagement Analysis", engagement_app)
multi_app.add_app("User Experience Analysis", experience_app)
multi_app.add_app("User Satisfaction Analysis", satisfaction_app)

# Run the app
multi_app.run()