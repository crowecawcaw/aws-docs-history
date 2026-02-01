# PutAccountPreferences

Use this operation to set the account preference in the current AWS Region
to use long 17 character (63 bit) or short 8 character (32 bit) resource IDs for new
EFS file system and mount target resources. All existing resource IDs are not
affected by any changes you make. You can set the ID preference during the opt-in period as
EFS transitions to long resource IDs. For more information, see [Managing Amazon EFS resource IDs](manage-efs-resource-ids.md "manage-efs-resource-ids.md").

###### Note

Starting in October, 2021, you will receive an error if you try to set the account preference
to use the short 8 character format resource ID. Contact AWS support if you
receive an error and must use short IDs for file system and mount target resources.

## Request Syntax

```
PUT /2015-02-01/account-preferences HTTP/1.1
Content-type: application/json

{
   "ResourceIdType": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ResourceIdType](#API_PutAccountPreferences_RequestSyntax "#API_PutAccountPreferences_RequestSyntax")**

Specifies the EFS resource ID preference to set for the user's AWS account, in the current AWS Region, either `LONG_ID`
(17 characters), or `SHORT_ID` (8 characters).

###### Note

Starting in October, 2021, you will receive an error when setting the account preference to
`SHORT_ID`. Contact AWS support if you receive an error and must
use short IDs for file system and mount target resources.

Type: String

Valid Values: `LONG_ID | SHORT_ID`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceIdPreference": {
      "ResourceIdType": "***string***",
      "Resources": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ResourceIdPreference](#API_PutAccountPreferences_ResponseSyntax "#API_PutAccountPreferences_ResponseSyntax")**

Describes the resource type and its ID preference for the user's AWS account, in the current AWS Region.

Type: [ResourceIdPreference](API_ResourceIdPreference.md "API_ResourceIdPreference.md") object

## Errors

**BadRequest**

Returned if the request is malformed or contains an error such as an invalid
parameter value or a missing required parameter.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/cli2/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/boto3/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutAccountPreferences.md")
