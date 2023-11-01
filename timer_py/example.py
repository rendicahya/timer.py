from time import sleep

from timer_py import Timer

timer = Timer()
timer.start()

# A one second process
sleep(1)

# Printing the elapsed time. The timer will continue to run
timer.elapsed()
# Output:
# [timer.py]  00:00:01.001

timer.pause()

# This process won't be counted as the timer is paused.
sleep(1)

timer.resume()

# This process will be counted
sleep(1)

# Overriding the tag for this time only (the previous tag will still be remembered)
timer.elapsed("Checkpoint 1")
# Output:
# [Checkpoint 1] 00:00:02.002

# Changing the tag
timer.set_tag("Custom tag")
timer.restart()

sleep(1)

# Storing the elapsed time to a variable as a float while hiding the output
elapsed = timer.elapsed(print=False, raw=True)
print(type(elapsed), elapsed)
# Output:
# <class 'float'> 1.0010546641424298

timer.stop()
# Output:
# [Custom title] 00:00:01.001
