from numpy import arange, repeat
from bolt import array
from bolt.utils import allclose
import generic


def test_map(sc):

    import random
    random.seed(42)

    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    # Test all map functionality when the base array is split after the first axis
    generic.map_suite(x, b)

    # Split the BoltArraySpark after the second axis and rerun the tests
    b = array(x, sc, axes=(0, 1))
    generic.map_suite(x, b)

def test_reduce(sc):

    from numpy import asarray

    dims = (10, 10, 10)
    area = dims[0] * dims[1]
    arr = asarray([repeat(x, area).reshape(dims[0], dims[1]) for x in range(dims[2])])
    b = array(arr, sc, axes=(0,))

    # Test all reduce functionality when the base array is split after the first axis
    generic.reduce_suite(arr, b)

    # Split the BoltArraySpark after the second axis and rerun the tests
    b = array(arr, sc, axes=(0, 1))
    generic.reduce_suite(arr, b)

def test_filter(sc):

    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    # Test all filter functionality when the base array is split after the first axis
    generic.filter_suite(x, b)

    # Split the BoltArraySpark after the second axis and rerun the tests
    b = array(x, sc, axes=(0, 1))
    generic.filter_suite(x, b)

def test_mean(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.mean(axes=(0,)), x.mean(axis=(0,)))
    assert allclose(b.mean(axes=(0,1)), x.mean(axis=(0, 1)))
    assert b.mean(axes=(0, 1, 2)) == x.mean(axis=(0, 1, 2))

def test_std(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.std(axes=(0,)), x.std(axis=(0,)))
    assert allclose(b.std(axes=(0,1)), x.std(axis=(0, 1)))
    assert b.std(axes=(0, 1, 2)) == x.std(axis=(0, 1, 2))

def test_var(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.var(axes=(0,)), x.var(axis=(0,)))
    assert allclose(b.var(axes=(0,1)), x.var(axis=(0, 1)))
    assert b.var(axes=(0,1,2)) == x.var(axis=(0, 1, 2))

def test_sum(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.sum(axes=(0,)), x.sum(axis=(0,)))
    assert allclose(b.sum(axes=(0,1)), x.sum(axis=(0,1)))
    assert b.sum(axes=(0, 1, 2)) == x.sum(axis=(0, 1, 2))

def test_min(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.min(axes=(0,)), x.min(axis=(0,)))
    assert allclose(b.min(axes=(0,1)), x.min(axis=(0, 1)))
    assert b.min(axes=(0, 1, 2)) == x.min(axis=(0, 1, 2))

def test_max(sc):
    x = arange(2*3*4).reshape(2, 3, 4)
    b = array(x, sc, axes=(0,))

    assert allclose(b.max(axes=(0,)), x.max(axis=(0,)))
    assert allclose(b.max(axes=(0,1)), x.max(axis=(0, 1)))
    assert b.max(axes=(0, 1, 2)) == x.max(axis=(0, 1, 2))