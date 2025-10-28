# Multi-container endpoints

SageMaker AI multi-container endpoints enable customers to deploy multiple containers,
that use different models or frameworks, on a single SageMaker AI endpoint. The containers
can be run in a sequence as an inference
pipeline, or each container can be accessed individually by using direct invocation to
improve endpoint utilization and optimize costs.

For information about invoking the containers in a multi-container endpoint in sequence, see [Inference pipelines in Amazon SageMaker AI](inference-pipelines.md "inference-pipelines.md").

For information about invoking a specific container in a multi-container endpoint, see
[Invoke a multi-container endpoint with direct
invocation](multi-container-direct.md "multi-container-direct.md")

###### Topics

- [Create a multi-container endpoint (Boto 3)](multi-container-create.md "multi-container-create.md")
- [Update a multi-container endpoint](multi-container-update.md "multi-container-update.md")
- [Invoke a multi-container endpoint with direct
  invocation](multi-container-direct.md "multi-container-direct.md")
- [Security with multi-container endpoints with direct
  invocation](multi-container-security.md "multi-container-security.md")
- [Metrics for multi-container endpoints with
  direct invocation](multi-container-metrics.md "multi-container-metrics.md")
- [Autoscale multi-container
  endpoints](multi-container-auto-scaling.md "multi-container-auto-scaling.md")
- [Troubleshoot multi-container
  endpoints](multi-container-troubleshooting.md "multi-container-troubleshooting.md")
  The following policy allows `invoke_endpoint` requests only when the value of
  the `TargetContainerHostname` field matches one of the specified regular
  expressions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sagemaker:InvokeEndpoint"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:endpoint/`endpoint_name`",
 "Condition": {
 "StringLike": {
 "sagemaker:TargetModel": [
 "customIps*",
 "common*"
 ]
 }
 }
 }
 ]
}`

```

The following policy denies `invoke_endpoint` requests when the value of the
`TargetContainerHostname` field matches one of the specified regular
expressions in the `Deny` statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sagemaker:InvokeEndpoint"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:endpoint/`endpoint_name`",
 "Condition": {
 "StringLike": {
 "sagemaker:TargetModel": [
 "`model_name`*"
 ]
 }
 }
 },
 {
 "Action": [
 "sagemaker:InvokeEndpoint"
 ],
 "Effect": "Deny",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:endpoint/`endpoint_name`",
 "Condition": {
 "StringLike": {
 "sagemaker:TargetModel": [
 "special-`model_name`*"
 ]
 }
 }
 }
 ]
}`

```

For information about SageMaker AI condition keys, see [Condition Keys for SageMaker AI](../../../IAM/latest/UserGuide/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../IAM/latest/UserGuide/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the _AWS Identity and Access Management User
Guide_.
