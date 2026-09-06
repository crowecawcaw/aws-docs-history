

# Export
<a name="v1-registries-name-registryname-schemas-name-schemaname-export"></a>

Exports a schema.

## URI
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-url"></a>

`/v1/registries/name/{{registryName}}/schemas/name/{{schemaName}}/export`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-name-schemaname-exportget"></a>

**Operation ID:** `ExportSchema`

Exports a schema.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| type | String | True | The type of schema to export. | 
| schemaVersion | String | False | Specifying this limits the results to only this schema version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ExportSchemaOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 429 | ErrorOutput | 429 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemas-name-schemaname-exportoptions"></a>


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
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-response-examples"></a>

#### ExportSchemaOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-response-body-exportschemaoutput-example"></a>

```
{
  "Type": "string",
  "SchemaVersion": "string",
  "Content": "string",
  "SchemaName": "string",
  "SchemaArn": "string"
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-properties"></a>

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ExportSchemaOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-export-model-exportschemaoutput"></a>

The schema to export.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Content | string | False | The content of the schema. | 
| SchemaArn | string | False | The ARN of the schema to export. | 
| SchemaName | string | False | The name of the schema to export. | 
| SchemaVersion | string | False | The version of the schema to export. | 
| Type | string | False | The type of schema to export. | 