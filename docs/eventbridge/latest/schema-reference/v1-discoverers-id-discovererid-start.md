

# Start Discoverer
<a name="v1-discoverers-id-discovererid-start"></a>

## URI
<a name="v1-discoverers-id-discovererid-start-url"></a>

`/v1/discoverers/id/{{discovererId}}/start`

## HTTP methods
<a name="v1-discoverers-id-discovererid-start-http-methods"></a>

### POST
<a name="v1-discoverers-id-discovererid-startpost"></a>

**Operation ID:** `StartDiscoverer`

Starts the discoverer


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | DiscovererStateOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-discoverers-id-discovererid-startoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-discoverers-id-discovererid-start-schemas"></a>

### Response bodies
<a name="v1-discoverers-id-discovererid-start-response-examples"></a>

#### DiscovererStateOutput schema
<a name="v1-discoverers-id-discovererid-start-response-body-discovererstateoutput-example"></a>

```
{
  "DiscovererId": "string",
  "State": enum
}
```

#### ErrorOutput schema
<a name="v1-discoverers-id-discovererid-start-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-discoverers-id-discovererid-start-properties"></a>

### DiscovererState
<a name="v1-discoverers-id-discovererid-start-model-discovererstate"></a>
+ `STARTED`
+ `STOPPED`

### DiscovererStateOutput
<a name="v1-discoverers-id-discovererid-start-model-discovererstateoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| DiscovererId | string | False | The ID of the discoverer. | 
| State | [DiscovererState](#v1-discoverers-id-discovererid-start-model-discovererstate) | False | The state of the discoverer. | 

### ErrorOutput
<a name="v1-discoverers-id-discovererid-start-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 