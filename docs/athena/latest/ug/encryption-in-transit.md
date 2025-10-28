# Encryption in transit

In addition to encrypting data at rest in Amazon S3, Amazon Athena uses Transport Layer
Security (TLS) encryption for data in-transit between Athena and Amazon S3, and between Athena
and customer applications accessing it.

You should allow only encrypted connections over HTTPS (TLS) using the [`aws:SecureTransport condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") on Amazon S3 bucket IAM
policies.

Query results that stream to JDBC or ODBC clients are encrypted using TLS. For
information about the latest versions of the JDBC and ODBC drivers and their
documentation, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md")
and [Connect to Amazon Athena with ODBC](connect-with-odbc.md "connect-with-odbc.md").

For Athena federated data source connectors, support for encryption in transit using
TLS depends on the individual connector. For information, see the documentation for the
individual [data source connectors](connectors-available.md "connectors-available.md").
