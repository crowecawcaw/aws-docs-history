

# Policy
<a name="v1-policy"></a>

The resource-based policy.

## URI
<a name="v1-policy-url"></a>

`/v1/policy`

## HTTP methods
<a name="v1-policy-http-methods"></a>

### GET
<a name="v1-policyget"></a>

**Operation ID:** `GetResourcePolicy`

Retrieves the resource-based policy attached to a given registry.


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| registryName | String | False | The name of the registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | GetResourcePolicyOutput | Get Resource-Based Policy Response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### PUT
<a name="v1-policyput"></a>

**Operation ID:** `PutResourcePolicy`

The name of the policy.


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| registryName | String | False | The name of the registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | PutResourcePolicyOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 412 | ErrorOutput | 412 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### DELETE
<a name="v1-policydelete"></a>

**Operation ID:** `DeleteResourcePolicy`

Delete the resource-based policy attached to the specified registry.


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| registryName | String | False | The name of the registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 204 | None | 204 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-policyoptions"></a>


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-policy-schemas"></a>

### Request bodies
<a name="v1-policy-request-examples"></a>

#### PUT schema
<a name="v1-policy-request-body-put-example"></a>

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

### Response bodies
<a name="v1-policy-response-examples"></a>

#### GetResourcePolicyOutput schema
<a name="v1-policy-response-body-getresourcepolicyoutput-example"></a>

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

#### PutResourcePolicyOutput schema
<a name="v1-policy-response-body-putresourcepolicyoutput-example"></a>

```
{
  "Policy": "string",
  "RevisionId": "string"
}
```

#### ErrorOutput schema
<a name="v1-policy-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-policy-properties"></a>

### ErrorOutput
<a name="v1-policy-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### GetResourcePolicyOutput
<a name="v1-policy-model-getresourcepolicyoutput"></a>

Information about the policy.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Policy | string | False | The resource-based policy. | 
| RevisionId | string | False | The revision ID. | 

### PutResourcePolicyInput
<a name="v1-policy-model-putresourcepolicyinput"></a>

Only update the policy if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Policy | string | True | The resource-based policy. | 
| RevisionId | string | False | The revision ID of the policy. | 

### PutResourcePolicyOutput
<a name="v1-policy-model-putresourcepolicyoutput"></a>

The resource-based policy.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Policy | string | False | The resource-based policy. | 
| RevisionId | string | False | The revision ID of the policy. | 