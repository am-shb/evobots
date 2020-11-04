from environment import ENVIRONMENT

class ENVIRONMENTS:
    def __init__(self, numEnvs):
        self.envs = {}
        for e in range(numEnvs):
            self.envs[e] = ENVIRONMENT(e)