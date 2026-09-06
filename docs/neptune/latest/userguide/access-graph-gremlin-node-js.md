

# Using Node.js to connect to a Neptune DB instance
<a name="access-graph-gremlin-node-js"></a>

**Important**  
Choosing the correct Apache TinkerPop Gremlin driver version is critical for compatibility with your Neptune engine version. Using an incompatible version can result in connection failures or unexpected behavior. For detailed version compatibility information, see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md).

The following section walks you through the running of a Node.js sample that connects to an Amazon Neptune DB instance and performs a Gremlin traversal.

You must follow these instructions from an Amazon EC2 instance in the same virtual private cloud (VPC) as your Neptune DB instance.

Before you begin, do the following:
+ Verify that Node.js version 8.11 or higher is installed. If it is not, download and install Node.js from the [Nodejs.org website](https://nodejs.org).

**To connect to Neptune using Node.js**

1. Enter the following to install the `gremlin-javascript` package:

   ```
   npm install gremlin
   ```

1. Create a file named `gremlinexample.js` and open it in a text editor.

1. Copy the following into the `gremlinexample.js` file. Replace {{your-neptune-endpoint}} with the address of your Neptune DB instance.

   For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md) section.

   ```
   const gremlin = require('gremlin');
   const DriverRemoteConnection = gremlin.driver.DriverRemoteConnection;
   const Graph = gremlin.structure.Graph;
   
   dc = new DriverRemoteConnection('wss://{{your-neptune-endpoint}}:8182/gremlin',{});
   
   const graph = new Graph();
   const g = graph.traversal().withRemote(dc);
   
   g.V().limit(1).count().next().
       then(data => {
           console.log(data);
           dc.close();
       }).catch(error => {
           console.log('ERROR', error);
           dc.close();
       });
   ```

1. Enter the following command to run the sample:

   ```
   node gremlinexample.js
   ```

The preceding example returns the count of a single vertex in the graph by using the `g.V().limit(1).count().next()` traversal. To query for something else, replace it with another Gremlin traversal with one of the appropriate ending methods.

**Note**  
The final part of the Gremlin query, `next()`, is required to submit the traversal to the server for evaluation. If you don't include that method or another equivalent method, the query is not submitted to the Neptune DB instance.

The following are examples of methods that submit the query to the Neptune DB instance:
+ `toList()`
+ `toSet()`
+ `next()`
+ `iterate()`

These terminal steps behave differently in script mode and bytecode mode. For the canonical list of terminal steps and details about how they affect transactions, see [Test Gremlin code in the context where you will deploy it](best-practices-gremlin-console-glv-differences.md).

Use `iterate()` when you don't need the results of your queries (e.g. mutations) as it saves serialization costs.

**Important**  
This is a standalone Node.js example. If you are planning to run code like this in an AWS Lambda function, see [Lambda function examples](lambda-functions-examples.md) for details about using JavaScript efficiently in a Neptune Lambda function.

## IAM authentication
<a name="access-graph-gremlin-nodejs-iam"></a>

Neptune supports [IAM authentication](iam-auth-enable.md) to control access to your DB cluster. If you have IAM authentication enabled, you need to use Signature Version 4 signing to authenticate your requests. For detailed instructions and code examples for connecting from a JavaScript client, see [Connecting to Amazon Neptune databases using IAM authentication with Gremlin JavaScript](gremlin-javascript-iam-auth.md).