

# Applications applicationId Templates templateId
<a name="applications-applicationid-templates-templateid"></a>

## URI
<a name="applications-applicationid-templates-templateid-url"></a>

`/applications/{{applicationId}}/templates/{{templateId}}`

## HTTP methods
<a name="applications-applicationid-templates-templateid-http-methods"></a>

### GET
<a name="applications-applicationid-templates-templateidget"></a>

**Operation ID:** `GetCloudFormationTemplate`

Gets the specified AWS CloudFormation template.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 
| {{templateId}} | String | True | The UUID returned by CreateCloudFormationTemplate.<br />Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12} | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | TemplateDetails | Success | 
| 400 | BadRequestException | One of the parameters in the request is invalid. | 
| 403 | ForbiddenException | The client is not authenticated. | 
| 404 | NotFoundException | The resource (for example, an access policy statement) specified in the request doesn't exist. | 
| 429 | TooManyRequestsException | The client is sending more than the allowed number of requests per unit of time. | 
| 500 | InternalServerErrorException | The AWS Serverless Application Repository service encountered an internal error. | 

### OPTIONS
<a name="applications-applicationid-templates-templateidoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 
| {{templateId}} | String | True | The UUID returned by CreateCloudFormationTemplate.<br />Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12} | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="applications-applicationid-templates-templateid-schemas"></a>

### Response bodies
<a name="applications-applicationid-templates-templateid-response-examples"></a>

#### TemplateDetails schema
<a name="applications-applicationid-templates-templateid-response-body-templatedetails-example"></a>

```
{
  "templateId": "string",
  "templateUrl": "string",
  "applicationId": "string",
  "semanticVersion": "string",
  "status": enum,
  "creationTime": "string",
  "expirationTime": "string"
}
```

#### BadRequestException schema
<a name="applications-applicationid-templates-templateid-response-body-badrequestexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ForbiddenException schema
<a name="applications-applicationid-templates-templateid-response-body-forbiddenexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### NotFoundException schema
<a name="applications-applicationid-templates-templateid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### TooManyRequestsException schema
<a name="applications-applicationid-templates-templateid-response-body-toomanyrequestsexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### InternalServerErrorException schema
<a name="applications-applicationid-templates-templateid-response-body-internalservererrorexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties
<a name="applications-applicationid-templates-templateid-properties"></a>

### BadRequestException
<a name="applications-applicationid-templates-templateid-model-badrequestexception"></a>

One of the parameters in the request is invalid.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 400 | 
| message | string | False | One of the parameters in the request is invalid. | 

### ForbiddenException
<a name="applications-applicationid-templates-templateid-model-forbiddenexception"></a>

The client is not authenticated.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 403 | 
| message | string | False | The client is not authenticated. | 

### InternalServerErrorException
<a name="applications-applicationid-templates-templateid-model-internalservererrorexception"></a>

The AWS Serverless Application Repository service encountered an internal error.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 500 | 
| message | string | False | The AWS Serverless Application Repository service encountered an internal error. | 

### NotFoundException
<a name="applications-applicationid-templates-templateid-model-notfoundexception"></a>

The resource (for example, an access policy statement) specified in the request doesn't exist.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 404 | 
| message | string | False | The resource (for example, an access policy statement) specified in the request doesn't exist. | 

### TemplateDetails
<a name="applications-applicationid-templates-templateid-model-templatedetails"></a>

Details of the template.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| applicationId | string | True | The application Amazon Resource Name (ARN). | 
| creationTime | string | True | The date and time this resource was created. | 
| expirationTime | string | True | The date and time this template expires. Templates expire 1 hour after creation. | 
| semanticVersion | string | True | The semantic version of the application:<br /> [https://semver.org/](https://semver.org/)  | 
| status | string<br />Values: `PREPARING \| ACTIVE \| EXPIRED` | True | Status of the template creation workflow.<br />Possible values: `PREPARING \| ACTIVE \| EXPIRED`  | 
| templateId | string | True | The UUID returned by CreateCloudFormationTemplate.<br />Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12} | 
| templateUrl | string | True | A link to the template that can be used to deploy the application using AWS CloudFormation. | 

### TooManyRequestsException
<a name="applications-applicationid-templates-templateid-model-toomanyrequestsexception"></a>

The client is sending more than the allowed number of requests per unit of time.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 429 | 
| message | string | False | The client is sending more than the allowed number of requests per unit of time. | 

## See also
<a name="applications-applicationid-templates-templateid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCloudFormationTemplate
<a name="GetCloudFormationTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for Python](/goto/boto3/serverlessrepo-2017-09-08/GetCloudFormationTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/serverlessrepo-2017-09-08/GetCloudFormationTemplate)