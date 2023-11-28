# Get ID | Title | Description and link test cases through VectorCast API

# ---------------------------- IMPORTS ------------------------- # 
# Common Libs
import sys, os

# Data handling dependencies
import pandas as pd
import numpy as np

# Dataclasses dependencies
from dataclasses import dataclass
from typing import List, Tuple

# ----------------------------------------------------------------------- #
# GLOBAL CONSTANTS

BASE_PATH:str = 
EXAMPLE_TST:str = 

# OTHER CONSTANTS
tested_fct_identifier:str = "**test.fct" # We will use this str to check for the name of function
# within .c file
testcase_identifier:str = "TestCase."

# ----------------------------------------------------------------------- #

def api_command(*args):
    pass

@dataclass (init=True, repr=True)
class TestedFunction:

    name: str
    id:int = 0
    c_file: str = ""
    test_cases = []

    def __init__(self, line:str, id:int=0)->None:
        # get test case name alone
        """ Initialise Name and ID for this TestedFunction """
        self.name = line.split(':', maxsplit=1)[-1].strip(" ")
        self.id = id
        self.c_file = ""
        self.test_cases = []

    def __del__(self):
        """ This calls when the object is destroyed (cleaned up) """
        print(f"Destroying TestedFunction Object: {self.name}")

    def collect_test(self, case:str)->None:
        """ Add test cases to list """
        res = case.split(".", maxsplit=1)[-1]
        self.test_cases.append(res)

    def info(self)->None:
        """ Print info contained in this TestedFunction """
        
        print(f"[Name: {self.name} | ID: {self.id}]")
        print(f"[{self.name}->Test Cases: {self.test_cases}]")

    def link(self)->None:
        """ Uses its relevant data to link test-cases in VC """
        for test in self.test_cases:
            # For each test case we link it individually
            api_command(self.name, self.id, test)
        
    def destroy(self)->None:
        del self

# CLASS tested_fct END - ----------------------------------------------------------------------- #


@dataclass (init=True, repr=True)
class LinkHandler:

    CSV_folder_path: str = ""
    CSV_name: str = ""
    CSV_full_path: str = ""
    table_data = []
    current_file = []
    sub_list = []

    def __init__(self, path:str)->None:
        """ Get the path to CSV File """
        temp = path.replace('\\', '/').split("/", maxsplit=-1)
        self.CSV_full_path = path
        self.CSV_name = temp[-1]
        self.CSV_folder_path = self.CSV_full_path.strip(self.CSV_name)
        self.sub_list = []
    
    @property
    def table_data(self)->list:
        """ Imports table using PD and the path variable. """
        temp = pd.read_csv(self.CSV_full_path)
        t2 = pd.DataFrame(temp)
        return t2

    def get_row_data(self, index=1)->List:
        """ Get ID and Title of Function at specific Row Index """
        my_id, my_title, my_desc = self.table_data.iloc[index]
        my_desc = ""
        return my_id, my_title

    def make_subpro(self, line:str, id:int=0):
        return TestedFunction(line, id)

    def open_tst(self, file):
        """ Open a text file and return it as array """
        text_file = open(file, "r")
        self.current_file = text_file.read().splitlines()
        text_file.close()

    def iterate_rows(self, stop_condition:str, collect:str, start_index:str=0)->List:
        """ Iterate until specific string has been reached """
        i = start_index
        cur_line:str = self.current_file[i]
        collection_list = []
        while not (stop_condition in cur_line):
            if collect in cur_line:
                collection_list.append(cur_line)
            cur_line = self.current_file[i]
            i+=1
            pass

    def link_tested_fct(self, sub:TestedFunction)->None:
        """ Get object of type TestedFunction and link it to Vectorcast via API """
        print(f"Linking tested_fct with name: {sub.name} and id: {sub.id}")
        #TODO
        pass

    def console_input(self, setting="path")->str:
        """ Set path and settings by console input """

        if setting.lower() == "path":
            if BASE_PATH == "":
                self.CSV_folder_path = input("!--| Enter path of folder here: \t")
                self.CSV_name = input("!--| Enter name of CSV here: \t") + ".csv"
                self.CSV_full_path = self.CSV_folder_path + '/' + self.CSV_name
                print("\n")
            else:
                self.CSV_full_path = BASE_PATH

    def info(self)->None:
        #print(f"{self.CSV_full_path}\n")
        print(self.CSV_full_path)
        print(f"{self.CSV_name=} {self.CSV_folder_path=}")
        print(f"Data at Index= 0{self.get_row_data(0)}")
        pass

    def info_data(self)->None:
        print(f"\tComplete Data in File: \n{self.table_data}")
        pass

    def child_info(self)->None:
        """ Returns info of the tested_fcts """
        for child in self.sub_list:
            child.info()

    def for_test_file(self):
        # for every test file
        # go through test file, create tested_fct Objects for each function inside
        in_tested_fct:bool = False # Checks to see if currently iterating within a TestedFunction
        self.open_tst(EXAMPLE_TST)
        curObj: TestedFunction = None
        for line in self.current_file:
            if (in_tested_fct == True):
                if testcase_identifier in line:
                    # We found a test case and will add it to the
                    # tested_fct (object) array
                    curObj.collect_test(line)
                if tested_fct_identifier in line:
                    # If we find another tested_fct while still in one, 
                    # it means we should switch to the other
                    in_tested_fct = False

            if (tested_fct_identifier in line) and (in_tested_fct==False):
                # We have left the old Subp and found a new one
                self.sub_list.append(self.make_subpro(line))
                curObj = self.sub_list[-1]
                in_tested_fct = True
        # for each tested_fct object, link test case and ID to API

        #TODO: cleanup & split this method

# CLASS LINKHANDLER END - ---------------------------------------------------------------------- #



def main():
    my_handler = LinkHandler(BASE_PATH)
    my_handler.for_test_file()
    my_handler.child_info()


# --------------------------------------- # 
if __name__ == "__main__":
    main()
    
