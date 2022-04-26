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

def update_parents(graph, parents):
    for g_node in graph:
        for gg_node in graph[g_node]:
            parents[gg_node] = g_node
    return parents

def update_costs(graph,parents,costs):
    for p_node in parents:
        costs[p_node] = float('inf')
    search_node = 'start'
    costs['start'] = 0
    while True:
        for s_node in parents:
            if search_node == parents[s_node]:
                costs[s_node] = graph[search_node][s_node] + costs[search_node]
                search_node = s_node
        if costs['fin'] != float('inf'):
            break

    return costs

graph = {'start':{'A':5,'B':2},'A':{'C':4,'D':2},'B':{'A':8,'D':7},'C':{'D':6,'fin':3},'D':{'fin':1},'fin':{}}
parents = {}
update_parents(graph,parents)
costs = {}
update_costs(graph,parents,costs)
print(costs,'\n',parents,'\n')

processed = ['start']
lowest_cost_to_fin(graph,costs,parents,processed)
print(costs,'\n',parents)