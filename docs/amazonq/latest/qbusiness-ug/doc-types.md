

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Supported document formats in Amazon Q Business
<a name="doc-types"></a>

When you add documents to an Amazon Q Business application environment ([directly](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-docs.html) or through [data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html)) using the console or the API, Amazon Q Business extracts document content and internally parses these to optimize chat responses. During this ingestion, there are file size limits depending on the file type. Video files have a limit of up to 10 GB/10,240 MB. Audio files have a 2 GB/2,048 MB limit. PDF/Word/Powerpoint documents have a 500 MB limit. Excel and other supported file formats have a 50 MB limit. There are also limits to the amount of text extracted from these documents. CSV and Excel have a extracted text limit of 10MB, all other document formats have a limit of 30MB of extracted text.

When you upload documents directly into chat using the [Upload files and chat](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-chat-files.html) feature, the size of each file you upload must be 10 MB or less, and 3.75 MB or less for images. The total parsed content for all files combined has to be under 665,000 characters.

For images, chat now supports direct uploads of JPEG, JPG, and PNG files. These images can be used for summarizing information and answering questions.

Additionally, if you’re uploading Comma Separated Values (CSV) or Microsoft Excel (XLS and XLSX) documents directly into chat, Amazon Q Business performs best for tables with up to 4 columns and 10 rows. Files indexed by an Amazon Q Business data source connector or uploaded directly have no such restrictions.

When you directly add files to Amazon Q Business using the [Using direct document upload](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-docs.html) or the [Upload files and chat](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-chat-files.html) feature, it considers each file you add a document. When you connect Amazon Q Business to a data source, what Amazon Q Business considers—and crawls—as a document varies by connector.

Along with specific formats like PDF, Word, for example, each enterprise data source also has different entities that it considers documents. To learn about supported entity types for each data source, see [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html).

For some file types (indicated in the table below), Amazon Q Business can extract semantic information and insights from various types of images embedded in the documents. You can enable content extraction when you add or update a data connector, or when you import a file directly. For more information see [Extracting semantic meaning from embedded visual content with Amazon Q Business](extracting-meaning-from-images.md).

**Topics**
+ [Supported document types](#doc-types-supported)

## Supported document types
<a name="doc-types-supported"></a>

The following table shows the document formats that Amazon Q Business supports.

**Note**  
 Provide a description of the file as metadata to improve retrieval accuracy. For more information, see [Configuring metadata controls in Amazon Q Business.](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/mapping-doc-attributes.html) 


| Document format | How document is treated | 
| --- | --- | 
| Portable Document Format (PDF) | If you're using a data source connector, or directly uploading documents into your application, Amazon Q can use optical character recognition (OCR) to convert images of typed, handwritten, or printed text into machine-readable text. If enabled, Amazon Q Business can extract semantic information and insights from images and other visuals. <br /> The maximum number of pages per PDF for optical character recognition (OCR) or insight extraction from embedded visual elements is 3000 pages. If your PDF is more than 3000 pages, only plaintext is extracted.<br />If you're directly uploading documents into chat, PDFs are converted to HTML, and only plaintext is extracted. | 
| HyperText Markup Language (HTML) | HTML tags are filtered out to extract plaintext. Content must be between the main HTML start and closing tags (<HTML>content</HTML>). | 
| Extensible Markup Language (XML) | XML tags are filtered out and plaintext is extracted. | 
| Extensible Stylesheet Language Transformations (XSLT) | Tags are filtered out to extract plaintext. | 
| Markdown (MD) | Content is extracted as plaintext with Markdown syntax retained. | 
| Comma Separated Values (CSV) | Content is extracted as plaintext from each cell, with a single file treated as a single document result. You can improve answer accuracy on CSVs by providing a [ metadata file](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/mapping-doc-attributes.html). Example: <pre>"Attributes":{<br />    "description": {{ "A description of your CSV table, a short paragraph providing details about what the use case is and insights you can derive from it."}},<br />    "_document_title": "document title",<br />    "_file_type": "CSV"<br />}<br /></pre> | 
| Microsoft Excel (XLS and XLSX) | Content is extracted as plaintext from each cell, with a single file treated as a single document result.  | 
| JavaScript Object Notation (JSON) | Content is extracted as plaintext with JSON syntax retained. | 
| Rich Text Format (RTF) | RTF syntax is filtered out to extract plaintext content. | 
| Microsoft PowerPoint (PPT, PPTX) | By default, only plaintext content is extracted from PowerPoint slides for ingestion. If enabled, Amazon Q Business can extract semantic information and insights from images and other visuals. Otherwise, images and other content aren't extracted. | 
| Microsoft Word (DOCX) | By default, only plaintext content is extracted from Word pages for ingestion. If enabled, Amazon Q Business can extract semantic information and insights from images and other visuals. Otherwise, images and other content aren't extracted. | 
| Plain text (TXT) | All text in the text document is extracted. | 
| Google Slides | By default, only plaintext content is extracted from Google Slides pages for ingestion. If enabled, Amazon Q Business can extract semantic information and insights from images and other visuals. Otherwise, images and other content aren't extracted. | 
| Google Docs  | By default, only plaintext content is extracted from Google Docs pages for ingestion. If enabled, Amazon Q Business can extract semantic information and insights from images and other visuals. Otherwise, images and other content aren't extracted. | 