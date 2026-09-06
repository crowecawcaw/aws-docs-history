

# Applications applicationId Versions
<a name="applications-applicationid-versions"></a>

## URI
<a name="applications-applicationid-versions-url"></a>

`/applications/{{applicationId}}/versions`

## HTTP methods
<a name="applications-applicationid-versions-http-methods"></a>

### GET
<a name="applications-applicationid-versionsget"></a>

**Operation ID:** `ListApplicationVersions`

Lists versions for the specified application.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Query parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| maxItems | String | False | The total number of items to return. | 
| nextToken | String | False | A token to specify where to start paginating. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | ApplicationVersionPage | Success | 
| 400 | BadRequestException | One of the parameters in the request is invalid. | 
| 403 | ForbiddenException | The client is not authenticated. | 
| 404 | NotFoundException | The resource (for example, an access policy statement) specified in the request doesn't exist. | 
| 429 | TooManyRequestsException | The client is sending more than the allowed number of requests per unit of time. | 
| 500 | InternalServerErrorException | The AWS Serverless Application Repository service encountered an internal error. | 

### OPTIONS
<a name="applications-applicationid-versionsoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="applications-applicationid-versions-schemas"></a>

### Response bodies
<a name="applications-applicationid-versions-response-examples"></a>

#### ApplicationVersionPage schema
<a name="applications-applicationid-versions-response-body-applicationversionpage-example"></a>

```
{
  "versions": [
    {
      "applicationId": "string",
      "semanticVersion": "string",
      "sourceCodeUrl": "string",
      "creationTime": "string"
    }
  ],
  "nextToken": "string"
}
```

#### BadRequestException schema
<a name="applications-applicationid-versions-response-body-badrequestexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ForbiddenException schema
<a name="applications-applicationid-versions-response-body-forbiddenexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### NotFoundException schema
<a name="applications-applicationid-versions-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### TooManyRequestsException schema
<a name="applications-applicationid-versions-response-body-toomanyrequestsexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### InternalServerErrorException schema
<a name="applications-applicationid-versions-response-body-internalservererrorexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties
<a name="applications-applicationid-versions-properties"></a>

### ApplicationVersionPage
<a name="applications-applicationid-versions-model-applicationversionpage"></a>

A list of version summaries for the application.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| nextToken | string | False | The token to request the next page of results. | 
| versions | Array of type [VersionSummary](#applications-applicationid-versions-model-versionsummary) | True | An array of version summaries for the application. | 

### BadRequestException
<a name="applications-applicationid-versions-model-badrequestexception"></a>

One of the parameters in the request is invalid.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 400 | 
| message | string | False | One of the parameters in the request is invalid. | 

### ForbiddenException
<a name="applications-applicationid-versions-model-forbiddenexception"></a>

The client is not authenticated.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 403 | 
| message | string | False | The client is not authenticated. | 

### InternalServerErrorException
<a name="applications-applicationid-versions-model-internalservererrorexception"></a>

The AWS Serverless Application Repository service encountered an internal error.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 500 | 
| message | string | False | The AWS Serverless Application Repository service encountered an internal error. | 

### NotFoundException
<a name="applications-applicationid-versions-model-notfoundexception"></a>

The resource (for example, an access policy statement) specified in the request doesn't exist.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 404 | 
| message | string | False | The resource (for example, an access policy statement) specified in the request doesn't exist. | 

### TooManyRequestsException
<a name="applications-applicationid-versions-model-toomanyrequestsexception"></a>

The client is sending more than the allowed number of requests per unit of time.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 429 | 
| message | string | False | The client is sending more than the allowed number of requests per unit of time. | 

### VersionSummary
<a name="applications-applicationid-versions-model-versionsummary"></a>

An application version summary.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| applicationId | string | True | The application Amazon Resource Name (ARN). | 
| creationTime | string | True | The date and time this resource was created. | 
| semanticVersion | string | True | The semantic version of the application:<br /> [https://semver.org/](https://semver.org/)  | 
| sourceCodeUrl | string | False | A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit. | 

## See also
<a name="applications-applicationid-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListApplicationVersions
<a name="ListApplicationVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for Python](/goto/boto3/serverlessrepo-2017-09-08/ListApplicationVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/serverlessrepo-2017-09-08/ListApplicationVersions)