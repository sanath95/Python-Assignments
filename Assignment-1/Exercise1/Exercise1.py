from inputs import get_your_calendar, get_your_working_hours, get_your_co_workers_calendar, get_your_co_workers_working_hours, get_meeting_duration
from utils.time_converter import convert_calendar_to_minutes, convert_working_hours_to_minutes, convert_minutes_to_time

def get_meeting_schedule(meeting_duration, your_calendar, your_working_hours, your_co_workers_calendar, your_co_workers_working_hours):
    
    # assume time and space complexity for helper files to be constant
    # time complexity = O(1)
    # space complexity = O(1)
    your_calendar = convert_calendar_to_minutes(get_your_calendar())
    your_working_hours = convert_working_hours_to_minutes(get_your_working_hours())
    your_co_workers_calendar = convert_calendar_to_minutes(get_your_co_workers_calendar())
    your_co_workers_working_hours = convert_working_hours_to_minutes(get_your_co_workers_working_hours())

    # time complexity = O(n log(n))
    # space complexity = O(2n) = O(n)
    meeting_start_times = sorted([meeting[0] for meeting in your_calendar] + [meeting[0] for meeting in your_co_workers_calendar])
    meeting_end_times = sorted([meeting[1] for meeting in your_calendar] + [meeting[1] for meeting in your_co_workers_calendar])

    # time complexity = O(n + 2) = O(n)
    # space complexity = O(n)
    meeting_start_times_without_overlap = []
    for i in range(len(meeting_start_times)):
        if (i == 0):
            meeting_start_times_without_overlap.append(meeting_start_times[i])
            continue
        if (meeting_start_times[i] > meeting_end_times[i-1]):
            meeting_start_times_without_overlap.append(meeting_start_times[i])

    # time complexity = O(n + 2) = O(n)
    # space complexity = O(n)
    meeting_end_times_without_overlap = []
    for i in range(len(meeting_end_times)):
        if (i == len(meeting_end_times)-1):
            meeting_end_times_without_overlap.append(meeting_end_times[i])
            continue
        if (meeting_end_times[i] < meeting_start_times[i+1]):
            meeting_end_times_without_overlap.append(meeting_end_times[i])

    # time complexity = O(1)
    # space complexity = O(1)
    work_start_time = your_working_hours[0] if your_working_hours[0] >= your_co_workers_working_hours[0] else your_co_workers_working_hours[0]
    work_end_time = your_working_hours[1] if your_working_hours[1] <= your_co_workers_working_hours[1] else your_co_workers_working_hours[1]

    # time complexity = O(1)
    # space complexity = O(1)
    meeting_time_blocks_in_minutes = []
    if (meeting_start_times_without_overlap[0] - work_start_time >= meeting_duration):
        meeting_time_blocks_in_minutes.append([work_start_time, meeting_start_times_without_overlap[0]])

    # time complexity = O(n + 1) = O(n)
    # space complexity = O(n)
    for i in range(len(meeting_start_times_without_overlap)-1):
        if (meeting_start_times_without_overlap[i+1]-meeting_end_times_without_overlap[i] >= meeting_duration):
            meeting_time_blocks_in_minutes.append([meeting_end_times_without_overlap[i], meeting_start_times_without_overlap[i+1]])

    # time complexity = O(1)
    # space complexity = O(1)
    if (work_end_time - meeting_end_times_without_overlap[-1] >= meeting_duration):
        meeting_time_blocks_in_minutes.append([meeting_end_times_without_overlap[-1], work_end_time])

    # list comprehension with 2 for loops
    # time complexity = O(n) for outer loop and O(2) for inner loop (slot will have only 2 elements - start and end time) = O(n)
    # space complexity = O(n)
    return [[convert_minutes_to_time(time) for time in slot] for slot in meeting_time_blocks_in_minutes]

if __name__ == "__main__":

    meeting_schedule = get_meeting_schedule(get_meeting_duration(), get_your_calendar(), get_your_working_hours(), get_your_co_workers_calendar(), get_your_co_workers_working_hours())
    print(meeting_schedule)

# overall time complexity = O(n log n)
# overall space complexity = O(n)