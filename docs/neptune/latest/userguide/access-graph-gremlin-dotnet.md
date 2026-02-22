# Using .NET to connect to a Neptune DB

instance

###### Important

Choosing the correct Apache TinkerPop Gremlin driver version is critical for compatibility
with your Neptune engine version. Using an incompatible version can result in connection
failures or unexpected behavior. For detailed version compatibility information, see
[Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

The following section contains a code example written in C# that connects to a
Neptune DB instance and performs a Gremlin traversal.

Connections to Amazon Neptune must be from an Amazon EC2 instance in the same virtual private
cloud (VPC) as your Neptune DB instance. This sample code was tested on an Amazon EC2 instance running
Ubuntu.

Before you begin, do the following:

- Install .NET on the Amazon EC2 instance. To get instructions for installing .NET on
  multiple operating systems, including Windows, Linux, and macOS, see [Get Started with
  .NET](https://www.microsoft.com/net/learn/get-started/ "https://www.microsoft.com/net/learn/get-started/").
- Install Gremlin.NET by running `dotnet add package gremlin.net` for your
  package. For more information, see [Gremlin.NET](https://tinkerpop.apache.org/docs/current/reference/#gremlin-DotNet "https://tinkerpop.apache.org/docs/current/reference/#gremlin-DotNet") in the TinkerPop documentation.

###### To connect to Neptune using Gremlin.NET

1. Create a new .NET project.

```
dotnet new console -o gremlinExample
```

2. Change directories into the new project directory.

```
cd gremlinExample
```

3. Copy the following into the `Program.cs` file. Replace
   `your-neptune-endpoint` with the address of your
   Neptune DB instance.

For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

```
using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using Gremlin.Net;
using Gremlin.Net.Driver;
using Gremlin.Net.Driver.Remote;
using Gremlin.Net.Structure;
using static Gremlin.Net.Process.Traversal.AnonymousTraversalSource;
namespace gremlinExample
{
  class Program
  {
    static void Main(string[] args)
    {
      try
      {
        var endpoint = "your-neptune-endpoint";
        // This uses the default Neptune and Gremlin port, 8182
        var gremlinServer = new GremlinServer(endpoint, 8182, enableSsl: true );
        var gremlinClient = new GremlinClient(gremlinServer);
        var remoteConnection = new DriverRemoteConnection(gremlinClient, "g");
        var g = Traversal().WithRemote(remoteConnection);
        g.AddV("Person").Property("Name", "Justin").Iterate();
        g.AddV("Custom Label").Property("name", "Custom id vertex 1").Iterate();
        g.AddV("Custom Label").Property("name", "Custom id vertex 2").Iterate();
        var output = g.V().Limit<Vertex>(3).ToList();
        foreach(var item in output) {
            Console.WriteLine(item);
        }
      }
      catch (Exception e)
      {
          Console.WriteLine("{0}", e);
      }
    }
  }
}
```

4. Enter the following command to run the sample:

```
dotnet run
```

The Gremlin query at the end of this example returns the count of a single vertex for
testing purposes. It is then printed to the console.

###### Note

The final part of the Gremlin query, `Next()`, is required to submit the
traversal to the server for evaluation. If you don't include that method or another
equivalent method, the query is not submitted to the Neptune DB instance.

The following methods submit the query to the Neptune DB instance:

    * `ToList()`
    * `ToSet()`
    * `Next()`
    * `NextTraverser()`
    * `Iterate()`

Use `Next()` if you need the query results to be serialized and
returned, or `Iterate()` if you don't.

The preceding example returns a list by using the `g.V().Limit(3).ToList()`
traversal. To query for something else, replace it with another Gremlin traversal with
one of the appropriate ending methods.
