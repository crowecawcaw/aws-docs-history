

# Discoverers
<a name="v1-discoverers"></a>

Discoverers allow you to infer EventBridge Schemas based on the events on an event bus. 

## URI
<a name="v1-discoverers-url"></a>

`/v1/discoverers`

## HTTP methods
<a name="v1-discoverers-http-methods"></a>

### GET
<a name="v1-discoverersget"></a>

**Operation ID:** `ListDiscoverers`

List the discoverers.


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| sourceArnPrefix | String | False | Specifying this limits the results to only those ARNs that start with the specified prefix. | 
| limit | String | False | The maximum number of results to return per page. | 
| nextToken | String | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 
| discovererIdPrefix | String | False | Specifying this limits the results to only those discoverer IDs that start with the specified prefix. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ListDiscoverersOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### POST
<a name="v1-discovererspost"></a>

**Operation ID:** `CreateDiscoverer`

Creates a discoverer.

Due to no name being passed in the CreateDiscoverer API call there is no resource to DENY against when the customer adds a resource ARN of an existing discoverer in their IAM policies.


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 201 | DiscovererOutput | 201 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 409 | ErrorOutput | 409 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-discoverersoptions"></a>


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-discoverers-schemas"></a>

### Request bodies
<a name="v1-discoverers-request-examples"></a>

#### POST schema
<a name="v1-discoverers-request-body-post-example"></a>

```
{
  "CrossAccount": boolean,
  "Description": "string",
  "SourceArn": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="v1-discoverers-response-examples"></a>

#### ListDiscoverersOutput schema
<a name="v1-discoverers-response-body-listdiscoverersoutput-example"></a>

```
{
  "NextToken": "string",
  "Discoverers": [
    {
      "DiscovererArn": "string",
      "DiscovererId": "string",
      "CrossAccount": boolean,
      "SourceArn": "string",
      "State": enum,
      "tags": {
      }
    }
  ]
}
```

#### DiscovererOutput schema
<a name="v1-discoverers-response-body-discovereroutput-example"></a>

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
<a name="v1-discoverers-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-discoverers-properties"></a>

### CreateDiscovererInput
<a name="v1-discoverers-model-creatediscovererinput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CrossAccount | boolean | False | Allows for the discovery of the event schemas that are sent to the event bus from another account. (default: true) | 
| Description | string<br />MinLength: 0<br />MaxLength: 256 | False | A description for the discoverer. | 
| SourceArn | string<br />MinLength: 20<br />MaxLength: 1600 | True | The ARN of the event bus. | 
| tags | [Tags](#v1-discoverers-model-tags) | False | Tags associated with the resource. | 

### DiscovererOutput
<a name="v1-discoverers-model-discovereroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CrossAccount | boolean | False | Whether cross-account events are discovered. | 
| Description | string | False | The description of the discoverer. | 
| DiscovererArn | string | False | The ARN of the discoverer. | 
| DiscovererId | string | False | The ID of the discoverer. | 
| SourceArn | string | False | The ARN of the event bus. | 
| State | [DiscovererState](#v1-discoverers-model-discovererstate) | False | The state of the discoverer. | 
| tags | [Tags](#v1-discoverers-model-tags) | False | Tags associated with the resource. | 

### DiscovererState
<a name="v1-discoverers-model-discovererstate"></a>
+ `STARTED`
+ `STOPPED`

### DiscovererSummary
<a name="v1-discoverers-model-discoverersummary"></a>

A summary of the discoverer.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| CrossAccount | boolean | False | Whether cross-account events are discovered. | 
| DiscovererArn | string | False | The ARN of the discoverer. | 
| DiscovererId | string | False | The ID of the discoverer. | 
| SourceArn | string | False | The ARN of the event bus. | 
| State | [DiscovererState](#v1-discoverers-model-discovererstate) | False | The state of the discoverer. | 
| tags | [Tags](#v1-discoverers-model-tags) | False | Tags associated with the resource. | 

### ErrorOutput
<a name="v1-discoverers-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ListDiscoverersOutput
<a name="v1-discoverers-model-listdiscoverersoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Discoverers | Array of type [DiscovererSummary](#v1-discoverers-model-discoverersummary) | False | An array of `DiscovererSummary` information. | 
| NextToken | string | False | The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts. | 

### Tags
<a name="v1-discoverers-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 