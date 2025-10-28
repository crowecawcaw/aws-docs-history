# Auto scaling prerequisites

Before you can use auto scaling, you must have already created an Amazon SageMaker AI model
endpoint. You can have multiple model versions for the same endpoint. Each model is
referred to as a [production (model) variant](model-ab-testing.md "model-ab-testing.md"). For
more information about deploying a model endpoint, see [Deploy the Model to SageMaker AI Hosting Services](ex1-model-deployment.md#ex1-deploy-model "ex1-model-deployment.md#ex1-deploy-model").

To activate auto scaling for a model, you can use the SageMaker AI console, the AWS Command Line Interface
(AWS CLI), or an AWS SDK through the Application Auto Scaling API.

- If this is your first time configuring scaling for a model, we recommend you
  [Configure model auto scaling with
  the console](endpoint-auto-scaling-add-console.md "endpoint-auto-scaling-add-console.md").
- When using the AWS CLI or the Application Auto Scaling API, the flow is to register the model as
  a scalable target, define the scaling policy, and then apply it. On the SageMaker AI
  console, under **Inference** in the navigation pane, choose
  **Endpoints**. Find your model's endpoint name and then
  choose it to find the variant name. You must specify both the endpoint name and
  the variant name to activate auto scaling for a model.
  Auto scaling is made possible by a combination of the Amazon SageMaker AI, Amazon CloudWatch, and Application Auto Scaling
  APIs. For information about the minimum required permissions, see [Application Auto Scaling identity-based policy examples](../../../autoscaling/application/userguide/security_iam_id-based-policy-examples.md "../../../autoscaling/application/userguide/security_iam_id-based-policy-examples.md") in the
  _Application Auto Scaling User Guide_.

The `SagemakerFullAccessPolicy` IAM policy has all the IAM permissions
required to perform auto scaling. For more information about SageMaker AI IAM permissions, see
[How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

If you manage your own permission policy, you must include the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:UpdateEndpointWeightsAndCapacities"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/sagemaker.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_SageMakerEndpoint",
 "Condition": {
 "StringLike": { "iam:AWSServiceName": "sagemaker.application-autoscaling.amazonaws.com" }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DeleteAlarms"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Service-linked role

Auto scaling uses the
`AWSServiceRoleForApplicationAutoScaling_SageMakerEndpoint`
service-linked role. This service-linked role grants Application Auto Scaling permission to describe
the alarms for your policies, to monitor current capacity levels, and to scale the
target resource. This role is created for you automatically. For automatic role
creation to succeed, you must have permission for the
`iam:CreateServiceLinkedRole` action. For more information, see
[Service-linked roles](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md") in the
_Application Auto Scaling User Guide_.
