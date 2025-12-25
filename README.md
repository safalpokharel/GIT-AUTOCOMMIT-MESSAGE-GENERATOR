🤖 Auto Commit Message Generator
I often found myself stuck when writing Git commit messages. Sometimes I didn’t know how to properly describe my changes, and other times I just rushed it. To make this easier, I built an Auto Commit Message Generator.
This is a Python CLI tool that reads your staged Git changes and uses Google Gemini to generate a clear, descriptive commit message. You can review or edit the suggested message before it commits automatically.

💡 What This Tool Does
Checks if you’re inside a Git repository
Detects if there are staged changes
Reads the Git diff of staged files
Generates a commit message using Google Gemini AI
Lets you edit the message if you want
Commits the changes for you

🛠 Technologies Used
Python
Git
Google Gemini API
python-dotenv for environment variables
rich for better terminal output

▶️ How to Use in Any Git Project
1. Clone this repo (if you haven’t already)
    git clone https://github.com/safalpokharel/GIT-AUTOCOMMIT-MESSAGE-GENERATOR.git

2. Install dependencies
    pip install -r requirements.txt

3. Set up your API key
    Create a .env file in the generator folder:
    GOOGLE_GEMINI_API_KEY=your_api_key_here

4. Stage changes in your project
    git add .

5. Run the generator script
    From any Git project folder, run:
    python /full/path/to/GIT-AUTOCOMMIT-MESSAGE-GENERATOR/main.py

6. Review and edit the suggested message
    The script will display a suggested commit message and let you edit it if you want. After that, it commits automatically.

🧠 What I Learned
This project helped me:
Work with Git programmatically
Use environment variables securely
Integrate AI APIs into real developer tools
Improve terminal UX using rich
Build a practical productivity tool for developers

👤 Author
Safal Pokharel