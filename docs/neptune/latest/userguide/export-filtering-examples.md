# Examples of filtering

what is exported

Here are examples that illustrate ways to filter the data that is exported.

## Filtering the export

of property-graph data

### Example of using `scope` to export only edges

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "scope": "edges"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Example of using

`nodeLabels` and `edgeLabels` to export only nodes and edges having specific labels

The `nodeLabels` parameter in the following example specifies that
only nodes having a `Person` label or a `Post` label should
be exported. The `edgeLabels` parameter specifies that only edges
with a `likes` label should be exported:

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name`)",
    "nodeLabels": ["Person", "Post"],
    "edgeLabels": ["likes"]
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Example of using `filter`

to export only specified nodes, edges and properties

The `filter` object in this example exports `country` nodes
with their `type`, `code` and `desc` properties,
and also `route` edges with their `dist` property.

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "filter": {
      "nodes": [
        {
          "label": "country",
          "properties": [
            "type",
            "code",
            "desc"
          ]
        }
      ],
      "edges": [
        {
          "label": "route",
          "properties": [
            "dist"
          ]
        }
      ]
    }
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Example that

uses `gremlinFilter`

This example uses `gremlinFilter` to export only those nodes and edges
created after 2021-10-10 (that is, with a `created` property whose value
is greater than 2021-10-10):

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "gremlinFilter" : "has(\"created\", gt(datetime(\"2021-10-10\")))"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Example that

uses `gremlinNodeFilter`

This example uses `gremlinNodeFilter` to export only deleted nodes
(nodes with a Boolean `deleted` property whose value is `true`):

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "gremlinNodeFilter" : "has(\"deleted\", true)"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Example that

uses `gremlinEdgeFilter`

This example uses `gremlinEdgeFilter` to export only edges with a
`strength` numerical property whose value is 5:

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "gremlinEdgeFilter" : "has(\"strength\", 5)"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Combining `filter`,

`gremlinNodeFilter`, `nodeLabels`, `edgeLabels` and `scope`

The `filter` object in this example exports:

- `country` nodes with their `type`,
  `code` and `desc` properties
- `airport` nodes with their `code`,
  `icao` and `runways` properties
- `route` edges with their `dist` property

The `gremlinNodeFilter` parameter filters the nodes so that only nodes
with a `code` property whose value begins with A are exported.

The `nodeLabels` and `edgeLabels` parameters further restrict
the output so that only `airport` nodes and `route` edges are
exported.

Finally, the `scope` parameter eliminates edges from the export,
which leaves only the designated `airport` nodes in the output.

```
{
  "command": "export-pg",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "filter": {
      "nodes": [
        {
          "label": "airport",
          "properties": [
            "code",
            "icao",
            "runways"
          ]
        },
        {
          "label": "country",
          "properties": [
            "type",
            "code",
            "desc"
          ]
        }
      ],
      "edges": [
        {
          "label": "route",
          "properties": [
            "dist"
          ]
        }
      ]
    },
    "gremlinNodeFilter": "has(\"code\", startingWith(\"A\"))",
    "nodeLabels": [
      "airport"
    ],
    "edgeLabels": [
      "route"
    ],
    "scope": "nodes"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

## Filtering the export of RDF data

### Using `rdfExportScope` and `sparql` to export specific edges

This example exports triples whose predicate is
<http://kelvinlawrence.net/air-routes/objectProperty/route> and whose object is
not a literal:

```
{
  "command": "export-rdf",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "rdfExportScope": "query",
    "sparql": "CONSTRUCT { ?s <http://kelvinlawrence.net/air-routes/objectProperty/route> ?o } WHERE { ?s ?p ?o . FILTER(!isLiteral(?o)) }"
  },
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export"
}
```

### Using `namedGraph`

to export a single named graph

This example exports triples belonging to the named graph
<http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph>:

```
{
  "command": "export-rdf",
  "params": {
    "endpoint": "(your Neptune endpoint DNS name)",
    "rdfExportScope": "graph",
    "namedGraph": "http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph"
  },
  "outputS3Path": "s3://(your Amazon S3 bucket)/neptune-export"
}
```
