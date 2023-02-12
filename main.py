import os 

def main():
    i = 0
    path = "C:/Users/manan/Desktop/bulk_renaming_test_folder/"
    for filename in os.listdir(path):
        my_dest = "temp_" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    i = 0
    for filename in os.listdir(path):

        my_dest = "img_" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()
