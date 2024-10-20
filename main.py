# main.py
import importlib
from datetime import datetime
from BST import BinarySearchTree


# import BinarySearchTree from BST.py file
# st = importlib.import_module("BST").BinarySearchTree()
# st = importlib.import_module("RBT").RedBlackTree()
st = importlib.import_module("ST").SplayTree()

# Usage


def bst_insert():
    # TODO: Read all "Insert data files" separately in sequential order
    # bst = BinarySearchTree()

    def read_numbers_from_file(filename):
        numbers = []
        with open(filename, 'r') as file:
            for line in file:
             # Convert each line to an integer and add to the list
             numbers.append(int(line.strip()))
        return numbers

    insert_set1_data_1 = read_numbers_from_file("insert_set1_data_1.txt")
    insert_set1_data_2 = read_numbers_from_file("insert_set1_data_2.txt")
    insert_set1_data_3 = read_numbers_from_file("insert_set1_data_3.txt")
    insert_set2_data_1 = read_numbers_from_file("insert_set2_data_1.txt")
    insert_set2_data_2 = read_numbers_from_file("insert_set2_data_2.txt")
    insert_set2_data_3 = read_numbers_from_file("insert_set2_data_3.txt")

    starts1d1 = datetime.now()
    for value in insert_set1_data_1:
        st.insert(value)
    ends1d1 = datetime.now()
    durations1d1 = ends1d1 - starts1d1
    height1 = st.height()

    starts1d2 = datetime.now()
    for value in insert_set1_data_2:
        st.insert(value)
    ends1d2 = datetime.now()
    durations1d2 = ends1d2 - starts1d2
    height2 = st.height()

    starts1d3 = datetime.now()
    for value in insert_set1_data_3:
        st.insert(value)
    ends1d3 = datetime.now()
    durations1d3 = ends1d3 - starts1d3
    height3 = st.height()




    starts2d1 = datetime.now()
    for value in insert_set2_data_1:
        st.insert(value)
    ends2d1 = datetime.now()
    durations2d1 = ends2d1 - starts2d1
    height4 = st.height()


    starts2d2 = datetime.now()
    for value in insert_set2_data_2:
        st.insert(value)
    ends2d2 = datetime.now()
    durations2d2 = ends2d2 - starts2d2
    height5 = st.height()


    starts2d3 = datetime.now()
    for value in insert_set2_data_3:
        st.insert(value)
    ends2d3 = datetime.now()
    durations2d3 = ends2d3 - starts2d3
    height6 = st.height()


    print("Insert Set1 Data1 ", durations1d1.microseconds)
    print("Height Set1 Data1 ", height1)
    print("----------------------------------------------")
    print("Insert Set1 Data2 ", durations1d2.microseconds)
    print("Height Set1 Data2 ", height2)
    print("----------------------------------------------")
    print("Insert Set1 Data3 ", durations1d3.microseconds)
    print("Height Set1 Data3 ", height3)
    print("----------------------------------------------")
    print("Insert Set2 Data1 ", durations2d1.microseconds)
    print("Height Set2 Data1 ", height4)
    print("----------------------------------------------")
    print("Insert Set2 Data2 ", durations2d2.microseconds)
    print("Height Set2 Data2 ", height5)
    print("----------------------------------------------")
    print("Insert Set2 Data3 ", durations2d3.microseconds)
    print("Height Set2 Data3 ", height6)

    return [durations1d1.microseconds,durations1d2.microseconds,durations1d3.microseconds,durations2d1.microseconds,durations2d2.microseconds,durations2d3.microseconds]




def bst_search():
    # We must insert data before doing any operation
    bst_insert() # Please ignore the time measurement of this data insertion
    print("-----------------------------------------------Search Begins-----------------------------------")
    def read_numbers_from_file(filename):
        numbers = []
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to an integer and add to the list
                numbers.append(int(line.strip()))
        return numbers
    
    search_set1_data_1 = read_numbers_from_file("search_set1_data_1.txt")
    search_set1_data_2 = read_numbers_from_file("search_set1_data_2.txt")
    search_set1_data_3 = read_numbers_from_file("search_set1_data_3.txt")
    search_set2_data_1 = read_numbers_from_file("search_set2_data_1.txt")
    search_set2_data_2 = read_numbers_from_file("search_set2_data_2.txt")
    search_set2_data_3 = read_numbers_from_file("search_set2_data_3.txt")
    # TODO: Read all "Search data files" separately in sequential order

    starts1d1 = datetime.now()
    for value in search_set1_data_1:
        st.search(value)
    ends1d1 = datetime.now()
    durations1d1 = ends1d1 - starts1d1
    height1 = st.height()

    starts1d2 = datetime.now()
    for value in search_set1_data_2:
        st.search(value)
    ends1d2 = datetime.now()
    durations1d2 = ends1d2 - starts1d2
    height2 = st.height()


    starts1d3 = datetime.now()
    for value in search_set1_data_3:
        st.search(value)
    ends1d3 = datetime.now()
    durations1d3 = ends1d3 - starts1d3
    height3 = st.height()


    starts2d1 = datetime.now()
    for value in search_set2_data_1:
        st.search(value)
    ends2d1 = datetime.now()
    durations2d1 = ends2d1 - starts2d1
    height4 = st.height()


    starts2d2 = datetime.now()
    for value in search_set2_data_2:
        st.search(value)
    ends2d2 = datetime.now()
    durations2d2 = ends2d2 - starts2d2
    height5 = st.height()


    starts2d3 = datetime.now()
    for value in search_set2_data_3:
        st.search(value)
    ends2d3 = datetime.now()
    durations2d3 = ends2d3 - starts2d3
    height6 = st.height()

    
    print("Insert Set1 Data1 ", durations1d1.microseconds)
    print("Height Set1 Data1 ", height1)
    print("----------------------------------------------")
    print("Insert Set1 Data2 ", durations1d2.microseconds)
    print("Height Set1 Data2 ", height2)
    print("----------------------------------------------")
    print("Insert Set1 Data3 ", durations1d3.microseconds)
    print("Height Set1 Data3 ", height3)
    print("----------------------------------------------")
    print("Insert Set2 Data1 ", durations2d1.microseconds)
    print("Height Set2 Data1 ", height4)
    print("----------------------------------------------")
    print("Insert Set2 Data2 ", durations2d2.microseconds)
    print("Height Set2 Data2 ", height5)
    print("----------------------------------------------")
    print("Insert Set2 Data3 ", durations2d3.microseconds)
    print("Height Set2 Data3 ", height6)

    return [durations1d1.microseconds,durations1d2.microseconds,durations1d3.microseconds,durations2d1.microseconds,durations2d2.microseconds,durations2d3.microseconds]



def bst_delete():
    # We must insert data before doing any operation
    bst_insert() # Please ignore the time measurement of this data insertion
    
    print("--------------------------------Delete Begins--------------------")


    def read_numbers_from_file(filename):
        numbers = []
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to an integer and add to the list
                numbers.append(int(line.strip()))
        return numbers
    
    delete_set1_data_2 = read_numbers_from_file("delete_set1_data_2.txt")
    delete_set1_data_3 = read_numbers_from_file("delete_set1_data_3.txt")
    delete_set2_data_1 = read_numbers_from_file("delete_set2_data_1.txt")
    delete_set2_data_2 = read_numbers_from_file("delete_set2_data_2.txt")
    delete_set2_data_3 = read_numbers_from_file("delete_set2_data_3.txt")
    delete_set1_data_1 = read_numbers_from_file("delete_set1_data_1.txt")



    starts1d1 = datetime.now()
    for value in delete_set1_data_1:
        st.delete(value)
    ends1d1 = datetime.now()
    durations1d1 = ends1d1 - starts1d1
    height1 = st.height()


    starts1d2 = datetime.now()
    for value in delete_set1_data_2:
        st.delete(value)
    ends1d2 = datetime.now()
    durations1d2 = ends1d2 - starts1d2
    height2 = st.height()


    starts1d3 = datetime.now()
    for value in delete_set1_data_3:
        st.delete(value)
    ends1d3 = datetime.now()
    durations1d3 = ends1d3 - starts1d3
    height3 = st.height()


    starts2d1 = datetime.now()
    for value in delete_set2_data_1:
        st.delete(value)
    ends2d1 = datetime.now()
    durations2d1 = ends2d1 - starts2d1
    height4 = st.height()


    starts2d2 = datetime.now()
    for value in delete_set2_data_2:
        st.delete(value)
    ends2d2 = datetime.now()
    durations2d2 = ends2d2 - starts2d2
    height5 = st.height()


    starts2d3 = datetime.now()
    for value in delete_set2_data_3:
        st.delete(value)
    ends2d3 = datetime.now()
    durations2d3 = ends2d3 - starts2d3
    height6 = st.height()



    print("Insert Set1 Data1 ", durations1d1.microseconds)
    print("Height Set1 Data1 ", height1)
    print("----------------------------------------------")
    print("Insert Set1 Data2 ", durations1d2.microseconds)
    print("Height Set1 Data2 ", height2)
    print("----------------------------------------------")
    print("Insert Set1 Data3 ", durations1d3.microseconds)
    print("Height Set1 Data3 ", height3)
    print("----------------------------------------------")
    print("Insert Set2 Data1 ", durations2d1.microseconds)
    print("Height Set2 Data1 ", height4)
    print("----------------------------------------------")
    print("Insert Set2 Data2 ", durations2d2.microseconds)
    print("Height Set2 Data2 ", height5)
    print("----------------------------------------------")
    print("Insert Set2 Data3 ", durations2d3.microseconds)
    print("Height Set2 Data3 ", height6)



    return [durations1d1.microseconds,durations1d2.microseconds,durations1d3.microseconds,durations2d1.microseconds,durations2d2.microseconds,durations2d3.microseconds]



def main():
    # Create the root of the BST
    # print(bst_insert())
    # print(bst_search())
    print(bst_delete())


if __name__ == "__main__":
    main()