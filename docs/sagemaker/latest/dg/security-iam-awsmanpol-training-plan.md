

# AWS managed policies for SageMaker training plans
<a name="security-iam-awsmanpol-training-plan"></a>

 This AWS managed policy grants permissions needed to create and manage Amazon SageMaker training plans and Reserved Capacity in SageMaker AI. The policy can be attached to IAM roles used for creating and managing training plans and reserved capacity within SageMaker AI including your [SageMaker AI execution role](sagemaker-roles.md).

**Topics**
+ [AWS managed policy: AmazonSageMakerTrainingPlanCreateAccess](#security-iam-awsmanpol-AmazonSageMakerTrainingPlanCreateAccess)
+ [AWS managed policy: AmazonSageMakerCapacityReservationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerCapacityReservationServiceRolePolicy)
+ [Amazon SageMaker AI updates to SageMaker training plans managed policies](#security-iam-awsmanpol-training-plan-updates)

## AWS managed policy: AmazonSageMakerTrainingPlanCreateAccess
<a name="security-iam-awsmanpol-AmazonSageMakerTrainingPlanCreateAccess"></a>

This policy provides the necessary permissions to create, describe, search for, and list training plans in SageMaker AI. Additionally, it also allows adding tags to training plans and reserved capacity resources under specific conditions.

**Permissions details**

This policy includes the following permissions.
+ `sagemaker` – Create training plans and reserved capacity, permits adding tags to training plans and reserved capacity when the tagging action is specifically `CreateTrainingPlan` or `CreateReservedCapacity`, allows describing training plans, permits searching for training plan offerings and listing existing training plans on all resources.

------
#### [ JSON ]

****  

```
{
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
}
```

------

## AWS managed policy: AmazonSageMakerCapacityReservationServiceRolePolicy
<a name="security-iam-awsmanpol-AmazonSageMakerCapacityReservationServiceRolePolicy"></a>

This policy is used by the service-linked role named AWSServiceRoleForSageMakerCapacityReservation to publish CloudWatch metrics for Reserved Capacity utilization into customer accounts. The service-linked role is created by the service principal capacityreservation.sagemaker.amazonaws.com.

**Note**  
This is a service-linked role policy. You cannot attach this policy to your IAM identities. SageMaker AI creates this policy and attaches it to a service-linked role that allows SageMaker AI to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.
+ `cloudwatch` – Allows publishing metric data to CloudWatch. This permission is scoped to the `aws/sagemaker/CapacityReservations` namespace using a condition key.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CloudwatchPutMetricDataAccess",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "aws/sagemaker/CapacityReservations"
                }
            }
        }
    ]
}
```

For more information, see [AmazonSageMakerCapacityReservationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerCapacityReservationServiceRolePolicy.html) in the AWS Managed Policy Reference Guide.

## Amazon SageMaker AI updates to SageMaker training plans managed policies
<a name="security-iam-awsmanpol-training-plan-updates"></a>

View details about updates to AWS managed policies for Amazon SageMaker AI since this service began tracking these changes.


| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerCapacityReservationServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerCapacityReservationServiceRolePolicy) – New policy | 1 | Initial policy | March 5, 2026 | 
| AmazonSageMakerTrainingPlanCreateAccess - updated policy | 2 | Updated policy to add permissions to retrieve information about a specific reserved capacity and list all UltraServers in a reserved capacity. | July 29, 2024 | 
| AmazonSageMakerTrainingPlanCreateAccess - New policy | 1 | Initial policy | December 4, 2024 | 