from __future__ import print_function
from __future__ import division

import logging
import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)

class Swing(gym.Env):
    metadata = {"render.modes": ["human", "rgb_array"],
                "video.frames_per)second": 50
    }

    def __init__(self):
        # define const
        self.g = 9.8
        self.m1 = 0.1
        self.m2 = 0.2
        # self.m3 = 0.2
        self.l_12 = 0.1
        # self.l_13 = 0.1
        self.torque_mag = 10
        self.dt = 0.02 # update frequency is set to 50Hz

        high = np.array([np.finfo(np.float32).max, np.finfo(np.float32).max])
        
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(-high, high)

        self._seed()
        self.viewer = None
        self.state = None

        self.state_beyond_done = None
        
        return
    
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def _step(self, action):
        assert self.action_space.contains(action),"%r (%s) invalid"%(action, type(action))
        
        return
    def _reset(self):
        return
    def _render(self, mode="human", close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        # parameters
        screen_width = 500
        screen_height = 500
        
        world_width = 2 * x_threshold
        scale = screen_width / world_width
        head_dim = 40
        torso_x = 30
        torso_y = 100
        thigh_x = 60
        thigh_y = 30
        thigh_joint_dim = 30
        leg_x = 30
        leg_y = 60
        axle_dim = 20
        swing_y = 150
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viwer(screen_width, screen_height)
            self.viwer.set_bounds(-2.2, 2.2, -2.2, 2.2)

            # swing
            
            # axle of the swing
            self.axle = rendering.make_circle(axle_dim / 2)
            self.axle.set_color(0, 0, 0)
            self.viewer.add_geom(self.axle)
            
