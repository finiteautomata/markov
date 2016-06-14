from process import Process
import numpy as np
import unittest

class ProcessTest(unittest.TestCase):
    def test_creating_a_process_with_one_state_creates_default_labels(self):
        transition_matrix = np.matrix([0.5])
        initial_probabilities = np.array([1.0])

        process = Process(transition_matrix, initial_probabilities)

        # Beware that assertCountEqual is 'assertItemsEqual'
        self.assertCountEqual(process.state_labels, [0])

    def test_creating_process_with_labels(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])

        process = Process(transition_matrix, initial_probabilities, state_labels=["a", "b"])

        self.assertCountEqual(process.state_labels, ["a", "b"])



    def test_returning_initial_probability(self):
        transition_matrix = np.matrix([[0.5, 0.5], [0.25, 0.75]])
        initial_probabilities = np.array([0.4, 0.6])

        process = Process(transition_matrix, initial_probabilities, state_labels=["a", "b"])

        self.assertEqual(process.initial_probability("a"), 0.4)




if __name__ == '__main__':
    unittest.main()