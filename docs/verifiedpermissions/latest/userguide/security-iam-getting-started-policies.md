

# IAM policies for Verified Permissions
<a name="security-iam-getting-started-policies"></a>

Verified Permissions manages the permissions of users within your application. In order for your application to call the Verified Permissions APIs or for AWS Management Console users to be allowed to manage Cedar policies in a Verified Permissions policy store, you must add the necessary IAM permissions.

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the IAM User Guide.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied (listed below). You can't specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the IAM User Guide.


|  **Action**  |  **Description**  | 
| --- | --- | 
| [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html) | Action to create a new identity source. | 
| [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) | Action to create a Cedar policy in a policy store. You can create either a static policy or a policy linked to a policy template. | 
| [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html) | Action to create a new policy store. | 
| [CreatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyTemplate.html) | Action to create a new policy template. | 
| [DeleteIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeleteIdentitySource.html) | Action to delete an identity source. | 
| [DeletePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicy.html) | Action to delete a policy from a policy store. | 
| [DeletePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStore.html) | Action to delete a policy store. | 
| [DeletePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyTemplate.html) | Action to delete a policy template. | 
| [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html) | Action to get an identity source. | 
| [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html) | Action to retrieve information about a specified policy. | 
| [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html) | Action to retrieve information about a specified policy store. | 
| [GetPolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyTemplate.html) | Action to get a policy template. | 
| [GetSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetSchema.html) | Action to get a schema. | 
| [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) | Action to get an [authorization response](terminology.md#term-authorization-response) based on the parameters described in the [authorization request](terminology.md#term-authorization-request). | 
| [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) | Action to get an [authorization response](terminology.md#term-authorization-response) based on the parameters described in the [authorization request](terminology.md#term-authorization-request) where the principal comes from an identity token. | 
| [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html) | Action to list all the identity sources in the AWS account. | 
| [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) | Action to list all policies in a policy store. | 
| [ListPolicyStores](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStores.html) | Action to list all policy stores in the AWS account. | 
| [ListPolicyTemplates](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyTemplates.html) | Action to list all policy templates in the AWS account. | 
| [ListTagsForResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListTagsForResource.html) | Action to list all the tags for a resource. | 
| [PutSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PutSchema.html) | Action to add a schema to a policy store. | 
| [TagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TagResource.html) | Action to add a tag to a resource. | 
| [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html) | Action to update an identity source. | 
| [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html) | Action to update a policy in a policy store. | 
| [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html) | Action to update a policy store. | 
| [UpdatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html) | Action to update a policy template. | 
| [UntagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UntagResource.html) | Action to remove a tag from a resource. | 

Example IAM policy for permission to the CreatePolicy action:

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
                "verifiedpermissions:CreatePolicy"
            ],
            "Resource": "*"
        }
    ]
 }
```

------