

# Manage access to resources
<a name="access-control-manage-access-intro"></a>

A *permissions policy* describes who has access to what. The following section explains the available options for creating permissions policies.

**Note**  
This section discusses using IAM in the context of AWS Control Tower. It doesn't provide detailed information about the IAM service. For complete IAM documentation, see [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*. For information about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

Policies attached to an IAM identity are referred to as *identity-based* policies (IAM polices). Policies attached to a resource are referred to as *resource-based* policies.

**Note**  
 AWS Control Tower supports only identity-based policies (IAM policies). 

**Topics**
+ [About identity-based policies (IAM policies)](#access-control-manage-access-intro-iam-policies)
+ [Create roles and assign permissions](assign-permissions.md)
+ [Resource-based policies](#access-control-manage-access-intro-resource-policies)

## About identity-based policies (IAM policies)
<a name="access-control-manage-access-intro-iam-policies"></a>

You can attach policies to IAM identities. For example, you can do the following:
+ **Attach a permissions policy to a user or a group in your account** – To grant a user permissions to create an AWS Control Tower resource, such as setting up a landing zone, you can attach a permissions policy to a user or group that the user belongs to.
+  **Attach a permissions policy to a role (grant cross-account permissions)** – You can attach an identity-based permissions policy to an IAM role to grant cross-account permissions. For example, an administrator for one AWS account (*Account A*) can create a role that grants cross-account permissions to another AWS account (*Account B*), or the administrator can create a role that grants permissions to another AWS service.

  1. The Account A administrator creates an IAM role and attaches a permissions policy to the role that grants permissions to manage resources in Account A.

  1. The Account A administrator attaches a trust policy to the role. The policy identifies Account B as the principal who can assume the role.

  1. As principal, the Account B administrator can give any user in Account B permission to assume the role. By assuming the role, users in Account B can create or gain access to resources in Account A.

  1. To grant an AWS service the ability (permissions) to assume the role, the principal that you specify in the trust policy can be an AWS service.

## Resource-based policies
<a name="access-control-manage-access-intro-resource-policies"></a>

Other services, such as Amazon S3, also support resource-based permissions policies. For example, you can attach a policy to an S3 bucket to manage access permissions to that bucket. AWS Control Tower does not support resource-based policies.