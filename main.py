import turtle
import pandas

FONT = ("Comic Sans", 8, "bold")

screen = turtle.Screen()
screen.title('U.S Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=725, height=491)
screen.tracer(0)
turtle.shape(image)

user_states = []
data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
missed_states = []



still_working = True
while still_working:
    screen.update()
    answer_state = screen.textinput(title=f'{len(user_states)}/50 States Correct', prompt="What's another state's name?").title()
    if len(user_states) == 50 or answer_state == 'Exit':
        for miss_state in all_states:
            if miss_state not in user_states:
                missed_states.append(miss_state)

        missed_states_data = {
            'missed states': missed_states
        }
        df = pandas.DataFrame(missed_states_data)
        df.to_csv('missed_states.csv')
        still_working = False


    if answer_state in all_states:
        state_check = data[data.state == answer_state]
        state_coordinates = (int(state_check.x), int(state_check.y))
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(state_coordinates)
        state.write(answer_state, align='left', font=FONT)
        user_states.append(answer_state)





