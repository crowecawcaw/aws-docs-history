Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Credentials and access

permissions

To load or unload data using another AWS resource, such as Amazon S3, Amazon DynamoDB, Amazon EMR,
or Amazon EC2, Amazon Redshift must have permission to access the resource and perform the
necessary actions to access the data. For example, to load data from Amazon S3, COPY must
have LIST access to the bucket and GET access for the bucket objects.

To obtain authorization to access a resource, Amazon Redshift must be authenticated. You
can choose either role-based access control or key-based access control. This section
presents an overview of the two methods. For complete details and examples, see [Permissions to access other AWS
Resources](copy-usage_notes-access-permissions.md "copy-usage_notes-access-permissions.md").

## Role-based access control

With role-based access control, Amazon Redshift temporarily assumes an AWS Identity and Access Management
(IAM) role on your behalf. Then, based on the authorizations granted to the role,
Amazon Redshift can access the required AWS resources.

We recommend using role-based access control because it is provides more secure,
fine-grained control of access to AWS resources and sensitive user data, in addition
to safeguarding your AWS credentials.

To use role-based access control, you must first create an IAM role using the
Amazon Redshift service role type, and then attach the role to your data warehouse. The role must have,
at a minimum, the permissions listed in [IAM permissions for COPY, UNLOAD,
and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions"). For steps to create an IAM
role and attach it to your cluster, see [Creating an IAM Role to Allow Your Amazon Redshift Cluster to Access AWS Services](../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-creating-an-iam-role "../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-creating-an-iam-role") in
the _Amazon Redshift Management Guide_.

You can add a role to a cluster or view the roles associated with a cluster by
using the Amazon Redshift Management Console, CLI, or API. For more information, see [Authorizing COPY and UNLOAD
Operations Using IAM Roles](../mgmt/copy-unload-iam-role.md "../mgmt/copy-unload-iam-role.md") in the
_Amazon Redshift Management Guide_.

When you create an IAM role, IAM returns an Amazon Resource Name (ARN) for the
role. To run a COPY command using an IAM role, provide the role ARN using the
IAM_ROLE parameter or the CREDENTIALS parameter.

The following COPY command example uses IAM_ROLE parameter with the role
`MyRedshiftRole` for authentication.

```
COPY customer FROM 's3://amzn-s3-demo-bucket/mydata'
IAM_ROLE 'arn:aws:iam::12345678901:role/MyRedshiftRole';
```

The AWS user must have, at a minimum, the permissions listed in [IAM permissions for COPY, UNLOAD,
and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions").

## Key-based access control

With key-based access control, you provide the access key ID and secret access key
for a user that is authorized to access the AWS resources that contain the
data. 

###### Note

We strongly recommend using an IAM role for authentication instead of
supplying a plain-text access key ID and secret access key. If you choose
key-based access control, never use your AWS account (root) credentials. Always
create an IAM user and provide that user's access key ID and secret access key.
For steps to create an IAM user, see [Creating an IAM User in Your AWS
Account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md").
