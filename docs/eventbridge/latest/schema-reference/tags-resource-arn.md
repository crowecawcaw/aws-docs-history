

# Tag
<a name="tags-resource-arn"></a>

A tag is a key-value pair associated with a resource. You can use these metadata tags to identify the purpose of a broker or configuration. 

## URI
<a name="tags-resource-arn-url"></a>

`/tags/{{resource-arn}}`

## HTTP methods
<a name="tags-resource-arn-http-methods"></a>

### GET
<a name="tags-resource-arnget"></a>

**Operation ID:** `ListTagsForResource`

Get tags for resource.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The ARN of the resource. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ListTagsForResourceOutput | 200 response | 
| 400 | ErrorOutput | 400 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 

### POST
<a name="tags-resource-arnpost"></a>

**Operation ID:** `TagResource`

Add tags to a resource.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The ARN of the resource. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 204 | None | 204 response | 
| 400 | ErrorOutput | 400 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 

### DELETE
<a name="tags-resource-arndelete"></a>

**Operation ID:** `UntagResource`

Removes tags from a resource.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{resource-arn}} | String | True | The ARN of the resource. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| tagKeys | String | True | Keys of key-value pairs. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 204 | None | 204 response | 
| 400 | ErrorOutput | 400 response | 
| 403 | ErrorOutput | 403 response | 
| 404 | ErrorOutput | 404 response | 
| 500 | ErrorOutput | 500 response | 

### OPTIONS
<a name="tags-resource-arnoptions"></a>


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="tags-resource-arn-schemas"></a>

### Request bodies
<a name="tags-resource-arn-request-examples"></a>

#### POST schema
<a name="tags-resource-arn-request-body-post-example"></a>

```
{
  "tags": {
  }
}
```

### Response bodies
<a name="tags-resource-arn-response-examples"></a>

#### ListTagsForResourceOutput schema
<a name="tags-resource-arn-response-body-listtagsforresourceoutput-example"></a>

```
{
  "tags": {
  }
}
```

#### ErrorOutput schema
<a name="tags-resource-arn-response-body-erroroutput-example"></a>

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties
<a name="tags-resource-arn-properties"></a>

### ErrorOutput
<a name="tags-resource-arn-model-erroroutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| Code | string | True | The error code. | 
| Message | string | True | The message string of the error output. | 

### ListTagsForResourceOutput
<a name="tags-resource-arn-model-listtagsforresourceoutput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| tags | [Tags](#tags-resource-arn-model-tags) | False |  | 

### TagResourceInput
<a name="tags-resource-arn-model-tagresourceinput"></a>


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| tags | [Tags](#tags-resource-arn-model-tags) | True | Tags associated with the resource. | 

### Tags
<a name="tags-resource-arn-model-tags"></a>

Key-value pairs associated with a resource.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| `*` | string | False |  | 