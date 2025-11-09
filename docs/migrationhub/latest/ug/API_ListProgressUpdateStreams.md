AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ListProgressUpdateStreams

Lists progress update streams associated with the user account making this call.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListProgressUpdateStreams_RequestSyntax "#API_ListProgressUpdateStreams_RequestSyntax")**

Filter to limit the maximum number of results to list per page.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListProgressUpdateStreams_RequestSyntax "#API_ListProgressUpdateStreams_RequestSyntax")**

If a `NextToken` was returned by a previous call, there are more results
available. To retrieve the next page of results, make the call again using the returned
token in `NextToken`.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "ProgressUpdateStreamSummaryList": [
      {
         "ProgressUpdateStreamName": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListProgressUpdateStreams_ResponseSyntax "#API_ListProgressUpdateStreams_ResponseSyntax")**

If there are more streams created than the max result, return the next token to be
passed to the next call as a bookmark of where to start from.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

**[ProgressUpdateStreamSummaryList](#API_ListProgressUpdateStreams_ResponseSyntax "#API_ListProgressUpdateStreams_ResponseSyntax")**

List of progress update streams up to the max number of results passed in the
input.

Type: Array of [ProgressUpdateStreamSummary](API_ProgressUpdateStreamSummary.md "API_ProgressUpdateStreamSummary.md") objects

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

### List progress update streams

The following example lists the progress update streams associated with the
account invoking the request and uses the value passed to the optional parameter
`MaxResults`.

#### Sample Request

```

{
    "MaxResults": 2
}
```

#### Sample Response

```

{
    "ProgressUpdateStreamSummaryList": [
        {
            "ProgressUpdateStreamName": "DMS"
        },
        {
            "ProgressUpdateStreamName": "SMS"
        }
    ],
    "NextToken": "AYADeDJG11y1VuQBWp87zGdqAkkAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZ
    XkAREFwM0s3MElDWDI4NVJ3RG4vQUVnWFZKa2xNQVI1a2RJZXNNQXZnN2Y4M0pMdjN6Ujhka2VE
    Z0lRZEFnQ2toUE1Rdz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjo2MzEzOTQ
    0NDA2MDg6a2V5L2UzNmUxYTc5LTUyYTUtNDdhZi05YmZjLWUxZDY2MjMyM2E0MwCnAQEBAHieuD
    SjpG16QpfVPv6L98gI73HcNP7jNyhyIMduHA8a4wAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoB
    gkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDGKeYQzVoDEvBo0EDwIBEIA7KbgCu41sTOBeQaU9
    BOchDBz6NGrh3AztXyqwJGczR7PiOOJZUPipWyiZDOSwVh/Exbkwm5clUF3VJ0kCAAAAAAwAABA
    Ac1MGWKEY/ySGi8kJmVlSZlU6rN/okwmmQCyymv////8AAAABvAPw0ZhHxJ3B4nsQAAAAbahc0b
    uugm7vytB05AobE5AWiEJaEEz5kMiYQJtzDfwXM8h9GS8kX7ydocfw0yLCMM9/sLa5JaaqY3yVh
    K3m9SwqxBSlBBhNhsjPMOZFBVMB12UcG5CW/Qo2rrzpNA/dVrCIweobaBVrxu4X9TkvT7qm67ns
    IGQM8SHofcfRAGcwZQIwElspH+HhwSxyI59eG6a3juJvgbHBNKwIH72N9Si3TZaTyiskL6QUPH5
    Y9PLmtIX7AjEAiZaqz55O+EUmaxiizH76sVuWoCMReEgFJtSm5NM3trucfj20AiIZ6/MG3bsJ43
    fZ"
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams.md")
