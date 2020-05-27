with open("dna.txt", "r") as dna_file:
    dna_string = dna_file.read()

# hair_is_black = "CCAGCAATCGC"
# hair_is_brown = "GCCAGTGCCG"
# hair_is_blonde = "TTAGCTATCGC"
#
# facial_is_square = "GCCACGG"
# facial_is_round = "ACCACAA"
# facial_is_oval = "AGGCCTCA"
#
# eye_is_blue = "TTGTGGTGGC"
# eye_is_green = "GGGAGGTGGC"
# eye_is_brown = "AAGTAGTGAC"
#
# gender_is_female = "TGAAGGACCTTC"
# gender_is_male = "TGCAGGAACTTC"
#
# race_is_white = "AAAACCTCA"
# race_is_black = "CGACTACAG"
# race_is_asian = "CGCGGGCCG"

# Eva = [gender_is_female, race_is_white, hair_is_blonde, eye_is_blue, facial_is_oval]
# Larisa = [gender_is_female, race_is_white, hair_is_brown, eye_is_brown, facial_is_oval]
# Matej = [gender_is_male, race_is_white, hair_is_black, eye_is_blue, facial_is_oval]
# Miha = [gender_is_male, race_is_white, hair_is_brown, eye_is_green, facial_is_square]

suspect = []
# if gender_is_female in dna_string:
#     print("is female")
#     suspect.append(gender_is_female)
# else:
#     print("is male")
#     suspect.append(gender_is_male)
#
# if race_is_white in dna_string:
#     print("is white")
#     suspect.append(race_is_white)
# elif race_is_asian in dna_string:
#     print("is asian")
#     suspect.append(race_is_asian)
# else:
#     print("is black")
#     suspect.append(race_is_black)
#
# if eye_is_blue in dna_string:
#     print("eye is blue")
#     suspect.append(eye_is_blue)
# elif eye_is_brown in dna_string:
#     print("eye is brown")
#     suspect.append(eye_is_brown)
# else:
#     print("eye is green")
#     suspect.append(eye_is_green)
#
# if facial_is_oval in dna_string:
#     print("facial is oval")
#     suspect.append(facial_is_oval)
# elif facial_is_round in dna_string:
#     print("facial is round")
#     suspect.append(facial_is_round)
# else:
#     print("facial is square")
#     suspect.append(facial_is_square)
#
# if hair_is_black in dna_string:
#     print("hair is black")
#     suspect.append(hair_is_black)
# elif hair_is_blonde in dna_string:
#     print("hair is blonde")
#     suspect.append(hair_is_blonde)
# else:
#     print("hair is brown")
#     suspect.append(hair_is_brown)
#
# for guess in suspect:
#     if suspect in Eva:
#         print("The suspect is Eva")
#     elif suspect in Larisa:
#         print("The suspect is Larisa")
#     elif suspect in Matej:
#         print("The suspect is Matej")
#     else:
#         print("The suspect is Miha")

hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGACTACAG"}

people = {"Eva": ["female", "white", "blonde", "blue", "oval"],
"Larisa": ["female", "white", "brown", "brown", "oval"],
"Matej": ["male", "white", "black", "blue", "oval"],
"Miha": ["male", "white", "brown", "green", "square"]}

for i in gender:
    if gender[i] in dna_string:
        suspect.append(i)
for i in race:
    if race[i] in dna_string:
        suspect.append(i)
for i in hair:
    if hair[i] in dna_string:
        suspect.append(i)
for i in eye:
    if eye[i] in dna_string:
        suspect.append(i)
for i in facial:
    if facial[i] in dna_string:
        suspect.append(i)


for p in people:
    if people[p] == suspect:
        print("the suspect is: " + str(p))
        break

















