# Querying HealthLake data with Amazon Athena

During a HealthLake import job, nested FHIR JSON data undergoes an ETL process and is stored in
[Apache Iceberg open table format](https://iceberg.apache.org/ "https://iceberg.apache.org/"),
where each FHIR resource type is represented as an individual table in Athena. This enables
users to query the FHIR data using SQL, but without having to export it first. This is
valuable, as it empowers clinicians and scientists to query FHIR data to validate their
decisions or advance their research. For more information about how Apache Iceberg
tables function in Athena, see [Query Apache Iceberg tables](../../../athena/latest/ug/querying-iceberg.md "../../../athena/latest/ug/querying-iceberg.md") in the
_Athena User Guide_.

###### Note

HealthLake supports FHIR R4 `read` interaction on your HealthLake data in Athena. For more information,
see [Reading a FHIR resource](managing-fhir-resources-read.md "managing-fhir-resources-read.md").

The topics in this section describe how to connect your HealthLake data store to Athena, how to
query it using SQL, and how to connect results with other AWS services for further
analysis.

###### Topics

- [Getting
  started](integrating-athena-getting-started.md "integrating-athena-getting-started.md")
- [Querying with SQL](integrating-athena-query-sql.md "integrating-athena-query-sql.md")
- [Example
  queries](integrating-athena-complex-filtering.md "integrating-athena-complex-filtering.md")
