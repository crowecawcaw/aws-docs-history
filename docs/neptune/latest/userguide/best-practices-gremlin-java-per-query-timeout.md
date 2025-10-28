# Optionally, set timeouts at a per-query level

Neptune provides you with the ability to set a timeout for your queries using the
parameter group option `neptune_query_timeout` (see [Parameters](parameters.md "parameters.md")). You can also override the global timeout, with code
like this:

```
  final Cluster cluster = Cluster.build("localhost")
                                 .port(8182)
                                 .maxInProcessPerConnection(32)
                                 .maxSimultaneousUsagePerConnection(32)
                                 .serializer(Serializers.GRAPHBINARY_V1D0)
                                 .create();

  try {
      final GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));
      List<Object> verticesWithNamePumba = g.with(ARGS_EVAL_TIMEOUT, 500L).V().has("name", "pumba").out("friendOf").id().toList();
      System.out.println(verticesWithNamePumba);
  } finally {
      cluster.close();
  }
```

Or, for string-based query submission, the code would look like this:

```
  RequestOptions options = RequestOptions.build().timeout(500).create();
  List<Result> result = client.submit("g.V()", options).all().get();

```

###### Note

It is possible to incur unexpected costs if you set the query timeout value
too high, particularly on a serverless instance. Without a reasonable timeout
setting, your query may keeps running much longer than you expected, incurring
costs you never anticipated. This is particularly true on a serverless instance
that could scale up to a large, expensive instance type while running the query.

You can avoid unexpected expenses of this kind by using a query timeout
value that accomodates the run-time your expect and only causes an unusually
long run to time out.

Starting from Neptune engine version 1.3.2.0, Neptune supports a new neptune_lab_mode parameter as
`StrictTimeoutValidation`. When this parameter has a value of `Enabled`, a per-query
timeout value specified as a request option or a query hint cannot exceed the value set globally in the parameter
group. In such a case, Neptune will throw `InvalidParameterException`.

This setting can be confirmed in a response on the '/status' endpoint when the value is `Disabled`, and
in `1.3.2.0`, the default value of this parameter is `Disabled`. Starting in `1.4.0.0`,
the `StrictTimeoutValidation` was changed so as to be `Enabled` by default.
