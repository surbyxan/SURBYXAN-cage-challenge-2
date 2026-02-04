from CybORG.Shared import Results
from CybORG.Shared.Actions import Sleep, Remove
from CybORG.Agents.SimpleAgents.BaseAgent import BaseAgent

class HeuristicBlue(BaseAgent):

    def __init__(self):
        pass

    def train(self, results):
        pass

    def get_action(self, observation, action_space):
        return Remove(session=0, agent='Blue', hostname='Enterprise2')

    def end_episode(self):
        pass

    def set_initial_values(self, action_space, observation):
        pass