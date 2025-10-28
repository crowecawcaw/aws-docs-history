# Encryption in transit

AWS provides Secure Sockets Layer (SSL) encryption for data in flight.

DataBrew support for JDBC data sources comes through AWS Glue. When connecting to JDBC data
sources, DataBrew uses the settings on your AWS Glue connection, including the
**Require SSL connection** option. For more information, see
[AWS Glue
Connection Properties - AWS Glue](../../../glue/latest/dg/connection-defining.md "../../../glue/latest/dg/connection-defining.md") in the _AWS Glue Developer Guide_.

AWS KMS provides both "bring your own key" encryption and server-side
encryption for DataBrew extract, transform, load (ETL) processing and for the AWS Glue Data Catalog.
