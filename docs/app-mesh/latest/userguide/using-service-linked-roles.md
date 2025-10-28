# Using service-linked roles for App Mesh

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

AWS App Mesh uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to App Mesh.
Service-linked roles are predefined by App Mesh and include all the permissions that the service requires
to call other AWS services on your behalf.

A service-linked role makes setting up App Mesh easier because you don’t have to manually add the
necessary permissions. App Mesh defines the permissions of its service-linked roles, and unless defined
otherwise, only App Mesh can assume its roles. The defined permissions include the trust policy and the
permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your
App Mesh resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link
to view the service-linked role documentation for that service.

## Service-linked role permissions for App Mesh

App Mesh uses the service-linked role named **AWSServiceRoleForAppMesh** –
The role allows App Mesh to call AWS services on your behalf.

The AWSServiceRoleForAppMesh service-linked role trusts the `appmesh.amazonaws.com` service to assume the
role.

**Permission details**

- `servicediscovery:DiscoverInstances` ‐ Allows App Mesh to complete actions on all AWS
  resources.
- `servicediscovery:DiscoverInstancesRevision` ‐ Allows App Mesh to complete actions on
  all AWS resources.

This policy includes the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudMapServiceDiscovery",
 "Effect": "Allow",
 "Action": [
 "servicediscovery:DiscoverInstances",
 "servicediscovery:DiscoverInstancesRevision"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ACMCertificateVerification",
 "Effect": "Allow",
 "Action": [
 "acm:DescribeCertificate"
 ],
 "Resource": "*"
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit,
or delete a service-linked role. For more information, see [Service-Linked
Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for App Mesh

If you created a mesh after June 5, 2019 in the AWS Management Console, the AWS CLI, or the AWS API, App Mesh
created the service-linked role for you. For the service-linked role to have been created for you, the IAM
account that you used to create the mesh must have had the [`AWSAppMeshFullAccess`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSAppMeshFullAccess%24jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSAppMeshFullAccess%24jsonEditor") IAM policy attached to it, or a policy attached to it that
contained the `iam:CreateServiceLinkedRole` permission. If you delete this service-linked role,
and then need to create it again, you can use the same process to recreate the role in your account. When you
create a mesh, App Mesh creates the service-linked role for you again. If your account only
contains meshes created before June 5, 2019 and you want to use the service-linked role with those meshes,
then you can create the role using the IAM console.

You can use the IAM console to create a service-linked role with the
**App Mesh** use case. In the AWS CLI or the AWS API, create a service-linked
role with the `appmesh.amazonaws.com` service name. For more information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for App Mesh

App Mesh does not allow you to edit the AWSServiceRoleForAppMesh service-linked role. After you create a
service-linked role, you cannot change the name of the role because various entities might reference the
role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for App Mesh

If you no longer need to use a feature or service that requires a service-linked role, we recommend that
you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained.
However, you must clean up the resources for your service-linked role before you can manually delete
it.

###### Note

If the App Mesh service is using the role when you try to delete the resources, then the deletion
might fail. If that happens, wait for a few minutes and try the operation again.

###### To delete App Mesh resources used by the AWSServiceRoleForAppMesh

1. Delete all [routes](routes.md "routes.md") defined for all routers in the
   mesh.
2. Delete all [virtual routers](virtual_routers.md "virtual_routers.md") in the mesh.
3. Delete all [virtual services](virtual_services.md "virtual_services.md") in the mesh.
4. Delete all [virtual nodes](virtual_nodes.md "virtual_nodes.md") in the mesh.
5. Delete the [mesh](meshes.md "meshes.md").

Complete the previous steps for all meshes in your account.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAppMesh service-linked role. For more
information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for App Mesh service-linked roles

App Mesh supports using service-linked roles in all of the Regions where the service is available.
For more information, see [App Mesh Endpoints and Quotas](../../../general/latest/gr/appmesh.md "../../../general/latest/gr/appmesh.md").
