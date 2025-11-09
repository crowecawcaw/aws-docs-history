# Policy

The resource-based policy.

## URI

`/v1/policy`

## HTTP methods

### GET

**Operation ID:** `GetResourcePolicy`

Retrieves the resource-based policy attached to a given registry.

| Query parameters | Name   | Type  | Required                  | Description |
| ---------------- | ------ | ----- | ------------------------- | ----------- |
| `registryName`   | String | False | The name of the registry. |

| Responses | Status code               | Response model                     | Description |
| --------- | ------------------------- | ---------------------------------- | ----------- |
| `200`     | `GetResourcePolicyOutput` | Get Resource-Based Policy Response |
| `400`     | `ErrorOutput`             | 400 response                       |
| `401`     | `ErrorOutput`             | 401 response                       |
| `403`     | `ErrorOutput`             | 403 response                       |
| `404`     | `ErrorOutput`             | 404 response                       |
| `500`     | `ErrorOutput`             | 500 response                       |
| `503`     | `ErrorOutput`             | 503 response                       |

### PUT

**Operation ID:** `PutResourcePolicy`

The name of the policy.

| Query parameters | Name   | Type  | Required                  | Description |
| ---------------- | ------ | ----- | ------------------------- | ----------- |
| `registryName`   | String | False | The name of the registry. |

| Responses | Status code               | Response model | Description |
| --------- | ------------------------- | -------------- | ----------- |
| `200`     | `PutResourcePolicyOutput` | 200 response   |
| `400`     | `ErrorOutput`             | 400 response   |
| `401`     | `ErrorOutput`             | 401 response   |
| `403`     | `ErrorOutput`             | 403 response   |
| `404`     | `ErrorOutput`             | 404 response   |
| `412`     | `ErrorOutput`             | 412 response   |
| `500`     | `ErrorOutput`             | 500 response   |
| `503`     | `ErrorOutput`             | 503 response   |

### DELETE

**Operation ID:** `DeleteResourcePolicy`

Delete the resource-based policy attached to the specified registry.

| Query parameters | Name   | Type  | Required                  | Description |
| ---------------- | ------ | ----- | ------------------------- | ----------- |
| `registryName`   | String | False | The name of the registry. |

| Responses | Status code   | Response model | Description |
| --------- | ------------- | -------------- | ----------- |
| `204`     | None          | 204 response   |
| `400`     | `ErrorOutput` | 400 response   |
| `401`     | `ErrorOutput` | 401 response   |
| `403`     | `ErrorOutput` | 403 response   |
| `404`     | `ErrorOutput` | 404 response   |
| `500`     | `ErrorOutput` | 500 response   |
| `503`     | `ErrorOutput` | 503 response   |

### OPTIONS

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Request bodies

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

### Response bodies

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties

### ErrorOutput

| Property  | Type   | Required | Description                             |
| --------- | ------ | -------- | --------------------------------------- |
| `Code`    | string | True     | The error code.                         |
| `Message` | string | True     | The message string of the error output. |

### GetResourcePolicyOutput

Information about the policy.

| Property     | Type   | Required | Description                |
| ------------ | ------ | -------- | -------------------------- |
| `Policy`     | string | False    | The resource-based policy. |
| `RevisionId` | string | False    | The revision ID.           |

### PutResourcePolicyInput

Only update the policy if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.

| Property     | Type   | Required | Description                    |
| ------------ | ------ | -------- | ------------------------------ |
| `Policy`     | string | True     | The resource-based policy.     |
| `RevisionId` | string | False    | The revision ID of the policy. |

### PutResourcePolicyOutput

The resource-based policy.

| Property     | Type   | Required | Description                    |
| ------------ | ------ | -------- | ------------------------------ |
| `Policy`     | string | False    | The resource-based policy.     |
| `RevisionId` | string | False    | The revision ID of the policy. |
