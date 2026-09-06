# Workspaces

Manage workspaces: isolated environments that contain all resources for a project or
team. Workspace operations are account-level and do not require a workspace ID.

###### Contents

- [ListWorkspaces](#acxd-workspaces-listworkspaces "#acxd-workspaces-listworkspaces")
- [CreateWorkspace](#acxd-workspaces-createworkspace "#acxd-workspaces-createworkspace")
- [GetWorkspace](#acxd-workspaces-getworkspace "#acxd-workspaces-getworkspace")
- [UpdateWorkspace](#acxd-workspaces-updateworkspace "#acxd-workspaces-updateworkspace")
- [DeleteWorkspace](#acxd-workspaces-deleteworkspace "#acxd-workspaces-deleteworkspace")
- [Request Parameters](#acxd-workspaces-request-parameters "#acxd-workspaces-request-parameters")

## ListWorkspaces

Lists all workspaces in the account.

### Input

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

### Sample Request

```
await client.send(new ListWorkspacesCommand({}));
```

### Output

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

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateWorkspace

Creates a new workspace.

### Input

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| `name`    | string | Yes      |
| `tags`    | array  | No       |

### Sample Request

```
await client.send(new CreateWorkspaceCommand({
  name: "SDK Test Workspace",
  tags: ["testing", "sdk"],
}));
```

### Output

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

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## GetWorkspace

Gets a single workspace by ID.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `workspaceId` | string | Yes      |

### Sample Request

```
await client.send(new GetWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateWorkspace

Updates a workspace.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `workspaceId` | string | Yes      |
| `name`        | string | No       |
| `tags`        | array  | No       |

### Sample Request

```
await client.send(new UpdateWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
  name: "SDK Test Workspace Updated",
  tags: ["testing", "sdk", "updated"],
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## DeleteWorkspace

Deletes a workspace and all its resources.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `workspaceId` | string | Yes      |

### Sample Request

```
await client.send(new DeleteWorkspaceCommand({
  workspaceId: "67898477-f36f-4b06-bdca-0d9a1f2eb9cc",
}));
```

### Output

No response body.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### `workspaceId`

Type: String

The workspace ID.

### `name`

Type: String

Workspace name. Alphanumeric + spaces/punctuation, 1–36 characters.

### `tags`

Type: Array

Classification tags (max 5, each a string).

### `createdAt`

Type: String

When the workspace was created (ISO 8601).

### `updatedAt`

Type: String

When the workspace was last modified (ISO 8601).

### `updatedBy`

Type: String

The identity of who last modified the workspace.

### `nextToken`

Type: String

Pagination token. See Common Types.

### `maxResults`

Type: Integer

Max items per page (1–100). See Common Types.
