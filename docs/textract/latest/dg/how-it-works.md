

# Identifying your Amazon Textract Core use case

Amazon Textract Core offers a variety of operations that apply to different documents. Below is a list of the operations you can perform with Amazon Textract Core and links to further information on each use case. To check which languages each operation supports, see [Supported languages](supported-languages.md).
+ Detecting text only. For more information, see [Detecting text](how-it-works-detecting.md).
+ Detecting and analyzing relationships between text. For more information, see [Analyzing documents](how-it-works-analyzing.md).
+ Detecting and analyzing text in invoices and receipts. For more information, see [Analyzing invoices and receipts](invoices-receipts.md).
+ Detecting and analyzing text in government identity documents. For more information, see [Analyzing identity documents](how-it-works-identity.md).
+ Detecting and analyzing text in lending documents. For more information, see [Analyzing lending documents](lending-document-classification-extraction.md).

Amazon Textract Core provides you with synchronous operations for processing single-page documents with near real-time responses. For more information, see [Processing documents synchronously](sync.md). Amazon Textract Core also provides asynchronous operations that you can use to process larger, multipage documents. Asynchronous responses aren't in real time. For more information, see [Processing documents asynchronously](async.md). 

Amazon Textract Core provides you with a workflow to automatically classify lending document pages and route them to existing solutions. For more information, see [Analyzing lending documents](lending-document-classification-extraction.md).

 Amazon Textract Core lets you customize the output of its pretrained Queries feature. With Amazon Textract Core Custom Queries, you can use your own documents and train an adapter to customize the base model, keeping complete control over your proprietary documents. See [Customizing your Queries responses](textract-using-adapters.md) for more information. 

 For information regarding the results returned by Analyze Lending, see [Analyze Lending response objects](lending-response-objects.md).

**Topics**
+ [Detecting text](how-it-works-detecting.md)
+ [Analyzing documents](how-it-works-analyzing.md)
+ [Analyzing invoices and receipts](invoices-receipts.md)
+ [Analyzing identity documents](how-it-works-identity.md)
+ [Analyzing lending documents](lending-document-classification-extraction.md)
+ [Customizing outputs](how-it-works-custom-queries.md)