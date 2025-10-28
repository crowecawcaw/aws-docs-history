# Cross-service confused deputy

prevention

The [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") is a security issue where an entity that doesn't have permission to perform an
action can coerce a more-privileged entity to perform the action. In AWS, the confused deputy
problem can arise due to cross-service impersonation. Cross-service impersonation can occur when
one service (the _calling service_) invokes another service (the
_called service_) and leverages the called service's elevated permissions to
act on resources the calling service has no authorization to access. To prevent unauthorized access
through the confused deputy problem, AWS provides tools to help secure your data across services.
These tools help you control the permissions granted to service principals,
limiting their access to only the resources in your account that are required.
By carefully managing the access privileges of service principals, you can help mitigate the risk of
services improperly accessing data or resources to which they should not have permissions.

Read on for general guidance or navigate to an example for a specific SageMaker AI feature:

###### Topics

- [Limit Permissions With Global
  Condition Keys](#security-confused-deputy-context-keys "#security-confused-deputy-context-keys")
- [SageMaker Edge Manager](#security-confused-deputy-edge-manager "#security-confused-deputy-edge-manager")
- [SageMaker Images](#security-confused-deputy-images "#security-confused-deputy-images")
- [SageMaker AI Inference](#security-confused-deputy-inference "#security-confused-deputy-inference")
- [SageMaker AI Batch Transform Jobs](#security-confused-deputy-batch "#security-confused-deputy-batch")
- [SageMaker AI Marketplace](#security-confused-deputy-marketplace "#security-confused-deputy-marketplace")
- [SageMaker Neo](#security-confused-deputy-neo "#security-confused-deputy-neo")
- [SageMaker Pipelines](#security-confused-deputy-pipelines "#security-confused-deputy-pipelines")
- [SageMaker Processing Jobs](#security-confused-deputy-processing-job "#security-confused-deputy-processing-job")
- [SageMaker Studio](#security-confused-deputy-studio "#security-confused-deputy-studio")
- [SageMaker Training Jobs](#security-confused-deputy-training-job "#security-confused-deputy-training-job")

## Limit Permissions With Global

Condition Keys

We recommend using the `aws:SourceArn` and `aws:SourceAccount` global condition keys in resource policies to limit the
permissions to the resource that Amazon SageMaker AI gives another service. If you use both global
condition keys and the `aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the `aws:SourceArn` value
must use the same account ID when used in the same policy statement. Use
`aws:SourceArn` if you want only one resource to be associated with the
cross-service access. Use `aws:SourceAccount` if you want to allow any resource in
that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition key with the full ARN of the resource. If you
don't know the full ARN of the resource or if you are specifying multiple resources, use the
`aws:SourceArn` global condition key with wildcards (`*`) for the
unknown portions of the ARN. For example,
`arn:aws:sagemaker:*:`123456789012`:*`.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition keys in SageMaker AI to prevent the confused deputy
problem.

```
{
  "Version": "2012-10-17",
  "Statement": {
    "Sid": "ConfusedDeputyPreventionExamplePolicy",
    "Effect": "Allow",
    "Principal": {
      "Service": "sagemaker.amazonaws.com"
    },
    # Specify an action and resource policy for another service
    "Action": "`service`:`ActionName`",
    "Resource": [
      "arn:aws:`service`:::`ResourceName`/*"
    ],
    "Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:`partition`:sagemaker:`region`:`123456789012`:*"
      },
      "StringEquals": {
        "aws:SourceAccount": "`123456789012`"
      }
    }
  }
}
```

## SageMaker Edge Manager

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker Edge Manager
created by account number `123456789012` in the
`us-west-2` Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": { "Service": "sagemaker.amazonaws.com" },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:*"
 }
 }
 }
}`

```

You can replace the `aws:SourceArn` in this template with the full ARN of one
specific packaging job to further limit permissions.

## SageMaker Images

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for [SageMaker Images](studio-byoi.md "studio-byoi.md"). Use
this template with either `Image` or `ImageVersion`. This example uses an `ImageVersion` record ARN
with the account number `123456789012`. Note that because
the account number is part of the `aws:SourceArn` value, you do not need to specify
an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-east-2`:`123456789012`:`image-version`/*"
 }
 }
 }
}`

```

Do not replace the `aws:SourceArn` in this template with the full ARN of a
specific image or image version. The ARN must be in the format provided above and specify
either `image` or `image-version`. The `partition`
placeholder should designate either an AWS commercial partition (`aws`) or an
AWS in China partition (`aws-cn`), depending on where the image or image version
is running. Similarly, the `region` placeholder in the ARN can be any [valid Region](regions-quotas.md "regions-quotas.md")
where SageMaker images are available.

## SageMaker AI Inference

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker AI [real-time](realtime-endpoints.md "realtime-endpoints.md"), [serverless](serverless-endpoints.md "serverless-endpoints.md"), and
[asynchronous](async-inference.md "async-inference.md")
inference. Note that because the account number is part of the `aws:SourceArn`
value, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": { "Service": "sagemaker.amazonaws.com" },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:*"
 }
 }
 }
}`

```

Do not replace the `aws:SourceArn` in this template with the full ARN of a
specific model or endpoint. The ARN must be in the format provided above. The asterisk in the
ARN template does not stand for wildcard and should not be changed.

## SageMaker AI Batch Transform Jobs

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker AI [batch transform
jobs](batch-transform.md "batch-transform.md") created by account number `123456789012` in
the `us-west-2` Region. Note that because the account number is in
the ARN, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:transform-job/*"
 }
 }
 }
 ]
}`

```

You can replace the `aws:SourceArn` in this template with the full ARN of one
specific batch transform job to further limit permissions.

## SageMaker AI Marketplace

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker AI Marketplace
resources created by account number `123456789012` in the
`us-west-2` Region. Note that because the account number is in the
ARN, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

Do not replace the `aws:SourceArn` in this template with the full ARN of a
specific algorithm or model package. The ARN must be in the format provided above. The
asterisk in the ARN template does stand for wildcard and covers all training jobs, models, and
batch transform jobs from validation steps, as well as algorithm and model packages published
to SageMaker AI Marketplace.

## SageMaker Neo

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker Neo compilation
jobs created by account number `123456789012` in the
`us-west-2` Region. Note that because the account number is in the
ARN, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:`compilation-job/*`"
 }
 }
 }
 ]
}`

```

You can replace the `aws:SourceArn` in this template with the full ARN of one
specific compilation job to further limit permissions.

## SageMaker Pipelines

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for [SageMaker Pipelines](pipelines-overview.md "pipelines-overview.md")
using pipeline execution records from one or more pipelines. Note that because the account
number is in the ARN, you do not need to specify an `aws:SourceAccount`
value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-east-1`:`123456789012`:pipeline/`mypipeline/*`"
 }
 }
 }
 ]
}`

```

Do not replace the `aws:SourceArn` in this template with the full ARN of a
specific pipeline execution. The ARN must be in the format provided above. The
`partition` placeholder should designate either an AWS commercial partition
(`aws`) or an AWS in China partition (`aws-cn`), depending on where
the pipeline is running. Similarly, the `region` placeholder in the ARN can be any
[valid
Region](regions-quotas.md "regions-quotas.md") where SageMaker Pipelines is available.

The asterisk in the ARN template does stand for wildcard and covers all pipeline
executions of a pipeline named `mypipeline`. If you want to allow the
`AssumeRole` permissions for all pipelines in account `123456789012`
rather than one specific pipeline, then the `aws:SourceArn` would be
`arn:aws:sagemaker:*:123456789012:pipeline/*`.

## SageMaker Processing Jobs

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker Processing jobs
created by account number `123456789012` in the
`us-west-2` Region. Note that because the account number is in the
ARN, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:`processing-job/*`"
 }
 }
 }
 ]
}`

```

You can replace the `aws:SourceArn` in this template with the full ARN of one
specific processing job to further limit permissions.

## SageMaker Studio

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker Studio created by
account number `123456789012` in the
`us-west-2` Region. Note that because the account number is part of
the `aws:SourceArn` value, you do not need to specify an
`aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

Do not replace the `aws:SourceArn` in this template with the full ARN of a
specific Studio application, user profile, or domain. The ARN must be in the format provided
in the previous example. The asterisk in the ARN template does not stand for wildcard and
should not be changed.

## SageMaker Training Jobs

The following example shows how you can use the `aws:SourceArn` global
condition key to prevent the cross-service confused deputy problem for SageMaker training jobs
created by account number `123456789012` in the
`us-west-2` Region. Note that because the account number is in the
ARN, you do not need to specify an `aws:SourceAccount` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sagemaker:`us-west-2`:`123456789012`:`training-job/*`"
 }
 }
 }
 ]
}`

```

You can replace the `aws:SourceArn` in this template with the full ARN of one
specific training job to further limit permissions.

###### Next Up

For more information on managing execution roles, see [SageMaker AI Roles](sagemaker-roles.md "sagemaker-roles.md").
