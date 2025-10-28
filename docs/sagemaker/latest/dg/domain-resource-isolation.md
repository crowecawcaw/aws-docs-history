# Isolate domain resources

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

You can isolate resources between each of the domains in your account and AWS Region
using an AWS Identity and Access Management (IAM) policy. The isolated resources will no longer be accessed from
other domains. In this topic we will discuss the conditions required for the IAM
policy and how to apply them.

The resources that can be isolated by this policy are the resource types that have
condition keys containing `aws:ResourceTag/${TagKey}` or
`sagemaker:ResourceTag/${TagKey}`. For a reference on the SageMaker AI resources and
associated condition keys, see [Actions,
resources, and condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md").

###### Warning

The resource types that _do not_ contain the above
condition keys (and therefore the [Actions](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions") that use the resource types) are _not_ impacted by this resource isolation policy. For example, the [pipeline-execution](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-pipeline-execution "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-pipeline-execution") resource type does _not_ contain the above condition keys and is _not_ impacted by this policy. Therefore, the following are a few actions,
with the pipeline-execution resource type, are _not_
supported for resource isolation:

- DescribePipelineExecution
- StopPipelineExecution
- UpdatePipelineExecution
- RetryPipelineExecution
- DescribePipelineDefinitionForExecution
- ListPipelineExecutionSteps
- SendPipelineExecutionStepSuccess
- SendPipelineExecutionStepFailure
  The following topic shows how to create a new IAM policy that limits access to resources
  in the domain to user profiles with the domain tag, as well as how to attach this policy to
  the IAM execution role of the domain. You must repeat this process for each domain in your
  account. For more information about domain tags and backfilling these tags, see [Multiple domains overview](domain-multiple.md "domain-multiple.md")

## Console

The following section shows how to create a new IAM policy that limits access to
resources in the domain to user profiles with the domain tag, as well as how to
attach this policy to the IAM execution role of the domain, from the Amazon SageMaker AI
console.

###### Note

This policy only works in domains that use Amazon SageMaker Studio Classic as the default
experience.

1. Create an IAM policy
   named `StudioDomainResourceIsolationPolicy-`domain-id``
   with the following JSON policy document by completing the steps in [Creating
   IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateAPIs",
 "Effect": "Allow",
 "Action": "sagemaker:Create*",
 "NotResource": [
 "arn:aws:sagemaker:*:*:domain/*",
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:space/*"
 ]
 },
 {
 "Sid": "ResourceAccessRequireDomainTag",
 "Effect": "Allow",
 "Action": [
 "sagemaker:Update*",
 "sagemaker:Delete*",
 "sagemaker:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:domain-arn": "`domain-arn`"
 }
 }
 },
 {
 "Sid": "AllowActionsThatDontSupportTagging",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeImageVersion",
 "sagemaker:UpdateImageVersion",
 "sagemaker:DeleteImageVersion",
 "sagemaker:DescribeModelCardExportJob",
 "sagemaker:DescribeAction"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DeleteDefaultApp",
 "Effect": "Allow",
 "Action": "sagemaker:DeleteApp",
 "Resource": "arn:aws:sagemaker:*:*:app/`domain-id`/*/jupyterserver/default"
 }
 ]
}`

```

2. Attach
   the `StudioDomainResourceIsolationPolicy-`domain-id``
   policy to the domain's execution role by completing the steps in [Modifying a role (console)](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy").

## AWS CLI

The following section shows how to create a new IAM policy that limits access to
resources in the domain to user profiles with the domain tag, as well as how to
attach this policy to the execution role of the domain, from the AWS CLI.

###### Note

This policy only works in domains that use Amazon SageMaker Studio Classic as the default
experience.

1. Create a file named
   `StudioDomainResourceIsolationPolicy-`domain-id``
   with the following content from your local machine.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateAPIs",
 "Effect": "Allow",
 "Action": "sagemaker:Create*",
 "NotResource": [
 "arn:aws:sagemaker:*:*:domain/*",
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:space/*"
 ]
 },
 {
 "Sid": "ResourceAccessRequireDomainTag",
 "Effect": "Allow",
 "Action": [
 "sagemaker:Update*",
 "sagemaker:Delete*",
 "sagemaker:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:domain-arn": "`domain-arn`"
 }
 }
 },
 {
 "Sid": "AllowActionsThatDontSupportTagging",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeImageVersion",
 "sagemaker:UpdateImageVersion",
 "sagemaker:DeleteImageVersion",
 "sagemaker:DescribeModelCardExportJob",
 "sagemaker:DescribeAction"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DeleteDefaultApp",
 "Effect": "Allow",
 "Action": "sagemaker:DeleteApp",
 "Resource": "arn:aws:sagemaker:*:*:app/`domain-id`/*/jupyterserver/default"
 }
 ]
}`

```

2. Create a new IAM policy using
   the `StudioDomainResourceIsolationPolicy-`domain-id``
   file.

```
aws iam create-policy --policy-name `StudioDomainResourceIsolationPolicy-`domain-id`` --policy-document file://`StudioDomainResourceIsolationPolicy-`domain-id``
```

3. Attach the newly created policy to a new or existing role that is used as the
   domain's execution role.

```
aws iam attach-role-policy --policy-arn arn:aws:iam:`account-id`:policy/`StudioDomainResourceIsolationPolicy-`domain-id`` --role-name `domain-execution-role`
```
