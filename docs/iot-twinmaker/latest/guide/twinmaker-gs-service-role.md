# Create and manage a service role for

AWS IoT TwinMaker

AWS IoT TwinMaker requires that you use a service role to allow it to access resources in other services on your behalf. This role must have a
trust relationship with AWS IoT TwinMaker. When you create a workspace, you must assign this role to the workspace. This topic contains example
policies that show you how to configure permissions for common scenarios.

## Assign trust

The following policy establishes a trust relationship between your role and AWS IoT TwinMaker. Assign this trust relationship to the role
that you use for your workspace.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "iottwinmaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Amazon S3 permissions

The following policy allows your role to read and delete from and write to an Amazon S3 bucket.
Workspaces store resources in Amazon S3, so the Amazon S3 permissions are required for all
workspaces.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucket*",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/DO_NOT_DELETE_WORKSPACE_*"
 ]
 }
 ]
}`

```

###### Note

When you create a workspace, AWS IoT TwinMaker creates a file in your Amazon S3 bucket that indicates it's
being used by a workspace. This policy gives AWS IoT TwinMaker permission to delete that
file when you delete the workspace.

AWS IoT TwinMaker places other objects related to your workspace. It's your responsibility to delete
these objects when you delete a workspace.

## Assign permissions to a specific

Amazon S3 bucket

When you create a workspace in the AWS IoT TwinMaker console, you can choose to have AWS IoT TwinMaker
create an Amazon S3 bucket for you. You can find information about this bucket by using
the following AWS CLI command.

```

  aws iottwinmaker get-workspace --workspace-id `workspace name`

```

The following example shows the format of the output of this command.

```

{
    "arn": "arn:aws:iottwinmaker:`region`:`account Id`:workspace/`workspace name`",
    "creationDateTime": "2021-11-30T11:30:00.000000-08:00",
    "description": "",
    "role": "arn:aws:iam::`account Id`:role/`service role name`",
    "s3Location": "arn:aws:s3:::`bucket name`",
    "updateDateTime": "2021-11-30T11:30:00.000000-08:00",
    "workspaceId": "`workspace name`"
}

```

To update your policy so that it assigns permissions for a specific Amazon S3 bucket,
use the value of `bucket name`.

The following policy allows your role to read and delete from and write to a specific Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucket*",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket name`",
 "arn:aws:s3:::`bucket name`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::iottwinmakerbucket/DO_NOT_DELETE_WORKSPACE_*"
 ]
 }
 ]
}`

```

## Permissions for built-in connectors

If your workspace interacts with other AWS services by using built-in connectors, you must include permissions for those services in this policy. If you use
the **com.amazon.iotsitewise.connector** component type, you must include permissions for AWS IoT SiteWise.
For more information about
component types, see [Using and creating component types](twinmaker-component-types.md "twinmaker-component-types.md").

###### Note

If you interact with other AWS services by using a custom component type, you must grant the
role permission to run the Lambda function that implements the function in your
component type. For more information, see [Permissions for a connector to an external data source](#twinmaker-gs-service-role-external "#twinmaker-gs-service-role-external").

The following example
shows how to include AWS IoT SiteWise in your policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucket*",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket name`",
 "arn:aws:s3:::`bucket name`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribeAsset"
 ],
 "Resource": "arn:aws:s3:::`bucket name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribeAssetModel"
 ],
 "Resource": "arn:aws:s3:::`bucket name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/DO_NOT_DELETE_WORKSPACE_*"
 ]
 }
 ]
}`

```

If you use the **com.amazon.iotsitewise.connector** component type and need to read
property data from AWS IoT SiteWise, you must include the following permission in your policy.

```

...
{
    "Action": [
        "iotsitewise:GetPropertyValueHistory",
    ],
    "Resource": [
        "`AWS IoT SiteWise asset resource ARN`"
    ],
    "Effect": "Allow"
},
...

```

If you use the **com.amazon.iotsitewise.connector** component type and need to write
property data to AWS IoT SiteWise, you must include the following permission in your policy.

```

...
{
    "Action": [
        "iotsitewise:BatchPutPropertyValues",
    ],
    "Resource": [
        "`AWS IoT SiteWise asset resource ARN`"
    ],
    "Effect": "Allow"
},
...

```

If you use the **com.amazon.iotsitewise.connector.edgevideo** component type, you must
include permissions for AWS IoT SiteWise and Kinesis Video Streams. The following example policy shows how to
include AWS IoT SiteWise and Kinesis Video Streams permissions in your policy.

```

...
{
    "Action": [
        "iotsitewise:DescribeAsset",
        "iotsitewise:GetAssetPropertyValue"
    ],
    "Resource": [
        "`AWS IoT SiteWise asset resource ARN for the Edge Connector for Kinesis Video Streams`"
    ],
    "Effect": "Allow"
},
{
    "Action": [
        "iotsitewise:DescribeAssetModel"
    ],
    "Resource": [
        "`AWS IoT SiteWise model resource ARN for the Edge Connector for Kinesis Video Streams`"
    ],
    "Effect": "Allow"
},
{
    "Action": [
        "kinesisvideo:DescribeStream"
    ],
    "Resource": [
        "`Kinesis Video Streams stream ARN`"
    ],
    "Effect": "Allow"
},
...

```

## Permissions for a connector to an external data source

If you create a component type that uses a function that connects to an external data source, you must
give your service role permission to use the Lambda function that implements the function. For more information about
creating component types and functions, see [Using and creating component types](twinmaker-component-types.md "twinmaker-component-types.md").

The following example gives permission to your service role to use a Lambda function.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucket*",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Action": [
 "lambda:invokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:us-east-1:`111122223333`:function:example-function"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/DO_NOT_DELETE_WORKSPACE_*"
 ]
 }
 ]
}`

```

For more information about creating roles and assigning policies and trust
relationships to them by using the IAM console, the AWS CLI, and the IAM API, see
[Creating a role to
delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

## Modify your workspace IAM role to use the Athena data connector

To use the [AWS IoT TwinMaker Athena tabular data connector](athena-tabular-data-connector.md "athena-tabular-data-connector.md"), you must update your AWS IoT TwinMaker workspace IAM role. Add the following permissions to your workspace IAM role:

###### Note

This IAM change only works for Athena tabular data stored with AWS Glue and Amazon S3.
To use Athena with other data sources, you must configure an IAM role for Athena, see [Identity and access management in Athena](../../../athena/latest/ug/security-iam-athena.md "../../../athena/latest/ug/security-iam-athena.md").

```
{
    "Effect": "Allow",
    "Action": [
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:GetTableMetadata",
        "athena:GetWorkGroup",
        "athena:StartQueryExecution",
        "athena:StopQueryExecution"
    ],
    "Resource": [
        "`athena resouces arn`"
    ]
},// Athena permission
{
    "Effect": "Allow",
    "Action": [
        "glue:GetTable",
        "glue:GetTables",
        "glue:GetDatabase",
        "glue:GetDatabases"
    ],
    "Resource": [
        "`glue resouces arn`"
    ]
},// This is an example for accessing aws glue
{
    "Effect": "Allow",
    "Action": [
        "s3:ListBucket",
        "s3:GetObject"
    ],
    "Resource": [
        "`Amazon S3 data source bucket resources arn`"
    ]
}, // S3 bucket for storing the tabular data.
{
    "Effect": "Allow",
    "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload",
        "s3:CreateBucket",
        "s3:PutObject",
        "s3:PutBucketPublicAccessBlock"
    ],
    "Resource": [
        "`S3 query result bucket resources arn`"
    ]
} // Storing the query results
```

Read the [Identity and access management in Athena](../../../athena/latest/ug/security-iam-athena.md "../../../athena/latest/ug/security-iam-athena.md") for more information on Athena IAM configuration.
