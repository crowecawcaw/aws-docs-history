# Using Node.js to connect to a Neptune DB

instance

###### Important

Choosing the correct Apache TinkerPop Gremlin driver version is critical for compatibility
with your Neptune engine version. Using an incompatible version can result in connection
failures or unexpected behavior. For detailed version compatibility information, see
[Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

The following section walks you through the running of a Node.js sample that connects to
an Amazon Neptune DB instance and performs a Gremlin traversal.

You must follow these instructions from an Amazon EC2 instance in the same virtual private
cloud (VPC) as your Neptune DB instance.

Before you begin, do the following:

- Verify that Node.js version 8.11 or higher is installed. If it is not, download and
  install Node.js from the [Nodejs.org website](https://nodejs.org "https://nodejs.org").

###### To connect to Neptune using Node.js

1. Enter the following to install the `gremlin-javascript` package:

```
npm install gremlin
```

2. Create a file named `gremlinexample.js` and open it in a text
   editor.
3. Copy the following into the `gremlinexample.js` file. Replace
   `your-neptune-endpoint` with the address of your
   Neptune DB instance.

For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

```
const gremlin = require('gremlin');
const DriverRemoteConnection = gremlin.driver.DriverRemoteConnection;
const Graph = gremlin.structure.Graph;

dc = new DriverRemoteConnection('wss://`your-neptune-endpoint`:8182/gremlin',{});

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

4. Enter the following command to run the sample:

```
node gremlinexample.js
```

The preceding example returns the count of a single vertex in the graph by using the
`g.V().limit(1).count().next()` traversal. To query for something else, replace it
with another Gremlin traversal with one of the appropriate ending methods.

###### Note

The final part of the Gremlin query, `next()`, is required to submit the
traversal to the server for evaluation. If you don't include that method or another
equivalent method, the query is not submitted to the Neptune DB instance.

The following methods submit the query to the Neptune DB instance:

- `toList()`
- `toSet()`
- `next()`
- `nextTraverser()`
- `iterate()`
  Use `next()` if you need the query results to be serialized and
  returned, or `iterate()` if you don't.

###### Important

This is a standalone Node.js example. If you are planning to run code
like this in an AWS Lambda function, see [Lambda function examples](lambda-functions-examples.md "lambda-functions-examples.md") for details about using
JavaScript efficiently in a Neptune Lambda function.
