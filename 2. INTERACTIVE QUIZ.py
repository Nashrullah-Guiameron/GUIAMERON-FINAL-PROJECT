import random

# Sample subset of trivia questions about the Philippines
questions = [
    {"question": "What is the capital city of the Philippines?", "answer": "Manila"},
    {"question": "In what year did the Philippines gain independence from the United States?", "answer": "1946"},
    {"question": "What is the national language of the Philippines?", "answer": "Filipino"},
    {"question": "What is the name of the traditional Filipino martial art?", "answer": "Arnis"},
    {"question": "Which Filipino festival is known as the 'Mother of all Philippine Festivals'?", "answer": "Ati-Atihan"},
    {"question": "Who is known as the 'Father of Philippine Revolution'?", "answer": "Andres Bonifacio"},
    {"question": "What is the largest island in the Philippines?", "answer": "Luzon"},
    {"question": "Which famous Filipino boxer is also a senator?", "answer": "Manny Pacquiao"},
    {"question": "What is the traditional Filipino cloth worn by women during special occasions?", "answer": "Baro't Saya"},
    {"question": "Which Filipino dish is made with marinated meat, usually pork or chicken, cooked in vinegar, soy sauce, and garlic?", "answer": "Adobo"},
    {"question": "What is the highest mountain in the Philippines?", "answer": "Mount Apo"},
    {"question": "Who was the first president of the Philippines?", "answer": "Emilio Aguinaldo"},
    {"question": "What is the name of the smallest primate found in the Philippines?", "answer": "Tarsier"},
    {"question": "Which city is known as the 'Queen City of the South'?", "answer": "Cebu"},
    {"question": "What is the name of the famous river in Palawan known for its underground cave system?", "answer": "Puerto Princesa Underground River"},
    {"question": "What is the Filipino term for the traditional boat used for fishing and transport?", "answer": "Bangka"},
    {"question": "Who is the national hero of the Philippines known for his novel 'Noli Me Tangere'?", "answer": "Jose Rizal"},
    {"question": "What is the Filipino festival that celebrates the blooming of flowers in Baguio City?", "answer": "Panagbenga"},
    {"question": "Which province is known as the 'Sugar Bowl of the Philippines'?", "answer": "Negros Occidental"},
    {"question": "What is the name of the traditional Filipino game similar to hopscotch?", "answer": "Piko"},
    {"question": "What is the name of the traditional Filipino Christmas lantern?", "answer": "Parol"},
    {"question": "Which city is known as the 'City of Pines'?", "answer": "Baguio"},
    {"question": "What is the Filipino term for a communal feast typically held during festivals?", "answer": "Fiesta"},
    {"question": "Which Philippine island is famous for its white sand beaches and vibrant nightlife?", "answer": "Boracay"},
    {"question": "What is the name of the Filipino dish made with boiled meat and vegetables, typically served in a broth?", "answer": "Sinigang"},
    {"question": "Who is the first Filipino to win a Pulitzer Prize?", "answer": "Carlos P. Romulo"},
    {"question": "What is the name of the oldest Chinatown in the world, located in Manila?", "answer": "Binondo"},
    {"question": "Which Filipino actress won the Best Actress award at the Cannes Film Festival for the movie 'Ma' Rosa'?", "answer": "Jaclyn Jose"},
    {"question": "What is the Filipino word for 'thank you'?", "answer": "Salamat"},
    {"question": "What is the name of the traditional Filipino folk dance that involves two people beating, tapping, and sliding bamboo poles on the ground?", "answer": "Tinikling"},
    {"question": "Who is known as the 'Star for All Seasons' in Philippine showbiz?", "answer": "Vilma Santos"},
    {"question": "What is the name of the longest-running noontime show in the Philippines?", "answer": "Eat Bulaga!"},
    {"question": "Which actress is known as the 'Diamond Star' of Philippine cinema?", "answer": "Maricel Soriano"},
    {"question": "Who was the first Filipino to win the Best Director award at the Cannes Film Festival?", "answer": "Brillante Mendoza"},
    {"question": "What is the name of the Filipino boy band that gained international fame for their synchronized dance routines?", "answer": "SB19"},
    {"question": "Which actress is dubbed as the 'Queen of All Media' in the Philippines?", "answer": "Kris Aquino"},
    {"question": "Who played the lead role in the Filipino historical film 'Heneral Luna'?", "answer": "John Arcilla"},
    {"question": "Which Filipino actor is known for his role as 'Ang Probinsyano'?", "answer": "Coco Martin"},
    {"question": "Who is the Filipino singer known as the 'Asia's Songbird'?", "answer": "Regine Velasquez"},
    {"question": "What is the title of the hit Filipino romantic comedy film starring John Lloyd Cruz and Bea Alonzo?", "answer": "One More Chance"},
    {"question": "Which Filipino actress starred in the Hollywood film 'Crazy Rich Asians'?", "answer": "Kris Aquino"},
    {"question": "Who is known as the 'Comedy King' of Philippine showbiz?", "answer": "Dolphy"},
    {"question": "Which actress is known for her role as 'Darna' in multiple adaptations of the Filipino superhero?", "answer": "Angel Locsin"},
    {"question": "What is the title of the popular Filipino TV drama series that ran for almost two decades?", "answer": "Maalaala Mo Kaya"},
    {"question": "Who is the famous Filipino comedian known for his character 'Enteng Kabisote'?", "answer": "Vic Sotto"},
    {"question": "Which Filipino actress won the Best Actress award at the 2013 Asian Film Awards for her role in 'Thy Womb'?", "answer": "Nora Aunor"},
    {"question": "What is the name of the Filipino reality talent show franchise that has produced successful artists like Sarah Geronimo?", "answer": "Starstruck"},
    {"question": "Which Filipino actor starred in the film 'On the Job', which was screened at the Cannes Film Festival?", "answer": "Piolo Pascual"},
    {"question": "Who is the Filipino singer known for her hit song 'Tala'?", "answer": "Sarah Geronimo"},
    {"question": "What is the name of the Filipino TV network known for its long-running show 'Ang Probinsyano'?", "answer": "ABS-CBN"},
    {"question": "What is the traditional Filipino folk dance that mimics the movements of a duck?", "answer": "Itik-Itik"},
    {"question": "What is the name of the Filipino tradition of visiting the homes of friends and relatives during Christmas to ask for gifts?", "answer": "Pamamasko"},
    {"question": "What is the traditional Filipino celebration of a girl's 18th birthday?", "answer": "Debut"},
    {"question": "Which Filipino festival is celebrated every January in Cebu City to honor the Santo Niño?", "answer": "Sinulog"},
    {"question": "What is the Filipino term for the spirit of communal unity and cooperation?", "answer": "Bayanihan"},
    {"question": "What is the traditional Filipino leaf wrap used to steam rice cakes?", "answer": "Banana Leaf"},
    {"question": "What is the name of the traditional Filipino courtship serenade?", "answer": "Harana"},
    {"question": "Which Filipino festival features giant lanterns and is held in San Fernando, Pampanga?", "answer": "Giant Lantern Festival"},
    {"question": "What is the traditional Filipino way of cooking where food is cooked using bamboo tubes?", "answer": "Binulo"},
    {"question": "What is the Filipino term for respect shown to elders by taking their hand and placing it on one's forehead?", "answer": "Mano Po"},
    {"question": "What is the Filipino custom of offering food to visitors as a sign of hospitality?", "answer": "Pakain"},
    {"question": "What is the name of the traditional Filipino Christmas decoration made from bamboo and paper?", "answer": "Parol"},
    {"question": "What is the Filipino term for the traditional handwoven cloth from the northern regions of the Philippines?", "answer": "Inabel"},
    {"question": "What is the Filipino festival that celebrates the bountiful harvest of rice?", "answer": "Pahiyas Festival"},
    {"question": "What is the name of the Filipino traditional healing practice that uses a bolo knife?", "answer": "Arbularyo"},
    {"question": "What is the Filipino tradition of honoring deceased loved ones by visiting their graves on November 1st and 2nd?", "answer": "Undas"},
    {"question": "What is the traditional Filipino soup made with tamarind broth and various meats?", "answer": "Sinigang"},
    {"question": "What is the Filipino term for a traditional village or community gathering?", "answer": "Barangay Fiesta"},
    {"question": "What is the name of the Filipino traditional harvest dance from the Ilocos region?", "answer": "Pandanggo sa Ilaw"},
    {"question": "What is the Filipino term for the traditional communal dining style where food is laid out on banana leaves and eaten by hand?", "answer": "Boodle Fight"},
     {"question": "What is the national flower of the Philippines?", "answer": "Sampaguita"},
    {"question": "What is the national tree of the Philippines?", "answer": "Narra"},
    {"question": "What is the national bird of the Philippines?", "answer": "Philippine Eagle"},
    {"question": "What is the national animal of the Philippines?", "answer": "Carabao"},
    {"question": "What is the national fruit of the Philippines?", "answer": "Mango"},
    {"question": "What is the national fish of the Philippines?", "answer": "Bangus"},
    {"question": "What is the national leaf of the Philippines?", "answer": "Anahaw"},
    {"question": "What is the national gem of the Philippines?", "answer": "Philippine Pearl"},
    {"question": "What is the national dance of the Philippines?", "answer": "Tinikling"},
    {"question": "What is the national hero of the Philippines?", "answer": "Jose Rizal"},
    {"question": "What is the national language of the Philippines?", "answer": "Filipino"},
    {"question": "What is the national costume for men in the Philippines?", "answer": "Barong Tagalog"},
    {"question": "What is the national house of the Philippines?", "answer": "Bahay Kubo"},
    {"question": "What is the national vehicle of the Philippines?", "answer": "Jeepney"},
    {"question": "What is the national instrument of the Philippines?", "answer": "Kudyapi"},
    {"question": "What is the national leaf-wrapped rice cake of the Philippines?", "answer": "Suman"},
    {"question": "What is the national anthem of the Philippines?", "answer": "Lupang Hinirang"},
    {"question": "What is the national dish of the Philippines?", "answer": "Adobo"},
    {"question": "What is the national anthem of the Philippines?", "answer": "Lupang Hinirang"},
    {"question": "Who is the first female president of the Philippines?", "answer": "Corazon Aquino"},
    {"question": "Which Philippine president declared Martial Law in 1972?", "answer": "Ferdinand Marcos"},
    {"question": "Who is the current president of the Philippines as of 2024?", "answer": "Ferdinand 'Bongbong' Marcos Jr."},
    {"question": "Which Philippine president was known for the 'Strong Republic' slogan?", "answer": "Gloria Macapagal-Arroyo"},
    {"question": "What is the term length for a Philippine senator?", "answer": "6 years"},
    {"question": "Who was the Philippine president during World War II and the Japanese occupation?", "answer": "Jose P. Laurel"},
    {"question": "Which political figure is known as the 'Iron Butterfly'?", "answer": "Imelda Marcos"},
    {"question": "Who was the first president of the independent Third Republic of the Philippines?", "answer": "Manuel Roxas"},
    {"question": "What is the name of the building that houses the Philippine Senate?", "answer": "GSIS Building"},
    {"question": "Which political party did Rodrigo Duterte belong to when he won the presidency in 2016?", "answer": "PDP-Laban"}
]

# Function to run the quiz
def run_quiz():
    score = 0
    user_answers = []
    random.shuffle(questions)
    
    print("Welcome to the Philippines Trivia Quiz!")
    print("There are a total of 100 questions. Try to answer as many as you can correctly.\n")
    
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        user_answer = input("Your answer: ")
        user_answers.append({"question": q['question'], "your_answer": user_answer, "correct_answer": q['answer']})
        if user_answer.strip().lower() == q['answer'].strip().lower():
            score += 1
    
    print("\nQuiz completed!")
    print(f"Your final score is {score} out of {len(questions)}.\n")
    
    print("Review your answers:")
    for ua in user_answers:
        print(f"Question: {ua['question']}")
        print(f"Your answer: {ua['your_answer']}")
        print(f"Correct answer: {ua['correct_answer']}\n")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
