from gym import spaces
class MountainCarWrapper:
    def __init__(self, env): 
        self._action_space = spaces.Discrete(2)
        self._env = env
        
    @property
    def observation_space(self):
        return self._env.observation_space
        
    @property
    def action_space(self):
        return self._action_space
        
    def reset(self):
        return self._env.reset()
    
    def step(self, action):
        if (action == 1):
            action = 2
        return self._env.step(action)
    
    def render(self):
        return self._env.render()