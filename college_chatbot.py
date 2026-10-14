# College Helpdesk Chatbot - Python if-elif-else version

def get_response(message):
    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey", "namaste"]):
        return "Hello! Welcome to the College Helpdesk. How can I help you?"
    elif "timing" in message or "time" in message or "open" in message:
        return "College office hours are generally 9:00 AM to 5:00 PM, Monday to Saturday. Confirm holidays with the office."
    elif "admission" in message or "apply" in message or "enroll" in message:
        return "For admission, visit the college admission office with your marksheets, ID proof, photographs, and required certificates."
    elif "fee" in message or "fees" in message or "payment" in message:
        return "For the latest fee details and deadlines, contact the accounts department or check the official college portal."
    elif "library" in message or "book" in message:
        return "The library provides textbooks and reference books. Carry your college ID card to borrow books."
    elif "exam" in message or "result" in message or "timetable" in message:
        return "Exam timetables and results are announced through the official college/university portal. Check it regularly."
    elif "course" in message or "department" in message or "diploma" in message:
        return "Please check the college prospectus or contact your department office for course and syllabus details."
    elif "contact" in message or "phone" in message or "email" in message or "address" in message:
        return "Please use the contact details listed on your college's official website."
    elif "thank" in message:
        return "You're welcome! Have a great day."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Best wishes for your studies."
    elif message in ["help", "options", "menu"]:
        return "Ask about timings, admissions, fees, library, exams/results, courses, or contact details."
    else:
        return "Sorry, I didn't understand. Type 'help' or ask about timings, admission, fees, library, exams, or courses."

print("=== College Helpdesk Chatbot ===")
print("Type 'bye' to exit.")
while True:
    user_message = input("You: ")
    bot_response = get_response(user_message)
    print("Bot:", bot_response)
    if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break
