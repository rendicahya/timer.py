# timer.py

## Installation
```python
pip install timerpy
```

## Usage
```python
from time import sleep
from timer_py import Timer

timer = Timer('Some Title')
timer.start()
# Or:
# timer = Timer('Some Title').start()

# Some one-second process
sleep(1)

# Printing the elapsed time. The timer will continue to run.
timer.elapsed()
# Output:
# [Some Title] 00:00:01.004

# Pause the timer
timer.pause()

# Process that won't be counted
sleep(1)

# Resume the timer
timer.resume()

# Another one-second process
sleep(1)

# Overriding the tag
timer.elapsed('Checkpoint 1')
# Output:
# [Checkpoint 1] 00:00:02.013

# Storing the elapsed time to a variable while hiding the output
elapsed = timer.elapsed(print=False)
print(elapsed)
# Output:
# 2.0134578000000003

# Stop the timer
timer.stop()
# Output:
# [Some Title] 00:00:02.013
```
