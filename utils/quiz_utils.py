import pandas as pd

def load_questions(filepath):
    return pd.read_csv(filepath)

#This function compares correct answers with user's answers
def calculate_score(questions, responses):
    score = 0
    for i, user_ans in enumerate(responses):
        if user_ans == questions.iloc[i]['answer']:
            score += 1
    return score