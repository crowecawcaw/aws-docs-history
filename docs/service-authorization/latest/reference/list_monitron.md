

# Actions, resources, and condition keys for Amazon Monitron
<a name="list_monitron"></a>

Amazon Monitron (service prefix: `monitron`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/Monitron/latest/user-guide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/monitron/monitron.json) for this service.

**Topics**
+ [Actions defined by Amazon Monitron](#list_monitron-actions-as-permissions)
+ [Permission-only actions for Amazon Monitron](#list_monitron-permission-only-actions)
+ [Resource types defined by Amazon Monitron](#list_monitron-resources-for-iam-policies)
+ [Condition keys for Amazon Monitron](#list_monitron-policy-keys)

## Actions defined by Amazon Monitron
<a name="list_monitron-actions-as-permissions"></a>

Amazon Monitron has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Amazon Monitron
<a name="list_monitron-permission-only-actions"></a>

The following actions are defined by Amazon Monitron but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)  **
  - **Description:** Grants permission to associate a user with the project as an administrator
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html)  **
  - **Description:** Grants permission to create a project
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_monitron-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_monitron-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProjectUserAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-user.html)  **
  - **Description:** Grants permission to associate a user with the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateUserAccessRoleAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-user.html)  **
  - **Description:** Grants permission to associate an access role with the user
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-delete-project.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProjectUserAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-user.html)  **
  - **Description:** Grants permission to disassociate a user from the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteUserAccessRoleAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-user.html)  **
  - **Description:** Grants permission to disassociate an access role from the user
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DisassociateProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-remove-project-admin.html)  **
  - **Description:** Grants permission to disassociate an administrator from the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [GetProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html)  **
  - **Description:** Grants permission to get information about a project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html)  **
  - **Description:** Grants permission to describe an administrator who is associated with the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProjectAdminUsers](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)  **
  - **Description:** Grants permission to list all administrators associated with the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ListProjectUserAssociations](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)  **
  - **Description:** Grants permission to list all users associated with the project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html)  **
  - **Description:** Grants permission to list all projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html)  **
  - **Description:** Grants permission to list all tags for a resource
  - **Resource types (\*required):** [project](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUserAccessRoleAssociations](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)  **
  - **Description:** Grants permission to list all access roles associated with the user
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [project](#list_monitron-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_monitron-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_monitron-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html#modify-tag-1)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [project](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_monitron-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-updating-project.html)  **
  - **Description:** Grants permission to update a project
  - **Resource types (\*required):** [project\*](#list_monitron-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Monitron
<a name="list_monitron-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [project](https://docs.aws.amazon.com/Monitron/latest/user-guide/projects-chapter.html)  | arn:${Partition}:monitron:${Region}:${Account}:project/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_monitron-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Monitron
<a name="list_monitron-policy-keys"></a>

Amazon Monitron defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 