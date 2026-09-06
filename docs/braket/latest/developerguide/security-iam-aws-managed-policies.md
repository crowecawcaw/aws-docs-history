

# AWS managed policies for Amazon Braket
<a name="security-iam-aws-managed-policies"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: AmazonBraketFullAccess](#about-amazonbraketfullaccess)
+ [AWS managed policy: AmazonBraketJobsExecutionPolicy](#about-amazonbraketjobsexecution)
+ [AWS managed policy: AmazonBraketServiceRolePolicy](#about-amazonbraketservicerolepolicy)
+ [Amazon Braket updates to AWS managed policies](#braket-aws-managed-policy-updates)

## AWS managed policy: AmazonBraketFullAccess
<a name="about-amazonbraketfullaccess"></a>

The **AmazonBraketFullAccess** policy grants permissions for Amazon Braket operations, including permissions for these tasks:
+  **Download containers from Amazon Elastic Container Registry** – To read and download container images that are used for the Amazon Braket Hybrid Jobs feature. The containers must conform to the format "arn:aws:ecr:::repository/amazon-braket".
+  **Keep AWS CloudTrail logs** – For all *describe*, *get*, and *list* actions in addition to starting and stopping queries, testing metrics filters, and filtering log events. The AWS CloudTrail log file contains a record of all Amazon Braket API activity that occurs in your account.
+  **Utilize roles to control resources** – To create a service-linked role in your account. The service-linked role has access to AWS resources on your behalf. It can be used only by the Amazon Braket service. Also, to pass in IAM roles to the Amazon Braket `CreateJob` API and to create a role and attach a policy scoped to AmazonBraketFullAccess to the role.
+  **Create log groups, log events, and query log groups in order to maintain usage log files for your account** – To create, store, and view logging information about Amazon Braket usage in your account. Query metrics on hybrid jobs log groups. Encompass the proper Braket path and allow putting log data. Put metric data in CloudWatch.
+  **Create and store data in Amazon S3 buckets, and list all buckets** – To create S3 buckets, list the S3 buckets in your account, and put objects into and get objects from any bucket in your account whose name begins with *amazon-braket-* or that is [ABAC-enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html) and tagged with `"AmazonBraket": "true"`. These permissions are required for Braket to put files containing results from processed quantum tasks into the bucket and to retrieve them from the bucket.
+  **Pass IAM roles** – To pass in IAM roles to the `CreateJob` API.
+  ** Amazon SageMaker AI Notebook** – To create and manage SageMaker notebook instances scoped to the resource from "arn:aws:sagemaker:::notebook-instance/amazon-braket-".
+  ** Validate service quotas** – To create SageMaker AI notebooks and Amazon Braket Hybrid jobs, your resource counts cannot exceed [quotas for your account](braket-quotas.md).
+  ** View product pricing** – Review and plan quantum hardware costs before submitting your workloads.

To view the permissions for this policy, see [AmazonBraketFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBraketFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonBraketJobsExecutionPolicy
<a name="about-amazonbraketjobsexecution"></a>

The **AmazonBraketJobsExecutionPolicy** policy grants permissions for execution roles used in Amazon Braket Hybrid Jobs as follows:
+  **Download containers from Amazon Elastic Container Registry** - Permissions to read and download container images that are used for the Amazon Braket Hybrid Jobs feature. Containers must conform to the format "arn:aws:ecr:\*:\*:repository/amazon-braket\*".
+  **Create log groups and log events and query log groups in order to maintain usage log files for your account** – Create, store, and view logging information about Amazon Braket usage in your account. Query metrics on hybrid jobs log groups. Encompass the proper Braket path and allow putting log data. Put metric data in CloudWatch.
+  **Store data in Amazon S3 buckets** – List the S3 buckets in your account, put objects into and get objects from any bucket in your account that starts with *amazon-braket-* in its name or that is [ABAC-enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html) and tagged with `"AmazonBraket": "true"`. These permissions are required for Braket to put files containing results from processed quantum tasks into the bucket, and to retrieve them from the bucket.
+  **Pass IAM roles** – Passing in IAM roles to the CreateJob API. Roles must conform to the format arn:aws:iam::\*:role/service-role/AmazonBraketJobsExecutionRole\*.

To view the permissions for this policy, see [AmazonBraketJobsExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBraketJobsExecutionPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonBraketServiceRolePolicy
<a name="about-amazonbraketservicerolepolicy"></a>

The **AmazonBraketServiceRolePolicy** policy grants permissions for Amazon Braket operations, including permissions for these tasks:
+  **Amazon S3** – permissions to list the buckets in your account, and put objects into and get objects from any bucket in your account with a name that starts with `amazon-braket-` or that is [ABAC-enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html) and tagged with `"AmazonBraket": "true"`.
+  **Amazon CloudWatch Logs** – permissions to list and create log groups, create the associated log streams, and put events into the log group created for Amazon Braket.

For more information on service-linked roles, see [Amazon Braket service-linked role](braket-slr.md).

To view the permissions for this policy, see [AmazonBraketServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBraketServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Amazon Braket updates to AWS managed policies
<a name="braket-aws-managed-policy-updates"></a>

The following table provides details about updates to AWS managed policies for Amazon Braket from the time this service began tracking these changes.


|  **Change**  |  **Description**  |  **Date**  | 
| --- | --- | --- | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  |  Added Amazon S3 permissions for arbitrarily-named buckets with the **"aws:ResourceAccount": "${aws:PrincipalAccount}"** and **"aws:ResourceTag/AmazonBraket": "true"** condition scope.  | July 6, 2026 | 
|  [AmazonBraketJobsExecutionPolicy](#about-amazonbraketjobsexecution) - Jobs execution policy  |  Added Amazon S3 permissions for arbitrarily-named buckets with the **"aws:ResourceTag/AmazonBraket": "true"** condition scope.  | July 6, 2026 | 
|  [ AmazonBraketServiceRolePolicy](#about-amazonbraketservicerolepolicy) - Resource management policy  |  Added Amazon S3 permissions for arbitrarily-named buckets with the **"aws:ResourceAccount": "${aws:PrincipalAccount}"** and **"aws:ResourceTag/AmazonBraket": "true"** condition scope.  | July 6, 2026 | 
|  [ AmazonBraketServiceRolePolicy](#about-amazonbraketservicerolepolicy) - Resource management policy |  Added the **"aws:ResourceAccount" : "${aws:PrincipalAccount}"** condition scope to Amazon S3 and CloudWatch logs actions.  | July 11, 2025 | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  |  Added the **"pricing:GetProducts"** action.  | April 14, 2025 | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  |  Added the **"aws:ResourceAccount": "${aws:PrincipalAccount}"** condition scope to S3 actions.  | March 7, 2025 | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  | Added the **servicequotas:GetServiceQuota** and **cloudwatch:GetMetricData** actions. | March 24, 2023 | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  | Added the **s3:ListAllMyBuckets** permissions to view and inspect the used Amazon S3 buckets. | March 31, 2022 | 
|  [AmazonBraketFullAccess](#about-amazonbraketfullaccess) - Full access policy for Braket  |  Braket adjusted iam:PassRole permissions for AmazonBraketFullAccess to include the `service-role/` path. | November 29, 2021 | 
|  [AmazonBraketJobsExecutionPolicy](#about-amazonbraketjobsexecution) - Hybrid jobs execution policy for Amazon Braket Hybrid Jobs |  Braket updated the hybrid jobs execution role ARN to include the `service-role/` path. | November 29, 2021 | 
|  Braket started tracking changes |  Braket started tracking changes for its AWS managed policies. | November 29, 2021 | 