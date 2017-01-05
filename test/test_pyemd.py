#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test/test_pyemd.py

"""Tests for PyEMD"""

import numpy as np
import pytest

from pyemd import emd, emd_with_flows


def test_case_1():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    assert emd(first_signature, second_signature, distance_matrix) == 3.5


def test_case_1_flows():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    assert (emd_with_flows(first_signature, second_signature, distance_matrix)
            == (3.5, [[0.0, 0.0], [0.0, 1.0]]))


def test_case_2():
    first_signature = np.array([1.0, 1.0])
    second_signature = np.array([1.0, 1.0])
    distance_matrix = np.array([[0.0, 1.0],
                                [1.0, 0.0]])
    assert emd(first_signature, second_signature, distance_matrix) == 0.0


def test_case_2_flows():
    first_signature = np.array([1.0, 1.0])
    second_signature = np.array([1.0, 1.0])
    distance_matrix = np.array([[0.0, 1.0],
                                [1.0, 0.0]])

    assert (emd_with_flows(first_signature, second_signature, distance_matrix)
            == (0.0, [[1.0, 0.0], [0.0, 1.0]]))


def test_case_3():
    first_signature = np.array([6.0, 1.0])
    second_signature = np.array([1.0, 7.0])
    distance_matrix = np.array([[0.0, 0.0],
                                [0.0, 0.0]])
    assert emd(first_signature, second_signature, distance_matrix) == 0.0


def test_case_3_flows():
    first_signature = np.array([6.0, 1.0])
    second_signature = np.array([1.0, 7.0])
    distance_matrix = np.array([[0.0, 0.0],
                                [0.0, 0.0]])
    assert (emd_with_flows(first_signature, second_signature, distance_matrix)
            == (0.0, [[1.0, 5.0], [0.0, 1.0]]))


def test_case_4_flows():
    first_signature = np.array([1.0, 7.0])
    second_signature = np.array([6.0, 1.0])
    distance_matrix = np.array([[0.0, 0.0],
                                [0.0, 0.0]])
    assert (emd_with_flows(first_signature, second_signature, distance_matrix)
            == (0.0, [[1.0, 0.0], [5.0, 1.0]]))



def test_case_5_flows():
    first_signature = np.array([3.0, 5.0])
    second_signature = np.array([6.0, 2.0])
    distance_matrix = np.array([[0.0, 0.0],
                                [0.0, 0.0]])
    assert (emd_with_flows(first_signature, second_signature, distance_matrix)
            == (0.0, [[3.0, 0.0], [3.0, 2.0]]))


def test_larger_signatures():
    first_signature = np.array([0.0, 1.0, 2.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd(first_signature, second_signature, distance_matrix)


def test_larger_signatures_flows():
    first_signature = np.array([0.0, 1.0, 2.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd_with_flows(first_signature, second_signature, distance_matrix)


def test_larger_signatures_1():
    first_signature = np.array([0.0, 1.0, 2.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd_with_flows(first_signature, second_signature, distance_matrix)


def test_larger_signatures_1_flows():
    first_signature = np.array([0.0, 1.0, 2.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd(first_signature, second_signature, distance_matrix)


def test_larger_signatures_2():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd(first_signature, second_signature, distance_matrix)


def test_larger_signatures_2_flows():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd_with_flows(first_signature, second_signature, distance_matrix)


def test_different_signature_dims():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5, 0.0],
                                [0.5, 0.0, 0.0],
                                [0.5, 0.0, 0.0]])
    with pytest.raises(ValueError):
        emd(first_signature, second_signature, distance_matrix)


def test_different_signature_dims_flows():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5, 0.0],
                                [0.5, 0.0, 0.0],
                                [0.5, 0.0, 0.0]])
    with pytest.raises(ValueError):
        emd_with_flows(first_signature, second_signature, distance_matrix)


def test_symmetric_distance_matrix():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5, 3.0],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd(first_signature, second_signature, distance_matrix)


def test_symmetric_distance_matrix_flows():
    first_signature = np.array([0.0, 1.0])
    second_signature = np.array([5.0, 3.0])
    distance_matrix = np.array([[0.0, 0.5, 3.0],
                                [0.5, 0.0]])
    with pytest.raises(ValueError):
        emd_with_flows(first_signature, second_signature, distance_matrix)
