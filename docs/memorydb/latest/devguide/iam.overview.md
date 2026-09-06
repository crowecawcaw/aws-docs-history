

# Overview of managing access permissions to your MemoryDB resources
<a name="iam.overview"></a>

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies. An account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles). In addition, MemoryDB also supports attaching permissions policies to resources. 

**Note**  
An *account administrator* (or administrator user) is a user with administrator privileges. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

**Topics**
+ [MemoryDB resources and operations](#iam.overview.resourcesandoperations)
+ [Understanding resource ownership](#access-control-resource-ownership)
+ [Managing access to resources](#iam.overview.managingaccess)
+ [Using identity-based policies (IAM policies) for MemoryDB](iam.identitybasedpolicies.md)
+ [Resource-level permissions](iam.resourcelevelpermissions.md)
+ [Using Service-Linked Roles for MemoryDB](using-service-linked-roles.md)
+ [AWS managed policies for MemoryDB](security-iam-awsmanpol.md)
+ [MemoryDB API permissions: Actions, resources, and conditions reference](iam.APIReference.md)

## MemoryDB resources and operations
<a name="iam.overview.resourcesandoperations"></a>

In MemoryDB, the primary resource is a *cluster*.

These resources have unique Amazon Resource Names (ARNs) associated with them as shown following. 

**Note**  
For resource-level permissions to be effective, the resource name on the ARN string should be lower case.



| Resource type | ARN format | 
| --- | --- | 
| User  | arn:aws:memorydb:{{us-east-1:123456789012}}:user/user1 | 
| Access Control List (ACL)  | arn:aws:memorydb:{{us-east-1:123456789012}}:acl/myacl | 
| Cluster  | arn:aws:memorydb:{{us-east-1:123456789012}}:cluster/my-cluster | 
| Snapshot  | arn:aws:memorydb:{{us-east-1:123456789012}}:snapshot/my-snapshot | 
| Parameter group  | arn:aws:memorydb:{{us-east-1:123456789012}}:parametergroup/my-parameter-group | 
| Subnet group  | arn:aws:memorydb:{{us-east-1:123456789012}}:subnetgroup/my-subnet-group | 

MemoryDB provides a set of operations to work with MemoryDB resources. For a list of available operations, see MemoryDB [Actions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Operations.html).

## Understanding resource ownership
<a name="access-control-resource-ownership"></a>

A *resource owner* is the AWS account that created the resource. That is, the resource owner is the AWS account of the principal entity that authenticates the request that creates the resource. A *principal entity* can be the root account, an IAM user, or an IAM role. The following examples illustrate how this works:
+ Suppose that you use the root account credentials of your AWS account to create a cluster. In this case, your AWS account is the owner of the resource. In MemoryDB, the resource is the cluster.
+ Suppose that you create an IAM user in your AWS account and grant permissions to create a cluster to that user. In this case, the user can create a cluster. However, your AWS account, to which the user belongs, owns the cluster resource.
+ Suppose that you create an IAM role in your AWS account with permissions to create a cluster. In this case, anyone who can assume the role can create a cluster. Your AWS account, to which the role belongs, owns the cluster resource. 

## Managing access to resources
<a name="iam.overview.managingaccess"></a>

A *permissions policy* describes who has access to what. The following section explains the available options for creating permissions policies.

**Note**  
This section discusses using IAM in the context of MemoryDB. It doesn't provide detailed information about the IAM service. For complete IAM documentation, see [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*. For information about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

Policies attached to an IAM identity are referred to as *identity-based* policies (IAM policies). Policies attached to a resource are referred to as *resource-based* policies. 

**Topics**
+ [Identity-based policies (IAM policies)](#iam.overview.managingaccess.identitybasedpolicies)
+ [Specifying policy elements: Actions, effects, resources, and principals](#iam.overview.policyelements)
+ [Specifying conditions in a policy](#iam.specifyconditions)

### Identity-based policies (IAM policies)
<a name="iam.overview.managingaccess.identitybasedpolicies"></a>

You can attach policies to IAM identities. For example, you can do the following:
+ **Attach a permissions policy to a user or a group in your account** – An account administrator can use a permissions policy that is associated with a particular user to grant permissions. In this case, the permissions are for that user to create a MemoryDB resource, such as a cluster, parameter group, or security group.
+ **Attach a permissions policy to a role (grant cross-account permissions)** – You can attach an identity-based permissions policy to an IAM role to grant cross-account permissions. For example, the administrator in Account A can create a role to grant cross-account permissions to another AWS account (for example, Account B) or an AWS service as follows:

  1. Account A administrator creates an IAM role and attaches a permissions policy to the role that grants permissions on resources in Account A.

  1. Account A administrator attaches a trust policy to the role identifying Account B as the principal who can assume the role. 

  1. Account B administrator can then delegate permissions to assume the role to any users in Account B. Doing this allows users in Account B to create or access resources in Account A. In some cases, you might want to grant an AWS service permissions to assume the role. To support this approach, the principal in the trust policy can also be an AWS service principal. 

  For more information about using IAM to delegate permissions, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.

The following is an example policy that allows a user to perform the `DescribeClusters` action for your AWS account. MemoryDB also supports identifying specific resources using the resource ARNs for API actions. (This approach is also referred to as resource-level permissions). 

For more information about using identity-based policies with MemoryDB, see [Using identity-based policies (IAM policies) for MemoryDB](iam.identitybasedpolicies.md). For more information about users, groups, roles, and permissions, see [Identities (Users, Groups, and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

### Specifying policy elements: Actions, effects, resources, and principals
<a name="iam.overview.policyelements"></a>

For each MemoryDB resource (see [MemoryDB resources and operations](#iam.overview.resourcesandoperations)), the service defines a set of API operations (see [Actions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Operations.html)). To grant permissions for these API operations, MemoryDB defines a set of actions that you can specify in a policy. For example, for the MemoryDB cluster resource, the following actions are defined: `CreateCluster`, `DeleteCluster`, and `DescribeClusters`. Performing an API operation can require permissions for more than one action.

The following are the most basic policy elements:
+ **Resource** – In a policy, you use an Amazon Resource Name (ARN) to identify the resource to which the policy applies. For more information, see [MemoryDB resources and operations](#iam.overview.resourcesandoperations).
+ **Action** – You use action keywords to identify resource operations that you want to allow or deny. For example, depending on the specified `Effect`, the `memorydb:CreateCluster` permission allows or denies the user permissions to perform the MemoryDB `CreateCluster` operation.
+ **Effect** – You specify the effect when the user requests the specific action—this can be either allow or deny. If you don't explicitly grant access to (allow) a resource, access is implicitly denied. You can also explicitly deny access to a resource. For example, you might do this to make sure that a user can't access a resource, even if a different policy grants access.
+ **Principal** – In identity-based policies (IAM policies), the user that the policy is attached to is the implicit principal. For resource-based policies, you specify the user, account, service, or other entity that you want to receive permissions (applies to resource-based policies only). 

To learn more about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

For a table showing all of the MemoryDB API actions, see [MemoryDB API permissions: Actions, resources, and conditions reference](iam.APIReference.md).

### Specifying conditions in a policy
<a name="iam.specifyconditions"></a>

When you grant permissions, you can use the IAM policy language to specify the conditions when a policy should take effect. For example, you might want a policy to be applied only after a specific date. For more information about specifying conditions in a policy language, see [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition) in the *IAM User Guide*. 

