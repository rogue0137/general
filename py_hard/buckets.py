#!/usr/bin/python2.7
def the_bucket_challenge(bucket_one,bucket_two,goal,starting=(0,0)):
    """This is the DieHard 3 Water Jug Problem, also known as the classic Water
    Pouring Problem."""
    
    if goal in starting:
        #print(starting)
        return [starting]
    explored = set() #set of states we have visited
    frontier = [[starting]] #ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x,y) = path[-1] #Last state in the first path of the frontier
        for (state, action) in successors (x,y,bucket_one,bucket_two).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action,state]
                #print(path2)
                if goal in state:
                    print(path2)
                    return path2
                else:
                    frontier.append(path2)
    
    return Fail 
    
Fail = []


def successors(x,y,bucket_one,bucket_two):
    """Return a dict of {state:action} pairs describing what can be reached from
    the (x,y) state, and how."""
    #x = level of bucket one
    #y = level of bucket two
    assert x <= bucket_one and y <= bucket_two 
    return {((0,y+x) if y+x<=bucket_two else (x-(bucket_two-y), y+(bucket_two-y))): 'pour bucket one into bucket two',
            ((x+y, 0) if x+y<=bucket_one else (x+(bucket_one-x), y-(bucket_one-x))): 'pour bucket two into bucket one',
            (bucket_one,y): 'fill bucket one with ' + str(bucket_one) + ' gallons' , (x,bucket_two):'fill bucket two with ' + str(bucket_two) + ' gallons',
            (0,y): 'empty bucket one', (x,0):'empty bucket two'}


solution = the_bucket_challenge(5,3,4)

if solution != Fail:
    print('Solution found.')
else:
    print('No solution possible.')
    
#the_bucket_challenge(0,1,0)
