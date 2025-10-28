**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# IAM role for importing endpoints or

segments

With Amazon Pinpoint, you can define a user segment by importing endpoint definitions from an
Amazon Simple Storage Service (Amazon S3) bucket in your AWS account. Before you import, you must delegate the
required permissions to Amazon Pinpoint. To do this, you create an AWS Identity and Access Management (IAM) role and
attach the following policies to the role:

- The `AmazonS3ReadOnlyAccess` AWS managed policy. This policy is
  created and managed by AWS, and it grants read-only access to your Amazon S3
  bucket.
- A trust policy that allows Amazon Pinpoint to assume the role.
  After you create the role, you can use Amazon Pinpoint to import segments from an Amazon S3 bucket.
  For information about creating the bucket, creating endpoint files, and importing a segment
  by using the console, see [Importing
  segments](../userguide/segments-importing.md "../userguide/segments-importing.md") in the _Amazon Pinpoint User Guide_. For an example of how to
  import a segment programmatically by using the AWS SDK for Java, see [Importing segments](../developerguide/segments-importing.md "../developerguide/segments-importing.md")
  in the _Amazon Pinpoint Developer Guide_.

## Attaching the trust

policy

To allow Amazon Pinpoint to assume the IAM role and perform the actions allowed by the
`AmazonS3ReadOnlyAccess` policy, attach the following trust policy to the
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUserToImportEndpointDefinitions",
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Creating the IAM role

(AWS CLI)

Complete the following steps to create the IAM role by using the AWS Command Line Interface (AWS CLI).
If you haven't installed the AWS CLI, see [Install or update to the latest
version of AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the _AWS Command Line Interface User Guide_.

###### To create the IAM role by using the AWS CLI

1. Create a JSON file that contains the trust policy for your role, and save the
   file locally. You can copy the trust policy provided in this topic.
2. At the command line, use the [`create-role`](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create the role and attach
   the trust policy:

```
aws iam create-role --role-name `PinpointSegmentImport` --assume-role-policy-document file://`PinpointImportTrustPolicy`.json
```

Following the `file://` prefix, specify the path to the JSON file
that contains the trust policy.

After you run this command, you will see an output that's similar to the
following in your terminal: 3. Use the [`attach-role-policy`](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command to attach the
`AmazonS3ReadOnlyAccess` AWS managed policy to the role:

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess --role-name `PinpointSegmentImport`
```
