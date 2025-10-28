# Best Practices for Bulk Document Uploader

The Bulk Document Uploader is an AWS Management Console tool intended to help you quickly
evaluate how Textract performs on a set of your own documents, without the need to write any
code. You can use the Bulk Document Uploader to process as many as 150 documents with one of
Textract’s features, instead of uploading and processing documents individually. You can bulk-
upload documents directly from your computer or import documents from an existing Amazon S3 bucket.

The Bulk Document Uploader provides results that you can download later for offline review.
Each downloadable zip file contains both the Textract JSON API response file and human-readable
CSV files of the output. The output results are available for download for 7 days after
processing. After 14 days, documents are cleared from the Submitted Documents panel.

# To use the Bulk Document Uploader, follow these steps:

1. Log in to the AWS Management Console and go to the Amazon Textract console.
2. Select the Bulk Document Uploader from the navigation pane.
3. Select the Upload Documents button.
4. Specify the source of your documents.
   1. If you are using an Amazon S3 bucket for your documents, provide
      the S3 URL for the bucket and folder. If the folder you specified
      contains more than 150 documents, then only the top 150 documents
      listed in the S3 folder will be sent to Textract for processing.
   2. If you are uploading documents from your local device, you can
      upload up to 50 documents at one time. To upload additional documents
      (up to the maximum of 150), click the Add Documents button after your
      initial documents are uploaded.

   When uploading documents from your computer, your documents are uploaded
   to an Amazon S3 bucket that is created on your behalf. In the future, you
   can use the path to this S3 bucket to process the same set of documents .

5. Specify the Textract feature you want to use to process your documents.
   Select one Textract feature at a time to process your documents. You must
   create a separate request if you want to test more than one feature on
   your documents.

If you select the “AnalyzeDocument - Queries” feature, write the Queries
you want to test against your documents. Queries are only applied to the
first page of each uploaded document. Consult the Queries Best Practices
section when constructing your queries. 6. Select the Start Processing button to submit the documents to Textract for processing. 7. You can track document status and download the output results of processed
documents in the Submitted Documents panel. After documents are submitted to
Textract for processing, they are displayed as a list in the Submitted Documents
panel. Each document is processed individually. The following information is
displayed for each document: Name, Status, Upload Date, Document Type, Textract
Feature, and Size.
The Submitted Documents panel updates periodically, and you can manually refresh it to see if your processing is complete.

## Limits

The following limits apply when using the Bulk Document Uploader

- Accepted File Formats: JPEG, PNG, PDF, and TIFF files. (JPEG 2000-encoded images within PDFs are supported)
- File Size and Page Count Limits: JPEG and PNG files have a 10 MB size limit. PDF and TIFF files have a 500 MB limit.
- PDF and TIFF files have a limit of 3,000 pages.
- Up to 150 documents can be processed for each bulk processing request. To process more than 150 documents,
  submit multiple requests of up to 150 documents each by using the Bulk Document Uploader.
- The AnalyzeLending and AnalyzeID API operations are not supported by the Bulk Document Uploader.
- The Bulk Document Uploader incurs the same charges as regular Textract usage.
  For more information on Textract pricing, see [here](https://aws.amazon.com/textract/pricing/ "https://aws.amazon.com/textract/pricing/").
