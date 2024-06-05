from customtkinter import *
from tkinter import messagebox
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

root = CTk()
root.title('Sentiment Detector v1.0')
root.geometry('650x500')
root.resizable(False, False)

# APP name Label
name_label = CTkLabel(root, text="Sentiment Detector", font=("Century Gothic", 30))
name_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Sentiment Entry
sentiment_text = CTkTextbox(root, font=("Century Gothic", 15), border_width=2, width=350)
sentiment_text.place(relx=0.5, rely=0.4, anchor=CENTER)

# Theme
a = 1


def theme_():
    global a
    if a == 1:
        set_appearance_mode("dark")
        a = 0
    elif a == 0:
        set_appearance_mode("light")
        a = 1


theme_switch = CTkSwitch(root, text="Theme", font=("Century Gothic", 15), command=theme_)
theme_switch.place(relx=0.93, rely=0.05, anchor=CENTER)


# check Sentiment Button
def check_sentiment():
    result = sentiment_text.get(1.0, END)
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_score = sentiment_analyzer.polarity_scores(result)
    sentiment_type = 'Positive' if sentiment_score['compound'] >= 0.05 else 'Negative' if sentiment_score[
                                                                                              'compound'] <= -0.05 else 'Neutral'
    messagebox.showinfo("Sentiment Result", f"The sentiment is: {sentiment_type}")


check_button = CTkButton(root, text="Check Sentiment", font=("Century Gothic", 15), command=check_sentiment, width=320)
check_button.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
