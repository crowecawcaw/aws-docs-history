

# Prerequisites
<a name="aurora-analytics-prerequisites"></a>

Your Aurora PostgreSQL DB cluster can read Iceberg and Parquet data from Amazon S3, Amazon S3 Tables, and the AWS Glue Data Catalog on your behalf. Before you query that data, the cluster needs three things: a way to authenticate to those services, an engine version that includes the `aurora_analytics` extension, and a network path from your VPC to reach them. The following sections walk you through creating an IAM policy and role that grant read access to the specific data you plan to query, attaching that role to your DB cluster, enabling the extension in your DB cluster parameter group, and configuring the network path your cluster uses to reach Amazon S3 and AWS Glue. You can complete these steps on any existing Aurora PostgreSQL DB cluster that meets the version requirement.

**Topics**
+ [Overview of setup steps](#aurora-analytics-setup-overview)
+ [Creating an IAM policy](#aurora-analytics-setup-iam-policy)
+ [Creating an IAM role](#aurora-analytics-setup-iam-role)
+ [Attaching the IAM role to the Aurora DB cluster](#aurora-analytics-setup-attach-role)
+ [Set up networking](#aurora-analytics-setup-networking)
+ [Enabling the feature in the parameter group](#aurora-analytics-setup-parameter-group)
+ [Next steps](#aurora-analytics-setup-next-steps)

## Overview of setup steps
<a name="aurora-analytics-setup-overview"></a>

The high-level setup steps are as follows:

1. Create an IAM policy that grants read access to your data.

1. Create an IAM role and attach that policy.

1. Attach the IAM role to the Aurora DB cluster.

1. Set up networking (VPC endpoints) if your cluster is in a private subnet.

1. Enable the `aurora_analytics` extension in the DB cluster parameter group.

## Creating an IAM policy
<a name="aurora-analytics-setup-iam-policy"></a>

Create an IAM policy that grants the extension read access to Amazon S3, and optionally to AWS Glue Data Catalog or Amazon S3 Tables, depending on the format of your data and where it's stored.

The minimum privileges depend on how you reference the data: the data format (Parquet or Iceberg), the source (Amazon S3, AWS Glue Data Catalog, or Amazon S3 Tables), and whether you point at a single file or a directory. The following table lists the minimum IAM role privileges for the common same-account scenarios:


**Minimum IAM role privileges by source**  

| Source | Minimum privileges | 
| --- | --- | 
| Amazon S3, single file (s3://bucket/path/data.parquet) | s3:GetObject | 
| Amazon S3, directory or glob (s3://bucket/path/) | s3:GetObject, s3:ListBucket | 
| AWS Glue Data Catalog (arn:aws:glue:us-east-1:123456789012:table/mydb/mytable) | glue:GetTable \+ Amazon S3 privileges above | 
| Amazon S3 Tables, direct ARN (arn:aws:s3tables:us-east-1:123456789012:bucket/mybucket/table/table\_id) | s3tables:GetTable, s3tables:GetTableBucket, s3tables:GetTableData, s3tables:GetNamespace | 
| Amazon S3 Tables, via AWS Glue catalog ARN (arn:aws:glue:us-east-1:123456789012:table/s3tablescatalog/mybucket/myns/mytable) | glue:GetTable \+ s3tables privileges above | 

**Note**  
`s3:ListBucket` is only needed when the extension lists an Amazon S3 prefix to discover files (for example, Parquet directory or glob access). Iceberg resolves exact file paths from its manifests, which means `s3:ListBucket` is not required.

**Note**  
If your data is encrypted with SSE-KMS, add `kms:Decrypt` on the KMS key.

**Note**  
Additional privileges are required for `IMPORT FOREIGN SCHEMA` (`glue:GetTables` or `s3tables:ListTables`), cross-account access, resource-policy-based access, and Lake Formation-governed tables.

For detailed policy examples, see [IAM policies reference](aurora-analytics-iam-policies-reference.md). For more information about creating IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

## Creating an IAM role
<a name="aurora-analytics-setup-iam-role"></a>

Create an IAM role that Aurora can assume to access your Amazon S3 data on behalf of the extension.

**To create an IAM role using the AWS Management Console**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, then choose **Create role**.

1. For **Trusted entity type**, choose **AWS service**.

1. For **Use case**, choose **RDS** from the service list.

1. Choose **RDS - Add Role to Database** from the use case options.

1. Choose **Next**.

1. Select the policy that you created in [Creating an IAM policy](#aurora-analytics-setup-iam-policy). You can also choose pre-built permissions policies such as **AmazonS3ReadOnlyAccess** and **AWSGlueConsoleFullAccess**.

1. Choose **Next**.

1. For **Role name**, enter a name for the role (for example, `AuroraAnalyticsRole`).

1. Choose **Create role**.

**To create an IAM role using the AWS CLI**

1. Create a role named `AuroraAnalyticsRole`:

   ```
   aws iam create-role \
     --role-name AuroraAnalyticsRole \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "rds.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }'
   ```

1. Attach the policy to the role:

   ```
   aws iam attach-role-policy \
     --role-name AuroraAnalyticsRole \
     --policy-arn arn:aws:iam::123456789012:policy/AuroraAnalyticsReadAccess
   ```

Note the role ARN. You need it when you attach the role to your Aurora DB cluster. For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

## Attaching the IAM role to the Aurora DB cluster
<a name="aurora-analytics-setup-attach-role"></a>

After you create the DB cluster, associate the IAM role that you created for the extension.

**To attach the IAM role using the AWS Management Console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the name of your Aurora PostgreSQL DB cluster.

1. On the **Connectivity & security** tab, in the **Manage IAM roles** section, choose the role to add under **Add IAM roles to this cluster**.

1. For **Feature**, choose **AuroraAnalytics**.

1. Choose **Add role**.

**To attach the IAM role using the AWS CLI**
+ 

  ```
  aws rds add-role-to-db-cluster \
    --region us-east-1 \
    --db-cluster-identifier my-analytics-cluster \
    --feature-name AuroraAnalytics \
    --role-arn arn:aws:iam::123456789012:role/AuroraAnalyticsRole
  ```

The IAM role status shows as **Active** after it is successfully attached. For more information, see [add-role-to-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/add-role-to-db-cluster.html) in the *AWS CLI Command Reference*.

## Set up networking
<a name="aurora-analytics-setup-networking"></a>

When your Aurora DB cluster is deployed in a private subnet, it needs a network path to reach Amazon S3 and (optionally) AWS Glue. You can provide this with VPC endpoints (recommended) or through a NAT gateway.

VPC endpoints keep traffic on the AWS network without traversing the public internet, and an Amazon S3 gateway endpoint has no additional hourly charge, which makes them the recommended approach. A NAT gateway also works if your VPC already routes outbound traffic through one, but it sends traffic over a public path and incurs NAT data-processing charges. The rest of this section describes the VPC endpoint setup. For more information about NAT gateways, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).


**Required VPC endpoints**  

| Service | Endpoint type | Required for | 
| --- | --- | --- | 
| Amazon S3 (com.amazonaws.region.s3) | Gateway | Amazon S3 and Amazon S3 Tables data access | 
| AWS Glue (com.amazonaws.region.glue) | Interface | AWS Glue Data Catalog access | 

### Creating an Amazon S3 gateway endpoint
<a name="aurora-analytics-setup-s3-gateway-endpoint"></a>

Create an Amazon S3 gateway endpoint and associate it with the route tables used by your Aurora DB cluster's subnets.

For more information, see [Creating a gateway endpoint for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the *AWS PrivateLink Guide*.

### Creating an AWS Glue interface endpoint
<a name="aurora-analytics-setup-glue-interface-endpoint"></a>

If you are using AWS Glue Data Catalog, create an AWS Glue VPC interface endpoint with the following configuration:
+ Deploy in the same subnets as your Aurora DB cluster.
+ Enable **Private DNS**.
+ Attach a security group that allows inbound traffic on TCP port 443 from your VPC CIDR block, or from the same security group used by your Aurora PostgreSQL DB cluster.

For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## Enabling the feature in the parameter group
<a name="aurora-analytics-setup-parameter-group"></a>

The `aurora_analytics.enabled` parameter is set to `false` by default. After you create the DB cluster, enable the feature by setting this parameter to `true` in the DB cluster parameter group.

**To enable the feature using the AWS CLI**
+ 

  ```
  aws rds modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name my-analytics-params \
    --parameters "ParameterName=aurora_analytics.enabled,ParameterValue=true,ApplyMethod=immediate"
  ```

As a dynamic parameter, `aurora_analytics.enabled` applies immediately without a reboot.

**Note**  
This applies when your DB cluster uses a *custom* DB cluster parameter group. You can't modify the *default* parameter group. If your cluster still uses the default, first create a custom DB cluster parameter group and associate it with the cluster. Associating a different parameter group requires a reboot of the DB instances for the new group to take effect, even though `aurora_analytics.enabled` itself is dynamic. For more information, see [Working with DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithDBClusterParamGroups.html) in the *Aurora User Guide*.

**To enable the feature using the AWS Management Console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

1. Choose the parameter group associated with your Aurora DB cluster.

1. Search for `aurora_analytics.enabled`.

1. Set the value to `true`.

1. Choose **Save changes**.

## Next steps
<a name="aurora-analytics-setup-next-steps"></a>

After you complete these steps, you're ready to get started. For more information, see [Getting started](aurora-analytics-getting-started.md).

For guidance on choosing the right DB instance class and sizing for your workload, see [Best practices](aurora-analytics-best-practices.md).