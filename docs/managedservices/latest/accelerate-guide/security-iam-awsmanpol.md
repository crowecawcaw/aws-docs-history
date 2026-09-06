

# AWS managed policies for AMS Accelerate
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

For a table of changes, see [Accelerate updates to AWS managed policies](#security-iam-awsmanpol-updates).

## AWS managed policy: AWSManagedServices\_AlarmManagerPermissionsBoundary
<a name="security-iam-awsmanpol-AlarmManagerPermissionsBoundary"></a>

AWS Managed Services (AMS) uses the `AWSManagedServices_AlarmManagerPermissionsBoundary` AWS managed policy. This AWS-managed policy is used in the AWSManagedServices\_AlarmManager\_ServiceRolePolicy to restrict permissions of IAM roles created by AWSServiceRoleForManagedServices\_AlarmManager.

This policy grants IAM roles created as part of [How Alarm Manager works](acc-mem-tag-alarms.md#acc-mem-how-tag-alarms-work), permissions to perform operations like AWS Config evaluation, AWS Config read to fetch Alarm Manager configuration, and creation of necessary Amazon CloudWatch alarms.

The `AWSManagedServices_AlarmManagerPermissionsBoundary` policy is attached to the `AWSServiceRoleForManagedServices_DetectiveControlsConfig` service-linked role. For updates to this role, see [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates).

You can attach this policy to your IAM identities.

**Permissions details**

This policy includes the following permissions.
+ `AWS Config` – Allows permissions to evaluate config rules and select resource configuration.
+ `AWS AppConfig` – Allows permissions to fetch AlarmManager configuration.
+ `Amazon S3` – Allows permissions to operate AlarmManager buckets and objects.
+ `Amazon CloudWatch` – Allows permissions to read and put AlarmManager managed alarms and metrics.
+ `AWS Resource Groups and Tags` – Allows permissions to read resource tags.
+ `Amazon EC2` – Allows permissions to read Amazon EC2 resources.
+ `Amazon Redshift` – Allows permissions to read Redshift instances and clusters.
+ `Amazon FSx` – Allows permissions to describe file systems, volumes and resource tags.
+ `Amazon CloudWatch Synthetics` – Allows permissions to read Synthetics resources.
+ `Amazon Elastic Kubernetes Service` – Allows permissions to describe Amazon EKS cluster.
+ `Amazon ElastiCache` – Allows permissions to describe resources.

You can download the policy file in this ZIP: [RecommendedPermissionBoundary.zip](samples/RecommendedPermissionBoundary.zip).

## AWS managed policy: AWSManagedServices\_DetectiveControlsConfig\_ServiceRolePolicy
<a name="security-iam-awsmanpol-DetectiveControlsConfig"></a>

AWS Managed Services (AMS) uses the `AWSManagedServices_DetectiveControlsConfig_ServiceRolePolicy` AWS managed policy. This AWS-managed policy is attached to the [`AWSServiceRoleForManagedServices_DetectiveControlsConfig` service-linked role](using-service-linked-roles.html#slr-deploy-detect-controls), (see [Detective controls service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-deploy-detect-controls)). For updates to the `AWSServiceRoleForManagedServices_DetectiveControlsConfig` service-linked role, see [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates).

The policy allows the service-linked role to complete actions for you.

You can attach the AWSManagedServices\_DetectiveControlsConfig\_ServiceRolePolicy policy to your IAM entities.

For more information, see [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md).

**Permissions details**

This policy has the following permissions to allow AWS Managed Services Detective Controls to deploy and configure all necessary resources.
+ `CloudFormation` – Allows AMS Detective Controls to deploy CloudFormation stacks with resources like s3 buckets, config rules and config-recorder.
+ `AWS Config` – Allows AMS Detective Controls to create AMS config rules, configure an aggregator and tag resources.
+ `Amazon S3` – allows AMS Detective Controls to manage its s3 buckets.

You can download the JSON policy file in this ZIP: [DetectiveControlsConfig\_ServiceRolePolicy.zip](samples/DetectiveControlsConfig_ServiceRolePolicy.zip).

## AWS managed policy: AWSManagedServicesDeploymentToolkitPolicy
<a name="security-iam-awsmanpol-DeploymentToolkitPolicy"></a>

AWS Managed Services (AMS) uses the `AWSManagedServicesDeploymentToolkitPolicy` AWS managed policy. This AWS-managed policy is attached to the [`AWSServiceRoleForAWSManagedServicesDeploymentToolkit` service-linked role](using-service-linked-roles.html#slr-deploy-acc), (see [Deployment toolkit service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-deploy-acc)). The policy allows the service-linked role to complete actions for you. You can't attach this policy to your IAM entities. For more information, see [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md).

For updates to the `AWSServiceRoleForManagedServicesDeploymentToolkitPolicy` service-linked role, see [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates).

**Permissions details**

This policy has the following permissions to allow AWS Managed Services Detective Controls to deploy and configure all necessary resources.
+ `CloudFormation` – Allows AMS Deployment Toolkit to deploy CFN stacks with S3 resources required by CDK.
+ `Amazon S3` – allows AMS Deployment Toolkit to manage its S3 buckets.
+ `Elastic Container Registry` – allows AMS Deployment Toolkit to manage its ECR repository that is used to deploy assets needed by AMS CDK apps.

You can download the JSON policy file in this ZIP: [AWSManagedServicesDeploymentToolkitPolicy.zip](samples/AWSManagedServices_DeploymentToolkitPolicy.zip).

## AWS managed policy: AWSManagedServices\_EventsServiceRolePolicy
<a name="EventsServiceRolePolicy"></a>

AWS Managed Services (AMS) uses the `AWSManagedServices_EventsServiceRolePolicy` AWS managed policy. This AWS-managed policy is attached to the [`AWSServiceRoleForManagedServices_Events` service-linked role](using-service-linked-roles.html#slr-evb-rule). The policy allows the service-linked role to complete actions for you. You can't attach this policy to your IAM entities. For more information, see [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md).

For updates to the `AWSServiceRoleForManagedServices_Events` service-linked role, see [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates).

**Permissions details**

This policy has the following permissions to allow Amazon EventBridge to deliver alarm state change information from your account to AWS Managed Services.
+ `events` – Allows Accelerate to create Amazon EventBridge managed rule. This rule is the infrastructure required in your AWS account to deliver alarm state change information from your account to AWS Managed Services.

You can download the JSON policy file in this ZIP: [EventsServiceRolePolicy.zip](samples/EventsServiceRolePolicy.zip).

## AWS managed policy: AWSManagedServices\_ContactsServiceRolePolicy
<a name="ContactsServiceManagedPolicy"></a>

AWS Managed Services (AMS) uses the `AWSManagedServices_ContactsServiceRolePolicy` AWS managed policy. This AWS-managed policy is attached to the [`AWSServiceRoleForManagedServices_Contacts` service-linked role](using-service-linked-roles.html#slr-contacts-service), (see [Creating a Contacts SLR for AMS Accelerate](using-service-linked-roles.md#slr-contacts-service-create)). The policy allows the AMS Contacts SLR to look at your resource tags, and their values, on AWS resources. You can't attach this policy to your IAM entities. For more information, see [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md).

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. AMS uses tags to provide you with administration services. Tags are not intended to be used for private or sensitive data.

For updates to the `AWSServiceRoleForManagedServices_Contacts` service-linked role, see [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates).

**Permissions details**

This policy has the following permissions to allow the Contacts SLR to read your resource tags to retrieve resource contact information that you have set up ahead of time.
+ `IAM` – Allows Contacts service to look at tags on IAM Roles and IAM users.
+ `Amazon EC2` – Allows Contacts service to look at tags on Amazon EC2 resources.
+ `Amazon S3` – Allows Contacts Service to look at tags on Amazon S3 buckets. This action uses a Condition to ensure AMS accesses your bucket tags using the HTTP Authorization header, using the SigV4 signature protocol, and using HTTPS with TLS 1.2 or greater. For more information, see [Authentication Methods](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html#auth-methods-intro) and [Amazon S3 Signature Version 4 Authentication Specific Policy Keys](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html).
+ `Tag` – Allows Contacts service to look at tags on other AWS resources.
+ "iam:ListRoleTags", "iam:ListUserTags", "tag:GetResources", "tag:GetTagKeys", "tag:GetTagValues", "ec2:DescribeTags", "s3:GetBucketTagging"

You can download the JSON policy file in this ZIP: [ContactsServicePolicy.zip](samples/ContactsServicePolicy.zip).

## Accelerate updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Accelerate since this service began tracking these changes. 


| Change | Description | Date | 
| --- | --- | --- | 
| Updated policy – [Deployment Toolkit](#security-iam-awsmanpol-DeploymentToolkitPolicy) | + These new permissions were added for resource `arn:aws:ecr:*:*:repository/ams-cdktoolkit*`: <pre>ecr:BatchGetRepositoryScanningConfiguration<br />ecr:PutImageScanningConfiguration</pre> | April 4, 2024 | 
| Updated policy – [Deployment Toolkit](#security-iam-awsmanpol-DeploymentToolkitPolicy) | + These new permissions were added for resource `arn:aws:cloudformation:*:*:stack/ams-cdk-toolkit*`: <pre>cloudformation:DeleteChangeSet<br /><br />cloudformation:DescribeStackEvents<br />cloudformation:GetTemplate<br />cloudformation:TagResource<br />cloudformation:UntagResource</pre><br />+ These new permissions were added for resource `arn:aws:ecr:*:*:repository/ams-cdktoolkit*`: <pre>ecr:CreateRepository<br /><br />ecr:DeleteLifecyclePolicy<br />ecr:DeleteRepository<br />ecr:DeleteRepositoryPolicy<br />ecr:DescribeRepositories<br />ecr:GetLifecyclePolicy<br />ecr:ListTagsForResource<br />ecr:PutImageTagMutability<br />ecr:PutLifecyclePolicy<br />ecr:SetRepositoryPolicy<br />ecr:TagResource<br />ecr:UntagResource</pre><br />+ Also, some existing actions with wildcard were scoped down to individual actions: <pre>- s3:DeleteObject*<br /><br />+ s3:DeleteObject<br />+ s3:DeleteObjectTagging<br />+ s3:DeleteObjectVersion<br />+ s3:DeleteObjectVersionTagging<br /><br />- s3:GetObject*<br />+ s3:GetObject<br />+ s3:GetObjectAcl<br />+ s3:GetObjectAttributes<br />+ s3:GetObjectLegalHold<br />+ s3:GetObjectRetention<br />+ s3:GetObjectTagging<br />+ s3:GetObjectVersion<br />+ s3:GetObjectVersionAcl<br />+ s3:GetObjectVersionAttributes<br />+ s3:GetObjectVersionForReplication<br />+ s3:GetObjectVersionTagging<br />+ s3:GetObjectVersionTorrent<br /><br />- cloudformation:UpdateTermination*<br />+ cloudformation:UpdateTerminationProtection</pre> | May 9, 2023 | 
| Updated policy – [Detective Controls](#security-iam-awsmanpol-DetectiveControlsConfig) | + The CloudFormation actions have been scoped down further after confirmation with security and access team<br />+ The Lambda actions have been removed from the policy as they don’t impact onboarding/off boarding | April 10, 2023 | 
| Updated policy – [Detective Controls](#security-iam-awsmanpol-DetectiveControlsConfig) | The `ListAttachedRolePolicies` action is removed from the policy. The action had Resource as wildcard (\*). As "list" is a non-mutative action, it is given access over all resources, and the wildcard is disallowed. | March 28, 2023 | 
| Updated policy – [Detective Controls](#security-iam-awsmanpol-DetectiveControlsConfig) | Updated the policy and added the permissions boundary policy. | March 21, 2023 | 
| New policy – [Contacts Service](#ContactsServiceManagedPolicy) | Accelerate added a new policy to look at your account contact information from your resource tags.<br />Accelerate added a new policy to read your resource tags so that it can retrieve the resource contact information that you have set up ahead of time. | February 16, 2023 | 
| New policy – [Events Service](#EventsServiceRolePolicy) | Accelerate added a new policy to deliver alarm state change information from your account to AWS Managed Services.<br />Grants IAM roles created as part of [How Alarm Manager works](acc-mem-tag-alarms.md#acc-mem-how-tag-alarms-work) permissions to create a required Amazon EventBridge managed rule. | February 07, 2023 | 
| Updated policy – [Deployment Toolkit](#security-iam-awsmanpol-DeploymentToolkitPolicy) | Added S3 permissions to support customer offboarding from Accelerate. | January 30, 2023 | 
| New policy – [Detective Controls](#security-iam-awsmanpol-DetectiveControlsConfig)  | Allows the service-linked role, [Detective controls service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-deploy-detect-controls), to complete actions for you to deploy Accelerate detective controls. | December 19, 2022 | 
| New policy – [Alarm Manager](#security-iam-awsmanpol-AlarmManagerPermissionsBoundary)  | Accelerate added a new policy to allow permissions to perform alarm manager tasks.<br />Grants IAM roles created as part of [How Alarm Manager works](acc-mem-tag-alarms.md#acc-mem-how-tag-alarms-work) permissions to perform operations like AWS Config evaluation, AWS Config read to fetch alarm manager configuration, creation of necessary Amazon CloudWatch alarms. | November 30, 2022 | 
| Accelerate started tracking changes | Accelerate started tracking changes for its AWS managed policies. | November 30, 2022 | 
| New policy – [Deployment Toolkit](#security-iam-awsmanpol-DeploymentToolkitPolicy) | Accelerate added this policy for deployment tasks.<br />Grants the service-linked role [AWSServiceRoleForAWSManagedServicesDeploymentToolkit](using-service-linked-roles.md#slr-deploy-acc) permissions to access and update deployment-related Amazon S3 buckets and CloudFormation stacks. | June 09, 2022 | 