# Troubleshooting AWS B2B Data Interchange

This section provides solutions to common issues you might encounter when working with
AWS B2B Data Interchange.

## Output file is not created after the input

file is placed into an Amazon S3 bucket

If your output file is not being created after placing an input file into an Amazon S3
bucket, follow these troubleshooting steps:

1. If you have logs enabled, first check AWS B2B Data Interchange service logs in CloudWatch.
   Specifically, check the default log group
   `/aws/vendedlogs/b2bi/default` for general errors and profile log
   group
   `/aws/vendedlogs/b2bi/profile/`profile-id``
   for profile and partnership specific errors. If logs contain errors, address
   them.
2. Check that the input file is not being misplaced and you are placing it into
   the correct directory of the Amazon S3 bucket assigned as an input bucket of your
   trading capability. For inbound use-case the files must be placed in a directory
   with the `.../`trading-partner-id`/` prefix,
   and for the outbound use-case they must be placed in a directory with the
   `.../`trading-capability-id`/`trading-partner-id`/`
   prefix.
3. Check that the input bucket is configured to emit EventBridge events.
   1. Go to the Amazon S3 console and select your bucket.
   2. Choose **Properties**.
   3. Scroll down to the **Event Notifications** section
      and ensure that **Send notifications to Amazon EventBridge for all events
      in this bucket** configuration is set to
      **On**.

## Transformation fails because of S3

bucket access issues

If your transformation is failing due to S3 bucket access issues, follow these
troubleshooting steps:

1. Ensure that the S3 bucket policy is configured to allow AWS B2B Data Interchange service to
   access the S3 bucket. For that follow the documentation steps in [Setting up S3 bucket policies and
   permissions](b2bi-prereq.md#buckets-and-permissions "b2bi-prereq.md#buckets-and-permissions").
2. If you have SSE-KMS or DSSE-KMS encryption enabled on your input or output
   bucket, ensure that the key policy in AWS KMS is updated. For that follow the
   documentation steps in [Setting up S3 bucket policies and
   permissions](b2bi-prereq.md#buckets-and-permissions "b2bi-prereq.md#buckets-and-permissions").
3. In case S3 bucket issue arises when directly invoking
   `StartTransformerJob` ensure that the invoking principal (e.g.,
   user, service role) has permissions to access the bucket. Moreover ensure that
   the user that is invoking `StartTransformerJob` is not the
   `root` user.
4. Make sure you are using AWS B2B Data Interchange service in the same region the S3 bucket is
   created in.

## The output file is successfully created but

it cannot be accessed

If your output file is created successfully but cannot be accessed, follow these
troubleshooting steps:

- Ensure that the output S3 bucket does not have ACL enabled.
  1.  Go to the Amazon S3 console and select your bucket.
  2.  Choose **Permissions**.
  3.  Scroll down to the **Object Ownership** section and
      ensure that it says that ACLs are disabled.

## Attaching sample files fails when creating

a transformer in the console under root user

If attaching sample files fails when creating a transformer in the console, follow
these troubleshooting steps:

1. Avoid using a root user to configure AWS B2B Data Interchange and specifically attach sample
   files in console.
2. Instead create a regular IAM user with necessary AWS B2B Data Interchange and Amazon S3
   permissions. For that follow the documentation steps in [Prerequisites for using AWS B2B Data Interchange](b2bi-prereq.md "b2bi-prereq.md").

## Policy length limit reached when Creating

Resources

In the case that you try to create a resource (such as a profile or transformer), and
experience an error saying the policy limit has been reached, you need to modify your
Amazon CloudWatch Logs resource policy. By default, CloudWatch Logs has a resource policy length limit that can
affect AWS B2B Data Interchange operations when you manage a large number of resources.

###### To modify your CloudWatch Logs resource policy:

1. Sign in to AWS CLI.
2. Add the following policy to enable B2B Data Interchange to deliver logs to resource log
   groups using the following command. Replace `REGION`
   and `ACCOUNT_ID` with your actual values for region and
   AWS account ID. For the policy name, we suggest using
   `AWSLogsDeliveryWriteB2Bi`, but you can choose your own
   name for the policy.

```
aws logs put-resource-policy \
--policy-name "AWSLogsDeliveryWriteB2Bi" \
--policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AWSLogDeliveryWrite",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "delivery.logs.amazonaws.com"
                ]
            },
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:`REGION`:`ACCOUNT_ID`:log-group:/aws/vendedlogs/b2bi/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`ACCOUNT_ID`"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:logs:`REGION`:`ACCOUNT_ID`:*"
                }
            }
        }
    ]
 }'
```

## Getting additional support

If you're unable to resolve an issue using the troubleshooting information in this
guide, you can get additional help through the following channels:

- [AWS Support
  Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") – Create a support case if you have an AWS Support
  plan.
- [AWS Contact Us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") –
  Contact AWS directly for account or billing questions.

When contacting support, be prepared to provide:

- Your AWS account ID
- The specific resource IDs involved (profiles, partnerships, etc.)
- Error messages and timestamps
- Steps you've already taken to troubleshoot the issue
