# Using service-linked roles for SageMaker AI Inference

Amazon SageMaker AI Inference uses the service-linked role named
`AWSServiceRoleForSageMakerInference`. The
`AmazonSageMakerInferenceServiceRolePolicy` policy attached to this role grants
SageMaker AI Inference permissions to manage Elastic Network Interfaces (ENIs) in your virtual
private cloud (VPC) for real-time inference endpoints.

With the service-linked role, you don't have to manually add the necessary permissions for
VPC networking operations. SageMaker AI Inference defines the permissions of its service-linked
role. Only SageMaker AI Inference can assume this role, as specified by the trust policy. The defined
permissions include the trust policy and the permissions policy. You cannot attach the
permissions policy to any other AWS Identity and Access Management (IAM) entity.

You can delete a service-linked role only after first deleting the related resources. This
protects your SageMaker AI Inference resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). In that guide, look for services that have
**Yes** in the **Service-linked
roles** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

## Service-linked role permissions for SageMaker AI Inference

SageMaker AI Inference uses the service-linked role named
`AWSServiceRoleForSageMakerInference` to manage ENIs
for real-time inference endpoints deployed in your VPC. With the service-linked role,
SageMaker AI Inference can reliably patch the infrastructure for these endpoints. The service-linked
role continues to function even if you modify or delete the endpoint execution role.

The `AWSServiceRoleForSageMakerInference` service-linked role trusts the
following service to assume the role:

- `inference.sagemaker.amazonaws.com`

The role permissions policy named `AmazonSageMakerInferenceServiceRolePolicy`
allows SageMaker AI Inference to complete the following actions on the specified
resources:

- `ec2:CreateNetworkInterface` – Allows the service to create ENIs in your
  VPC subnets and security groups. ENIs are tagged with
  `AmazonSageMakerManaged: true` at creation time. The create action is scoped
  to resources in the caller's account.
- `ec2:CreateNetworkInterfacePermission` – Allows the service to grant ENI
  attach permissions scoped to SageMaker-managed ENIs only (gated on
  `AmazonSageMakerManaged: true` tag and
  `ec2:AuthorizedService: sagemaker.amazonaws.com`).
- `ec2:DeleteNetworkInterface` – Allows the service to delete ENIs that it
  previously created. Scoped to ENIs tagged with
  `AmazonSageMakerManaged: true`.
- `ec2:DeleteNetworkInterfacePermission` – Allows the service to remove ENI
  permissions for SageMaker-managed ENIs.
- `ec2:CreateTags` – Allows the service to tag ENIs at creation time only
  (gated on `ec2:CreateAction: CreateNetworkInterface`).
- `ec2:DescribeNetworkInterfaces`,
  `ec2:DescribeVpcs`,
  `ec2:DescribeDhcpOptions`,
  `ec2:DescribeSubnets`,
  `ec2:DescribeSecurityGroups` – Allows the service to read VPC and network
  configuration. All describe actions are scoped to the caller's account.

For the full JSON policy document, see [AmazonSageMakerInferenceServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerInferenceServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerInferenceServiceRolePolicy.md") in the [AWS Managed Policies Reference Guide](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for SageMaker AI Inference

You don't need to manually create a service-linked role. When you create a real-time
inference endpoint with VPC configuration using the AWS Management Console, the AWS CLI, or the AWS SDKs,
SageMaker AI Inference creates the service-linked role for you automatically.

To allow SageMaker AI Inference to create the service-linked role on your behalf, your
IAM principal must have the following permission when calling
`CreateEndpoint`:

```
{
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/inference.sagemaker.amazonaws.com/*",
    "Condition": {
        "StringEquals": {
            "iam:AWSServiceName": "inference.sagemaker.amazonaws.com"
        }
    }
}
```

If you use the `AmazonSageMakerFullAccess` managed policy, that policy
includes this permission automatically.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a new VPC-enabled inference
endpoint, SageMaker AI Inference creates the service-linked role for you again.

###### Note

If the calling principal does not have `iam:CreateServiceLinkedRole`
permission, SageMaker AI Inference falls back to using the endpoint execution role for VPC
networking operations. SageMaker AI Inference creates the endpoint successfully, but does
not protect the endpoint against future execution role modifications.

## Editing a service-linked role for SageMaker AI Inference

You cannot edit the
`AWSServiceRoleForSageMakerInference` service-linked role. After you create a
service-linked role, you cannot change the name of the role because various entities might
reference the role. However, you can edit the description of the role using IAM. For more
information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for SageMaker AI Inference

If you no longer need a feature or service that requires a service-linked role, we
recommend that you delete that role to avoid maintaining unused permissions. However, you must
clean up the resources for your service-linked role before you can manually delete it.

###### Note

If the SageMaker AI Inference service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete SageMaker AI Inference resources used by the AWSServiceRoleForSageMakerInference

- Delete all VPC-enabled real-time inference endpoints in your account. Use one of the
  following options:

  - [Delete an
    endpoint](realtime-endpoints-delete-resources.md "realtime-endpoints-delete-resources.md") using the SageMaker AI console
  - Use the `DeleteEndpoint` operation with the AWS CLI or SDKs

###### To manually delete the service-linked role using IAM

- Use the IAM console, the AWS CLI, or the AWS API to delete the
  `AWSServiceRoleForSageMakerInference` service-linked role. For more
  information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
  _IAM User Guide_.

## Supported AWS Regions for SageMaker AI Inference service-linked roles

SageMaker AI Inference supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").
