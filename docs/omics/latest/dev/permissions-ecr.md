# Amazon ECR permissions

Before the HealthOmics service can run a workflow in a container from your private Amazon ECR repository, you create a
resource policy for the repository. The policy grants permission for the HealthOmics service to use the container. You add
this resource policy to each private repository referenced by the workflow.

###### Note

The private repository and the workflow must be in the same region.

If different AWS accounts own the workflow and the repository, you need to configure cross-account
permissions.

You don't need to grant additional repository access for shared workflows. However, you can create policies that
allow or deny specific workflows access to the container image.

To use the Amazon ECR pull through cache feature, you need to create a registry permission policy.

The following sections describe how to configure Amazon ECR resource permissions for these scenarios. For more
information about permissions in Amazon ECR, see [Private registry permissions in Amazon ECR](../../../AmazonECR/latest/userguide/registry-permissions.md "../../../AmazonECR/latest/userguide/registry-permissions.md").

###### Topics

- [Create a resource policy for the Amazon ECR repository](#permissions-resource-policy "#permissions-resource-policy")
- [Running workflows with cross-account containers](#permissions-cross-account-containers "#permissions-cross-account-containers")
- [Amazon ECR policies for shared workflows](#permissions-shared-workflows "#permissions-shared-workflows")
- [Policies for Amazon ECR pull through cache](#permissions-ecr-ptc "#permissions-ecr-ptc")

## Create a resource policy for the Amazon ECR repository

Create a resource policy to allow the HealthOmics service to run a workflow using a container in the repository.
The policy grants permission for the HealthOmics service principal to access the required Amazon ECR actions.

Follow these steps to create the policy:

1. Open the [private repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories") page in the
   Amazon ECR console and select the repository you're granting access to.
2. From the side bar navigation, select **Permissions**.
3. Choose **Edit**.
4. Choose **Edit policy JSON**.
5. Add the following policy statement and then select **Save**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "omics workflow access",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Running workflows with cross-account containers

If different AWS accounts own the workflow and the container, you need to configure the following cross-account permissions:

1. Update the Amazon ECR policy for the repository to explicitly grant permission to the account that owns the workflow.
2. Update the service role for the account that owns the workflow to grant it access to the container image.

The following example demonstrates an Amazon ECR resource policy that grants access to the account that owns the workflow.

In this example:

- Workflow account ID: 111122223333
- Container repository account ID: 444455556666
- Container name: samtools

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessToTheServiceRoleOfTheAccountThatOwnsTheWorkflow",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/DemoCustomer"
 },
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 }
 ]
}`

```

To complete the setup, add the following policy statement to the service role of the account that owns
the workflow. The policy grants permission for the service role to access the “samtools” container image.
Make sure to replace the account numbers, container name, and region with your own values.

```
{
    "Sid": "CrossAccountEcrRepoPolicy",
    "Effect": "Allow",
    "Action": ["ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage", "ecr:GetDownloadUrlForLayer"],
    "Resource": "arn:aws:ecr:us-west-2:444455556666:repository/samtools"
}
```

## Amazon ECR policies for shared workflows

###### Note

HealthOmics automatically allows a shared workflow to access the Amazon ECR repository in the workflow owner's account, while the workflow is running in the
subscriber's account. You don't need to grant additional repository access for shared workflows. For more information see
[Sharing HealthOmics workflows](sharing-workflows.md "sharing-workflows.md").

By default, subscriber don’t have access to the Amazon ECR repository to use the underlying containers.
Optionally, you can customize access to the Amazon ECR repository by adding condition keys to the repository's
resource policy. The following sections provide example policies.

### Restrict access to specific workflows

You can list individual workflows in a condition statement, so only these workflow can use containers in
the repository. The **SourceArn** condition key specifies the ARN of the shared
workflow. The following example grants permission for the specified workflow to use this repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OmicsAccessPrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:omics:`us-east-1`:`111122223333`:workflow/1234567"
 }
 }
 }
 ]
}`

```

### Restrict access to specific accounts

You can list subscriber accounts in a condition statement, so that only these accounts have permission to
use containers in the repository. The **SourceAccount** condition key specifies
the AWS account of the subscriber. The following example grants permission for the specified account to use
this repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OmicsAccessPrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

You can also deny Amazon ECR permissions to specific subscribers, as shown in the following example
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OmicsAccessPrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
 }`

```

## Policies for Amazon ECR pull through cache

To use Amazon ECR pull through cache, you create a registry permission policy. You also create a repository
creation template, which defines the permissions for the repositories created by Amazon ECR pull through cache.

The following sections include examples of these policies. For more information about pull through cache, see
[Sync an upstream
registry with an Amazon ECR private registry](../../../AmazonECR/latest/userguide/pull-through-cache-private.md "../../../AmazonECR/latest/userguide/pull-through-cache-private.md") in the _Amazon Elastic Container Registry User Guide_.

### Registry permission policy

To use Amazon ECR pull through cache, create a registry permission policy. The registry permissions policy
provides control over replication and pull through cache permissions.

For cross-account replication, you must explictly allow each AWS account that can replicate its
repositories to your registry.

By default, when you create a pull through cache rule, any IAM principal that has permission to pull
images from a private registry can also use the pull through cache rule. You can use registry permissions to
further scope down these permissions to specific repositories.

Add a registry permission policy to the account that owns the container image.

In the following example, the policy allows the HealthOmics service to create repositories for each upstream
registry and to initiate upstream pull requests from the created repositories.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPTCinRegPermissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:CreateRepository",
 "ecr:BatchImportUpstreamImage"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/ecr-public/*",
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/docker-hub/*"
 ]
 }
 ]
}`

```

### Repository creation template

To use pull through cache in HealthOmics, the Amazon ECR repository must have a repository creation template. The
template defines configuration settings for the private repositories created for an upstream registry.

Each template contains a repository namespace prefix, which Amazon ECR uses to match new repositories to a
specific template. Templates can specify the configuration for all repository settings including resource-based
access policies, tag immutability, encryption, and lifecycle policies. For more information, see [Repository creation
templates](../../../AmazonECR/latest/userguide/repository-creation-templates.md "../../../AmazonECR/latest/userguide/repository-creation-templates.md") in the _Amazon Elastic Container Registry User Guide_.

In the following example, the policy allows the HealthOmics service to initiate upstream pull requests from the
upstream repositories.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PTCRepoCreationTemplate",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Policies for cross-account Amazon ECR access

For cross-account access, the owner of the private repository updates the registry permission policy and the
repository creation template to allow access for the other account and that account's run role.

In the registry permission policy, add a policy statement to allow the other account's run role to access
the Amazon ECR actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountPTCinRegPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`RUN_ROLE`"},
 "Action": [
 "ecr:CreateRepository",
 "ecr:BatchGetImage",
 "ecr:BatchImportUpstreamImage"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/`path`/*"
 }
 ]
}`

```

In the repository creation template, add a policy statement to allow the other account's run role to access
the new container images. Optionally, you can add condition statements to limit access to specific
workflows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountPTCinRepoCreationTemplate",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`RUN_ROLE`"},
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:omics:us-east-1:`444455556666`:workflow/`WORKFLOW_ID`",
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

Add permissions for two additional actions (CreateRepository and BatchImportUpstreamImage) in the run role
and specify the resource that the run role can access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountPTCRunRolePolicy",
 "Effect": "Allow",
 "Action": [
 "ecr:CreateRepository",
 "ecr:BatchImportUpstreamImage",
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:`123456789012`::repository/{path}/*"
 }
 ]
}`

```
