from datetime import datetime

def _convert_time_to_minutes(this_time):
    return ((datetime.strptime(this_time, '%H:%M') - datetime.strptime('00:00', '%H:%M')).total_seconds())/60

def convert_calendar_to_minutes(calendar):
    # using list instead of set because set does not enforce or maintain any particular order of the elements
    return [[_convert_time_to_minutes(x) for x in meeting] for meeting in calendar]

def convert_working_hours_to_minutes(working_hours):
    # using list instead of set because set does not enforce or maintain any particular order of the elements
    return [_convert_time_to_minutes(x) for x in working_hours]

def convert_minutes_to_time(minutes):
    hh = str(int(minutes/60)).zfill(2)
    mm = str(int(minutes%60)).zfill(2)
    return hh + ':' + mm