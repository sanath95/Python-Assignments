class Inputs:
    def __init__(self):
        self.YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
        self.YourWorkingHours = ['9:00', '20:00']
        self.YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
        self.YourCoWorkersWorkingHours = ['10:00', '18:30']
        self.meetingDuration = 30

    def get_your_calendar(self):
        return self.YourCalendar
    
    def get_your_working_hours(self):
        return self.YourWorkingHours
    
    def get_your_co_workers_calendar(self):
        return self.YourCoWorkersCalendar
    
    def get_your_co_workers_working_hours(self):
        return self.YourCoWorkersWorkingHours
    
    def get_meeting_duration(self):
        return self.meetingDuration