 #define the base class player
class player:
  def play(self):
    print("the player is playing cricket...")

#define the derived class Batsman
class Batsman(player):
  def play(self):
    print("the Batsman is batting...")

#define the derived clas Bowler
class Bowler(player):
  def play(self):
    print("the Bowler is bowling...")


#define derived class catcher
class catcher(player):
  def play(self):
    print("the catcher is catching the ball...")
    
#create objects of Batsmanand Bowler classes
batsman=Batsman()
bowler=Bowler()
catcher=catcher()
#call the play() method for each obeject
batsman.play()
bowler.play()
catcher.play()