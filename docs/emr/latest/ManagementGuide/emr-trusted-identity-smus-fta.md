

# Full Table Access with Amazon SageMaker Unified Studio and TIP on Amazon EMR on EC2
<a name="emr-trusted-identity-smus-fta"></a>

In Full Table Access (FTA) mode, Lake Formation grants authorized IAM Identity Center users access to full tables without row or column filtering. For more information about the FTA access model, see [Application integration for full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html).

**Important**  
A job cannot simultaneously run Full Table Access (FTA) and Fine-Grained Access Control (FGAC) on the same Amazon EMR cluster. Use separate clusters for each mode.

## Prerequisites
<a name="emr-trusted-identity-smus-fta-prereqs"></a>
+ Complete the [Common setup for Amazon SageMaker Unified Studio with TIP on Amazon EMR on EC2](emr-trusted-identity-smus-tip-common-setup.md) steps.
+ Use Amazon EMR release 7.8.0 or later. Full Table Access with Amazon SageMaker Unified Studio and trusted identity propagation requires a minimum Amazon EMR version of 7.8.0.
+ In the Lake Formation console, navigate to **Administration** > **Application integration settings**. Enable **Allow third-party query engines to access data without the IAM session tag validation**. For more information, see [Application integration for full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html).
+ Complete the [Connect existing Amazon EMR on EC2 clusters to Amazon SageMaker Unified Studio](emr-trusted-identity-smus-tip-connect-existing-cluster.md) steps to prepare the connection to an existing cluster.

## Step 1: Create an Amazon EMR on EC2 cluster for FTA
<a name="emr-trusted-identity-smus-fta-cluster"></a>

Create an Amazon EMR security configuration with IAM Identity Center enabled but *without* Lake Formation enabled:

```
{
    "AuthenticationConfiguration": {
        "IdentityCenterConfiguration": {
            "EnableIdentityCenter": true,
            "IdentityCenterInstanceARN": "arn:aws:sso:::instance/ssoins-{{instance-id}}"
        }
    },
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": true,
        "EnableAtRestEncryption": false,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "PEM",
                "S3Object": "s3://{{your-bucket}}/cert/my-certs.zip"
            }
        }
    }
}
```

Launch the Amazon EMR cluster with this security configuration and the software settings specified in [Step 8: Configure Amazon EMR cluster software settings](emr-trusted-identity-smus-tip-connect-existing-cluster.md#emr-trusted-identity-smus-tip-connect-cluster-config).

## Step 2: Connect the cluster to Amazon SageMaker Unified Studio
<a name="emr-trusted-identity-smus-fta-connect"></a>

1. In your Amazon SageMaker Unified Studio project, navigate to **Compute** > **Data Processing** tab.

1. Choose **Add compute** > **Connect to existing compute resources** > **Amazon EMR on EC2 cluster**.

1. Enter the cluster ID and access role ARN (`EMRAccessRole` created in the connection prerequisites).

1. Verify the cluster appears under the **Data Processing** tab.

## Step 3: Query data using Full Table Access
<a name="emr-trusted-identity-smus-fta-query"></a>

1. Click on the open space for the compute, which opens the JupyterLab notebook.

1. Select **PySpark** from the kernel options, and select the Amazon EMR on EC2 compute you added from the compute dropdown.

1. In the first cell, select **Python** from the language dropdown for the cell, then configure Spark for Full Table Access using the `%%configure` magic command:

   **For Hive/Parquet tables:**

   ```
   %%configure -f
   {
       "conf": {
           "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
           "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": true,
           "spark.hadoop.fs.s3.folderObject.autoAction.disabled": true,
           "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": true,
           "spark.sql.catalog.createDirectoryAfterTable.enabled": true,
           "spark.sql.catalog.dropDirectoryBeforeTable.enabled": true
       }
   }
   ```

   **For Iceberg tables:**

   ```
   %%configure -f
   {
       "conf": {
           "spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
           "spark.sql.catalog.spark_catalog.warehouse": "{{S3_DATA_LOCATION}}",
           "spark.sql.catalog.spark_catalog.client.region": "{{REGION}}",
           "spark.sql.catalog.spark_catalog.type": "glue",
           "spark.sql.catalog.spark_catalog.glue.account-id": "{{ACCOUNT_ID}}",
           "spark.sql.catalog.spark_catalog.glue.lakeformation-enabled": "true",
           "spark.sql.catalog.dropDirectoryBeforeTable.enabled": "true"
       }
   }
   ```
**Note**  
You must run the `%%configure` cell before executing any other Spark operations.

   The preceding examples show the Spark configurations for Hive/Parquet and Iceberg tables. For the complete set of Spark configurations for full table access on each table type, including Hive, Iceberg, Delta Lake, and Hudi, see [Use Lake Formation for full table access with Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html).

1. In the next cell, query your table:

   ```
   spark.sql("select * from {{database_name}}.{{table_name}}").show()
   ```

1. Verify that the query returns data, confirming your IAM Identity Center identity was propagated and FTA credentials were used.

## Considerations
<a name="emr-trusted-identity-smus-fta-considerations"></a>
+ FTA and FGAC cannot run simultaneously on the same cluster.
+ FTA is supported with Amazon EMR release 7.8.0 and higher.
+ Supported for Hive, Iceberg, Delta, and Hudi tables.
+ You must use a user-defined role (not the service-linked role) when registering Amazon S3 locations with Lake Formation.
+ For more details, see [](lake-formation-unfiltered-ec2-access.md).

## Clean up resources
<a name="emr-trusted-identity-smus-fta-cleanup"></a>

To avoid ongoing charges, delete the resources you created for this tutorial:
+ Terminate the Amazon EMR on EC2 cluster.
+ Remove the Amazon EMR compute connection from your Amazon SageMaker Unified Studio project, and delete the Amazon SageMaker Unified Studio project and domain if you created them only for this tutorial.
+ Deregister the Amazon S3 data location in Lake Formation and delete any test Amazon S3 buckets.
+ Delete the IAM roles you created (for example, the access role and the Lake Formation location registration role).