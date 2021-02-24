# Sort_Me_Please
Vizualization of sorting algorithms
**Note**: this code is not meant to be used as perfomance mark, since all sorts are run in single thread
and not optimized for best perfomance

## Metrics for sorts
Metrics for sorts are based on time and space(memory usage) complexity, number of operations and loops, memory acceses
*Big O notation* - most popular asymptotic approximation used for defying upper sort function complexity limit (theta - for equavalent, sigma - for lower limit)
Asymptotic analysis used for neglecting small problem size, constant factors as language realisation etc, approximating sort perfomance. Netherless strict operation count and union of several algorithms othen used for best perfomance.
1) Worst case perfomance
   Minimum theoretical number of iterations needed for algorithm to sort an array
2) Average case pefomance
   Benchmarked or theoretical average numbers of iterations
3) Best case is hardly used for not having practical value
Stability of sorting algorithm is a preservance of order
Online is ability to sort stream of incoming data

## Comparison sorts vs count(integer) sorts
Comarison sorts compare values, best complexity is O(nlog(n))
Pros: suitible for arbitary types
Cons: upper limit O(nlog(n))
 
Count sorts count elements by key (must be integer key, ex: position of integer scale)
Pros: can be faster than comparison sorts
Cons: slow initialization, variation must not be significantly greater than the number of items

## Top tier
### Quick sort

### Merge sort
1) Divide array into tree with leafs array of minimum length 1
2) Repeatedly merge arrays from bottom up the tree whilst sorting
Worst: O(nlog(n))
Average: O(nlog(n))
Memory: O(n)
Pros: parallelism, stable, best for linked lists
Cons: extra memory


## Mid tier
### Insertion sort
1) Step by one element, comparing with all elements before
2) Insert element than it is sorted relative to elements checked
Worst: O(n^2)
Average: O(n^2)
Memory: inplace, aux O(1)
Pros: fast for small or partially sorted arrays, stable, online
Cons: slow worst case
### Counting sort
1) Create count array of keys, built histogram of values in array
2) Prefix sum through count array
3) Create output array size of original, step through original array and place element in its count array position, decresing count array position by 1
Worst: O(n+k)
Average: O(n+k)
Memorty: O(n+k)
Pros: linear for integer sequence permutations (1,2...n), could be faster than O(nlog(n))
Cons: suited for integers, varience between integers must not be big, slow initialization, aux memory

## Low tier
### Selection sort
1) Divide array into sorted and unsorted parts, scan through unsorted 
2) Select the minimum(or max) element, swap(or insert and shift for stable version) in begining of sorted part
Worst: O(n^2)
Average: O(n^2)
Memory: inplace, aux O(1)
Pros: low memory writes, stable, simple
Cons: slow


## Entertainment tier
### Buble sort
1) Step through list while sorting adjacent elements
2) Repeat 1 till sorted
Worst: O(n^2)
Average: O(n^2)
Memory: inplace, aux O(1)
Pros: simple, inplace, stable
Cons: very slow