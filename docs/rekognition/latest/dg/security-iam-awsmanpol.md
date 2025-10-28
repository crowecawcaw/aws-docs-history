# AWS managed policies for Amazon Rekognition

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AmazonRekognitionFullAccess

`AmazonRekognitionFullAccess` grants full access to Amazon Rekognition resources including creating and
deleting collections.

You can attach the `AmazonRekognitionFullAccess` policy to your IAM identities.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rekognition:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonRekognitionReadOnlyAccess

`AmazonRekognitionReadOnlyAccess` grants read-only access to Amazon Rekognition resources.

You can attach the `AmazonRekognitionReadOnlyAccess` policy to your IAM identities.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonRekognitionReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "rekognition:CompareFaces",
 "rekognition:DetectFaces",
 "rekognition:DetectLabels",
 "rekognition:ListCollections",
 "rekognition:ListFaces",
 "rekognition:SearchFaces",
 "rekognition:SearchFacesByImage",
 "rekognition:DetectText",
 "rekognition:GetCelebrityInfo",
 "rekognition:RecognizeCelebrities",
 "rekognition:DetectModerationLabels",
 "rekognition:GetLabelDetection",
 "rekognition:GetFaceDetection",
 "rekognition:GetContentModeration",
 "rekognition:GetPersonTracking",
 "rekognition:GetCelebrityRecognition",
 "rekognition:GetFaceSearch",
 "rekognition:GetTextDetection",
 "rekognition:GetSegmentDetection",
 "rekognition:DescribeStreamProcessor",
 "rekognition:ListStreamProcessors",
 "rekognition:DescribeProjects",
 "rekognition:DescribeProjectVersions",
 "rekognition:DetectCustomLabels",
 "rekognition:DetectProtectiveEquipment",
 "rekognition:ListTagsForResource",
 "rekognition:ListDatasetEntries",
 "rekognition:ListDatasetLabels",
 "rekognition:DescribeDataset",
 "rekognition:ListProjectPolicies",
 "rekognition:ListUsers",
 "rekognition:SearchUsers",
 "rekognition:SearchUsersByImage",
 "rekognition:GetMediaAnalysisJob",
 "rekognition:ListMediaAnalysisJobs"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AmazonRekognitionServiceRole

`AmazonRekognitionServiceRole` allows Amazon Rekognition to call Amazon Kinesis Data Streams and
Amazon SNS services on your behalf.

You can attach the `AmazonRekognitionServiceRole` policy to your IAM
identities.

If using this service role, you should keep your account secure by limiting the scope
of Amazon Rekognition's access to just the resources you are using. This can be done by attaching a
trust policy to your IAM service role. For information on how to do this, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:*:*:AmazonRekognition*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:PutRecord",
 "kinesis:PutRecords"
 ],
 "Resource": "arn:aws:kinesis:*:*:stream/AmazonRekognition*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:GetDataEndpoint",
 "kinesisvideo:GetMedia"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonRekognitionCustomLabelsFullAccess

This policy is for Amazon Rekognition Custom Labels; users. Use the AmazonRekognitionCustomLabelsFullAccess
policy to allow users full access to the Amazon Rekognition Custom Labels API and full access to the
console buckets created by the Amazon Rekognition Custom Labels console.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:GetObjectVersion",
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::*custom-labels*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "rekognition:CopyProjectVersion",
 "rekognition:CreateProject",
 "rekognition:CreateProjectVersion",
 "rekognition:StartProjectVersion",
 "rekognition:StopProjectVersion",
 "rekognition:DescribeProjects",
 "rekognition:DescribeProjectVersions",
 "rekognition:DetectCustomLabels",
 "rekognition:DeleteProject",
 "rekognition:DeleteProjectVersion",
 "rekognition:TagResource",
 "rekognition:UntagResource",
 "rekognition:ListTagsForResource",
 "rekognition:CreateDataset",
 "rekognition:ListDatasetEntries",
 "rekognition:ListDatasetLabels",
 "rekognition:DescribeDataset",
 "rekognition:UpdateDatasetEntries",
 "rekognition:DistributeDatasetEntries",
 "rekognition:DeleteDataset",
 "rekognition:PutProjectPolicy",
 "rekognition:ListProjectPolicies",
 "rekognition:DeleteProjectPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon Rekognition updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Rekognition since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the Amazon Rekognition
Document
history page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                 | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Actions involving media analysis jobs have been added to the following managed policy: <br>• [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess "#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess")                                                                                                                                                                                                                                                                                                                      | Amazon Rekognition added the following actions to the `AmazonRekognitionReadOnlyAccess` managed policy: <br>• `GetMediaAnalysisJob` <br>• `ListMediaAnalysisJob`                                                                                                                                                                                                            | October 31st, 2023 |
| Actions involving managing users have been added to the following managed policy: <br>• [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess "#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess")                                                                                                                                                                                                                                                                                                                           | Amazon Rekognition added the following actions to the `AmazonRekognitionReadOnlyAccess` managed policy: <br>• `ListUsers` <br>• `SearchUsers` <br>• `SearchUsersByImage`                                                                                                                                                                                                    | June 12th, 2023    |
| Actions for ProjectPolicy and Custom Labels Model Copy have been added to the following managed policies: <br>• [AWS managed policy: AmazonRekognitionFullAccess](#security-iam-awsmanpol-AmazonRekognitionFullAccess "#security-iam-awsmanpol-AmazonRekognitionFullAccess") <br>• [AWS managed policy: AmazonRekognitionCustomLabelsFullAccess](#security-iam-awsmanpol-custom-labels-full-access "#security-iam-awsmanpol-custom-labels-full-access")                                                                                                                                    | Amazon Rekognition added the following actions to the `AmazonRekognitionCustomLabelsFullAccess` and `AmazonRekognitionFullAccess` managed policies: <br>• `CopyProjectVersion` <br>• `PutProjectPolicy` <br>• `ListProjectPolicies` <br>• `DeleteProjectPolicy`                                                                                                             | July 21st, 2022    |
| Actions for ProjectPolicy and Custom Labels Model Copy have been added to the following managed policies: <br>• [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess "#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess")                                                                                                                                                                                                                                                                                                   | Amazon Rekognition added the following actions to the AmazonRekognitionReadOnlyAccess managed policy: <br>• `ListProjectPolicies`                                                                                                                                                                                                                                           | July 21st, 2022    |
| Dataset management update for the following managed policies: <br>• [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess "#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess") <br>• [AWS managed policy: AmazonRekognitionFullAccess](#security-iam-awsmanpol-AmazonRekognitionFullAccess "#security-iam-awsmanpol-AmazonRekognitionFullAccess") <br>• [AWS managed policy: AmazonRekognitionCustomLabelsFullAccess](#security-iam-awsmanpol-custom-labels-full-access "#security-iam-awsmanpol-custom-labels-full-access") | Amazon Rekognition added the following actions to the AmazonRekognitionReadOnlyAccess, AmazonRekognitionFullOnlyAccess, and AmazonRekognitionCustomLabelsFullAccess managed policies <br>• `CreateDataset` <br>• `ListDatasetEntries` <br>• `ListDatasetLabels` <br>• `DescribeDataset` <br>• `UpdateDatasetEntries` <br>• `DistributeDatasetEntries` <br>• `DeleteDataset` | November 1, 2021   |
| Tagging update for [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess "#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess") and [AWS managed policy: AmazonRekognitionFullAccess](#security-iam-awsmanpol-AmazonRekognitionFullAccess "#security-iam-awsmanpol-AmazonRekognitionFullAccess")                                                                                                                                                                                                                               | Amazon Rekognition added new tagging actions to the AmazonRekognitionFullAccess and AmazonRekognitionReadOnlyAccess policies.                                                                                                                                                                                                                                               | April 2, 2021      |
| Amazon Rekognition started tracking changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Amazon Rekognition started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                   | April 2, 2021      |
