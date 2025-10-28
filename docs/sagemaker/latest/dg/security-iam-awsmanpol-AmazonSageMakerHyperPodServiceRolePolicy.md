# AWS

managed policy: AmazonSageMakerHyperPodServiceRolePolicy

SageMaker HyperPod creates and uses the service-linked role named
`AWSServiceRoleForSageMakerHyperPod` with the
`AmazonSageMakerHyperPodServiceRolePolicy` attached to the role. This policy
grants Amazon SageMaker HyperPod permissions to related AWS services such as Amazon EKS and
Amazon CloudWatch.

The service-linked role makes setting up SageMaker HyperPod easier because you don’t have to
manually add the necessary permissions. SageMaker HyperPod defines the permissions of its
service-linked roles, and unless defined otherwise, only SageMaker HyperPod can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your SageMaker HyperPod resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose
a **Yes** with a link to view the service-linked role
documentation for that service.

The `AmazonSageMakerHyperPodServiceRolePolicy` allows SageMaker HyperPod to complete
the following actions on the specified resources on your behalf.

**Permissions details**

This service-linked role policy includes the following permissions.

- `eks` – Allows principals to read Amazon Elastic Kubernetes Service (EKS) cluster
  information.
- `logs` – Allows principals to publish Amazon CloudWatch log streams to
  `/aws/sagemaker/Clusters`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EKSClusterDescribePermissions",
 "Effect": "Allow",
 "Action": "eks:DescribeCluster",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "CloudWatchLogGroupPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/Clusters/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "CloudWatchLogStreamPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/Clusters/*:log-stream:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for SageMaker HyperPod

You don't need to manually create a service-linked role. When you create a SageMaker HyperPod
cluster using the SageMaker AI console, the AWS CLI, or the AWS SDKs, SageMaker HyperPod creates the
service-linked role for you.

If you delete this service-linked role but need to create it again, you can use the same
process (create a new SageMaker HyperPod cluster) to recreate the role in your account.

## Editing a service-linked role for SageMaker HyperPod

SageMaker HyperPod does not allow you to edit the
`AWSServiceRoleForSageMakerHyperPod` service-linked role. After you create a
service-linked role, you cannot change the name of the role because various entities might
reference the role. However, you can edit the description of the role using IAM. For more
information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for SageMaker HyperPod

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

**To delete SageMaker HyperPod cluster resources using the service-linked
role**

Use one of the following options to delete SageMaker HyperPod cluster resources.

- [Delete a SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster") using the SageMaker AI console
- [Delete a SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-delete-cluster "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-delete-cluster") using the AWS CLI

###### Note

If the SageMaker HyperPod service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForSageMakerHyperPod` service-linked role. For more information,
see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for SageMaker HyperPod service-linked

roles

SageMaker HyperPod supports using service-linked roles in all of the Regions where the service
is available. For more information, see [Prerequisites for SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md").
