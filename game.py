from graphics import *
import random
import time
def main():
    win = GraphWin(("Game"), 1000, 800)
    win.setBackground(color_rgb(101, 67, 33))
    points = 0
    t = Text(Point(500, 200), "Square CLicker")
    t2 = Text(Point(500, 250), "Click On The Squares As Soon As They Appear")
    t3 = Text(Point(500, 325), "Click Here To Start")
    t3.setSize(20)
    t2.setSize(20)
    t.setSize(20)
    t.draw(win)
    t2.draw(win)
    start = Rectangle(Point(350, 300), Point(650, 350))
    start.setOutline("red")
    start.setFill("red")
    start.draw(win)
    t3.draw(win)
    start_click = win.getMouse()
    start_click_x = start_click.getX()
    start_click_y = start_click.getY()
    if(start_click_x >= 350 and start_click_x <= 650 and start_click_y >= 300 and start_click_y <= 350):
        start.undraw()
        t.undraw()
        t2.undraw()
        t3.undraw()
        t0 = time.time()
        square1 = Rectangle(Point(50, 50), Point(75,75))
        square1.setOutline("black")
        square1.setFill("pink")
        square1.draw(win)
        for i in range(1, 21):
            dx = random.randint(50, 950)
            dy = random.randint(50, 750)
            if(i == 1):
                square1.move(dx, dy)
            else:
                square1.move(dx - center_X, dy - center_Y)
                pass
            play_click = win.getMouse()
            play_click_x = play_click.getX()
            play_click_y = play_click.getY()
            center_X = square1.getCenter().getX()
            center_Y = square1.getCenter().getY()
            if(play_click_x <= center_X + 12.5 and play_click_x >= center_X - 12.5 and play_click_y <= center_Y + 12.5 and play_click_y >= center_Y - 12.5):
                points += 1
        square1.undraw()
        t1 = time.time()
        accu = (points/20) * 100
        round(accu, 0)
        tfinal = round(t1-t0, 2)
        time_result_data = Text(Point(450, 200), tfinal)
        time_result_data.setSize(20)
        time_result = Text(Point(560, 200), "Seconds!")
        time_result.setSize(20)
        final_score_data = Text(Point(450, 250), accu)
        final_score_data.setSize(20)
        final_score = Text(Point(560, 250), "% Accuracy")
        final_score.setSize(20)
        time_result_data.draw(win)
        final_score_data.draw(win)
        time_result.draw(win)
        final_score.draw(win)

    win.getMouse()
    win.close()
main()