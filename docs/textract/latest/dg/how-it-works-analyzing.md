# Analyzing Documents

Amazon Textract analyzes documents and forms for relationships among detected text.
Amazon Textract analysis operations return 5 categories of document extraction — text,
forms, tables, query responses, and signatures. The analysis of invoices and receipts is
handled through a different process, for more information see [Analyzing Invoices and Receipts](invoices-receipts.md "invoices-receipts.md").

###### Text Extraction

The raw text extracted from a document. For more information, see [Lines and words of text](how-it-works-lines-words.md "how-it-works-lines-words.md").

###### Form Extraction

Form data is linked to text items extracted from a document. Amazon Textract
represents form data as key-value pairs.

In the following example, one of the lines of text detected by Amazon Textract is
_Name: Jane Doe_. Amazon Textract also identifies a key
(_Name:_) and a value (_Jane Doe_). For more
information, see [Form data (Key-value
pairs)](how-it-works-kvp.md "how-it-works-kvp.md").

_Name: Jane Doe_

_Address: 123 Any Street, Anytown, USA_

_Birth date: 12-26-1980_

Key-value pairs are also used to represent check boxes or option buttons (radio
buttons) that are extracted from forms.

_Male:_ ☑

For more information, see [Selection
elements](how-it-works-selectables.md "how-it-works-selectables.md").

###### Table Extraction

Amazon Textract can extract tables, table cells, the items within table cells,
table titles and footers, and the type of table. Amazon Textract can also be programmed
to return the results in a JSON, CSV, or TXT file.

| Name         | Address      |
| ------------ | ------------ |
| Ana Carolina | 123 Any Town |

For more information, see [Tables](how-it-works-tables.md "how-it-works-tables.md"). Selection
elements can also be extracted from tables. For more information, see [Selection elements](how-it-works-selectables.md "how-it-works-selectables.md").

###### Signatures in Document Analysis

Amazon Textract can detect the locations of signatures in text documents. These are
returned as geometry objects with bounding boxes that provide the location of a
signature on the page, alongside the confidence that a signature is in that
location. If the signature feature is used by itself, Amazon Textract will return both
signatures and standard text detection results. Signature detection can be used in
conjunction with other feature types such as forms, tables, and queries. When using
it with forms and tables, signatures can be detected as part of a key-value pair or
within a table cell respectively.

###### Queries in Document Analysis

When processing a document with Amazon Textract, you may add queries to your
analysis to specify what information you need. This involves passing a question,
such as "What is the customer's social security number?" to Amazon Textract. Amazon
Textract will then find the information in the document for that question and return
it in a response structure separate from the rest of the document's information. For
more information about this response structure, see [Query Response Structures](queryresponse.md "queryresponse.md"). For more information on best practices for
query use, see [Best Practices for Queries](bestqueries.md "bestqueries.md"). Queries
can be processed alone, or in combination with any other `FeatureType`,
such as Tables or Forms.

Example Query: What is the customer’s SSN?

Example Answer: 111-xx-333

For analyzed items, Amazon Textract returns the following in multiple [Block](API_Block.md "API_Block.md") objects:

- The lines and words of detected text
- The content of detected items
- The relationship between detected items
- The page that the item was detected on
- The location of the item on the document page

###### Custom Queries

With Amazon Textract document analysis, you can customize the model output through
adapters trained on your own documents. Adapters are components that plug in to the
Amazon Textract pre-trained deep learning model, customizing its output for your business
specific documents. You create an adapter for your specific use case by
annotating/labeling your sample documents and training the adapter on the annotated
samples.

After you create an adapter, Amazon Textract provides you with an AdapterId. You can have
multiple adapter versions within a single adapter. You can provide the AdapterId, along
with an AdapterVersion, to an operation to specify that you want to use the adapter that
you created. For example, you provide the two parameters to the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") API for
synchronous document analysis, or the [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md") operation for asynchronous analysis.
Providing the AdapterId as part of the request will automatically integrate the adapter
into the analysis process and use it to enhance predictions for your documents. This
way, you can leverage the capabilities of AnalyzeDocument while customizing the model to
fit your own use case.

For more information on creating and using adapters, see [Customizing your Queries Responses](textract-using-adapters.md "textract-using-adapters.md"). For a
tutorial on how to create, train, and use adapters with the AWS Management Console, see [Custom Queries tutorial](textract-adapters-tutorial.md "textract-adapters-tutorial.md").

###### Layout in Document Analysis

Amazon Textract can be used to detect the layout of a document by finding the locations of different elements and their associated lines of text.
These elements are paragraphs, lists, headers, footers, page numbers, figures, tables, titles, and section headers.
When analyzing the layout of a document, Amazon Textract returns a bounding box location of the layout elements as well as
the text in those elements. This information is returned in the implied reading order of the document, listing elements
from top to bottom, left to right.

You can use synchronous or asynchronous operations to analyze text in a document. To
analyze text synchronously, use the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") operation, and pass a document as input.
`AnalyzeDocument` returns the entire set of results. For more
information, see [Analyzing Document Text with Amazon Textract](analyzing-document-text.md "analyzing-document-text.md").

To detect text asynchronously, use [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md") to start processing. To get the results,
call [GetDocumentAnalysis](API_GetDocumentAnalysis.md "API_GetDocumentAnalysis.md").
The results are returned in one or more responses from `GetDocumentAnalysis`.
For more information and an example, see [Detecting or Analyzing Text in a Multipage
Document](async-analyzing-with-sqs.md "async-analyzing-with-sqs.md").

To specify which type of analysis to perform, you can use the
`FeatureTypes` list input parameter. Add TABLES to the list to return
information about the tables that are detected in the input document—for example, table
cells, cell text, and selection elements in cells. Add FORMS to return word
relationships, such as key-value pairs and selection elements. Add QUERIES to specify
information you want Amazon Textract to look for in the document and get a response back
in the form of a question-answer pair. Add LAYOUT to determine the layout of the document.
To perform all types of analysis, add TABLES,
FORMS, QUERIES, and LAYOUT to `FeatureTypes`.

All lines and words that are detected in the document are included in the response
(including text not related to the value of `FeatureTypes`).
