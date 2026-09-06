

# Applications applicationId Unshare
<a name="applications-applicationid-unshare"></a>

## URI
<a name="applications-applicationid-unshare-url"></a>

`/applications/{{applicationId}}/unshare`

## HTTP methods
<a name="applications-applicationid-unshare-http-methods"></a>

### POST
<a name="applications-applicationid-unsharepost"></a>

**Operation ID:** `UnshareApplication`

Unshares an application from an AWS Organization.

This operation can be called only from the organization's management account.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 204 | None | Success | 
| 400 | BadRequestException | One of the parameters in the request is invalid. | 
| 403 | ForbiddenException | The client is not authenticated. | 
| 404 | NotFoundException | The resource (for example, an access policy statement) specified in the request doesn't exist. | 
| 429 | TooManyRequestsException | The client is sending more than the allowed number of requests per unit of time. | 
| 500 | InternalServerErrorException | The AWS Serverless Application Repository service encountered an internal error. | 

### OPTIONS
<a name="applications-applicationid-unshareoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="applications-applicationid-unshare-schemas"></a>

### Request bodies
<a name="applications-applicationid-unshare-request-examples"></a>

#### POST schema
<a name="applications-applicationid-unshare-request-body-post-example"></a>

```
{
  "organizationId": "string"
}
```

### Response bodies
<a name="applications-applicationid-unshare-response-examples"></a>

#### BadRequestException schema
<a name="applications-applicationid-unshare-response-body-badrequestexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ForbiddenException schema
<a name="applications-applicationid-unshare-response-body-forbiddenexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### NotFoundException schema
<a name="applications-applicationid-unshare-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### TooManyRequestsException schema
<a name="applications-applicationid-unshare-response-body-toomanyrequestsexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### InternalServerErrorException schema
<a name="applications-applicationid-unshare-response-body-internalservererrorexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties
<a name="applications-applicationid-unshare-properties"></a>

### BadRequestException
<a name="applications-applicationid-unshare-model-badrequestexception"></a>

One of the parameters in the request is invalid.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 400 | 
| message | string | False | One of the parameters in the request is invalid. | 

### ForbiddenException
<a name="applications-applicationid-unshare-model-forbiddenexception"></a>

The client is not authenticated.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 403 | 
| message | string | False | The client is not authenticated. | 

### InternalServerErrorException
<a name="applications-applicationid-unshare-model-internalservererrorexception"></a>

The AWS Serverless Application Repository service encountered an internal error.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 500 | 
| message | string | False | The AWS Serverless Application Repository service encountered an internal error. | 

### NotFoundException
<a name="applications-applicationid-unshare-model-notfoundexception"></a>

The resource (for example, an access policy statement) specified in the request doesn't exist.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 404 | 
| message | string | False | The resource (for example, an access policy statement) specified in the request doesn't exist. | 

### TooManyRequestsException
<a name="applications-applicationid-unshare-model-toomanyrequestsexception"></a>

The client is sending more than the allowed number of requests per unit of time.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 429 | 
| message | string | False | The client is sending more than the allowed number of requests per unit of time. | 

### UnshareApplicationInput
<a name="applications-applicationid-unshare-model-unshareapplicationinput"></a>

Unshare application request.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| organizationId | string | True | The AWS Organizations ID to unshare the application from. | 

## See also
<a name="applications-applicationid-unshare-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UnshareApplication
<a name="UnshareApplication-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for Python](/goto/boto3/serverlessrepo-2017-09-08/UnshareApplication)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/serverlessrepo-2017-09-08/UnshareApplication)