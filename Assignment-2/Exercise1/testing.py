from random import seed, randint
from datetime import date

class Testing:

    def __init__(self, recovered_patients, batch_size, datetime_format, random_seed):
        self.recovered_patients = recovered_patients
        self.batch_size = batch_size
        self.datetime_format = datetime_format
        seed(random_seed)

    def choose_patients(self):
        # time complexity = O(n/k) where n is number of recovered patients and k in batch size
        # space complexity = O(n/k)
        chosen_patients = [self._select_patient_from_batch(i, i + self.batch_size - 1) for i in range(0, len(self.recovered_patients), self.batch_size)]

        # time complexity = O(n/k)
        # space complexity = O(n/k)
        return [self.recovered_patients[patient] for patient in chosen_patients]

    def _test_date_logger(func):
        def magic_func(self, start, end):
            print(date.today().strftime(format=self.datetime_format))
            return func(self, start, end)
        return magic_func
    
    @_test_date_logger
    def _select_patient_from_batch(self, start, end):
        return randint(start, end)




    # ANOTHER SOLUTION
    # def choose_patients(self):
    #     number_of_patients_to_choose = (int(len(self.recovered_patients) / self.batch_size)) if (len(self.recovered_patients) % self.batch_size == 0) else (int(len(self.recovered_patients) / self.batch_size) + 1)
    #     chosen_patients = self._select_random_patients(number_of_patients_to_choose)
          # time complexity = O(n/k)
          # space complexity = O(n/k)
    #     return [self.recovered_patients[patient] for patient in chosen_patients]
    
    # def _test_date_logger(func):
    #     def magic_func(self, n):
    #         print(date.today().strftime(format=self.datetime_format))
    #         return func(self, n)
    #     return magic_func

    # @_test_date_logger
    # def _select_random_patients(self, n):
          # time complexity = O(n/k) where n is number of recovered patients and k in batch size
          # space complexity = O(n/k)
    #     return [randint(0, len(self.recovered_patients)-1) for _ in range(n)]

    # BOTH METHODS ARE GIVING SAME TIME AND SPACE COMPLEXITY