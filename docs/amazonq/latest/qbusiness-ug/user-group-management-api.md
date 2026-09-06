

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing users and groups for an Amazon Q Business application using APIs
<a name="user-group-management-api"></a>

Amazon Q Business provides APIs to manage users and groups in your Amazon Q Business. You can't configure user management using the console—Amazon Q Business automatically invokes these API operations for you when you configure your data source connector connection. You can use these APIs to implement your own user and group management solution if you create a Amazon Q Business application environment programmatically.

**Note**  
As of Dec 17, 2024, Amazon Q Business will recognize all email addresses as case-insensitive and recognize subaddresses as equivalent to the original email address. For example, JohnDoe@example.com, johndoe@example.com, and johndoe\+work@example.com will be considered the same email address. For assistance with applications or to report a concern, contact Support, sign into the [AWS Support Center](https://console.aws.amazon.com/support/home#/) .



| API action | API description | Relevant User Guide topic | 
| --- | --- | --- | 
| [CreateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateUser.html) | Creates a universally unique identifier (UUID) mapped to a list of local user ids within an application | [User mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#user-mapping) | 
| [GetUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetUser.html) | Describes the universally unique identifier (UUID) associated with a local user in a data source | [User mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#user-mapping) | 
| [UpdateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateUser.html) | Updates information associated with a user id | [User mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#user-mapping) | 
| [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html) | Creates, or updates, a mapping of users to groups | [Group mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#group-mapping) | 
| [DeleteGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteGrooup.html) | Deletes a group so that all users and sub groups that belong to the group can no longer access documents only available to that group | [Group mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#group-mapping) | 
| [GetGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetGroup.html) | Describes a group by group name | [Group mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#group-mapping) | 
| [ListGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListGroups.html) | Provides a list of groups that are mapped to users | [Group mapping](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html#group-mapping) | 