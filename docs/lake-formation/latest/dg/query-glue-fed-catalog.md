# Querying federated catalogs

After you grant permissions to other principals, they can sign in and start querying the tables in the federated catalogs
using Athena.

To create and delete tables in the federated database, the principal must have Lake Formation `Create table`, `Drop` permissions.

For more information on granting Data Catalog permissions, see [Granting permissions on Data Catalog resources](granting-catalog-permissions.md "granting-catalog-permissions.md").

For more information on querying the Data Catalog from Amazon Athena, see [Querying AWS Glue Data Catalog from Amazon Athena](../../../athena/latest/ug/gdc-register.md "../../../athena/latest/ug/gdc-register.md") in
Amazon Athena User Guide.
