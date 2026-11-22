

# Analyzing documents

Amazon Textract Core analyzes documents and forms for relationships among detected text. Amazon Textract Core analysis operations return 5 categories of document extraction — text, forms, tables, query responses, and signatures. The analysis of invoices and receipts is handled through a different process. For more information, see [Analyzing invoices and receipts](invoices-receipts.md).

**Text extraction**  
The raw text extracted from a document. For more information, see [Lines and words of text](how-it-works-lines-words.md).

**Form extraction**  
Form data is linked to text items extracted from a document. Amazon Textract Core represents form data as key-value pairs. 

In the following example, one of the lines of text detected by Amazon Textract Core is *Name: Jane Doe*. Amazon Textract Core also identifies a key (*Name:*) and a value (*Jane Doe*). For more information, see [Form data (Key-value pairs)](how-it-works-kvp.md).

*Name: Jane Doe*

*Address: 123 Any Street, Anytown, USA*

*Birth date: 12-26-1980*

Key-value pairs are also used to represent check boxes or option buttons (radio buttons) that are extracted from forms.

*Male:* ☑

For more information, see [Selection elements](how-it-works-selectables.md).

**Table extraction**  
Amazon Textract Core can extract tables, table cells, the items within table cells, table titles and footers, and the type of table. Amazon Textract Core can also be programmed to return the results in a JSON, CSV, or TXT file.


| **Name** | **Address** | 
| --- | --- | 
| Ana Carolina | 123 Any Town | 

For more information, see [Tables](how-it-works-tables.md). Selection elements can also be extracted from tables. For more information, see [Selection elements](how-it-works-selectables.md).

**Signatures in document analysis**  
Amazon Textract Core can detect the locations of signatures in text documents. These are returned as geometry objects with bounding boxes that provide the location of a signature on the page, alongside the confidence that a signature is in that location. If the signature feature is used by itself, Amazon Textract Core will return both signatures and standard text detection results. Signature detection can be used in conjunction with other feature types such as forms, tables, and queries. When using it with forms and tables, signatures can be detected as part of a key-value pair or within a table cell respectively.

**Queries in document analysis**  
When processing a document with Amazon Textract Core, you may add queries to your analysis to specify what information you need. This involves passing a question, such as "What is the customer's social security number?", to Amazon Textract Core. Amazon Textract Core will then find the information in the document for that question and return it in a response structure separate from the rest of the document's information. For more information about this response structure, see [Query response structures](queryresponse.md). For more information on best practices for query use, see [Best practices for Queries](bestqueries.md). Queries can be processed alone, or in combination with any other `FeatureType`, such as Tables or Forms.

 Example Query: What is the customer's SSN?

 Example Answer: 111-xx-333

For analyzed items, Amazon Textract Core returns the following in multiple [Block](https://docs.aws.amazon.com/textract/latest/APIReference/API_Block.html) objects:
+ The lines and words of detected text
+ The content of detected items
+ The relationship between detected items
+ The page that the item was detected on
+ The location of the item on the document page

**Custom Queries**  
With Amazon Textract Core document analysis, you can customize the model output through adapters trained on your own documents. Adapters are components that plug in to the Amazon Textract Core pre-trained deep learning model, customizing its output for your business specific documents. You create an adapter for your specific use case by annotating/labeling your sample documents and training the adapter on the annotated samples.

After you create an adapter, Amazon Textract Core provides you with an AdapterId. You can have multiple adapter versions within a single adapter. You can provide the AdapterId, along with an AdapterVersion, to an operation to specify that you want to use the adapter that you created. For example, you provide the two parameters to the [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/APIReference/API_AnalyzeDocument.html) API for synchronous document analysis, or the [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentAnalysis.html) operation for asynchronous analysis. Providing the AdapterId as part of the request will automatically integrate the adapter into the analysis process and use it to enhance predictions for your documents. This way, you can leverage the capabilities of AnalyzeDocument while customizing the model to fit your own use case. 

For more information on creating and using adapters, see [Customizing your Queries responses](textract-using-adapters.md). For a tutorial on how to create, train, and use adapters with the AWS Management Console, see [Custom Queries tutorial](textract-adapters-tutorial.md).

**Layout in document analysis**  
Amazon Textract Core can be used to detect the layout of a document by finding the locations of different elements and their associated lines of text. These elements are paragraphs, lists, headers, footers, page numbers, figures, tables, titles, and section headers. When analyzing the layout of a document, Amazon Textract Core returns a bounding box location of the layout elements as well as the text in those elements. This information is returned in the implied reading order of the document, listing elements from top to bottom, then left to right.

You can use synchronous or asynchronous operations to analyze text in a document. To analyze text synchronously, use the [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/APIReference/API_AnalyzeDocument.html) operation, and pass a document as input. `AnalyzeDocument` returns the entire set of results. For more information, see [Analyzing document text with Amazon Textract Core](analyzing-document-text.md). 

To detect text asynchronously, use [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentAnalysis.html) to start processing. To get the results, call [GetDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetDocumentAnalysis.html). The results are returned in one or more responses from `GetDocumentAnalysis`. For more information and an example, see [Detecting or analyzing text in a multipage document](async-analyzing-with-sqs.md). 

To specify which type of analysis to perform, you can use the `FeatureTypes` list input parameter:
+ Add TABLES to the list to return information about the tables that are detected in the input document—for example, table cells, cell text, and selection elements in cells.
+ Add FORMS to return word relationships, such as key-value pairs and selection elements.
+ Add QUERIES to specify information you want Amazon Textract Core to look for in the document and get a response back in the form of a question-answer pair.
+ Add LAYOUT to determine the layout of the document.

To perform all types of analysis, add TABLES, FORMS, QUERIES, and LAYOUT to `FeatureTypes`.

All lines and words that are detected in the document are included in the response (including text not related to the value of `FeatureTypes`).