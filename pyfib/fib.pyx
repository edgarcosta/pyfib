# distutils: language=c
# clang c

from sage.rings.integer cimport Integer

cpdef int fib(int n):
    cdef int a = 0, b = 1
    cdef int i
    for i in range(n):
        a, b = b, a+b
    return a

