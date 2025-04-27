import requests
import json

url = "https://api.asi1.ai/v1/chat/completions"
name = "Mishka"
resume = """Education
Mishka Jethwani
(475)-257-2351 | mjethwani@ucsd.edu | jethwanimishka0@gmail.com | https://www.linkedin.com/in/mishka-jethwani/
 University of California, San Diego San Diego, CA Bachelor of Science in Computer Science — Provost Honors — Major GPA: 3.8/4.0 Sept. 2022 – March 2026
Certifications: AWS Certification Machine Learning Speciality
Objective: Student at UCSD, with experience in Full Stack Development, through internships and efficient ML and AI through research,
along with expertise in cloud computing, aiming to contribute in creating scalable, impactful solutions.
Other Positions: President @ ISA | Student Assistant @ Qualcomm Institute | Software Developer @ ACM AI | Mentor and Tutor @ UCSD
Experience
Software Engineering Intern August 2024 – September 2024
Reydeo LLC Irvine, CA
• Worked in a cross-functional team, following the Agile development process to develop a admin dashboard with React.js and Next.js for Reydeo Apps Creator, a No-Code SaaS platform for ML/AI app development and achieved 90% test coverage
• Implemented RESTful APIs with Node.js, optimized MongoDB queries, improving dashboard loading times by over 30%.
• Implemented asynchronous programming patterns using TypeScript, including Promises and async/await, to optimize data fetching
and API interactions, reducing load times and Integrated real-time data updates using WebSockets.
Summer Machine Learning and Research Intern June 2024 – August 2024
STABLE Labs, UC San Diego San Diego, CA
• Submitted a paper to SIGCSE’24 with Dr. Jishen Zhao on improving the CodeGen model by prompting and fine tuning, improving code generation of the 350M model from 12.8% to 35.6% on the HumanEval dataset, awarded 2 scholarships (FMP & TRELS).
• Engineered a dual-agent LLM system integrating a fine-tuned CodeGen model with GPT-3.5, implementing bidirectional information exchange protocols to enhance code generation capabilities of the model.
• Implementing advanced Natural Language Processing techniques using LangChain and Retrieval Augmented Generation (RAG) to enhance decision-making capabilities in Autonomous Vehicle systems and improve capabilities of Large Language Models.
• Developing an iterative framework with self-feedback loops and ScratchPad-LLM, for enhancing self-refinement capabilities, implementing a two-stage generation process to improve performance in reasoning, & reduce hallucination by instruction tuning.
Software Development Intern July 2023 – September 2023
Parfait Consultancy Firm
• Developed an end-to-end automated OCR pipeline using OpenCV and Tesseract, leveraging Docker for deployement to analyze data from over 1000+ scanned documents daily and achieving 92% accuracy on average.
• Deployed and scaled the OCR pipeline on AWS, leveraging ECS for container orchestration to process 90+ requests per minute.
• Utilized data analysis techniques with Pandas and NumPy to analyze large-scale datasets and applied k-means clustering for
customer segmentation, contributing to insightful data visualizations using Matplotlib to help quantify bussiness driving decisions.
• Implemented CI/CD pipelines including Linters, automated tests, code coverage, static code analysis, build processes, dependency
management using GitHub Actions and set up automated testing with Jest and Puperteer for unit and end-to-end testing.
Vice President of Operations August 2023 – Present
CSE Society OpenSource San Diego, CA
• Managed 16 developers and 8 software leads overseeing milestones and PRs, to promote the open-source community at UCSD.
• Led the development of CSES TritonScript, a collaborative MERN Stack app enhancing student resources at UCSD, and contributed
to Activist, an open-source platform built with Django, PostgreSQL, Vue.js, and TypeScript.
• Currently leading development of a finance app using MERN Stack, featuring user authentication, budget tracking, financial goal
setting, and a personalized virtual financial advisor; with AWS integration and API connections with banking platforms. Projects
ConnectCore : Full Stack Web App | Next.js, Tailwind CSS, React, TypeScript
• Architected microservices by Node.js, implementing OAuth 2.0 for API integrations with Google Drive, Slack, Discord, & Notion.
• Developed React components for drag-drop functionality on infinite canvas, optimizing render efficiency for workflow visualization.
• Engineered a SaaS platform featuring automated multi-channel notifications, workflow automation, and with light/dark modes.
Stock Trend Prediction Web App | Python, Streamlit, Scikit-learn, Pandas, Numpy, Plotly
• Developed a responsive stock analysis platform with data processing and websocket integration for real-time market data.
• Engineered an ensemble machine learning pipeline combining LSTM, and Prophet models, and deployed on Streamlit.
Ba.Chat: Medical AI | MERN Stack (MongoDB, Express.js, React, Node.js), Git, GPT API (Special mention at LA Hacks ’24)
• Engineered a web application using MERN stack, and authentication using Firebase, integrating it with the GPT-3.5 API using
prompt tuning technique chain-of-thought to create a medical insurnance chatbot.
• Orchestrated automated email negotiation with Gmail, insurance database analysis, and virtual medical second opinions.
Web-Scraper @ Qualcomm Institute | Python, Beautiful-Soup, WordPress (PHP)
• Developed a web scraping tool for data extraction to tranfer over 900+ articles from our legacy system to a WordPress platform,
with Qualcomm’s IT team and Implemented asynchronous programming, resulting in a 96% reduction in data migration. Technical Skills
Languages: Python, Java, C, C++, HTML/CSS, JavaScript, TypeScript, MATLAB
Developer Tools: Git, Bash/Shell Scripts, Nano/Vim, JUnit, Jest, Puppeteer, Babel
Frameworks: Front-End (React, React Native, Vue.js, Tailwind CSS, Next.js); Back-End (Express.js, Node.js, Django, REST API, FAST API, MongoDB, PostgreSQL, MySQL); Dev-Ops (Docker, AWS, CI/CD, Websockets, WordPress/PHP); ML/Data Science (Pandas, NumPy, PyTorch, TensorFlow, Keras, Seaborn, Scikit-learn, NLTK, spaCy, Hugging Face, OpenCV, Prompting Fine tuning)
   """

payload = json.dumps({
  "model": "asi1-mini",
  "messages": [
    {
      "role": "user",
      "content": f"""You are a friendly, wise, and supportive AI mentor of a real person, described to you later.
                    You speak like a real person. 
                    You give thoughtful career advice, mentorship tips, and emotional support.
                    Keep your tone encouraging, personal, and positive.
                    If you don't know something, be honest but still motivating.
                    You have to act like a person called {name} with the following {resume}. Act like this person."""
    }
  ],
  "temperature": 0.7,
  "stream": False,
  "max_tokens": 500
})

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer sk_5e8dbfb687c84cc0b32ca1ef309e329d6e49084d44aa4c61a9a1bc5fbd92064f'  
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)