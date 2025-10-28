# Using the HTTPS REST endpoint to connect to a

Neptune DB instance

Amazon Neptune provides an HTTPS endpoint for Gremlin queries. The REST
interface is compatible with whatever Gremlin version your DB cluster is
using (see the [engine release page](engine-releases.md "engine-releases.md")
of the Neptune engine version you are running to determine which
Gremlin release it supports).

###### Note

As discussed in [Encrypting connections to your Amazon Neptune database with SSL/HTTPS](security-ssl.md "security-ssl.md"),
Neptune now requires that you connect using HTTPS instead of HTTP.

The following instructions walk you through connecting to the Gremlin endpoint using the
`curl` command and HTTPS. You must follow these instructions from an Amazon EC2 instance
in the same virtual private cloud (VPC) as your Neptune DB instance.

The HTTPS endpoint for Gremlin queries to a Neptune DB instance is
`https://`your-neptune-endpoint`:`port`/gremlin`.

###### Note

For information about finding the hostname of your Neptune DB instance, see [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md").

## To connect to Neptune using the HTTP REST endpoint

The following example uses **curl** to submit a Gremlin query through
HTTP **POST**. The query is submitted in JSON format in the body of the
post as the `gremlin` property.

```
curl -X POST -d '{"gremlin":"*g.V().limit(1)*"}' https://`your-neptune-endpoint`:`port`/gremlin
```

This example returns the first vertex in the graph by using the `g.V().limit(1)` traversal.
You can query for something else by replacing it with another Gremlin traversal.

###### Important

By default, the REST endpoint returns all results in a single JSON result set.
If this result set is too large, an `OutOfMemoryError` exception can occur
on the Neptune DB instance.

You can avoid this by enabling chunked responses (results returned in a series
of separate responses). See [Use optional HTTP
trailing headers to enable multi-part Gremlin responses](access-graph-gremlin-rest-trailing-headers.md "access-graph-gremlin-rest-trailing-headers.md").

Although HTTP **POST** requests are recommended for sending Gremlin
queries, it is also possible to use HTTP **GET** requests:

```
curl -G "https://`your-neptune-endpoint`:`port`?gremlin=*g.V().count()*"
```

###### Note

Neptune does not support the `bindings` property.
