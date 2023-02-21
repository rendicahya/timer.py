from time import sleep

from timer_py import Timer

timer = Timer()
timer.start()
# Or:
# timer = Timer(start=True)

# A one-second process
sleep(1)

# Printing the elapsed time. The timer will continue to run.
timer.elapsed()
# Output:
# [timer.py] 00:00:01.004

# Pause the timer.
timer.pause()

# A one-second process that won't be counted while the timer is paused.
sleep(1)

# Resume the timer.
timer.resume()

# Another one-second process.
sleep(1)

# Overriding the tag for one time only (the original tag will still be remembered).
timer.elapsed("Checkpoint 1")
# Output:
# [Checkpoint 1] 00:00:02.008

# Changing the tag
timer.set_tag("Custom title")

# Restarting the time
timer.restart()

# Another one-second process.
sleep(1)

# Storing the elapsed time to a variable as a float while hiding the output.
elapsed = timer.elapsed(print=False)
print(elapsed)
# Output:
# 2.0134578000000003

# Stop the timer
timer.stop()
# Output:
# [Custom title] 00:00:01.006
