# Inputs for real-time custom analysis

Real-time analysis using custom models takes a single document as input. The following topics describe the input
document types that you can use.

###### Topics

- [Plain text documents](#idp-inputs-sync-text "#idp-inputs-sync-text")
- [Semi-structured documents](#idp-inputs-sync-semi "#idp-inputs-sync-semi")
- [Image files and scanned PDF files](#idp-inputs-sync-ocr "#idp-inputs-sync-ocr")
- [Amazon Textract output](#idp-inputs-sync-textract "#idp-inputs-sync-textract")
- [Maximum document sizes for real-time analysis](#idp-inputs-sync-sizes "#idp-inputs-sync-sizes")
- [Errors in semi-structured documents](#idp-inputs-sync-err "#idp-inputs-sync-err")

## Plain text documents

Provide the input document as UTF-8-formatted text.

## Semi-structured documents

Semi-structured documents include native PDF documents and Word documents.

By default, real-time custom analysis uses the Amazon Comprehend parser to extract the text from Word files and digital
PDF files. For PDF files, you can override this default and use Amazon Textract to extract the text. See [Setting text extraction options](idp-set-textract-options.md "idp-set-textract-options.md").

## Image files and scanned PDF files

Supported image types include JPEG, PNG, and TIFF.

By default, custom entity recognition uses the Amazon Textract `DetectDocumentText` API operation to
extract the text from image files and scanned PDF files. You can override this default to use the
`AnalyzeDocument` API operation instead. See [Setting text extraction options](idp-set-textract-options.md "idp-set-textract-options.md").

## Amazon Textract output

You can provide the JSON output from the Amazon Textract `DetectDocumentText` API or
`AnalyzeDocument` API as input to the real-time API operations for custom classification and custom
entity recognition. Amazon Comprehend supports this input type for the real-time API operations, but not for the
console.

## Maximum document sizes for real-time analysis

For all input document types, the input file maximum is one page, with no more than 10,000 characters.

The following table shows the maximum file sizes for input documents.

| File type             | Maximum size (API) | Maximum size (console) |
| --------------------- | ------------------ | ---------------------- |
| UTF-8 text documents  | 10 KB              | 10 KB                  |
| PDF documents         | 10 MB              | 5 MB                   |
| Word documents        | 10 MB              | 1 MB                   |
| Image files           | 10 MB              | 5 MB                   |
| Textract output files | 1 MB               | n/a                    |

## Errors in semi-structured documents

The [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") or [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md") API operation can encounter document-level or page-level errors
while extracting text from a semi-structured document or an image file.

### Page-level errors

If the [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") or [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md") API operation encounters errors while processing a page in the input document,
the API response includes an entry in the [Errors list](../APIReference/API_ErrorsListItem.md "../APIReference/API_ErrorsListItem.md") for each error.

The `ErrorCode` in the error list entry contains one of the following values:

- TEXTRACT_BAD_PAGE – Amazon Textract cannot read the page. For more information about page limits in
  Amazon Textract, see [Page Quotas in
  Amazon Textract](../../../textract/latest/dg/limits-document.md "../../../textract/latest/dg/limits-document.md").
- TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED – The number of requests exceeded your throughput limit.
  For more information about throughput quotas in Amazon Textract, see [Default quotas in Amazon Textract](../../../textract/latest/dg/limits-quotas-explained.md "../../../textract/latest/dg/limits-quotas-explained.md").
- PAGE_CHARACTERS_EXCEEDED – Too many text characters on the page (10,000 characters maximum).
- PAGE_SIZE_EXCEEDED – The maximum page size is 10 MB.
- INTERNAL_SERVER_ERROR – The request encountered a service issue. Try the API request again.

### Document-level errors

If the [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") or [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md") API operation detects a document-level error in your input document,
the API returns an `InvalidRequestException` error response.

In the error response, the **Reason** field contains the value `INVALID_DOCUMENT`.

The **Detail** field contains one of the following values:

- DOCUMENT_SIZE_EXCEEDED – Document size is too large. Check the size of your file and resubmit the request.
- UNSUPPORTED_DOC_TYPE – Document type is not supported. Check the file type and resubmit the request.
- PAGE_LIMIT_EXCEEDED – Too many pages in the document. Check the number of pages in your file and
  resubmit the request.
- TEXTRACT_ACCESS_DENIED_EXCEPTION – Access denied to Amazon Textract. Verify that your account has permission to use the
  Amazon Textract [DetectDocumentText](../../../textract/latest/dg/API_DetectDocumentText.md "../../../textract/latest/dg/API_DetectDocumentText.md") and
  [AnalyzeDocument](../../../textract/latest/dg/API_AnalyzeDocument.md "../../../textract/latest/dg/API_AnalyzeDocument.md")
  API operations and resubmit the request.
