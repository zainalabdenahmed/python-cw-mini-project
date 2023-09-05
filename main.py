def padel_court_cost(court_type):
    if court_type == ("Indoor"):
        return 30
    if court_type == ("outdoor"):
         return 20 

def rackets_cost(racket_briand):
    if racket_briand == ("bullpadel"):
        return 100
    if racket_briand == ("nox"):
        return 140
    if racket_briand == ("slux"):
         return 200
    
def padel_ball_cost(ball_boxes):    
    if ball_boxes == 1 :
       return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
def padel_game_cost():
    court_type = input("indoor / outdoor: ")
    rackets_brand = input("bullpadel / nox / siux")
    ball_boxes = input("1 /2 /3 balls :")
    print = padel_court_cost(court_type) + rackets_cost(rackets_brand) + padel_ball_cost(ball_boxes)
    return print

print(padel_game_cost())