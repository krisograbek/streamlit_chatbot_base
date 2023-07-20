## Template for creating your own ChatGPT with Streamlit and OpenAI API

This repository contains the code for a simple web application built with [Streamlit](https://streamlit.io/), which uses OpenAI's GPT-3 model for generating AI responses in a chat-like interface.

### Prerequisites
1. Python 3.6 or above
2. An OpenAI API Key

### App Demo
![StreamlitChatbot](https://github.com/krisograbek/streamlit_chatbot_base/assets/48050596/e1c62c71-0b3d-4a3b-9855-e48fc73e402b)


### Steps to run the application
**1. Clone the repository to your local machine:**
```shell
git clone https://github.com/krisograbek/streamlit_chatbot_base.git
```

**2. Navigate to the project directory:**
```shell
cd streamlit_chatbot_base
```

3. Create a virtual environment and activate it:

On macOS and Linux:
```shell
python3 -m venv myenv
source myenv/bin/activate
```

On Windows:
```shell
python -m venv myenv
.\myenv\Scripts\activate
```

3a. Upgrade pip (optional but recommended)
```shell
pip install --upgrade pip
```

4. Install the necessary Python packages:
```shell
pip install -r requirements.txt
```

5. Create a .env file in the root directory of the project and add your OpenAI API key:
```shell
echo OPENAI_API_KEY=your-api-key > .env
```
OR

```shell
cp .env.example .env
```

Please replace your-api-key with your actual OpenAI API key.

6. Run the Streamlit application:
```shell
streamlit run chatbot.py
```

Open a web browser and navigate to http://localhost:8501 to interact with the application.

License
This project is open source, under the terms of the MIT license.

Note: This app makes requests to OpenAI's servers whenever the chat is used. Please be aware of this, especially if you're on a paid plan with OpenAI.
