

# Amazon Textract Core

Amazon Textract Core provides a set of application programming interfaces (APIs) for detecting text and analyzing documents. Using Amazon Textract Core, you can do the following:
+ Detect typed and handwritten text in a variety of documents, including financial reports, medical records, and tax forms.
+ Extract text, forms, tables, signatures, and layout elements from documents with structured data, using the Amazon Textract Core Analyze Document API.
+ Specify and extract information from documents using the Queries feature within the Amazon Textract Core Analyze Document API.
+ Process invoices and receipts with the `AnalyzeExpense` API.
+ Process ID documents, such as driver's licenses and passports issued by the U.S. government, using the `AnalyzeID` API.
+ Upload and process mortgage loan packages, through automatic routing of the document pages to the appropriate Amazon Textract analysis operations using the Analyze Lending workflow. You can retrieve analysis results for each document page or retrieve summarized results for a set of document pages.
+ Use Custom Queries to customize the pretrained Queries feature using your data to support your downstream processing needs.

Amazon Textract Core is based on the same proven, highly scalable, deep-learning technology that was developed by Amazon's computer vision scientists to analyze billions of images and videos daily. You don't need any machine learning expertise to use it, as Amazon Textract Core includes simple, easy-to-use API operations that can analyze image files and PDF files. Amazon is continually adding new features to the service.

With synchronous processing, Amazon Textract Core can analyze single-page documents for applications where latency is critical. Amazon Textract Core also provides asynchronous operations to extend support to multi-page documents.

## Common use cases
<a name="core-common-use-cases"></a>

The following are common use cases for Amazon Textract Core:
+ **Creating an intelligent search index** – Using Amazon Textract Core, you can create libraries of text that is detected in image and PDF files.
+ **Using intelligent text extraction for natural language processing (NLP)** – Amazon Textract Core provides you with control over how text is grouped as an input for NLP applications. It can extract text as words and lines. It also groups text by table cells if document table analysis is enabled.
+ **Accelerating the capture and normalization of data from different sources** – Amazon Textract Core enables text and tabular data extraction from a wide variety of documents, such as financial documents, research reports, and medical notes. With the Analyze Document APIs, you can quickly extract unstructured and structured data from your documents.
+ **Automating data capture from forms** – Amazon Textract Core enables extraction of structured data from forms. With the Analysis APIs, you can build extraction capabilities into existing business workflows so that user data submitted through forms can be extracted into a usable format.
+ **Automating document classification and extraction** – With the Analyze Lending document processing API, you can automate the classification of lending documents into various document classes, and then automatically route the classified pages to the correct analysis operation for further processing.

## Benefits
<a name="core-benefits"></a>

Some of the benefits of using Amazon Textract Core include the following:
+ **Integration of document text detection into your apps** – Amazon Textract Core removes the complexity of building text detection capabilities into your applications by making powerful and accurate analysis available with a simple API. You don't need computer vision or deep learning expertise to detect document text. With the Text APIs, you can build text detection into any web, mobile, or connected device application.
+ **Scalable document analysis** – Amazon Textract Core enables you to analyze and extract data quickly from millions of documents, which can accelerate decision making.
+ **Low cost** – With Amazon Textract Core, you only pay for the documents you analyze. There are no minimum fees or upfront commitments. You can get started for free, and save more as you grow with a tiered pricing model.

## Quotas
<a name="core-quotas"></a>

Amazon Textract Core's API operations have quotas that limit how quickly and how often you can use them. If the quota set for your account is frequently exceeded, you can request a quota increase. To change a quota, select the **Amazon Textract** option in the Service Quotas console. You can use the Quotas Calculator in the Amazon Textract console to determine your quota requirements. For more information about default quotas that can be changed, see [Modifying default quotas in Amazon Textract Core](limits-quotas-explained.md).

Other quotas, such as file size and languages supported by Amazon Textract Core, cannot be changed. For more information about set quotas, see [Set quotas in Amazon Textract Core](limits-document.md).

## Related information
<a name="core-related-information"></a>

To split, classify, and extract data from documents in a single request using generative AI, see [Amazon Textract Insights](amazon-textract-insights.md).

You can also process documents by asking your AI coding agent in natural language. See [Amazon Textract document processing skill](textract-document-processing-skill.md).