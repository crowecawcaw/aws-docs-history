

# Applications applicationId Dependencies
<a name="applications-applicationid-dependencies"></a>

## URI
<a name="applications-applicationid-dependencies-url"></a>

`/applications/{{applicationId}}/dependencies`

## HTTP methods
<a name="applications-applicationid-dependencies-http-methods"></a>

### GET
<a name="applications-applicationid-dependenciesget"></a>

**Operation ID:** `ListApplicationDependencies`

Retrieves the list of applications nested in the containing application.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| nextToken | String | False | A token to specify where to start paginating. | 
| maxItems | String | False | The total number of items to return. | 
| semanticVersion | String | False | The semantic version of the application to get. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ApplicationDependencyPage | Success | 
| 400 | BadRequestException | One of the parameters in the request is invalid. | 
| 403 | ForbiddenException | The client is not authenticated. | 
| 404 | NotFoundException | The resource (for example, an access policy statement) specified in the request doesn't exist. | 
| 429 | TooManyRequestsException | The client is sending more than the allowed number of requests per unit of time. | 
| 500 | InternalServerErrorException | The AWS Serverless Application Repository service encountered an internal error. | 

### OPTIONS
<a name="applications-applicationid-dependenciesoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="applications-applicationid-dependencies-schemas"></a>

### Response bodies
<a name="applications-applicationid-dependencies-response-examples"></a>

#### ApplicationDependencyPage schema
<a name="applications-applicationid-dependencies-response-body-applicationdependencypage-example"></a>

```
{
  "dependencies": [
    {
      "applicationId": "string",
      "semanticVersion": "string"
    }
  ],
  "nextToken": "string"
}
```

#### BadRequestException schema
<a name="applications-applicationid-dependencies-response-body-badrequestexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ForbiddenException schema
<a name="applications-applicationid-dependencies-response-body-forbiddenexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### NotFoundException schema
<a name="applications-applicationid-dependencies-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### TooManyRequestsException schema
<a name="applications-applicationid-dependencies-response-body-toomanyrequestsexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### InternalServerErrorException schema
<a name="applications-applicationid-dependencies-response-body-internalservererrorexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties
<a name="applications-applicationid-dependencies-properties"></a>

### ApplicationDependencyPage
<a name="applications-applicationid-dependencies-model-applicationdependencypage"></a>

A list of application summaries nested in the application.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| dependencies | Array of type [ApplicationDependencySummary](#applications-applicationid-dependencies-model-applicationdependencysummary) | True | An array of application summaries nested in the application. | 
| nextToken | string | False | The token to request the next page of results. | 

### ApplicationDependencySummary
<a name="applications-applicationid-dependencies-model-applicationdependencysummary"></a>

A nested application summary.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| applicationId | string | True | The Amazon Resource Name (ARN) of the nested application. | 
| semanticVersion | string | True | The semantic version of the nested application. | 

### BadRequestException
<a name="applications-applicationid-dependencies-model-badrequestexception"></a>

One of the parameters in the request is invalid.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 400 | 
| message | string | False | One of the parameters in the request is invalid. | 

### ForbiddenException
<a name="applications-applicationid-dependencies-model-forbiddenexception"></a>

The client is not authenticated.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 403 | 
| message | string | False | The client is not authenticated. | 

### InternalServerErrorException
<a name="applications-applicationid-dependencies-model-internalservererrorexception"></a>

The AWS Serverless Application Repository service encountered an internal error.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 500 | 
| message | string | False | The AWS Serverless Application Repository service encountered an internal error. | 

### NotFoundException
<a name="applications-applicationid-dependencies-model-notfoundexception"></a>

The resource (for example, an access policy statement) specified in the request doesn't exist.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 404 | 
| message | string | False | The resource (for example, an access policy statement) specified in the request doesn't exist. | 

### TooManyRequestsException
<a name="applications-applicationid-dependencies-model-toomanyrequestsexception"></a>

The client is sending more than the allowed number of requests per unit of time.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 429 | 
| message | string | False | The client is sending more than the allowed number of requests per unit of time. | 

## See also
<a name="applications-applicationid-dependencies-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListApplicationDependencies
<a name="ListApplicationDependencies-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for Python](/goto/boto3/serverlessrepo-2017-09-08/ListApplicationDependencies)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/serverlessrepo-2017-09-08/ListApplicationDependencies)