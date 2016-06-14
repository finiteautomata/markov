from process import Process
import numpy as np
import unittest

class ProcessTest(unittest.TestCase):
    def test_creating_a_process_with_one_state(self):
        transition_matrix = np.matrix([0.5])
        initial_probabilities = np.array([1.0])

        process = Process(transition_matrix, initial_probabilities)

        self.assertEqual(process.state_labels, [0])

if __name__ == '__main__':
    unittest.main()