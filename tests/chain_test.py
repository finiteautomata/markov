from markov import Model, Chain
import numpy as np
import unittest

class ChainTest(unittest.TestCase):
    def setUp(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])
        self.model = Model(transition_matrix, initial_probabilities, state_labels=["a", "b"])

    def test_an_empty_chain_has_no_states(self):
        chain = Chain(self.model)

        self.assertEqual(chain.states, [])

    def test_creating_chain_with_initial_state(self):
        chain = Chain(self.model, "a")

        self.assertEqual(chain.states, ["a"])

    def test_moving_to_specific_state_from_empty(self):
        chain = Chain(self.model)

        chain.move_to("a")

        self.assertEqual(chain.states, ["a"])

    def test_moving_stochastically_adds_new_state(self):
        chain = Chain(self.model)

        chain.move()

        self.assertEqual(len(chain.states), 1)


if __name__ == '__main__':
    unittest.main()