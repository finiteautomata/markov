from markov.model import Model
import numpy as np
import unittest

class ModelTest(unittest.TestCase):
    def test_creating_a_Model_with_one_state_creates_default_labels(self):
        transition_matrix = np.matrix([0.5])
        initial_probabilities = np.array([1.0])

        model = Model(transition_matrix, initial_probabilities)

        # Beware that assertCountEqual is 'assertItemsEqual'
        self.assertCountEqual(model.state_labels, [0])

    def test_creating_Model_with_labels(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])

        model = Model(transition_matrix, initial_probabilities, state_labels=["a", "b"])

        self.assertCountEqual(model.state_labels, ["a", "b"])


    def test_returning_initial_probability(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])

        model = Model(transition_matrix, initial_probabilities, state_labels=["a", "b"])

        self.assertEqual(model.initial_probability("a"), 0.4)


    def test_returning_transition_probability(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])

        model = Model(transition_matrix, initial_probabilities, state_labels=["a", "b"])

        self.assertEqual(model.transition_probability("b", "a"), 0.25)


if __name__ == '__main__':
    unittest.main()