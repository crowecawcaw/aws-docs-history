

# Processing Documents Asynchronously
<a name="async"></a>

You can use Amazon Textract to detect and analyze text in multipage documents in PDF or TIFF format, including invoices and receipts. Multipage document processing is an asynchronous operation, and it is useful for processing large, multipage documents. For example, a PDF file with over 1,000 pages takes a long time to process, but processing the PDF file asynchronously allows your application to complete other tasks while the operation completes.

This section describes how you can use Amazon Textract to asynchronously detect and analyze text on a multipage or single-page document. Multipage documents must be in PDF or TIFF format. Single-page documents processed with asynchronous operations can be in JPEG, PNG, TIFF or PDF format.

You can use Amazon Textract asynchronous operations for the following purposes:
+ Text detection – You can detect lines and words on a multipage document. The asynchronous operations are [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentTextDetection.html) and [GetDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetDocumentTextDetection.html). For more information, see [Detecting Text](how-it-works-detecting.md).
+ Text analysis – You can identify relationships between detected text on a multipage document. The asynchronous operations are [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentAnalysis.html) and [GetDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetDocumentAnalysis.html). For more information, see [Analyzing Documents](how-it-works-analyzing.md).
+ Expense analysis – You can identify data relationships on multipage invoices and receipts. Amazon Textract treats each invoice or a receipt page of a multi-page document as an individual receipt or an invoice. It does not retain the context from one page to another of a multi-page document. The asynchronous operations are [StartExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartExpenseAnalysis.html) and [GetExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetExpenseAnalysis.html). For more information, see [Analyzing Invoices and Receipts](invoices-receipts.md).
+ Lending document analysis – You can classify and analyze lending documents using the Analyze Lending workflow, which classifies documents and then automatically sends the documents to the proper Amazon Textract operation for information extraction. You can start the asynchronous analysis of lending documents with `StartLendingAnalysis`, and retrieve the extracted information with `GetLendingAnalysis` or get a summary of the information with `GetLendingAnalysisSummary`. Analyze Lending returns the relevant information extracted from the documents, including detected signatures. You can also get the different types of documents in the submitted package, split by the logical boundaries for a given document type, if you use the `OutputConfig` feature.

**Topics**
+ [Calling Amazon Textract Asynchronous Operations](api-async.md)
+ [Configuring Amazon Textract for Asynchronous Operations](api-async-roles.md)
+ [Detecting or Analyzing Text in a Multipage Document](async-analyzing-with-sqs.md)
+ [Using the Analyze Lending Workflow](async-using-lending.md)
+ [Amazon Textract Results Notification](async-notification-payload.md)