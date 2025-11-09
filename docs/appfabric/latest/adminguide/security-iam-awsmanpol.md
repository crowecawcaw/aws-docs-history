# AWS managed policies for AWS AppFabric

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
Services don't remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy:

AWSAppFabricReadOnlyAccess

You can attach the `AWSAppFabricReadOnlyAccess` policy to your IAM
identities. This policy grants read-only permissions to the AppFabric service.

###### Note

The `AWSAppFabricReadOnlyAccess` policy does not grant read-only access to
the AppFabric for productivity features.

**Permissions details**

This policy includes the following permissions:

- `appfabric` – Grants permission to get an app bundle, list app
  bundles, get an app authorization, list app authorizations, get an ingestion, list
  ingestions, get an ingestion destination, list ingestion destinations, and list
  resource tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "appfabric:GetAppAuthorization",
 "appfabric:GetAppBundle",
 "appfabric:GetIngestion",
 "appfabric:GetIngestionDestination",
 "appfabric:ListAppAuthorizations",
 "appfabric:ListAppBundles",
 "appfabric:ListIngestionDestinations",
 "appfabric:ListIngestions",
 "appfabric:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AWSAppFabricFullAccess

You can attach the `AWSAppFabricFullAccess` policy to your IAM identities.
This policy grants administrative permissions to the AppFabric service.

###### Important

The `AWSAppFabricFullAccess` policy does not grant access to the
AppFabric for productivity features because they are currently in preview. For more information about
ranting access to the AppFabric for productivity features, see [AppFabric for productivity IAM policy
examples](security_iam_id-based-policy-examples.md#appfabric-for-productivity-policy-examples "security_iam_id-based-policy-examples.md#appfabric-for-productivity-policy-examples").

**Permissions details**

This policy includes the following permissions:

- `appfabric` – Grants full administrative permission to
  AppFabric.
- `kms` – Grants permission to list aliases.
- `s3` – Grants permission to list all of your Amazon S3 buckets, and
  get bucket location.
- `firehose` – Grants permission to list Amazon Data Firehose delivery
  streams, and describe delivery streams.
- `iam` – Grants permission to create the
  `AWSServiceRoleForAppFabric` service-linked role for AppFabric. For more
  information, see [Using service-linked roles for
  AppFabric](using-service-linked-roles.md "using-service-linked-roles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["appfabric:*"],
 "Resource": "*"
 },
 {
 "Sid": "KMSListAccess",
 "Effect": "Allow",
 "Action": ["kms:ListAliases"],
 "Resource": "*"
 },
 {
 "Sid": "S3ReadAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "FirehoseReadAccess",
 "Effect": "Allow",
 "Action": [
 "firehose:DescribeDeliveryStream",
 "firehose:ListDeliveryStreams"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUseOfServiceLinkedRole",
 "Effect": "Allow",
 "Action": ["iam:CreateServiceLinkedRole"],
 "Condition": {
 "StringEquals": {"iam:AWSServiceName": "appfabric.amazonaws.com"}
 },
 "Resource": "arn:aws:iam::*:role/aws-service-role/appfabric.amazonaws.com/AWSServiceRoleForAppFabric"
 }
 ]
}`

```

## AWS managed

policy: AWSAppFabricServiceRolePolicy

You can't attach the `AWSAppFabricServiceRolePolicy` policy to your IAM
entities. This policy is attached to a service-linked role that allows AppFabric to perform
actions on your behalf. For more information, see [Using service-linked roles for
AppFabric](using-service-linked-roles.md "using-service-linked-roles.md").

**Permissions details**

This policy includes the following permissions:

- `cloudwatch` – Grants permission for AppFabric to put metric data
  into the Amazon CloudWatch `AWS/AppFabric` namespace. For more information about
  the AppFabric metrics available in CloudWatch, see [Monitoring AWS AppFabric with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- `s3` – Grants permission for AppFabric to put ingested data into an
  Amazon S3 bucket that you specify.
- `firehose` – Grants permission for AppFabric to put ingested data
  into an Amazon Data Firehose delivery stream that you specify.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchEmitMetric",
 "Effect": "Allow",
 "Action": ["cloudwatch:PutMetricData"],
 "Resource": "*",
 "Condition": {
 "StringEquals": {"cloudwatch:namespace": "AWS/AppFabric"}
 }
 },
 {
 "Sid": "S3PutObject",
 "Effect": "Allow",
 "Action": ["s3:PutObject"],
 "Resource": "arn:aws:s3:::*/AWSAppFabric/*",
 "Condition": {
 "StringEquals": {"s3:ResourceAccount": "${aws:PrincipalAccount}"}
 }
 },
 {
 "Sid": "FirehosePutRecord",
 "Effect": "Allow",
 "Action": ["firehose:PutRecordBatch"],
 "Resource": "arn:aws:firehose:*:*:deliverystream/*",
 "Condition": {
 "StringEqualsIgnoreCase": {"aws:ResourceTag/AWSAppFabricManaged": "true"}
 }
 }
 ]
}`

```

## AppFabric updates to AWS managed

policies

View details about updates to AWS managed policies for AppFabric since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the [AppFabric Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                         | Description                                                                                   | Date          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------- |
| [AWSAppFabricReadOnlyAccess](#security-iam-awsmanpol-AWSAppFabricReadOnlyAccess "#security-iam-awsmanpol-AWSAppFabricReadOnlyAccess") – New<br>policy          | AppFabric added a new policy to grant read-only permissions to the AppFabric<br>service.      | June 27, 2023 |
| [AWSAppFabricFullAccess](#security-iam-awsmanpol-AWSAppFabricFullAccess "#security-iam-awsmanpol-AWSAppFabricFullAccess") – New<br>policy                      | AppFabric added a new policy to grant administrative permissions to the<br>AppFabric service. | June 27, 2023 |
| [AWSAppFabricServiceRolePolicy](#security-iam-awsmanpol-AWSAppFabricServiceRolePolicy "#security-iam-awsmanpol-AWSAppFabricServiceRolePolicy") – New<br>policy | AppFabric added a new policy for the<br>`AWSServiceRoleForAppFabric` service-linked role.     | June 27, 2023 |
| AppFabric started tracking changes                                                                                                                             | AppFabric started tracking changes for its AWS managed policies.                              | June 27, 2023 |
