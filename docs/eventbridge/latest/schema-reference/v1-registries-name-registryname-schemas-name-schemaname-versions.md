

# List Schema Versions
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions"></a>

## URI
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-url"></a>

`/v1/registries/name/{{registryName}}/schemas/name/{{schemaName}}/versions`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-name-schemaname-versionsget"></a>

**Operation ID:** `ListSchemaVersions`

Provides a list of the schema versions and related information.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| limit | String | False | The maximum number of results to return per page. | 
| nextToken | String | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ListSchemaVersionsOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemas-name-schemaname-versionsoptions"></a>


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
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-response-examples"></a>

#### ListSchemaVersionsOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-response-body-listschemaversionsoutput-example"></a>

```
{
  "NextToken": "string",
  "SchemaVersions": [
    {
      "Type": "string",
      "SchemaVersion": "string",
      "SchemaName": "string",
      "SchemaArn": "string"
    }
  ]
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-properties"></a>

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ListSchemaVersionsOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-model-listschemaversionsoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| NextToken | string | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| SchemaVersions | Array of type [SchemaVersionSummary](#v1-registries-name-registryname-schemas-name-schemaname-versions-model-schemaversionsummary) | False | An array of schema version summaries. | 

### SchemaVersionSummary
<a name="v1-registries-name-registryname-schemas-name-schemaname-versions-model-schemaversionsummary"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| SchemaArn | string | False | The ARN of the schema version. | 
| SchemaName | string | False | The name of the schema. | 
| SchemaVersion | string | False | The version number of the schema. | 
| Type | string | False | The type of schema to export. | 