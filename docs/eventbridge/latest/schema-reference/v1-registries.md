

# Registries
<a name="v1-registries"></a>

## URI
<a name="v1-registries-url"></a>

`/v1/registries`

## HTTP methods
<a name="v1-registries-http-methods"></a>

### GET
<a name="v1-registriesget"></a>

**Operation ID:** `ListRegistries`

List the registries.


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| scope | String | False | Can be set to `Local` or `AWS` to limit responses to your custom registries, or the ones provided by AWS. | 
| limit | String | False | The maximum number of results to return per page. | 
| nextToken | String | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| registryNamePrefix | String | False | Specifying this limits the results to only those registry names that start with the specified prefix. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ListRegistriesOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-registriesoptions"></a>


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-registries-schemas"></a>

### Response bodies
<a name="v1-registries-response-examples"></a>

#### ListRegistriesOutput schema
<a name="v1-registries-response-body-listregistriesoutput-example"></a>

```
{
  "NextToken": "string",
  "Registries": [
    {
      "RegistryName": "string",
      "RegistryArn": "string",
      "tags": {
      }
    }
  ]
}
```

#### ErrorOutput schema
<a name="v1-registries-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-registries-properties"></a>

### ErrorOutput
<a name="v1-registries-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ListRegistriesOutput
<a name="v1-registries-model-listregistriesoutput"></a>

List the registries.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| NextToken | string | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| Registries | Array of type [RegistrySummary](#v1-registries-model-registrysummary) | False | An array of registry summaries. | 

### RegistrySummary
<a name="v1-registries-model-registrysummary"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| RegistryArn | string | False | The ARN of the registry. | 
| RegistryName | string | False | The name of the registry. | 
| tags | [Tags](#v1-registries-model-tags) | False | Tags associated with the registry. | 

### Tags
<a name="v1-registries-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 