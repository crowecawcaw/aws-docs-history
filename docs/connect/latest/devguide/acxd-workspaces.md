

# Workspaces
<a name="acxd-workspaces"></a>

Manage workspaces: isolated environments that contain all resources for a project or team. Workspace operations are account-level and do not require a workspace ID.

**Topics**
+ [ListWorkspaces](#acxd-workspaces-listworkspaces)
+ [CreateWorkspace](#acxd-workspaces-createworkspace)
+ [GetWorkspace](#acxd-workspaces-getworkspace)
+ [UpdateWorkspace](#acxd-workspaces-updateworkspace)
+ [DeleteWorkspace](#acxd-workspaces-deleteworkspace)
+ [Request Parameters](#acxd-workspaces-request-parameters)

## ListWorkspaces
<a name="acxd-workspaces-listworkspaces"></a>

Lists all workspaces in the account.

### Input
<a name="acxd-workspaces-listworkspaces-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-workspaces-listworkspaces-sample-request"></a>

```
await client.send(new ListWorkspacesCommand({}));
```

### Output
<a name="acxd-workspaces-listworkspaces-output"></a>

```
{
  "items": [
    {
      "workspaceId": "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
      "name": "Production",
      "tags": ["prod", "main"],
      "createdAt": "2026-01-15T10:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "updatedBy": "admin-user"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-workspaces-listworkspaces-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateWorkspace
<a name="acxd-workspaces-createworkspace"></a>

Creates a new workspace.

### Input
<a name="acxd-workspaces-createworkspace-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| tags | array | No | 

### Sample Request
<a name="acxd-workspaces-createworkspace-sample-request"></a>

```
await client.send(new CreateWorkspaceCommand({
  name: "SDK Test Workspace",
  tags: ["testing", "sdk"],
}));
```

### Output
<a name="acxd-workspaces-createworkspace-output"></a>

```
{
  "workspaceId": "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
  "name": "SDK Test Workspace",
  "tags": ["testing", "sdk"],
  "createdAt": "2026-01-15T10:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "admin-user"
}
```

### Errors
<a name="acxd-workspaces-createworkspace-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetWorkspace
<a name="acxd-workspaces-getworkspace"></a>

Gets a single workspace by ID.

### Input
<a name="acxd-workspaces-getworkspace-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| workspaceId | string | Yes | 

### Sample Request
<a name="acxd-workspaces-getworkspace-sample-request"></a>

```
await client.send(new GetWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
}));
```

### Output
<a name="acxd-workspaces-getworkspace-output"></a>

```
{
  "workspaceId": "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
  "name": "SDK Test Workspace",
  "tags": ["testing", "sdk"],
  "createdAt": "2026-01-15T10:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "admin-user"
}
```

### Errors
<a name="acxd-workspaces-getworkspace-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateWorkspace
<a name="acxd-workspaces-updateworkspace"></a>

Updates a workspace.

### Input
<a name="acxd-workspaces-updateworkspace-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| workspaceId | string | Yes | 
| name | string | No | 
| tags | array | No | 

### Sample Request
<a name="acxd-workspaces-updateworkspace-sample-request"></a>

```
await client.send(new UpdateWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
  name: "SDK Test Workspace Updated",
  tags: ["testing", "sdk", "updated"],
}));
```

### Output
<a name="acxd-workspaces-updateworkspace-output"></a>

```
{
  "workspaceId": "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
  "name": "SDK Test Workspace Updated",
  "tags": ["testing", "sdk", "updated"],
  "createdAt": "2026-01-15T10:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "admin-user"
}
```

### Errors
<a name="acxd-workspaces-updateworkspace-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## DeleteWorkspace
<a name="acxd-workspaces-deleteworkspace"></a>

Deletes a workspace and all its resources.

### Input
<a name="acxd-workspaces-deleteworkspace-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| workspaceId | string | Yes | 

### Sample Request
<a name="acxd-workspaces-deleteworkspace-sample-request"></a>

```
await client.send(new DeleteWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
}));
```

### Output
<a name="acxd-workspaces-deleteworkspace-output"></a>

No response body.

### Errors
<a name="acxd-workspaces-deleteworkspace-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-workspaces-request-parameters"></a>

### `workspaceId`
<a name="acxd-workspaces-request-parameters-workspaceid"></a>

Type: String

The workspace ID.

### `name`
<a name="acxd-workspaces-request-parameters-name"></a>

Type: String

Workspace name. Alphanumeric \+ spaces/punctuation, 1–36 characters.

### `tags`
<a name="acxd-workspaces-request-parameters-tags"></a>

Type: Array

Classification tags (max 5, each a string).

### `createdAt`
<a name="acxd-workspaces-request-parameters-createdat"></a>

Type: String

When the workspace was created (ISO 8601).

### `updatedAt`
<a name="acxd-workspaces-request-parameters-updatedat"></a>

Type: String

When the workspace was last modified (ISO 8601).

### `updatedBy`
<a name="acxd-workspaces-request-parameters-updatedby"></a>

Type: String

The identity of who last modified the workspace.

### `nextToken`
<a name="acxd-workspaces-request-parameters-nexttoken"></a>

Type: String

Pagination token. See Common Types.

### `maxResults`
<a name="acxd-workspaces-request-parameters-maxresults"></a>

Type: Integer

Max items per page (1–100). See Common Types.