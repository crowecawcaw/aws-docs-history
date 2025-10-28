# Grant access to managed AWS Glue Data Catalog assets in

Amazon SageMaker Unified Studio

###### Note

Access management for the AWS Glue Data Catalog assets using the AWS Lake Formation LF-TBAC method is not
supported.

Support for cross-Region sharing of assets in AWS Glue Data Catalog is not
supported.

Support for cross-account sharing of assets in a federated catalog within AWS Glue Data
Catalog is not supported.

When a subscription request to managed AWS Glue Data Catalog assets is approved, Amazon SageMaker Unified Studio grants
and manages access to the approved AWS Glue Data Catalog tables on your behalf through AWS Lake Formation. For the
subscriber project, assets that are granted appear in the AWS Glue Data Catalog as resources in your
account. You can then use Amazon Athena, Amazon Redshift, or Spark to query the
tables.

For Amazon SageMaker Unified Studio to be able to grant access to AWS Glue Data Catalog tables, the following
conditions must be met.

- The AWS Glue table must be Lake Formation-managed since Amazon SageMaker Unified Studio grants access by
  managing Lake Formation permissions.
- The IAM role of the project that has published the asset to the Amazon SageMaker Catalog
  must have the following AWS Lake Formation permissions:

      + `DESCRIBE` and `DESCRIBE GRANTABLE` permissions on the AWS
       Glue database that contains the published table.
      + `DESCRIBE`, `SELECT`, `DESCRIBE GRANTABLE`,
       `SELECT GRANTABLE` permissions in Lake Formation on the published table
       itself.

  For more information, see [Granting and revoking permissions on catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md") in the _AWS Lake Formation Developer Guide_.
