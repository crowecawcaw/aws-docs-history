# AWS managed policies for Deadline Cloud

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed 
 to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because 
 they're available for all AWS customers to use. We recommend that you reduce permissions further by defining 
 [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS 
 managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is 
 most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
 existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the 
 *IAM User Guide*.


## AWS managed policy:
 AWSDeadlineCloud-FleetWorker


You can attach the `AWSDeadlineCloud-FleetWorker` policy to your AWS Identity and Access Management
 (IAM) identities.


This policy grants workers in this fleet the permissions that are needed to connect to and
 receive tasks from the service.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows principals to manage workers in a fleet.

For a JSON listing of the policy details, see [AWSDeadlineCloud-FleetWorker](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-FleetWorker.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-FleetWorker.html") in the *AWS Managed Policy reference
 guide*.


## AWS managed policy:
 AWSDeadlineCloud-WorkerHost


You can attach the `AWSDeadlineCloud-WorkerHost` policy to your IAM
 identities.



This policy grants the permissions that are needed to initially connect to the service. It
 can be used as an Amazon Elastic Compute Cloud (Amazon EC2) instance profile.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows the user to create workers, assume the fleet
 role for workers, and apply tags to workers

For a JSON listing of the policy details, see [AWSDeadlineCloud-WorkerHost](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-WorkerHost.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-WorkerHost.html") in the *AWS Managed Policy reference
 guide*.


## AWS managed policy:
 AWSDeadlineCloud-UserAccessFarms


You can attach the `AWSDeadlineCloud-UserAccessFarms` policy to your IAM
 identities.


This policy allows users to access farm data based on the farms that they are members of
 and their membership level.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows the user to access farm data.
* `ec2` – Allows users to see details about Amazon EC2 instance types.
* `identitystore` – Allows users to see user and group names.

For a JSON listing of the policy details, see [AWSDeadlineCloud-UserAccessFarms](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFarms.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFarms.html") in the *AWS Managed Policy reference
 guide*.


## AWS managed policy:
 AWSDeadlineCloud-UserAccessFleets


You can attach the `AWSDeadlineCloud-UserAccessFleets` policy to your IAM
 identities.


This policy allows users to access fleet data based on the farms that they are members of
 and their membership level.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows the user to access farm data.
* `ec2` – Allows users to see details about Amazon EC2 instance types.
* `identitystore` – Allows users to see user and group names.

For a JSON listing of the policy details, see [AWSDeadlineCloud-UserAccessFleets](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFleets.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFleets.html") in the *AWS Managed Policy reference
 guide*.


## AWS managed policy:
 AWSDeadlineCloud-UserAccessJobs


You can attach the `AWSDeadlineCloud-UserAccessJobs` policy to your IAM
 identities.


This policy allows users to access job data based on the farms that they are members of
 and their membership level.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows the user to access farm data.
* `ec2` – Allows users to see details about Amazon EC2 instance types.
* `identitystore` – Allows users to see user and group names.

For a JSON listing of the policy details, see [AWSDeadlineCloud-UserAccessJobs](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessJobs.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessJobs.html") in the *AWS Managed Policy reference
 guide*.


## AWS managed policy:
 AWSDeadlineCloud-UserAccessQueues


You can attach the `AWSDeadlineCloud-UserAccessQueues` policy to your IAM
 identities.


This policy allows users to access queue data based on the farms that they are members of
 and their membership level.


**Permissions details**


This policy includes the following permissions:



* `deadline` – Allows the user to access farm data.
* `ec2` – Allows users to see details about Amazon EC2 instance types.
* `identitystore` – Allows users to see user and group names.

For a JSON listing of the policy details, see [AWSDeadlineCloud-UserAccessQueues](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessQueues.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessQueues.html") in the *AWS Managed Policy reference
 guide*.



## Deadline Cloud updates to AWS managed
 policies



View details about updates to AWS managed policies for Deadline Cloud since this service
 began tracking these changes. For automatic alerts about changes to this page, subscribe to
 the
 RSS feed on the Deadline Cloud Document history page.





| Change | Description | Date |
| --- | --- | --- |
| [AWSDeadlineCloud-WorkerHost](#security-iam-awsmanpol-WorkerHost "#security-iam-awsmanpol-WorkerHost") – Change | Deadline Cloud added new actions `deadline:TagResource` and
 `deadline:ListTagsForResource` to allow you to add and view tags
 associated with workers in your fleet. | May 30, 2025 |
| [AWSDeadlineCloud-UserAccessFarms](#security-iam-awsmanpol-UserAccessFarms "#security-iam-awsmanpol-UserAccessFarms") – Change[AWSDeadlineCloud-UserAccessJobs](#security-iam-awsmanpol-UserAccessJobs "#security-iam-awsmanpol-UserAccessJobs") – Change[AWSDeadlineCloud-UserAccessQueues](#security-iam-awsmanpol-UserAccessQueues "#security-iam-awsmanpol-UserAccessQueues") – Change | Deadline Cloud added new actions `deadline:GetJobTemplate` and
 `deadline:ListJobParameterDefinitions` to allow you to resubmit
 jobs. | October 7, 2024 |
| Deadline Cloud started tracking changes | Deadline Cloud started tracking changes to its AWS managed policies. | April 2, 2024 |
