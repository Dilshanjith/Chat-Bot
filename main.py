import openai
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Set your OpenAI API key
openai.api_key ="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"

# Function to handle OpenAI API calls
def ask_openai():
    user_question = question_entry.get("1.0", tk.END).strip()
    if not user_question:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Replace with the appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        answer_display.configure(state="normal")
        answer_display.delete("1.0", tk.END)
        answer_display.insert(tk.END, answer)
        answer_display.configure(state="disabled")
    except openai.error.RateLimitError:
        messagebox.showerror("API Error", "API Quota Exceeded. Please check your usage or try again later.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Create the main GUI window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("600x400")
root.resizable(False, False)

# Widgets
# Question Label
question_label = tk.Label(root, text="Ask a Question:", font=("Arial", 12))
question_label.pack(pady=10, anchor="w", padx=20)

# Question Entry (multiline)
question_entry = tk.Text(root, height=4, width=60, font=("Arial", 10))
question_entry.pack(pady=5, padx=20)

# Ask Button
ask_button = tk.Button(root, text="Ask", font=("Arial", 12), command=ask_openai)
ask_button.pack(pady=10)

# Answer Label
answer_label = tk.Label(root, text="Answer:", font=("Arial", 12))
answer_label.pack(pady=10, anchor="w", padx=20)

# Answer Display (readonly)
answer_display = scrolledtext.ScrolledText(root, height=10, width=60, font=("Arial", 10), state="disabled", wrap=tk.WORD)
answer_display.pack(pady=5, padx=20)

# Start the GUI event loop
root.mainloop()