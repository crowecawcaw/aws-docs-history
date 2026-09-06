

# Describe or Update Discoverer
<a name="v1-discoverers-id-discovererid"></a>

## URI
<a name="v1-discoverers-id-discovererid-url"></a>

`/v1/discoverers/id/{{discovererId}}`

## HTTP methods
<a name="v1-discoverers-id-discovererid-http-methods"></a>

### GET
<a name="v1-discoverers-id-discovereridget"></a>

**Operation ID:** `DescribeDiscoverer`

Describes the discoverer.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | DiscovererOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### PUT
<a name="v1-discoverers-id-discovereridput"></a>

**Operation ID:** `UpdateDiscoverer`

Updates the discoverer


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | DiscovererOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### DELETE
<a name="v1-discoverers-id-discovereriddelete"></a>

**Operation ID:** `DeleteDiscoverer`

Deletes a discoverer.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


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
<a name="v1-discoverers-id-discovereridoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-discoverers-id-discovererid-schemas"></a>

### Request bodies
<a name="v1-discoverers-id-discovererid-request-examples"></a>

#### PUT schema
<a name="v1-discoverers-id-discovererid-request-body-put-example"></a>

```
{
  "CrossAccount": boolean,
  "Description": "string"
}
```

### Response bodies
<a name="v1-discoverers-id-discovererid-response-examples"></a>

#### DiscovererOutput schema
<a name="v1-discoverers-id-discovererid-response-body-discovereroutput-example"></a>

```
{
  "DiscovererArn": "string",
  "DiscovererId": "string",
  "CrossAccount": boolean,
  "Description": "string",
  "SourceArn": "string",
  "State": enum,
  "tags": {
  }
}
```

#### ErrorOutput schema
<a name="v1-discoverers-id-discovererid-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-discoverers-id-discovererid-properties"></a>

### DiscovererOutput
<a name="v1-discoverers-id-discovererid-model-discovereroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CrossAccount | boolean | False | Whether cross-account events are discovered. | 
| Description | string | False | The description of the discoverer. | 
| DiscovererArn | string | False | The ARN of the discoverer. | 
| DiscovererId | string | False | The ID of the discoverer. | 
| SourceArn | string | False | The ARN of the event bus. | 
| State | [DiscovererState](#v1-discoverers-id-discovererid-model-discovererstate) | False | The state of the discoverer. | 
| tags | [Tags](#v1-discoverers-id-discovererid-model-tags) | False | Tags associated with the resource. | 

### DiscovererState
<a name="v1-discoverers-id-discovererid-model-discovererstate"></a>
+ `STARTED`
+ `STOPPED`

### ErrorOutput
<a name="v1-discoverers-id-discovererid-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### Tags
<a name="v1-discoverers-id-discovererid-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 

### UpdateDiscovererInput
<a name="v1-discoverers-id-discovererid-model-updatediscovererinput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CrossAccount | boolean | False |  | 
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | The description of the discoverer to update. | 