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
  import a segment programmatically by using the AWS SDK for Java, see [Import segments in Amazon Pinpoint](segments-importing.md "segments-importing.md") in this guide.

## Creating the IAM role

(AWS CLI)

Complete the following steps to create the IAM role by using the AWS Command Line Interface (AWS CLI).
If you haven't installed the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_.

###### To create the IAM role by using the AWS CLI

1. Create a JSON file that contains the trust policy for your role, and save the
   file locally. You can use the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`application-id`"
 }
 }
 }
 ]
}`

```

In the preceding example, do the following:

    * Replace `region` with the AWS Region that
     you use Amazon Pinpoint in.
    * Replace `accountId` with the unique ID for
     your AWS account.
    * Replace `application-id` with the unique ID
     of the project.

2. At the command line, use the [`create-role`](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create the role and attach
   the trust policy:

```
aws iam create-role --role-name `PinpointSegmentImport` --assume-role-policy-document file://`PinpointImportTrustPolicy`.json
```

Following the `file://` prefix, specify the path to the JSON file
that contains the trust policy.

After you run this command, you see output that's similar to the following in
your terminal: 3. Use the [`attach-role-policy`](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command to attach the
`AmazonS3ReadOnlyAccess` AWS managed policy to the role:

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess --role-name `PinpointSegmentImport`
```
