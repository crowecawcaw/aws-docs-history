# Configure

Lake Formation permissions for Amazon SageMaker Unified Studio

When you create a project in Amazon SageMaker Unified Studio, an AWS Glue database is added as part of this
project. If you want to publish assets from this AWS Glue database, no additional
permissions are needed.

However, if you want to publish assets and subscribe to assets from an AWS Glue database
that exists outside of your Amazon SageMaker Unified Studio project, you must explicitly provide your project
with the permissions to access tables in the external AWS Glue database. To do this, you
must complete the following settings in AWS Lake Formation and attach
necessary AWS Lake Formation permissions to the project's IAM role
role.

- Configure the Amazon S3 location for your data lake in
  AWS Lake Formation with **Lake Formation** permission
  mode or **Hybrid access mode**. For more information, see
  [https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md").
- Attach the following AWS Lake Formation permissions to the AWS Glue
  manage access role:
  - `Describe` and `Describe grantable` permissions
    on the database where the tables exist.
  - `Describe`, `Select`, `Describe
Grantable`, `Select Grantable` permissions on the
    all the tables in the above database that you want DataZone to manage
    access on your behalf.

###### Note

Amazon SageMaker Unified Studio supports the AWS Lake Formation hybrid mode. Lake Formation
hybrid mode enables you to start managing permissions on you AWS Glue databases and
tables through Lake Formation, while continuing to maintain any existing IAM
permissions on these tables and databases.
