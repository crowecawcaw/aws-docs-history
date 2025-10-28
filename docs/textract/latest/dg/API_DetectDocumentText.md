# DetectDocumentText

Detects text in the input document. Amazon Textract can detect lines of text and the
words that make up a line of text. The input document must be in one of the following image
formats: JPEG, PNG, PDF, or TIFF. `DetectDocumentText` returns the detected
text in an array of [Block](API_Block.md "API_Block.md") objects.

Each document page has as an associated `Block` of type PAGE. Each PAGE `Block` object
is the parent of LINE `Block` objects that represent the lines of detected text on a page. A LINE `Block` object is
a parent for each word that makes up the line. Words are represented by `Block` objects of type WORD.

`DetectDocumentText` is a synchronous operation. To analyze documents
asynchronously, use [StartDocumentTextDetection](API_StartDocumentTextDetection.md "API_StartDocumentTextDetection.md").

For more information, see [Document Text Detection](how-it-works-detecting.md "how-it-works-detecting.md").

## Request Syntax

```
{
   "Document": {
      "Bytes": `blob`,
      "S3Object": {
         "Bucket": "`string`",
         "Name": "`string`",
         "Version": "`string`"
      }
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Document](#API_DetectDocumentText_RequestSyntax "#API_DetectDocumentText_RequestSyntax")**

The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI
to call Amazon Textract operations, you can't pass image bytes. The document must be an image
in JPEG or PNG format.

If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode
image bytes that are passed using the `Bytes` field.

Type: [Document](API_Document.md "API_Document.md") object

Required: Yes

## Response Syntax

```
{
   "Blocks": [
      {
         "BlockType": "***string***",
         "ColumnIndex": ***number***,
         "ColumnSpan": ***number***,
         "Confidence": ***number***,
         "EntityTypes": [ "***string***" ],
         "Geometry": {
            "BoundingBox": {
               "Height": ***number***,
               "Left": ***number***,
               "Top": ***number***,
               "Width": ***number***
            },
            "Polygon": [
               {
                  "X": ***number***,
                  "Y": ***number***
               }
            ],
            "RotationAngle": ***number***
         },
         "Id": "***string***",
         "Page": ***number***,
         "Query": {
            "Alias": "***string***",
            "Pages": [ "***string***" ],
            "Text": "***string***"
         },
         "Relationships": [
            {
               "Ids": [ "***string***" ],
               "Type": "***string***"
            }
         ],
         "RowIndex": ***number***,
         "RowSpan": ***number***,
         "SelectionStatus": "***string***",
         "Text": "***string***",
         "TextType": "***string***"
      }
   ],
   "DetectDocumentTextModelVersion": "***string***",
   "DocumentMetadata": {
      "Pages": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Blocks](#API_DetectDocumentText_ResponseSyntax "#API_DetectDocumentText_ResponseSyntax")**

An array of `Block` objects that contain the text that's detected in the
document.

Type: Array of [Block](API_Block.md "API_Block.md") objects

**[DetectDocumentTextModelVersion](#API_DetectDocumentText_ResponseSyntax "#API_DetectDocumentText_ResponseSyntax")**

Type: String

**[DocumentMetadata](#API_DetectDocumentText_ResponseSyntax "#API_DetectDocumentText_ResponseSyntax")**

Metadata about the document. It contains the number of pages that are detected in the
document.

Type: [DocumentMetadata](API_DocumentMetadata.md "API_DocumentMetadata.md") object

## Errors

**AccessDeniedException**

You aren't authorized to perform the action. Use the Amazon Resource Name (ARN)
of an authorized user or IAM role to perform the operation.

HTTP Status Code: 400

**BadDocumentException**

Amazon Textract isn't able to read the document. For more information on the document
limits in Amazon Textract, see [Quotas in Amazon Textract](limits.md "limits.md").

HTTP Status Code: 400

**DocumentTooLargeException**

The document can't be processed because it's too large. The maximum document size for
synchronous operations 10 MB. The maximum document size for asynchronous operations is 500
MB for PDF files.

HTTP Status Code: 400

**InternalServerError**

Amazon Textract experienced a service issue. Try your call again.

HTTP Status Code: 500

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

**ProvisionedThroughputExceededException**

The number of requests exceeded your throughput limit. If you want to increase this limit,
contact Amazon Textract.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**UnsupportedDocumentException**

The format of the input document isn't supported. Documents for operations can be in
PNG, JPEG, PDF, or TIFF format.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/DetectDocumentText.md "../../../goto/cli2/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/textract-2018-06-27/DetectDocumentText.md "../../../goto/DotNetSDKV3/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForCpp/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForGoV2/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForJavaV2/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForKotlin/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForPHPV3/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/DetectDocumentText.md "../../../goto/boto3/textract-2018-06-27/DetectDocumentText.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/DetectDocumentText.md "../../../goto/SdkForRubyV3/textract-2018-06-27/DetectDocumentText.md")
