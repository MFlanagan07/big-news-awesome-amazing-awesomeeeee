pts = 0
pts = int(pts)
life = 3
play = True
answers = []
countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ]
while play == True:
    ans = input("enter a country in africa ")
    if ans in answers:
        print("already said try again")
    elif ans in countries:
        pts += 1
        print("Correct")
        print(pts, "points")
        answers.append(ans)
    elif ans != countries:
        life -= 1
        print("incorrect, guess again")
        print("you have",life,"guesses left")
    if life == 0:
        play == False
        print("you lose")
        break
    if pts == 54:
        play == False
        print("you win nerd")
        break

        
        