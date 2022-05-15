#include<bits/stdc++.h>
using namespace std;

// Data structure to store a graph edge
struct Edge {
    int src, dest;
};
 
// A class to represent a graph object
class Graph
{
public:
    // a vector of vectors to represent an adjacency list
    vector<vector<int>> adjList;
 
    // Graph Constructor
    Graph(vector<Edge> const &edges, int n)
    {
        // resize the vector to hold `n` elements of type `vector<int>`
        adjList.resize(n);
 
        // add edges to the undirected graph
        for (auto &edge: edges)
        {
            adjList[edge.src].push_back(edge.dest);
            adjList[edge.dest].push_back(edge.src);
        }
    }
};

// Perform BFS on the graph starting from vertex `v`
void BFS(Graph const &graph, int v, vector<bool> &discovered)
{
    // create a queue for doing BFS
    queue<int> q;
 
    // mark the source vertex as discovered
    discovered[v] = true;
 
    // enqueue source vertex
    q.push(v);
 
    // loop till queue is empty
    while (!q.empty())
    {
        // dequeue front node and print it
        v = q.front();
        q.pop();
        cout << v << " ";
 
        // do for every edge (v, u)
        for (int u: graph.adjList[v])
        {
            if (!discovered[u])
            {
                // mark it as discovered and enqueue it
                discovered[u] = true;
                q.push(u);
            }
        }
    }
}


void DFS(Graph const &graph, int v, vector<bool> &discovered)
{

    discovered[v] = true;
    cout << v << " ";

    // vector<int> ::iterator i;

    for (int i = 0; i < graph.adjList[v].size(); i++)
    {
        if (!discovered[graph.adjList[v][i]])
            DFS(graph,graph.adjList[v][i],discovered);
    }
        

}

int main()
{
    // vector of graph edges as per the above diagram
    vector<Edge> edges ;
 
    cout<<"Enter the number of nodes: ";
    int n;
    cin>>n;
 
    // to keep track of whether a vertex is discovered or not
    vector<bool> discovered(n+1, false);
    
    int edge_no;
    cout<<"Enter total no. of edges: ";
    cin>>edge_no;
    for(int i=0;i<edge_no;i++)
    {
        int src,dest;
        cout<<"Enter source and destination: ";
        cin>>src>>dest;
        edges.push_back({src,dest});
    }

    // build a graph from the given edges
    Graph graph(edges, n);

    int choice;
    int start;

    while (1)
    {
        cout<<"Enter a choice:\n1) BFS\n2) DFS\n3) Exit\n";
        cin>>choice;
    
        switch(choice)
        {
            case 1:
                for(int i=0;i<n;i++)
                {
                    discovered[i] = false;
                }
                
                for (int i = 0; i < n; i++)
                {
                    if (discovered[i] == false)
                    {
                        // start BFS traversal from vertex `i`
                        BFS(graph, i, discovered);
                    }
                }

                cout<<endl;
                break;

            case 2:
                for(int i=0;i<n;i++)
                {
                    discovered[i] = false;
                }
                cout<<"Enter node from which you wish to start DFS: ";
                cin>>start;
                DFS(graph, start, discovered);
                for (int i = 0; i < n; i++)
                {
                    if (discovered[i] == false)
                    {
                        // start DFS traversal from vertex `i`
                        DFS(graph, start, discovered);
                    }
                }

                cout<<endl;
                break;
            
            case 3: 
                return 0;
                break;

            default:
                cout<<"Invalid choice";
        }
    }

    return 0;

}