# Python-Assignments

## Assignment 1

### Exercise 1

Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and your co-worker's calendar (both of which contain your respective meetings for the day, in the form of [startTime,endTime] , as well as both of your daily working hours (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestStartTime,latestEndTime]
during which you could schedule the meeting. 

Write a function that takes in your calendar, your daily working hours, your co-worker's calendar, your co-worker's working hours, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startTime,endTime] during which you could schedule the meeting. 

Note that times will be given and should be returned in 24 hour clock. For example: [8:30,23:59] and meeting durations will always be in minutes. Mention the (worst case) space and time complexity of your program with an explanation as comment. Feel free to use a data structure of your choice that best suits the problem.

### Exercise 2

You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note that you can't rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times. 

Mention the (worst case) space and time complexity of your program with an explanation as comment feel free to use a data structure of your choice that best suits the problem. When more than combination equals the maximum height , all combinations must be present in the output.

## Assignment 2

### Exercise 1

City Council for City 'X' has decided to test recovered patients of COVID-19 so that it can safely confirm that patients cured of the virus are not getting infected again. Given the huge number of tests City 'X' needs to do on all its inhabitants, the council has decided not to test all recovered patients but instead choose 1 random recovered patients in every recovered patient 5.

The batch size of 5 can change depending on whether City 'X' wants to do more or less testing. Before choosing the next patient, City 'X' also needs to record the test date as its an important parameter to know when the patient was tested. Only print the test date in your program. 

Write an object-oriented python program that helps City 'X' choose recovered patients for testing.

### Exercise 2

Write a function that takes a list of cartesian co-ordinates (x,y) and returns the numbers of squares formed by these co-ordinates.

A square should have its four corners amongst the co-ordinates to be counted as a square. Only squares whos sides are parallel to the x and y axes to be considered.

Try and get the optimum big O notation (considering the worst case) and mention the reason for the same in a comment.