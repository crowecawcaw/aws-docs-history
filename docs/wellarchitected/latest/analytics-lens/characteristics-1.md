# Characteristics

**Scalable data lake:** A data lake should be able to scale
easily to petabytes and exabytes as data grows. Use a scalable, durable data store that
provides the fastest performance at the lowest cost, supports multiple ways to bring data in,
and has a good partner ecosystem.

**Data diversity:** Applications generate data in many formats. A
data lake should support diverse data types—structured, semi-structured, or unstructured.

**Schema management:** A modern data architecture should support
schema on read for a data lake with no strict source data requirement. The choice of storage
structure, schema, ingestion frequency, and data quality should be left to the data producer.
A data lake should also be able to incorporate changes to the structure of the incoming data
that is referred to as schema evolution. In addition, schema enforcement helps businesses
ensure data quality by preventing writes that do not match the schema.

**Metadata management:** Data should be self-discoverable with
the ability to track lineage as data ﬂows through tiers within the data lake. A comprehensive
Data Catalog that captures the metadata and provides a queryable interface for all data assets
is recommended.

**Unified governance:** A modern data architecture should have a
robust mechanism for centralized authorization and auditing. Configuring access policies in
the data lake and across all the data stores can be overly complex and error prone. Having a
centralized location to define the policies and enforce them is critical to a secure modern
data architecture.

**Transactional semantics:** In a data lake, data is often
ingested nearly continuously from multiple sources and is queried concurrently by multiple
analytic engines. Having atomic, consistent, isolated, and durable (ACID) transactions is
pivotal to keeping data consistent.

**Transactional Data Lake:** Data lakes offer one of the best options for cost, scalability, and flexibility to store data at a low cost, and to use this data for different types of analytics workloads. However, data lakes are not databases, and object storage does not provide support for ACID processing semantics, which you may require to effectively optimize and manage your data at scale across hundreds or thousands of users using a multitude of different technologies. Open table formats provide additional database-like functionality that simplifies the optimization and management overhead of data lakes, while still supporting storage on cost-effective systems. These features include:

- **ACID transactions:** Allowing a write to completely succeed or be rolled back in its entirety
- **Record-level operations:** Allowing for single rows to be inserted, updated, or deleted
- **Indexes:** Improving performance in addition to data lake techniques like partitioning
- **Concurrency control:** Allowing for multiple processes to read and write the same data at the same time
- **Schema evolution:** Allowing for columns of a table to be added or modified over the life of a table
- **Time travel:** Query data as of a point in time in the past

The three most common and prevalent open table formats are Apache Hudi, Apache Iceberg, and Delta Lake.
