# Using the SPARQL 1.1 Graph Store HTTP Protocol (GSP) in Amazon Neptune

In the [SPARQL 1.1 Graph
Store HTTP Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/ "https://www.w3.org/TR/sparql11-http-rdf-update/") recommendation, the W3C defined an HTTP protocol for managing
RDF graphs. It defines operations for removing, creating, and replacing RDF graph content
as well as for adding RDF statements to existing content.

The graph-store protocol (GSP) provides a convenient way to manipulate your
entire graph without having to write complex SPARQL queries.

As of [Release: 1.0.5.0 (2021-07-27)](engine-releases-1.0.5.md "engine-releases-1.0.5.md"),
Neptune fully supports this protocol.

The endpoint for the graph-store protocol (GSP) is:

```
https://`your-neptune-cluster`:`port`/sparql/gsp/
```

To access the default graph with GSP, use:

```
https://`your-neptune-cluster`:`port`/sparql/gsp/?default
```

To access a named graph with GSP, use:

```
https://`your-neptune-cluster`:`port`/sparql/gsp/?graph=`named-graph-URI`
```

## Special details of the Neptune GSP implementation

Neptune fully implements the [W3C
recommendation](https://www.w3.org/TR/sparql11-http-rdf-update/ "https://www.w3.org/TR/sparql11-http-rdf-update/") that defines GSP. However, there are a few situations that the
specification doesn't cover.

One of these is the case where a `PUT` or `POST`
request specifies one or more named graphs in the request body that differ
from the graph specified by the request URL. This can only happen when the
request body RDF format supports named graphs, as, for example, using
`Content-Type: application/n-quads` or `Content-Type:
 application/trig`.

In this situation, Neptune adds or updates all the named graphs present
in the body, as well as the named graph specified in the URL.

For example, suppose that starting with an empty database, you send a
`PUT` request to upsert votes into three graphs. One, named
`urn:votes`, contains all votes from all election years.
Two others, named `urn:votes:2005` and `urn:votes:2019`,
contain votes from specific election years. The request and its payload look
like this:

```
PUT "http://`your-Neptune-cluster`:`port`/sparql/gsp/?graph=urn:votes"
  Host: example.com
  Content-Type: application/n-quads

  PAYLOAD:

  <urn:JohnDoe> <urn:votedFor> <urn:Labour> <urn:votes:2005>
  <urn:JohnDoe> <urn:votedFor> <urn:Conservative> <urn:votes:2019>
  <urn:JaneSmith> <urn:votedFor> <urn:LiberalDemocrats> <urn:votes:2005>
  <urn:JaneSmith> <urn:votedFor> <urn:Conservative> <urn:votes:2019>
```

After the request is executed, the data in the database looks like this:

```
<urn:JohnDoe>   <urn:votedFor> <urn:Labour>           <urn:votes:2005>
<urn:JohnDoe>   <urn:votedFor> <urn:Conservative>     <urn:votes:2019>
<urn:JaneSmith> <urn:votedFor> <urn:LiberalDemocrats> <urn:votes:2005>
<urn:JaneSmith> <urn:votedFor> <urn:Conservative>     <urn:votes:2019>
<urn:JohnDoe>   <urn:votedFor> <urn:Labour>           <urn:votes>
<urn:JohnDoe>   <urn:votedFor> <urn:Conservative>     <urn:votes>
<urn:JaneSmith> <urn:votedFor> <urn:LiberalDemocrats> <urn:votes>
<urn:JaneSmith> <urn:votedFor> <urn:Conservative>     <urn:votes>
```

Another ambiguous situation is where more than one graph is specied
in the request URL itself, using any of `PUT`, `POST`,
`GET` or `DELETE`. For example:

```
POST "http://`your-Neptune-cluster`:`port`/sparql/gsp/?graph=urn:votes:2005&graph=urn:votes:2019"
```

Or:

```
GET "http://`your-Neptune-cluster`:`port`/sparql/gsp/?default&graph=urn:votes:2019"
```

In this situation, Neptune returns an HTTP 400 with a message indicating that
only one graph can be specified in the request URL.
