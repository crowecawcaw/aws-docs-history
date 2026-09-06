

# Stop Discoverer
<a name="v1-discoverers-id-discovererid-stop"></a>

## URI
<a name="v1-discoverers-id-discovererid-stop-url"></a>

`/v1/discoverers/id/{{discovererId}}/stop`

## HTTP methods
<a name="v1-discoverers-id-discovererid-stop-http-methods"></a>

### POST
<a name="v1-discoverers-id-discovererid-stoppost"></a>

**Operation ID:** `StopDiscoverer`

Stops the discoverer


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
<a name="v1-discoverers-id-discovererid-stopoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{discovererId}} | String | True | The ID of the discoverer. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-discoverers-id-discovererid-stop-schemas"></a>

### Response bodies
<a name="v1-discoverers-id-discovererid-stop-response-examples"></a>

#### DiscovererStateOutput schema
<a name="v1-discoverers-id-discovererid-stop-response-body-discovererstateoutput-example"></a>

```
{
  "DiscovererId": "string",
  "State": enum
}
```

#### ErrorOutput schema
<a name="v1-discoverers-id-discovererid-stop-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-discoverers-id-discovererid-stop-properties"></a>

### DiscovererState
<a name="v1-discoverers-id-discovererid-stop-model-discovererstate"></a>
+ `STARTED`
+ `STOPPED`

### DiscovererStateOutput
<a name="v1-discoverers-id-discovererid-stop-model-discovererstateoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| DiscovererId | string | False | The ID of the discoverer. | 
| State | [DiscovererState](#v1-discoverers-id-discovererid-stop-model-discovererstate) | False | The state of the discoverer. | 

### ErrorOutput
<a name="v1-discoverers-id-discovererid-stop-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 