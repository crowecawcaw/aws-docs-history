# Applications

## URI

`/applications`

## HTTP methods

### GET

**Operation ID:** `ListApplications`

Lists applications owned by the requester.

| Query parameters | Name   | Type  | Required                                      | Description |
| ---------------- | ------ | ----- | --------------------------------------------- | ----------- |
| `maxItems`       | String | False | The total number of items to return.          |
| `nextToken`      | String | False | A token to specify where to start paginating. |

| Responses | Status code                    | Response model                                                                                 | Description |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | ----------- |
| `200`     | `ApplicationPage`              | Success                                                                                        |
| `400`     | `BadRequestException`          | One of the parameters in the request is invalid.                                               |
| `403`     | `ForbiddenException`           | The client is not authenticated.                                                               |
| `404`     | `NotFoundException`            | The resource (for example, an access policy statement) specified in the request doesn't exist. |
| `500`     | `InternalServerErrorException` | The AWS Serverless Application Repository service encountered an internal error.               |

### POST

**Operation ID:** `CreateApplication`

Creates an application, optionally including an AWS SAM file to create the first application
version in the same call.

| Responses | Status code                    | Response model                                                                   | Description |
| --------- | ------------------------------ | -------------------------------------------------------------------------------- | ----------- |
| `201`     | `Application`                  | Success                                                                          |
| `400`     | `BadRequestException`          | One of the parameters in the request is invalid.                                 |
| `403`     | `ForbiddenException`           | The client is not authenticated.                                                 |
| `409`     | `ConflictException`            | The resource already exists.                                                     |
| `429`     | `TooManyRequestsException`     | The client is sending more than the allowed number of requests per unit of time. |
| `500`     | `InternalServerErrorException` | The AWS Serverless Application Repository service encountered an internal error. |

### OPTIONS

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Request bodies

```
{
  "name": "string",
  "description": "string",
  "author": "string",
  "spdxLicenseId": "string",
  "licenseBody": "string",
  "licenseUrl": "string",
  "readmeBody": "string",
  "readmeUrl": "string",
  "labels": [
    "string"
  ],
  "homePageUrl": "string",
  "semanticVersion": "string",
  "templateBody": "string",
  "templateUrl": "string",
  "sourceCodeUrl": "string",
  "sourceCodeArchiveUrl": "string"
}
```

### Response bodies

```
{
  "applications": [
    {
      "applicationId": "string",
      "name": "string",
      "description": "string",
      "author": "string",
      "spdxLicenseId": "string",
      "labels": [
        "string"
      ],
      "creationTime": "string",
      "homePageUrl": "string"
    }
  ],
  "nextToken": "string"
}
```

```
{
  "applicationId": "string",
  "name": "string",
  "description": "string",
  "author": "string",
  "isVerifiedAuthor": boolean,
  "verifiedAuthorUrl": "string",
  "spdxLicenseId": "string",
  "licenseUrl": "string",
  "readmeUrl": "string",
  "labels": [
    "string"
  ],
  "creationTime": "string",
  "homePageUrl": "string",
  "version": {
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
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

```
{
  "message": "string",
  "errorCode": "string"
}
```

## Properties

### Application

Details about the application.

| Property            | Type                                                                 | Required | Description                                                                                                                                                                                                                                                                           |
| ------------------- | -------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `applicationId`     | string                                                               | True     | The application Amazon Resource Name (ARN).                                                                                                                                                                                                                                           |
| `author`            | string                                                               | True     | The name of the author publishing the app.Minimum length=1. Maximum length=127.Pattern "^[a-z0-9](([a-z0-9]                                                                                                                                                                           | -(?!-))\*[a-z0-9])?$"; |
| `creationTime`      | string                                                               | False    | The date and time this resource was created.                                                                                                                                                                                                                                          |
| `description`       | string                                                               | True     | The description of the application.Minimum length=1. Maximum length=256                                                                                                                                                                                                               |
| `homePageUrl`       | string                                                               | False    | A URL with more information about the application, for example the location of your GitHub repository for the<br>application.                                                                                                                                                         |
| `isVerifiedAuthor`  | boolean                                                              | False    | Specifies whether the author of this application has been verified. This means that AWS has<br>made a good faith review, as a reasonable and prudent service provider, of the information provided by the<br>requester and has confirmed that the requester's identity is as claimed. |
| `labels`            | Array of type string                                                 | False    | Labels to improve discovery of apps in search results.Minimum length=1. Maximum length=127. Maximum number of labels: 10Pattern: "^[a-zA-Z0-9+\\-\_:\\/@]+$";                                                                                                                         |
| `licenseUrl`        | string                                                               | False    | A link to a license file of the app that matches the spdxLicenseID value of your application.Maximum size 5 MB                                                                                                                                                                        |
| `name`              | string                                                               | True     | The name of the application.Minimum length=1. Maximum length=140Pattern: "[a-zA-Z0-9\\-]+";                                                                                                                                                                                           |
| `readmeUrl`         | string                                                               | False    | A link to the readme file in Markdown language that contains a more detailed description of the application<br>and how it works.Maximum size 5 MB                                                                                                                                     |
| `spdxLicenseId`     | string                                                               | False    | A valid identifier from https://spdx.org/licenses/.                                                                                                                                                                                                                                   |
| `verifiedAuthorUrl` | string                                                               | False    | The URL to the public profile of a verified author. This URL is submitted by the author.                                                                                                                                                                                              |
| `version`           | [Version](#applications-model-version "#applications-model-version") | False    | Version information about the application.                                                                                                                                                                                                                                            |

### ApplicationPage

A list of application details.

| Property       | Type                             | Required | Description                                    |
| -------------- | -------------------------------- | -------- | ---------------------------------------------- |
| `applications` | Array of type ApplicationSummary | True     | An array of application summaries.             |
| `nextToken`    | string                           | False    | The token to request the next page of results. |

### ApplicationSummary

Summary of details about the application.

| Property        | Type                 | Required | Description                                                                                                                                                   |
| --------------- | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `applicationId` | string               | True     | The application Amazon Resource Name (ARN).                                                                                                                   |
| `author`        | string               | True     | The name of the author publishing the app.Minimum length=1. Maximum length=127.Pattern "^[a-z0-9](([a-z0-9]                                                   | -(?!-))\*[a-z0-9])?$"; |
| `creationTime`  | string               | False    | The date and time this resource was created.                                                                                                                  |
| `description`   | string               | True     | The description of the application.Minimum length=1. Maximum length=256                                                                                       |
| `homePageUrl`   | string               | False    | A URL with more information about the application, for example the location of your GitHub repository for the<br>application.                                 |
| `labels`        | Array of type string | False    | Labels to improve discovery of apps in search results.Minimum length=1. Maximum length=127. Maximum number of labels: 10Pattern: "^[a-zA-Z0-9+\\-\_:\\/@]+$"; |
| `name`          | string               | True     | The name of the application.Minimum length=1. Maximum length=140Pattern: "[a-zA-Z0-9\\-]+";                                                                   |
| `spdxLicenseId` | string               | False    | A valid identifier from [https://spdx.org/licenses/](https://spdx.org/licenses/ "https://spdx.org/licenses/").                                                |

### BadRequestException

One of the parameters in the request is invalid.

| Property    | Type   | Required | Description                                      |
| ----------- | ------ | -------- | ------------------------------------------------ |
| `errorCode` | string | False    | 400                                              |
| `message`   | string | False    | One of the parameters in the request is invalid. |

### Capability

Values that must be specified in order to deploy some applications.

- `CAPABILITY_IAM`
- `CAPABILITY_NAMED_IAM`
- `CAPABILITY_AUTO_EXPAND`
- `CAPABILITY_RESOURCE_POLICY`

### ConflictException

The resource already exists.

| Property    | Type   | Required | Description                  |
| ----------- | ------ | -------- | ---------------------------- |
| `errorCode` | string | False    | 409                          |
| `message`   | string | False    | The resource already exists. |

### CreateApplicationInput

Create an application request.

| Property               | Type                 | Required | Description                                                                                                                                                                                                                                                                                   |
| ---------------------- | -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `author`               | string               | True     | The name of the author publishing the app.Minimum length=1. Maximum length=127.Pattern "^[a-z0-9](([a-z0-9]                                                                                                                                                                                   | -(?!-))\*[a-z0-9])?$"; |
| `description`          | string               | True     | The description of the application.Minimum length=1. Maximum length=256                                                                                                                                                                                                                       |
| `homePageUrl`          | string               | False    | A URL with more information about the application, for example the location of your GitHub repository for the<br>application.                                                                                                                                                                 |
| `labels`               | Array of type string | False    | Labels to improve discovery of apps in search results.Minimum length=1. Maximum length=127. Maximum number of labels: 10Pattern: "^[a-zA-Z0-9+\\-\_:\\/@]+$";                                                                                                                                 |
| `licenseBody`          | string               | False    | A local text file that contains the license of the app that matches the spdxLicenseID value of your<br>application. The file has the format `file://<path>/<filename>`.Maximum size 5 MBYou can specify only one of `licenseBody` and `licenseUrl`; otherwise, an error<br>results.           |
| `licenseUrl`           | string               | False    | A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your<br>application.Maximum size 5 MBYou can specify only one of `licenseBody` and `licenseUrl`; otherwise, an error<br>results.                                                         |
| `name`                 | string               | True     | The name of the application that you want to publish.Minimum length=1. Maximum length=140Pattern: "[a-zA-Z0-9\\-]+";                                                                                                                                                                          |
| `readmeBody`           | string               | False    | A local text readme file in Markdown language that contains a more detailed description of the application and<br>how it works. The file has the format `file://<path>/<filename>`.Maximum size 5 MBYou can specify only one of `readmeBody` and `readmeUrl`; otherwise, an error<br>results. |
| `readmeUrl`            | string               | False    | A link to the S3 object in Markdown language that contains a more detailed description of the application and<br>how it works.Maximum size 5 MBYou can specify only one of `readmeBody` and `readmeUrl`; otherwise, an error<br>results.                                                      |
| `semanticVersion`      | string               | False    | The semantic version of the application:<br>[https://semver.org/](https://semver.org/ "https://semver.org/")                                                                                                                                                                                  |
| `sourceCodeArchiveUrl` | string               | False    | A link to the S3 object that contains the ZIP archive of the source code for this version of your<br>application.Maximum size 50 MB                                                                                                                                                           |
| `sourceCodeUrl`        | string               | False    | A link to a public repository for the source code of your application, for example the URL of a specific<br>GitHub commit.                                                                                                                                                                    |
| `spdxLicenseId`        | string               | False    | A valid identifier from [https://spdx.org/licenses/](https://spdx.org/licenses/ "https://spdx.org/licenses/").                                                                                                                                                                                |
| `templateBody`         | string               | False    | The local raw packaged AWS SAM template file of your application. The file has the format<br>`file://<path>/<filename>`.You can specify only one of `templateBody` and `templateUrl`; otherwise an error<br>results.                                                                          |
| `templateUrl`          | string               | False    | A link to the S3 object containing the packaged AWS SAM template of your application.You can specify only one of `templateBody` and `templateUrl`; otherwise an error<br>results.                                                                                                             |

### ForbiddenException

The client is not authenticated.

| Property    | Type   | Required | Description                      |
| ----------- | ------ | -------- | -------------------------------- |
| `errorCode` | string | False    | 403                              |
| `message`   | string | False    | The client is not authenticated. |

### InternalServerErrorException

The AWS Serverless Application Repository service encountered an internal error.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 500                                                                              |
| `message`   | string | False    | The AWS Serverless Application Repository service encountered an internal error. |

### NotFoundException

The resource (for example, an access policy statement) specified in the request doesn't exist.

| Property    | Type   | Required | Description                                                                                    |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 404                                                                                            |
| `message`   | string | False    | The resource (for example, an access policy statement) specified in the request doesn't exist. |

### ParameterDefinition

Parameters supported by the application.

| Property                | Type                 | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `allowedPattern`        | string               | False    | A regular expression that represents the patterns to allow for `String` types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `allowedValues`         | Array of type string | False    | An array containing the list of values allowed for the parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `constraintDescription` | string               | False    | A string that explains a constraint when the constraint is violated. For example, without a constraint<br>description, a parameter that has an allowed pattern of `[A-Za-z0-9]+` displays the following error<br>message when the user specifies an invalid value:<br>`Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+`<br>By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers,"<br>you can display the following customized error message:<br>`Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.` |
| `defaultValue`          | string               | False    | A value of the appropriate type for the template to use if no value is specified when a stack is created. If<br>you define constraints for the parameter, you must specify a value that adheres to those constraints.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `description`           | string               | False    | A string of up to 4,000 characters that describes the parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `maxLength`             | integer              | False    | An integer value that determines the largest number of characters that you want to allow for<br>`String` types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `maxValue`              | integer              | False    | A numeric value that determines the largest numeric value that you want to allow for `Number`<br>types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `minLength`             | integer              | False    | An integer value that determines the smallest number of characters that you want to allow for<br>`String` types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `minValue`              | integer              | False    | A numeric value that determines the smallest numeric value that you want to allow for `Number`<br>types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `name`                  | string               | True     | The name of the parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `noEcho`                | boolean              | False    | Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the<br>value to true, the parameter value is masked with asterisks (\*\*\*\*\*).                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `referencedByResources` | Array of type string | True     | A list of AWS SAM resources that use this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `type`                  | string               | False    | The type of the parameter.Valid values: `String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Number | List<Number> | CommaDelimitedList`<br>`String`: A literal string.For example, users can specify `"MyUserName"`.<br>`Number`: An integer or float. CloudFormation validates the parameter value as a number. However,<br>when you use the parameter elsewhere in your template (for example, by using the `Ref`intrinsic<br>function), the parameter value becomes a string.For example, users might specify`"8888"`.<br>`List<Number>`: An array of integers or floats that are separated by commas. CloudFormation<br>validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for<br>example, by using the `Ref`intrinsic function), the parameter value becomes a list of strings.For example, users might specify "80,20", and then`Ref` results in<br>`["80","20"]`.<br>`CommaDelimitedList`: An array of literal strings that are separated by commas. The total number of<br>strings should be one more than the total number of commas. Also, each member string is space-trimmed.For example, users might specify "test,dev,prod", and then `Ref` results in<br>`["test","dev","prod"]`. |

### TooManyRequestsException

The client is sending more than the allowed number of requests per unit of time.

| Property    | Type   | Required | Description                                                                      |
| ----------- | ------ | -------- | -------------------------------------------------------------------------------- |
| `errorCode` | string | False    | 429                                                                              |
| `message`   | string | False    | The client is sending more than the allowed number of requests per unit of time. |

### Version

Application version details.

| Property               | Type                              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applicationId`        | string                            | True     | The application Amazon Resource Name (ARN).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `creationTime`         | string                            | True     | The date and time this resource was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `parameterDefinitions` | Array of type ParameterDefinition | True     | An array of parameter types supported by the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `requiredCapabilities` | Array of type Capability          | True     | A list of values that you must specify before you can deploy certain applications. Some applications might<br>include resources that can affect permissions in your AWS account, for example, by creating new<br>AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their<br>capabilities by specifying this parameter.The only valid values are `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`,<br>`CAPABILITY_RESOURCE_POLICY`, and `CAPABILITY_AUTO_EXPAND`.The following resources require you to specify `CAPABILITY_IAM` or<br>`CAPABILITY_NAMED_IAM`: [AWS::IAM::Group](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md"), [AWS::IAM::InstanceProfile](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md"), [AWS::IAM::Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), and [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md").<br>If the application contains IAM resources, you can specify either `CAPABILITY_IAM` or<br>`CAPABILITY_NAMED_IAM`. If the application contains IAM resources with custom names, you must specify<br>`CAPABILITY_NAMED_IAM`.The following resources require you to specify `CAPABILITY_RESOURCE_POLICY`: [AWS::Lambda::Permission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md"), [AWS::IAM:Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), [AWS::ApplicationAutoScaling::ScalingPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md"), [AWS::S3::BucketPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md"), [AWS::SQS::QueuePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md"), and [AWS::SNS::TopicPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md").Applications that contain one or more nested applications require you to specify<br>`CAPABILITY_AUTO_EXPAND`.If your application template contains any of the above resources, we recommend that you review all permissions<br>associated with the application before deploying. If you don't specify this parameter for an application that<br>requires capabilities, the call will fail. |
| `resourcesSupported`   | boolean                           | True     | Whether all of the AWS resources contained in this application are supported in the region in<br>which it is being retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `semanticVersion`      | string                            | True     | The semantic version of the application:<br>[https://semver.org/](https://semver.org/ "https://semver.org/")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sourceCodeArchiveUrl` | string                            | False    | A link to the S3 object that contains the ZIP archive of the source code for this version of your<br>application.Maximum size 50 MB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sourceCodeUrl`        | string                            | False    | A link to a public repository for the source code of your application, for example the URL of a specific<br>GitHub commit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `templateUrl`          | string                            | True     | A link to the packaged AWS SAM template of your application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## See also

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListApplications

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/cli2/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/boto3/serverlessrepo-2017-09-08/ListApplications.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/ListApplications.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/ListApplications.md")

### CreateApplication

- [AWS Command Line Interface V2](../../../goto/cli2/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/cli2/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/DotNetSDKV3/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForCpp/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForGoV2/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForJavaV2/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForJavaScriptV3/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForKotlin/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForPHPV3/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for Python](../../../goto/boto3/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/boto3/serverlessrepo-2017-09-08/CreateApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/CreateApplication.md "../../../goto/SdkForRubyV3/serverlessrepo-2017-09-08/CreateApplication.md")
