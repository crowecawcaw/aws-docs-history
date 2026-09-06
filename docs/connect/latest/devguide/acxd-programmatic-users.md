# Programmatic Users

Manage machine identities that authenticate with the Platform SDK. Programmatic users are assigned role configurations that determine their access level.

###### Contents

- [ListProgrammaticUsers](#acxd-programmatic-users-listprogrammaticusers "#acxd-programmatic-users-listprogrammaticusers")
- [CreateProgrammaticUser](#acxd-programmatic-users-createprogrammaticuser "#acxd-programmatic-users-createprogrammaticuser")
- [GetProgrammaticUser](#acxd-programmatic-users-getprogrammaticuser "#acxd-programmatic-users-getprogrammaticuser")
- [UpdateProgrammaticUser](#acxd-programmatic-users-updateprogrammaticuser "#acxd-programmatic-users-updateprogrammaticuser")
- [DeleteProgrammaticUser](#acxd-programmatic-users-deleteprogrammaticuser "#acxd-programmatic-users-deleteprogrammaticuser")
- [Request Parameters](#acxd-programmatic-users-request-parameters "#acxd-programmatic-users-request-parameters")
- [Role Config](#acxd-programmatic-users-role-config "#acxd-programmatic-users-role-config")

## ListProgrammaticUsers

Lists all programmatic users.

**Input**

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

**Sample Request**

```
await client.send(new ListProgrammaticUsersCommand({}));
```

**Output**

```
{
  "items": [
    {
      "userId": "u1a2b3c4-5678-90ab-cdef-1234567890ab",
      "teamId": "team-uuid",
      "name": "ci-deploy-bot",
      "roleConfig": {
        "accountRole": "administrator"
      },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z"
    }
  ],
  "nextToken": null
}
```

**Errors**

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateProgrammaticUser

Creates a new programmatic user.

**Input**

| Parameter    | Type   | Required |
| ------------ | ------ | -------- |
| `name`       | string | Yes      |
| `roleConfig` | object | Yes      |

**Sample Request**

```
await client.send(new CreateProgrammaticUserCommand({
  name: "ci-deploy-bot",
  roleConfig: {
    accountRole: "administrator",
  },
}));
```

**Output**

```
{
  "userId": "u1a2b3c4-5678-90ab-cdef-1234567890ab",
  "teamId": "team-uuid",
  "name": "ci-deploy-bot",
  "roleConfig": {
    "accountRole": "administrator"
  },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z"
}
```

**Errors**

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## GetProgrammaticUser

Gets a single programmatic user by ID.

**Input**

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| `userId`  | string | Yes      |

**Sample Request**

```
await client.send(new GetProgrammaticUserCommand({
  userId: "u1a2b3c4-5678-90ab-cdef-1234567890ab",
}));
```

**Output**

```
{
  "userId": "u1a2b3c4-5678-90ab-cdef-1234567890ab",
  "teamId": "team-uuid",
  "name": "ci-deploy-bot",
  "roleConfig": {
    "accountRole": "administrator"
  },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z"
}
```

**Errors**

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateProgrammaticUser

Updates a programmatic user's name or role configuration.

**Input**

| Parameter    | Type   | Required |
| ------------ | ------ | -------- |
| `userId`     | string | Yes      |
| `name`       | string | No       |
| `roleConfig` | object | No       |

**Sample Request**

```
await client.send(new UpdateProgrammaticUserCommand({
  userId: "u1a2b3c4-5678-90ab-cdef-1234567890ab",
  name: "ci-deploy-bot-updated",
  roleConfig: {
    accountRole: "administrator",
  },
}));
```

**Output**

```
{
  "userId": "u1a2b3c4-5678-90ab-cdef-1234567890ab",
  "teamId": "team-uuid",
  "name": "ci-deploy-bot-updated",
  "roleConfig": {
    "accountRole": "administrator"
  },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z"
}
```

**Errors**

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## DeleteProgrammaticUser

Deletes a programmatic user. Fails if API keys are still associated, delete all keys first.

**Input**

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| `userId`  | string | Yes      |

**Sample Request**

```
await client.send(new DeleteProgrammaticUserCommand({
  userId: "u1a2b3c4-5678-90ab-cdef-1234567890ab",
}));
```

**Output**

No response body.

**Errors**

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `ConflictException` (409) API keys still exist for this user
- `InternalServerException` (500)

## Request Parameters

`userId`

Type: String

The programmatic user ID.

`teamId`

Type: String

The team/account this user belongs to (read-only).

`name`

Type: String

Display name for the programmatic user. 1–128 characters.

`roleConfig`

Type: Object

Role configuration determining access level. See Role Config.

`createdAt`

Type: String

When the user was created (ISO 8601).

`updatedAt`

Type: String

When the user was last modified (ISO 8601).

`nextToken`

Type: String

Pagination token. See Common Types.

`maxResults`

Type: Integer

Max items per page. See Common Types.

## Role Config

Provide exactly one variant:

`accountRole`

Type: String

Account-level role granting full access across all workspaces. Currently the only value is `administrator`.

```
{
  "roleConfig": {
    "accountRole": "administrator"
  }
}
```

`workspaceRoles`

Type: Array

Workspace-scoped role assignments. Each entry grants access to a specific workspace with a designated role.

```
{
  "roleConfig": {
    "workspaceRoles": [
      { "workspaceId": "ws-uuid-1", "role": "developer" },
      { "workspaceId": "ws-uuid-2", "roleId": "custom-role-uuid" }
    ]
  }
}
```

### Workspace Role Assignment

| Field         | Type   | Required |
| ------------- | ------ | -------- |
| `workspaceId` | string | Yes      |
| `role`        | string | No       |
| `roleId`      | string | No       |

`workspaceId`

Type: String

The workspace this assignment applies to.

`role`

Type: String

A pre-defined role name. One of: `administrator`, `developer`, `contentManager`, `readOnly`. Provide `role` OR `roleId`, not both.

`roleId`

Type: String

A custom role ID (created via the Roles API). Provide `role` OR `roleId`, not both.
