# Reading from Monday entities

**Prerequisites**

- A Monday Object you would like to read from. Refer the supported entities table below to check the available
  entities.

**Supported entities for Source**

Entities list:

- Account: [https://developer.monday.com/api-reference/docs/account#queries](https://developer.monday.com/api-reference/docs/account#queries "https://developer.monday.com/api-reference/docs/account#queries")
- Board: [https://developer.monday.com/api-reference/docs/boards#queries](https://developer.monday.com/api-reference/docs/boards#queries "https://developer.monday.com/api-reference/docs/boards#queries")
- Column: [https://developer.monday.com/api-reference/docs/columns#queries](https://developer.monday.com/api-reference/docs/columns#queries "https://developer.monday.com/api-reference/docs/columns#queries")
- Docs: [https://developer.monday.com/api-reference/docs/docs#queries](https://developer.monday.com/api-reference/docs/docs#queries "https://developer.monday.com/api-reference/docs/docs#queries")
- Document Block: [https://developer.monday.com/api-reference/docs/blocks#queries](https://developer.monday.com/api-reference/docs/blocks#queries "https://developer.monday.com/api-reference/docs/blocks#queries")
- Files: [https://developer.monday.com/api-reference/docs/files#queries](https://developer.monday.com/api-reference/docs/files#queries "https://developer.monday.com/api-reference/docs/files#queries")
- Folders: [https://developer.monday.com/api-reference/docs/folders#queries](https://developer.monday.com/api-reference/docs/folders#queries "https://developer.monday.com/api-reference/docs/folders#queries")
- Groups: [https://developer.monday.com/api-reference/docs/groups#queries](https://developer.monday.com/api-reference/docs/groups#queries "https://developer.monday.com/api-reference/docs/groups#queries")
- Item: [https://developer.monday.com/api-reference/docs/items#queries](https://developer.monday.com/api-reference/docs/items#queries "https://developer.monday.com/api-reference/docs/items#queries")
- Subitems: [https://developer.monday.com/api-reference/docs/subitems#queries](https://developer.monday.com/api-reference/docs/subitems#queries "https://developer.monday.com/api-reference/docs/subitems#queries")
- Tags: [https://developer.monday.com/api-reference/docs/tags-queries#queries](https://developer.monday.com/api-reference/docs/tags-queries#queries "https://developer.monday.com/api-reference/docs/tags-queries#queries")
- Teams: [https://developer.monday.com/api-reference/docs/teams#queries](https://developer.monday.com/api-reference/docs/teams#queries "https://developer.monday.com/api-reference/docs/teams#queries")
- Updates: [https://developer.monday.com/api-reference/docs/updates#queries](https://developer.monday.com/api-reference/docs/updates#queries "https://developer.monday.com/api-reference/docs/updates#queries")
- Users: [https://developer.monday.com/api-reference/docs/users#queries](https://developer.monday.com/api-reference/docs/users#queries "https://developer.monday.com/api-reference/docs/users#queries")
- Workspaces: [https://developer.monday.com/api-reference/docs/workspaces#queries](https://developer.monday.com/api-reference/docs/workspaces#queries "https://developer.monday.com/api-reference/docs/workspaces#queries")

| Entity          | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| --------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account         | No              | No             | No                | Yes                | No                    |
| Boards          | Yes             | Yes            | No                | Yes                | No                    |
| Columns         | No              | No             | No                | Yes                | No                    |
| Docs            | Yes             | Yes            | No                | Yes                | No                    |
| Document Blocks | No              | Yes            | No                | Yes                | No                    |
| Files           | Yes             | No             | No                | Yes                | No                    |
| Groups          | No              | No             | No                | Yes                | No                    |
| Item            | Yes             | Yes            | No                | Yes                | No                    |
| Subitems        | No              | No             | No                | Yes                | No                    |
| Tags            | Yes             | No             | No                | Yes                | Yes                   |
| Teams           | Yes             | No             | No                | Yes                | No                    |
| Updates         | No              | Yes            | No                | Yes                | No                    |
| Users           | Yes             | Yes            | No                | Yes                | No                    |
| Workspaces      | Yes             | Yes            | No                | Yes                | No                    |
| Folders         | Yes             | Yes            | No                | Yes                | No                    | **Example** `monday_read = glueContext.create_dynamic_frame.from_options( connection_type="monday", connection_options={ "connectionName": "connectionName", "ENTITY_NAME": "account", "API_VERSION": "v2" }` |
