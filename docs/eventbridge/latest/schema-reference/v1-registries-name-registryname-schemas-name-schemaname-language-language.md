

# Code Binding
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language"></a>

## URI
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-url"></a>

`/v1/registries/name/{{registryName}}/schemas/name/{{schemaName}}/language/{{language}}`

## HTTP methods
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-http-methods"></a>

### GET
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-languageget"></a>

**Operation ID:** `DescribeCodeBinding`

Describe the code binding URI.


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
| 200 | CodeBindingOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 429 | ErrorOutput | 429 response | 
| 500 | ErrorOutput | 500 response | 

### POST
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-languagepost"></a>

**Operation ID:** `PutCodeBinding`

Put code binding URI


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
| 202 | CodeBindingOutput | 202 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 410 | ErrorOutput | 410 response | 
| 429 | ErrorOutput | 429 response | 
| 500 | ErrorOutput | 500 response | 

### OPTIONS
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-languageoptions"></a>


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
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-schemas"></a>

### Response bodies
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-response-examples"></a>

#### CodeBindingOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-response-body-codebindingoutput-example"></a>

```
{
  "Status": enum,
  "LastModified": "string",
  "CreationDate": "string",
  "SchemaVersion": "string"
}
```

#### ErrorOutput schema
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-properties"></a>

### CodeBindingOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-model-codebindingoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CreationDate | string<br />Format: date-time | False | The time and date that the code binding was created. | 
| LastModified | string<br />Format: date-time | False | The date and time that code bindings were modified. | 
| SchemaVersion | string | False | The version number of the schema. | 
| Status | [CodeGenerationStatus](#v1-registries-name-registryname-schemas-name-schemaname-language-language-model-codegenerationstatus) | False | The current status of code binding generation. | 

### CodeGenerationStatus
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-model-codegenerationstatus"></a>
+ `CREATE_IN_PROGRESS`
+ `CREATE_COMPLETE`
+ `CREATE_FAILED`

### ErrorOutput
<a name="v1-registries-name-registryname-schemas-name-schemaname-language-language-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 