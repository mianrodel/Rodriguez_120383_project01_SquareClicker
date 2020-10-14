# from graphics import *
# import random
# import time
from gameClass import GAMECLASS

# def game_window_creation():
#     win = GraphWin(("Game"), 1000, 750)
#     win.setBackground(color_rgb(101, 67, 33))
#     t = Text(Point(500, 200), "Square CLicker")
#     t2 = Text(Point(500, 250), "Click On The Squares As Soon As They Appear, DONT CLICK ON BLACK")
#     t3 = Text(Point(500, 325), "Click Here To Start")
#     t3.setSize(20)
#     t2.setSize(20)
#     t.setSize(20)
#     t.draw(win)
#     t2.draw(win)
#     start = Rectangle(Point(350, 300), Point(650, 350))
#     start.setOutline("red")
#     start.setFill("red")
#     start.draw(win)
#     t3.draw(win)
#     return win, t, t2, t3, start
# #END OF game_window_creation()

# def get_Click(win):
#     user_click = win.getMouse()
#     user_click_x = user_click.getX()
#     user_click_y = user_click.getY()
#     return user_click_x, user_click_y
# #END OF get_Click()

# def start_or_null(x, y, win, t, t2, t3, start):
#     if(x >= 350 and x <= 650 and y >= 300 and y <= 350):
#         start.undraw()
#         t.undraw()
#         t2.undraw()
#         t3.undraw()
#         game_start(win)
# #END OF start_or_null()

# def game_start(win):
#     t0 = time.time()
#     points = 0
#     square1 = Rectangle(Point(50, 50), Point(75,75))
#     square1.setOutline("black")
#     square1.setFill("pink")
#     square1.draw(win)
#     square2 = Rectangle(Point(50, 50), Point(75,75))
#     square2.setOutline("black")
#     square2.setFill("Black")
#     square2.draw(win)
#     for i in range(1, 21):
#         dx = random.randint(50, 950)
#         dy = random.randint(50, 750)
#         dx_Trap = random.randint(50, 950)
#         dy_Trap = random.randint(50, 750)
#         if(i == 1):
#             square1.move(dx, dy)
#             square2.move(dx_Trap, dy_Trap)
#         else:
#             square1.move(dx - center_X, dy - center_Y)
#             square2.move(dx_Trap - center_trap_x, dy_Trap - center_trap_y)
#             pass
#         #FUNCTION OF USED TO GET CLICK
#         play_click_x, play_click_y = get_Click(win)
#         center_X = square1.getCenter().getX()
#         center_Y = square1.getCenter().getY()
#         center_trap_x = square2.getCenter().getX()
#         center_trap_y = square2.getCenter().getY()
#         if(play_click_x <= center_X + 12.5 and play_click_x >= center_X - 12.5 and play_click_y <= center_Y + 12.5 and play_click_y >= center_Y - 12.5):
#             points += 1
#         if(play_click_x <= center_trap_x + 12.5 and play_click_x >= center_trap_x - 12.5 and play_click_y <= center_trap_y + 12.5 and play_click_y >= center_trap_y - 12.5):
#             points -= 1
#     square1.undraw()
#     square2.undraw()
#     t1 = time.time()
#     data_claculate_print(points, t0, t1, win)
# #END OF game_start()

# def data_claculate_print(points, t0, t1, win):
#     accu = (points/20) * 100
#     round(accu, 0)
#     tfinal = round(t1-t0, 2)
#     time_result_data = Text(Point(450, 200), tfinal)
#     time_result_data.setSize(20)
#     time_result = Text(Point(560, 200), "Seconds!")
#     time_result.setSize(20)
#     final_score_data = Text(Point(450, 250), accu)
#     final_score_data.setSize(20)
#     final_score = Text(Point(560, 250), "% Accuracy")
#     final_score.setSize(20)
#     point_display = Text(Point(560, 400), points)
#     point_display.setSize(20)
#     point_display_text = Text(Point(450, 400), "Points: ")
#     point_display_text.setSize(20)

#     time_result_data.draw(win)
#     final_score_data.draw(win)
#     time_result.draw(win)
#     final_score.draw(win)
#     point_display.draw(win)
#     point_display_text.draw(win)
#     score = points + accu
#     rankings(score, win)
# #END OF data_claculate_print()

# def rankings(score, win):
#     file_object = open('Rankings.txt')
#     content = file_object.readlines() 
#     place = 0
#     for line in content: 
#         for i in line:
#             if i != '\n':
#                 if int(i) < score: 
#                     place = int(i) + 1
#                     break 
#     Leaderboard_text = Text(Point(450, 300), "You placed: ")
#     Leaderboard_text.setSize(20)
#     Leaderboard = Text(Point(560, 300), place)
#     Leaderboard.setSize(20)
#     Leaderboard_text.draw(win)
#     Leaderboard.draw(win)
#     file_object.close()
# #END OF rankings

def main():
    # win, t, t2, t3, start = game_window_creation()
    # x_click, y_click = get_Click(win)
    # start_or_null(x_click, y_click, win, t, t2, t3, start)
    g1 = GAMECLASS()
    
    g1.run_game()
    # win.getMouse()
    # win.close()
main()