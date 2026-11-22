

# Processing documents synchronously

Amazon Textract Core can detect and analyze text in single-page documents that are provided as images in JPEG, PNG, PDF, and TIFF format. The operations are synchronous and return results in near real time. For more information about documents, see [Text detection and document analysis response objects](how-it-works-document-layout.md).

This section covers how you can use Amazon Textract Core to detect and analyze text in a single-page document synchronously. To detect and analyze text in multipage documents, or to detect JPEG and PNG documents asynchronously, see [Processing documents asynchronously](async.md).

You can use Amazon Textract Core synchronous operations for the following purposes:
+ Text detection – You can detect lines and words on a single-page document image by using the [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/APIReference/API_DetectDocumentText.html) operation. For more information, see [Detecting text](how-it-works-detecting.md).
+ Text analysis – You can identify relationships between detected text on a single-page document by using the [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/APIReference/API_AnalyzeDocument.html) operation. For more information, see [Analyzing documents](how-it-works-analyzing.md).
+ Invoice and receipt analysis – You can identify financial relationships between detected text on a single-page invoice or receipt using the AnalyzeExpense operation. For more information, see [Analyzing invoices and receipts](invoices-receipts.md).
+ Identity document analysis – You can analyze identity documents issued by the U.S. government and extract common types of information found on identity documents. For more information, see [Analyzing identity documents](how-it-works-identity.md). 

**Topics**
+ [Calling Amazon Textract Core synchronous operations](sync-calling.md)
+ [Detecting document text with Amazon Textract Core](detecting-document-text.md)
+ [Analyzing document text with Amazon Textract Core](analyzing-document-text.md)
+ [Analyzing invoices and receipts with Amazon Textract Core](analyzing-document-expense.md)
+ [Analyzing identity documentation with Amazon Textract Core](analyzing-document-identity.md)