# Exporting data from a Neptune DB cluster

There are several good ways to export data from a Neptune DB cluster:

- For small amounts of data, simply use the results of a query or
  queries.
- For RDF data, the [Graph
  Store Protocol (GSP)](sparql-graph-store-protocol.md "sparql-graph-store-protocol.md") can make exporting easy. For example:

```
curl --request GET \
  'https://`your-neptune-endpoint`:`port`/sparql/gsp/?graph=`http://www.example.com/named/graph`'
```

- There is also a powerful and flexible open-source tool for
  exporting Neptune data, namely [`neptune-export`](https://github.com/aws/neptune-export "https://github.com/aws/neptune-export").
  The following sections describe the features of this tool and how to use it.

###### Topics

- [Using neptune-export](neptune-export.md "neptune-export.md")
- [Using the Neptune-Export service to export Neptune data](export-service.md "export-service.md")
- [Using the neptune-export command-line
  tool to export data from Neptune](export-utility.md "export-utility.md")
- [Files exported by Neptune-Export
  and neptune-export](exported-files.md "exported-files.md")
- [Parameters used to control the Neptune export process](export-parameters.md "export-parameters.md")
- [Troubleshooting the Neptune export process](export-troubleshooting.md "export-troubleshooting.md")
- [Exporting Gremlin query results to Amazon S3](exporting-gremlin.md "exporting-gremlin.md")
