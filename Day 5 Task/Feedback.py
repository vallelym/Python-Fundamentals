rating_phrases = {
    1: "Poor",
    2: "Fair",
    3: "Good",
    4: "Very Good",
    5: "Excellent"
}

detailed_templates = {
    1: {
        "Understanding Level": "Your understanding level is poor. Please focus on understanding the core concepts better. Additional practice and support may be required.",
        "Contribution Level": "Your contribution level is poor. You need to participate more actively in class discussions and activities.",
        "Lab Comfortability": "Your comfortability in the lab is poor. Consider spending more time familiarizing yourself with the lab environment and equipment.",
        "Engagement Level": "Your engagement level is poor. Try to be more attentive and involved during sessions.",
        "Punctuation Level": "Your punctuation level is poor. Ensure you are punctual and adhere to deadlines.",
        "Further Learning": "Your further learning needs significant improvement. Seek additional resources and support to enhance your learning."
    },
    2: {
        "Understanding Level": "Your understanding level is fair. There are areas that need attention and improvement.",
        "Contribution Level": "Your contribution level is fair. Try to contribute more consistently in class.",
        "Lab Comfortability": "Your comfortability in the lab is fair. Spend more time practicing to become more comfortable.",
        "Engagement Level": "Your engagement level is fair. Increase your participation and focus during sessions.",
        "Punctuation Level": "Your punctuation level is fair. Work on being more punctual and meeting deadlines.",
        "Further Learning": "Your further learning could be better. Consider seeking additional resources or help."
    },
    3: {
        "Understanding Level": "Your understanding level is good. You have a good grasp of the basics but there is room for improvement.",
        "Contribution Level": "Your contribution level is good. You participate well but can contribute even more.",
        "Lab Comfortability": "Your comfortability in the lab is good. Continue practicing to enhance your skills.",
        "Engagement Level": "Your engagement level is good. Stay focused and involved to improve further.",
        "Punctuation Level": "Your punctuation level is good. Maintain your punctuality and adherence to deadlines.",
        "Further Learning": "Your further learning is satisfactory. Keep practicing to enhance your skills."
    },
    4: {
        "Understanding Level": "Your understanding level is very good. You have a strong grasp of the concepts.",
        "Contribution Level": "Your contribution level is very good. You actively participate and contribute valuable insights.",
        "Lab Comfortability": "Your comfortability in the lab is very good. You handle the lab environment and equipment well.",
        "Engagement Level": "Your engagement level is very good. You are attentive and involved during sessions.",
        "Punctuation Level": "Your punctuation level is very good. You are punctual and meet deadlines consistently.",
        "Further Learning": "Your further learning is very good. Continue to engage actively and refine your skills."
    },
    5: {
        "Understanding Level": "Your understanding level is excellent. You have a thorough understanding of the concepts.",
        "Contribution Level": "Your contribution level is excellent. You make significant contributions to class discussions and activities.",
        "Lab Comfortability": "Your comfortability in the lab is excellent. You are highly proficient with the lab environment and equipment.",
        "Engagement Level": "Your engagement level is excellent. You are highly attentive and involved during sessions.",
        "Punctuation Level": "Your punctuation level is excellent. You are always punctual and adhere to deadlines.",
        "Further Learning": "Your further learning is excellent. Keep up the great work and continue to excel."
    }
}

general_template = """
Feedback for {name}
====================
Understanding Level: {understanding} - {understanding_detail}
Contribution Level: {contribution} - {contribution_detail}
Lab Comfortability: {lab_comfort} - {lab_comfort_detail}
Engagement Level: {engagement} - {engagement_detail}
Punctuation Level: {punctuation} - {punctuation_detail}
Further Learning: {learning} - {learning_detail}

General Comments:
{comments}
"""

name = input("Please enter your name: ")

feedback = {}

categories = ["Understanding Level", "Contribution Level", "Lab Comfortability", "Engagement Level", "Punctuation Level", "Further Learning"]
for category in categories:
    while True:
        try:
            rating = int(input(f"Rate your {category} (1-5): "))
            if 1 <= rating <= 5:
                feedback[category] = (rating_phrases[rating], detailed_templates[rating][category])
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

comments = input("Please enter any general comments: ")

filename = f"{name}_feedback.txt"

with open(filename, "w") as file:
    file.write(general_template.format(
        name=name,
        understanding=feedback["Understanding Level"][0],
        understanding_detail=feedback["Understanding Level"][1],
        contribution=feedback["Contribution Level"][0],
        contribution_detail=feedback["Contribution Level"][1],
        lab_comfort=feedback["Lab Comfortability"][0],
        lab_comfort_detail=feedback["Lab Comfortability"][1],
        engagement=feedback["Engagement Level"][0],
        engagement_detail=feedback["Engagement Level"][1],
        punctuation=feedback["Punctuation Level"][0],
        punctuation_detail=feedback["Punctuation Level"][1],
        learning=feedback["Further Learning"][0],
        learning_detail=feedback["Further Learning"][1],
        comments=comments
    ))

print(f"Feedback saved to {filename}")
