package main

import (
	"fmt"
)

var data = []int{-1, 0, 2, 5, 6, 3, 8, 1, 9, 4, 7}
var DATA_SIZE int = 10

func swap(x, y int) (int, int) {
	return y, x
}

func sink(start, end int) {
	for start*2 < end {
		var childLeftIndex int = start * 2

		if (childLeftIndex+1) <= DATA_SIZE && data[childLeftIndex] < data[childLeftIndex+1] {
			childLeftIndex++
		}

		if data[start] > data[childLeftIndex] {
			break
		}

		data[start], data[childLeftIndex] = swap(data[start], data[childLeftIndex])
		start = childLeftIndex
	}
}

func heapSort() {
	var N int = DATA_SIZE

	for i := N / 2; i > 0; i-- {
		sink(i, N)
	}

	for N > 1 {
		data[1], data[N] = swap(data[1], data[N])
		N--
		sink(1, N)
	}
}

func print() {
	for i := 1; i < 10; i++ {
		fmt.Print(data[i], ",")
	}
	fmt.Println(data[DATA_SIZE])
}

func main() {
	// var a, b int = 1, 2
	fmt.Println("Before HeapSort")
	print()
	fmt.Println("After HeapSort")
	heapSort()
	print()
}
