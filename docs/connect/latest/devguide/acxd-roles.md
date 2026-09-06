

# Roles
<a name="acxd-roles"></a>

Manage permission roles that can be assigned to programmatic users. Roles define what actions a user can perform within a workspace.

**Topics**
+ [ListRoles](#acxd-roles-listroles)
+ [CreateRole](#acxd-roles-createrole)
+ [GetRole](#acxd-roles-getrole)
+ [UpdateRole](#acxd-roles-updaterole)
+ [DeleteRole](#acxd-roles-deleterole)
+ [GetRolePermissions](#acxd-roles-getrolepermissions)
+ [Request Parameters](#acxd-roles-request-parameters)
+ [Role Permission](#acxd-roles-role-permission)
+ [Condition Catalog](#acxd-roles-condition-catalog)

## ListRoles
<a name="acxd-roles-listroles"></a>

Lists all roles.

### Input
<a name="acxd-roles-listroles-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| type | string | No | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-roles-listroles-sample-request"></a>

```
await client.send(new ListRolesCommand({}));
```

### Output
<a name="acxd-roles-listroles-output"></a>

```
{
  "items": [
    {
      "roleId": "role-a1b2c3d4-5678-90ab-cdef-1234567890ab",
      "name": "Content Editor",
      "type": "studio",
      "description": "Can edit flows and knowledge bases but cannot deploy",
      "permissions": [
        { "permissionId": "ds:ListFlows", "effect": "allow" },
        { "permissionId": "ds:CreateFlow", "effect": "allow" },
        { "permissionId": "ds:UpdateFlow", "effect": "allow" },
        { "permissionId": "ds:DeleteFlow", "effect": "allow" },
        { "permissionId": "ds:CreateApplicationDeployment", "effect": "deny" }
      ],
      "conditionCatalog": [],
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "updatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-roles-listroles-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateRole
<a name="acxd-roles-createrole"></a>

Creates a new custom role.

### Input
<a name="acxd-roles-createrole-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| type | string | No | 
| description | string | No | 
| permissions | array | No | 
| conditionCatalog | array | No | 

### Sample Request
<a name="acxd-roles-createrole-sample-request"></a>

```
await client.send(new CreateRoleCommand({
  name: "Content Editor",
  type: "studio",
  description: "Can edit flows but cannot deploy",
  permissions: [
    { permissionId: "ds:ListFlows", effect: "allow" },
    { permissionId: "ds:CreateFlow", effect: "allow" },
    { permissionId: "ds:UpdateFlow", effect: "allow" },
    { permissionId: "ds:DeleteFlow", effect: "allow" },
    { permissionId: "ds:CreateApplicationDeployment", effect: "deny" },
  ],
  conditionCatalog: [],
}));
```

### Output
<a name="acxd-roles-createrole-output"></a>

```
{
  "roleId": "a80d56c4-3829-4f63-9500-13948d0fea87",
  "name": "Content Editor",
  "type": "studio",
  "description": "Can edit flows but cannot deploy",
  "permissions": [
    { "permissionId": "ds:ListFlows", "effect": "allow" },
    { "permissionId": "ds:CreateFlow", "effect": "allow" },
    { "permissionId": "ds:UpdateFlow", "effect": "allow" },
    { "permissionId": "ds:DeleteFlow", "effect": "allow" },
    { "permissionId": "ds:CreateApplicationDeployment", "effect": "deny" }
  ],
  "conditionCatalog": [],
  "createdAt": "2026-08-10T20:35:16.003Z",
  "updatedAt": "2026-08-10T20:35:16.003Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-roles-createrole-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetRole
<a name="acxd-roles-getrole"></a>

Gets a single role by ID.

### Input
<a name="acxd-roles-getrole-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| roleId | string | Yes | 

### Sample Request
<a name="acxd-roles-getrole-sample-request"></a>

```
await client.send(new GetRoleCommand({
  roleId: "a80d56c4-3829-4f63-9500-13948d0fea87",
}));
```

### Output
<a name="acxd-roles-getrole-output"></a>

```
{
  "roleId": "a80d56c4-3829-4f63-9500-13948d0fea87",
  "name": "Content Editor",
  "type": "studio",
  "description": "Can edit flows but cannot deploy",
  "permissions": [
    { "permissionId": "ds:ListFlows", "effect": "allow" },
    { "permissionId": "ds:CreateFlow", "effect": "allow" },
    { "permissionId": "ds:UpdateFlow", "effect": "allow" },
    { "permissionId": "ds:DeleteFlow", "effect": "allow" },
    { "permissionId": "ds:CreateApplicationDeployment", "effect": "deny" }
  ],
  "conditionCatalog": [],
  "createdAt": "2026-08-10T20:35:16.003Z",
  "updatedAt": "2026-08-10T20:35:16.003Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-roles-getrole-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateRole
<a name="acxd-roles-updaterole"></a>

Updates an existing role. Only include fields you want to change.

### Input
<a name="acxd-roles-updaterole-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| roleId | string | Yes | 
| name | string | No | 
| type | string | No | 
| description | string | No | 
| permissions | array | No | 
| conditionCatalog | array | No | 

### Sample Request
<a name="acxd-roles-updaterole-sample-request"></a>

```
await client.send(new UpdateRoleCommand({
  roleId: "a80d56c4-3829-4f63-9500-13948d0fea87",
  name: "Content Editor",
  type: "studio",
  description: "Updated - content editor with KB access",
  permissions: [
    { permissionId: "ds:ListFlows", effect: "allow" },
    { permissionId: "ds:CreateFlow", effect: "allow" },
    { permissionId: "ds:UpdateFlow", effect: "allow" },
    { permissionId: "ds:DeleteFlow", effect: "allow" },
    { permissionId: "ds:ListKnowledgeBases", effect: "allow" },
    { permissionId: "ds:CreateApplicationDeployment", effect: "deny" },
  ],
  conditionCatalog: [],
}));
```

### Output
<a name="acxd-roles-updaterole-output"></a>

```
{
  "roleId": "a80d56c4-3829-4f63-9500-13948d0fea87",
  "name": "Content Editor",
  "type": "studio",
  "description": "Updated - content editor with KB access",
  "permissions": [
    { "permissionId": "ds:ListFlows", "effect": "allow" },
    { "permissionId": "ds:CreateFlow", "effect": "allow" },
    { "permissionId": "ds:UpdateFlow", "effect": "allow" },
    { "permissionId": "ds:DeleteFlow", "effect": "allow" },
    { "permissionId": "ds:ListKnowledgeBases", "effect": "allow" },
    { "permissionId": "ds:CreateApplicationDeployment", "effect": "deny" }
  ],
  "conditionCatalog": [],
  "createdAt": "2026-08-10T20:35:16.003Z",
  "updatedAt": "2026-08-10T20:35:16.003Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-roles-updaterole-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## DeleteRole
<a name="acxd-roles-deleterole"></a>

Deletes a custom role. Fails if the role is still assigned to programmatic users.

### Input
<a name="acxd-roles-deleterole-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| roleId | string | Yes | 

### Sample Request
<a name="acxd-roles-deleterole-sample-request"></a>

```
await client.send(new DeleteRoleCommand({
    roleId: created.roleId,
}));
```

### Output
<a name="acxd-roles-deleterole-output"></a>

No response body.

### Errors
<a name="acxd-roles-deleterole-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `ConflictException` (409) role still assigned to users
+ `InternalServerException` (500)

## GetRolePermissions
<a name="acxd-roles-getrolepermissions"></a>

Gets the list of all available permissions that can be assigned to roles.

### Input
<a name="acxd-roles-getrolepermissions-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| type | string | Yes | 

### Sample Request
<a name="acxd-roles-getrolepermissions-sample-request"></a>

```
await client.send(new GetRolePermissionsCommand({
  type: "studio",
}));
```

### Output
<a name="acxd-roles-getrolepermissions-output"></a>

```
{
  "permissions": [
    { "permissionId": "ds:ListApplications", "effect": "allow" },
    { "permissionId": "ds:CreateApplication", "effect": "allow" },
    { "permissionId": "ds:GetApplication", "effect": "allow" },
    { "permissionId": "ds:ListFlows", "effect": "allow" },
    { "permissionId": "ds:CreateFlow", "effect": "allow" },
    { "permissionId": "ds:UpdateFlow", "effect": "allow" },
    { "permissionId": "ds:DeleteFlow", "effect": "allow" },
    { "permissionId": "ds:ListDataRequests", "effect": "allow" },
    { "permissionId": "ds:CreateDataRequest", "effect": "allow" },
    { "permissionId": "ds:ListSlotTypes", "effect": "allow" },
    { "permissionId": "ds:CreateApplicationDeployment", "effect": "allow" },
    { "permissionId": "ds:ListKnowledgeBases", "effect": "allow" }
  ]
}
```

### Errors
<a name="acxd-roles-getrolepermissions-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-roles-request-parameters"></a>

`roleId`  
Type: String  
The role ID.

`name`  
Type: String  
Role name. Alphanumeric \+ spaces/dashes, 3–36 characters.

`type`  
Type: String  
The role type. One of: `studio`, `voicecompass`, `voiceinsights`.

`description`  
Type: String  
Role description. Max 200 characters.

`permissions`  
Type: Array  
Permission assignments. See Role Permission.

`conditionCatalog`  
Type: Array  
Conditional permission rules for fine-grained access control. See Condition Catalog.

`nextToken`  
Type: String  
Pagination token. See Common Types.

`maxResults`  
Type: Integer  
Max items per page (1–100). See Common Types.

`createdAt`  
Type: String  
When the role was created (ISO 8601).

`updatedAt`  
Type: String  
When the role was last modified (ISO 8601).

`updatedBy`  
Type: String  
The identity of who last modified the role.

## Role Permission
<a name="acxd-roles-role-permission"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| permissionId | string | Yes | 
| effect | string | Yes | 
| conditionId | string | No | 

`permissionId`  
Type: String  
The permission identifier (e.g., `ds:CreateFlow`, `ds:ListApplications`). Use GetRolePermissions to discover available values.

`effect`  
Type: String  
Whether to allow or deny this permission. One of: `allow`, `deny`.

`conditionId`  
Type: String  
Optional reference to a condition in the condition catalog. When present, the permission only applies when the condition is met.

## Condition Catalog
<a name="acxd-roles-condition-catalog"></a>

Conditions enable fine-grained access control (e.g., restrict a user to specific languages or resources).


| Field | Type | Required | 
| --- | --- | --- | 
| categoryId | string | No | 
| subcategoryId | string | No | 
| conditionId | string | No | 
| conditions | object | No | 

`categoryId`  
Type: String  
Category grouping for the condition.

`subcategoryId`  
Type: String  
Subcategory grouping.

`conditionId`  
Type: String  
Unique condition ID. Referenced by permissions via `conditionId`.

`conditions`  
Type: Object  
The condition logic. Either a single condition or a composite:  
Single condition:  

```
{
  "condition": {
    "left": { "type": "languageCode", "value": "" },
    "right": { "type": "constant", "value": "en-US" },
    "operator": "EQ"
  }
}
```
Composite condition (multiple conditions combined):  

```
{
  "composite": {
    "operator": "OR",
    "items": [
      { "condition": { "left": { "type": "languageCode" }, "right": { "type": "constant", "value": "en-US" }, "operator": "EQ" } },
      { "condition": { "left": { "type": "languageCode" }, "right": { "type": "constant", "value": "es-ES" }, "operator": "EQ" } }
    ]
  }
}
```

### Condition Operand Types
<a name="acxd-roles-condition-operand-types"></a>


| Type | Description | 
| --- | --- | 
| languageCode | The language of the resource being accessed | 
| resourceId | The ID of the resource being accessed | 
| constant | A literal value to compare against | 

### Condition Operators
<a name="acxd-roles-condition-operators"></a>


| Operator | Description | 
| --- | --- | 
| EQ | Equals | 
| NEQ | Not equals | 
| PREFIX | Starts with | 
| NOT\_PREFIX | Does not start with | 
| SUFFIX | Ends with | 
| NOT\_SUFFIX | Does not end with | 
| CONTAINS | Contains | 
| NOT\_CONTAINS | Does not contain | 

### Boolean Operators
<a name="acxd-roles-boolean-operators"></a>


| Operator | Description | 
| --- | --- | 
| AND | All conditions must be true | 
| OR | At least one condition must be true | 