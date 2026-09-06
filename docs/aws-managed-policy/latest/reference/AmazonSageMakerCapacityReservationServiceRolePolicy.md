

# AmazonSageMakerCapacityReservationServiceRolePolicy
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy"></a>

**Description**: This policy grants permissions to Amazon SageMaker Capacity Reservations to publish CloudWatch metrics into customer accounts for utilization visibility.

`AmazonSageMakerCapacityReservationServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: April 08, 2026, 20:27 UTC 
+ **Edited time:** April 08, 2026, 20:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AmazonSageMakerCapacityReservationServiceRolePolicy`

## Policy version
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CloudwatchPutMetricDataAccess",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:PutMetricData"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "cloudwatch:namespace" : "aws/sagemaker/CapacityReservations"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerCapacityReservationServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)