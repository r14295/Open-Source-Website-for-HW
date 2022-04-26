def find_lowest_cost_node(costs,processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node_not_in_processed(processed,node):
            lowest_cost = cost
            lowest_cost_node = node
    #print(lowest_cost_node)
    return lowest_cost_node

def node_not_in_processed(processed,node):
    for node_processed in processed:
        if node == node_processed:
            return False
    return True

def lowest_cost_to_fin(graph,costs,parents,processed):
    lowest_cost_node = find_lowest_cost_node(costs,processed)
    while lowest_cost_node != None:
        cost = costs[lowest_cost_node]
        neighbors = graph[lowest_cost_node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = lowest_cost_node
        processed.append(lowest_cost_node)
        lowest_cost_node = find_lowest_cost_node(costs,processed)
    return costs,parents

def creat_parents(graph, parents):
    for g_node in graph:
        for gg_node in graph[g_node]:
            parents[gg_node] = None
    return parents

def creat_costs(parents,costs):
    for p_node in parents:
        costs[p_node] = float('inf')
    return costs

graph = {'start':{'A':1,'B':2,'C':1},
         'A':{'D':3,'E':4},
         'B':{'A':2,'E':6},
         'C':{'E':8,'F':2},
         'D':{'G':7},
         'E':{'G':6,'H':8,'J':5},
         'F':{'J':3},
         'G':{'H':2,'fin':9},
         'H':{'fin':1},
         'J':{'fin':2},
         'fin':{}
         }
parents = {}
creat_parents(graph,parents)
costs = {}
creat_costs(parents,costs)

costs['A'] = 1
costs['B'] = 2
costs['C'] = 1
parents['A'] = 'start'
parents['B'] = 'start'
parents['C'] = 'start'
print('costs:',costs,'\n','parents:',parents,'\n')
processed = ['start']
lowest_cost_to_fin(graph,costs,parents,processed)
print('costs:',costs,'\n','parents:',parents,'\n')