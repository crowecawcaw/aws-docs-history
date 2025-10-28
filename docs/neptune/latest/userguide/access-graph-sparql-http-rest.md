# Using the HTTP REST endpoint to connect to a

Neptune DB instance

Amazon Neptune provides an HTTP endpoint for SPARQL queries. The REST interface is compatible
with SPARQL version 1.1.

###### Important

[Release: 1.0.4.0 (2020-10-12)](engine-releases-1.0.4.md "engine-releases-1.0.4.md")
made TLS 1.2 and HTTPS mandatory for all connections to Amazon Neptune. It is no longer possible
to connect to Neptune using unsecured HTTP, or using HTTPS with a version of TLS earlier than 1.2.

The following instructions walk you through connecting to the SPARQL endpoint using the
**curl** command, connecting through HTTPS, and using HTTP syntax. Follow these
instructions from an Amazon EC2 instance in the same virtual private cloud (VPC) as your
Neptune DB instance.

The HTTP endpoint for SPARQL queries to a Neptune DB instance is: 
`https://`your-neptune-endpoint`:`port`/sparql`.

###### Note

For information about finding the hostname of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

###### QUERY Using HTTP POST

The following example uses **curl** to submit a SPARQL **`QUERY`** through HTTP **POST**.

```
curl -X POST --data-binary 'query=select ?s ?p ?o where {?s ?p ?o} limit 10' https://`your-neptune-endpoint`:`port`/sparql
```

The preceding example returns up to 10 of the triples (subject-predicate-object) in the
graph by using the `?s ?p ?o` query with a limit of 10. To query for something
else, replace it with another SPARQL query.

###### Note

The default MIME media type of a response is `application/sparql-results+json` for
`SELECT` and `ASK` queries.

The default MIME type of a response is `application/n-quads` for
`CONSTRUCT` and `DESCRIBE` queries.

For a list of the media types used by Neptune for serialization, see
[RDF serialization formats used by Neptune SPARQL](sparql-media-type-support.md#sparql-serialization-formats "sparql-media-type-support.md#sparql-serialization-formats").

###### UPDATE Using HTTP POST

The following example uses **curl** to submit a SPARQL **`UPDATE`** through HTTP **POST**.

```
curl -X POST --data-binary 'update=INSERT DATA { <https://test.com/s> <https://test.com/p> <https://test.com/o> . }' https://`your-neptune-endpoint`:`port`/sparql
```

The preceding example inserts the following triple into the SPARQL default graph:
`<https://test.com/s> <https://test.com/p> <https://test.com/o>`
