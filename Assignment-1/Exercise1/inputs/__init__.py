from .get_inputs import Inputs

inputs = Inputs()

def get_your_calendar():
    return inputs.get_your_calendar()

def get_your_working_hours():
    return inputs.get_your_working_hours()

def get_your_co_workers_calendar():
    return inputs.get_your_co_workers_calendar()

def get_your_co_workers_working_hours():
    return inputs.get_your_co_workers_working_hours()

def get_meeting_duration():
    return inputs.get_meeting_duration()