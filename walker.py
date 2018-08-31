#!/usr/bin/env python

import sys, random, time, noise

class Walker:
    def get_random_direction(self, x, y, w, h):
        delta = time.time() - self.last_time    
        self.p_time += delta
        rng = noise.pnoise3(x, y, self.p_time)
        
        print rng

        if rng < -0.5 and y != 0: 
            y -= 1
        elif rng < 0.0 and y != h-1: 
            y += 1
        elif rng < 0.5 and x != 0: 
            x -= 1
        elif rng < 1.0 and x != w-1: 
            x += 1

        return x, y

    def get_random_float_direction(self, last_dir, x, y, w, h):
        dirs = {'n': 0, 's': 0, 'e': 0, 'w': 0} # weights
        dirs[last_dir] = 3 # slighty higher chance of keeping going in the same direction

        high = 0
        direction = 'n'

        for dir, weight in dirs.items():
            val = random.randint(weight, len(dirs) +1)
            random.gauss(320, 60)
            if val > high:
                high = val
                direction = dir
        
        if direction == 'n' and y != 0: 
            y -= 1
        elif direction == 's' and y != h-1: 
            y += 1
        elif direction == 'e' and x != 0: 
            x -= 1
        elif direction == 'w' and x != w-1: 
            x += 1
        

        return x, y, direction

    def __init__(self):
        self.ground = "#"
        self.walker = "@"

        self.w,self.h = 10,10
        self.area = [[self.ground for y in range(self.w)] for x in range(self.h)]

        self.x_pos = random.randint(0, self.w-1)
        self.y_pos = random.randint(0, self.h-1)
        self.p_time = float(0)
        self.last_time = time.time()
        print self.x_pos, self.y_pos
        self.area[self.x_pos][self.y_pos] = self.walker

        while True:
            for y in range(0, len(self.area)):
                for x in range(0, len(self.area[x])):
                    sys.__stdout__.write(self.area[y][x])
                print ''
            self.area[self.x_pos][self.y_pos] = self.ground
            self.x_pos, self.y_pos = self.get_random_direction(self.x_pos, self.y_pos, self.w, self.h)    
            self.area[self.x_pos][self.y_pos] = self.walker
            time.sleep(0.5)
            print ''


if __name__ == "__main__":
    walker = Walker()


        

