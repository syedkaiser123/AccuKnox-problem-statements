from os.path import exists
import sys

def validate_file_paths(log_files, defualt_read_flag):
    """validating the file paths.

    Args:
        log_files (File): file path
        defualt_read_flag (bool): boolean value 'True' or 'False', default=True.

    Returns:
        bool: True or False
    """
    valid_file_paths = []
    invalid_file_paths = []
    if defualt_read_flag:
        return log_files
    for file in log_files:
        file_exists = exists("./log_files/%s" %(file))
        if file_exists:
            valid_file_paths.append(file)
        else:
            invalid_file_paths.append(file)
    if invalid_file_paths:
        print("File(s) Not Found: %s" %(", ".join(invalid_file_paths)))
    return valid_file_paths

def read_log_file(filename):
    """reading log files from log_files directory.

    Args:
        filename (File): log filename

    Returns:
        list: list of dictionary objects.
    """
    
    try:
        data = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            for i,each in enumerate(lines):                        
                data.append({
                    "eater_id":each.split(',')[0],
                    "food_menu_id":each.split(',')[1].replace("\n","")
                })
        return data
    except Exception as e:
        return {"message": "{}".format(e)}