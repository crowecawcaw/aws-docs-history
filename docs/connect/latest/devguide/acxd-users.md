

# Users
<a name="acxd-users"></a>

Manage users in the account. Users are human identities (as opposed to programmatic users which are machine identities).

**Topics**
+ [ListUsers](#acxd-users-listusers)
+ [CreateUser](#acxd-users-createuser)
+ [GetUser](#acxd-users-getuser)
+ [UpdateUser](#acxd-users-updateuser)
+ [DeleteUser](#acxd-users-deleteuser)
+ [Request Parameters](#acxd-users-request-parameters)
+ [User Role Assignment](#acxd-users-user-role-assignment)
+ [Default Role](#acxd-users-default-role)

## ListUsers
<a name="acxd-users-listusers"></a>

Lists all users.

### Input
<a name="acxd-users-listusers-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-users-listusers-sample-request"></a>

```
await client.send(new ListUsersCommand({}));
```

### Output
<a name="acxd-users-listusers-output"></a>

```
{
  "items": [
    {
      "userId": "user-id-string",
      "cxnRole": "administrator",
      "userArn": "arn:aws:connect:us-west-2:123456789:instance/.../user/...",
      "username": "jane.doe",
      "firstName": "Jane",
      "lastName": "Doe",
      "email": "jane@example.com",
      "applicationIds": ["05c3fcc2-..."],
      "roles": [
        { "applicationId": "05c3fcc2-...", "role": "administrator" }
      ],
      "defaultRole": { "role": "administrator" },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "updatedBy": "admin-user"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-users-listusers-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateUser
<a name="acxd-users-createuser"></a>

Creates a new user.

### Input
<a name="acxd-users-createuser-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 
| cxnRole | string | Yes | 
| userArn | string | Yes | 
| username | string | Yes | 
| firstName | string | No | 
| lastName | string | No | 
| email | string | No | 
| applicationIds | array | No | 
| roles | array | No | 
| defaultRole | object | No | 

### Sample Request
<a name="acxd-users-createuser-sample-request"></a>

```
await client.send(new CreateUserCommand({
      userId: "00000000-0000-4000-8000-000000000099",
      cxnRole: "member",
      userArn: "arn:aws:connect:us-west-2:176202286863:instance/cb0ac315-73ce-4def-a2cc-cf3caf9866cc/agent/00000000-0000-4000-8000-000000000099",
      username: "sdk.testuser",
      firstName: "SDK",
      lastName: "TestUser",
      email: "sdk-test@example.com",
      applicationIds: ["a018836f-a909-4be0-a28b-53b413f1429c"],
      defaultRole: { role: "developer" },
      roles: [
        { applicationId: "a018836f-a909-4be0-a28b-53b413f1429c", role: "developer" },
      ],
}));
```

### Output
<a name="acxd-users-createuser-output"></a>

```
{
  "userId": "00000000-0000-4000-8000-000000000099",
  "cxnRole": "member",
  "userArn": "arn:aws:connect:us-west-2:176202286863:instance/cb0ac315-73ce-4def-a2cc-cf3caf9866cc/agent/00000000-0000-4000-8000-000000000099",
  "username": "sdk.testuser",
  "firstName": "SDK",
  "lastName": "TestUser",
  "email": "sdk-test@example.com",
  "applicationIds": [
    "a018836f-a909-4be0-a28b-53b413f1429c"
  ],
  "roles": [
    {
      "applicationId": "a018836f-a909-4be0-a28b-53b413f1429c",
      "role": "developer"
    }
  ],
  "defaultRole": {
    "role": "developer"
  },
  "createdAt": "2026-08-10T22:54:16.796Z",
  "updatedAt": "2026-08-10T22:54:16.796Z",
  "updatedBy": "deploy-ci-bot"
}
```

### Errors
<a name="acxd-users-createuser-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetUser
<a name="acxd-users-getuser"></a>

Gets a single user by ID.

### Input
<a name="acxd-users-getuser-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 

### Sample Request
<a name="acxd-users-getuser-sample-request"></a>

```
await client.send(new GetUserCommand({
  userId: "00000000-0000-4000-8000-000000000099",
}));
```

### Output
<a name="acxd-users-getuser-output"></a>

```
{
  "userId": "00000000-0000-4000-8000-000000000099",
  "cxnRole": "member",
  "userArn": "arn:aws:connect:us-west-2:<account-id>:instance/cb0ac315-73ce-4def-a2cc-cf3caf9866cc/agent/00000000-0000-4000-8000-000000000099",
  "username": "sdk.testuser",
  "firstName": "SDK",
  "lastName": "TestUser",
  "email": "sdk-test@example.com",
  "applicationIds": [
    "a018836f-a909-4be0-a28b-53b413f1429c"
  ],
  "roles": [
    {
      "applicationId": "a018836f-a909-4be0-a28b-53b413f1429c",
      "role": "developer"
    }
  ],
  "defaultRole": {
    "role": "developer"
  },
  "createdAt": "2026-08-10T22:54:16.796Z",
  "updatedAt": "2026-08-10T22:54:16.796Z",
  "updatedBy": "deploy-ci-bot"
}
```

### Errors
<a name="acxd-users-getuser-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateUser
<a name="acxd-users-updateuser"></a>

Updates a user. Only include fields you want to change.

### Input
<a name="acxd-users-updateuser-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 
| cxnRole | string | No | 
| userArn | string | No | 
| firstName | string | No | 
| lastName | string | No | 
| email | string | No | 
| applicationIds | array | No | 
| roles | array | No | 
| defaultRole | object | No | 

### Sample Request
<a name="acxd-users-updateuser-sample-request"></a>

```
await client.send(new UpdateUserCommand({
  userId: "00000000-0000-4000-8000-000000000099",
  cxnRole: "member",
  userArn: "arn:aws:connect:us-west-2:<account-id>:instance/cb0ac315-73ce-4def-a2cc-cf3caf9866cc/agent/00000000-0000-4000-8000-000000000099",
  firstName: "SDKUpdated",
  lastName: "TestUser",
  email: "sdk-test@example.com",
  applicationIds: ["a018836f-a909-4be0-a28b-53b413f1429c"],
  roles: [
    { applicationId: "a018836f-a909-4be0-a28b-53b413f1429c", role: "developer" },
  ],
  defaultRole: { role: "contentManager" },
}));
```

### Output
<a name="acxd-users-updateuser-output"></a>

```
{
  "userId": "00000000-0000-4000-8000-000000000099",
  "cxnRole": "member",
  "userArn": "arn:aws:connect:us-west-2:<account-id>:instance/cb0ac315-73ce-4def-a2cc-cf3caf9866cc/agent/00000000-0000-4000-8000-000000000099",
  "username": "sdk.testuser",
  "firstName": "SDKUpdated",
  "lastName": "TestUser",
  "email": "sdk-test@example.com",
  "applicationIds": [
    "a018836f-a909-4be0-a28b-53b413f1429c"
  ],
  "roles": [
    {
      "applicationId": "a018836f-a909-4be0-a28b-53b413f1429c",
      "role": "developer"
    }
  ],
  "defaultRole": {
    "role": "contentManager"
  },
  "createdAt": "2026-08-10T22:54:16.796Z",
  "updatedAt": "2026-08-10T22:54:20.530Z",
  "updatedBy": "deploy-ci-bot"
}
```

### Errors
<a name="acxd-users-updateuser-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## DeleteUser
<a name="acxd-users-deleteuser"></a>

Deletes a user.

### Input
<a name="acxd-users-deleteuser-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 

### Sample Request
<a name="acxd-users-deleteuser-sample-request"></a>

```
await client.send(new DeleteUserCommand({
  userId: created.userId,
}));
```

### Output
<a name="acxd-users-deleteuser-output"></a>

No response body.

### Errors
<a name="acxd-users-deleteuser-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-users-request-parameters"></a>

`userId`  
Type: String  
The user identifier.

`cxnRole`  
Type: String  
The user's account-level role. One of: `member`, `administrator`, `owner`.

`userArn`  
Type: String  
The user's Amazon Connect ARN.

`username`  
Type: String  
Username. 1–128 characters.

`firstName`  
Type: String  
First name. 1–36 characters.

`lastName`  
Type: String  
Last name. Max 36 characters.

`email`  
Type: String  
Email address. 3–256 characters.

`applicationIds`  
Type: Array  
Workspace IDs the user can access.

`roles`  
Type: Array  
Per-workspace role assignments. See User Role Assignment.

`defaultRole`  
Type: Object  
Default role when no workspace-specific role applies. See Default Role.

`createdAt`  
Type: String  
When the user was created (ISO 8601).

`updatedAt`  
Type: String  
When the user was last modified (ISO 8601).

`updatedBy`  
Type: String  
The identity of who last modified the user.

`nextToken`  
Type: String  
Pagination token. See Common Types.

`maxResults`  
Type: Integer  
Max items per page (1–100). See Common Types.

## User Role Assignment
<a name="acxd-users-user-role-assignment"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| applicationId | string | Yes | 
| role | string | Yes | 
| roleId | string | No | 

`applicationId`  
Type: String  
The workspace this assignment applies to.

`role`  
Type: String  
Pre-defined role name. One of: `administrator`, `developer`, `contentManager`, `readOnly`.

`roleId`  
Type: String  
Custom role ID (alternative to `role`). Created via the Roles API.

## Default Role
<a name="acxd-users-default-role"></a>

The fallback role applied when the user accesses a workspace without a specific role assignment.


| Field | Type | Required | 
| --- | --- | --- | 
| role | string | Yes | 
| roleId | string | No | 

`role`  
Type: String  
Pre-defined role name. One of: `administrator`, `developer`, `contentManager`, `readOnly`.

`roleId`  
Type: String  
Custom role ID (alternative to `role`).