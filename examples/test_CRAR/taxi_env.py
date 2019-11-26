""" wrapper for the taxi environment to provide compatibility with crar/deer framework"""

import numpy as np

from deer.base_classes import Environment

from gym_taxi.envs.taxi_env import JsonTaxiEnv

class MyEnv(Environment):
    VALIDATION_MODE = 0

    def __init__(self, rng, **kwargs):
        self.env = JsonTaxiEnv("screen","original",rewards={"base": 0, "failed-action": 0, "drop-off": 1})
        self.done = False
        self.env.seed(rng)

    def reset(self, mode): 
        self.obs = self.env.reset()
        return [self.env.observation_space.converter(self.obs)]

    def act(self, action):
        obs,reward,done,info = self.env.step(action)
        self.obs = obs
        self.done = done
        return reward

    def summarizePerformance(self, test_data_set, learning_algo, *args, **kwargs):
        pass

    def inputDimensions(self):
        c,h,w= self.env.observation_space.image.shape
        return [(1,c,h,w)]
        # if(self._higher_dim_obs==True):
        #     return [(1,self._size_maze*6,self._size_maze*6)]
        # else:
        #     return [(1,self._size_maze,self._size_maze)]

    def observationType(self, subject):
        return np.uint8

    def nActions(self):
        return self.env.action_space.n

    def observe(self):
        return [self.env.observation_space.converter(self.obs)]
        # obs=copy.deepcopy(self._map)
                
        # obs[self._pos_agent[0],self._pos_agent[1]]=0.5                
        # if(self._higher_dim_obs==True):
        #     "self._pos_agent"
        #     self._pos_agent
        #     obs=self.get_higher_dim_obs([self._pos_agent],[self._pos_goal])
            
        # return [obs]
    
    def get_higher_dim_obs(self,indices_agent,indices_reward): #called from observe
        pass

    def inTerminalState(self):
        return self.done

    def render(self):
        return self.env.render()