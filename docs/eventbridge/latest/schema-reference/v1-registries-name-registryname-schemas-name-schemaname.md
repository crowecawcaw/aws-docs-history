

# Schema
<a name="v1-registries-name-registryname-schemas-name-schemaname"></a>

## URI
<a name="v1-registries-name-registryname-schemas-name-schemaname-url"></a>

`/v1/registries/name/{{registryName}}/schemas/name/{{schemaName}}`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-name-schemaname-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-name-schemanameget"></a>

**Operation ID:** `DescribeSchema`

Retrieve the schema definition.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| schemaVersion | String | False | Specifying this limits the results to only this schema version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | DescribeSchemaOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### POST
<a name="v1-registries-name-registryname-schemas-name-schemanamepost"></a>

**Operation ID:** `CreateSchema`

Creates a schema definition.

**Note**  
Inactive schemas will be deleted after two years.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 201 | SchemaOutput | 201 response | 
| 400 | ErrorOutput | 400 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### PUT
<a name="v1-registries-name-registryname-schemas-name-schemanameput"></a>

**Operation ID:** `UpdateSchema`

Updates the schema definition

**Note**  
Inactive schemas will be deleted after two years.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | SchemaOutput | 200 response | 
| 304 | None | 304 response | 
| 400 | ErrorOutput | 400 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### DELETE
<a name="v1-registries-name-registryname-schemas-name-schemanamedelete"></a>

**Operation ID:** `DeleteSchema`

Delete a schema definition.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


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
<a name="v1-registries-name-registryname-schemas-name-schemanameoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-name-registryname-schemas-name-schemaname-schemas"></a>

### Request bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-request-examples"></a>

#### POST schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-request-body-post-example"></a>

```
{
  "Type": enum,
  "Description": "string",
  "Content": "string",
  "tags": {
  }
}
```

#### PUT schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-request-body-put-example"></a>

```
{
  "Type": enum,
  "Description": "string",
  "ClientTokenId": "string",
  "Content": "string"
}
```

### Response bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-response-examples"></a>

#### DescribeSchemaOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-response-body-describeschemaoutput-example"></a>

```
{
  "LastModified": "string",
  "Type": "string",
  "Description": "string",
  "SchemaVersion": "string",
  "Content": "string",
  "VersionCreatedDate": "string",
  "SchemaArn": "string",
  "SchemaName": "string",
  "tags": {
  }
}
```

#### SchemaOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-response-body-schemaoutput-example"></a>

```
{
  "LastModified": "string",
  "Type": "string",
  "Description": "string",
  "SchemaVersion": "string",
  "VersionCreatedDate": "string",
  "SchemaArn": "string",
  "SchemaName": "string",
  "tags": {
  }
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-name-schemaname-properties"></a>

### CreateSchemaInput
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-createschemainput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Content | string<br />MinLength: 1<br />MaxLength: 100000 | True | The source of the schema definition. | 
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | A description of the schema. | 
| tags | [Tags](#v1-registries-name-registryname-schemas-name-schemaname-model-tags) | False | Tags associated with the schema. | 
| Type | [Type](#v1-registries-name-registryname-schemas-name-schemaname-model-type) | True | The type of schema.<br />Valid types include `OpenApi3` and `JSONSchemaDraft4`. | 

### DescribeSchemaOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-describeschemaoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Content | string | False | The source of the schema definition. | 
| Description | string | False | The description of the schema. | 
| LastModified | string<br />Format: date-time | False | The date and time that schema was modified. | 
| SchemaArn | string | False | The ARN of the schema. | 
| SchemaName | string | False | The name of the schema. | 
| SchemaVersion | string | False | The version number of the schema | 
| tags | [Tags](#v1-registries-name-registryname-schemas-name-schemaname-model-tags) | False | Tags associated with the resource. | 
| Type | string | False | The type of the schema.<br />Valid types include `OpenApi3` and `JSONSchemaDraft4`. | 
| VersionCreatedDate | string<br />Format: date-time | False | The date the schema version was created. | 

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### SchemaOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-schemaoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Description | string | False | The description of the schema. | 
| LastModified | string<br />Format: date-time | False | The date and time that schema was modified. | 
| SchemaArn | string | False | The ARN of the schema. | 
| SchemaName | string | False | The name of the schema. | 
| SchemaVersion | string | False | The version number of the schema | 
| tags | [Tags](#v1-registries-name-registryname-schemas-name-schemaname-model-tags) | False |  | 
| Type | string | False | The type of the schema.<br />Valid types include `OpenApi3` and `JSONSchemaDraft4`. | 
| VersionCreatedDate | string<br />Format: date-time | False | The date the schema version was created. | 

### Tags
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 

### Type
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-type"></a>

The type of schema to export.
+ `OpenApi3`
+ `JSONSchemaDraft4`

### UpdateSchemaInput
<a name="v1-registries-name-registryname-schemas-name-schemaname-model-updateschemainput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| ClientTokenId | string<br />MinLength: 0<br />MaxLength: 36 | False | The ID of the client token. | 
| Content | string<br />MinLength: 1<br />MaxLength: 100000 | False | The source of the schema definition. | 
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | The description of the schema. | 
| Type | [Type](#v1-registries-name-registryname-schemas-name-schemaname-model-type) | False | The schema type for the events schema.<br />Valid types include `OpenApi3` and `JSONSchemaDraft4`. | 