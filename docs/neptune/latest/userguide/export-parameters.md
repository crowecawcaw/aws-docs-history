# Parameters used to control the Neptune export process

Whether you are using the Neptune-Export service or the `neptune-export`
command line utility, the parameters you use to control the export are mostly the same.
They contain a JSON object passed to the Neptune-Export endpoint or to
`neptune-export` on the command line.

The object passed in to the export process has up to five top-level fields:

```
-d '{
      "command" : "`(either `export-pg` or `export-rdf`)`",
      "outputS3Path" : "s3:/`(your Amazon S3 bucket)`/`(path to the folder for exported data)`",
      "jobsize" : "`(for Neptune-Export service only)`",
      "params" : { `(a JSON object that contains export-process parameters)` },
      "additionalParams": { `(a JSON object that contains parameters for training configuration)` }
    }'
```

###### Contents

- [The command parameter](export-parameters.md#export-parameters-command "export-parameters.md#export-parameters-command")
- [The outputS3Path parameter](export-parameters.md#export-parameters-outputS3Path "export-parameters.md#export-parameters-outputS3Path")
- [The jobSize parameter](export-parameters.md#export-parameters-jobSize "export-parameters.md#export-parameters-jobSize")
- [The params object](export-parameters.md#export-parameters-params "export-parameters.md#export-parameters-params")
- [The additionalParams object](export-parameters.md#export-parameters-additionalParams "export-parameters.md#export-parameters-additionalParams")
- [Export parameter fields in the params top-level JSON object](export-params-fields.md "export-params-fields.md")
  - [List of possible fields in the export
    parameters params object](export-params-fields.md#export-params-fields-list "export-params-fields.md#export-params-fields-list")
    - [List of fields common to all types of export](export-params-fields.md#export-params-common-fields-list "export-params-fields.md#export-params-common-fields-list")
    - [List of fields for property-graph exports](export-params-fields.md#export-params-property-graph-fields-list "export-params-fields.md#export-params-property-graph-fields-list")
    - [List of fields for RDF exports](export-params-fields.md#export-params-RDF-fields-list "export-params-fields.md#export-params-RDF-fields-list")

  - [Fields common to all types of export](export-params-fields.md#export-params-common-fields "export-params-fields.md#export-params-common-fields")
    - [cloneCluster field in params](export-params-fields.md#export-params-cloneCluster "export-params-fields.md#export-params-cloneCluster")
    - [cloneClusterInstanceType field in params](export-params-fields.md#export-params-cloneClusterInstanceType "export-params-fields.md#export-params-cloneClusterInstanceType")
    - [cloneClusterReplicaCount field in params](export-params-fields.md#export-params-cloneClusterReplicaCount "export-params-fields.md#export-params-cloneClusterReplicaCount")
    - [cloneClusterEnableAuditLogs field in params](export-params-fields.md#export-params-cloneClusterEnableAuditLogs "export-params-fields.md#export-params-cloneClusterEnableAuditLogs")
    - [clusterId field in params](export-params-fields.md#export-params-clusterId "export-params-fields.md#export-params-clusterId")
    - [endpoint field in params](export-params-fields.md#export-params-endpoint "export-params-fields.md#export-params-endpoint")
    - [endpoints field in params](export-params-fields.md#export-params-endpoints "export-params-fields.md#export-params-endpoints")
    - [profile field in params](export-params-fields.md#export-params-profile "export-params-fields.md#export-params-profile")
    - [useIamAuth field in params](export-params-fields.md#export-params-useIamAuth "export-params-fields.md#export-params-useIamAuth")
    - [includeLastEventId field in params](export-params-fields.md#export-params-includeLastEventId "export-params-fields.md#export-params-includeLastEventId")

  - [Fields for property-graph export](export-params-fields.md#export-params-property-graph-fields "export-params-fields.md#export-params-property-graph-fields")
    - [concurrency field in params](export-params-fields.md#export-params-concurrency "export-params-fields.md#export-params-concurrency")
    - [edgeLabels field in params](export-params-fields.md#export-params-edgeLabels "export-params-fields.md#export-params-edgeLabels")
    - [filter field in params](export-params-fields.md#export-params-filter "export-params-fields.md#export-params-filter")
    - [filterConfigFile field in params](export-params-fields.md#export-params-filterConfigFile "export-params-fields.md#export-params-filterConfigFile")
    - [format field used for property-graph data in params](export-params-fields.md#export-params-format-pg "export-params-fields.md#export-params-format-pg")
    - [gremlinFilter field in params](export-params-fields.md#export-params-gremlinFilter "export-params-fields.md#export-params-gremlinFilter")
    - [gremlinNodeFilter field in params](export-params-fields.md#export-params-gremlinNodeFilter "export-params-fields.md#export-params-gremlinNodeFilter")
    - [gremlinEdgeFilter field in params](export-params-fields.md#export-params-gremlinEdgeFilter "export-params-fields.md#export-params-gremlinEdgeFilter")
    - [nodeLabels field in params](export-params-fields.md#export-params-nodeLabels "export-params-fields.md#export-params-nodeLabels")
    - [scope field in params](export-params-fields.md#export-params-scope "export-params-fields.md#export-params-scope")

  - [Fields for RDF export](export-params-fields.md#export-params-rdf-fields "export-params-fields.md#export-params-rdf-fields")
    - [format field used for RDF data in params](export-params-fields.md#export-params-format-rdf "export-params-fields.md#export-params-format-rdf")
    - [rdfExportScope field in params](export-params-fields.md#export-params-rdfExportScope "export-params-fields.md#export-params-rdfExportScope")
    - [sparql field in params](export-params-fields.md#export-params-sparql "export-params-fields.md#export-params-sparql")
    - [namedGraph field in params](export-params-fields.md#namedgraph-params-sparql "export-params-fields.md#namedgraph-params-sparql")

- [Examples of filtering
  what is exported](export-filtering-examples.md "export-filtering-examples.md")
  - [Filtering the export
    of property-graph data](export-filtering-examples.md#export-property-graph-filtering-examples "export-filtering-examples.md#export-property-graph-filtering-examples")
    - [Example of using scope to export only edges](export-filtering-examples.md#export-property-graph-filtering-scope-example "export-filtering-examples.md#export-property-graph-filtering-scope-example")
    - [Example of using
      nodeLabels and edgeLabels to export only nodes and edges having specific labels](export-filtering-examples.md#export-property-graph-filtering-labels-example "export-filtering-examples.md#export-property-graph-filtering-labels-example")
    - [Example of using filter
      to export only specified nodes, edges and properties](export-filtering-examples.md#export-property-graph-filtering-filter-example "export-filtering-examples.md#export-property-graph-filtering-filter-example")
    - [Example that
      uses gremlinFilter](export-filtering-examples.md#export-property-graph-filtering-gremlinFilter-example "export-filtering-examples.md#export-property-graph-filtering-gremlinFilter-example")
    - [Example that
      uses gremlinNodeFilter](export-filtering-examples.md#export-property-graph-filtering-gremlinNodeFilter-example "export-filtering-examples.md#export-property-graph-filtering-gremlinNodeFilter-example")
    - [Example that
      uses gremlinEdgeFilter](export-filtering-examples.md#export-property-graph-filtering-gremlinEdgeFilter-example "export-filtering-examples.md#export-property-graph-filtering-gremlinEdgeFilter-example")
    - [Combining filter,
      gremlinNodeFilter, nodeLabels, edgeLabels and scope](export-filtering-examples.md#export-property-graph-filtering-combo-example "export-filtering-examples.md#export-property-graph-filtering-combo-example")

  - [Filtering the export of RDF data](export-filtering-examples.md#export-RDF-filtering-examples "export-filtering-examples.md#export-RDF-filtering-examples")
    - [Using rdfExportScope and sparql to export specific edges](export-filtering-examples.md#export-RDF-filtering-rdfExportScope-sparql-example "export-filtering-examples.md#export-RDF-filtering-rdfExportScope-sparql-example")
    - [Using namedGraph
      to export a single named graph](export-filtering-examples.md#export-RDF-filtering-rdfExportScope-sparql-namedGraph-example "export-filtering-examples.md#export-RDF-filtering-rdfExportScope-sparql-namedGraph-example")

## The `command` parameter

The `command` top-level parameter determines whether to export
property-graph data or RDF data. If you omit the `command` parameter, the
export process defaults to exporting property-graph data.

- **`export-pg`**   –  
  Export property-graph data.
- **`export-rdf`**   –  
  Export RDF data.

## The `outputS3Path` parameter

The `outputS3Path` top-level parameter is required, and
must contain the URI of an Amazon S3 location to which the exported files can be published:

```
  "outputS3Path" : "s3://`(your Amazon S3 bucket)`/`(path to output folder)`"
```

The value must begin with `s3://`, followed by a valid bucket name
and optionally a folder path within the bucket.

## The `jobSize` parameter

The `jobSize` top-level parameter is only used with the
the Neptune-Export service, not with the `neptune-export`
command line utility, and is optional. It lets you characterize the size of
the export job you are starting, which helps determine the amount of compute
resources devoted to the job and its maximum concurrency level.

```
  "jobsize" : "`(one of four size descriptors)`"
```

The four valid size descriptors are:

- `small`   –   Maximum concurrency: 8.
  Suitable for storage volumes up to 10 GB.
- `medium`   –   Maximum concurrency: 32.
  Suitable for storage volumes up to 100 GB.
- `large`   –   Maximum concurrency: 64.
  Suitable for storage volumes over 100 GB but less than 1 TB.
- `xlarge`   –   Maximum concurrency: 96.
  Suitable for storage volumes over 1 TB.

By default, an export initiated on the Neptune-Export service runs as a
`small` job.

The performance of an export depends not only on the `jobSize` setting,
but also on the number of database instances that you're exporting from, the size of
each instance, and the effective concurrency level of the job.

For property-graph exports, you can configure the number of database instances
using the [cloneClusterReplicaCount](export-params-fields.md#export-params-cloneClusterReplicaCount "export-params-fields.md#export-params-cloneClusterReplicaCount") parameter,
and you can configure the job's effective concurrency level using the
[concurrency](export-params-fields.md#export-params-concurrency "export-params-fields.md#export-params-concurrency")
parameter.

## The `params` object

The `params` top-level parameter is a JSON object that contains parameters
that you use to control the export process itself, as explained in [Export parameter fields in the params top-level JSON object](export-params-fields.md "export-params-fields.md"). Some of the fields in the
`params` object are specific to property-graph exports, some to RDF.

## The `additionalParams` object

The `additionalParams` top-level parameter is a JSON object that contains
parameters you can use to control actions that are applied to the data after it has been
exported. At present, `additionalParams` is used only for exporting training
data for [Neptune ML](machine-learning-additionalParams.md "machine-learning-additionalParams.md").
