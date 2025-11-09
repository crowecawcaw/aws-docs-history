# Managing users and groups for an Amazon Q Business application using APIs

Amazon Q Business provides APIs to manage users and groups in your Amazon Q Business. You can't configure user management using the
console—Amazon Q Business automatically invokes these API operations
for you when you configure your data source connector connection. You can use these APIs
to implement your own user and group management solution if you create a Amazon Q Business application environment programmatically.

###### Note

As of Dec 17, 2024, Amazon Q Business will recognize all email addresses as
case-insensitive and recognize subaddresses as equivalent to the original email
address. For example, JohnDoe@example.com, johndoe@example.com, and
johndoe+work@example.com will be considered the same email address. For assistance
with applications or to report a concern, contact Support, sign into the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") .

| API action                                                                                 | API description                                                                                                                             | Relevant User Guide topic                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [CreateUser](../api-reference/API_CreateUser.md "../api-reference/API_CreateUser.md")      | Creates a universally unique identifier (UUID) mapped to a list of<br>local user ids within an application                                  | [User mapping](connector-principal-store.md#user-mapping "connector-principal-store.md#user-mapping")    |
| [GetUser](../api-reference/API_GetUser.md "../api-reference/API_GetUser.md")               | Describes the universally unique identifier (UUID) associated with a<br>local user in a data source                                         | [User mapping](connector-principal-store.md#user-mapping "connector-principal-store.md#user-mapping")    |
| [UpdateUser](../api-reference/API_UpdateUser.md "../api-reference/API_UpdateUser.md")      | Updates information associated with a user id                                                                                               | [User mapping](connector-principal-store.md#user-mapping "connector-principal-store.md#user-mapping")    |
| [PutGroup](../api-reference/API_PutGroup.md "../api-reference/API_PutGroup.md")            | Creates, or updates, a mapping of users to groups                                                                                           | [Group mapping](connector-principal-store.md#group-mapping "connector-principal-store.md#group-mapping") |
| [DeleteGroup](../api-reference/API_DeleteGrooup.md "../api-reference/API_DeleteGrooup.md") | Deletes a group so that all users and sub groups that belong to the<br>group can no longer access documents only available to that<br>group | [Group mapping](connector-principal-store.md#group-mapping "connector-principal-store.md#group-mapping") |
| [GetGroup](../api-reference/API_GetGroup.md "../api-reference/API_GetGroup.md")            | Describes a group by group name                                                                                                             | [Group mapping](connector-principal-store.md#group-mapping "connector-principal-store.md#group-mapping") |
| [ListGroups](../api-reference/API_ListGroups.md "../api-reference/API_ListGroups.md")      | Provides a list of groups that are mapped to users                                                                                          | [Group mapping](connector-principal-store.md#group-mapping "connector-principal-store.md#group-mapping") |
