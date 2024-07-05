import streamlit as st
import google.generativeai as genai
import datetime
date = datetime.datetime.now()

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(
    page_title="Shreesha's Portfolio",
    page_icon=":tada:",
    layout="centered",
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        background-color: #E67629;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .subheader {
        background-color: #87CEEB;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .section {
        background-color: #E0FFFF;
        color: #4682B4;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4682B4;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        display: inline-block;
        margin-top: 10px;
    }
    .button a {
        color: white;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section with an image
st.markdown('<div class="header"><h1>👋 WELCOME 🙏 </h1><h2>I am Shreesha Beejanthadka</h2></div>', unsafe_allow_html=True)

col1 , col2 = st.columns(2)

with col1:
    st.subheader(" ") # for space
    st.subheader("&nbsp;&nbsp;&nbsp;&nbsp; About Me")
    st.markdown("""
    - **Passionate AI & ML Student**
    - **Proficient in Python & Web Development**
    - **Committed to Innovation**
    - **Proven Academic Achiever**
    - **Strong Problem-Solver**
    - **Published Researcher**
    """)
    with open("images/Shreesha_B_Resume.pdf", "rb") as file:
        st.download_button(
            label="Click here to download my PDF resume",
            data=file,
            file_name="Shreesha_B_Resume_2024.pdf",
            mime="application/pdf"
        )

col2.image(r"images/shreesha_photo.png")

# with col2:
#     st.image(r"images/shreesha_photo.png")

st.write(" ") # for space

# st.markdown("# :robot_face: Shreesha's AI :robot_face:")
st.markdown("""
    <div style="background-color:pink;padding:10px;border-radius:5px;">
    <h1 style="text-align:center;">🤖 Shreesha's AI 🤖</h1>
    </div>
    """, unsafe_allow_html=True)

persona = f"""
You are Shreesha's AI bot. You help people answer questions about your self (i.e Shreesha B)
Answer as if you are responding. Don't answer in second or third person.
If you don't know they answer you simply say "That's a secret".
Just for your reference todays date is {date}. (to calculate age, and other if required)
Here is more info about Shreesha B (i.e Shreesha Beejanthadka):

Name : Shreesha Beejanthadka (in short Shreesha B) 
Data of Birth : 5th July 2002 
Gender : Male 
Nationality: Indian
Location: Current residence : #3-42 , Pilinja House ,Vittal Mudnoor Post & Village , Bantwal taluk ,Dakshina Kannada 574243
Education: 
Bachelor of Engineering (B.E.) - Artificial Intelligence and Machine Learning Branch. (Jun 2020 - May 2024) - CGPA - 9.04 - At Vivekananda College of Engineering and Technology, Puttur
Pre-University College (PUC) - PCMB (May 2018 - Mar 2020) - Percentage - 78% - At Vidya Soudha PU College, Bengaluru
Secondary School Leaving Certificate (SSLC) - (Apr 2017 - Mar 2018) - Percentage - 93.92% - At Sri Ayyappa Education Center, Bengaluru

Shreesha's Occupation: Currently Looking for Job
Family: The only one son 
Hobbies and Interests: Developing Websites , Listening to music , Automating tasks.
Programming Languages Known : Python (Advanced), MySQL (Intermediate), C (Beginner), Java (Beginner) , Web and App Development : HTML, CSS, JS, WordPress, Android Studio, Flask, PHP, Jupyter Notebook 
Languages Known : English (Fluent), Kannada (Proficient), Hindi (Proficient)
Soft Skills : Efficient Task Prioritization, Problem-Solving, Teamwork, Creativity , Inovation, Leadership, Adaptability, Empathy, Stress Management

Shreesha's Experience: (by Interships) 
1) LearnWik, Bengaluru Machine Learning With Python Intern ,  Sep 2023 - Nov 2023
Proficient in Python, adeptly applying advanced concepts in machine learning to construct and optimize regression and classification models, enhancing performance through ensemble methods.
2) Pacewisdom, Mangaluru Python Upskill Internship , Aug 2023 - Sep 2023
Achieved a 95% efficiency rating in email communication, enhancing soft skills. Developed expertise in HTML, CSS, and Bootstrap, creating 10 responsive web designs. 
Gained extensive experience in Python Flask, deploying web applications.Led project creation and presentation, resulting in a 15% efficiency improvement in team collaboration.

Shreesha's Projects : (can see in my github)
1) Enhancing User Input with Human-Computer Interaction ,  Mar 2023 - Apr 2024
Advanced authentications: QR code scanning, face recognition, voice authentication.
Intuitive voice and gesture controls for browsing, presentations, mouse actions, and more.
Developed over 100 diverse applications such as AI-powered fitness trainers, virtual painting
tools, emotion-driven music players, gesture touch, media controllers, volume, brightness,
and scrolling controllers using real-time hand gestures. Redefining HCI with natural and
efficient computing, leveraging available resources. Integrated innovative gaming solutions
using hand gestures, body pose, and facial movements for both online and offline games.

2) Truth, BPM Analyzer and Motion Mate , Mar 2023 - Mar 2024
Implemented a lie detector using heart rate monitoring and integrated emotion detection
and visualization. Developed a real-time heart rate and behavioral analysis tool.
Motion Mate tracks human poses and evaluates performance using advanced algorithms
like cosine similarity, all processed on your device for privacy and performance.

3) Mobile Apps: Video Player, Meeting Manager , Apr 2023 - Jul 2023
Developed a feature-rich Android app with video playback, meeting scheduling, calculator,
user authentication, dynamic wallpaper, event tracking, data parsing, and text-to-speech,
showcasing comprehensive app development expertise.

4) Many Website Projects
Jun 2020 - May 2022
A feature-rich gallery with slideshow, zoom and many other functionalities. Developed
Photo Editor, educational websites for HTML, CSS, Python, and SQL learning. Created a
Flask-based web application for note-taking, YouTube to any format downloader, protected
text, and also built a WordPress website for VCFYALab. Developed and implemented a
comprehensive database management system for medical management, centralizing data
storage, enhancing inventory tracking. Developed numerous web pages for occasions such
as New Year, birthdays for friends, and Teachers Day for educators. Created platforms for
sharing notes and personal websites, as well as models for API calling and generating results.

Shreesha's CERTIFICATIONS :
Python Basics, Functions, Files, Dictionaries
Supervised Machine Learning: Regression and Classification
Mathematics for Machine Learning: Linear Algebra
Postman API Fundamentals Student Expert
C++ For C Programmers, Part A

Shreesha's ACHIEVEMENTS :
Attended Live Master class on Claude AI
1st prize in Jnanasangama, a national level student conference
2nd prize in Innovation Technology at I2connect conducted by IEEE
1st prize in code blind 
2nd prize in Quiz
2nd prize in odeve
2nd prize in Speakup 
2nd prize in Elocution competitions
Actively participated in the Yuva Sangam youth exchange program
Actively participated in the Srishti Innovation Exchange.
Attended webinar on IPR and Patent Laws
Attended sessions on Generative AI Revolution
Attended webinar on Apple Siri and AI for all
Attended Bootcamp on React and Practical Web Application Hacking
Participated in a National Level Quiz 
Qualified GATE exam (4559 AIR)
Delivered a talk on Website and App Development, HCI
Published research in the International Journal Of Creative Research Thoughts and successfully developed
Developed project into a market-ready product
Attended Essential Program in AWS Cloud Computing ZERO TO HERO
Attended PowerBI Workshop

Shreesha is Passionate AI and ML Student, Proficient in Python, Web App Development Strong Problem-Solver, Committed to Innovation, Proven Academic Achiever, Active in the Tech Community.
 
Shreesha's Youtube Channel: https://www.youtube.com/@aiforshreesha
Shreesha's Email: shreeshapilinja@gmail.com 
Shreesha's Whatsapp : https://wa.me/919353917389
Shreesha's Phone Number: +919353917389
Shreesha's Facebook: https://www.facebook.com/shreeshabaiml/
Shreesha's Instagram: https://www.instagram.com/shreeshapilinja/
Shreesha's Linkdin: https://www.linkedin.com/in/shreeshapilinja/
Shreesha's Discord: https://discordapp.com/users/1156835916208410676
Shreesha's Github : https://github.com/shreeshapilinja
"""

st.write(" 💬 Ask anything about Shreesha")
user_question = st.text_input("Enter your question:", "", label_visibility="collapsed")
if st.button("ASK",use_container_width=400):
    prompt = persona + " Here is the question the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.subheader(" ") # for spacing 

col1 , col2 = st.columns(2)

with col1:
    st.subheader(":tv: YouTube Channel")
    st.markdown("""
    - **AI & Computer Vision Featured Channel** :star:
    - **Latest Videos** :new:
    - **100s of Featured Application Showcases** :fire:
    - **All in One Video** 🎬
    - **Subscribe for More!** :bell:
    """)


with col2:
    st.video("https://www.youtube.com/embed/uh4GFXjdpKo",autoplay=True)


st.write(" ") # for spacing 
st.title("My Setup")
st.image(r"images/setup.jpg")

st.write(" ") # for spacing 
st.title("My Skills")

st.slider("Programming", 0, 100, 75)
st.slider("Web and App Development", 0, 100, 80)
st.slider("Soft Skills", 0, 100, 85)
st.slider("Soft Skills", 0, 100, 70)

# skills = {
#     "Python": 90,
#     "C++": 85,
#     "OpenCV": 80,
#     "Django": 75,
#     "Linux": 70,
#     "ROS": 65,
#     "Git": 80,
# }

# for skill, proficiency in skills.items():
#     st.slider(skill, 0, 100, proficiency)

st.title("Gallery")

st.image(r"images/long.jpg")

# col1 , col2 , col3 = st.columns(3)

# with col1:
#     st.image(r"images/g1.jpg")
#     st.image(r"images/g4.jpg")

# with col2:
#     st.image(r"images/g2.jpg")
#     st.image(r"images/g5.jpg")

# with col3:
#     st.image(r"images/g3.jpg")
#     st.image(r"images/g6.jpg")

cols = st.columns(3)

# start, end = 1, 3
# for col in cols:
#     for i in range(start, end):
#         col.image(rf"images/g{i}.jpg")
#     start += 2
#     end += 2

num_images = 6
for i in range(1, num_images + 1):
    col = cols[(i - 1) % 3]
    with col:
        col.image(rf"images/g{i}.jpg")

st.write(" ") # for spacing
st.markdown("""
    <style>
    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .line {
        width: 150px;
        height: 5px;
        background-color: blue;
        margin-top: 5px;
    }
    </style>
    <div class="center">
        <h1>Socials</h1>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .social-icons a {
        display: inline-block;
        width: 50px;
        height: 50px;
        background-color: #f1f1f1;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        transition: transform 0.3s ease;
    }
    .social-icons a:hover {
        transform: scale(1.1);
    }
    .social-icons img {
        width: 70%;
        height: 70%;
        border-radius: 5px;
    }
    </style>
    <div class="social-icons">
        <a href="https://www.youtube.com/@aiforshreesha"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube"></a>
        <a href="https://www.facebook.com/shreeshabaiml/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Facebook_f_logo_%282019%29.svg/2048px-Facebook_f_logo_%282019%29.svg.png" alt="Facebook"></a>
        <a href="https://www.instagram.com/shreeshapilinja/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png" alt="Instagram"></a>
        <a href="https://www.linkedin.com/in/shreeshapilinja/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/LinkedIn_Logo_2013.svg/2048px-LinkedIn_Logo_2013.svg.png" alt="LinkedIn"></a>
        <a href="https://discordapp.com/users/1156835916208410676"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/98/Discord_logo.svg/2048px-Discord_logo.svg.png" alt="Discord"></a>
        <a href="https://github.com/shreeshapilinja"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub"></a>
    </div>
    """, unsafe_allow_html=True)

st.title(" ")
st.write("CONTACT")
st.title("For any inquiries, email at")
st.subheader("shreeshapilinja@gmail.com")
