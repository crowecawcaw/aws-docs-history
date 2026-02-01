# GetSupportedResourceTypes

Returns the AWS resource types supported by AWS Backup.

## Request Syntax

```
GET /supported-resource-types HTTP/1.1

```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceTypes": [ "***string***" ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ResourceTypes](#API_GetSupportedResourceTypes_ResponseSyntax "#API_GetSupportedResourceTypes_ResponseSyntax")**

Contains a string with the supported AWS resource types:

- `Aurora` for Amazon Aurora
- `CloudFormation` for AWS CloudFormation
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
- `EKS` for Amazon Elastic Kubernetes Service
- `FSx` for Amazon FSx
- `Neptune` for Amazon Neptune
- `RDS` for Amazon Relational Database Service
- `Redshift` for Amazon Redshift
- `S3` for Amazon Simple Storage Service (Amazon S3)
- `SAP HANA on Amazon EC2` for SAP HANA databases
  on Amazon Elastic Compute Cloud instances
- `Storage Gateway` for AWS Storage Gateway
- `Timestream` for Amazon Timestream
- `VirtualMachine` for VMware virtual machines

Type: Array of strings

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/cli2/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForCpp/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/boto3/backup-2018-11-15/GetSupportedResourceTypes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetSupportedResourceTypes.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetSupportedResourceTypes.md")
