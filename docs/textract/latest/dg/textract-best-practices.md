

# Best practices

Amazon Textract Core uses machine learning to read documents as a person would. It extracts text, tables, and forms from documents. Use the following best practices to get the best results from your documents.

## Provide an optimal input document
<a name="optimal-document"></a>

A suitable input for an Amazon Textract Core operation is a single- or multipage-document. Some examples are a legal document, a form, an ID, or a letter. A form is a document with questions or prompts for a user to provide answers. Some examples are a patient registration form, a tax form, or an insurance claim form. 

A document can be in JPEG, PNG, PDF, or TIFF format. With PDF and TIFF format files, you can process multipage documents. For information about how Amazon Textract Core represents documents as `Block` objects, see [Text detection and document analysis response objects](how-it-works-document-layout.md).

The following is an acceptable input document example:

![Image of a white piece of paper with a header Employment Application. The next line says Application Information, the next Full Name: Jane Doe, the next Phone Number: 555-0100, the next Home Address: 123 Any Street, AnyTown USA, the next Mailing Address: same as above. Underneath is a table titled Previous Employment History. It has five columns and four rows. The column titles are Start Date, End Date, Employer Name, Position Held, and Reason for leaving. The next row lists 1/15/2009, 6/30/2011, Any Company, Assistant baker, and relocated. The next 7/1/2011, 8/10/2013, Example Corp. Baker, better opp. The next 8/15/2013, Present, AnyCompany, head baker, and N/A, current.](https://docs.aws.amazon.com/textract/latest/dg/images/Handwriting%20Sample%203.png)


For information about document limits, see [Quotas in Amazon Textract Core](limits.md).

For Amazon Textract Core synchronous operations, you can use input documents that are stored in an Amazon S3 bucket, or you can pass Base64-encoded image bytes. For more information, see [Calling Amazon Textract Core synchronous operations](sync-calling.md). For asynchronous operations, you need to supply input documents in an Amazon S3 bucket. For more information, see [Calling Amazon Textract Core asynchronous operations](api-async.md). 

The following is a list of a few ways that you can optimize your input documents for better results:
+ Ensure that your document text is in a language that Amazon Textract Core supports. For the languages that Amazon Textract Core supports, see [Supported languages](supported-languages.md).
+ Provide a high-quality image, ideally at least 150 DPI.
+ If your document is already in one of the file formats that Amazon Textract Core supports (PDF, TIFF, JPEG, and PNG), don't convert or downsample the document before uploading it to Amazon Textract Core.
+ Ensure that the pages in your document are in their upright reading orientation.

For the best results when extracting text from tables in documents, ensure that:
+ Tables in your document are visually separated from surrounding elements on the page. For example, the table isn't overlaid onto an image or complex pattern.
+ Text within the table is upright. For example, the text isn't rotated relative to other text on the page.

When extracting text from tables, you might see inconsistent results when: 
+ Merged table cells span multiple columns.
+ Tables with cells, rows, or columns are different from other parts of the same table.

We recommend using [text detection](how-it-works-detecting.md) as a workaround.

## Use confidence scores
<a name="confidence-score"></a>

You should take into account the confidence scores returned by Amazon Textract Core API operations and the sensitivity of their use case. A confidence score is a number between 0 and 100 that indicates the probability that a given prediction is correct. It helps you make informed decisions about how you use the results. 

In applications that are sensitive to detection errors (false positives), enforce a minimum confidence score threshold. The application should discard results below that threshold or flag situations as requiring a higher level of human scrutiny.

The optimal threshold depends on the application. For archival purposes, such as documenting handwritten notes, it might be as low as 50%. Business processes involving financial decisions might require thresholds of 90% or higher.