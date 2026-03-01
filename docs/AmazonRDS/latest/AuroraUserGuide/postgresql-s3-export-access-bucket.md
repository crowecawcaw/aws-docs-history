# Setting up access to an Amazon S3 bucket

To export data to Amazon S3, give your PostgreSQL DB
cluster
permission to access the Amazon S3 bucket that the files are to go in.

To do this, use the following procedure.

###### To give a PostgreSQL DB cluster access to Amazon S3 through an IAM role

1. Create an IAM policy.

This policy provides the bucket and object permissions that allow your PostgreSQL DB
cluster
to access Amazon S3.

As part of creating this policy, take the following steps:

    1. Include in the policy the following required actions to allow the
     transfer of files from your PostgreSQL DB cluster to
     an Amazon S3 bucket:




    	* `s3:PutObject`
    	* `s3:AbortMultipartUpload`
    2. Include the Amazon Resource Name (ARN) that identifies the Amazon S3 bucket and objects in the bucket. The ARN
     format for accessing Amazon S3 is: `arn:aws:s3:::`amzn-s3-demo-bucket`/*`For more information on creating an IAM policy for Aurora PostgreSQL, see [Creating and using an IAM policy for IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md"). See also [Tutorial: Create and

attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the
_IAM User Guide_.

The following AWS CLI command creates an IAM policy named
`rds-s3-export-policy` with these options. It grants access to a
bucket named `amzn-s3-demo-bucket`.

###### Warning

We recommend that you set up your database within a private VPC that has
endpoint policies configured for accessing specific buckets. For more
information, see [Using endpoint policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3") in the
Amazon VPC User Guide.

We strongly recommend that you do not create a policy with all-resource
access. This access can pose a threat for data security. If you create a
policy that gives `S3:PutObject` access to all resources using
`"Resource":"*"`, then a user with export privileges can
export data to all buckets in your account. In addition, the user can export
data to _any publicly writable bucket within your AWS
Region_.

After you create the policy, note the Amazon Resource Name (ARN) of the
policy. You need the ARN for a subsequent step when you attach the policy to an
IAM role.

```
aws iam create-policy  --policy-name rds-s3-export-policy  --policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "s3export",
         "Action": [
           "s3:PutObject*",
           "s3:ListBucket",
           "s3:GetObject*",
           "s3:DeleteObject*",
           "s3:GetBucketLocation",
           "s3:AbortMultipartUpload"
         ],
         "Effect": "Allow",
         "Resource": [
           "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
         ]
       }
     ]
   }'
```

2. Create an IAM role.

You do this so Aurora PostgreSQL can assume this IAM role on your behalf
to access your Amazon S3 buckets. For more information, see [Creating a role to
delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the
_IAM User Guide_.

We recommend using the `aws:SourceArn` and
`aws:SourceAccount`
global condition context keys in resource-based policies to limit the service's permissions to a specific
resource. This is the most effective way to protect against the [confused
deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

If you use both global condition context keys and the
`aws:SourceArn` value contains the account ID, the `aws:SourceAccount` value and
the account in the `aws:SourceArn` value must use the same account ID when used in the
same policy statement.

    * Use `aws:SourceArn` if you want cross-service access for a single resource.
    * Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

In the policy, be sure to use
the `aws:SourceArn` global condition context key with the full ARN of the resource.
The following example shows how to do so using the AWS CLI command to create a role named
`rds-s3-export-role`.

###### Example

For Linux, macOS, or Unix:

```
aws iam create-role  \
    --role-name rds-s3-export-role  \
    --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole",
         "Condition": {
             "StringEquals": {
                "aws:SourceAccount": "`111122223333`",
                "aws:SourceArn": "`arn:aws:rds:us-east-1:111122223333:cluster:dbname`"
                }
             }
       }
     ]
   }'
```

For Windows:

```
aws iam create-role  ^
    --role-name rds-s3-export-role  ^
    --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole",
         "Condition": {
             "StringEquals": {
                "aws:SourceAccount": "`111122223333`",
                "aws:SourceArn": "`arn:aws:rds:us-east-1:111122223333:cluster:dbname`"
                }
             }
       }
     ]
   }'
```

3. Attach the IAM policy that you created to the IAM role that you
   created.

The following AWS CLI command attaches the policy created earlier to the role
named `rds-s3-export-role.` Replace
`your-policy-arn` with the policy
ARN that you noted in an earlier step.

```
aws iam attach-role-policy  --policy-arn `your-policy-arn`  --role-name rds-s3-export-role
```

4. Add the IAM role to the DB cluster. You do so by using the AWS Management Console or
   AWS CLI, as described following.

###### To add an IAM role for a PostgreSQL DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose the PostgreSQL DB cluster
   name to display its
   details.
3. On the **Connectivity & security** tab, in the
   **Manage IAM roles** section, choose the role to
   add under **Add IAM roles to this instance**.
4. Under **Feature**, choose
   **s3Export**.
5. Choose **Add role**.

###### To add an IAM role for a PostgreSQL DB cluster using the CLI

- Use the following command to add the role to the PostgreSQL DB cluster
  named `my-db-cluster`. Replace
  `your-role-arn` with the
  role ARN that you noted in a previous step. Use `s3Export`
  for the value of the `--feature-name` option.

###### Example

For Linux, macOS, or Unix:

```
aws rds add-role-to-db-cluster \
   --db-cluster-identifier `my-db-cluster` \
   --feature-name s3Export \
   --role-arn `your-role-arn`   \
   --region `your-region`
```

For Windows:

```
aws rds add-role-to-db-cluster ^
   --db-cluster-identifier `my-db-cluster` ^
   --feature-name s3Export ^
   --role-arn `your-role-arn` ^
   --region `your-region`
```
