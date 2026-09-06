

# Actions, resources, and condition keys for Amazon EKS Auth
<a name="list_eks-auth"></a>

Amazon EKS Auth (service prefix: `eks-auth`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eks/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eks/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eks/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/eks-auth/eks-auth.json) for this service.

**Topics**
+ [API operations defined by Amazon EKS Auth](#list_eks-auth-operations)
+ [Actions defined by Amazon EKS Auth](#list_eks-auth-actions-as-permissions)
+ [Resource types defined by Amazon EKS Auth](#list_eks-auth-resources-for-iam-policies)
+ [Condition keys for Amazon EKS Auth](#list_eks-auth-policy-keys)

## API operations defined by Amazon EKS Auth
<a name="list_eks-auth-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_eks-auth-actions-as-permissions).




- **   AssumeRoleForPodIdentity  **
  - **IAM action:**  [eks-auth:AssumeRoleForPodIdentity](#list_eks-auth-action-AssumeRoleForPodIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon EKS Auth
<a name="list_eks-auth-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssumeRoleForPodIdentity](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.html)  **
  - **Description:** Grants permission to exchange a Kubernetes service account token for temporary AWS credentials
  - **Resource types (\*required):** [cluster\*](#list_eks-auth-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-auth-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon EKS Auth
<a name="list_eks-auth-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html)  | arn:${Partition}:eks:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_eks-auth-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EKS Auth
<a name="list_eks-auth-policy-keys"></a>

Amazon EKS Auth defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a tag key and value pair | String | 