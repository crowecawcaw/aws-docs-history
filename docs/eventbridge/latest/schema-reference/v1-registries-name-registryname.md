

# Registry
<a name="v1-registries-name-registryname"></a>

## URI
<a name="v1-registries-name-registryname-url"></a>

`/v1/registries/name/{{registryName}}`

## HTTP methods
<a name="v1-registries-name-registryname-http-methods"></a>

### GET
<a name="v1-registries-name-registrynameget"></a>

**Operation ID:** `DescribeRegistry`

Describes the registry.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | RegistryOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### POST
<a name="v1-registries-name-registrynamepost"></a>

**Operation ID:** `CreateRegistry`

Creates a registry.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 201 | RegistryOutput | 201 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 409 | ErrorOutput | 409 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### PUT
<a name="v1-registries-name-registrynameput"></a>

**Operation ID:** `UpdateRegistry`


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | RegistryOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### DELETE
<a name="v1-registries-name-registrynamedelete"></a>

**Operation ID:** `DeleteRegistry`

Deletes a Registry.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


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
<a name="v1-registries-name-registrynameoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-name-registryname-schemas"></a>

### Request bodies
<a name="v1-registries-name-registryname-request-examples"></a>

#### POST schema
<a name="v1-registries-name-registryname-request-body-post-example"></a>

```
{
  "Description": "string",
  "tags": {
  }
}
```

#### PUT schema
<a name="v1-registries-name-registryname-request-body-put-example"></a>

```
{
  "Description": "string"
}
```

### Response bodies
<a name="v1-registries-name-registryname-response-examples"></a>

#### RegistryOutput schema
<a name="v1-registries-name-registryname-response-body-registryoutput-example"></a>

```
{
  "Description": "string",
  "RegistryName": "string",
  "RegistryArn": "string",
  "tags": {
  }
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-properties"></a>

### CreateRegistryInput
<a name="v1-registries-name-registryname-model-createregistryinput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | A description of the registry to be created. | 
| tags | [Tags](#v1-registries-name-registryname-model-tags) | False | Tags to associate with the registry. | 

### ErrorOutput
<a name="v1-registries-name-registryname-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### RegistryOutput
<a name="v1-registries-name-registryname-model-registryoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Description | string | False | The description of the registry. | 
| RegistryArn | string | False | The ARN of the registry. | 
| RegistryName | string | False | The name of the registry. | 
| tags | [Tags](#v1-registries-name-registryname-model-tags) | False | Tags associated with the registry. | 

### Tags
<a name="v1-registries-name-registryname-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 

### UpdateRegistryInput
<a name="v1-registries-name-registryname-model-updateregistryinput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | The description of the registry to update. | 