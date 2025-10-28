# Using AWS Database Migration Service (AWS DMS) to migrate from a

relational or NoSQL database to Amazon Neptune

AWS Database Migration Service (AWS DMS) is a cloud service that makes it easy to migrate relational
databases, data warehouses, NoSQL databases, and other types of data stores.
If you have graph data stored in one of the relational or NoSQL [databases that AWS DMS supports](../../../dms/latest/userguide/CHAP_Introduction.md "../../../dms/latest/userguide/CHAP_Introduction.md"),
AWS DMS can help you migrate to Neptune quickly and securely, without requiring
downtime from your current database. See [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md "dms-neptune.md") for details.

The migration dataflow using AWS DMS is as follows:

- Create a AWS DMS table-mapping object. This JSON object
  specifies which tables should be read from your source database and in
  what order, and how their columns are named. It can also filter the
  rows being copied and provide simple value transformations such as
  converting to lower case or rounding.
- Create a Neptune `GraphMappingConfig` to
  specify how the data extracted from the source database should be
  loaded into Neptune.
  - For RDF data (queried using SPARQL), the
    `GraphMappingConfig` is written in the W3's standard [R2RML](https://www.w3.org/TR/r2rml/ "https://www.w3.org/TR/r2rml/") mapping
    language.
  - For property graph data (queried using Gremlin), the
    `GraphMappingConfig` is a JSON object, as described in
    [GraphMappingConfig Layout for Property-Graph/Gremlin Data](dms-neptune-graph-mapping.md#dms-neptune-graph-mapping-gremlin "dms-neptune-graph-mapping.md#dms-neptune-graph-mapping-gremlin")

- Create an AWS DMS replication instance in the same VPC as
  your Neptune DB cluster, to perform the migration.
- Create an Amazon S3 bucket to be used as intermediary
  storage for staging the data being migrated.
- Run the AWS DMS migration task.
  See [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md "dms-neptune.md") for
  the details, and also Chris Smith's four-piece blog post, "Populating
  your graph in Amazon Neptune from a relational database using AWS
  Database Migration Service (DMS):"

- [Part 1: Setting the stage](https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-1-setting-the-stage/ "https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-1-setting-the-stage/")
- [Part 2: Designing the property graph model](https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-2-designing-the-property-graph-model/ "https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-2-designing-the-property-graph-model/")
- [Part 3: Designing the RDF Model](https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-3-designing-the-rdf-model/ "https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-3-designing-the-rdf-model/")
- [Part 4: Putting it all together](https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-4-putting-it-all-together/ "https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-4-putting-it-all-together/")
