

# Discover
<a name="v1-discover"></a>

Allows you get the discovered schemas that have been inferred from events on an event bus.

**Note**  
 Discoverer will only infer events that are nested up to 255 levels. Any events past 255 levels are ignored. 

## URI
<a name="v1-discover-url"></a>

`/v1/discover`

## HTTP methods
<a name="v1-discover-http-methods"></a>

### POST
<a name="v1-discoverpost"></a>

**Operation ID:** `GetDiscoveredSchema`

Get the discovered schema that was generated based on sampled events.


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | GetDiscoveredSchemaOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 401 | ErrorOutput | 401 response | 
| 403 | ErrorOutput | 403 response | 
| 500 | ErrorOutput | 500 response | 
| 503 | ErrorOutput | 503 response | 

### OPTIONS
<a name="v1-discoveroptions"></a>


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="v1-discover-schemas"></a>

### Request bodies
<a name="v1-discover-request-examples"></a>

#### POST schema
<a name="v1-discover-request-body-post-example"></a>

```
{
  "Type": enum,
  "Events": [
    "string"
  ]
}
```

### Response bodies
<a name="v1-discover-response-examples"></a>

#### GetDiscoveredSchemaOutput schema
<a name="v1-discover-response-body-getdiscoveredschemaoutput-example"></a>

```
{
  "Content": "string"
}
```

#### ErrorOutput schema
<a name="v1-discover-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="v1-discover-properties"></a>

### ErrorOutput
<a name="v1-discover-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### GetDiscoveredSchemaInput
<a name="v1-discover-model-getdiscoveredschemainput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Events | Array of type string | True | An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events. | 
| Type | [Type](#v1-discover-model-type) | True | The type of event. | 

### GetDiscoveredSchemaOutput
<a name="v1-discover-model-getdiscoveredschemaoutput"></a>




| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Content | string | False | The source of the schema definition. | 

### Type
<a name="v1-discover-model-type"></a>

The type of schema to export.
+ `OpenApi3`
+ `JSONSchemaDraft4`