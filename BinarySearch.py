def BinarySearch(datas,traget):
	low = 0;
	high = len(datas) - 1
	while low <= high:
		mid = (low+high) >> 1
		if(datas[mid]<traget):
			low = mid + 1
		elif datas[mid] > traget:
			high = mid - 1
		else:
			return mid

	return -1


datas = [1,2,3,4,5,6]

print("find target in index of %d",BinarySearch(datas,2))