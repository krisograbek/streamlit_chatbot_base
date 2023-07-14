## Template for creating your own ChatGPT with Streamlit and OpenAI API

This repository contains the code for a simple web application built with Streamlit, which uses OpenAI's GPT-3 model for generating AI responses in a chat-like interface.

### Prerequisites
1. Python 3.6 or above
2. An OpenAI API Key


### Steps to run the application
1 Clone the repository to your local machine:
```shell
git clone https://github.com/krisograbek/streamlit_chatbot_base.git
```

2. Navigate to the project directory:
```shell
cd streamlit_chatbot_base
```

3. Create a virtual environment and activate it:

On macOS and Linux:
shell
Copy code
python3 -m venv myenv
source myenv/bin/activate
On Windows:
shell
Copy code
python -m venv myenv
.\myenv\Scripts\activate
Install the necessary Python packages:
shell
Copy code
pip install -r requirements.txt
Create a .env file in the root directory of the project and add your OpenAI API key:
shell
Copy code
echo OPENAI_API_KEY=your-api-key > .env
Please replace your-api-key with your actual OpenAI API key.

Run the Streamlit application:
shell
Copy code
streamlit run your-app-script.py
Please replace your-app-script.py with the name of your Streamlit app script.

Open a web browser and navigate to http://localhost:8501 to interact with the application.
License
This project is open source, under the terms of the MIT license.

Note: This app makes requests to OpenAI's servers whenever the chat is used. Please be aware of this, especially if you're on a paid plan with OpenAI.
