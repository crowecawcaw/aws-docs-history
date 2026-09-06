

# Setting up trusted identity propagation for AWS Glue Data Catalog
<a name="catalog-integration-glue-tip"></a>

Trusted identity propagation enables AWS services to access resources based on the end user's identity context. When you configure Quick, AWS Glue Data Catalog, Amazon S3 Access Grants, and Lake Formation with AWS IAM Identity Center, the signed-in user's identity is propagated across services. Lake Formation and S3 Access Grants make authorization decisions based on permissions defined for that user or their group membership from your identity provider.

**Important**  
Trusted identity propagation with AWS Glue Data Catalog requires AWS IAM Identity Center. It is not supported for other authentication methods.

## Prerequisites
<a name="catalog-integration-glue-tip-prerequisites"></a>

**Important**  
Your AWS IAM Identity Center instance, Lake Formation, AWS Glue Data Catalog, and Amazon S3 Access Grants must all be deployed in the same AWS Region.
+ **Configure Quick with AWS IAM Identity Center** – Trusted identity propagation is supported only for Quick accounts integrated with AWS IAM Identity Center. To create AWS Glue Data Catalog data sources with identity propagation, you must be an AWS IAM Identity Center user (author).
+ **AWS Glue Data Catalog must be managed by Lake Formation** – Lake Formation must enforce permissions on your databases and tables. If a database or table still grants `Super` to `IAMAllowedPrincipals`, Lake Formation does not enforce per-user permissions.
+ **Lake Formation must be integrated with AWS IAM Identity Center** – Use the same AWS IAM Identity Center instance that Quick uses. This integration allows Lake Formation to recognize a propagated user identity.
+ **Register data S3 locations with Lake Formation** – When a user queries a table, Lake Formation vends temporary, scoped S3 credentials for the data. The user's query does not need its own S3 permissions on the data bucket. Register the location for all table formats (Parquet, Apache Iceberg, S3 Tables).
+ **Grant permissions to IAM Identity Center users and groups in Lake Formation** – Configure permissions and any row, column, or cell data filters to control which catalogs, databases, tables, rows, and columns each user can access.
+ **Quick administrator authorizes the connection** – With trusted identity propagation, the Quick role does not need direct S3 permissions on the table data. Lake Formation vends those credentials.
+ **S3 Access Grants on the Athena results bucket** – Glue queries execute through the Athena engine, which writes results to the query results bucket. That bucket is governed by S3 Access Grants (separate from Lake Formation). Each user or group may need an S3 Access Grant (READ/WRITE) on the results bucket.

## Step 1: Enable the Lake Formation – AWS IAM Identity Center integration
<a name="catalog-integration-glue-tip-step1"></a>

Lake Formation must be connected to your AWS IAM Identity Center instance so it can recognize identities propagated from Quick. This is a one-time, account-level and Region-level step. If you already use Athena trusted identity propagation, this step is already complete. You must be a Lake Formation data lake administrator.

**Console:** In the Lake Formation console, choose **Administration**, **IAM Identity Center integration**, and then **Create**. Select your AWS IAM Identity Center instance.

**AWS CLI:**

```
aws lakeformation create-lake-formation-identity-center-configuration \
    --catalog-id 111122223333 \
    --instance-arn arn:aws:sso:::instance/<idc-instance-id> \
    --region us-west-2
```

This command creates the Lake Formation AWS IAM Identity Center application. Note the `ApplicationArn` from the response. You use it as the authorized target when you configure identity propagation.

To retrieve the application ARN later, run:

```
aws lakeformation describe-lake-formation-identity-center-configuration \
    --catalog-id 111122223333 \
    --region us-west-2
```

The response includes an `ApplicationArn` in the following format:

```
arn:aws:sso::111122223333:application/<idc-instance-id>/<lf-application-id>
```

## Step 2: Configure the IAM role with required permissions
<a name="catalog-integration-glue-tip-step2"></a>

Your Quick account must use an IAM role with the required permissions. If your account already uses a custom IAM role, modify it. Otherwise, create a new role.

**Required trust policy:**

The role's trust policy must allow the Quick service principal to assume it and attach the user's identity context to the session:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": { "Service": "quicksight.amazonaws.com" },
        "Action": ["sts:AssumeRole", "sts:TagSession", "sts:SetContext"]
    }]
}
```

**Note**  
`sts:SetContext` is required so that the user's AWS IAM Identity Center identity context can be attached to the assumed-role session.

**Required permissions:**

The role needs permissions to read AWS Glue Data Catalog metadata and obtain Lake Formation vended data access. The role does not need direct `s3:*` permissions on the table data because Lake Formation vends scoped, temporary S3 credentials.

```
"Action": [
    "glue:GetCatalog", "glue:GetCatalogs",
    "glue:GetDatabase", "glue:GetDatabases",
    "glue:GetTable", "glue:GetTables",
    "glue:GetConnection", "glue:GetConnections",
    "glue:GetTags", "glue:ListDataQualityResults",
    "glue:GetDataQualityResult",
    "lakeformation:GetTemporaryGlueTableCredentials",
    "lakeformation:GetDataAccess"
]
```

## Step 3: Configure the Quick account to use the IAM role
<a name="catalog-integration-glue-tip-step3"></a>

This step must be completed by the Quick administrator.

1. In the Quick console, choose your profile icon and then choose **Manage Quick**.

1. Choose **Security & permissions**.

1. Under **Quick access to AWS services**, choose **Manage**.

1. Find or add the **Glue Data Catalog** resource.

1. Select the IAM role that you configured in Step 2.

1. Under **Amazon S3**, allow access to the Athena query results bucket.

1. Choose **Update**.

## Step 4: Update the identity propagation configuration
<a name="catalog-integration-glue-tip-step4"></a>

Run the following AWS CLI command to enable identity propagation for Data Catalog:

```
aws quicksight update-identity-propagation-config \
    --aws-account-id 111122223333 \
    --service GLUE_DATA_CATALOG \
    --authorized-targets arn:aws:sso::111122223333:application/<idc-instance-id>/<lf-application-id>
```

The `--authorized-targets` value is the Lake Formation AWS IAM Identity Center application ARN that you obtained in Step 1. This tells Quick which AWS IAM Identity Center application to propagate identity to.

To verify, run:

```
aws quicksight list-identity-propagation-configs \
    --aws-account-id 111122223333
```

Confirm that `GLUE_DATA_CATALOG` appears in the services list.

## Step 5: Create a AWS Glue Data Catalog data source
<a name="catalog-integration-glue-tip-step5"></a>

When the author creates a AWS Glue Data Catalog data source, Quick validates accessibility by listing catalogs using the signed-in user's propagated identity. The user sees only the catalogs, databases, and tables that their Lake Formation grants allow.

## Verifying the setup
<a name="catalog-integration-glue-tip-verify"></a>

Use the following checklist to verify your configuration:
+ The Lake Formation–AWS IAM Identity Center integration returns an `ApplicationArn`.
+ Identity propagation scope shows `GLUE_DATA_CATALOG`.
+ The IAM role has correct permissions and `sts:SetContext` in the trust policy.
+ Data S3 locations are registered with Lake Formation.
+ Lake Formation grants are configured for IAM Identity Center users and groups.
+ S3 Access Grants are configured on the Athena results bucket (if applicable).
+ End-to-end test: sign in as a test user, create a data source, and query a table.

## Key considerations and limits
<a name="catalog-integration-glue-tip-considerations"></a>
+ Permissions are evaluated against the IAM Identity Center end user and their groups.
+ The query path runs through Athena. Each user needs S3 Access Grants on the Athena results bucket.
+ A data filter has no effect if a full-table `SELECT` is also granted to the same user.
+ Best practice: Grant permissions to groups rather than individual users for easier management.
+ S3 Access Grants are eventually consistent. Newly added grants may take minutes to propagate.
+ Configure fine-grained access control (row, column, and cell filters) in Lake Formation.
+ Scope-down policies are evaluated against the end user's identity.

For information about Athena trusted identity propagation, see [Amazon Athena trusted identity propagation](https://docs.aws.amazon.com/quicksuite/latest/userguide/athena#athena-trusted-identity-propagation).