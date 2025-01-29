from retrieval import search_faiss, startChat
from advisor import getData, getSummary, start_questions
from embed import add_to_faiss
import os

name = input("\nEnter Your Name: ")
user_number = input("\nEnter your phone number: ")
db = f"{user_number}_Faiss.bin"
while True:
    session_num = (input("\nSession Number: "))
    try:
        session = int(session_num)
        break
    except:
        print("\nEnter valid integer")

retrieval_session = session - 1
if os.path.exists(f"{db}"):
    print("\n\nYour previous Session Exists!!")
    query = f"Give me summary for session number: {retrieval_session}"
    new_qna = start_questions()
    new_summary = getSummary(qna=new_qna, session_num=session, user_name=name, user_num=user_number)
    add_to_faiss(data=new_summary, user_number=user_number)
    user_summary = search_faiss(user_number, query=query, top_k=1)
    startChat(user_summary)
else:
    userData = getData(name, user_number)
    add_to_faiss(data=userData, user_number=user_number)
