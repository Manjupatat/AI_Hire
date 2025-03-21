
# AI Interview Bot

## 🚀 Overview
The **AI Interview Bot** is a smart chatbot that conducts technical interviews based on a user's resume. It generates customized questions from the uploaded resume and evaluates responses in a WhatsApp-style chat format using **Streamlit** and **Google Gemini AI**.

## ✨ Features
✅ **ChatGPT-like UI** (WhatsApp-style chat interaction)  
✅ **AI-generated Interview Questions** (Tailored to user's skills)  
✅ **Streamlit Web Interface** (Interactive and user-friendly)  


---

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/ai-interview-bot.git
cd ai-interview-bot
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
Create a **`.streamlit/secrets.toml`** file and add your Google API Key:
```toml
[general]
GOOGLE_API_KEY = "your_google_api_key_here"
```

### 5️⃣ Run the App
```sh
streamlit run main.py
```


---

🎥 Live Demo

Check out the live demo: [AI Interview Bot Demo](https://hire-bot-oztt.onrender.com/)

---

## 📄 How It Works
1️⃣ **User enters name** 👤  
2️⃣ **Uploads resume (PDF/DOCX)** 📄  
3️⃣ **AI extracts skills & generates questions** 🤖  
4️⃣ **User answers in a chat format** 💬  
5️⃣ **AI evaluates and provides feedback** ✅  
6️⃣ **After all questions, AI thanks the user** 🎉  

---

## 🏗️ Technologies Used
- **Python** 🐍
- **Streamlit** 🎨 (Frontend UI)
- **Google Gemini AI** 🧠 (AI-powered interview)
- **PyPDF2 & python-docx** 📄 (Resume processing)

---

## 📌 Future Enhancements
- **Multilingual Support** 🌍
- **More Interview Modes** (Behavioral, HR, etc.)
- **Live Coding Challenges** 💻
- **Database Integration for Reports** 📊

---

## 💡 Contributing
Feel free to submit PRs, open issues, and contribute to making this bot even better! 😊

---

## 📞 Contact
For any queries or suggestions, reach out to:  
📧 **Email**: manjupatat80@gmail.com  
🐙 **GitHub**: [Manjunath L Patat](https://github.com/Manjupatat)

>>>>>>> 30ee8ae (Initial commit)
