# Send queries to the server as bytecode rather than as strings

There are advantages to using bytecode rather than a string when submitting queries:

- **Catch invalid query syntax early:**  
  Using the bytecode variant lets you detect invalid query syntax at the compilation stage.
  If you use the string-based variation, you won't discover the invalid syntax
  until the query is submitted to the server and an error is returned.
- **Avoid string-based performance penalty:**  
  Any string-based query submission, whether you're using WebSockets or HTTP, results in
  a detached vertex, which implies that the Vertex object consists of the ID, Label and all
  the properties associated with the Vertex (see [Properties
  of Elements](http://tinkerpop.apache.org/docs/current/reference/#_properties_of_elements "http://tinkerpop.apache.org/docs/current/reference/#_properties_of_elements")).

This can lead to unnecessary computation on the server in cases where the properties
are not required. For example, if the customer is interested in getting the vertex with
the ID "hakuna#1" using the query, `g.V("hakuna#1")`. If the query is sent
as a string based submission, the server would spend time in retrieving the ID, label
and all properties for this vertex. If the query is sent as a bytecode submission, the
server only spends time retrieving the ID and the label of the vertex.
In other words, rather than submit a query like this:

```
  final Cluster cluster = Cluster.build("localhost")
                                 .port(8182)
                                 .maxInProcessPerConnection(32)
                                 .maxSimultaneousUsagePerConnection(32)
                                 .serializer(Serializers.GRAPHBINARY_V1D0)
                                 .create();

  try {
      final Client client = cluster.connect();
      List<Result> results = client.submit("g.V().has('name','pumba').out('friendOf').id()").all().get();
      System.out.println(verticesWithNamePumba);
  } finally {
      cluster.close();
  }
```

Instead, submit the query using bytecode, like this:

```
  final Cluster cluster = Cluster.build("localhost")
                                 .port(8182)
                                 .maxInProcessPerConnection(32)
                                 .maxSimultaneousUsagePerConnection(32)
                                 .serializer(Serializers.GRAPHBINARY_V1D0)
                                 .create();

  try {
      final GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));
      List<Object> verticesWithNamePumba = g.V().has("name", "pumba").out("friendOf").id().toList();
      System.out.println(verticesWithNamePumba);
  } finally {
      cluster.close();
  }
```
