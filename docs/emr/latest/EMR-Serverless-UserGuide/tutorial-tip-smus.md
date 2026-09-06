

# Using Trusted Identity Propagation with Amazon SageMaker Unified Studio
<a name="tutorial-tip-smus"></a>

This tutorial shows how to set up an EMR Serverless application with Trusted Identity Propagation (TIP). You then query a sample table using identity-based access controls through Amazon SageMaker Unified Studio. With this setup, EMR Serverless runs each user's Spark queries with their own IAM Identity Center identity, and Lake Formation enforces per-user permissions on AWS Glue Data Catalog tables.

**TIP not supported in EMR Studio interactive workloads**  
Interactive workloads through EMR Studio do not support Trusted Identity Propagation with EMR Serverless. Use Amazon SageMaker Unified Studio as the client-facing application for TIP-enabled interactive workloads.

**Costs**  
This tutorial uses AWS services that might incur charges, including EMR Serverless, AWS Lake Formation, AWS IAM Identity Center, Amazon Simple Storage Service, and Amazon SageMaker Unified Studio. To avoid ongoing charges, follow the clean up steps at the end of this tutorial. For pricing information, see the pricing page for each service.

## Prerequisites and setup
<a name="tutorial-tip-smus-prereqs"></a>

Complete the following steps to set up all required resources before querying data with trusted identity propagation.

### Step 1: Set up IAM Identity Center
<a name="tutorial-tip-smus-step1-idc"></a>

1. [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html) in your AWS account. An IAM Identity Center instance can only exist in a single Region per account.
**Important**  
Note which Region your IAM Identity Center is deployed in. All subsequent resources (Lake Formation, EMR Serverless, AWS Glue) must be created in the same Region. For example, if your IAM Identity Center is in us-west-2, all resources must also be in us-west-2.

1. [Provision users and groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) into IAM Identity Center, either manually or by syncing from an external identity provider (such as Okta or Microsoft Entra ID).

1. Note your IAM Identity Center instance ARN. You will need it in subsequent steps. Find it in the IAM Identity Center console under **Settings**.

   To find your instance programmatically, run:

   ```
   aws sso-admin list-instances --region {{your-region}}
   ```

   Example output:

   ```
   {
       "Instances": [
           {
               "InstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef",
               "IdentityStoreId": "d-1234567890",
               "OwnerAccountId": "123456789012",
               "Status": "ACTIVE"
           }
       ]
   }
   ```

### Step 2: Configure Lake Formation with IAM Identity Center
<a name="tutorial-tip-smus-step2-lf"></a>

1. Open the Lake Formation console.

1. Set up a [data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/admins-setup.html).
**Important**  
Ensure the IAM role or user you are using to run these commands is added as a Data Lake Administrator in Lake Formation. Otherwise, you will receive "Insufficient Lake Formation permission(s)" errors when creating databases or tables. To add your role as admin:

   ```
   aws lakeformation put-data-lake-settings \
       --data-lake-settings '{
           "DataLakeAdmins": [
               {"DataLakePrincipalIdentifier": "arn:aws:iam::{{account-id}}:role/{{your-role}}"}
           ],
           "CreateDatabaseDefaultPermissions": [],
           "CreateTableDefaultPermissions": [],
           "Parameters": {"CROSS_ACCOUNT_VERSION": "3", "SET_CONTEXT": "TRUE"}
       }'
   ```

1. Create the IAM Identity Center integration for Lake Formation using the instance ARN you noted in Step 1:

   ```
   aws lakeformation create-lake-formation-identity-center-configuration \
       --catalog-id {{account-id}} \
       --instance-arn "arn:aws:sso:::instance/ssoins-{{instance-id}}"
   ```

1. Create an IAM role for Lake Formation location registration. Do not use the service-linked role for trusted identity propagation. For more information, see [Setting up AWS Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html).

   **Trust policy:**

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "lakeformation.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetContext"
               ]
           }
       ]
   }
   ```
**sts:SetContext is required**  
The trust policy must include `sts:SetContext`, which is required for trusted identity propagation. The IAM role created by the default wizard is a service-linked role and does not include `sts:SetContext`. If you previously registered a location with the service-linked role, you must re-register it with a custom role that includes `sts:SetContext`.

   **Permission policy** (grants access to the Amazon S3 data location):

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "LakeFormationDataAccessPermissionsForS3",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject",
                   "s3:GetObject",
                   "s3:DeleteObject"
               ],
               "Resource": [
                   "arn:aws:s3:::{{your-data-bucket}}/*"
               ]
           },
           {
               "Sid": "LakeFormationDataAccessPermissionsForS3ListBucket",
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::{{your-data-bucket}}"
               ]
           }
       ]
   }
   ```

   Create the role and attach the policy:

   ```
   aws iam create-role \
       --role-name LFLocationRegistrationRole \
       --assume-role-policy-document file://lf-trust-policy.json \
       --description "Lake Formation location registration role with sts:SetContext for TIP"
   
   aws iam put-role-policy \
       --role-name LFLocationRegistrationRole \
       --policy-name LFDataAccessPolicy \
       --policy-document file://lf-permissions-policy.json
   ```

1. Register your Amazon S3 data location with Lake Formation using the role you created:

   ```
   aws lakeformation register-resource \
       --resource-arn "arn:aws:s3:::{{your-data-bucket}}" \
       --role-arn "arn:aws:iam::{{account-id}}:role/LFLocationRegistrationRole"
   ```

1. Create a database and table in the AWS Glue Data Catalog pointing to your sample data.

1. Grant IAM Identity Center users or groups permissions on both the database and table.
**Important**  
You must grant DESCRIBE on the database in addition to SELECT and DESCRIBE on the table. Without database-level permissions, the database will not appear in SHOW DATABASES results when using identity-based access.

   **Using the console:**

   1. In the Lake Formation console, choose **Data lake permissions** > **Grant**.

   1. Under **Principals**, choose **IAM Identity Center users and groups** and select your user or group.

   1. Under **Named Data Catalog resources**, select your database.

   1. Under **Database permissions**, select **Describe**.

   1. Choose **Grant**.

   1. Repeat steps 1 through 5, this time selecting the table and granting **Select** and **Describe** under **Table permissions**.

   **Using the AWS CLI:**
**Important**  
The principal identifier format for IAM Identity Center users in Lake Formation grants is: `arn:aws:identitystore:::user/<UserId>`. Note the triple colon (:::). No region or account is specified. Get the UserId from the Identity Store:

   ```
   # List users to get their UserIds
   aws identitystore list-users --identity-store-id {{identity-store-id}} --region {{your-region}}
   
   # Grant DESCRIBE on the database
   aws lakeformation grant-permissions \
       --principal '{"DataLakePrincipalIdentifier": "arn:aws:identitystore:::user/{{UserId}}"}' \
       --permissions '["DESCRIBE"]' \
       --resource '{"Database": {"DatabaseName": "{{tip_tutorial_db}}", "CatalogId": "{{account-id}}"}}'
   
   # Grant SELECT and DESCRIBE on the table
   aws lakeformation grant-permissions \
       --principal '{"DataLakePrincipalIdentifier": "arn:aws:identitystore:::user/{{UserId}}"}' \
       --permissions '["SELECT","DESCRIBE"]' \
       --resource '{"Table": {"DatabaseName": "{{tip_tutorial_db}}", "Name": "{{employees}}", "CatalogId": "{{account-id}}"}}'
   ```

### Step 3: Create the TIP-enabled EMR Serverless application
<a name="tutorial-tip-smus-step3-create-app"></a>

Ensure your IAM role has the required IAM Identity Center permissions to create the application:

```
"sso:DescribeInstance",
"sso:CreateApplication", 
"sso:DeleteApplication",
"sso:PutApplicationAuthenticationMethod",
"sso:PutApplicationAssignmentConfiguration",  
"sso:PutApplicationGrant", 
"sso:PutApplicationAccessScope"
```

Create the application with trusted identity propagation, Apache Livy endpoint enabled, and the AWS Glue Data Catalog configured as the metastore:

```
aws emr-serverless create-application \
    --release-label emr-7.8.0 \
    --type "SPARK" \
    --identity-center-configuration '{"identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-{{instance-id}}"}' \
    --interactive-configuration '{"livyEndpointEnabled":true}' \
    --runtime-configuration '[{"classification": "spark-defaults", "properties": {"spark.sql.catalogImplementation": "hive", "spark.hadoop.hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"}}]'
```

**Important**  
**AWS CLI version requirement:** The `--identity-center-configuration`, `--interactive-configuration`, and `--runtime-configuration` flags require AWS CLI v2.15\+. If you receive "Unknown options" errors, either upgrade your AWS CLI or use Python boto3 (v1.35\+) as an alternative:

```
import boto3

session = boto3.Session(profile_name='{{your-profile}}', region_name='{{your-region}}')
client = session.client('emr-serverless')

response = client.create_application(
    name='tip-tutorial-app',
    releaseLabel='emr-7.8.0',
    type='SPARK',
    identityCenterConfiguration={
        'identityCenterInstanceArn': 'arn:aws:sso:::instance/ssoins-{{instance-id}}'
    },
    interactiveConfiguration={
        'livyEndpointEnabled': True
    },
    runtimeConfiguration=[
        {
            'classification': 'spark-defaults',
            'properties': {
                'spark.sql.catalogImplementation': 'hive',
                'spark.hadoop.hive.metastore.client.factory.class': 'com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory'
            }
        }
    ]
)
print(response['applicationId'])
```

**Glue Data Catalog metastore configuration**  
The `runtimeConfiguration` setting for `spark.sql.catalogImplementation` and the AWS Glue metastore factory class ensures that Spark sessions can access all table types (CSV, Parquet, ORC, Iceberg) in the AWS Glue Data Catalog. Without this configuration, only Iceberg tables might be visible.

**Apache Livy endpoint is required for TIP**  
Trusted identity propagation requires `--interactive-configuration '{"livyEndpointEnabled":true}'`. TIP is enabled for the Apache Livy endpoint only.

If you don't have the required IAM Identity Center permissions, create the application without the `--identity-center-configuration` parameter and ask your IAM Identity Center administrator to enable TIP later using the update-application API:

```
aws emr-serverless update-application \
    --application-id {{application-id}} \
    --identity-center-configuration '{"identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-{{instance-id}}"}'
```

### Step 4: Configure the job execution role
<a name="tutorial-tip-smus-step4-job-role"></a>

The job execution role's trust policy must include `sts:SetContext` to allow EMR Serverless to enhance credentials with the user's identity:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "emr-serverless.amazonaws.com"
            },
            "Action": ["sts:AssumeRole", "sts:SetContext"]
        }
    ]
}
```

Create the role:

```
aws iam create-role \
    --role-name emr-serverless-tip-job-role \
    --assume-role-policy-document file://trust-policy.json \
    --description "EMR Serverless job execution role with TIP support"
```

Attach permissions for the downstream services the job will access. The role needs Lake Formation, AWS Glue, Amazon S3, and Amazon CloudWatch Logs permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LakeFormationAndGlueAccess",
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess",
                "glue:GetTable", "glue:GetTables",
                "glue:GetDatabase", "glue:GetDatabases",
                "glue:GetPartitions"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3DataAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{your-data-bucket}}",
                "arn:aws:s3:::{{your-data-bucket}}/*"
            ]
        },
        {
            "Sid": "CloudWatchLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": "arn:aws:logs:{{region}}:{{account-id}}:*"
        }
    ]
}
```

**S3 permissions are required in addition to Lake Formation permissions**  
The Amazon S3 permissions (`s3:GetObject`, `s3:PutObject`, `s3:ListBucket`) on your data bucket are required in addition to the Lake Formation and AWS Glue permissions. The `s3:PutObject` permission is needed for Spark scratch and shuffle data. Without Amazon S3 permissions, Spark jobs might fail with access denied errors when reading the underlying data files or writing temporary data.

**CloudWatch Logs permissions are required**  
Amazon CloudWatch Logs permissions are required for Spark driver and executor log delivery. Without them, Spark sessions might fail to start.

Attach the policy to the role:

```
aws iam put-role-policy \
    --role-name emr-serverless-tip-job-role \
    --policy-name tip-lakeformation-access \
    --policy-document file://permissions-policy.json
```

**Grant Lake Formation permissions to the job execution role:**

The job execution role also requires Lake Formation permissions on the database and table. This is in addition to the grants given to the IAM Identity Center user.

```
# Grant DESCRIBE on the database to the job role
aws lakeformation grant-permissions \
    --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::{{account-id}}:role/emr-serverless-tip-job-role"}' \
    --permissions '["DESCRIBE"]' \
    --resource '{"Database": {"DatabaseName": "{{tip_tutorial_db}}", "CatalogId": "{{account-id}}"}}'

# Grant SELECT and DESCRIBE on the table to the job role
aws lakeformation grant-permissions \
    --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::{{account-id}}:role/emr-serverless-tip-job-role"}' \
    --permissions '["SELECT","DESCRIBE"]' \
    --resource '{"Table": {"DatabaseName": "{{tip_tutorial_db}}", "Name": "{{employees}}", "CatalogId": "{{account-id}}"}}'
```

For additional downstream service configurations, see [Using Lake Formation with EMR Serverless](lake-formation-section.html) and [Using Amazon S3 Access Grants with EMR Serverless](access-grants.html).

## Query data with Trusted Identity Propagation through Amazon SageMaker Unified Studio
<a name="tutorial-tip-smus-query"></a>

After you complete the setup, you can query data using your TIP-enabled EMR Serverless application as compute in a Amazon SageMaker Unified Studio project. EMR Serverless runs each user's queries with their own IAM Identity Center identity, and Lake Formation enforces per-user permissions.

### Prerequisites
<a name="tutorial-tip-smus-query-prereqs"></a>
+ A TIP-enabled EMR Serverless application (completed in Step 3 above).
+ A Amazon SageMaker Unified Studio domain configured with IAM Identity Center authentication.
+ Lake Formation permissions granted to your IAM Identity Center user or group on the target database and table (completed in Step 2 above).

### Step 5: Create a Amazon SageMaker Unified Studio project with TIP enabled
<a name="tutorial-tip-smus-query-setup-project"></a>

1. Sign in to Amazon SageMaker Unified Studio using your IAM Identity Center credentials.

1. Create a new project or open an existing project.

1. In the project settings, ensure the profile has `enableTrustedIdentityPropagationPermissions` set to `true` in the blueprint parameters.

### Step 6: Add the EMR Serverless application as compute
<a name="tutorial-tip-smus-query-add-compute"></a>

Amazon SageMaker Unified Studio project compute configuration does not currently support adding an existing EMR Serverless application through the console. Use the AWS CLI to create the connection:

```
aws datazone create-connection \
  --domain-identifier {{domain-id}} \
  --name "{{my-emr-serverless-connection}}" \
  --environment-identifier {{environment-id}} \
  --props '{
    "sparkEmrProperties": {
      "computeArn": "arn:aws:emr-serverless:{{region}}:{{account-id}}:/applications/{{application-id}}",
      "runtimeRole": "arn:aws:iam::{{account-id}}:role/emr-serverless-tip-job-role"
    }
  }'
```

Replace the following values:
+ `{{domain-id}}`: Your Amazon SageMaker Unified Studio domain identifier.
+ `{{environment-id}}`: The environment identifier for your project (use the Tooling environment).
+ `{{application-id}}`: The EMR Serverless application ID from Step 3.
+ `{{emr-serverless-tip-job-role}}`: The job execution role from Step 4.

**Important**  
The `create-connection` API requires the caller to be a member of the DataZone project. If you receive an `AccessDeniedException`, add your IAM role as a project contributor before creating the connection:

```
import boto3

session = boto3.Session(profile_name='{{your-profile}}', region_name='{{your-region}}')
client = session.client('datazone')

client.create_project_membership(
    domainIdentifier='{{domain-id}}',
    projectIdentifier='{{project-id}}',
    designation='PROJECT_CONTRIBUTOR',
    member={'userIdentifier': 'arn:aws:iam::{{account-id}}:role/{{your-role}}'}
)
```

**Configure the project's DataZone user role for EMR Serverless access.**

The DataZone user role for the project environment must have permissions to interact with the EMR Serverless application. Add the following inline policy to the role (the role name follows the pattern `datazone_usr_role_<project-id>_<environment-id>`):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "emr-serverless:GetApplication",
                "emr-serverless:StartApplication",
                "emr-serverless:StopApplication",
                "emr-serverless:ListApplications",
                "emr-serverless:CreatePresignedUrl",
                "emr-serverless:AccessLivyEndpoints",
                "emr-serverless:StartJobRun",
                "emr-serverless:GetJobRun",
                "emr-serverless:ListJobRuns",
                "emr-serverless:CancelJobRun",
                "emr-serverless:GetDashboardForJobRun"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/emr-serverless-tip-job-role",
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "emr-serverless.amazonaws.com"
                }
            }
        }
    ]
}
```

**Grant Lake Formation permissions to the DataZone user role:**

```
# Grant DESCRIBE on the database
aws lakeformation grant-permissions \
    --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::{{account-id}}:role/datazone_usr_role_{{project-id}}_{{environment-id}}"}' \
    --permissions '["DESCRIBE"]' \
    --resource '{"Database": {"DatabaseName": "{{tip_tutorial_db}}", "CatalogId": "{{account-id}}"}}'

# Grant SELECT and DESCRIBE on the table
aws lakeformation grant-permissions \
    --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::{{account-id}}:role/datazone_usr_role_{{project-id}}_{{environment-id}}"}' \
    --permissions '["SELECT","DESCRIBE"]' \
    --resource '{"Table": {"DatabaseName": "{{tip_tutorial_db}}", "Name": "{{employees}}", "CatalogId": "{{account-id}}"}}'
```

**Console limitation for EMR Serverless connections**  
Amazon SageMaker Unified Studio currently supports adding existing Amazon EMR on EC2 clusters through the console compute configuration. For EMR Serverless applications, use the AWS CLI method shown above.

### Step 7: Query a sample table
<a name="tutorial-tip-smus-query-run"></a>

1. Open a JupyterLab IDE space in your Amazon SageMaker Unified Studio project.

1. Select the EMR Serverless connection as the compute for notebook execution.

1. In a new notebook cell, run the following PySpark queries:

   ```
   %%pyspark my-emr-serverless-connection
   spark.sql("SHOW DATABASES").show()
   
   %%pyspark my-emr-serverless-connection
   spark.sql("SELECT * FROM tip_tutorial_db.employees LIMIT 10").show()
   ```

1. Verify that the query returns data. This confirms that your IAM Identity Center identity was propagated through to Lake Formation and access was granted based on your identity.

**Application cold start**  
The first time you run a cell after creating the connection, EMR Serverless starts the application (cold start). This can take 2 to 3 minutes. Subsequent cells run within seconds while the session is active.

**Troubleshooting access denied errors**  
If you receive an access denied error, verify that:   
Your IAM Identity Center user or group has been granted DESCRIBE on the database and SELECT/DESCRIBE on the table in Lake Formation.
The job execution role has `lakeformation:GetDataAccess` and AWS Glue Data Catalog permissions.
The DataZone user role has Lake Formation permissions on the database and table.
The Lake Formation Amazon S3 location is registered with a custom role that includes `sts:SetContext` (not the service-linked role).

## Troubleshooting
<a name="tutorial-tip-smus-troubleshooting"></a>


| Error | Cause | Fix | 
| --- | --- | --- | 
| AccessDeniedException: emr-serverless:GetApplication | The DataZone user role lacks EMR Serverless permissions. | Add the EMR Serverless inline policy to the DataZone user role (see Step 6). | 
| Timed out waiting for application to reach STARTED status | EMR Serverless app cold start exceeds the default timeout. | Re-run the cell. The app continues starting in the background and will be ready on the next attempt. | 
| Session not found. Cleaned up due to idle timeout. | The Spark session failed to start due to insufficient permissions on the job execution role. | Ensure the job execution role has Amazon S3, Amazon CloudWatch Logs, AWS Glue, and Lake Formation permissions (see Step 4). | 
| Insufficient Lake Formation permission(s): Required Describe on database | Your identity or role does not have database-level Lake Formation permissions. | Grant DESCRIBE on the database to the IAM Identity Center user, job execution role, and DataZone user role. | 
| TABLE\_OR\_VIEW\_NOT\_FOUND | The Spark session is not configured to use the AWS Glue Data Catalog. | Ensure the EMR Serverless application includes spark.sql.catalogImplementation=hive and the AWS Glue metastore factory class in its runtimeConfiguration (see Step 3). | 
| AccessDeniedException: CreateConnection | The caller is not a member of the DataZone project. | Add your role as a project contributor before calling create-connection (see Step 6). | 

## Clean up resources
<a name="tutorial-tip-smus-cleanup"></a>

To avoid ongoing charges, delete the resources you created in this tutorial:

1. Delete the EMR Serverless application.

1. Remove the Amazon SageMaker Unified Studio connection and delete the Amazon SageMaker Unified Studio project (and domain, if you created it only for this tutorial).

1. Revoke the Lake Formation permissions you granted, and deregister the Amazon S3 data location.

1. Delete the IAM roles you created in Step 2 and Step 4.

1. Delete any test Amazon S3 buckets and sample data.

## Next steps
<a name="tutorial-tip-smus-next-steps"></a>
+ To verify identity propagation in CloudTrail, look for `AssumeRole` events with `sts:SetContext` from the EMR Serverless service.
+ To restrict access for different users, create additional IAM Identity Center users and grant them different Lake Formation permissions on the same table (for example, column-level or row-level filtering).
+ For production deployments, scope the job execution role's Amazon S3 and AWS Glue permissions to specific resources rather than using wildcards.
+ For more information about using EMR Serverless with Amazon SageMaker Unified Studio, see [EMR Serverless in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/emr-serverless.html).