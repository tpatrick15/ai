def simplereflexagent():
    """
    Siple implementation of a simple reflex agent.
    Note that those agents select actions based solely on the current percept. They do not/ cannot take into consideration history or even weigh the consequences of the actions they will take
    """
    def __init__(self, rules):
        """
        Initialize the agent with a set of rules.

        :param rules: A dictionary mapping percepts to actions.
        """
        self.rules = rules

    def perceive(self, percept):
        """
        Given a percept, return the corresponding action based on the rules.

        :param percept: The current percept from the environment.
        :return: The action to be taken or None if no rule matches.
        """
        return self.rules.get(percept, None)
