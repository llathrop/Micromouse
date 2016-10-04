import numpy as np

class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [0, 0]
        self.heading = 'up'
        self.maze_dim = maze_dim
        self.last_movement = 0
        self.last_rotation = 0
        self.last_sensors = [0,1,0]
        self.last_heading =  self.heading
        self.goal = [self.maze_dim[0]/2,self.maze_dim[1]/2]
        
    def update_state(self,sensors,rotation,movement):
        possible_headings = ['left','up','right','down']
        possible_rotation = [-90,0,90]
        print possible_headings
        
        self.last_movement = movement
        self.last_rotation = rotation
        self.last_sensors = sensors
        self.last_heading = self.heading
        
        last_heading=possible_headings.index(self.last_heading)
        heading_rotation=(possible_rotation.index(rotation) -1)
        new_heading=(last_heading+heading_rotation)%3
        self.heading = possible_headings[new_heading]   # this is pointing wrong somehow. FIXXXXX
        
    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        
        #Sense
        print 'sensors', sensors
        
        #Locate
        
        #Map
        
        #take action:        
        rotation = 0
        movement = 0
        
        if sensors[0]>0:
            rotation=-90
        if sensors[1]>0:
            rotation=0
        if sensors[2]>0:
            rotation=90
        if sensors==[0, 0, 0]:
            rotation=90
        
        movement = 1
        
        self.update_state(sensors,rotation,movement)
        print "rotation:",rotation,"movement:",movement, "heading",self.heading
        
        return rotation, movement