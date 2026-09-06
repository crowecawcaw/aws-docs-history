

# Schemas
<a name="v1-registries-name-registryname-schemas"></a>

## URI
<a name="v1-registries-name-registryname-schemas-url"></a>

`/v1/registries/name/{{registryName}}/schemas`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemasget"></a>

**Operation ID:** `ListSchemas`

List the schemas.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| schemaNamePrefix | String | False | Specifying this limits the results to only those schema names that start with the specified prefix. | 
| limit | String | False | The maximum number of results to return per page. | 
| nextToken | String | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ListSchemasOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemasoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-name-registryname-schemas-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-response-examples"></a>

#### ListSchemasOutput schema
<a name="v1-registries-name-registryname-schemas-response-body-listschemasoutput-example"></a>

```
{
  "NextToken": "string",
  "Schemas": [
    {
      "LastModified": "string",
      "VersionCount": integer,
      "SchemaName": "string",
      "SchemaArn": "string",
      "tags": {
      }
    }
  ]
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-properties"></a>

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ListSchemasOutput
<a name="v1-registries-name-registryname-schemas-model-listschemasoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| NextToken | string | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| Schemas | Array of type [SchemaSummary](#v1-registries-name-registryname-schemas-model-schemasummary) | False | An array of schema summaries. | 

### SchemaSummary
<a name="v1-registries-name-registryname-schemas-model-schemasummary"></a>

A summary of schema details.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| LastModified | string<br />Format: date-time | False | The date and time that schema was modified. | 
| SchemaArn | string | False | The ARN of the schema. | 
| SchemaName | string | False | The name of the schema. | 
| tags | [Tags](#v1-registries-name-registryname-schemas-model-tags) | False | Tags associated with the schema. | 
| VersionCount | integer<br />Format: int64 | False | The number of versions available for the schema. | 

### Tags
<a name="v1-registries-name-registryname-schemas-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 