# Fine-Grained Access Control with Amazon SageMaker Unified Studio and TIP on Amazon EMR on EC2

In Fine-Grained Access Control (FGAC) mode, Lake Formation enforces row-level, column-level, and cell-level permissions on AWS Glue Data Catalog tables based on the propagated IAM Identity Center user identity. For more information about the FGAC access model, see [Enable Lake Formation with Amazon EMR](emr-lf-enable.md "emr-lf-enable.md").

## Prerequisites

- Complete the [Common setup for Amazon SageMaker Unified Studio with TIP on Amazon EMR on EC2](emr-trusted-identity-smus-tip-common-setup.md "emr-trusted-identity-smus-tip-common-setup.md") steps.
- In Lake Formation, configure **Application integration settings**: enable **Allow external engines to filter data in Amazon S3 locations registered with Lake Formation** and provide `Amazon EMR` as the **AuthorizedSessionTagValue**.

## Step 1: Add Amazon EMR on EC2 compute to your Amazon SageMaker Unified Studio project

You can add Amazon EMR on EC2 compute for FGAC in two ways:

**Option A: Launch a new Amazon EMR on EC2 cluster from Amazon SageMaker Unified Studio**

Amazon SageMaker Unified Studio automatically creates the necessary roles and security configuration (with both IAM Identity Center and Lake Formation enabled) when launching an Amazon EMR on EC2 cluster.

1. In your Amazon SageMaker Unified Studio project, navigate to **Compute** > **Data Processing** tab.
2. Choose **Add compute** > **Add a new EMR on EC2 cluster**.
3. Amazon SageMaker Unified Studio launches the cluster with IAM Identity Center and Lake Formation enabled in the security configuration. Wait for the cluster to reach **Running** state.

**Option B: Connect to an existing Amazon EMR on EC2 cluster**

If you have an existing Amazon EMR on EC2 cluster with both IAM Identity Center and Lake Formation enabled in the security configuration, you can connect it to Amazon SageMaker Unified Studio. First complete the [Connect existing Amazon EMR on EC2 clusters to Amazon SageMaker Unified Studio](emr-trusted-identity-smus-tip-connect-existing-cluster.md "emr-trusted-identity-smus-tip-connect-existing-cluster.md") steps, then:

1. Create an Amazon EMR security configuration with _both_ IAM Identity Center and Lake Formation enabled using the following AWS CLI command:

```
aws emr create-security-configuration --name "IdentityCenterConfiguration-with-lf-smustip" --region `your-region` --security-configuration '{
    "AuthenticationConfiguration":{
        "IdentityCenterConfiguration":{
            "EnableIdentityCenter":true,
            "IdentityCenterApplicationAssignmentRequired":false,
            "IdentityCenterInstanceARN": "arn:aws:sso:::instance/ssoins-`instance-id`",
            "IAMRoleForEMRIdentityCenterApplicationARN": "arn:aws:iam::`account-id`:role/`your_EMR_Instance_profile_role`"
        }
    },
    "AuthorizationConfiguration": {
        "LakeFormationConfiguration": {
            "AuthorizedSessionTagValue": "Amazon EMR"
        },
        "IAMConfiguration": {
          "EnableApplicationScopedIAMRole": true,
          "ApplicationScopedIAMRoleConfiguration": {
            "PropagateSourceIdentity": true
          }
        }
    },
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": true,
        "EnableAtRestEncryption": false,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "PEM",
                "S3Object": "s3://`DomainBucketName`/`AmazonDataZoneDomainID`/certificate_location/certs.zip"
            }
        }
    },
  "InstanceMetadataServiceConfiguration": {
    "MinimumInstanceMetadataServiceVersion": 2,
    "HttpPutResponseHopLimit": 2
}
}'
```

###### Note

The key difference from FTA is the inclusion of `AuthorizationConfiguration.LakeFormationConfiguration` in the security configuration. This enables Lake Formation to filter data at the row, column, and cell level. 2. Launch the Amazon EMR cluster with this security configuration and the software settings specified in [Step 8: Configure Amazon EMR cluster software settings](emr-trusted-identity-smus-tip-connect-existing-cluster.md#emr-trusted-identity-smus-tip-connect-cluster-config "emr-trusted-identity-smus-tip-connect-existing-cluster.md#emr-trusted-identity-smus-tip-connect-cluster-config"). 3. In your Amazon SageMaker Unified Studio project, navigate to **Compute** > **Data Processing** tab. 4. Choose **Add compute** > **Connect to existing compute resources** > **Amazon EMR on EC2 cluster**. 5. Enter the cluster ID and access role ARN (`EMRAccessRole` created in the connection prerequisites).

## Step 2: Query data with Fine-Grained Access Control

1. Click on the open space for the compute, which opens the JupyterLab notebook.
2. Select **PySpark** from the kernel options, and select the Amazon EMR on EC2 compute you added from the compute dropdown.
3. In the notebook cell, query your table:

```
spark.sql("select * from `database_name`.`table_name`").show()
```

4. Verify that the query returns only the data your IAM Identity Center user is authorized to see based on the Lake Formation fine-grained permissions (row/column/cell filters).

###### Note

With FGAC mode, no additional `%%configure` Spark configuration is needed. Lake Formation credential vending and data filtering are handled automatically by the Amazon EMR cluster's security configuration.

## Step 3: Verify fine-grained access control

To verify that fine-grained permissions are enforced:

1. Grant different Lake Formation permissions to different IAM Identity Center users. For example, grant one user access to all columns and another user access to only specific columns.
2. Sign in to Amazon SageMaker Unified Studio as each user and run the same query.
3. Confirm that each user sees only the columns/rows they are authorized to access.

For detailed information on setting up Named Data Catalog and LF-Tag based permissions, see [Using Identity based federation with Parquet tables](emr-trusted-identity-auth-parquet.md "emr-trusted-identity-auth-parquet.md").

## Considerations

- FGAC requires Lake Formation to be enabled in the Amazon EMR security configuration.
- FGAC is supported with Amazon EMR release 6.15.0 and higher for TIP, and 7.8.0 and higher for runtime roles with TIP.
- Only Apache Spark is supported with FGAC and TIP.
- FGAC and FTA cannot run simultaneously on the same cluster.
- For more details on FGAC setup, see [Enable Lake Formation with Amazon EMR](emr-lf-enable.md "emr-lf-enable.md").

## Clean up resources

To avoid ongoing charges, delete the resources you created for this tutorial:

- Terminate the Amazon EMR on EC2 cluster.
- Remove the Amazon EMR compute connection from your Amazon SageMaker Unified Studio project, and delete the Amazon SageMaker Unified Studio project and domain if you created them only for this tutorial.
- Deregister the Amazon S3 data location in Lake Formation and delete any test Amazon S3 buckets.
- Delete the Amazon EMR security configuration and the IAM roles you created.

## Related resources

- [Trusted identity propagation](../../../sagemaker-unified-studio/latest/adminguide/trusted-identity-propagation.md "../../../sagemaker-unified-studio/latest/adminguide/trusted-identity-propagation.md") in the _Amazon SageMaker Unified Studio Administrator Guide_.
- [Enable Amazon EMR on EC2 blueprint](../../../sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.md "../../../sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.md") in the _Amazon SageMaker Unified Studio Administrator Guide_.
- [Enable Lake Formation with Amazon EMR](emr-lf-enable.md "emr-lf-enable.md").
- [Use trusted identity propagation for Apache Spark interactive sessions in Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/big-data/use-trusted-identity-propagation-for-apache-spark-interactive-sessions-in-amazon-sagemaker-unified-studio/ "https://aws.amazon.com/blogs/big-data/use-trusted-identity-propagation-for-apache-spark-interactive-sessions-in-amazon-sagemaker-unified-studio/").
