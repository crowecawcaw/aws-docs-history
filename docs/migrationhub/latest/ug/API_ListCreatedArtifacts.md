AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ListCreatedArtifacts

Lists the created artifacts attached to a given migration task in an update stream. This
API has the following traits:

- Gets the list of the created artifacts while
  migration is taking place.
- Shows the artifacts created by the migration tool that was associated by the
  `AssociateCreatedArtifact` API.
- Lists created artifacts in a paginated interface.

## Request Syntax

```
{
   "MaxResults": `number`,
   "MigrationTaskName": "`string`",
   "NextToken": "`string`",
   "ProgressUpdateStream": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListCreatedArtifacts_RequestSyntax "#API_ListCreatedArtifacts_RequestSyntax")**

Maximum number of results to be returned per page.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10.

Required: No

**[MigrationTaskName](#API_ListCreatedArtifacts_RequestSyntax "#API_ListCreatedArtifacts_RequestSyntax")**

Unique identifier that references the migration task. _Do not store personal
data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[NextToken](#API_ListCreatedArtifacts_RequestSyntax "#API_ListCreatedArtifacts_RequestSyntax")**

If a `NextToken` was returned by a previous call, there are more results
available. To retrieve the next page of results, make the call again using the returned
token in `NextToken`.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

Required: No

**[ProgressUpdateStream](#API_ListCreatedArtifacts_RequestSyntax "#API_ListCreatedArtifacts_RequestSyntax")**

The name of the ProgressUpdateStream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

## Response Syntax

```
{
   "CreatedArtifactList": [
      {
         "Description": "***string***",
         "Name": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreatedArtifactList](#API_ListCreatedArtifacts_ResponseSyntax "#API_ListCreatedArtifacts_ResponseSyntax")**

List of created artifacts up to the maximum number of results specified in the
request.

Type: Array of [CreatedArtifact](API_CreatedArtifact.md "API_CreatedArtifact.md") objects

**[NextToken](#API_ListCreatedArtifacts_ResponseSyntax "#API_ListCreatedArtifacts_ResponseSyntax")**

If there are more created artifacts than the max result, return the next token to be
passed to the next call as a bookmark of where to start from.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

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

## Examples

### List created artifacts associated with a migration task and update stream

The following example lists the created artifact name and its description that is
associated with the values passed to the required parameters of
`MigrationTaskName` and `ProgressUpdateStream` in the
request.

#### Sample Request

```

{
    "ProgressUpdateStream": "SMS",
    "MigrationTaskName": "sms-12de3cf1a",
    "MaxResults": 1
}
```

#### Sample Response

```

{
    "CreatedArtifactList": [
        {
            "Name": "arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b",
            "Description": "Using SMS to migrate server to EC2"
        }
    ]
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListCreatedArtifacts.md")
