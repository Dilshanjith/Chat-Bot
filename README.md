# AI Chatbot with GUI

This project is a simple AI-powered chatbot application built using OpenAI's API and Tkinter for the graphical user interface (GUI). The chatbot can answer questions and provide helpful responses through a user-friendly interface.

![Image](https://github.com/user-attachments/assets/76412479-24c5-498f-9053-395c66bf3818)

## Features
- **User-friendly Interface**: Simple and intuitive GUI built with Tkinter.
- **Multiline Question Input**: Allows users to input detailed questions.
- **Scrollable Answer Display**: Displays chatbot responses in a scrollable text area.
- **Error Handling**: Handles API errors and user input validation gracefully.

## Prerequisites

1. **Python**: Ensure you have Python 3.7 or later installed.
2. **OpenAI API Key**: You need an OpenAI API key to interact with the chatbot. You can obtain one from [OpenAI](https://platform.openai.com/).
3. **Required Python Libraries**: Install the following Python libraries:
   ```bash
   pip install openai
   ```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/dilshanjith/ai-chatbot-gui.git
   cd ai-chatbot-gui
   ```

2. Set up your OpenAI API key in the `main.py` file:
   ```python
   openai.api_key = "your-openai-api-key"
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## File Structure
- `main.py`: The main Python script that runs the chatbot.
- `README.md`: Documentation for the project.

## Usage
1. Launch the application.
2. Enter your question in the text box labeled "Ask a Question".
3. Click the "Ask" button to send the query to the chatbot.
4. View the chatbot's response in the "Answer" section.

## Limitations
- Requires an active internet connection to interact with OpenAI's API.
- Limited by the quota of your OpenAI API key.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more detail.

## Contributing
Feel free to fork this repository and submit pull requests with enhancements or bug fixes. For major changes, please open an issue first to discuss your ideas.

## Support
For any issues or questions, please open an issue in this repository or contact me at [your-email@example.com].
