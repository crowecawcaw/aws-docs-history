# Actions, resources, and condition keys for Amazon EKS Auth

Amazon EKS Auth (service prefix: `eks-auth`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../eks/latest/APIReference.md "../../../eks/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../eks/latest/userguide/security-iam.md "../../../eks/latest/userguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/eks-auth/eks-auth.json "https://servicereference.us-east-1.amazonaws.com/v1/eks-auth/eks-auth.json") for this service.

###### Topics

- [API operations defined by Amazon EKS Auth](#list_eks-auth-operations "#list_eks-auth-operations")
- [Actions defined by Amazon EKS Auth](#list_eks-auth-actions-as-permissions "#list_eks-auth-actions-as-permissions")
- [Resource types defined by Amazon EKS Auth](#list_eks-auth-resources-for-iam-policies "#list_eks-auth-resources-for-iam-policies")
- [Condition keys for Amazon EKS Auth](#list_eks-auth-policy-keys "#list_eks-auth-policy-keys")

## API operations defined by Amazon EKS Auth

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_eks-auth-actions-as-permissions "#list_eks-auth-actions-as-permissions").

| Operation                | IAM action                                                                                                                           | Condition key | Possible value(s) | Access level |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| AssumeRoleForPodIdentity | [eks-auth:AssumeRoleForPodIdentity](#list_eks-auth-action-AssumeRoleForPodIdentity "#list_eks-auth-action-AssumeRoleForPodIdentity") |               |                   | Read         |

## Actions defined by Amazon EKS Auth

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                   | Description                                                                                    | Resource types (\*required)                                                    | Condition keys                                                                                                   | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| [AssumeRoleForPodIdentity](../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md "../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md") | Grants permission to exchange a Kubernetes service account token for temporary AWS credentials | [cluster\*](#list_eks-auth-resource-cluster "#list_eks-auth-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_eks-auth-aws_ResourceTag___TagKey_ "#list_eks-auth-aws_ResourceTag___TagKey_") | Read         |

## Resource types defined by Amazon EKS Auth

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                   | ARN                                                              | Condition keys                                                                                                   |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [cluster](../../../eks/latest/userguide/clusters.md "../../../eks/latest/userguide/clusters.md") | arn:${Partition}:eks:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_eks-auth-aws_ResourceTag___TagKey_ "#list_eks-auth-aws_ResourceTag___TagKey_") |

## Condition keys for Amazon EKS Auth

Amazon EKS Auth defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                                     | Description                                | Type   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------ |
| [aws:ResourceTag/${TagKey}](../../../eks/latest/userguide/security_iam_service-with-iam.md#security_iam_service-with-iam-tags "../../../eks/latest/userguide/security_iam_service-with-iam.md#security_iam_service-with-iam-tags") | Filters access by a tag key and value pair | String |
