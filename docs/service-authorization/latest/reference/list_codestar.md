

# Actions, resources, and condition keys for AWS CodeStar
<a name="list_codestar"></a>

AWS CodeStar (service prefix: `codestar`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codestar/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codestar/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codestar/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codestar/codestar.json) for this service.

**Topics**
+ [Actions defined by AWS CodeStar](#list_codestar-actions-as-permissions)
+ [Permission-only actions for AWS CodeStar](#list_codestar-permission-only-actions)
+ [Resource types defined by AWS CodeStar](#list_codestar-resources-for-iam-policies)
+ [Condition keys for AWS CodeStar](#list_codestar-policy-keys)

## Actions defined by AWS CodeStar
<a name="list_codestar-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateTeamMember](https://docs.aws.amazon.com/codestar/latest/APIReference/API_AssociateTeamMember.html)  **
  - **Description:** Grants permission to add a user to the team for an AWS CodeStar project
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project with minimal structure, customer policies, and no resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codestar-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreateUserProfile](https://docs.aws.amazon.com/codestar/latest/APIReference/API_CreateUserProfile.html)  **
  - **Description:** Grants permission to create a profile for a user that includes user preferences, display name, and email
  - **Resource types (\*required):** [user\*](#list_codestar-resource-user)
  - **Condition keys:** [iam:ResourceTag/${TagKey}](#list_codestar-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project, including project resources. Does not delete users associated with the project, but does delete the IAM roles that allowed access to the project
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteUserProfile](https://docs.aws.amazon.com/codestar/latest/APIReference/API_DeleteUserProfile.html)  **
  - **Description:** Grants permission to delete a user profile in AWS CodeStar, including all personal preference data associated with that profile, such as display name and email address. It does not delete the history of that user, for example the history of commits made by that user
  - **Resource types (\*required):** [user\*](#list_codestar-resource-user)
  - **Condition keys:** [iam:ResourceTag/${TagKey}](#list_codestar-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_DescribeProject.html)  **
  - **Description:** Grants permission to describe a project and its resources
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserProfile](https://docs.aws.amazon.com/codestar/latest/APIReference/API_DescribeUserProfile.html)  **
  - **Description:** Grants permission to describe a user in AWS CodeStar and the user attributes across all projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateTeamMember](https://docs.aws.amazon.com/codestar/latest/APIReference/API_DisassociateTeamMember.html)  **
  - **Description:** Grants permission to remove a user from a project. Removing a user from a project also removes the IAM policies from that user that allowed access to the project and its resources
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ListProjects](https://docs.aws.amazon.com/codestar/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list all projects in CodeStar associated with your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResources](https://docs.aws.amazon.com/codestar/latest/APIReference/API_ListResources.html)  **
  - **Description:** Grants permission to list all resources associated with a project in CodeStar
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_ListTagsForProject.html)  **
  - **Description:** Grants permission to list the tags associated with a project in CodeStar
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTeamMembers](https://docs.aws.amazon.com/codestar/latest/APIReference/API_ListTeamMembers.html)  **
  - **Description:** Grants permission to list all team members associated with a project
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserProfiles](https://docs.aws.amazon.com/codestar/latest/APIReference/API_ListUserProfiles.html)  **
  - **Description:** Grants permission to list user profiles in AWS CodeStar
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_TagProject.html)  **
  - **Description:** Grants permission to add tags to a project in CodeStar
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_UntagProject.html)  **
  - **Description:** Grants permission to remove tags from a project in CodeStar
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateProject](https://docs.aws.amazon.com/codestar/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to update a project in CodeStar
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTeamMember](https://docs.aws.amazon.com/codestar/latest/APIReference/API_UpdateTeamMember.html)  **
  - **Description:** Grants permission to update team member attributes within a CodeStar project
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateUserProfile](https://docs.aws.amazon.com/codestar/latest/APIReference/API_UpdateUserProfile.html)  **
  - **Description:** Grants permission to update a profile for a user that includes user preferences, display name, and email
  - **Resource types (\*required):** [user\*](#list_codestar-resource-user)
  - **Condition keys:** [iam:ResourceTag/${TagKey}](#list_codestar-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   VerifyServiceRole  **
  - **Description:** Grants permission to verify whether the AWS CodeStar service role exists in the customer's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List



## Permission-only actions for AWS CodeStar
<a name="list_codestar-permission-only-actions"></a>

The following actions are defined by AWS CodeStar but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   DeleteExtendedAccess  **
  - **Description:** Grants permission to extended delete APIs
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   GetExtendedAccess  **
  - **Description:** Grants permission to extended read APIs
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   PutExtendedAccess  **
  - **Description:** Grants permission to extended write APIs
  - **Resource types (\*required):** [project\*](#list_codestar-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CodeStar
<a name="list_codestar-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [project](https://docs.aws.amazon.com/codestar/latest/userguide/working-with-projects.html)  | arn:${Partition}:codestar:${Region}:${Account}:project/${ProjectId} | [aws:ResourceTag/${TagKey}](#list_codestar-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/codestar/latest/userguide/working-with-user-info.html)  | arn:${Partition}:iam::${Account}:user/${AwsUserName} | [iam:ResourceTag/${TagKey}](#list_codestar-iam_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeStar
<a name="list_codestar-policy-keys"></a>

AWS CodeStar defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   aws:RequestTag/${TagKey}  | Filters access by requests based on the allowed set of values for each of the tags | String | 
|   aws:ResourceTag/${TagKey}  | Filters access by actions based on tag-value associated with the resource | String | 
|   aws:TagKeys  | Filters access by requests based on the presence of mandatory tags in the request | ArrayOfString | 
|   iam:ResourceTag/${TagKey}  | Filters access by actions based on tag-value associated with the resource | String | 