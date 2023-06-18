import xlrd
import os

def write_from_xls(file):
    
    def file_name(cell):
        num_type = type(cell.value)
        if num_type == float:
            num = str(int(cell.value))
        elif num_type == int:
            num = str(cell.value)
        elif num_type == str:
            num = cell.value
        return num

    def split_title(cell):
        string1 = cell.value.split(" / ")
        string2 = string1[0].replace("*", "")
        return string2
    
    def split_key(cell):
        return cell.value.replace(" – ", " - ").split(" - ")


    wb = xlrd.open_workbook(file)
    sh = wb.sheet_by_index(0)
       
    folder_name = file.split("/")[-1].split(".")[0]
    folder_path = file.rsplit("/", 1)[0]
    folder = os.path.join(folder_path + "/", folder_name)
    os.mkdir(folder)
    
    for row in sh.get_rows():
        n = file_name(row[0])
        txt = split_title(row[1])
        keys = split_key(row[2])

        txt_file = folder + "/" + n + ".txt"
        with open(txt_file, 'w+', encoding='utf-8') as tf:
            tf.write(txt)
        
        key_file = folder + "/" + n + ".key"
        with open(key_file, 'w+', encoding='utf-8') as kf:
            for key in keys:
                kf.write(key)
                kf.write('\n')