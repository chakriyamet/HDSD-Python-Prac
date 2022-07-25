from turtle import window_height


class graph:
    def __init__(self, num_of_nodes):
        self .m_num_of_nodes = num_of_nodes
        self .m_graph = [[0 for column in range (num_of_nodes)] 
                         for row in range(num_of_nodes)]  #9 column n 9 rows
        
    def add_edge(self, node1, node2, weight):
        self .m_graph[node1][node2] = weight
        self .m_graph[node2][node1] = weight
        
    def prims_mst(self):
        postitive_inf = float('inf')
        selected_nodes = [False for node in range(self .m_num_of_nodes)]
        result = [[0 for column in range(self .m_num_of_nodes)] 
                  for row in range(self .m_num_of_nodes)]
        
        indx = 0
        for i in range(self .m_num_of_nodes):
            print(self .m_graph[i])
            
        print(selected_nodes)
        
        while(False is selected_nodes):
            minimum = postitive_inf
            start = 0
            end = 0
            
            for i in range(self .m_num_of_nodes):
                if selected_nodes[i]:
                    for j in range(self .m_num_of_nodes):
                        if (not selected_nodes[j] and self .m_graph[i][j]>0):
                            if self .m_graph[i][j] < minimum:
                                minimum = self .m_graph[i][j]
                                start, end = i, j
            selected_nodes[end] = True
            result[start][end] = minimum
            
            if minimum == postitive_inf:
                result[start][end] = 0
                
            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            
            result[end][start] = result[start][end]
            
        for i in range(len(result)):
            for j in range (0+i, len(result)):
                if result[i][j] !=0:
                    print("%d = %d: %d" % (i, j, result[i][j]))
                    
#Example graph has 11 nodes
example_graph = graph(11)

example_graph.add_edge(1, 2, 30)
example_graph.add_edge(1, 4, 40)
example_graph.add_edge(2, 3, 50)
example_graph.add_edge(7, 4, 50)
example_graph.add_edge(4, 5, 30)
example_graph.add_edge(7, 5, 45)
example_graph.add_edge(7, 6, 50)
example_graph.add_edge(3, 5, 35)
example_graph.add_edge(5, 3, 40)
example_graph.add_edge(5, 6, 35)
example_graph.add_edge(6, 5, 25)

example_graph.prims_mst()



                    
            
        
        