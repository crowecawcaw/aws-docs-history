# Calling the Neptune Streams REST API

You access Neptune Streams using a REST API that sends an HTTP GET request to one
of the following local endpoints:

- For a SPARQL graph DB:   `https://`Neptune-DNS`:8182/sparql/stream`.
- For a Gremlin or openCypher graph DB:  
  `https://`Neptune-DNS`:8182/propertygraph/stream` or
  `https://`Neptune-DNS`:8182/pg/stream`.

###### Note

As of [engine release 1.1.0.0](engine-releases-1.1.0.md "engine-releases-1.1.0.md"),
the Gremlin stream endpoint (`https://`Neptune-DNS`:8182/gremlin/stream`)
is being deprecated, along with its associated output format (`GREMLIN_JSON`).
It is still supported for backward compatibility but may be removed in future releases.

Only an HTTP `GET` operation is allowed.

Neptune supports `gzip` compression of the response, provided that
the HTTP request includes an `Accept-Encoding` header that specifies `gzip`
as an accepted compression format (that is, `"Accept-Encoding: gzip"`).

###### Parameters

- `limit`   –  
  long, optional. Range: 1–100,000. Default: 10.

Specifies the maximum number of records to return. There is also a size limit of 10 MB
on the response that can't be modified and that takes precedence over the number of
records specified in the `limit` parameter. The response does include a
threshold-breaching record if the 10 MB limit was reached.

- `iteratorType`   –  
  String, optional.

This parameter can take one of the following values:

    + `AT_SEQUENCE_NUMBER`(default)   –  
     Indicates that reading should start from the event sequence number specified
     jointly by the `commitNum` and `opNum` parameters.
    + `AFTER_SEQUENCE_NUMBER`   –  
     Indicates that reading should start right after the event sequence number
     specified jointly by the `commitNum` and `opNum`
     parameters.
    + `TRIM_HORIZON`   –  
     Indicates that reading should start at the last untrimmed record in the system,
     which is the oldest unexpired (not yet deleted) record
     in the change-log stream. This mode is useful during application startup, when
     you don't have a specific starting event sequence number.
    + `LATEST`   –  
     Indicates that reading should start at the most recent record in the system,
     which is the latest unexpired (not yet deleted) record in the change-log stream.
     This is useful when there is a need to read records from current top of the
     streams so as not to process older records, such as during disaster recovery
     or a zero-downtime upgrade. Note that in this mode, there is at most only one
     record returned.

- `commitNum`   –  
  long, required when iteratorType is `AT_SEQUENCE_NUMBER` or
  `AFTER_SEQUENCE_NUMBER`.

The commit number of the starting record to read from the change-log stream.

This parameter is ignored when `iteratorType` is `TRIM_HORIZON`
or `LATEST`.

- `opNum`   –  
  long, optional (the default is `1`).

The operation sequence number within the specified commit to start reading from in the
change-log stream data.
Operations that change SPARQL graph data generally only generate a single change record
per operation. However, operations that change Gremlin graph data can generate multiple change
records per operation, as in the following examples:

- `INSERT`   –  
  A Gremlin vertex can have multiple labels, and a Gremlin
  element can have multiple properties. A separate change record is generated for each label
  and property when an element is inserted.
- `UPDATE`   –  
  When a Gremlin element property is changed, two change
  records are generated: the first for removing the previous value, and the second for
  inserting the new value.
- `DELETE`   –  
  A separate change record is generated for each
  element property that is deleted. For example, when a Gremlin edge with properties is
  deleted, one change record is generated for each of the properties, and after that, one is
  generated for deletion of the edge label.

When a Gremlin vertex is deleted, all the incoming and outgoing edge
properties are deleted first, then the edge labels, then the vertex properties,
and finally the vertex labels. Each of these deletions generates a change record.
