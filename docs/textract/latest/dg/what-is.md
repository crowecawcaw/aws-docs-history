

# What is Amazon Textract?

Amazon Textract is a document analysis service that helps you add document text detection and analysis to your applications. It is available as Amazon Textract Core and Amazon Textract Insights, a generative AI capability. You can use either one, or both together, depending on your needs, without machine learning (ML) expertise, through simple API operations.

## Amazon Textract Core
<a name="textract-core"></a>

Amazon Textract Core detects and extracts printed text, handwriting, forms, tables, and layout information from images and scans of documents. It also includes specialized processing for invoices and receipts, identity documents, and mortgage loan packages. It provides a separate API for each task and returns results as building blocks, such as words, lines, and cells, or as a fixed set of fields for supported document types. You can use it synchronously for single-page documents or asynchronously for multi-page documents. For more information about Amazon Textract Core, see [Amazon Textract Core](amazon-textract-core.md).

## Amazon Textract Insights
<a name="textract-insights"></a>

Amazon Textract Insights builds on the text and layout extraction from Amazon Textract Core. It uses generative AI to turn unstructured documents into structured data. In a single asynchronous request, it can split a file that contains several documents and match each document to a blueprint. It extracts the fields you define, each with a confidence score and its location on the page. It can also return Markdown, HTML, and plain text for large language model (LLM) and retrieval-augmented generation (RAG) applications. It can generate document summaries and figure captions, and detect and redact personally identifiable information (PII). You can use Amazon Textract Insights in the US East (N. Virginia) and US West (Oregon) AWS Regions. For more information about Amazon Textract Insights, see [Amazon Textract Insights](amazon-textract-insights.md).

## Choosing between Amazon Textract Core and Amazon Textract Insights
<a name="choosing-core-insights"></a>

Choose Amazon Textract Core if you need synchronous responses, cell-level table detail, every key-value pair on a form, or only the raw text. Choose Amazon Textract Insights if you feed documents into an LLM or RAG pipeline, need specific fields in your own schema, process files that contain several documents, or need to redact personal data. Forms, Queries, and Custom Queries are available in Amazon Textract Core only. For more information about the differences, see [Amazon Textract Insights compared with Amazon Textract Core APIs](insights-compared-core.md).

**Note**  
Before you choose Amazon Textract Insights, confirm that it is available in the AWS Region you plan to use. Amazon Textract Insights is currently available only in the US East (N. Virginia) and US West (Oregon) AWS Regions.

## Common use cases
<a name="common-use-cases"></a>

Common use cases for Amazon Textract Core include the following:
+ Creating an intelligent search index from text detected in image and PDF files
+ Extracting text for natural language processing (NLP), grouped as words, lines, or table cells
+ Capturing and normalizing text and tabular data from a wide variety of documents, such as financial documents, research reports, and medical notes
+ Automating data capture from forms
+ Automating the classification and extraction of lending documents

Common use cases for Amazon Textract Insights include the following:
+ Splitting, classifying, and extracting data from mixed document packets, such as loan files, claims files, and onboarding packages
+ Turning invoices, tax forms, bank statements, pay stubs, and identity documents into structured records for downstream systems
+ Preparing documents for generative AI and RAG applications
+ Detecting and redacting PII before extracted content reaches downstream systems

## Where to start
<a name="where-to-start"></a>

To get started with Amazon Textract, see the following resources:
+ To start with Amazon Textract Core, see [First-time Amazon Textract Core users](first-time-user.md).
+ To start with Amazon Textract Insights, see [Getting started with Amazon Textract Insights](insights-getting-started.md).