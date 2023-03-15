# timer.py

timer.py provides convenient functions to measure time in Python. 

## Installation
```
pip install timer.py
```

## Usage
```python
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
# [timer.py] 00:00:01.001

timer.pause()

# A one-second process that won't be counted while the timer is paused.
sleep(1)

timer.resume()

# Another one-second process.
sleep(1)

# Overriding the tag for one time only (the original tag will still be remembered).
timer.elapsed('Checkpoint 1')
# Output:
# [Checkpoint 1] 00:00:02.002

timer.set_tag('Custom title')

timer.restart()

# Another one-second process.
sleep(1)

# Storing the elapsed time to a variable as a float while hiding the output.
elapsed = timer.elapsed(print=False)
print(elapsed)
# Output:
# 00:00:01.001

timer.stop()
# Output:
# [Custom title] 00:00:01.001
```
