# IAM permissions and

execution roles

To use the The Amazon SageMaker Python SDK requires permissions to interact with AWS services.
The following policies are required for full Feature Processor functionality. You can attach
the [AmazonSageMakerFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") and [AmazonEventBridgeSchedulerFullAccess](../../../scheduler/latest/UserGuide/security_iam_id-based-policy-examples.md#security_iam_id-based-policies-managed-policies "../../../scheduler/latest/UserGuide/security_iam_id-based-policy-examples.md#security_iam_id-based-policies-managed-policies") AWS Managed Policies attached to your
IAM role. For information on attaching policies to your IAM role, see [Adding policies to your IAM role](feature-store-adding-policies.md "feature-store-adding-policies.md").
See the following examples for details.

The trust policy of the role to which this policy is applied must allow the
"scheduler.amazonaws.com", "sagemaker.amazonaws.com", and "glue.amazonaws.com"
principles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "scheduler.amazonaws.com",
 "sagemaker.amazonaws.com",
 "glue.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
