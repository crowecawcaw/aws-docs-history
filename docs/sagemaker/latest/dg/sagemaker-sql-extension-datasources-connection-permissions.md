# Set up the IAM

permissions to access the data sources (for administrators)

Administrators should ensure that the execution role used by the JupyterLab applications
has the necessary AWS IAM permissions to access the data through the configured AWS Glue
connections.

- **Connections created by administrators using the
  AWS CLI**: To view the AWS Glue connections [created by
  administrators](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md") and access their data, users need to have their administrator
  attach specific permissions to the SageMaker AI execution role used by their JupyterLab
  application in Studio. This includes access to AWS Glue, Secrets Manager, and
  database-specific permissions. Connections created by administrators are visible to all
  applications sharing the execution role granted the permissions to view specific AWS Glue
  catalogs or databases. To learn about the list of required permissions per type of data
  source, see the admin-defined connections permissions in [Admin-defined connections required
  IAM permissions](#admin-defined-connections-permissions "#admin-defined-connections-permissions").
- **Connections created by users using the SQL extension UI in
  JupyterLab**: Connections [created by
  user profiles](sagemaker-sql-extension-datasources-glue-connection-user-defined.md "sagemaker-sql-extension-datasources-glue-connection-user-defined.md") sharing the same execution role will also be listed unless the
  visibility of their connections is scoped down to only those created by the user.
  Connections created by users are tagged with the user profile that created them. To
  restrict the ability to view, update, or delete those user-created connections to only the
  user who created them, administrators can add additional tag-based access control
  restrictions to the execution role IAM permissions. To learn about the additional
  tag-based access control required, see [User-defined connections required
  IAM permissions](#user-defined-connections-permissions "#user-defined-connections-permissions").

## Admin-defined connections required

IAM permissions

To grant the SageMaker AI execution role used by your JupyterLab application in Studio
access to a data source through an AWS Glue connection, attach the following inline policy to
the role.

To view the specific permissions and policy details for each data source or
authentication method, choose the relevant connection type below.

###### Note

We recommend limiting your policy's permissions to only the resources and actions
required.

To scope down policies and grant least privilege access, replace wildcard
`"Resource": ["*"]` in your policy with specific ARNs for the exact resources
needing access. For more information about how to control access to your resources, see
[Fine-tune AWS resource access with
granular ARN permissions](#resource-access-control "#resource-access-control").

###### Note

We strongly recommend scoping down this policy to only the actions and resources
required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetS3AndDataSourcesMetadata",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabases",
 "glue:GetSchema",
 "glue:GetTables",
 "s3:ListBucket",
 "s3:GetObject",
 "s3:GetBucketLocation",
 "glue:GetDatabase",
 "glue:GetTable",
 "glue:ListSchemas",
 "glue:GetPartitions"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/*"
 ]
 },
 {
 "Sid": "ExecuteQueries",
 "Effect": "Allow",
 "Action": [
 "athena:ListDataCatalogs",
 "athena:ListDatabases",
 "athena:ListTableMetadata",
 "athena:StartQueryExecution",
 "athena:GetQueryExecution",
 "athena:RunQuery",
 "athena:StartSession",
 "athena:GetQueryResults",
 "athena:ListWorkGroups",
 "s3:ListMultipartUploadParts",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "athena:GetDataCatalog",
 "s3:AbortMultipartUpload",
 "s3:GetObject",
 "s3:PutObject",
 "athena:GetWorkGroup"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "arn:aws:athena:`us-east-1`:`111122223333`:workgroup/`workgroup-name`"
 ]
 },
 {
 "Sid": "GetGlueConnections",
 "Effect": "Allow",
 "Action": [
 "glue:GetConnections",
 "glue:GetConnection"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/*"
 ]
 },
 {
 "Sid": "GetSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:`secret:secret-name`"
 ]
 },
 {
 "Sid": "GetClusterCredentials",
 "Effect": "Allow",
 "Action": [
 "redshift:GetClusterCredentials"
 ],
 "Resource": [
 "arn:aws:redshift:`us-east-1`:`111122223333`:cluster:`cluster-name`"
 ]
 }
 ]
}`

```

###### Note

We strongly recommend scoping down this policy to only the resources
required.

For more information, see _Example IAM permissions
policies_ in [Athena
documentation](../../../athena/latest/ug/federated-query-iam-access.md "../../../athena/latest/ug/federated-query-iam-access.md").

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GetS3AndDataSourcesMetadata",
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabases",
                "glue:GetSchema",
                "glue:GetTables",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetBucketLocation",
                "glue:GetDatabase",
                "glue:GetTable",
                "glue:ListSchemas",
                "glue:GetPartitions"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "arn:aws:glue:`region`:`account_id`:catalog",
                "arn:aws:glue:`region`:`account_id`:connection/*",
                "..."
            ]
        },
        {
            "Sid": "ExecuteAthenaQueries",
            "Effect": "Allow",
            "Action": [
                "athena:ListDataCatalogs",
                "athena:ListDatabases",
                "athena:ListTableMetadata",
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:RunQuery",
                "athena:StartSession",
                "athena:GetQueryResults",
                "athena:ListWorkGroups",
                "s3:ListMultipartUploadParts",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "athena:GetDataCatalog",
                "s3:AbortMultipartUpload",
                "s3:GetObject",
                "s3:PutObject",
                "athena:GetWorkGroup"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "arn:aws:athena:`region`:`account_id`:workgroup/`workgroup-name`",
                "..."
            ]
            ]
        },
        {
            "Sid": "GetGlueConnections",
            "Effect": "Allow",
            "Action": [
                "glue:GetConnections",
                "glue:GetConnection"
            ],
            "Resource": [
                "arn:aws:glue:`region`:`account_id`:catalog",
                "arn:aws:glue:`region`:`account_id`:connection/*",
                "..."
            ]
        },
        {
            "Sid": "GetSecrets",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:`region`:`account_id`:secret:`secret-name`",
                "..."
            ]
        }
    ]
}
```

###### Note

We strongly recommend scoping down this policy to only the resources
required.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GetS3Metadata",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "..."
            ]
        },
        {
            "Sid": "GetGlueConnections",
            "Effect": "Allow",
            "Action": [
                "glue:GetConnections",
                "glue:GetConnection"
            ],
            "Resource":
                "arn:aws:glue:`region`:`account_id`:catalog",
                "arn:aws:glue:`region`:`account_id`:connection/*",
                "..."
            ]
        },
        {
            "Sid": "GetSecrets",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:`region`:`account_id`:secret:`secret-name`",
                "..."
            ]
        }
    ]
}
```

###### Note

We strongly recommend scoping down this policy to only the resources
required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetS3Metadata",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Sid": "GetGlueConnections",
 "Effect": "Allow",
 "Action": [
 "glue:GetConnections",
 "glue:GetConnection"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/`connection-name`"
 ]
 },
 {
 "Sid": "GetSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name`",
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name-with-suffix`"
 ]
 },
 {
 "Sid": "GetClusterCredentials",
 "Effect": "Allow",
 "Action": [
 "redshift:GetClusterCredentials"
 ],
 "Resource": [
 "arn:aws:redshift:`us-east-1`:`111122223333`:cluster:`cluster-name`",
 "arn:aws:redshift:`us-east-1`:`111122223333`:dbuser:`cluster-name`/`db-user-name`"
 ]
 }
 ]
}`

```

###### Note

We strongly recommend scoping down this policy to only the resources
required.

```
{
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GetS3Metadata",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "..."
            ]
        },
        {
            "Sid": "GetGlueConnections",
            "Effect": "Allow",
            "Action": [
                "glue:GetConnections",
                "glue:GetConnection"
            ],
            "Resource": [
                "arn:aws:glue:`region`:`account_id`:catalog",
                "arn:aws:glue:`region`:`account_id`:connection/*",
                "..."
            ]
        },
        {
            "Sid": "GetSecrets",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:`region`:`account_id`:secret:`secret-name`",
                "..."
            ]
        },
        {
            "Sid": "GetRedshiftServerlessCredentials",
            "Effect": "Allow",
            "Action": [
                "redshift-serverless:GetCredentials"
            ],
            "Resource": [
                "arn:aws:redshift-serverless:`region`:`account_id`:namespace/`namespace-id`",
                "..."
            ]
        }
    ]
}
}
```

## User-defined connections required

IAM permissions

The IAM policy permissions for a user can account for the presence of the
`UserProfile` tag on AWS Glue connection resources.

- **For viewing AWS Glue connections**:
  - Users can view all connections that do not have the `UserProfile` tag
    (created by an administrator).
  - Users can view connections that have the `UserProfile` tag with the
    same value as their user profile name.
  - Users cannot view connections that have the `UserProfile` tag with a
    different value than their user profile name.

- **For updating or deleting AWS Glue connections**:
  - Users can update or delete a connection that has the `UserProfile`
    tag with the same value as their user profile name.
  - Users cannot update or delete a connection that has the `UserProfile`
    tag with a different value than their user profile name.
  - Users cannot update or delete connections that do not have the
    `UserProfile` tag.

To achieve this, administrators must grant the execution role used by the user profile's
JupyterLab application additional permissions beyond their existing [admin-defined connections
permissions](#admin-defined-connections-permissions "#admin-defined-connections-permissions"). Specifically, in addition to the permissions required for accessing
admin-defined AWS Glue connections, the following two additional IAM permissions must be
granted to the user's execution role:

- Permission to create AWS Glue connections and associate the `UserProfile`
  tag with the value of the user's profile name.
- Permission to view, update, and delete AWS Glue connections that have the
  `UserProfile` tag matching the user's profile name.

This permission restricts access to AWS Glue connections based on a specific user profile
tag value. Update the `UserProfile` tag value with the profile name of the user
you want to target.

```
"Action": [
    "glue:GetConnection",
    "glue:GetConnections"
],
"Resource": [
    "arn:aws:glue:`region`:`account_id`:connection/*"
],
"Condition": {
    "StringEqualsIfExists": {
        "aws:ResourceTag/UserProfile": "`user_profile_name`"
    }
}
```

This permission restricts the ability to create, update, and delete user-created
connections to only the connections created by the user profile with the specified
`UserProfile` tag value.

```
"Action": [
    "glue:DeleteConnection",
    "glue:UpdateConnection",
    "glue:CreateConnection",
    "glue:TagResource"
],
"Resource": [
    "arn:aws:glue:`region`:`account_id`:connection/*"
],
"Condition": {
    "StringEquals": {
        "aws:ResourceTag/UserProfile": "`user_profile`"
    }
}
```

## Fine-tune AWS resource access with

granular ARN permissions

For finer-grained control over access to your AWS resources, replace the
wildcard resource `"Resource": ["*"]` in your policies with the specific Amazon
Resource Names (ARNs) of only those resources that require access. Using the exact ARNs
rather than a wildcard restricts access to the intended resources.

- **Use specific Amazon S3 bucket ARNs**

For example `"arn:aws:s3:::bucket-name"` or `"arn:aws:s3:::bucket-name/*"` for bucket-level or object-level
operations.

For information about all resource types in Amazon S3, see [Resource types defined by Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-resources-for-iam-policies").

- **Use specific AWS Glue database ARNs**

For example `"arn:aws:glue:region:account-id:catalog"` or `"arn:aws:glue:region:account-id:database/db-name"`. For information about all
resource types in AWS Glue, see [Resource types defined by AWS Glue](../../../service-authorization/latest/reference/list_awsglue.md#awsglue-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsglue.md#awsglue-resources-for-iam-policies").

- **Use specific Athena workgroup ARNs**

For example
`"arn:aws:athena:region:account-id:workgroup/workgroup-name"`. For
information about all resource types in Athena, see [Resource types defined by Athena](../../../service-authorization/latest/reference/list_amazonathena.md#amazonathena-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonathena.md#amazonathena-resources-for-iam-policies").

- **Use specific AWS Secrets Manager secret
  ARNs**

For example
`"arn:aws:secretsmanager:region:account-id:secret:secret-name"`. For
information about all resource types in AWS Secrets Manager, see [Resource types defined by AWS Secrets Manager](../../../service-authorization/latest/reference/list_awssecretsmanager.md#awssecretsmanager-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awssecretsmanager.md#awssecretsmanager-resources-for-iam-policies")

- **Use specific Amazon Redshift cluster ARNs**

For example `"arn:aws:redshift:region:account-id:cluster:cluster-name"`.
For information about resource types in Amazon Redshift, see [Resource types defined by Amazon Redshift](../../../service-authorization/latest/reference/list_amazonredshift.md#amazonredshift-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonredshift.md#amazonredshift-resources-for-iam-policies"). For information about all resource types in
Redshift Serverless, see [Resource types defined by Redshift Serverless](../../../service-authorization/latest/reference/list_amazonredshiftserverless.md#amazonredshiftserverless-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonredshiftserverless.md#amazonredshiftserverless-resources-for-iam-policies").
