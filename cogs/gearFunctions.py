#Functions to use with blackDesert.py to log gear entries for Yukii

#Functions to use with blackDesert.py to log gear entries for Yukii

import openpyxl as op
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet as ws
from openpyxl.writer.excel import save_workbook
from openpyxl.workbook import Workbook as WB
import os

FILE = os.environ.get("DATABASE")
wb = load_workbook(FILE)
c = wb["Guild Gear Sheet"]

def check_if_exists(userid):
	"""
    Searches through the first column of the sheet where the userid would be
    and returns whether the user with the given ID is in the file or not.
    Returns: bool
    """

	VALS = get_list()
	searchVar = str(userid)
	if searchVar not in VALS:
		new_user(userid)
	elif searchVar in VALS:
		pass

def get_list():
    """
    Enters every value in column A into a list
    Returns: list
    """

    VALUES = []
    for cell in c['A']:
        try:
            VALUES.append(str(cell.value))
        except:
            pass
    return VALUES

def new_user(userid):
    """
    Adds a new row to the bottom of column A with the specified value
    """
    rownum = len(c['A']) + 1
    c[f'A{rownum}'] = str(userid)
    WB.save(wb, FILE)

def set_value(userid, item:str, entry):
    """
    Set cell value
    Uses names to associate with columns for ease of use;
    names can be edited by changing values of colval
    userid-- row index
    item:str-- column
    """
    try:
        row = 0
        idx = ''
        
        colval = ['FN', 'CLASS', 'AP', 'AAP', 'DP', 'GS']
        colidx = ['B', 'C', 'D', 'E', 'F', 'G']
        col = zip(colval, colidx)

        ctrl = False

        while ctrl == False:
            for cell in c['A']:
                if cell.value == None:
                    pass
                elif str(cell.value) == f'{userid}':
                    row = cell.row
                    ctrl = True
                else:
                    ctrl = False
        for val, indx in col:
            if val == item:
                idx = indx
                
        c[f'{idx}{row}'] = entry
        
        WB.save(wb, FILE)
    except:
        import traceback
        traceback.print_exc()

def set_char(userid, index:str, entry):
    """
    Sets all the cell values associated with character info
    """
    try:
        row = 0
        idx = index
        ctrl = False

        while ctrl == False:
            for cell in c['A']:
                if cell.value == None:
                    pass
                elif str(cell.value) == f'{userid}':
                    row = cell.row
                    ctrl = True
                else:
                    ctrl = False
                        
        c[f'{idx}{row}'] = entry

        WB.save(wb, FILE)
    except:
        import traceback
        traceback.print_exc()

def new_char(userid, FN, CLASS, AP:int, AAP:int, DP:int, GS:int):
    """
    Adds character information for a user
    """
    check_if_exists(userid)

    colval = ['FN', 'CLASS', 'AP', 'AAP', 'DP', 'GS']
    colidx = ['B', 'C', 'D', 'E', 'F', 'G']
    entries = [FN, CLASS, AP, AAP, DP, GS]
    col = zip(colval, colidx, entries)

    for val, idx, entry in col:
        set_char(userid, str(idx), str(entry))

    WB.save(wb, FILE)

def get_val(userid, item:str):
    """
    Returns the item searched for using userid as the row index parameter
    Uses names to associate with columns for ease of use;
    names can be edited by changing values of colval
    
    Returns: string or int
    """

    colval = ['FN', 'CLASS', 'AP', 'AAP', 'DP', 'GS']
    colidx = ['B', 'C', 'D', 'E', 'F', 'G']
    col = zip(colval, colidx)

    row = 0
    idx = ''

    ctrl = False

    while ctrl == False:
        for cell in c['A']:
            if cell.value == None:
                pass
            elif str(cell.value) == f'{userid}':
                row = cell.row
                ctrl = True
            else:
                ctrl = False
    for val, indx in col:
        if val == item:
            idx = indx

    piece = c[f'{idx}{row}'].value
    return piece

def get_char(userid):
    """
    Gets the character info of a user given their id
    """
    try:
        row = 0
        idx = ''
        
        colval = ['FN', 'CLASS', 'AP', 'AAP', 'DP', 'GS']
        colidx = ['B', 'C', 'D', 'E', 'F', 'G']
        col = zip(colval, colidx)

        VALUES = []

        ctrl = False

        while ctrl == False:
            for cell in c['A']:
                if cell.value == None:
                    pass

                elif str(cell.value) == f'{userid}':
                    row = cell.row
                    ctrl = True
                else:
                    ctrl = False
        for cell in c[f'A{row}']:
            VALUES.append(cell.value)
            print("Values gathered successfully")

        return VALUES

    except:
        import traceback
        traceback.print_exc()

def calcGS(userid):
    """
    Calculates gear score as a function of ((AP + AAP)/2)+DP
    """
    AP = int(get_val(userid, "AP"))
    AAP = int(get_val(userid, "AAP"))
    DP = int(get_val(userid, "DP"))

    GS = ((AP + AAP) / 2) + DP
    set_value(userid, "GS", int(GS))