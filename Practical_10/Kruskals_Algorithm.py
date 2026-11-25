def Kruskals(V, E): 
    E.sort(key=lambda x: x[2]) 
    groups = [[v] for v in V] 
    mst = [] 
    cost = 0 
    for i, j, w in E: 
        group_i = None 
        group_j = None 
        for group in groups: 
            if i in group: 
                group_i = group 
            if j in group: 
                group_j = group 
        if group_i != group_j: 
            mst.append((i, j, w)) 
            cost += w 
            group_i.extend(group_j) 
            groups.remove(group_j) 
    return mst, cost 

if __name__ == "__main__": 
    V = ['A', 'B', 'C', 'D'] 
    E = [('A', 'B', 2), ('B', 'D', 3), ('D', 'C', 4), ('A', 'C', 1), ('C', 'B', 5)] 
    
    mst, total_cost = Kruskals(V, E)
    print("Minimum Spanning Tree:", mst)
    print("Total Cost:", total_cost)
