

# Granting cross-account access
<a name="cross-account-access"></a>

Granting access to Data Catalog resources across accounts enables your extract, transform, and load (ETL) jobs to query and join data from different accounts.

**Topics**
+ [Methods for granting cross-account access in AWS Glue](#cross-account-how-works)
+ [Adding or updating the Data Catalog resource policy](#cross-account-adding-resource-policy)
+ [Making a cross-account API call](#cross-account-calling)
+ [Making a cross-account ETL call](#cross-account-calling-etl)
+ [Cross-account CloudTrail logging](#cross-account-ct-logs)
+ [Cross-account resource ownership and billing](#cross-account-ownership-and-billing)
+ [Cross-account access limitations](#cross-account-limitations)

## Methods for granting cross-account access in AWS Glue
<a name="cross-account-how-works"></a>

You can grant access to your data to external AWS accounts by using AWS Glue methods or by using AWS Lake Formation cross-account grants. The AWS Glue methods use AWS Identity and Access Management (IAM) policies to achieve fine-grained access control. Lake Formation uses a simpler `GRANT/REVOKE` permissions model similar to the `GRANT/REVOKE` commands in a relational database system.

This section describes using the AWS Glue methods. For information about using Lake Formation cross-account grants, see [Granting Lake Formation Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html) in the *AWS Lake Formation Developer Guide*.

There are two AWS Glue methods for granting cross-account access to a resource:
+ Use a Data Catalog resource policy
+ Use an IAM role

**Granting cross-account access using a resource policy**  
The following are the general steps for granting cross-account access using a Data Catalog resource policy:

1. An administrator (or other authorized identity) in Account A attaches a resource policy to the Data Catalog in Account A. This policy grants Account B specific cross-account permissions to perform operations on a resource in Account A's catalog.

1. An administrator in Account B attaches an IAM policy to an IAM identity in Account B that delegates the permissions received from Account A.

   The identity in Account B now has access to the specified resource in Account A.

   The identity needs permission from *both* the resource owner (Account A) *and* their parent account (Account B) to be able to access the resource.

**Granting cross-account access using an IAM role**  
The following are the general steps for granting cross-account access using an IAM role:

1. An administrator (or other authorized identity) in the account that owns the resource (Account A) creates an IAM role.

1. The administrator in Account A attaches a policy to the role that grants cross-account permissions for access to the resource in question.

1. The administrator in Account A attaches a trust policy to the role that identifies an IAM identity in a different account (Account B) as the principal who can assume the role.

   The principal in the trust policy can also be an AWS service principal if you want to grant an AWS service permission to assume the role.

1. An administrator in Account B now delegates permissions to one or more IAM identities in Account B so that they can assume that role. Doing so gives those identities in Account B access to the resource in account A.

For more information about using IAM to delegate permissions, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*. For more information about users, groups, roles, and permissions, see [Identities (users, groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

For a comparison of these two approaches, see [How IAM roles differ from resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html) in the *IAM User Guide*. AWS Glue supports both options, with the restriction that a resource policy can grant access only to Data Catalog resources.

For example, to give the `Dev` role in Account B access to database `db1` in Account A, attach the following resource policy to the catalog in Account A.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase"
      ],
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:role/Dev"
        ]
      },
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/db1"
      ]
    }
  ]
}
```

------

In addition, Account B would have to attach the following IAM policy to the `Dev` role before it would actually get access to `db1` in Account A.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/db1"
      ]
    }
  ]
}
```

------

## Adding or updating the Data Catalog resource policy
<a name="cross-account-adding-resource-policy"></a>

You can add or update the AWS Glue Data Catalog resource policy using the console, API, or AWS Command Line Interface (AWS CLI).

**Important**  
If you have already made cross-account permission grants from your account with AWS Lake Formation, adding or updating the Data Catalog resource policy requires an extra step. For more information, see [Managing cross-account permissions using both AWS Glue and Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-cross-account.html) in the *AWS Lake Formation Developer Guide*.  
To determine if Lake Formation cross-account grants exist, use the `glue:GetResourcePolicies` API operation or the AWS CLI. If `glue:GetResourcePolicies` returns any policies other than an already existing Data Catalog policy, then Lake Formation grants exist. For more information, see [Viewing all cross-account grants using the GetResourcePolicies API operation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-getresourcepolicies.html) in the *AWS Lake Formation Developer Guide*.

**To add or update the Data Catalog resource policy (console)**

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

   Sign in as an AWS Identity and Access Management (IAM) administrative user who has the `glue:PutResourcePolicy` permission.

1. In the navigation pane, choose **Settings**.

1. On the **Data catalog settings** page, under **Permissions**, paste a resource policy into the text area. Then choose **Save**.

   If the console displays a alert stating that the permissions in the policy will be in addition to any permissions granted using Lake Formation, choose **Proceed**.

**To add or update the Data Catalog resource policy (AWS CLI)**
+ Submit an `aws glue put-resource-policy` command. If Lake Formation grants already exist, ensure that you include the `--enable-hybrid` option with the value `'TRUE'`.

  For examples of using this command, see [Resource-based policy examples for AWS Glue](security_iam_resource-based-policy-examples.md).

## Making a cross-account API call
<a name="cross-account-calling"></a>

All AWS Glue Data Catalog operations have a `CatalogId` field. If the required permissions have been granted to enable cross-account access, a caller can make Data Catalog API calls across accounts. The caller does this by passing the target AWS account ID in `CatalogId` so as to access the resource in that target account.

If no `CatalogId` value is provided, AWS Glue uses the caller's own account ID by default, and the call is not cross-account.

## Making a cross-account ETL call
<a name="cross-account-calling-etl"></a>

Some AWS Glue PySpark and Scala APIs have a catalog ID field. If all the required permissions have been granted to enable cross-account access, an ETL job can make PySpark and Scala calls to API operations across accounts by passing the target AWS account ID in the catalog ID field to access Data Catalog resources in a target account.

If no catalog ID value is provided, AWS Glue uses the caller's own account ID by default, and the call is not cross-account.

For PySpark APIs that support `catalog_id`, see [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md). For Scala APIs that support `catalogId`, see [AWS Glue Scala GlueContext APIs](glue-etl-scala-apis-glue-gluecontext.md).

The following example shows the permissions required by the grantee to run an ETL job. In this example, {{grantee-account-id}} is the `catalog-id` of the client running the job and {{grantor-account-id}} is the owner of the resource. This example grants permission to all catalog resources in the grantor's account. To limit the scope of resources granted, you can provide specific ARNs for the catalog, database, table, and connection.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetConnection",
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:GetPartition"
      ],
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:root"
        ]
      },
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:*"
      ]
    }
  ]
}
```

------

**Note**  
If a table in the grantor's account points to an Amazon S3 location that is also in the grantor's account, the IAM role used to run an ETL job in the grantee's account must have permission to list and get objects from the grantor's account.

Given that the client in Account A already has permission to create and run ETL jobs, the following are the basic steps to set up an ETL job for cross-account access:

1. Allow cross-account data access (skip this step if Amazon S3 cross-account access is already set up).

   1. Update the Amazon S3 bucket policy in Account B to allow cross-account access from Account A.

   1. Update the IAM policy in Account A to allow access to the bucket in Account B.

1. Allow cross-account Data Catalog access.

   1. Create or update the resource policy attached to the Data Catalog in Account B to allow access from Account A.

   1. Update the IAM policy in Account A to allow access to the Data Catalog in Account B.

## Cross-account CloudTrail logging
<a name="cross-account-ct-logs"></a>

When an AWS Glue extract, transform, and load (ETL) job accesses the underlying data of a Data Catalog table shared through AWS Lake Formation cross-account grants, there is additional AWS CloudTrail logging behavior.

For purposes of this discussion, the AWS account that shared the table is the owner account, and the account that the table was shared with is the recipient account. When an ETL job in the recipient account accesses data in the table in the owner account, the data-access CloudTrail event that is added to the logs for the recipient account gets copied to the owner account's CloudTrail logs. This is so owner accounts can track data accesses by the various recipient accounts. By default, the CloudTrail events do not include a human-readable principal identifier (principal ARN). An administrator in the recipient account can opt in to include the principal ARN in the logs.

For more information, see [Cross-account CloudTrail logging](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-logging.html) in the *AWS Lake Formation Developer Guide*.

**See Also**  
[Logging and monitoring in AWS Glue](logging-and-monitoring.md)

## Cross-account resource ownership and billing
<a name="cross-account-ownership-and-billing"></a>

When a user in one AWS account (Account A) creates a new resource such as a database in a different account (Account B), that resource is then owned by Account B, the account where it was created. An administrator in Account B automatically gets full permissions to access the new resource, including reading, writing, and granting access permissions to a third account. The user in Account A can access the resource that they just created only if they have the appropriate permissions granted by Account B.

Storage costs and other costs that are directly associated with the new resource are billed to Account B, the resource owner. The cost of requests from the user who created the resource are billed to the requester's account, Account A.

 For more information about AWS Glue billing and pricing, see [How AWS Pricing Works](https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf).

## Cross-account access limitations
<a name="cross-account-limitations"></a>

AWS Glue cross-account access has the following limitations:
+ Cross-account access to AWS Glue is not allowed if you created databases and tables using Amazon Athena orAmazon Redshift Spectrum prior to a region's support for AWS Glue and the resource owner account has not migrated the Amazon Athena data catalog to AWS Glue. You can find the current migration status using the [GetCatalogImportStatus (get\_catalog\_import\_status)](aws-glue-api-catalog-migration.md#aws-glue-api-catalog-migration-GetCatalogImportStatus). For more details on how to migrate an Athena catalog to AWS Glue, see [Upgrading to the AWS Glue Data Catalog step-by-step](https://docs.aws.amazon.com/athena/latest/ug/glue-upgrade.html) in the *Amazon Athena User Guide*.
+ Cross-account access is *only* supported for Data Catalog resources, including databases, tables, user-defined functions, and connections.
+ Cross-account access to the Data Catalog from Athena requires you to register the catalog as an Athena `DataCatalog` resource. For instructions, see [Registering an AWS Glue Data Catalog from another account](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue-cross-account.html) in the *Amazon Athena User Guide*.