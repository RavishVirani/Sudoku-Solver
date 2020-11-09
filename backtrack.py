from Cell import Cell
from copy import deepcopy


def backtracking_search(board):
    unassigned = {}
    indices = []
    tried ={}
    
    #Put all the remaining cells in the CSP into these structures    
    for i,j in board.items():
        if len(j.domain)>1:
            unassigned[i] = Cell(i,".")
            unassigned[i].domain = j.domain.copy()
            indices.append(i)
            tried[i]=[]
    for i,j in unassigned.items():
        unassigned[i].relations = remove_relations(unassigned[i].relations,indices)


    order = []
    i = 0
    other_dict = deepcopy(unassigned)
    temp = {key:val for key,val in sorted(other_dict.items(),key = sorting_key)}
    
    #Backtrack search for a valid solution.
    #Uses the Minimum Remaining Values, Degree, and the Least Constraining Value heuristics
    while i>=0 and i<len(indices):
        #Check the best variable to choose
        first_key = next(iter(temp))
        first_value = best_value(first_key,temp)

        #If there are no valid domain values
        if first_value==0:
            if len(order)==0:
                print("Impossible Puzzle")
                return

            #Backtrack one cell and variable pair
            old_key,old_value = order.pop()

            #Reset the current tried values and add the backtracked value into the tried values
            tried[first_key] = []
            tried[old_key].append(old_value)

            #Add the backtracked index back into the CSP and reset the domain of the current variable
            temp = add_pair(old_key,old_value,temp,unassigned,order,tried)
            temp[first_key].domain = restore_domain(first_key,order,unassigned)            
            i-=1
        else:
            #Add the current best value and cell pair into the history, remove the value from affected cells and remove the chosen cell from the CSP
            order.append([first_key,first_value])
            temp = remove_pair(first_key,first_value,temp)
            del temp[first_key]
            i+=1
        #Sort the remaining values to find the next best value to choose
        temp = {key:val for key,val in sorted(temp.items(),key = sorting_key)}
        
    #Set the variables chosen from backtracking to the main board
    for i,j in order:
        board[i].domain = [j]
        
    return board

def smallest_domain(cell):
    return len(cell.domain)

def most_constraints(cell):
    return -len(cell.relations)

def sorting_key(item):
    return (smallest_domain(item[1]),most_constraints(item[1]))

def remove_relations(relations,unassigned):
    return [index for index in relations if index in unassigned]

def best_value(cell,unassigned):
    count = -1
    best = 0
    for value in unassigned[cell].domain:
        temp = count_constraints(cell,value,unassigned)
        if count==-1 or temp<count:
            best = value
    return best

def count_constraints(cell,value,unassigned):
    count = 0
    for related in unassigned[cell].relations:
        if value in unassigned[related].domain:
            count+=1
    return count

def remove_pair(index,value,temp):
    for i,j in temp.items():
        if index in j.relations:
            j.relations.remove(index)
            if value in j.domain:
                j.domain.remove(value)
    return temp
    
def add_pair(index,value,temp,unassigned,order,tried):
    domain_want = []
    for i,j in temp.items():
        if index in unassigned[i].relations:
            j.relations.append(index)
            if value in unassigned[i].domain:
                domain_want.append(i)

    #restore the value to the cells that should have it if index was the only one constraining it
    for wanting in domain_want:
        give = True
        for history in order:
            if history[0] in unassigned[wanting].relations:
                if history[1]==value:
                    give = False
                    break
        if give:
            temp[wanting].domain.append(value)


    #restore the index back into the unassigned dictionary
    temp[index] = Cell(index,".")
    temp[index].domain = [val for val in unassigned[index].domain]
    
    for history in order:
        if history[0] in temp[index].relations:
            if history[1] in temp[index].domain:
                temp[index].domain.remove(history[1])
                
    for already in tried[index]:
        if already in temp[index].domain:
            temp[index].domain.remove(already)
    temp[index].relations = [relate for relate in unassigned[index].relations if relate in temp.keys()]
    return temp
    
def restore_domain(index,order,unassigned):
    temp = [val for val in unassigned[index].domain]
    for history in order:
        if history[0] in unassigned[index].relations:
            if history[1] in temp:
                temp.remove(history[1])
    return temp
    
