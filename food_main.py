import sys
import os

from utils.utils import validate_file_paths, read_log_file


"""
python3 ./food_main.py [FILENAMES]

FILENAMES are optional, by default script will run for all the files in the log_files directory

"""

class restaurant():
    
    def __init__(self, *args, **kwargs):
        """initialising global variables.
        """
        
        self.data = kwargs.get("data", [])
        self.filename = kwargs.get("file", "")
        self.dinings = []
    
    def is_duplicate_entries(self):
        """checking for duplicate values/entries.

        Returns:
            bool: True or False.
        """
        
        self.dinings = [
            "%s - %s"%(data.get("eater_id", ""), data.get("food_menu_id", ""))
                for data in self.data
        ]
        if len(set(self.dinings)) != len(self.dinings):
            return True 
        return False
        

    def get_top_food_items(self):
        """identifying top 3 consumed food items based on their count.

        Returns:
            list: list of items.
        """

        is_duplicate = self.is_duplicate_entries()
        if is_duplicate:
            print("#"*50)
            print("filename: %s" %(self.filename))
            print("Error: Duplicate diners not allowed")
            print("#"*50)
            print()
            return

        dining_count = {}
        for dining in self.data:
            food_item = dining.get("food_menu_id")
            if food_item not in dining_count:
                dining_count[food_item] = 1
            else:
                dining_count[food_item] +=1
        # print(dining_count)
        temp_result = {}
        for dining, count in dining_count.items():
            if count not in temp_result:
                temp_result[count] = [dining]
            else:
                temp_result[count].append(dining)
        
        counts = sorted(temp_result.keys(), reverse=True)
        result = []
        for key in counts:
            if len(result)>=3:
                break
            result = [*result, *temp_result.get(key)]
        result = result[:3]
        # result_string = ["%s: %s" %(food.split("-")[-1], dining_count.get(food)) for food in result]
        return result

if __name__ == "__main__":

    defualt_read_flag = True
    command_arguments = sys.argv[1:]
    if command_arguments:
        log_files = command_arguments
        defualt_read_flag = False
    else:
        log_files = os.listdir('./log_files/')
        valid_files = log_files

    if not defualt_read_flag:
        valid_files = validate_file_paths(log_files, defualt_read_flag)

    if valid_files:
        for file in valid_files:
            file = "./log_files/%s"%(file)
            data = read_log_file(file)
            restaurant_obj = restaurant(data=data, file=file)
            result = restaurant_obj.get_top_food_items()
            if result:
                print("#"*50)
                print("filename: %s" %(restaurant_obj.filename))
                print("top %s consumed food items are (food_menu_id, count):\n\t" %(len(result)))
                print( "%s" %(", ".join(result)) )
                print("#"*50)
                print()