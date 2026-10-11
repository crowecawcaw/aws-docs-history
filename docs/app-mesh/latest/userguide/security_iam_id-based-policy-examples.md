

# AWS App Mesh identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

**Important**  
End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect). 

By default, IAM users and roles don't have permission to create or modify App Mesh resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Scope App Mesh permissions to segment workloads](#security_iam_id-based-policy-examples-scope-permissions)
+ [Using the App Mesh console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Create a mesh](#policy_example1)
+ [List and describe all meshes](#policy_example2)
+ [Creating App Mesh meshes with restricted tags](#security_iam_id-based-policy-examples-view-widget-tags)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete App Mesh resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Scope App Mesh permissions to segment workloads
<a name="security_iam_id-based-policy-examples-scope-permissions"></a>

This topic explains how App Mesh uses a service-linked role to access other AWS services on your behalf, and describes practices you can use to scope permissions and segment workloads that share an account or a mesh.

App Mesh acts on your behalf when it resolves the resources that your mesh refers to. It uses its service-linked role, `AWSServiceRoleForAppMesh`, to call other AWS services. It doesn't use the credentials of the principal that created the mesh resource. For example, when a virtual node uses AWS Cloud Map service discovery, App Mesh discovers the instances in the namespace with the service-linked role.

Because of this, if you grant a principal permission to call App Mesh APIs, you also give that principal indirect access to any resource that the service-linked role can reach. IAM doesn't evaluate policies that deny the principal access to the downstream service, such as `servicediscovery`, for these calls. For more information about this behavior, see [Indirect permissions with service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#create-service-linked-role-permissions-transfer) in the *IAM User Guide*.

To segment workloads that share an account or a mesh, control access at the App Mesh layer with the following practices.
+ **Scope resource management permissions to the resources a principal owns** – Don't grant `appmesh:*` to deployment roles, developer roles, or the service account of the App Mesh controller for Kubernetes. Instead, scope actions such as `appmesh:CreateVirtualNode` and `appmesh:UpdateVirtualNode` to the resource ARNs that the principal owns. For example, allow a team to manage only virtual nodes whose names start with that team's prefix. This prevents a principal from creating a virtual node that refers to another team's namespace or service. For more information about resource ARNs, see [Resources](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources).
+ **Scope Envoy proxy authorization to each proxy's own virtual node** – Enable proxy authorization for all virtual nodes and virtual gateways. Grant `appmesh:StreamAggregatedResources` to each workload's IAM role only for the ARN of the virtual node or virtual gateway that the workload runs. An Envoy proxy can then read only its own configuration, including the endpoints that App Mesh discovered for it. For more information about proxy authorization, see [Envoy Proxy authorization](proxy-authorization.md).
+ **Don't rely on denying downstream service permissions** – Even if you deny a principal `servicediscovery` or other downstream actions, you can't restrict what App Mesh resolves for that principal. App Mesh makes those calls with its service-linked role. Use the App Mesh permissions described in the previous practices instead.

## Using the App Mesh console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS App Mesh console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the App Mesh resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (IAM users or roles) with that policy. You can attach the `[AWSAppMeshReadOnly](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSAppMeshReadOnly%24jsonEditor)` managed policy to users. For more information, see [Adding Permissions to a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that you're trying to perform.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Create a mesh
<a name="policy_example1"></a>

This example shows how you can create a policy that allows a user to create a mesh for an account, in any Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "appmesh:CreateMesh",
            "Resource": "arn:aws:appmesh:*:{{123456789012}}:CreateMesh"
        }
    ]
}
```

------

## List and describe all meshes
<a name="policy_example2"></a>

This example shows how you can create a policy that allows a user read-only access to list and describe all meshes.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "appmesh:DescribeMesh",
                "appmesh:ListMeshes"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Creating App Mesh meshes with restricted tags
<a name="security_iam_id-based-policy-examples-view-widget-tags"></a>

You can use tags in your IAM policies to control what tags can be passed in the IAM request. You can specify which tag key-value pairs can be added, changed, or removed from an IAM user or role. This example shows how you might create a policy that allows creating a mesh, but only if the mesh is created with a tag named {{teamName}} and a value of {{booksTeam}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "appmesh:CreateMesh",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/{{teamName}}": "{{booksTeam}}"
                }
            }
        }
    ]
}
```

------

You can attach this policy to the IAM users in your account. If a user attempts to create a mesh, the mesh must include a tag named `teamName` and a value of `booksTeam`. If the mesh does not include this tag and value, the attempt to create the mesh fails. For more information, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.