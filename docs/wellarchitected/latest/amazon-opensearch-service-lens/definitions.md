# Definitions

- **Domain:** The primary
  container for all OpenSearch resources. It represents the
  entire environment where your data is stored and indexed.
- **Node:** A single instance of
  OpenSearch running within your domain. Nodes work together to
  form a cluster and distribute the workloads and data among
  them.
- **Leader nodes:** Nodes that
  perform cluster management tasks but do not hold data or
  respond to data requests.
- **Dedicated leader nodes:**
  Nodes that serve exclusively as specialized nodes that are
  configured to perform the role of a leader.
- **Data nodes:** Nodes that are
  responsible for storing and managing data. Data nodes handle
  indexing and searching operations and store the actual index
  and document data.
- **UltraWarm and cold nodes:**
  UltraWarm nodes provide a cost-effective way to store large
  amounts of read-only data on Amazon OpenSearch Service. Rather
  than attached storage, UltraWarm nodes use Amazon S3 and a
  sophisticated caching solution to improve performance.
- **Multi-AZ with Standby:** A
  deployment option for Amazon OpenSearch Service domains
  providing 99.99% availability and consistent performance by
  spanning three Availability Zones, each with a complete data
  copy.
- **Index:** A data structure
  used to store, organize, and search documents, similar to a
  database table.
- **Shard:** A smaller, more
  manageable segment of an index. Each shard acts as a
  self-contained index, and in Amazon OpenSearch Service, shards are
  distributed across data nodes for load balancing, redundancy,
  and fault tolerance.
- **Replica:** A duplication of a
  shard, offering failover and load balancing capabilities.
  Amazon OpenSearch Service automatically distributes replica shards
  across various nodes within the domain.
- **Document:** A single unit of
  searchable data, like a row in a database table. Each document
  possesses a unique identification (ID) and encompasses a set
  of fields.
- **Field:** A named, typed value
  within a document, resembling a column in a database table.
  Fields may have various data types, including string, number,
  date, or Boolean.
- **Mapping:** Defines the
  structure of documents in an index, including field names,
  data types, and other metadata. It acts as a schema for the
  documents and helps Amazon OpenSearch Service understand the data and
  optimize search performance.
- **Query:** A request to search,
  filter, or aggregate data from an OpenSearch index. Amazon OpenSearch Service accommodates various query types, including term,
  match, range, and Boolean queries.
- **Aggregation:** A process of
  grouping and summarizing data based on specified criteria.
  OpenSearch supports various aggregation types, such as bucket
  aggregations, metric aggregations, and pipeline aggregations.
- **Snapshot:** Refers to a
  point-in-time copy of the data in one or more indices. It is
  essentially a backup mechanism that captures the state of your
  data at a specific moment.
