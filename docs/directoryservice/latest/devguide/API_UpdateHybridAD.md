# UpdateHybridAD

Updates the configuration of an existing hybrid directory. You can recover hybrid
directory administrator account or modify self-managed instance settings.

Updates are applied asynchronously. Use [DescribeHybridADUpdate](API_DescribeHybridADUpdate.md "API_DescribeHybridADUpdate.md") to
monitor the progress of configuration changes.

The `InstanceIds` must have a one-to-one correspondence with
`CustomerDnsIps`, meaning that if the IP address for instance i-10243410
is 10.24.34.100 and the IP address for instance i-10243420 is 10.24.34.200, then the
input arrays must maintain the same order relationship, either [10.24.34.100,
10.24.34.200] paired with [i-10243410, i-10243420] or [10.24.34.200, 10.24.34.100]
paired with [i-10243420, i-10243410].

###### Note

You must provide at least one update to [UpdateHybridAD:HybridAdministratorAccountUpdate](#DirectoryService-UpdateHybridAD-request-HybridAdministratorAccountUpdate "#DirectoryService-UpdateHybridAD-request-HybridAdministratorAccountUpdate") or [UpdateHybridAD:SelfManagedInstancesSettings](#DirectoryService-UpdateHybridAD-request-SelfManagedInstancesSettings "#DirectoryService-UpdateHybridAD-request-SelfManagedInstancesSettings").

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "HybridAdministratorAccountUpdate": {
      "SecretArn": "`string`"
   },
   "SelfManagedInstancesSettings": {
      "CustomerDnsIps": [ "`string`" ],
      "InstanceIds": [ "`string`" ]
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_UpdateHybridAD_RequestSyntax "#API_UpdateHybridAD_RequestSyntax")**

The identifier of the hybrid directory to update.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[HybridAdministratorAccountUpdate](#API_UpdateHybridAD_RequestSyntax "#API_UpdateHybridAD_RequestSyntax")**

We create a hybrid directory administrator account when we create a hybrid directory.
Use `HybridAdministratorAccountUpdate` to recover the hybrid directory
administrator account if you have deleted it.

To recover your hybrid directory administrator account, we need temporary access to a
user in your self-managed AD with administrator permissions in the form of a secret from
AWS Secrets Manager. We use these credentials once during recovery and don't store them.

If your hybrid directory administrator account exists, then you don’t need to use
`HybridAdministratorAccountUpdate`, even if you have updated your
self-managed AD administrator user.

Type: [HybridAdministratorAccountUpdate](API_HybridAdministratorAccountUpdate.md "API_HybridAdministratorAccountUpdate.md") object

Required: No

**[SelfManagedInstancesSettings](#API_UpdateHybridAD_RequestSyntax "#API_UpdateHybridAD_RequestSyntax")**

Updates to the self-managed AD configuration, including DNS server IP addresses and
AWS System Manager managed node identifiers.

Type: [HybridCustomerInstancesSettings](API_HybridCustomerInstancesSettings.md "API_HybridCustomerInstancesSettings.md") object

Required: No

## Response Syntax

```
{
   "AssessmentId": "***string***",
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AssessmentId](#API_UpdateHybridAD_ResponseSyntax "#API_UpdateHybridAD_ResponseSyntax")**

The identifier of the assessment performed to validate the update configuration. This
assessment ensures the updated settings are compatible with your environment.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

**[DirectoryId](#API_UpdateHybridAD_ResponseSyntax "#API_UpdateHybridAD_ResponseSyntax")**

The identifier of the updated hybrid directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ADAssessmentLimitExceededException**

A directory assessment is automatically created when you create a hybrid directory.
There are two types of assessments: `CUSTOMER` and `SYSTEM`. Your
AWS account has a limit of 100 `CUSTOMER` directory assessments.

If you attempt to create a hybrid directory; and you already have 100
`CUSTOMER` directory assessments;, you will encounter an error. Delete
assessments to free up capacity before trying again.

You can request an increase to your `CUSTOMER` directory assessment quota
by contacting customer support or delete existing CUSTOMER directory assessments; to
free up capacity.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

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

This example illustrates one usage of UpdateHybridAD.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 245
X-Amz-Target: DirectoryService_20150416.UpdateHybridAD
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
    "DirectoryId": d-926example,
    "HybridAdministratorAccountUpdate": {
        "SecretArn": "arn:aws:secretsmanager:eu-west-1:111122223333:secret:CredExample-DZESji"
    },
    "SelfManagedInstancesSettings": {
        "CustomerDnsIps": ["10.24.34.100", "10.24.34.200"],
        "InstanceIds": ["i-10243410", "i-10243420"],
    }
}
```

### Example Response

This example illustrates one usage of UpdateHybridAD.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 75
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "DirectoryId": "d-926example",
    "AssessmentId": "da-1234567890example1"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateHybridAD.md "../../../goto/cli2/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/UpdateHybridAD.md "../../../goto/DotNetSDKV4/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateHybridAD.md "../../../goto/boto3/ds-2015-04-16/UpdateHybridAD.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateHybridAD.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateHybridAD.md")
