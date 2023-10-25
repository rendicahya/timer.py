from time import sleep

from timer_py import Timer

timer = Timer('Timer demo')
timer.start()

# A one-second process
sleep(1)

# Printing the elapsed time. The timer will continue to run
timer.elapsed()
# Output:
# [Timer demo]  00:00:01.001

timer.pause()

# Process that won't be counted
sleep(1)

timer.resume()

sleep(1)

# Overriding the tag for this time only (the previously set tag will still be remembered)
timer.elapsed("Checkpoint 1")
# Output:
# [Checkpoint 1] 00:00:02.002

# Changing the tag
timer.set_tag("Another tag")
timer.restart()

sleep(1)

# Storing the elapsed time to a variable as a float while hiding the output
elapsed = timer.elapsed(print=False, raw=True)
print(type(elapsed), elapsed)
# Output:
# <class 'float'> 1.0010546641424298

# Stop the timer
timer.stop()
# Output:
# [Another tag] 00:00:01.001
