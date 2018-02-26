import collections.dequeue as dq

def manage_queue(max_length, queue, point):
    if len(array) > max_length:
	    queue.append(point)
		queue.popleft()
	else:
	    queue.append(point)
	return queue


def get_diff(q, length):
    tmp = q
	ref = q.pop()
	sum = 0
	for i in range(0:length):
	    sum += ref - q.pop()
	return sum / length
	
	
def choose(queue):
    tmp = queue
	choose = []
	choose.append(10 * get_diff(tmp, 100))
	choose.append(20 * get_diff(tmp, 200))
	choose.append(30 * get_diff(tmp, 300))
	choose.append(50 * get_diff(tmp, 500))
	choose.append(100 * get_diff(tmp, 1000))
	

array_length = 1000
