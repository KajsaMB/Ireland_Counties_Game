import turtle as t
import pandas
import time

screen = t.Screen()
screen.title("Ireland Counties Game")
image = "ireland_blank_counties.gif"
screen.addshape(image)
states = t.shape(image)
screen.tracer(0)

# Used for initial set up. To map correct name to county.
# def get_mouse_click_coor(x, y):
#      print(x, y)

# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()

data = pandas.read_csv("ireland_counties.csv")
all_counties = data.county.to_list()

correct_counties = 0
guessed_counties = []

time.sleep(0.1)
screen.update()
while len(guessed_counties) < 27:
    answer_county = screen.textinput(title=f"{correct_counties}/27 Guess the County", prompt="Write the name of a county").title()
    if answer_county == "Exit":
        missed_counties = [county for county in all_counties if county not in guessed_counties]
        new_data = pandas.DataFrame(missed_counties)
        new_data.to_csv("counties_to_learn.csv")
        break
    if answer_county in all_counties and answer_county not in guessed_counties:
        correct_counties += 1
        new_t = t.Turtle()
        new_t.hideturtle()
        new_t.penup()
        county_data = data[data.county == answer_county]
        new_t.goto(int(county_data.x), int(county_data.y))
        new_t.write(answer_county)
        guessed_counties.append(answer_county)


screen.exitonclick()
