# Prerequisites for managing Amazon Redshift managed catalog in the AWS Glue Data Catalog

This section covers the prerequisites needed to manage Amazon Redshift
managed storage catalogs within the AWS Glue Data Catalog using Lake Formation permissions.

1. AWS account setup
   - AWS account with administrative permissions
   - Lake Formation service enabled in your Region

2. Lake Formation configuration
   - Create a data lake administrator – Create an IAM role that is authorized to create the AWS Glue Data Catalog objects (catalogs, databases,
     tables/views), and grant Lake Formation permissions to other users.

   For step-by-step instructions on creating a data lake administrator, see [Create data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin").

   If the IAM role used for creating federated catalogs is not a data lake administrator, you need to grant the role the `Create catalog` permission.

   ```
   aws lakeformation grant-permissions \
   --cli-input-json \
   '{
       "Principal": {
        "DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/Admin"
       },
       "Resource": {
           "Catalog": {
           }
       },
       "Permissions": [
           "CREATE_CATALOG",
           "DESCRIBE"
       ]
   }'

   ```

   - Create a read only administrator role to discover the Amazon Redshift federated catalogs in the
     Data Catalog from Amazon Redshift Query Editor v2.

   To query the Amazon Redshift tables in the federated catalog from Amazon Redshift Query Editor v2, ensure that
   the Read only administrator role policy contains the ARN for the Amazon Redshift service-linked
   role-`AWSServiceRoleForRedshift`.

   ```
    aws lakeformation put-data-lake-settings
           region us-east-1 \
           data-lake-settings \
    '{
      "DataLakeAdmins": [{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/Admin"}],
      "ReadOnlyAdmins":[{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift"}],
      "CreateDatabaseDefaultPermissions":[],
      "CreateTableDefaultPermissions":[],
      "Parameters":{"CROSS_ACCOUNT_VERSION":"4","SET_CONTEXT":"TRUE"}

     }'

   ```

   - Data Catalog configured to use Lake Formation permissions
   - Default Data Catalog settings disabled (recommended)
   - Cross-account version set to 4 or higher is required to grant cross account permissions on the federated catalog objects

3. Create a data transfer role that Amazon Redshift can assume on your behalf to transfer data to and from the Amazon S3 bucket.

When you enable data lake access for Apache Iceberg compatible query engines
such as Athena, Amazon EMR on Amazon EC2 to access the Amazon Redshift resources in the Data Catalog, you need to
create an IAM role with the required permissions to perform data transfer to and from
the Amazon S3 bucket.

    * glue:GetCatalog
    * glue:GetDatabase
    * kms:GenerateDataKey
    * kms:Decrypt

4. Add a trust policy (`sts:AssumeRole`) to the data transfer role for
   AWS Glue and Amazon Redshift services to assume the role to transfer data to and from the Amazon S3
   bucket.
5. Add a key policy to the AWS KMS key if you're using a customer managed key to encrypt
   the data in the Amazon Redshift cluster/namespace. Replace the account number with a valid
   AWS account number, and specify data transfer role name. By default, the data
   in the Amazon Redshift cluster is encrypted using an KMS key. Lake Formation provides an option to
   create your custom KMS key for encryption. If you're using a customer managed
   key, you must add specific key policies to the key.

For more information about managing the permissions of a customer managed key,
see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").
