**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshooting IAM

This topic covers some common errors that you may see while using Amazon EKS with IAM and how to work around them.

## AccessDeniedException

If you receive an `AccessDeniedException` when calling an AWS API operation, then the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") credentials that you’re using don’t have the required permissions to make that call.

```
 An error occurred (AccessDeniedException) when calling the DescribeCluster operation:
User: <shared id="region.arn"/>iam::111122223333:user/user_name is not authorized to perform:
eks:DescribeCluster on resource: <shared id="region.arn"/>eks:region:111122223333:cluster/my-cluster
```

In the previous example message, the user does not have permissions to call the Amazon EKS `DescribeCluster` API operation. To provide Amazon EKS admin permissions to an IAM principal, see [Amazon EKS identity-based policy examples](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

For more general information about IAM, see [Controlling access using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.

## Can’t see **Nodes** on the **Compute** tab or anything on the **Resources** tab and you receive an error in the AWS Management Console

You may see a console error message that says `Your current user or role does not have access to Kubernetes objects on this EKS cluster`. Make sure that the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") user that you’re using the AWS Management Console with has the necessary permissions. For more information, see [Required permissions](view-kubernetes-resources.md#view-kubernetes-resources-permissions "view-kubernetes-resources.md#view-kubernetes-resources-permissions").

## aws-auth `ConfigMap` does not grant access to the cluster

The [AWS IAM Authenticator](https://github.com/kubernetes-sigs/aws-iam-authenticator "https://github.com/kubernetes-sigs/aws-iam-authenticator") doesn’t permit a path in the role ARN used in the `ConfigMap`. Therefore, before you specify `rolearn`, remove the path. For example, change `arn:aws:iam::`111122223333`:role/`team`/`developers`/`eks-admin`` to `arn:aws:iam::`111122223333`:role/`eks-admin``.

## I am not authorized to perform iam:PassRole

If you receive an error that you’re not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon EKS.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Amazon EKS. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: {arn-aws}iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary’s policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people outside of my AWS account to access my Amazon EKS resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- To learn whether Amazon EKS supports these features, see [How Amazon EKS works with IAM](security-iam-service-with-iam.md "security-iam-service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Pod containers receive the following error: `An error occurred (SignatureDoesNotMatch) when calling the GetCallerIdentity operation: Credential should be scoped to a valid region`

Your containers receive this error if your application is explicitly making requests to the AWS STS global endpoint (`https://sts.amazonaws`) and your Kubernetes service account is configured to use a regional endpoint. You can resolve the issue with one of the following options:

- Update your application code to remove explicit calls to the AWS STS global endpoint.
- Update your application code to make explicit calls to regional endpoints such as `https://sts.us-west-2.amazonaws.com`. Your application should have redundancy built in to pick a different AWS Region in the event of a failure of the service in the AWS Region. For more information, see [Managing AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md") in the IAM User Guide.
- Configure your service accounts to use the global endpoint. Clusters use the regional endpoint by default. For more information, see [Configure the AWS Security Token Service endpoint for a service account](configure-sts-endpoint.md "configure-sts-endpoint.md").
