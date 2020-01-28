import os
import sys
import re
import numpy as np

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

import exam

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()

def teardown_module(module):
    '''Cleanup process'''
    sh_pywrapper.kill_process(module.process)

def unix_command_check(exercise_number):

    # Test for existance of Unix command file
    commands_list = sh_pywrapper.parse('exam.sh')

    # Test that there are at least n commands
    assert len(commands_list) >= exercise_number and len(commands_list[exercise_number-1]) > 0

    # Run command
    return sh_pywrapper.run(process, commands_list[exercise_number-1])

def parse_unix_output(command_outputs):
    output = []
    for command_output in command_outputs:
        if command_output.strip() == '':
            continue
        output += [o.strip() for o in command_output.split('\n')]
    return output

def test_exam_test_import():
    '''Test that exam_test works'''
    import exam_test

def test_ex1_1_basic():
    '''Test that command exists in .sh file'''
    unix_command_check(1)

def test_ex1_2_basic():
    '''Test for existence and callability of read_year_to_anomaly_data'''

    # Check that the function exists
    assert hasattr(exam, "read_year_to_anomaly_data")

    # Check that the function can be called 
    exam.read_year_to_anomaly_data("data/Land_and_Ocean_summary.txt")

def test_ex1_3_basic():
    '''Test for existence and callability of create_line_plot'''

    # Check that the function exists
    assert hasattr(exam, "create_line_plot")

    # Check that the function can be called
    exam.create_line_plot({2017:0.0, 2018:1.0}, "test.png")
    
def test_ex2_1_basic():
    '''Test for existence and instantiability of ColorMapper'''

    # Check that the function exists
    assert hasattr(exam, "ColorMapper")

    # Check that the class can be instantiated
    exam.ColorMapper([-1.0, 0.0, 1.2])

def test_ex2_2_basic():
    '''Test for existence and callability of construct_blocks'''

    # Check that the function exists
    assert hasattr(exam, "construct_blocks")

    # Check that the function can be called
    exam.construct_blocks({2017:0.09, 2018: 0.07})

def test_ex2_3_basic():
    '''Test for existence and callability of calculate_anomalies_per_decade'''

    # Check that the function exists
    assert hasattr(exam, "calculate_anomalies_per_decade")

    # Check that the function can be called
    exam.calculate_anomalies_per_decade({1850: -0.532, 1851: -0.405, 1852: -0.395, 1853: -0.418, 1854: -0.363, 1855: -0.34, 1856: -0.483, 1857: -0.608, 1858: -0.463, 1859: -0.408, 1860: -0.482, 1861: -0.575, 1862: -0.659, 1863: -0.427, 1864: -0.452, 1865: -0.354, 1866: -0.298, 1867: -0.277, 1868: -0.264, 1869: -0.281, 1870: -0.36})
        
def test_ex3_1_basic():
    '''Test for existence and callability of read_latitude_year_to_anomaly_data'''

    # Check that the function exists
    assert hasattr(exam, "read_latitude_year_to_anomaly_data")

    # Check that the function can be called
    exam.read_latitude_year_to_anomaly_data('data/anomalies_per_latitude.txt')

def test_ex3_2_basic():
    '''Test for existence and callability of get_values_from_nested_dict'''

    # Check that the function exists
    assert hasattr(exam, "get_values_from_nested_dict")

    # Check that the function can be called
    exam.get_values_from_nested_dict({})

def test_ex3_3_basic():
    '''Test for existence and callability of construct_latitude_blocks'''

    # Check that the function exists
    assert hasattr(exam, "construct_latitude_blocks")

    # Check that the function can be called
    exam.construct_latitude_blocks({2.5:{2016:0.,2017:1.}, 7.5:{2016:0.,2017:1.}})

def test_ex4_1_basic():
    '''Test that command exists in .sh file'''
    unix_command_check(2)

    # Check that output file exists
    assert os.path.exists("top10_CO2.csv")

    
def test_ex4_2_basic():
    '''Test for existence and callability of find_top10_emitting_countries'''

    # Check that the function exists
    assert hasattr(exam, "find_top10_emitting_countries")

    # Check that the function can be called
    exam.find_top10_emitting_countries('data/annual-co-emissions-by-region.csv')
    
def test_ex4_3_basic():
    '''Test for existence and callability of read_population_data'''

    # Check that the function exists
    assert hasattr(exam, "read_population_data")

    # Check that the function can be called
    exam.read_population_data('data/population.csv', 2017)
    
