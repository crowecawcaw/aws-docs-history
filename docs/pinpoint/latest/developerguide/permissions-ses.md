**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# IAM role for sending email with Amazon SES

Amazon Pinpoint uses your Amazon SES resources to send email for your campaign or journey. Before
Amazon Pinpoint can use your Amazon SES resources to send email, you must grant the required
permissions to Amazon Pinpoint. Your account must have the `iam:PutRolePolicy` and
`iam:UpdateAssumeRolePolicy` permissions to update or create IAM
roles.

The Amazon Pinpoint console can automatically create an AWS Identity and Access Management (IAM) role with the required
permissions. For more information, see [Creating an email orchestration sending role](../userguide/channels-email-orchestration-sending-role.md "../userguide/channels-email-orchestration-sending-role.md") in the
_Amazon Pinpoint User Guide_.

If you want to create the role manually, attach the following policies to the role:

- A permissions policy that grants Amazon Pinpoint access to your Amazon SES resources.
- A trust policy that allows Amazon Pinpoint to assume the role.
  After you create the role, you can configure Amazon Pinpoint to use your Amazon SES resources.

You can test IAM policies with the IAM policy simulator. For more information, see
[Testing IAM policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Creating the IAM role (AWS Management Console)

Complete the following steps to manually create an IAM role for your campaign or
journey to send email.

1. Create a new **permission policy** by following the
   directions in [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
   [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
   1. In [step 5](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor"), use the following **permission policy** for the IAM role.
      - Replace `partition` with the partition
        that the resource is in. For standard AWS Regions, the partition
        is `aws`. If you have resources in other partitions, the partition
        is `aws-partitionname`. For example, the partition for resources
        in the AWS GovCloud (US-West) is `aws-us-gov`.
      - Replace `region` with the name of the AWS Region that hosts the Amazon Pinpoint project.
      - Replace `accountId` with the unique ID for your
        AWS account.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "PinpointUsesSESForEmailSends",
    "Effect": "Allow",
    "Action": [
    "ses:SendEmail",
    "ses:SendRawEmail"
    ],
    "Resource": [
    "arn:aws:ses:`us-east-1`:`111122223333`:identity/*",
    "arn:aws:ses:`us-east-1`:`111122223333`:configuration-set/*"
    ]
    }
    ]
   }`

   ```

2. Create a new **trust policy** by following the
   directions in [Creating a role using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the
   [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
   1. In [step 4](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md"), use the following **trust policy**.
      - Replace `accountId` with the unique ID for your
        AWS account.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "AllowPinpoint",
    "Effect": "Allow",
    "Principal": {
    "Service": "pinpoint.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`accountId`"
    }
    }
    }
    ]
   }`

   ```

   2. In [step 11](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md"), add the **permission policy** that you created in the previous
      step.
