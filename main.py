import turtle
import pandas
from dependencies import Functions


def know_the_world():


    country_class = Functions()
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.title("KNOW THE WORLD")
    image = './background_images/world.gif' 
    screen.addshape(image)
    turtle.shape(image)

    continents = {"Africa" : [-353, -76], "Americas": [120, 179], "Asia":[-316, -255], "Europe": [-406, 247], "Oceania": [350, -180]}
    
    valid_choice = False
    
    while valid_choice != True:
    
        user_choice = screen.textinput("Choose a Continent", "Which continent do you wish to test your knowledge on: Africa, Americas, Europe, Asia or Oceania").title()
    
        for (key, value) in continents.items():
            if key == user_choice:
                image = f'./background_images/{user_choice}.gif' 
                screen.addshape(image)
                turtle.shape(image)
                data = pandas.read_csv(f"./csv_files/{user_choice}.csv")
                abbr_x = value[0]
                abbr_y = value[1]
                valid_choice = True
    
    
    countries = data.Country
    
    guessed_countries = []
    
    score = 0
    
    gameover = False
    
    
    while gameover != True:
    
        guess = screen.textinput(f"Guessed {score} Countries out of a possible {len(countries)}", "Enter the name of the country. Don't forget to type 'Exit' if you've exhausted your knowledge.").title()
    
        if guess in countries.tolist() and guess not in guessed_countries:
            guessed_countries.append(guess)
            score += 1

            country_data = data[data.Country == guess]
            x_pos = int(country_data.x)
            y_pos = int(country_data.y)
            name = country_class.rename(guess)

            if name is None:
                name = guess
            else:
                country_class.abbreviations(guess, abbr_x, abbr_y)
                abbr_y -= 13
    
            country_class.create(name, x_pos, y_pos)
    
        if guess == "Exit":
            unlisted_countries = [country for country in countries if country not in guessed_countries]
    
            for country in unlisted_countries:
                country_data = data[data.Country == country]
                x_pos = int(country_data.x)
                y_pos = int(country_data.y)
                name = country_class.rename(country)

                if name is None:
                    country_class.unlisted_countries(country, x_pos, y_pos)
                else:
                    country_class.unlisted_countries(name, x_pos, y_pos)
                    country_class.abbreviations(country, abbr_x, abbr_y)
                    abbr_y -= 13
    
            gameover = True

    replay = screen.textinput("Try Again", "Do you want to try again? Type 'y' or 'n'").title()    

    if replay == "Y":
        screen.clearscreen()
        know_the_world()
        
    screen.mainloop()


know_the_world()
