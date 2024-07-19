from testing import Testing
from inputs import get_list_of_recovered_patients
from utils.config import Config

if __name__ == '__main__':

    # time complexity = O(1)
    # space complexity = O(1)
    patients = get_list_of_recovered_patients()

    # time complexity = O(1)
    # space complexity = O(1)
    config = Config()
    
    # time complexity = O(1)
    # space complexity = O(1)
    testing = Testing(patients, config.get_batch_size(), config.get_datetime_format(), config.get_random_seed())
    
    # time complexity = O(n/k)
    # space complexity = O(n/k) where n is number of recovered patients and k in batch size
    chosen_patients = testing.choose_patients()

    print(chosen_patients)


# overall time complexity = O(n/k)
# overall space complexity = O(n/k)