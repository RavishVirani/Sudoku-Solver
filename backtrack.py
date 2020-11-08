# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:33:14 2020

@author: Karan Grewal
"""

def backtracking_search(csp, board):
    return backtrack({},csp, board)

def backtrack(assignment,csp, board):
    
    #check if assignemnt is complete
    if len(assignment) == len(csp):
        return assignment
    
    #selects unassigned variable
    var = select_unassigned_variable(assignment, csp, board)
    
    
    for value in order_domain_values(var,assignment,csp, board):
        
        
        if is_consistent(value,assignment, board):
            
            #add {cell = value} to assignment
            assignment[var] = value
            
            #forward checking
            inferences = inference(csp,var,value,assignment,board)
            
            
            if inferences != []:
                for i in inferences:
                    assignment.add(i)
                result = backtrack(assignment, csp, board)
                
                if result != -1:
                    return result
        assignment.remove(value)
        for k in inferences:
            assignment.remove(k)
    return -1

#selects an unsassigned variable
def select_unassigned_variable(assignment, csp, board):
    unassigned = []
    
    # for each cell
    for cell in csp:
        
        #if it is not assinged
        if cell not in assignment:
            
            #add to unassigned list
            unassigned.append(cell)
            
    #uses MCV heuristic to find next best unassigned variable
    criteria = lambda cell: len(board[cell].domain)
    
    return min(unassigned, key=criteria)


#function to find LCV
def order_domain_values(var, assignment, csp, board):
    if len(board[var].domain) == 1:
        return board[var]
    
    criteria = lambda value: numConflict(csp,var,value, board)
    return sorted(board[var].domain, key=criteria)
    

#counts number of conflicts and returns count
def numConflict(csp,var,value, board):
    count=0
    
    for relate in board[var].relatations:
        if len(board[relate].domain) > 1 and value in board[relate].relations:
            count += 1
    return count


#check to see if consistent
def is_consistent(value,assignment, board):
    is_consistent = True
    
    for current_cell, current_value in board.items():
        
        #if values are same and cells are related, function no longer consistent
        if current_value == value and current_cell in board[current_cell].relations:
            is_consistent = False
    return is_consistent


#forward check to reduce domain if possible
def inference(csp,var, value, assignment, board):
    
    inferences = []
    #for each related cell of var
    for relatedc in csp[var]:
        
        #if this cell is not in assignment
        if relatedc not in assignment:
            
            #and if this value remains possible
            if value in board[relatedc].domain:
                
                #add to list of inferences
                inferences.append(value)
                #remove it from possibilities
                board[relatedc].domain.remove(value)
                
    return inferences