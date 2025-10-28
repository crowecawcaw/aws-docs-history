# Using AWS Database Migration Service to load data into Amazon Neptune from a different data store

AWS Database Migration Service (AWS DMS) can load data into Neptune from [supported source databases](../../../dms/latest/userguide/CHAP_Source.md "../../../dms/latest/userguide/CHAP_Source.md")
quickly and securely. The source database remains fully operational during the
migration, minimizing downtime for applications that rely on it.

You can find detailed information about AWS DMS in the [AWS Database Migration Service User Guide](../../../dms/latest/userguide.md "../../../dms/latest/userguide.md") and the
[AWS Database Migration Service API Reference](../../../dms/latest/APIReference.md "../../../dms/latest/APIReference.md"). In particular, you can find out how to set up a Neptune cluster
as a target for migration in [Using
Amazon Neptune as a Target for AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md").

Here are some prerequisites for importing data into Neptune using AWS DMS:

- You will need to create a AWS DMS table mapping object to define
  how data should be extracted from the source database (see [Specifying table selection and transformations by table mapping using JSON](../../../dms/latest/userguide/CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation "../../../dms/latest/userguide/CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation")
  in the AWS DMS Userguide for details). This table mapping configuration object
  specifies which tables should be read and in what order, and how their columns
  are named. It can also filter the rows being copied and provide simple value transformations
  such as converting to lower case or rounding.
- You will need to create a Neptune `GraphMappingConfig`
  to specify how the data extracted from the source database should be loaded
  into Neptune. For RDF data (queried using SPARQL), the `GraphMappingConfig`
  is written in the W3's standard [R2RML](https://www.w3.org/TR/r2rml/ "https://www.w3.org/TR/r2rml/")
  mapping language. For property graph data (queried using Gremlin), the
  `GraphMappingConfig` is a JSON object, described in [GraphMappingConfig Layout for Property-Graph/Gremlin Data](dms-neptune-graph-mapping.md#dms-neptune-graph-mapping-gremlin "dms-neptune-graph-mapping.md#dms-neptune-graph-mapping-gremlin").
- You must use AWS DMS to create a replication instance in the same VPC
  as your Neptune DB cluster, to mediate the transfer of data.
- You will also need an Amazon S3 bucket to be used as intermediate storage
  for staging the migration data.
