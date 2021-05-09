
import time

start = time.time()
tmp = 3
for i in range(9):
    tmp = tmp**7

end = time.time()
duration = round(end - start, 2)
print('done', duration, 'seconds')
