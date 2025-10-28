# Troubleshooting AWS App Mesh identity

and access

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

Use the following information to help you diagnose and fix common issues that you might
encounter when working with App Mesh and IAM.

###### Topics

- [I am not authorized to
  perform an action in App Mesh](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I want to allow people
  outside of my AWS account to access my App Mesh resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I am not authorized to

perform an action in App Mesh

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your sign-in credentials.

The following error occurs when the `mateojackson` IAM user tries to use
the console to create a virtual node named `my-virtual-node` in
the mesh named `my-mesh` but does not have the
`appmesh:CreateVirtualNode` permission.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: appmesh:CreateVirtualNode on resource: arn:aws:appmesh:us-east-1:123456789012:mesh/my-mesh/virtualNode/my-virtual-node
```

In this case, Mateo asks his administrator to update his policies to allow him to
create a virtual node using the `appmesh:CreateVirtualNode`
action.

###### Note

Since a virtual node is created within a mesh, Mateo's account also requires the
`appmesh:DescribeMesh` and
`appmesh:ListMeshes` actions to create the virtual node in
the console.

## I want to allow people

outside of my AWS account to access my App Mesh resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether App Mesh supports these features, see [How AWS App Mesh works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
