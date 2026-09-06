

# Actions, resources, and condition keys for Multi-party approval
<a name="list_mpa"></a>

Multi-party approval (service prefix: `mpa`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mpa/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mpa/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mpa/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mpa/mpa.json) for this service.

**Topics**
+ [API operations defined by Multi-party approval](#list_mpa-operations)
+ [Actions defined by Multi-party approval](#list_mpa-actions-as-permissions)
+ [Permission-only actions for Multi-party approval](#list_mpa-permission-only-actions)
+ [Resource types defined by Multi-party approval](#list_mpa-resources-for-iam-policies)
+ [Condition keys for Multi-party approval](#list_mpa-policy-keys)

## API operations defined by Multi-party approval
<a name="list_mpa-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mpa-actions-as-permissions).




- **   CancelSession  **
  - **IAM action:**  [mpa:CancelSession](#list_mpa-action-CancelSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApprovalTeam  **
  - **IAM action:**  [mpa:CreateApprovalTeam](#list_mpa-action-CreateApprovalTeam)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mpa:TagResource](#list_mpa-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIdentitySource  **
  - **IAM action:**  [mpa:CreateIdentitySource](#list_mpa-action-CreateIdentitySource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mpa:TagResource](#list_mpa-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteIdentitySource  **
  - **IAM action:**  [mpa:DeleteIdentitySource](#list_mpa-action-DeleteIdentitySource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInactiveApprovalTeamVersion  **
  - **IAM action:**  [mpa:DeleteInactiveApprovalTeamVersion](#list_mpa-action-DeleteInactiveApprovalTeamVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApprovalTeam  **
  - **IAM action:**  [mpa:GetApprovalTeam](#list_mpa-action-GetApprovalTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentitySource  **
  - **IAM action:**  [mpa:GetIdentitySource](#list_mpa-action-GetIdentitySource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyVersion  **
  - **IAM action:**  [mpa:GetPolicyVersion](#list_mpa-action-GetPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [mpa:GetResourcePolicy](#list_mpa-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **IAM action:**  [mpa:GetSession](#list_mpa-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApprovalTeams  **
  - **IAM action:**  [mpa:ListApprovalTeams](#list_mpa-action-ListApprovalTeams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentitySources  **
  - **IAM action:**  [mpa:ListIdentitySources](#list_mpa-action-ListIdentitySources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **IAM action:**  [mpa:ListPolicies](#list_mpa-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyVersions  **
  - **IAM action:**  [mpa:ListPolicyVersions](#list_mpa-action-ListPolicyVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcePolicies  **
  - **IAM action:**  [mpa:ListResourcePolicies](#list_mpa-action-ListResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **IAM action:**  [mpa:ListSessions](#list_mpa-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mpa:ListTagsForResource](#list_mpa-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartActiveApprovalTeamDeletion  **
  - **IAM action:**  [mpa:StartActiveApprovalTeamDeletion](#list_mpa-action-StartActiveApprovalTeamDeletion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartApprovalTeamBaseline  **
  - **IAM action:**  [mpa:StartApprovalTeamBaseline](#list_mpa-action-StartApprovalTeamBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mpa:TagResource](#list_mpa-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mpa:UntagResource](#list_mpa-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApprovalTeam  **
  - **IAM action:**  [mpa:UpdateApprovalTeam](#list_mpa-action-UpdateApprovalTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Multi-party approval
<a name="list_mpa-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CancelSession.html)  **
  - **Description:** Grants permission to cancel an approval session
  - **Resource types (\*required):** [session\*](#list_mpa-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[mpa:ProtectedResourceAccount](#list_mpa-mpa_ProtectedResourceAccount)<br />[mpa:RequestedOperation](#list_mpa-mpa_RequestedOperation)
  - **Access level:** Write

- **   [CreateApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateApprovalTeam.html)  **
  - **Description:** Grants permission to create an approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mpa-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mpa-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateIdentitySource.html)  **
  - **Description:** Grants permission to create an identity source
  - **Resource types (\*required):** [identity-source\*](#list_mpa-resource-identity-source)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mpa-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mpa-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteIdentitySource.html)  **
  - **Description:** Grants permission to delete an identity source
  - **Resource types (\*required):** [identity-source\*](#list_mpa-resource-identity-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInactiveApprovalTeamVersion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteInactiveApprovalTeamVersion.html)  **
  - **Description:** Grants permission to delete an inactive approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeam.html)  **
  - **Description:** Grants permission to retrieve details for an approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetIdentitySource.html)  **
  - **Description:** Grants permission to retrieve details for an identity source
  - **Resource types (\*required):** [identity-source\*](#list_mpa-resource-identity-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyVersion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetPolicyVersion.html)  **
  - **Description:** Grants permission to retrieve details for a policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve details for a specific resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to retrieve details for an approval session
  - **Resource types (\*required):** [session\*](#list_mpa-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[mpa:ProtectedResourceAccount](#list_mpa-mpa_ProtectedResourceAccount)<br />[mpa:RequestedOperation](#list_mpa-mpa_RequestedOperation)
  - **Access level:** Read

- **   [ListApprovalTeams](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeams.html)  **
  - **Description:** Grants permission to list approval teams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdentitySources](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListIdentitySources.html)  **
  - **Description:** Grants permission to list identity sources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyVersions](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListPolicyVersions.html)  **
  - **Description:** Grants permission to list the versions for policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourcePolicies](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListResourcePolicies.html)  **
  - **Description:** Grants permission to list policies for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list approval sessions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartActiveApprovalTeamDeletion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartActiveApprovalTeamDeletion.html)  **
  - **Description:** Grants permission to start the deletion process for an active approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartApprovalTeamBaseline](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartApprovalTeamBaseline.html)  **
  - **Description:** Grants permission to start a baseline for an active approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mpa-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mpa-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mpa-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_UpdateApprovalTeam.html)  **
  - **Description:** Grants permission to update approval team
  - **Resource types (\*required):** [approval-team\*](#list_mpa-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Multi-party approval
<a name="list_mpa-permission-only-actions"></a>

The following actions are defined by Multi-party approval but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update policies for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartSessionInternal.html)  **
  - **Description:** Grants permission to start an approval session
  - **Resource types (\*required):** [session\*](#list_mpa-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_)<br />[mpa:ProtectedResourceAccount](#list_mpa-mpa_ProtectedResourceAccount)<br />[mpa:RequestedOperation](#list_mpa-mpa_RequestedOperation)
  - **Access level:** Write



## Resource types defined by Multi-party approval
<a name="list_mpa-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [approval-team](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | arn:${Partition}:mpa:${Region}:${Account}:approval-team/${ApprovalTeamId} | [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_) | 
|  [identity-source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | arn:${Partition}:mpa:${Region}:${Account}:identity-source/${IdentitySourceId} | [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | arn:${Partition}:mpa:${Region}:${Account}:session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_mpa-aws_ResourceTag___TagKey_) | 

## Condition keys for Multi-party approval
<a name="list_mpa-policy-keys"></a>

Multi-party approval defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [mpa:ProtectedResourceAccount](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | Filters access by the account that owns the resource that is the target of the operation that requires approval | String | 
|   [mpa:RequestedOperation](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | Filters access by a requested operation that requires team approval before it can be executed | String | 