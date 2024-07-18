# Computer_Hub_Chatbot


The Wine ChatBot project aims to provide a user-friendly interface for customers visiting a wine business's website. The chatbot allows users to inquire about various wines available, providing descriptions and prices directly from a predefined corpus of data. It uses Flask for the backend server and integrates with OpenAI's GPT-3.5 model for generating responses based on user queries.

Features
Interactive Chat Interface: Users can interact with the chatbot to ask about different wines available.
Data-driven Responses: Responses are generated from a predefined JSON corpus (wine.json) containing wine details.
Fallback Handling: If the chatbot cannot understand the user query or encounters an error, it provides fallback responses to guide the user.
Minimalistic UI: The UI is designed to be simple and intuitive, enhancing user experience.
Technologies Used
Flask: Python-based web framework used for backend development.
OpenAI GPT-3.5: AI model used for generating natural language responses.
HTML/CSS/JavaScript: Frontend technologies used for building the chatbot interface.
JSON: Data format used to store wine details (wine.json).
Setup Instructions
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd WineChatBot
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
The application will run on http://localhost:5000/.

Accessing the ChatBot:
Open a web browser and navigate to http://localhost:5000/ to interact with the Wine ChatBot.

Files and Directory Structure
app.py: Main Flask application file handling routes and logic.
wine.json: JSON file containing wine details including names, types, descriptions, and prices.
templates/: Directory containing HTML templates for the chatbot interface.
static/: Directory containing static assets (CSS, JavaScript) for styling and interactivity.
Usage
Chat Interface: Users can type messages in the input field and receive responses from the chatbot.
View Wines: Users can click on specific buttons or links to view details of different wines available.
Future Enhancements
Integration with External APIs: Fetch real-time data or reviews about wines from external sources.
Natural Language Processing (NLP) Improvements: Enhance the chatbot's ability to understand and respond to more complex queries.
User Authentication: Implement user authentication for personalized recommendations or purchases.
Contributors
Your Name
License
This project is licensed under the MIT License.
