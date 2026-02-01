AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# AssociateDiscoveredResource

Associates a discovered resource ID from Application Discovery Service with a migration
task.

## Request Syntax

```
{
   "DiscoveredResource": {
      "ConfigurationId": "`string`",
      "Description": "`string`"
   },
   "DryRun": `boolean`,
   "MigrationTaskName": "`string`",
   "ProgressUpdateStream": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DiscoveredResource](#API_AssociateDiscoveredResource_RequestSyntax "#API_AssociateDiscoveredResource_RequestSyntax")**

Object representing a Resource.

Type: [DiscoveredResource](API_DiscoveredResource.md "API_DiscoveredResource.md") object

Required: Yes

**[DryRun](#API_AssociateDiscoveredResource_RequestSyntax "#API_AssociateDiscoveredResource_RequestSyntax")**

Optional boolean flag to indicate whether any effect should take place. Used to test if
the caller has permission to make the call.

Type: Boolean

Required: No

**[MigrationTaskName](#API_AssociateDiscoveredResource_RequestSyntax "#API_AssociateDiscoveredResource_RequestSyntax")**

The identifier given to the MigrationTask. _Do not store personal data in this
field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[ProgressUpdateStream](#API_AssociateDiscoveredResource_RequestSyntax "#API_AssociateDiscoveredResource_RequestSyntax")**

The name of the ProgressUpdateStream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 400

**DryRunOperation**

Exception raised to indicate a successfully authorized action when the
`DryRun` flag is set to "true".

HTTP Status Code: 400

**HomeRegionNotSetException**

The home region is not set. Set the home region to continue.

HTTP Status Code: 400

**InternalServerError**

Exception raised when an internal, configuration, or dependency error is
encountered.

HTTP Status Code: 500

**InvalidInputException**

Exception raised when the provided input violates a policy constraint or is entered in
the wrong format or data type.

HTTP Status Code: 400

**PolicyErrorException**

Exception raised when there are problems accessing Application Discovery Service
(Application Discovery Service); most likely due to a misconfigured policy or the
`migrationhub-discovery` role is missing or not configured correctly.

HTTP Status Code: 400

**ResourceNotFoundException**

Exception raised when the request references a resource (Application Discovery Service
configuration, update stream, migration task, etc.) that does not exist in Application
Discovery Service (Application Discovery Service) or in Migration Hub's repository.

HTTP Status Code: 400

**ServiceUnavailableException**

Exception raised when there is an internal, configuration, or dependency error
encountered.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

**Message**

A message that provides information about the exception.

**RetryAfterSeconds**

The number of seconds the caller should wait before retrying.

HTTP Status Code: 400

**UnauthorizedOperation**

Exception raised to indicate a request was not authorized when the `DryRun`
flag is set to "true".

HTTP Status Code: 400

## Examples

### Associate a discovered resource

The following example associates an AWS Application Discovery Service discovered
resource specified by its configuration id and description to the migration task
identified by the values passed to the required parameters of
`MigrationTaskName` and `ProgressUpdateStream` in the
request.

#### Sample Request

```

{
    "ProgressUpdateStream": "SMS",
    "MigrationTaskName": "sms-12de3cf1a",
    "DiscoveredResource": {
        "ConfigurationId": "d-server-0025db43a885966c8",
        "Description": "Amazon Linux AMI release 2016.09"
    }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource.md")
