import copy
import random
class Hat:
    #taking the arguements as dictionary
    def __init__(self,**colors):
        self.coldict=colors
        self.contents=list()
        for key, value in colors.items():
            colour=key
            colourcount=colors[key]
            for k in range(colourcount):
                self.contents.append(colour)
        #print(self.contents)

    def draw(self,ndrawn):
        if ndrawn>len(self.contents):
            return self.contents
        else:
            self.new=random.sample(self.contents,ndrawn)

            for l in self.new:
                ind=self.contents.index(l)
                self.contents.pop(ind)
            return self.new
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    hat=copy.copy(hat)


    expected_balls=expected_balls


    num_balls_drawn=num_balls_drawn
    num_experiments=num_experiments
    m=0
    for k in range(num_experiments):
        if num_balls_drawn>len(hat.contents):
            result=hat.contents

        else:
            hat.new=random.sample(hat.contents,num_balls_drawn)
            result=hat.new


        y=0
        for k,v in expected_balls.items():
            colour=k
            colourcount=v

            if (result.count(colour)>=colourcount):
                y=y+1
        if(y==len(expected_balls.items())):
            m=m+1
    prob=m/num_experiments
    return prob


hat=Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability=experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)
