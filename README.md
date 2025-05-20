# AI-Powered Code Review Assistant

A Python application that uses AI to provide automated code reviews for your code snippets.

## Overview

This application allows users to submit code snippets (primarily Python code) and receive AI-powered feedback on potential bugs, code style, best practices, and efficiency improvements. The application uses LangChain with Google Gemini (or optionally OpenAI) to analyze code and provide actionable suggestions.

## Features

- 🔍 **Identify potential bugs and logic errors**
- 📝 **Code style and readability suggestions**
- ⚙️ **Best practice recommendations**
- ⚡ **Performance and efficiency insights**
- 💻 **Simple, browser-based user interface**

## Requirements

- Python 3.7+
- An API key for either Google Gemini or OpenAI

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-code-review-assistant.git
   cd ai-code-review-assistant
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Copy `example.env` to `.env`
   ```bash
   cp example.env .env
   ```
   - Edit `.env` and add your API key:
     - For Google Gemini: Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
     - For OpenAI: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Paste your code snippet into the text area

4. Click "Review Code" to get AI feedback on your code

## Customization

### Switching LLM Providers

By default, the application uses Google Gemini. To switch to OpenAI:

1. Edit `app.py` and change `LLM_PROVIDER = "google"` to `LLM_PROVIDER = "openai"`
2. Uncomment the OpenAI configuration sections in both `app.py` and `requirements.txt`
3. Make sure you have an OpenAI API key in your `.env` file

### Custom Prompts

You can modify the prompts used for code review by editing the `prompts.py` file:

- `CODE_REVIEW_PROMPT_TEMPLATE` - The main prompt for general code review
- `PYTHON_STYLE_CHECK_PROMPT_TEMPLATE` - A more specific prompt for Python style checks

## Project Structure

```
ai-code-review-assistant/
├── app.py             # Main Streamlit application
├── requirements.txt   # Python dependencies
├── prompts.py         # LLM prompt templates
├── .env.example       # Example environment variables file
└── .gitignore         # Git ignore file
```

## Future Improvements

- Support for additional programming languages
- Custom review types (security-focused, performance-focused, etc.)
- Ability to upload entire files or directories
- Integration with GitHub/GitLab for automated PR reviews

## License

This project is licensed under the MIT License - see the LICENSE file for details. 