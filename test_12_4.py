import unittest
import logging
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
#    is_frozen = False

#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_ = rt_with_exceptions.Runner('Ivan', -2)
            for i in range(10):
                 runner_.walk()
            self.assertEqual(runner_.distance, 50)
            logging.info('test_walk выполнен нормально')
        except Exception as e:
            logging.warning('Неверная скорость для Runner')
#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_ran(self):
        try:
            runner_ = rt_with_exceptions.Runner(10)
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('test_ran выполнен нормально')
        except Exception as e:
            logging.warning('Неверный тип данных для объекта Runner')
#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = rt_with_exceptions.Runner('Ivan1')
        runner_2 = rt_with_exceptions.Runner('Ivan2')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)




class TournamentTest(unittest.TestCase):
#    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
         self.runner_1 = rt_with_exceptions.Runner('Усэйн', 10)
         self.runner_2 = rt_with_exceptions.Runner('Андрей', 9)
         self.runner_3 = rt_with_exceptions.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            temp_dict = {}
            for j in cls.all_results[i]:
                temp_dict[j] = str(cls.all_results[i][j])
            print(temp_dict)


#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tournament1 = rt_with_exceptions.Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tournament1.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1].keys())] == 'Ник')
#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tournament2 = rt_with_exceptions.Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tournament2.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2].keys())] == 'Ник')
#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tournament3 = rt_with_exceptions.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = tournament3.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == 'Ник')


if __name__ == "__main__":
    logging.basicConfig(level='INFO', filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()