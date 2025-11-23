# Access AWS resources using an IAM Execution Role

Device Farm supports specifying an IAM role that will be assumed by the custom test runtime environment during test execution. This feature allows your tests to securely access AWS resources in your account, such as Amazon S3 buckets, DynamoDB tables, or other AWS services on which your application depends.

###### Topics

- [Overview](#iam-execution-role-overview "#iam-execution-role-overview")
- [IAM role requirements](#iam-role-requirements "#iam-role-requirements")
- [Configuring an IAM execution role](#configuring-iam-execution-role "#configuring-iam-execution-role")
- [Best practices](#iam-role-best-practices "#iam-role-best-practices")
- [Troubleshooting](#troubleshooting-iam-roles "#troubleshooting-iam-roles")

## Overview

When you specify an IAM execution role, Device Farm assumes this role during test execution, allowing your tests to interact with AWS services using the permissions defined in the role.

Common use cases for IAM execution roles include:

- Accessing test data stored in Amazon S3 buckets
- Pushing test artifacts to Amazon S3 buckets
- Retrieving application configuration from AWS AppConfig
- Writing test logs and metrics to Amazon CloudWatch
- Sending test results or status messages to Amazon SQS queues
- Calling AWS Lambda functions as part of test workflows

## IAM role requirements

To use an IAM execution role with Device Farm, your role must meet the following requirements:

- **Trust relationship**: The Device Farm service principal must be trusted to assume the role. The trust policy must include `devicefarm.amazonaws.com` as a trusted entity.
- **Permissions**: The role must have the necessary permissions to access the AWS resources your tests require.
- **Session duration**: The role's maximum session duration must be at least as long as your Device Farm project's job timeout setting. By default, Device Farm projects have a job timeout of 150 minutes, so your role must support a session duration of at least 150 minutes.
- **Same account requirement**: The IAM role must be in the same AWS account as the one used to call Device Farm. Cross-account role assumption is not supported.
- **PassRole permission**: The caller must be authorized to pass the IAM role by a policy allowing the `iam:PassRole` action on the specified execution role.

### Example trust policy

The following example shows a trust policy that allows Device Farm to assume your execution role. This trust policy should only be attached to the specific IAM role you intend to use with Device Farm, not to other roles in your account:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "devicefarm.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Example permissions policy

The following example shows a permissions policy that grants access to common AWS services used in testing:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-test-bucket",
        "arn:aws:s3:::my-test-bucket/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "appconfig:GetConfiguration",
        "appconfig:StartConfigurationSession"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:/devicefarm/test-*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "sqs:SendMessage",
        "sqs:GetQueueUrl"
      ],
      "Resource": "arn:aws:sqs:*:*:test-results-*"
    }
  ]
}
```

## Configuring an IAM execution role

You can specify an IAM execution role at the project level or for individual test runs. When configured at the project level, all runs within that project will inherit the execution role. An execution role configured on a run will supersede any configured on its parent project.

For detailed instructions on configuring execution roles, see:

- [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md") - for configuring execution roles at the project level
- [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md") - for configuring execution roles for individual runs

You can also configure execution roles using the Device Farm API. For more information, see the [Device Farm API Reference](../APIReference.md "../APIReference.md").

## Best practices

Follow these best practices when configuring IAM execution roles for your Device Farm tests:

- **Principle of least privilege**: Grant only the minimum permissions necessary for your tests to function. Avoid using overly broad permissions like `*` actions or resources.
- **Use resource-specific permissions**: When possible, limit permissions to specific resources (e.g., specific S3 buckets or DynamoDB tables) rather than all resources of a type.
- **Separate test and production resources**: Use dedicated test resources and roles to avoid accidentally affecting production systems during testing.
- **Regular role review**: Periodically review and update your execution roles to ensure they still meet your testing needs and follow security best practices.
- **Use condition keys**: Consider using IAM condition keys to further restrict when and how the role can be used.

## Troubleshooting

If you encounter issues with IAM execution roles, check the following:

- **Trust relationship**: Verify that the role's trust policy includes `devicefarm.amazonaws.com` as a trusted service.
- **Permissions**: Check that the role has the necessary permissions for the AWS services your tests are trying to access.
- **Test logs**: Review the test execution logs for specific error messages related to AWS API calls or permission denials.
