# Using SPARQL UPDATE UNLOAD to delete data from Neptune

Neptune also provides a custom SPARQL operation, `UNLOAD`, for removing
data that is specified in a remote source. `UNLOAD` can be regarded as a
counterpart to the `LOAD` operation. Its syntax is:

###### Note

This feature is available starting in [Neptune engine release 1.0.4.1](engine-releases-1.0.4.md "engine-releases-1.0.4.md").

```
UNLOAD SILENT `(URL of the remote data to be unloaded)` FROM GRAPH `(named graph from which to remove the data)`
```

- **`SILENT`**   –  
  (_Optional_) Causes the operation to return success even if
  there was an error when processing the data.

This can be useful when a single transaction contains multiple statements
like `"LOAD ...; LOAD ...; UNLOAD ...; LOAD ...;"` and you want the
transaction to complete even if some of the remote data could not be processed.

- `URL of the remote data to be unloaded`   –  
  (_Required_) Specifies a remote data file containing data to be
  unloaded from a graph.

The remote file must have one of the following extensions (these are the
same formats that UPDATE-LOAD supports):

    + `.nt` for NTriples.
    + `.nq` for NQuads.
    + `.trig` for Trig.
    + `.rdf` for RDF/XML.
    + `.ttl` for Turtle.
    + `.n3` for N3.
    + `.jsonld` for JSON-LD.

All the data that this file contains will be removed from your DB cluster
by the `UNLOAD` operation.

Any Amazon S3 authentication must be included in the URL for the data to unload. You can pre-sign an
Amazon S3 file and then use the resulting URL to access it securely. For example:

```
aws s3 presign --expires-in `(number of seconds)` s3://`(bucket name)`/`(path to file of data to unload)`
```

Then:

```
curl https://`(a Neptune endpoint URL)`:8182/sparql \
  --data-urlencode 'update=unload `(pre-signed URL of the remote Amazon S3 data to be unloaded)` \
                           from graph `(named graph)`'
```

For more information, see [Authenticating Requests: Using Query Parameters](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md").

- **`FROM GRAPH`** `(named
graph from which to remove the data)`   –  
  (_Optional_) Specifies the named graph from which the remote
  data should be unloaded.

Neptune associates every triple with a named graph. You can specify the
default named graph using the fallback named-graph URI,
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`, like this:

```
FROM GRAPH <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph>
```

In the same way that `LOAD` corresponds to `INSERT DATA
 { `(inline data)` }`, `UNLOAD` corresponds to
`DELETE DATA { `(inline data)` }`. Like
`DELETE DATA`, `UNLOAD` does not work on data that contains blank nodes.

For example, if a local web server serves a file named `data.nt`
that contains the following 2 triples:

```
<http://example.org/resource#a> <http://example.org/resource#p> <http://example.org/resource#b> .
<http://example.org/resource#a> <http://example.org/resource#p> <http://example.org/resource#c> .
```

The following `UNLOAD` command would delete those two triples from the
named graph, `<http://example.org/graph1>`:

```
UNLOAD <http://localhost:80/data.nt> FROM GRAPH <http://example.org/graph1>
```

This would have the same effect as using the following `DELETE DATA` command:

```
DELETE DATA {
  GRAPH <http://example.org/graph1> {
    <http://example.org/resource#a> <http://example.org/resource#p> <http://example.org/resource#b> .
    <http://example.org/resource#a> <http://example.org/resource#p> <http://example.org/resource#c> .
  }
}
```

###### Exceptions thrown by the `UNLOAD` command

- **`InvalidParameterException`**   –  
  There were blank nodes in the data. _HTTP status_: 400 Bad Request.

_Message_: `Blank nodes are not allowed for UNLOAD`

- **`InvalidParameterException`**   –  
  There was broken syntax in the data. _HTTP status_: 400 Bad Request.

_Message_: `Invalid syntax in the specified file.`

- **`UnloadUrlAccessDeniedException`**   –  
  Access was denied. _HTTP status_: 400 Bad Request.

_Message_: `Update failure: Endpoint `(Neptune
endpoint)` reported access denied error. Please verify access.`

- **`BadRequestException`**   –  
  The remote data cannot be retrieved. _HTTP status_: 400 Bad Request.

_Message_: _(depends on the HTTP response)._
