

# Prerequisites
<a name="training-sessions-prereqs"></a>

The training session APIs extend serverless model customization with the SageMaker AI `CreateTrainingSession` API and a set of runtime operations that run training and sampling against an active session. Before you create your first session, configure three things: the IAM identity that calls the API (the *caller identity*), the IAM execution role that the session assumes (the `RoleArn` you pass to `CreateTrainingSession`), and a model package group for your checkpoints.

## Managed policies
<a name="training-sessions-prereqs-managed-policies"></a>

The training session APIs provide two AWS managed policies. Attach each to the appropriate identity before you create a session. For the full permission lists, see [AWS managed policies for SageMaker AI training session APIs](training-sessions-security-iam-awsmanpol.md).
+ **AmazonSageMakerTrainingSessionAccess** – attach to the IAM users and roles that create and interact with training sessions. It grants control-plane actions (create, describe, stop, delete, list), the runtime operations that run training and sampling, model package management for checkpoint publication, `iam:PassRole` to hand the execution role to the service, and the AWS KMS permissions needed to use a customer managed key through SageMaker AI.
+ **AmazonSageMakerTrainingSessionFullAccess** – attach to the IAM role you pass as the session execution role. It grants the session the permissions it needs while running: read and write access to your training data and checkpoints in Amazon S3, AWS KMS permissions for Amazon S3-side encryption, access to SageMaker AI hub content and model packages, and Amazon EC2 network interface management for sessions that run in Amazon VPC mode.

## Pass the execution role
<a name="training-sessions-prereqs-passrole"></a>

Allow the caller identity to pass the execution role to the Training Sessions service principal. The `AmazonSageMakerTrainingSessionAccess` managed policy already includes this permission, scoped to roles under the `service-role` path whose names contain `SageMaker`. If you use a custom caller policy, include the following statement:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PassExecutionRolePermissions",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::*:role/service-role/*SageMaker*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "training-session.sagemaker.amazonaws.com"
        }
      }
    }
  ]
}
```

## Execution role trust policy
<a name="training-sessions-prereqs-trust-policy"></a>

Add the Training Sessions service principal to the trust policy of your execution role so that the service can assume it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "training-session.sagemaker.amazonaws.com"
      },
      "Action": ["sts:AssumeRole", "sts:TagSession"]
    }
  ]
}
```

## Create a model package group
<a name="training-sessions-prereqs-model-package-group"></a>

The service registers each checkpoint you save as a model package in a SageMaker AI model package group. Create a group for your checkpoints and pass its ARN as `model_package_group_arn` when you create the `ServiceClient`:

```
aws sagemaker create-model-package-group \
    --model-package-group-name {{my-training-session-checkpoints}} \
    --region {{us-west-2}}
```

For more information, see [Create a Model Group](model-registry-model-group.md).

## Other setup
<a name="training-sessions-prereqs-other-setup"></a>
+ If you run sessions inside a customer-managed Amazon VPC, see [Configure a VPC for SageMaker AI training sessions](training-sessions-vpc.md).
+ If you use a customer managed KMS key to encrypt session data, the caller identity, execution role, and key policy need additional permissions. See [Encryption at rest for SageMaker AI Training Sessions](training-sessions-encryption-at-rest.md).