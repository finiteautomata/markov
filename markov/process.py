class Process:
    def __init__(self,
        transition_matrix,
        initial_probabilities,
        state_labels=None):
        self.transition_matrix = transition_matrix
        self.initial_probabilities = initial_probabilities

        self.create_state_labels(state_labels)

    def create_state_labels(self, state_labels):
        no_states = self.transition_matrix.shape[0]

        if state_labels:
            if len(state_labels) != no_states:
                raise TypeError("Number of labels not equal to number of states")
            self.state_labels = state_labels
        else:
            self.state_labels = list(range(no_states))

