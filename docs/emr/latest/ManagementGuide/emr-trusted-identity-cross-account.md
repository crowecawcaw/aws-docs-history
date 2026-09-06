

# Cross account setup with trusted identity propagation
<a name="emr-trusted-identity-cross-account"></a>

This tutorial demonstrates how to configure trusted identity propagation (TIP) with Amazon EMR on EC2 in a cross-account scenario. In this setup, an EMR cluster in one AWS account (the consumer account) accesses data governed by Lake Formation in a different AWS account (the producer account), while preserving the end user's identity throughout the request chain.

In a cross-account trusted identity propagation architecture, two accounts participate:
+ **Account A (Producer)** — Owns the data stored in Amazon S3 and registered with Lake Formation. The AWS Glue Data Catalog in this account contains the databases and tables you want to share.
+ **Account B (Consumer)** — Runs the Amazon EMR cluster with trusted identity propagation enabled. Users connect to this cluster through EMR Studio and run Spark queries against data in Account A.

Both accounts must belong to the same AWS Organization, and both must use the same IAM Identity Center organization instance. When a user runs a Spark query from EMR Studio in Account B, the user's identity token is propagated through the EMR cluster to Lake Formation, which evaluates permissions against the shared resources from Account A.

## How it works
<a name="emr-trusted-identity-cross-account-how-it-works"></a>

1. A user authenticates to EMR Studio through IAM Identity Center.

1. EMR Studio passes an identity-enhanced token to the EMR cluster in Account B.

1. The EMR cluster's instance profile role acts as a carrier role, exchanging the token for temporary credentials that include the user's identity context.

1. When the Spark job accesses a resource link pointing to Account A's Data Catalog, Lake Formation evaluates permissions based on the IAM Identity Center user or group.

1. Lake Formation in Account A authorizes access to the underlying Amazon S3 data based on the granted permissions.

## Prerequisites
<a name="emr-trusted-identity-cross-account-prereqs"></a>

**General prerequisites**
+ Both Account A and Account B belong to the same AWS Organization.
+ An IAM Identity Center organization instance is enabled. Account-level instances do not support cross-account trusted identity propagation.
+ Users and groups are provisioned in IAM Identity Center (either manually or synced from an external identity provider such as Okta or Microsoft Entra ID).
+ Amazon EMR release 6.15.0 or later (7.8.0 or later for runtime roles with TIP).
+ Apache Spark is the only engine supported with trusted identity propagation.

**Account B (Consumer) prerequisites**
+ Trusted identity propagation is configured for single-account access as described in [](emr-trusted-identity-prerequisites.md).
+ An EMR security configuration with IAM Identity Center and Lake Formation enabled.
+ An EMR Studio integrated with IAM Identity Center.
+ Lake Formation integrated with IAM Identity Center.
+ The EMR cluster's EC2 instance profile role has the required IAM Identity Center OAuth permissions.

**Account A (Producer) prerequisites**
+ Lake Formation is set up with a data lake administrator defined.
+ Lake Formation is integrated with IAM Identity Center in Account A.
+ The Amazon S3 data location is registered with Lake Formation using a user-defined role (not the service-linked role).
+ Databases and tables exist in the AWS Glue Data Catalog.
+ AWS RAM is enabled for your organization (**Enable sharing with AWS Organizations** is turned on).

Lake Formation IAM Identity Center integration in Account A:

```
aws lakeformation create-lake-formation-identity-center-configuration \
    --catalog-id {{ACCOUNT_A_ID}} \
    --instance-arn "arn:aws:sso:::instance/ssoins-{{INSTANCE_ID}}"
```

## Step 1: Register data location in Account A with a user-defined role
<a name="emr-trusted-identity-cross-account-register-data"></a>

Lake Formation does not support using its service-linked role when you integrate with Amazon EMR for cross-account access. You must register your Amazon S3 data location with a custom IAM role.

**Warning**  
If you previously registered the location with the Lake Formation service-linked role, you must deregister and re-register with a user-defined role.

**Create the data location role**

1. Open the IAM console in Account A.

1. Create a new IAM role with the following trust policy:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "lakeformation.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

1. Attach a policy that allows the role to access the Amazon S3 location:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
               "Resource": [
                   "arn:aws:s3:::{{YOUR-DATA-BUCKET}}",
                   "arn:aws:s3:::{{YOUR-DATA-BUCKET}}/*"
               ]
           }
       ]
   }
   ```

**Register the Amazon S3 location**

```
aws lakeformation register-resource \
    --resource-arn "arn:aws:s3:::{{YOUR-DATA-BUCKET}}" \
    --role-arn "arn:aws:iam::{{ACCOUNT_A_ID}}:role/LakeFormationDataLocationRole" \
    --use-service-linked-role false
```

## Step 2: Grant cross-account permissions from Account A to Account B
<a name="emr-trusted-identity-cross-account-grant-permissions"></a>

In this step, you grant Lake Formation permissions on your database and table to Account B's AWS account ID.

```
aws lakeformation grant-permissions \
    --principal '{"DataLakePrincipalIdentifier": "{{ACCOUNT_B_ID}}"}' \
    --resource '{
        "Table": {
            "DatabaseName": "{{my_database}}",
            "Name": "{{my_table}}",
            "CatalogId": "{{ACCOUNT_A_ID}}"
        }
    }' \
    --permissions '["SELECT", "DESCRIBE"]' \
    --permissions-with-grant-option '["SELECT", "DESCRIBE"]'
```

**Important**  
You must grant with `--permissions-with-grant-option` so that Account B can subsequently grant permissions to IAM Identity Center users and groups. Without grantable permissions, Account B cannot propagate access to individual users.

## Step 3: Enable external data filtering for Amazon EMR in Account A
<a name="emr-trusted-identity-cross-account-external-filtering"></a>

To allow EMR clusters in Account B to apply Lake Formation data filtering, you must opt in to external data filtering in Account A.

**Using the Lake Formation console:**

1. Navigate to **Administration** > **Application integration settings**.

1. Choose **Allow external engines to filter data from these AWS accounts**.

1. Add the Account B ID to the list of allowed AWS account IDs.

1. Select **Amazon EMR** as the allowed engine.

1. Choose **Save**.

**AWS CLI alternative:**

```
aws lakeformation put-data-lake-settings \
    --data-lake-settings '{
        "DataLakeAdmins": [
            {"DataLakePrincipalIdentifier": "arn:aws:iam::{{ACCOUNT_A_ID}}:role/LakeFormationAdmin"}
        ],
        "ExternalDataFilteringAllowList": [
            {"DataLakePrincipalIdentifier": "{{ACCOUNT_B_ID}}"}
        ],
        "AllowExternalDataFiltering": true,
        "AuthorizedSessionTagValueList": ["Amazon EMR"]
    }'
```

## Step 4: Accept the resource share in Account B
<a name="emr-trusted-identity-cross-account-accept-share"></a>

When you grant cross-account permissions in Account A, Lake Formation uses AWS RAM to share the resource with Account B. If your accounts are in the same organization and RAM sharing with Organizations is enabled, the share is auto-accepted. Otherwise, you must manually accept it.

**If auto-accept is not enabled:**

1. Log in to the AWS Management Console with Account B.

1. Open the AWS RAM console.

1. In the navigation pane, choose **Shared with me** > **Resource shares**.

1. Find the pending invitation from Account A and choose **Accept resource share**.

## Step 5: Create resource links in Account B
<a name="emr-trusted-identity-cross-account-create-resource-links"></a>

A resource link is a Data Catalog object that points to a shared database or table in another account. You need resource links so that EMR queries in Account B can reference the shared resources using a local name.

**Create a database resource link**

1. In the Lake Formation console in Account B, navigate to **Databases** and choose **Create database**.

1. Select **Resource link**.

1. For **Resource link name**, enter a local name (for example, `cross_account_db_link`).

1. For **Shared database**, select the database shared from Account A.

1. Choose **Create**.

**AWS CLI alternative:**

```
aws glue create-database \
    --database-input '{
        "Name": "cross_account_db_link",
        "TargetDatabase": {
            "CatalogId": "{{ACCOUNT_A_ID}}",
            "DatabaseName": "{{my_database}}"
        }
    }'
```

## Step 6: Grant permissions on resource links to IAM Identity Center users
<a name="emr-trusted-identity-cross-account-grant-idc-permissions"></a>

This is the critical step that connects IAM Identity Center identities to the shared cross-account data. You must grant two types of permissions:
+ **Permissions on the resource link** — Allows users to see and describe the link.
+ **Permissions on the target resource** — Allows users to actually query the underlying data.

**Note**  
Lake Formation permits IAM roles from external accounts to act as carrier roles on behalf of IAM Identity Center users and groups for accessing Data Catalog resources, but permissions can only be granted on Data Catalog resources within the owning account. This means you grant permissions to IAM Identity Center users in Account B on the resource link (owned by Account B), and separately grant permissions on the target (Account A's database/table) using the grantable permissions passed from Account A.

**Grant permissions on the resource link**

1. In the Lake Formation console in Account B, navigate to **Data lake permissions** > **Grant**.

1. Under **Principals**, choose **IAM Identity Center** and select the users or groups.

1. Under catalog resources, select the resource link database (`cross_account_db_link`).

1. Under **Resource link permissions**, select **Describe**.

1. Choose **Grant**.

**Grant permissions on the target resource**

1. In the Lake Formation console in Account B, choose **Grant** again.

1. Under **Principals**, choose **IAM Identity Center** and select the same users or groups.

1. Under catalog resources, select the shared table from Account A.

1. Under **Table permissions**, select **Select** and **Describe**.

1. Choose **Grant**.

**Note**  
The "Grant on target" action in the console grants permissions on the underlying resource from Account A using the grantable permissions you received in Step 2.

## Step 7: Configure the EMR security configuration in Account B
<a name="emr-trusted-identity-cross-account-security-config"></a>

If you have not yet created an EMR security configuration with trusted identity propagation enabled, create one now. If you already have one from your single-account setup, you can reuse it.

```
aws emr create-security-configuration \
    --name "TIP-CrossAccount-SecurityConfig" \
    --security-configuration '{
        "AuthorizationConfiguration": {
            "LakeFormationConfiguration": {
                "AuthorizedSessionTagValue": "Amazon EMR",
                "QueryEngineSecurityConfiguration": {
                    "LakeFormationSecurityConfiguration": {
                        "QuerySessionContext": {
                            "ClusterId": {"EmrClusterArn": true},
                            "QueryId": {"SparkQueryId": true}
                        }
                    }
                }
            },
            "IAMConfiguration": {
                "EnableApplicationScopedIAMRole": {"Enabled": true}
            }
        },
        "IdentityCenterConfiguration": {
            "EnableIdentityCenter": true,
            "IdentityCenterInstanceARN": "arn:aws:sso:::instance/ssoins-{{INSTANCE_ID}}",
            "IdentityCenterApplicationARN": "arn:aws:sso::{{REGION}}:{{ACCOUNT_B_ID}}:application/ssoins-{{INSTANCE_ID}}/apl-{{APP_ID}}"
        }
    }'
```

**Note**  
The `IdentityCenterApplicationARN` is the ARN of the EMR-managed IAM Identity Center application created when you first set up Lake Formation with IAM Identity Center. Find it in the IAM Identity Center console under **Applications** > **AWS managed applications**.

## Step 8: Ensure the instance profile role has cross-account permissions
<a name="emr-trusted-identity-cross-account-instance-profile"></a>

The EC2 instance profile role for your EMR cluster in Account B must be able to exchange IAM Identity Center tokens, access the AWS Glue Data Catalog in Account A (via the resource link), and access Amazon S3 data in Account A (via Lake Formation vending credentials).

**Required IAM Identity Center OAuth permissions**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCPermissions",
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        }
    ]
}
```

**Required Lake Formation and AWS Glue permissions**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LakeFormationPermissions",
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess",
                "lakeformation:GetTemporaryGluePartitionCredentials",
                "lakeformation:GetTemporaryGlueTableCredentials"
            ],
            "Resource": "*"
        },
        {
            "Sid": "GlueCatalogAccess",
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabase", "glue:GetDatabases",
                "glue:GetTable", "glue:GetTables",
                "glue:GetPartitions", "glue:SearchTables"
            ],
            "Resource": [
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_B_ID}}:catalog",
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_B_ID}}:database/*",
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_B_ID}}:table/*",
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_A_ID}}:catalog",
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_A_ID}}:database/*",
                "arn:aws:glue:{{REGION}}:{{ACCOUNT_A_ID}}:table/*"
            ]
        }
    ]
}
```

**STS self-assume permission (carrier role pattern)**

The instance profile role must be allowed to assume itself, which is how the carrier role pattern works with trusted identity propagation:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSelfAssume",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::{{ACCOUNT_B_ID}}:role/{{INSTANCE_PROFILE_ROLE}}"
        }
    ]
}
```

## Step 9: Launch the EMR cluster with the security configuration
<a name="emr-trusted-identity-cross-account-launch-cluster"></a>

Launch an EMR cluster in Account B using the security configuration you created.

```
aws emr create-cluster \
    --name "TIP-CrossAccount-Cluster" \
    --release-label emr-7.8.0 \
    --applications Name=Spark Name=Livy \
    --instance-type m5.xlarge \
    --instance-count 3 \
    --security-configuration "TIP-CrossAccount-SecurityConfig" \
    --ec2-attributes '{
        "InstanceProfile": "arn:aws:iam::{{ACCOUNT_B_ID}}:instance-profile/{{NAME}}",
        "SubnetId": "{{SUBNET_ID}}",
        "EmrManagedMasterSecurityGroup": "{{MASTER_SG}}",
        "EmrManagedSlaveSecurityGroup": "{{WORKER_SG}}"
    }' \
    --service-role "arn:aws:iam::{{ACCOUNT_B_ID}}:role/EMR_DefaultRole"
```

**Note**  
Use Amazon EMR release 7.8.0 or later for the best trusted identity propagation experience with runtime roles. Amazon EMR 6.15.0\+ supports basic TIP without runtime roles.

## Step 10: Verify cross-account access from EMR Studio
<a name="emr-trusted-identity-cross-account-verify"></a>

1. Open EMR Studio in Account B and log in with your IAM Identity Center credentials.

1. Attach a Workspace to the EMR cluster you launched.

1. Open a Spark notebook and run the following test query:

   ```
   spark.sql("SHOW DATABASES").show()
   ```

   You should see `cross_account_db_link` in the output.

1. Query the cross-account table:

   ```
   # Query data in Account A through the resource link
   df = spark.sql("SELECT * FROM cross_account_db_link.my_table LIMIT 10")
   df.show()
   ```

1. Verify identity propagation by checking CloudTrail. In Account A's CloudTrail logs, look for `lakeformation:GetDataAccess` events. The `onBehalfOf` field should show the IAM Identity Center user ID who made the request.

## Considerations and limitations
<a name="emr-trusted-identity-cross-account-considerations"></a>
+ **Organization instance required.** Cross-account trusted identity propagation requires an IAM Identity Center organization instance. Account-level instances do not support cross-account TIP.
+ **Same Region constraint.** The IAM Identity Center instance, both Lake Formation configurations, and the EMR cluster must all be in the same AWS Region.
+ **Apache Spark only.** Trusted identity propagation is only supported with Apache Spark on EMR. Other engines (Hive, Presto/Trino) are not supported.
+ **Permissions on target vs. link.** Granting permissions on a resource link does not grant permissions on the target (linked) database or table. You must grant both separately.
+ **Direct IAM Identity Center principal grants not supported cross-account.** Lake Formation returns an error if you try to grant permissions directly to an IAM Identity Center user or group in a different account. Grant to the account ID instead.
+ **Service-linked role not supported.** When registering data locations in Account A for cross-account EMR access, you must use a user-defined role.
+ **Carrier role permissions.** The EMR instance profile role in Account B acts as a carrier role. It must have the `sso-oauth` permissions and the self-assume permission.
+ **External data filtering opt-in.** Account A must explicitly opt in to allow Account B to apply data filtering.

## Troubleshooting
<a name="emr-trusted-identity-cross-account-troubleshooting"></a>

Error: "Cross-account grants are not supported for the principal"  
**Cause:** You attempted to grant Lake Formation permissions directly to an IAM Identity Center user or group for a resource in another account.  
**Solution:** Grant permissions to the external account ID instead. In the consumer account, create resource links and grant permissions to IAM Identity Center principals on the local resource link and its target.

Error: "User is not authorized to perform lakeformation:GetDataAccess"  
**Cause:** The EMR instance profile role does not have the required Lake Formation or IAM Identity Center OAuth permissions.  
**Solution:** Verify the instance profile role has `lakeformation:GetDataAccess`, `lakeformation:GetTemporaryGlueTableCredentials`, and the `sso-oauth:*WithIAM` permissions (see Step 8).

Error: "Access Denied" when querying through the resource link  
**Cause:** Permissions were only granted on the resource link but not on the target resource.  
**Solution:** In Account B, grant permissions on both the resource link (Describe) and the target resource (Select, Describe) to the IAM Identity Center user or group.

Error: "External data filtering is not enabled"  
**Cause:** Account A has not opted in to allow external engines to filter data for Account B.  
**Solution:** In Account A's Lake Formation settings, enable "Allow external engines to filter data" and add Account B's account ID (see Step 3).

Error: Queries return empty results even though data exists  
**Cause:** The IAM Identity Center user does not have correct column-level or row-level permissions on the target table.  
**Solution:** Verify the permissions granted on the target resource include all required columns. Check row-level filter expressions.

Error: CloudTrail shows the carrier role but not the user identity  
**Cause:** The security configuration does not have `EnableIdentityCenter` set to `true`, or the IAM Identity Center application ARN is incorrect.  
**Solution:** Verify the security configuration JSON includes the correct `IdentityCenterConfiguration` block with the right application ARN.