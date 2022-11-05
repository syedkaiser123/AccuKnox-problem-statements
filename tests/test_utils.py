import sys
import os

sys.path.append("/home/recosenselabs/Downloads/accuknox/utils/")
from accuknox.utils.utils import read_log_file, validate_file_paths


def test_read_log_file():
    """unit test case for the class method read_log_file().
    """
    
    temp = [
                {
                    'eater_id': '#100',
                    'food_menu_id': '*001'
                },
                {
                    'eater_id': '#100',
                    'food_menu_id': '*001'
                },
                {
                    'eater_id': '#101',
                    'food_menu_id': '*002'
                },
                {
                    'eater_id': '#101',
                    'food_menu_id': '*002'
                },
                {
                    'eater_id': '#102',
                    'food_menu_id': '*003'
                },
                {
                    'eater_id': '#103',
                    'food_menu_id': '*004'
                },
                {
                    'eater_id': '#104',
                    'food_menu_id': '*005'
                },
                {
                    'eater_id': '#105',
                    'food_menu_id': '*003'
                },
                {
                    'eater_id': '#105',
                    'food_menu_id': '*003'
                },
                {
                    'eater_id': '#106',
                    'food_menu_id': '*009'
                },
                {
                    'eater_id': '#107',
                    'food_menu_id': '*002'
                },
                {
                    'eater_id': '#108',
                    'food_menu_id': '*009'
                },
                {
                    'eater_id': '#109',
                    'food_menu_id': '*009'
                }
            ]

    
    assert temp == read_log_file("log_files/testlog_1.log")
    
    
def test_validate_file_paths_true():
    """unit test case for the class method validate_file_paths() when true.
    """
    
    log_files = os.listdir('./log_files/')
    res = validate_file_paths(log_files, False)  
    assert res == log_files
    
    
def test_validate_file_paths_false():
    """unit test case for the class method validate_file_paths() when false.
    """
    
    log_files = os.listdir('./log_files/')
    res = validate_file_paths(log_files, False)  
    assert [] != res