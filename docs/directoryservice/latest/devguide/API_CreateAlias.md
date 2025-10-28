# CreateAlias

Creates an alias for a directory and assigns the alias to the directory. The alias is used
to construct the access URL for the directory, such as
`http://<alias>.awsapps.com`.

###### Important

After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

## Request Syntax

```
{
   "Alias": "`string`",
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Alias](#API_CreateAlias_RequestSyntax "#API_CreateAlias_RequestSyntax")**

The requested alias.

The alias must be unique amongst all aliases in AWS. This operation throws an
`EntityAlreadyExistsException` error if the alias already exists.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 62.

Pattern: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`

Required: Yes

**[DirectoryId](#API_CreateAlias_RequestSyntax "#API_CreateAlias_RequestSyntax")**

The identifier of the directory for which to create the alias.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "Alias": "***string***",
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Alias](#API_CreateAlias_ResponseSyntax "#API_CreateAlias_ResponseSyntax")**

The alias for the directory.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 62.

Pattern: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`

**[DirectoryId](#API_CreateAlias_ResponseSyntax "#API_CreateAlias_ResponseSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

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

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of CreateAlias.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 52X-Amz-Target:DirectoryService_20150416.CreateAlias
X-Amz-Date: 20161209T175951Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161209/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=673029721752b71c1ff4752d0e42e6a05283c305238538d746c2b42d7864ec11

 {
   "DirectoryId": "d-926example",
   "Alias": "myaccess"
 }
```

### Example Response

This example illustrates one usage of CreateAlias.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 49abfbf6-be39-11e6-9458-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 49
Date: Fri, 09 Dec 2016 17:59:57 GMT

{
  "Alias": "myaccess",
  "DirectoryId": "d-926example"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateAlias.md "../../../goto/cli2/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/CreateAlias.md "../../../goto/DotNetSDKV3/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateAlias.md "../../../goto/boto3/ds-2015-04-16/CreateAlias.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateAlias.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateAlias.md")
