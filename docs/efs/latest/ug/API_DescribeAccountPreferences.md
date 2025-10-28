# DescribeAccountPreferences

Returns the account preferences settings for the AWS account associated with the user making the request, in the current AWS Region.

## Request Syntax

```
GET /2015-02-01/account-preferences HTTP/1.1
Content-type: application/json

{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[MaxResults](#API_DescribeAccountPreferences_RequestSyntax "#API_DescribeAccountPreferences_RequestSyntax")**

(Optional) When retrieving account preferences,
you can optionally specify the `MaxItems` parameter to limit the number of objects returned in a response.
The default value is 100.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[NextToken](#API_DescribeAccountPreferences_RequestSyntax "#API_DescribeAccountPreferences_RequestSyntax")**

(Optional) You can use `NextToken` in a subsequent request to fetch the next page of
AWS account preferences if the response payload was paginated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "ResourceIdPreference": {
      "ResourceIdType": "***string***",
      "Resources": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeAccountPreferences_ResponseSyntax "#API_DescribeAccountPreferences_ResponseSyntax")**

Present if there are more records than returned in the response.
You can use the `NextToken` in the subsequent request to fetch the additional descriptions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[ResourceIdPreference](#API_DescribeAccountPreferences_ResponseSyntax "#API_DescribeAccountPreferences_ResponseSyntax")**

Describes the resource ID preference setting for the AWS account associated with the user making the request, in the current AWS Region.

Type: [ResourceIdPreference](API_ResourceIdPreference.md "API_ResourceIdPreference.md") object

## Errors

**InternalServerError**

Returned if an error occurred on the server side.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeAccountPreferences.md")
