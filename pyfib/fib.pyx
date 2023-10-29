from sage.rings.integer cimport Integer

cpdef int fib(int n):
    cdef Integer a = 0, b = 1
    cdef Integer i
    for i in range(n):
        a, b = b, a+b
    return a
