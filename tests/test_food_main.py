import sys
import os

sys.path.append("/home/recosenselabs/Downloads/accuknox/")
from accuknox.food_main import restaurant


def test_is_duplicate_entries():
    """unit test case for is_duplicate_entries().
    """
    
    assert restaurant().is_duplicate_entries() == False


def test_get_top_food_items():
    """unit test case for get_top_food_items().
    """
    
    res = ['*003', '*002', '*001']
    data = [
            {'eater_id': '#100', 'food_menu_id': '*001'
            },
            {'eater_id': '#100', 'food_menu_id': '*002'
            },
            {'eater_id': '#100', 'food_menu_id': '*003'
            },
            {'eater_id': '#100', 'food_menu_id': '*004'
            },
            {'eater_id': '#101', 'food_menu_id': '*001'
            },
            {'eater_id': '#102', 'food_menu_id': '*002'
            },
            {'eater_id': '#103', 'food_menu_id': '*003'
            },
            {'eater_id': '#104', 'food_menu_id': '*004'
            },
            {'eater_id': '#103', 'food_menu_id': '*002'
            },
            {'eater_id': '#105', 'food_menu_id': '*003'
            },
            {'eater_id': '#106', 'food_menu_id': '*003'
            },
            {'eater_id': '#107', 'food_menu_id': '*003'
            },
            {'eater_id': '#108', 'food_menu_id': '*002'
            }
        ]
    
    test_obj = restaurant(data=data, file="log_files/testlog_2.log")
    assert res == test_obj.get_top_food_items()