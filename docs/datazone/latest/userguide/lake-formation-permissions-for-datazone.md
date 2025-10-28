# Configure Lake Formation

permissions for Amazon DataZone

When you create an environment using the built-in data lake blueprint
(**DefaultDataLake**), an AWS Glue database is added in
Amazon DataZone as part of this environment's creation process. If you want to publish assets
from this AWS Glue database, no additional permissions are needed.

However, if you want to publish assets and subscribe to assets from an AWS Glue
database that exists outside of your Amazon DataZone environment, you must explicitly provide
Amazon DataZone with the permissions to access tables in this external AWS Glue database.
To do this, you must complete the following settings in AWS Lake Formation and attach
necessary Lake Formation permissions to the [AmazonDataZoneGlueAccess-<region>-<domainId>](glue-manage-access-role.md "glue-manage-access-role.md") .

- Configure the Amazon S3 location for your data lake in AWS Lake Formation
  with **Lake Formation** permission mode or **Hybrid
  access mode**. For more information, see [https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md").
- Remove the `IAMAllowedPrincipals` permission from the Amazon Lake
  Formation tables for which Amazon DataZone handles permissions. For more information,
  see [https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation-background.html](../../../lake-formation/latest/dg/upgrade-glue-lake-formation-background.md "../../../lake-formation/latest/dg/upgrade-glue-lake-formation-background.md").
- Attach the following AWS Lake Formation permissions to the [AmazonDataZoneGlueAccess-<region>-<domainId>](glue-manage-access-role.md "glue-manage-access-role.md"):
  - `Describe` and `Describe grantable` permissions
    on the database where the tables exist
  - `Describe`, `Select`, `Describe
Grantable`, `Select Grantable` permissions on the
    all the tables in the above database that you want DataZone to manage
    access on your behalf.

###### Note

Amazon DataZone supports the AWS Lake Formation Hybrid mode. Lake Formation hybrid
mode enables you to start managing permissions on you AWS Glue databases and
tables through Lake Formation, while continuing to maintain any existing IAM
permissions on these tables and databases. For more information, see [Amazon DataZone integration with AWS Lake Formation
hybrid mode](hybrid-mode.md "hybrid-mode.md")

For more information, see [Troubleshooting AWS Lake
Formation permissions for Amazon DataZone](troubleshooting-datazone.md#troubleshooting-lake-formation-permissions "troubleshooting-datazone.md#troubleshooting-lake-formation-permissions").
