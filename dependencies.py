import turtle


country_initials = [
    {"Central African Republic" : "CAR"},
    {"Sao Tome and Principe": "STP"},
    {"Seychelles": "S"},
    {"Equatorial Guinea": "EG"},
    {"Burkina Faso": "BF"},
    {"Congo Republic" : "CR"},
    {"Democratic Republic of Congo" : "DRC"},
    {"Sierra Leone": "SL"},
    {"Ivory Coast" : "IV"},
    {"Mauritius" : "M"},
    {"Gambia" : "G"},
    {"Guinea Bissau" : "GB"},
    {"El Salvador" : "EL"},
    {"Guatemala" : "G"},
    {"Costa Rica" : "CR"},
    {"Jamaica" : "J"},
    {"Haiti" : "H"},
    {"Albania" : "Alb"},
    {"Andorra" : "And"},
    {"Bosnia-Herzegovina" : "BH"},
    {"Liechtenstein" : "Lie"},
    {"Luxembourg" : "Lux"},
    {"Montenegro" : "MO"},
    {"North Macedonia" : "NM"},
    {"San Marino" : "SM"},
    {"Vatican City" : "VC"},
    {"Switzerland" : "Swi"},
    {"Slovenia" : "Slo"},
    {"Armenia" : "Ar"},
    {"Azerbaijan" : "Az"},
    {"Saudi Arabia" : "Saudi A"},
    {"Wallis and Futuna" : "W-F"},
    {"Tahiti": "T"}
] 


class Functions(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def create(self,country_name, posx, pos_y):
        """Creates a turtle and writes the country name at the real-world country location using the x and y coordinates"""
        self.goto(posx, pos_y)
        self.write(arg=f"*{country_name}", move=True, align="center", font=("Century Gothic", 8, "bold"))
        
    
    def rename(self, text_input):
        """This function replaces country name with initials if country is in the country_initials list"""
        for country in country_initials:
            for (key, value) in country.items():
                if key == text_input:
                    return value

                    
    def abbreviations(self, text, posx, pos_y):
        """This function checks if a country is in the country initials list and then prints the initials and full name at the side of the screen"""  
        for country in country_initials:
            for (key, value) in country.items():
                if key == text:
                    self.goto(posx, pos_y)
                    self.write(arg=f"{value} - {key}", move=True, align="left", font=("Century Gothic", 8, "bold"))


    def unlisted_countries(self, country, pos_x, pos_y):
        """This prints all the countries in the unlisted list"""
        self.goto(pos_x, pos_y)
        self.color('red')
        self.write(arg=f"*{country}", move=True, align="center", font=("Century Gothic", 8, "bold"))
