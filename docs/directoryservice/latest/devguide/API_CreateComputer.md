# CreateComputer

Creates an Active Directory computer object in the specified directory.

## Request Syntax

```
{
   "ComputerAttributes": [
      {
         "Name": "`string`",
         "Value": "`string`"
      }
   ],
   "ComputerName": "`string`",
   "DirectoryId": "`string`",
   "OrganizationalUnitDistinguishedName": "`string`",
   "Password": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ComputerAttributes](#API_CreateComputer_RequestSyntax "#API_CreateComputer_RequestSyntax")**

An array of [Attribute](API_Attribute.md "API_Attribute.md") objects that contain any LDAP attributes to apply to the
computer account.

Type: Array of [Attribute](API_Attribute.md "API_Attribute.md") objects

Required: No

**[ComputerName](#API_CreateComputer_RequestSyntax "#API_CreateComputer_RequestSyntax")**

The name of the computer account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 15.

Required: Yes

**[DirectoryId](#API_CreateComputer_RequestSyntax "#API_CreateComputer_RequestSyntax")**

The identifier of the directory in which to create the computer account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[OrganizationalUnitDistinguishedName](#API_CreateComputer_RequestSyntax "#API_CreateComputer_RequestSyntax")**

The fully-qualified distinguished name of the organizational unit to place the computer account in.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

Required: No

**[Password](#API_CreateComputer_RequestSyntax "#API_CreateComputer_RequestSyntax")**

A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 64.

Pattern: `[\u0020-\u00FF]+`

Required: Yes

## Response Syntax

```
{
   "Computer": {
      "ComputerAttributes": [
         {
            "Name": "***string***",
            "Value": "***string***"
         }
      ],
      "ComputerId": "***string***",
      "ComputerName": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Computer](#API_CreateComputer_ResponseSyntax "#API_CreateComputer_ResponseSyntax")**

A [Computer](API_Computer.md "API_Computer.md") object that represents the computer account.

Type: [Computer](API_Computer.md "API_Computer.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AuthenticationFailedException**

An authentication error occurred.

**Message**

The textual message for the exception.

**RequestId**

The identifier of the request that caused the exception.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryUnavailableException**

The specified directory is unavailable.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityAlreadyExistsException**

The specified entity already exists.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of CreateComputer.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 245
X-Amz-Target: DirectoryService_20150416.CreateComputer
X-Amz-Date: 20161213T163452Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=5fa12f147bce3620568504361b860de07868da3b1c27d5f0bde6e5ffa51bf6ef

 {
   "DirectoryId":"d-926example",
   "ComputerName":"labcomputer",
   "Password":"Str0ngP@ssw0rd",
   "ComputerAttributes":[
      {
         "Name":"ip",
         "Value":"192.168.101.100"
      }
   ],
   "OrganizationalUnitDistinguishedName":"OU=Computers,OU=example,DC=corp,DC=example,DC=com"
 }
```

### Example Response

This example illustrates one usage of CreateComputer.

```
HTTP/1.1 200 OK
x-amzn-RequestId: afcea813-c196-11e6-a6a8-5110402a26c3
Content-Type: application/x-amz-json-1.1
Content-Length: 286
Date: Wed, 14 Dec 2016 00:46:03 GMT

{
   "Computer":{
      "ComputerAttributes":[
         {
            "Name":"DistinguishedName",
            "Value":"CN=labcomputer,OU=Computers,OU=example,DC=corp,DC=example,DC=com"
         },
         {
            "Name":"WindowsSamName",
            "Value":"labcomputer$"
         }
      ],
      "ComputerId":"S-1-5-21-1932691875-1648176379-1176097576-1124",
      "ComputerName":"labcomputer"
   }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateComputer.md "../../../goto/cli2/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/CreateComputer.md "../../../goto/DotNetSDKV4/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateComputer.md "../../../goto/boto3/ds-2015-04-16/CreateComputer.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateComputer.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateComputer.md")
