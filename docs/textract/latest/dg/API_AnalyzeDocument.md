# AnalyzeDocument

Analyzes an input document for relationships between detected items.

The types of information returned are as follows:

- Form data (key-value pairs). The related information is returned in two [Block](API_Block.md "API_Block.md") objects, each of type `KEY_VALUE_SET`: a KEY
  `Block` object and a VALUE `Block` object. For example,
  _Name: Ana Silva Carolina_ contains a key and value.
  _Name:_ is the key. _Ana Silva Carolina_ is
  the value.
- Table and table cell data. A TABLE `Block` object contains information
  about a detected table. A CELL `Block` object is returned for each cell in
  a table.
- Lines and words of text. A LINE `Block` object contains one or more
  WORD `Block` objects. All lines and words that are detected in the
  document are returned (including text that doesn't have a relationship with the value
  of `FeatureTypes`).
- Signatures. A SIGNATURE `Block` object contains the location information
  of a signature in a document. If used in conjunction with forms or tables, a signature
  can be given a Key-Value pairing or be detected in the cell of a table.
- Query. A QUERY Block object contains the query text, alias and link to the
  associated Query results block object.
- Query Result. A QUERY_RESULT Block object contains the answer to the query and an
  ID that connects it to the query asked. This Block also contains a confidence
  score.
  Selection elements such as check boxes and option buttons (radio buttons) can be
  detected in form data and in tables. A SELECTION_ELEMENT `Block` object contains
  information about a selection element, including the selection status.

You can choose which type of analysis to perform by specifying the
`FeatureTypes` list.

The output is returned in a list of `Block` objects.

`AnalyzeDocument` is a synchronous operation. To analyze documents
asynchronously, use [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md").

For more information, see [Document Text
Analysis](how-it-works-analyzing.md "how-it-works-analyzing.md").

## Request Syntax

```
{
   "AdaptersConfig": {
      "Adapters": [
         {
            "AdapterId": "`string`",
            "Pages": [ "`string`" ],
            "Version": "`string`"
         }
      ]
   },
   "Document": {
      "Bytes": `blob`,
      "S3Object": {
         "Bucket": "`string`",
         "Name": "`string`",
         "Version": "`string`"
      }
   },
   "FeatureTypes": [ "`string`" ],
   "HumanLoopConfig": {
      "DataAttributes": {
         "ContentClassifiers": [ "`string`" ]
      },
      "FlowDefinitionArn": "`string`",
      "HumanLoopName": "`string`"
   },
   "QueriesConfig": {
      "Queries": [
         {
            "Alias": "`string`",
            "Pages": [ "`string`" ],
            "Text": "`string`"
         }
      ]
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AdaptersConfig](#API_AnalyzeDocument_RequestSyntax "#API_AnalyzeDocument_RequestSyntax")**

Specifies the adapter to be used when analyzing a document.

Type: [AdaptersConfig](API_AdaptersConfig.md "API_AdaptersConfig.md") object

Required: No

**[Document](#API_AnalyzeDocument_RequestSyntax "#API_AnalyzeDocument_RequestSyntax")**

The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS
CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an
image in JPEG, PNG, PDF, or TIFF format.

If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode
image bytes that are passed using the `Bytes` field.

Type: [Document](API_Document.md "API_Document.md") object

Required: Yes

**[FeatureTypes](#API_AnalyzeDocument_RequestSyntax "#API_AnalyzeDocument_RequestSyntax")**

A list of the types of analysis to perform. Add TABLES to the list to return information
about the tables that are detected in the input document. Add FORMS to return detected form
data. Add SIGNATURES to return the locations of detected signatures. Add LAYOUT to the list
to return information about the layout of the document. All lines and words detected in the document are included in the response (including
text that isn't related to the value of `FeatureTypes`).

Type: Array of strings

Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

Required: Yes

**[HumanLoopConfig](#API_AnalyzeDocument_RequestSyntax "#API_AnalyzeDocument_RequestSyntax")**

Sets the configuration for the human in the loop workflow for analyzing
documents.

Type: [HumanLoopConfig](API_HumanLoopConfig.md "API_HumanLoopConfig.md") object

Required: No

**[QueriesConfig](#API_AnalyzeDocument_RequestSyntax "#API_AnalyzeDocument_RequestSyntax")**

Contains Queries and the alias for those Queries, as determined by the input.

Type: [QueriesConfig](API_QueriesConfig.md "API_QueriesConfig.md") object

Required: No

## Response Syntax

```
{
   "AnalyzeDocumentModelVersion": "***string***",
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
   "DocumentMetadata": {
      "Pages": ***number***
   },
   "HumanLoopActivationOutput": {
      "HumanLoopActivationConditionsEvaluationResults": "***string***",
      "HumanLoopActivationReasons": [ "***string***" ],
      "HumanLoopArn": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AnalyzeDocumentModelVersion](#API_AnalyzeDocument_ResponseSyntax "#API_AnalyzeDocument_ResponseSyntax")**

The version of the model used to analyze the document.

Type: String

**[Blocks](#API_AnalyzeDocument_ResponseSyntax "#API_AnalyzeDocument_ResponseSyntax")**

The items that are detected and analyzed by `AnalyzeDocument`.

Type: Array of [Block](API_Block.md "API_Block.md") objects

**[DocumentMetadata](#API_AnalyzeDocument_ResponseSyntax "#API_AnalyzeDocument_ResponseSyntax")**

Metadata about the analyzed document. An example is the number of pages.

Type: [DocumentMetadata](API_DocumentMetadata.md "API_DocumentMetadata.md") object

**[HumanLoopActivationOutput](#API_AnalyzeDocument_ResponseSyntax "#API_AnalyzeDocument_ResponseSyntax")**

Shows the results of the human in the loop evaluation.

Type: [HumanLoopActivationOutput](API_HumanLoopActivationOutput.md "API_HumanLoopActivationOutput.md") object

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

**HumanLoopQuotaExceededException**

Indicates you have exceeded the maximum number of active human in the loop workflows available

**QuotaCode**

The quota code.

**ResourceType**

The resource type.

**ServiceCode**

The service code.

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

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/AnalyzeDocument.md "../../../goto/cli2/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/textract-2018-06-27/AnalyzeDocument.md "../../../goto/DotNetSDKV3/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForCpp/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForGoV2/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForKotlin/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForPHPV3/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/AnalyzeDocument.md "../../../goto/boto3/textract-2018-06-27/AnalyzeDocument.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AnalyzeDocument.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AnalyzeDocument.md")
