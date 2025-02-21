# Sorting Algorithms

## **Introduction**

Sorting algorithms play a crucial role in computer science, as they help organize data efficiently for searching, processing, and analysis. Choosing the right sorting algorithm can significantly impact the performance of an application. This document explores three widely used sorting techniques: Bubble Sort, Merge Sort, and Shell Sort. We will examine their mechanisms, efficiency, and ideal use cases to help  make decisions.

---

## **1. Bubble Sort 🫧**

### **Description**

Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is fully sorted.

### **Algorithm Steps**

1. Start from the beginning of the list.
2. Compare adjacent elements.
3. If the current element is greater than the next one, swap them.
4. Move to the next adjacent pair and repeat step 3.
5. After each complete pass through the list, the largest unsorted element is placed in its correct position.
6. Repeat until no swaps are required in a full pass.

---
## **2. Merge Sort**

### **Description**

Merge Sort is a **divide-and-conquer** sorting algorithm. It recursively divides the list into smaller sublists, sorts them individually, and merges them back into a sorted sequence.

### **Algorithm Steps**

1. If the list contains only one element, return it (base case).
2. Divide the list into two halves.
3. Recursively apply Merge Sort on both halves.
4. Merge the two sorted halves back into a single sorted list.

---

## **3. Shell Sort 🐚**

### **Description**

Shell Sort is an improved version of Insertion Sort. It works by comparing elements at a **certain gap (interval)** apart and reducing the gap over time, eventually performing a standard Insertion Sort.

### **Algorithm Steps**

1. Choose an initial interval (gap) size.
2. Compare elements at the given interval and swap if necessary.
3. Reduce the interval and repeat step 2.
4. Continue reducing the interval until it becomes 1 (which results in Insertion Sort).

---

## **Coverage 🐚**

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `python -m coverage run -m unittest discover` and after that run `python -m coverage report` to get the following table:
```
Name                                Stmts   Miss  Cover
------------------------------------------------------
data\constants.py                      2      0   100%
data\data_generator.py                 9      1    89%
sorting_algorithms\bubblesort.py      10      2    80%
sorting_algorithms\mergesort.py       20      3    85%
sorting_algorithms\shellsort.py       12      0   100%
test\__init__.py                       0      0   100%
test\test_algorithms.py               24      1    96%
test\test_data_generator.py           29      1    97%
------------------------------------------------------
TOTAL                                106      8    92%
```
---
If you want to see the lines that are not being used you can run 'python -m cover html' and then 'start htmlcov\index.html'
## **Conclusion**

- **Use Merge Sort** when efficiency and stability are priorities.
- **Shell Sort** is a good choice when memory constraints exist and better performance than Bubble Sort is needed.
- **Avoid Bubble Sort** for large datasets due to its inefficiency.



