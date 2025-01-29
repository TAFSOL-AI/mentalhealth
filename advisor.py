from ollamaserver import OllamaClient
client = OllamaClient()

# system_prompt = """
#                 You are a mental health advisor who analyzes user's mental health after holding a session of question answers with the user
#                 -these are your 10 questions:
#                     1.	How are you feeling today?
#                     (This can be open-ended or have options like: Happy, Anxious, Tired, Stressed, etc.)
#                     2.	Did anything stand out today as a positive experience?
#                     (Encourages the user to reflect on good moments.)
#                     3.	What's something you felt challenged by today?
#                     (Helps identify stressors or obstacles.)
#                     4.	On a scale of 1-10, how would you rate your energy levels today?
#                     (Measures physical and emotional energy.)
#                     5.	Did you experience any moments of stress or anxiety today? If so, how did you cope?
#                     (Explores emotional health and coping strategies.)
#                     6.	How was your sleep last night?
#                     (Simple check-in on rest, which greatly affects mental health.)
#                     7.	How were your interactions with others today?
#                     (Assesses relationship dynamics and social well-being.)
#                     8.	Did you have time for self-care today?
#                     (Focuses on self-care and mindfulness.)
#                     9.	How's your appetite been today?
#                     (A check on physical health that can influence mental well-being.)
#                     10.	What's one thing you're grateful for today?
#                     (Encourages positive thinking and self-reflection.)
                
#                 -You will only ask these questions.
#                 -Your only objective is to ask these questions and nothing else.
#                 -You are restricted to these questions 
#                 """
# message_context = []
# answer_context = []
# message_context.append({"role":"system", "content": system_prompt})

def start_questions():
    questions = [
        "How are you feeling today?",  
        "Did anything stand out today as a positive experience?",  
        "What's something you felt challenged by today?",  
        "On a scale of 1-10, how would you rate your energy levels today?",  
        "Did you experience any moments of stress or anxiety today? If so, how did you cope?",  
        "How was your sleep last night?",  
        "How were your interactions with others today?",  
        "Did you have time for self-care today?",  
        "How's your appetite been today?",  
        "What's one thing you're grateful for today?"
    ]
    # qna = """Question 1: How are you feeling today?\nAnswer: Feeling exausted\n\nQuestion 2: Did anything stand out today as a positive experience?\nAnswer: No, not a single one\n\nQuestion 3: What's something you felt challenged by today?\nAnswer: Work load, i am not getting any leisure time to relax my minds\n\nQuestion 4: On a scale of 1-10, how would you rate your energy levels today?\nAnswer: 1\n\nQuestion 5: Did you experience any moments of stress or anxiety today? If so, how did you cope?\nAnswer: Yes, facing lot of problems in current ongoing project, i spent entire day debugging the errors\n\nQuestion 6: How was your sleep last night?\nAnswer: Only got 4 hours sleep due to mentally tiredness\n\nQuestion 7: How were your interactions with others today?\nAnswer: Normal with my collegue. But with outsiders very bad\n\nQuestion 8: Did you have time for self-care today?\nAnswer: No not a single second\n\nQuestion 9: How's your appetite been today?\nAnswer: Very bad, food was cold\n\nQuestion 10: What's one thing you're grateful for today?\nAnswer: Atleast i have a job\n\n"""
    qna = ""
    count = 0
    for q in questions:
        count += 1
        print(f"\nBOT: {q}")
        user_reply = input("-------------------------------------------------\nYOU: ")
        qna = qna + f"Question {count}: " + q + "\nAnswer: " + user_reply + "\n\n"
    print("Creating summary.....")
    return qna



# while True:
#     user_prompt = input("You: ")
#     message_context.append({"role":"user", "content": user_prompt})
#     response = client.generate_response(messages=message_context, model_name="llama3.2")
#     answer_text = response["message"]["content"]
#     answer_context.append(answer_text)

def getSummary(qna, user_name, user_num, session_num):
    summary_prompt = f"""You are a mental health advisor and your goal is to create summary by analyzing a question answer session
                    held with the user. The content of the question answers will be provided by the user. The user name and
                    phone number will be provided so make sure you include user name and phone number in summary for retrieval purpose.
                    Make sure you include session number in the summary as well. here session number is {session_num}
                    """
    message_context = []
    user_name = input("Give me your name\n")
    user_num = input("Give me your phone number\n")
    message_context.append({"role":"system", "content": summary_prompt})
    message_context.append({"role":"user", "content": f"User Name: {user_name}, User Number: {user_num}. Generate user summary based on these questions {qna}"})
    response = client.generate_response(messages=message_context, model_name="llama3.2")
    answer_text = response["message"]["content"]
    print("----------------------\nCREATED!")

    return answer_text
def getData():
    summary_prompt = f"""You are a mental health advisor and your goal is to create summary by analyzing a question answer session
                    held with the user. The content of the question answers will be provided by the user. The user name and
                    phone number will be provided so make sure you include user name and phone number in summary for retrieval purpose.
                    Make sure you include the session number in the summary as well. Session number is 1.
                    """
    qna = start_questions()
    message_context = []
    user_name = input("Give me your name\n")
    user_num = input("Give me your phone number\n")
    message_context.append({"role":"system", "content": summary_prompt})
    message_context.append({"role":"user", "content": f"User Name: {user_name}, User Number: {user_num}. Generate user summary based on these questions {qna}"})
    response = client.generate_response(messages=message_context, model_name="llama3.2")
    answer_text = response["message"]["content"]
    print("----------------------\nCREATED!")
    return answer_text
