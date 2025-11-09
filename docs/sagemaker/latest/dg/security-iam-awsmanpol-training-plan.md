# AWS managed policies for

SageMaker training plans

This AWS managed policy grants permissions needed to create and manage
Amazon SageMaker training plans and Reserved Capacity in SageMaker AI. The policy can be attached to IAM
roles used for creating and managing training plans and reserved capacity within SageMaker AI
including your [SageMaker AI execution role](sagemaker-roles.md "sagemaker-roles.md").

###### Topics

- [AWS
  managed policy: AmazonSageMakerTrainingPlanCreateAccess](#security-iam-awsmanpol-AmazonSageMakerTrainingPlanCreateAccess "#security-iam-awsmanpol-AmazonSageMakerTrainingPlanCreateAccess")
- [Amazon SageMaker AI updates to
  SageMaker training plans managed policies](#security-iam-awsmanpol-training-plan-updates "#security-iam-awsmanpol-training-plan-updates")

## AWS

managed policy: AmazonSageMakerTrainingPlanCreateAccess

This policy provides the necessary permissions to create, describe, search for, and
list training plans in SageMaker AI. Additionally, it also allows adding tags to training plans
and reserved capacity resources under specific conditions.

**Permissions details**

This policy includes the following permissions.

- `sagemaker` – Create training plans and reserved capacity,
  permits adding tags to training plans and reserved capacity when the tagging
  action is specifically `CreateTrainingPlan` or
  `CreateReservedCapacity`, allows describing training plans,
  permits searching for training plan offerings and listing existing training
  plans on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateTrainingPlanPermissions",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingPlan",
 "sagemaker:CreateReservedCapacity",
 "sagemaker:DescribeReservedCapacity"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:training-plan/*",
 "arn:aws:sagemaker:*:*:reserved-capacity/*"
 ]
 },
 {
 "Sid": "AggTagsToTrainingPlanPermissions",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:training-plan/*",
 "arn:aws:sagemaker:*:*:reserved-capacity/*"
 ],
 "Condition": {
 "StringEquals": {
 "sagemaker:TaggingAction": ["CreateTrainingPlan","CreateReservedCapacity"]
 }
 }
 },
 {
 "Sid": "DescribeTrainingPlanPermissions",
 "Effect": "Allow",
 "Action": "sagemaker:DescribeTrainingPlan",
 "Resource": [
 "arn:aws:sagemaker:*:*:training-plan/*"
 ]
 },
 {
 "Sid": "NonResourceLevelTrainingPlanPermissions",
 "Effect": "Allow",
 "Action": [
 "sagemaker:SearchTrainingPlanOfferings",
 "sagemaker:ListTrainingPlans"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ListUltraServersByReservedCapacityPermissions",
 "Effect": "Allow",
 "Action": "sagemaker:ListUltraServersByReservedCapacity",
 "Resource": [
 "arn:aws:sagemaker:*:*:reserved-capacity/*"
 ]
 }
 ]
}`

```

## Amazon SageMaker AI updates to

SageMaker training plans managed policies

View details about updates to AWS managed policies for Amazon SageMaker AI since this service
began tracking these changes.

| Policy                                                      | Version | Change                                                                                                                                            | Date             |
| ----------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AmazonSageMakerTrainingPlanCreateAccess<br>• updated policy | 2       | Updated policy to add permissions to retrieve information about a<br>specific reserved capacity and list all UltraServers in a reserved capacity. | July 29, 2024    |
| AmazonSageMakerTrainingPlanCreateAccess<br>• New<br>policy  | 1       | Initial policy                                                                                                                                    | December 4, 2024 |
