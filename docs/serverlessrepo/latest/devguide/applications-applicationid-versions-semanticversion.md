

# Applications applicationId Versions semanticVersion
<a name="applications-applicationid-versions-semanticversion"></a>

## URI
<a name="applications-applicationid-versions-semanticversion-url"></a>

`/applications/{{applicationId}}/versions/{{semanticVersion}}`

## HTTP methods
<a name="applications-applicationid-versions-semanticversion-http-methods"></a>

### PUT
<a name="applications-applicationid-versions-semanticversionput"></a>

**Operation ID:** `CreateApplicationVersion`

Creates an application version.


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 
| {{semanticVersion}} | String | True | The semantic version of the new version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 201 | Version | Success | 
| 400 | BadRequestException | One of the parameters in the request is invalid. | 
| 403 | ForbiddenException | The client is not authenticated. | 
| 409 | ConflictException | The resource already exists. | 
| 429 | TooManyRequestsException | The client is sending more than the allowed number of requests per unit of time. | 
| 500 | InternalServerErrorException | The AWS Serverless Application Repository service encountered an internal error. | 

### OPTIONS
<a name="applications-applicationid-versions-semanticversionoptions"></a>


**Path parameters**  

| Name | Type | Required | Description | 
| --- |--- |--- |--- |
| {{applicationId}} | String | True | The Amazon Resource Name (ARN) of the application. | 
| {{semanticVersion}} | String | True | The semantic version of the new version. | 


**Responses**  

| Status code | Response model | Description | 
| --- |--- |--- |
| 200 | None | 200 response | 

## Schemas
<a name="applications-applicationid-versions-semanticversion-schemas"></a>

### Request bodies
<a name="applications-applicationid-versions-semanticversion-request-examples"></a>

#### PUT schema
<a name="applications-applicationid-versions-semanticversion-request-body-put-example"></a>

```
{
  "templateBody": "string",
  "templateUrl": "string",
  "sourceCodeUrl": "string",
  "sourceCodeArchiveUrl": "string"
}
```

### Response bodies
<a name="applications-applicationid-versions-semanticversion-response-examples"></a>

#### Version schema
<a name="applications-applicationid-versions-semanticversion-response-body-version-example"></a>

```
{
  "applicationId": "string",
  "semanticVersion": "string",
  "sourceCodeUrl": "string",
  "sourceCodeArchiveUrl": "string",
  "templateUrl": "string",
  "creationTime": "string",
  "parameterDefinitions": [
    {
      "name": "string",
      "defaultValue": "string",
      "description": "string",
      "type": "string",
      "noEcho": boolean,
      "allowedPattern": "string",
      "constraintDescription": "string",
      "minValue": integer,
      "maxValue": integer,
      "minLength": integer,
      "maxLength": integer,
      "allowedValues": [
        "string"
      ],
      "referencedByResources": [
        "string"
      ]
    }
  ],
  "requiredCapabilities": [
    enum
  ],
  "resourcesSupported": boolean
}
```

#### BadRequestException schema
<a name="applications-applicationid-versions-semanticversion-response-body-badrequestexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ForbiddenException schema
<a name="applications-applicationid-versions-semanticversion-response-body-forbiddenexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### ConflictException schema
<a name="applications-applicationid-versions-semanticversion-response-body-conflictexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### TooManyRequestsException schema
<a name="applications-applicationid-versions-semanticversion-response-body-toomanyrequestsexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

#### InternalServerErrorException schema
<a name="applications-applicationid-versions-semanticversion-response-body-internalservererrorexception-example"></a>

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties
<a name="applications-applicationid-versions-semanticversion-properties"></a>

### BadRequestException
<a name="applications-applicationid-versions-semanticversion-model-badrequestexception"></a>

One of the parameters in the request is invalid.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 400 | 
| message | string | False | One of the parameters in the request is invalid. | 

### Capability
<a name="applications-applicationid-versions-semanticversion-model-capability"></a>

Values that must be specified in order to deploy some applications.
+ `CAPABILITY_IAM`
+ `CAPABILITY_NAMED_IAM`
+ `CAPABILITY_AUTO_EXPAND`
+ `CAPABILITY_RESOURCE_POLICY`

### ConflictException
<a name="applications-applicationid-versions-semanticversion-model-conflictexception"></a>

The resource already exists.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 409 | 
| message | string | False | The resource already exists. | 

### CreateApplicationVersionInput
<a name="applications-applicationid-versions-semanticversion-model-createapplicationversioninput"></a>

Create a version request.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| sourceCodeArchiveUrl | string | False | A link to the S3 object that contains the ZIP archive of the source code for this version of your application.<br />Maximum size 50 MB | 
| sourceCodeUrl | string | False | A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit. | 
| templateBody | string | False | The raw packaged AWS SAM template of your application. | 
| templateUrl | string | False | A link to the packaged AWS SAM template of your application. | 

### ForbiddenException
<a name="applications-applicationid-versions-semanticversion-model-forbiddenexception"></a>

The client is not authenticated.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 403 | 
| message | string | False | The client is not authenticated. | 

### InternalServerErrorException
<a name="applications-applicationid-versions-semanticversion-model-internalservererrorexception"></a>

The AWS Serverless Application Repository service encountered an internal error.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 500 | 
| message | string | False | The AWS Serverless Application Repository service encountered an internal error. | 

### ParameterDefinition
<a name="applications-applicationid-versions-semanticversion-model-parameterdefinition"></a>

Parameters supported by the application.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| allowedPattern | string | False | A regular expression that represents the patterns to allow for `String` types. | 
| allowedValues | Array of type string | False | An array containing the list of values allowed for the parameter. | 
| constraintDescription | string | False | A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of `[A-Za-z0-9]+` displays the following error message when the user specifies an invalid value:<br /> `Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+` <br />By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:<br /> `Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.`  | 
| defaultValue | string | False | A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints. | 
| description | string | False | A string of up to 4,000 characters that describes the parameter. | 
| maxLength | integer | False | An integer value that determines the largest number of characters that you want to allow for `String` types. | 
| maxValue | integer | False | A numeric value that determines the largest numeric value that you want to allow for `Number` types. | 
| minLength | integer | False | An integer value that determines the smallest number of characters that you want to allow for `String` types. | 
| minValue | integer | False | A numeric value that determines the smallest numeric value that you want to allow for `Number` types. | 
| name | string | True | The name of the parameter. | 
| noEcho | boolean | False | Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (\*\*\*\*\*). | 
| referencedByResources | Array of type string | True | A list of AWS SAM resources that use this parameter. | 
| type | string | False | The type of the parameter.<br />Valid values: `String \| Number \| List<Number> \| CommaDelimitedList` <br /> `String`: A literal string.<br />For example, users can specify `"MyUserName"`.<br /> `Number`: An integer or float. CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the `Ref` intrinsic function), the parameter value becomes a string.<br />For example, users might specify `"8888"`.<br /> `List<Number>`: An array of integers or floats that are separated by commas. CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the `Ref` intrinsic function), the parameter value becomes a list of strings.<br />For example, users might specify "80,20", and then `Ref` results in `["80","20"]`.<br /> `CommaDelimitedList`: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.<br />For example, users might specify "test,dev,prod", and then `Ref` results in `["test","dev","prod"]`. | 

### TooManyRequestsException
<a name="applications-applicationid-versions-semanticversion-model-toomanyrequestsexception"></a>

The client is sending more than the allowed number of requests per unit of time.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| errorCode | string | False | 429 | 
| message | string | False | The client is sending more than the allowed number of requests per unit of time. | 

### Version
<a name="applications-applicationid-versions-semanticversion-model-version"></a>

Application version details.


| Property | Type | Required | Description | 
| --- |--- |--- |--- |
| applicationId | string | True | The application Amazon Resource Name (ARN). | 
| creationTime | string | True | The date and time this resource was created. | 
| parameterDefinitions | Array of type [ParameterDefinition](#applications-applicationid-versions-semanticversion-model-parameterdefinition) | True | An array of parameter types supported by the application. | 
| requiredCapabilities | Array of type [Capability](#applications-applicationid-versions-semanticversion-model-capability) | True | A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.<br />The only valid values are `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_RESOURCE_POLICY`, and `CAPABILITY_AUTO_EXPAND`.<br />The following resources require you to specify `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`: [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html), [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html), [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html), and [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html). If the application contains IAM resources, you can specify either `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`. If the application contains IAM resources with custom names, you must specify `CAPABILITY_NAMED_IAM`.<br />The following resources require you to specify `CAPABILITY_RESOURCE_POLICY`: [AWS::Lambda::Permission](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html), [AWS::IAM:Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html), [AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html), [AWS::S3::BucketPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html), [AWS::SQS::QueuePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html), and [AWS::SNS::TopicPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html).<br />Applications that contain one or more nested applications require you to specify `CAPABILITY_AUTO_EXPAND`.<br />If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don't specify this parameter for an application that requires capabilities, the call will fail. | 
| resourcesSupported | boolean | True | Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved. | 
| semanticVersion | string | True | The semantic version of the application:<br /> [https://semver.org/](https://semver.org/)  | 
| sourceCodeArchiveUrl | string | False | A link to the S3 object that contains the ZIP archive of the source code for this version of your application.<br />Maximum size 50 MB | 
| sourceCodeUrl | string | False | A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit. | 
| templateUrl | string | True | A link to the packaged AWS SAM template of your application. | 

## See also
<a name="applications-applicationid-versions-semanticversion-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateApplicationVersion
<a name="CreateApplicationVersion-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for Python](/goto/boto3/serverlessrepo-2017-09-08/CreateApplicationVersion)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/serverlessrepo-2017-09-08/CreateApplicationVersion)