# Querying federated catalogs

After you grant permissions to other principals, they can sign in and start querying the
tables in the federated catalogs by logging into the SQL tools using Amazon Redshift, Amazon EMR,
Amazon Athena, and AWS Glue ETL.

For more information on connecting to the AWS Glue Data Catalog using Apache Iceberg Rest extension endpoint or standalone Spark application, see [Accessing the AWS Glue Data Catalog](../../../glue/latest/dg/access_catalog.md "../../../glue/latest/dg/access_catalog.md")
section in the AWS Glue Developer Guide.

You can use the data definition language (DDL) queries to create and manage tables in the database using Apache Spark on Amazon EMR.
To create and delete tables in the Amazon Redshift database, the principal must have Lake Formation `Create table`, `Drop` permissions.

For more information on granting Data Catalog permissions, see [Granting permissions on Data Catalog resources](granting-catalog-permissions.md "granting-catalog-permissions.md").

For more information on querying the catalog resources from Amazon Athena, see [Querying AWS Glue Data Catalog from Amazon Athena](../../../athena/latest/ug/gdc-register.md "../../../athena/latest/ug/gdc-register.md") in
Amazon Athena User Guide.
