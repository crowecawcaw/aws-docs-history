Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up permissions to

schedule a query

To schedule queries, the AWS Identity and Access Management (IAM) user defining the schedule and the IAM role
associated with the schedule must be configured with the IAM permissions to use
Amazon EventBridge and Amazon Redshift Data API. To receive emails from scheduled queries, the Amazon SNS notification
you optionally specify must be configured also.

The following describes the tasks to use AWS managed policies to provide permission,
but depending on your environment, you might want to scope down the permissions
allowed.

For the IAM user logged into query editor v2, edit the IAM user using the IAM console
([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).

- In addition to permissions to run Amazon Redshift and query editor v2 operations, attach the
  `AmazonEventBridgeFullAccess` and
  `AmazonRedshiftDataFullAccess` AWS managed policies to an IAM
  user.
- Alternatively, assign the permissions to a role and assign the role to the
  user.

Attach a policy that allows the `sts:AssumeRole` permission to the
resource ARN of the IAM role you specify when you define the scheduled query.
For more information about assuming roles, see [Granting
a user permissions to switch roles](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md") in the
_IAM User Guide_.

The following example shows a permission policy that assumes the IAM role
`myRedshiftRole` in account `123456789012`. The IAM
role `myRedshiftRole`is also the IAM role that is attached to the
cluster or workgroup where the scheduled query runs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AssumeIAMRole",
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": [
 "arn:aws:iam::`123456789012`:role/`myRedshiftRole`"
 ]
 }
 ]
}`

```

Update the trust policy of the IAM role used to schedule the query to allow
the IAM user to assume it.

```
{
            "Sid": "AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`123456789012`:user/`myIAMusername`"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

For the IAM role that you specify to allow the scheduled query to run, edit the
IAM role using the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).

- Attach the `AmazonRedshiftDataFullAccess` and
  `AmazonEventBridgeFullAccess` AWS managed policies to the IAM
  role. The `AmazonRedshiftDataFullAccess` managed policy only allows
  `redshift-serverless:GetCredentials` permission for Redshift Serverless
  workgroups that are tagged with the key
  `RedshiftDataFullAccess`.
