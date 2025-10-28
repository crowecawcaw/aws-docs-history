# ListTags

Returns the tags assigned to the resource, such as a target recovery point, backup plan,
or backup vault.

This operation returns results depending on the resource type used in the value for
`resourceArn`. For example, recovery points of Amazon DynamoDB with
Advanced Settings have an ARN (Amazon Resource Name) that begins with
`arn:aws:backup`. Recovery points (backups) of DynamoDB without
Advanced Settings enabled have an ARN that begins with
`arn:aws:dynamodb`.

When this operation is called and when you include values of `resourceArn`
that have an ARN other than `arn:aws:backup`, it may return one of the
exceptions listed below. To prevent this exception, include only values representing
resource types that are fully managed by AWS Backup. These have an ARN that begins
`arn:aws:backup` and they are noted in the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table.

## Request Syntax

```
GET /tags/`resourceArn`/?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListTags_RequestSyntax "#API_ListTags_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListTags_RequestSyntax "#API_ListTags_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

**[resourceArn](#API_ListTags_RequestSyntax "#API_ListTags_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the type of resource. Valid targets for `ListTags` are recovery
points, backup plans, and backup vaults.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTags_ResponseSyntax "#API_ListTags_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

**[Tags](#API_ListTags_ResponseSyntax "#API_ListTags_ResponseSyntax")**

Information about the tags.

Type: String to string map

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListTags.md "../../../goto/cli2/backup-2018-11-15/ListTags.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListTags.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListTags.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListTags.md "../../../goto/SdkForCpp/backup-2018-11-15/ListTags.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListTags.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListTags.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListTags.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListTags.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListTags.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListTags.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListTags.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListTags.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListTags.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListTags.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListTags.md "../../../goto/boto3/backup-2018-11-15/ListTags.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListTags.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListTags.md")
