class Process:
    # Creates a Markov Process with transition_matrix
    # transition_matrix must be a rectangular matrix of nxn
    # initial_probabilities must be an array of length n
    # Optional arguments:
    #   - state_labels:
    def __init__(self,
        transition_matrix,
        initial_probabilities,
        state_labels=None):
        self._transition_matrix = transition_matrix
        self._initial_probabilities = initial_probabilities

        self.__create_state_labels__(state_labels)

    def __create_state_labels__(self, state_labels):
        no_states = self._transition_matrix.shape[0]

        if state_labels:
            if len(state_labels) != no_states:
                raise TypeError("Number of labels not equal to number of states")
            state_labels = state_labels
        else:
            state_labels = range(no_states)

        self._label_to_position = dict(zip(state_labels, range(no_states)))

    @property
    def state_labels(self):
        return self._label_to_position.keys()

    def initial_probability(self, label):
        pos = self._label_to_position[label]

        return self._initial_probabilities[pos]

    # Returns the transition probability from 'origin' label to 'to' label
    def transition_probability(self, origin, to):
        from_label, to_label = self._label_to_position[origin], self._label_to_position[to]

        return self._transition_matrix[from_label, to_label]


