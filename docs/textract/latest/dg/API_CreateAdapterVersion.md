# CreateAdapterVersion

Creates a new version of an adapter. Operates on a provided AdapterId and a specified
dataset provided via the DatasetConfig argument. Requires that you
specify an Amazon S3 bucket with the OutputConfig argument. You can provide an optional KMSKeyId,
an optional ClientRequestToken, and optional tags.

## Request Syntax

```
{
   "AdapterId": "`string`",
   "ClientRequestToken": "`string`",
   "DatasetConfig": {
      "ManifestS3Object": {
         "Bucket": "`string`",
         "Name": "`string`",
         "Version": "`string`"
      }
   },
   "KMSKeyId": "`string`",
   "OutputConfig": {
      "S3Bucket": "`string`",
      "S3Prefix": "`string`"
   },
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AdapterId](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

A string containing a unique ID for the adapter that will receive a new version.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: Yes

**[ClientRequestToken](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

Idempotent token is used to recognize the request. If the same token is used with multiple
CreateAdapterVersion requests, the same session is returned.
This token is employed to avoid unintentionally creating the same session multiple times.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^[a-zA-Z0-9-_]+$`

Required: No

**[DatasetConfig](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

Specifies a dataset used to train a new adapter version. Takes a ManifestS3Object as the
value.

Type: [AdapterVersionDatasetConfig](API_AdapterVersionDatasetConfig.md "API_AdapterVersionDatasetConfig.md") object

Required: Yes

**[KMSKeyId](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

**[OutputConfig](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

Sets whether or not your output will go to a user created bucket. Used to set the name
of the bucket, and the prefix on the output file.

`OutputConfig` is an optional parameter which lets you adjust where your
output will be placed. By default, Amazon Textract will store the results internally and can
only be accessed by the Get API operations. With `OutputConfig` enabled, you can
set the name of the bucket the output will be sent to the file prefix of the results where
you can download your results. Additionally, you can set the `KMSKeyID`
parameter to a customer master key (CMK) to encrypt your output. Without this parameter set
Amazon Textract will encrypt server-side using the AWS managed CMK for Amazon S3.

Decryption of Customer Content is necessary for processing of the documents by Amazon Textract. If your account
is opted out under an AI services opt out policy then all unencrypted Customer Content is immediately and permanently deleted after
the Customer Content has been processed by the service. No copy of of the output is retained by Amazon Textract. For information about how to opt out, see [Managing AI services opt-out policy.](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md")

For more information on data privacy,
see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

Type: [OutputConfig](API_OutputConfig.md "API_OutputConfig.md") object

Required: Yes

**[Tags](#API_CreateAdapterVersion_RequestSyntax "#API_CreateAdapterVersion_RequestSyntax")**

A set of tags (key-value pairs) that you want to attach to the adapter version.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

## Response Syntax

```
{
   "AdapterId": "***string***",
   "AdapterVersion": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AdapterId](#API_CreateAdapterVersion_ResponseSyntax "#API_CreateAdapterVersion_ResponseSyntax")**

A string containing the unique ID for the adapter that has received a new version.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

**[AdapterVersion](#API_CreateAdapterVersion_ResponseSyntax "#API_CreateAdapterVersion_ResponseSyntax")**

A string describing the new version of the adapter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors

**AccessDeniedException**

You aren't authorized to perform the action. Use the Amazon Resource Name (ARN)
of an authorized user or IAM role to perform the operation.

HTTP Status Code: 400

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 400

**IdempotentParameterMismatchException**

A `ClientRequestToken` input parameter was reused with an operation, but at
least one of the other input parameters is different from the previous call to the
operation.

HTTP Status Code: 400

**InternalServerError**

Amazon Textract experienced a service issue. Try your call again.

HTTP Status Code: 500

**InvalidKMSKeyException**

Indicates you do not have decrypt permissions with the KMS key entered, or the KMS key
was entered incorrectly.

HTTP Status Code: 400

**InvalidParameterException**

An input parameter violated a constraint. For example, in synchronous operations,
an `InvalidParameterException` exception occurs
when neither of the `S3Object` or `Bytes` values are supplied in the `Document`
request parameter.
Validate your parameter before calling the API operation again.

HTTP Status Code: 400

**InvalidS3ObjectException**

Amazon Textract is unable to access the S3 object that's specified in the request.
for more information, [Configure Access to Amazon S3](../../../AmazonS3/latest/dev/s3-access-control.md "../../../AmazonS3/latest/dev/s3-access-control.md")
For troubleshooting information, see [Troubleshooting Amazon S3](../../../AmazonS3/latest/dev/troubleshooting.md "../../../AmazonS3/latest/dev/troubleshooting.md")

HTTP Status Code: 400

**LimitExceededException**

An Amazon Textract service limit was exceeded. For example, if you start too many
asynchronous jobs concurrently, calls to start operations
(`StartDocumentTextDetection`, for example) raise a LimitExceededException
exception (HTTP status code: 400) until the number of concurrently running jobs is below
the Amazon Textract service limit.

HTTP Status Code: 400

**ProvisionedThroughputExceededException**

The number of requests exceeded your throughput limit. If you want to increase this limit,
contact Amazon Textract.

HTTP Status Code: 400

**ResourceNotFoundException**

Returned when an operation tried to access a nonexistent resource.

HTTP Status Code: 400

**ServiceQuotaExceededException**

Returned when a request cannot be completed as it would exceed a maximum service quota.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**ValidationException**

Indicates that a request was not valid. Check request for proper formatting.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/cli2/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/DotNetSDKV4/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForCpp/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForGoV2/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForJavaV2/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForKotlin/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForPHPV3/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/boto3/textract-2018-06-27/CreateAdapterVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/CreateAdapterVersion.md "../../../goto/SdkForRubyV3/textract-2018-06-27/CreateAdapterVersion.md")
