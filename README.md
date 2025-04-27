# 🚀 Ment2Meet - AI-Powered Mentorship Platform

[![Made with Love](https://img.shields.io/badge/Made%20With-%E2%99%A5-red?style=flat-square)](https://github.com/your-repo/ment2meet)  
[![Linkd](https://img.shields.io/badge/Powered%20By-Linkd-blue?style=flat-square)](https://linkd.inc)  
[![Gemini](https://img.shields.io/badge/Powered%20By-Gemini-purple?style=flat-square)](https://www.gemini.com)  
[![FetchAI](https://img.shields.io/badge/Powered%20By-FetchAI-green?style=flat-square)](https://fetch.ai)  
[![Flask](https://img.shields.io/badge/Powered%20By-Flask-lightgrey?style=flat-square)](https://flask.palletsprojects.com/)

Ment2Meet is a transformative platform designed to bridge the gap between **education** and **real-world mentorship** by offering AI-powered versions of real mentors. It provides a low-pressure environment for users to practice networking, ask questions, and connect with professionals in a judgment-free space before initiating real-world interactions.

---

## 📚 Index

- [About Ment2Meet](#about-ment2meet)
- [Badges](#badges)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Installation Instructions](#installation-instructions)
- [Setup and Usage](#setup-and-usage)
- [Who It Benefits](#who-it-benefits)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 💡 About Ment2Meet

Ment2Meet is designed to help **students**, **alumni**, **career centers**, **counselors**, and **professors** by providing **AI-powered mentorship**, enabling users to learn from real-world experiences and chart personalized roadmaps to success. Powered by **Fetch AI's ASI 1 Mini**, the platform uses AI mentors to help users practice networking, build confidence, and ultimately connect with real-life professionals.

**Key Features**:
- AI-powered mentors
- Personalized roadmap generation
- Real-time learning with AI chatbots
- Connecting with mentors via email and phone
- Tailored career and educational insights

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy
- **Database**: SQLite
- **AI Integration**: Fetch AI's ASI 1 Mini, GPT-3/4
- **Frontend**: TailwindCSS
- **Email Service**: Flask-Mail
- **API Integration**: Linkd API, Fetch AI, Gemini
- **Visualization**: Gemini for roadmap generation

---

## ⚡ Key Features

- **Interactive AI Chatbots**: Create AI-driven mentor personas to help students practice networking.
- **AI-Powered Career Roadmaps**: Generate personalized educational and career roadmaps from successful professionals’ journeys.
- **Real-World Connections**: Use insights from AI mentors to make meaningful real-world connections with actual mentors.

---

## 🛠️ Installation Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-repo/ment2meet.git
    ```

2. **Install dependencies**:

    Navigate into the project directory and install the required Python packages:

    ```bash
    cd ment2meet
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory and add the following variables:

    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your-secret-key
    SQLALCHEMY_DATABASE_URI=sqlite:///mentors.db
    ASI_API_KEY=your-fetch-ai-api-key
    ```

4. **Run the app**:

    To run the application locally:

    ```bash
    flask run
    ```

---

## 🚀 Setup and Usage

1. **Navigate to the landing page**:

    Once the app is running, open your browser and go to `http://127.0.0.1:5001/` to access the landing page.

2. **Register as a mentor**:

    - Click on "Register Yourself as a Mentor" to fill out a questionnaire with your personal and professional details.
    - This information is saved to the database, creating an AI-powered version of you.

3. **Explore the network**:

    - Visit the "Network" page to browse available mentors.
    - Use the search bar to find mentors based on your interests or field of study.

4. **Chat with an AI Mentor**:

    - Select a mentor and start chatting with the AI version. Ask questions and get career insights.

5. **Connect with a real mentor**:

    - After interacting with the AI, you can connect with the actual mentor via email.

6. **View Personalized Roadmaps**:

    - Generate career and education roadmaps based on real-world professionals.

---

## 👥 Who It Benefits

**Ment2Meet** benefits a wide range of individuals and organizations, including:

- **Students**: Gain insights, practice networking, and receive mentorship before reaching out to real professionals.
- **Professors**: Enhance student learning by providing them with AI mentors that can guide their academic journey.
- **Alumni**: Engage with new generations of students and help them navigate their career paths.
- **Career Centers**: Offer students an AI-driven resource to better prepare for their careers.
- **Counselors**: Help students chart personalized educational and career paths with mentorship-driven insights.

---

## 🔮 Future Plans

- **Video Mentoring**: Integrate **video conferencing** with mentors for more engaging, real-time interactions.
- **AI-powered Phone Calls**: Introduce **AI-driven phone calls** with mentors for a more authentic experience.
- **Scheduling System**: Allow users to **schedule real phone or video calls** with mentors.
- **More AI Models**: Implement additional AI mentors trained in specific fields, e.g., software development, business, or medicine.

---

## 🤝 Contributing

We welcome contributions to Ment2Meet! Here’s how you can get involved:

1. **Fork** the repository.
2. **Clone** your fork and make changes.
3. **Commit** your changes and push them to your fork.
4. **Submit a pull request** with a description of your changes.

We’re open to bug fixes, feature improvements, and new ideas!

---

## 🚀 Thank You!

Thank you for checking out **Ment2Meet**! Together, we can transform the way we network, learn, and grow.
