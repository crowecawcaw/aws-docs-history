

# Search Schemas
<a name="v1-registries-name-registryname-schemas-search"></a>

## URI
<a name="v1-registries-name-registryname-schemas-search-url"></a>

`/v1/registries/name/{{registryName}}/schemas/search`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-search-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-searchget"></a>

**Operation ID:** `SearchSchemas`

Search the schemas


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| keywords | String | True | Specifying this limits the results to only schemas that include the provided keywords. | 
| limit | String | False | The maximum number of results to return per page. | 
| nextToken | String | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | SearchSchemasOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemas-searchoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-name-registryname-schemas-search-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-search-response-examples"></a>

#### SearchSchemasOutput schema
<a name="v1-registries-name-registryname-schemas-search-response-body-searchschemasoutput-example"></a>

```
{
  "NextToken": "string",
  "Schemas": [
    {
      "Type": "string",
      "RegistryName": "string",
      "SchemaVersions": [
        {
          "SchemaVersion": "string",
          "CreatedDate": "string"
        }
      ],
      "SchemaName": "string",
      "SchemaArn": "string"
    }
  ]
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-search-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-search-properties"></a>

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-search-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### SearchSchemaSummary
<a name="v1-registries-name-registryname-schemas-search-model-searchschemasummary"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| RegistryName | string | False | The name of the registry. | 
| SchemaArn | string | False | The ARN of the schema. | 
| SchemaName | string | False | The name of the schema. | 
| SchemaVersions | Array of type [SearchSchemaVersionSummary](#v1-registries-name-registryname-schemas-search-model-searchschemaversionsummary) | False | An array of schema version summaries. | 
| Type | string | False | The type of schema to export.<br />Valid types include `OpenApi3` and `JSONSchemaDraft4`. | 

### SearchSchemaVersionSummary
<a name="v1-registries-name-registryname-schemas-search-model-searchschemaversionsummary"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CreatedDate | string<br />Format: date-time | False | The date the schema version was created. | 
| SchemaVersion | string | False | The version number of the schema | 

### SearchSchemasOutput
<a name="v1-registries-name-registryname-schemas-search-model-searchschemasoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| NextToken | string | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| Schemas | Array of type [SearchSchemaSummary](#v1-registries-name-registryname-schemas-search-model-searchschemasummary) | False | An array of `SearchSchemaSummary` information. | 