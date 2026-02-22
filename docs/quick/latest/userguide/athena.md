# Authorizing connections to Amazon Athena

If you need use Amazon Quick Sight with Amazon Athena or Amazon Athena Federated
Query, you first need to authorize connections to Athena and the associated buckets in
Amazon Simple Storage Service (Amazon S3). Amazon Athena is an interactive query service that makes it easy to analyze
data directly in Amazon S3 using standard SQL. Athena Federated Query provides access to more
types of data by using AWS Lambda. Using a connection from Quick to Athena,
you can write SQL queries to interrogate data that's stored in relational,
non-relational, object, and custom data sources. For more information, see [Using
Athena federated query](../../../athena/latest/ug/connect-to-a-data-source.md "../../../athena/latest/ug/connect-to-a-data-source.md") in the Amazon Athena User Guide.

Review the following considerations when setting up access to Athena from
Quick:

- Athena stores query results from Amazon Quick Sight in a bucket. By default, this bucket
  has a name similar to
  `aws-athena-query-results-AWSREGION-AWSACCOUNTID`, for example
  `aws-athena-query-results-us-east-2-111111111111`. Therefore, it's
  important to make sure Amazon Quick Sight has permissions to access the bucket Athena is
  currently using.
- If your data file is encrypted with an AWS KMS key, grant permissions to the
  Amazon Quick Sight IAM role to decrypt the key. The easiest way to do this is to use the
  AWS CLI.

You can run the KMS [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") API operation in AWS CLI to do this.

```
aws kms create-grant --key-id <KMS_KEY_ARN> /
--grantee-principal `<QS_ROLE_ARN>` --operations Decrypt
```

The Amazon Resource Name (ARN) for the Amazon Quick role has the format
`arn:aws:iam::<account
 id>:role/service-role/aws-quicksight-s3-consumers-role-v<version
 number>` and can be accessed from the IAM console. To find your KMS
key ARN, use the S3 console. Go to the bucket that contains your data file and
choose the **Overview** tab. The key is located near
**KMS key ID**.

- For Amazon Athena, Amazon S3, and Athena Query Federation connections, Amazon Quick uses
  the following IAM role by default:

```
arn:aws:iam::`AWS-ACCOUNT-ID`:role/service-role/aws-quicksight-s3-consumers-role-v0
```

If the `aws-quicksight-s3-consumers-role-v0` is not present, then
Amazon Quick uses:

```
arn:aws:iam::`AWS-ACCOUNT-ID`:role/service-role/aws-quicksight-service-role-v0
```

- If you assigned scope-down policies to your users, verify that the policies
  contain the `lambda:InvokeFunction` permission. Without this
  permission, your users can't access Athena Federated Queries. For more
  information about assigning IAM policies to your users in Amazon Quick, see
  [Setting granular access to AWS services through
  IAM](../../../quicksight/latest/user/scoping-policies-iam-interface.md "../../../quicksight/latest/user/scoping-policies-iam-interface.md"). For more information about the lambda:InvokeFunction
  permission, see [Actions, resources, and
  condition keys for AWS Lambda](../../../IAM/latest/UserGuide/list_awslambda.md "../../../IAM/latest/UserGuide/list_awslambda.md") in the
  _IAM User Guide_.

###### To authorize Amazon Quick to connect to Athena or Athena federated data

sources

1. (Optional) If you are using AWS Lake Formation with Athena, you also need to enable Lake Formation.
   For more information, see [Authorizing connections through AWS Lake Formation](../../../quicksight/latest/user/lake-formation.md "../../../quicksight/latest/user/lake-formation.md").
2. Open your profile menu at top right and choose **Manage
   QuickSight**. You must be a Amazon Quick administrator to do this.
   If you don't see **Manage QuickSight** on the profile menu, you
   don't have sufficient permissions.
3. Choose **Security & permissions**, **Add or
   remove**.
4. Choose the box near Amazon Athena, **Next**.

If it was already enabled, you might have to double-click it. Do this even if
Amazon Athena is already enabled, so you can view the settings. No changes are saved
until you choose **Update** at the end of this
procedure. 5. Enable the S3 buckets you want to access. 6. (Optional) To enable Athena federated queries, select the Lambda functions you
want to use.

###### Note

You can only see Lambda functions for the Athena catalogs in the same
region of Amazon Quick. 7. To confirm your changes, choose **Finish**.

To cancel, choose **Cancel**. 8. To save changes to security and permissions, choose
**Update**.

###### To test the connection authorization settings

1. From the Amazon Quick start page, choose **Datasets**,
   **New dataset**.
2. Choose the Athena card.
3. Follow the screen prompts to create a new Athena data source using the
   resources you need to connect to. Choose **Validate
   connection** to test the connection.
4. If the connection validates, you have successfully configured an Athena or
   Athena Federated Query connection.

If you don't have sufficient permissions to connect to an Athena dataset or run
an Athena query, an error displays directing you to contact a Amazon Quick
administrator. This error means need to recheck your connection authorization
settings to find the discrepancy. 5. After you can connect successfully, you or your Amazon Quick authors can
create data sources connections and share them with other Amazon Quick authors.
The authors can then create multiple datasets from the connections, to use in
Amazon Quick dashboards.

For troubleshooting information on Athena, see [Connectivity issues when using Athena with Amazon Quick](../../../quicksight/latest/user/troubleshoot-athena.md "../../../quicksight/latest/user/troubleshoot-athena.md").

## Using trusted identity

propagation with Athena

Trusted identity propagation gives AWS services access to AWS resources based
on the user’s identity context and securely shares this user’s identity with other
AWS services. These capabilities enable user access to be more easily defined,
granted, and logged.

When administrators configure Quick, Athena, Amazon S3 Access Grants, and
AWS Lake Formation with IAM Identity Center, they can now enable trusted identity propagation across these
services and allow the user’s identity to be propagated across services. When data
is accessed from Quick by an IAM Identity Center user, Athena or Lake Formation can make
authorization decisions using the permissions defined for their user or group
membership from the organization’s identity provider.

Trusted identity propagation with Athena only works when permissions are managed
through Lake Formation. User permissions to data reside in Lake Formation.

### Prerequisites

Before you get started, make sure that you have the following required
prerequisites completed.

###### Important

As you complete the following prerequisites, note that your IAM Identity Center
instance, Athena workgroup, Lake Formation and Amazon S3 Access Grants must all be deployed
in the same AWS Region.

- Configure your Quick account with IAM Identity Center. Trusted identity
  propagation is only supported for Quick accounts that are
  integrated with IAM Identity Center. For more information, see [Configure your Amazon Quick
  account with IAM Identity Center](setting-up-sso.md#sec-identity-management-identity-center "setting-up-sso.md#sec-identity-management-identity-center").

###### Note

To create Athena data sources, you must be an IAM Identity Center user (author)
in a Quick account that uses IAM Identity Center.

- An Athena workgroup that is enabled with IAM Identity Center. The Athena workgroup
  that you use must be using the same IAM Identity Center instance as the
  Quick account. For more information about configuring an
  Athena workgroup, see [Creating an IAM Identity Center enabled Athena workgroup.](../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-creating-an-identity-center-enabled-athena-workgroup "../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-creating-an-identity-center-enabled-athena-workgroup") in the
  _Amazon Athena User Guide_.
- Access to Athena query results bucket is managed with Amazon S3 Access
  Grants. For more details, see [Managing access
  with Amazon S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md") in the
  _Amazon S3 User Guide_. If your query results are
  encrypted with an AWS KMS key, the Amazon S3 Access Grant IAM role and the
  Athena workgroup role both need permissions to AWS KMS.
  - For more information, see [Amazon S3
    Access Grants and corporate directory identities](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md") in
    the Amazon S3 User Guide.
  - The Amazon S3 Access Grant role should have the
    `STS:SetContext` action in its trust policy for
    identity propagation. To see an example, see [Register a location](../../../AmazonS3/latest/userguide/access-grants-location-register.md "../../../AmazonS3/latest/userguide/access-grants-location-register.md") in the Amazon S3 User Guide.

- Permissions to data must be managed with Lake Formation and Lake Formation must be
  configured with the same IAM Identity Center instance as Quick and the
  Athena workgroup. For configuration information, see [Integrating IAM Identity Center](../../../lake-formation/latest/dg/identity-center-integration.md "../../../lake-formation/latest/dg/identity-center-integration.md") in the
  _AWS Lake Formation Developer Guide_.
- The data lake administrator needs to grant permissions to IAM Identity Center users
  and groups in Lake Formation. For more details, [Granting
  permissions to users and groups](../../../lake-formation/latest/dg/grant-permissions-sso.md "../../../lake-formation/latest/dg/grant-permissions-sso.md") in the
  _AWS Lake Formation Developer Guide_.
- The Quick administrator needs to authorize connections to
  Athena. For details, see [Authorizing connections to Amazon Athena](athena.md "athena.md").
  Note, with trusted identity propagation, you do not need to give the
  Quick role Amazon S3 bucket permissions or AWS KMS permissions. You
  need to keep your users and groups that have permissions to the
  workgroup in Athena in sync with the Amazon S3 bucket that stores query
  results with Amazon S3 Access Grants permissions so that users can
  successfully run queries and retrieve query results in the Amazon S3 bucket
  using trusted identity propagation.

### Configure

IAM role with required permissions

To use trusted identity propagation with Athena, your Quick account
must have the required permissions to access your resources. To provide those
permissions, you must configure your Quick account to use an IAM
role with the permissions.

If your Quick account is already using a custom IAM role, you
can modify that one. If you do not have an existing IAM role, create one by
following the instructions in [Create a role for
an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

The IAM role you create or modify must contain the following trust policy
and permissions.

#### Required trust policy

For information about updating the trust policy of an IAM role, see
[Update
a role trust policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md").

#### Required Athena permissions

For information about updating the trust policy of an IAM role, see
[Update
permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md").

###### Note

The `Resource` uses the `*` wildcard. We
recommend that you update it to include only the Athena resources you
want to use with Quick.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:BatchGetQueryExecution",
 "athena:CancelQueryExecution",
 "athena:GetCatalogs",
 "athena:GetExecutionEngine",
 "athena:GetExecutionEngines",
 "athena:GetNamespace",
 "athena:GetNamespaces",
 "athena:GetQueryExecution",
 "athena:GetQueryExecutions",
 "athena:GetQueryResults",
 "athena:GetQueryResultsStream",
 "athena:GetTable",
 "athena:GetTables",
 "athena:ListQueryExecutions",
 "athena:RunQuery",
 "athena:StartQueryExecution",
 "athena:StopQueryExecution",
 "athena:ListWorkGroups",
 "athena:ListEngineVersions",
 "athena:GetWorkGroup",
 "athena:GetDataCatalog",
 "athena:GetDatabase",
 "athena:GetTableMetadata",
 "athena:ListDataCatalogs",
 "athena:ListDatabases",
 "athena:ListTableMetadata"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Configure

your Quick account to use the IAM role

After configuring the IAM role in the previous step, you must configure your
Quick account to use it. For information about how to do that, see
[Using existing IAM roles in
Quick](security-create-iam-role.md#security-create-iam-role-use "security-create-iam-role.md#security-create-iam-role-use").

### Update the

identity propogation config with the AWS CLI

To authorize Quick to propagate end user identities to Athena
workgroups, run the following `update-identity-propagation-config`
API from the AWS CLI, replacing the following values:

- Replace `us-west-2` with the AWS Region
  that your IAM Identity Center instance is in.
- Replace `111122223333` with your
  AWS account ID.

```
aws quicksight update-identity-propagation-config \
--service ATHENA \
--region `us-west-2` \
--aws-account-id `111122223333`
```

### Create an

Athena dataset in Quick

Now, create an Athena dataset in Quick configured with the IAM Identity Center
enabled Athena workgroup you want to connect to. For information about how to
create an Athena dataset, see [Creating a dataset using Amazon Athena
data](create-a-data-set-athena.md "create-a-data-set-athena.md").

### Key callouts, considerations, and limits

The following list contains some important considerations when using trusted
identity propagation with Quick and Athena.

- Quick Athena data sources that use trusted identity
  propagation have Lake Formation permissions evaluated against the IAM Identity Center end user
  and the IAM Identity Center groups that the user might belong to.
- When using Athena data sources that use trusted identity propagation,
  we recommend any fine tuned access control is done in Lake Formation. However, If
  you elect to use Quick’s scope down policy feature, scope
  down policies will be evaluated against the end user.
- The following features are disabled for data sources and data sets
  that use trusted identity propagation: SPICE datasets, Custom SQL on
  data sources, threshold alerts, email reports, Q Topics, stories,
  scenarios, CSV, Excel, and PDF exports, anomaly detection.
- If you experience high latency or timeouts, it may be because of a
  combination of high number of IAM Identity Center groups, Athena databases, tables, and
  Lake Formation rules. We recommend trying to use only the necessary number of
  those resources.
