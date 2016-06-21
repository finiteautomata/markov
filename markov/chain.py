class Chain:
    """ This class models a concrete instance of a Markov Process

    It is created with an initial state, and then following calls to transition will create the chain.

    It can be created deterministically: you can create it with an initial state, and then succesively call transition(new_state) to create the

    > model = markov.Model(state_labels=["a", "b", "c"])
    > markov.Chain(markovmodel, "a")
    > markov.move_to("b")
    > markov.move_to("c")
    > markov.states
    > > ["a", "b", "c"]
    ''
    """


    def __init__(self, model, initial_state=None):
        self._model = model
        self._states = []

        if initial_state:
            self._states.append(initial_state)


    @property
    def states(self):
        return self._states

    @property
    def current_state(self):
        if len(self._states) > 0:
            return self.states[-1]
        else:
            return None

    def move_to(self, state):
        """
        Move deterministically to a new state
        """

        self._states.append(state)

    def move(self, times=1):
        """
        Move stochastically to a new state
        """
        for _ in range(times):
            current_state = self.current_state
            if current_state:
                self._states.append(self._model.random_state_from(current_state))
            else:
                self._states.append(self._model.random_initial_state())

        return self

    def __repr__(self):
        return ", ".join(self._states)