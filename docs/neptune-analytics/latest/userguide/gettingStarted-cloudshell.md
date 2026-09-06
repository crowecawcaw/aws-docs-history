

# Quick start using AWS CloudShell
<a name="gettingStarted-cloudshell"></a>

 You can connect to your Neptune Analytics graph with a single click through [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) directly from the AWS Management Console. CloudShell provides a pre-authenticated shell environment with the `graphsh` tool pre-installed, connecting to your graph's public endpoint. You don't need to provision notebooks to interact with the graph. 

**Time to complete:** Approximately 2 minutes

**Cost:** CloudShell is available at no additional charge. Neptune Analytics graphs incur charges based on provisioned memory. For pricing details, see [Neptune Analytics pricing](https://aws.amazon.com/neptune/pricing/).

## Prerequisites
<a name="gettingStarted-cloudshell-prereqs"></a>
+ An AWS account with appropriate IAM permissions.
+ A Neptune Analytics graph with public connectivity enabled and status **Available**. If you don't already have one, see [Create an empty Neptune graph](gettingStarted-creating-a-graph.md). When creating your graph, you must enable public connectivity.

## Step 1: Connect to your Neptune Analytics graph
<a name="gettingStarted-cloudshell-connect"></a>

 Connect to your Neptune Analytics graph using [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html). 

**Note**  
 You must enable public connectivity to connect to a Neptune Analytics graph using CloudShell. 

**To connect to your graph**

1.  In the Neptune console, in the navigation pane, choose **Graphs**. 

1.  Select the check box next to the graph that you created. 

1.  Choose **Connect to graph**. 
**Note**  
This button is active when you select a graph with **Available** status and public connectivity turned on.

    The CloudShell **Run command** screen appears. 

1.  Choose **Run** to connect to the graph. 

After you connect, the `graphsh` console appears.

## Step 2: Insert and query data
<a name="gettingStarted-cloudshell-query"></a>

 Now that you are connected to your graph, run a few queries to get familiar with Neptune Analytics. The following examples use openCypher, the query language supported by Neptune Analytics. 

**To insert nodes and relationships**  
Run the following query to create two person nodes and a relationship:

```
CREATE (a:Person {name: 'Alice', age: 30}), (b:Person {name: 'Bob', age: 40}), (a)-[:KNOWS]->(b)
```

The output looks similar to the following:

```
╭────────╮
│ result │
├────────┤
│ []     │
╰────────╯
```

**To find nodes**  
Run the following query to return all person names in alphabetical order:

```
MATCH (p:Person) RETURN p.name AS name ORDER BY name
```

The output looks similar to the following:

```
╭───────╮
│ name  │
├───────┤
│ Alice │
│ Bob   │
╰───────╯
```

**To run an algorithm**  
Run a breadth-first search (BFS) to find nodes reachable from Alice:

```
MATCH (n {name: "Alice"}) CALL neptune.algo.bfs(n, {edgeLabels: ["KNOWS"]}) YIELD node RETURN node
```

The output looks similar to the following (order might vary):

```
╭──────────────────────────────────────────────────────────────────────╮
│ node                                                                 │
├──────────────────────────────────────────────────────────────────────┤
│ (:Person {~id: "...", age: 40, name: "Bob"})                         │
│ (:Person {~id: "...", age: 30, name: "Alice"})                       │
╰──────────────────────────────────────────────────────────────────────╯
```

## Next steps
<a name="gettingStarted-cloudshell-next"></a>

 You have completed this quick start. To learn more, explore the following features: 
+ [Managing your Neptune Analytics graphs](managing.md) – Manage your graphs, endpoints, and configurations.
+ [Neptune Analytics algorithms](algorithms.md) – Run built-in graph algorithms on your data.
+ [Working with vector similarity in Neptune Analytics](vector-similarity.md) – Use vector embeddings for similarity search.

To avoid ongoing charges, delete the graph if you created it only for this quick start. For instructions, see [Managing your Neptune Analytics graphs](managing.md).