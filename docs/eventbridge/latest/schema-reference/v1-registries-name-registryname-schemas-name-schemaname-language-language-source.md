

# Get Code Binding Source
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source"></a>

## URI
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-url"></a>

`/v1/registries/name/{{registryName}}/schemas/name/{{schemaName}}/language/{{language}}/source`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-sourceget"></a>

**Operation ID:** `GetCodeBindingSource`

Get the code binding source URI.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 
| {{language}} | String | True | The language of the code binding. The supported languages and corresponding values are as follows:+  Java: Java8 <br />+  Python: Python36 <br />+  TypeScript: TypeScript3 <br />+  Golang: Go1  | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| schemaVersion | String | False | Specifying this limits the results to only this schema version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | GetCodeBindingSourceOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 429 | ErrorOutput | 429 response | 
| 500 | ErrorOutput | 500 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-sourceoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{registryName}} | String | True | The name of the schema registry. | 
| {{schemaName}} | String | True | The name of the schema. | 
| {{language}} | String | True | The language of the code binding. The supported languages and corresponding values are as follows:+  Java: Java8 <br />+  Python: Python36 <br />+  TypeScript: TypeScript3 <br />+  Golang: Go1  | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| schemaVersion | String | False | Specifying this limits the results to only this schema version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-response-examples"></a>

#### GetCodeBindingSourceOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-response-body-getcodebindingsourceoutput-example"></a>

```
"string"
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-properties"></a>

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-source-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 