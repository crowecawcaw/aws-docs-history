

# Set quotas in Amazon Textract Core

The following is a list of set quotas in Amazon Textract Core, which cannot be changed. For information about limitations in default quotas you can change, see [Modifying default quotas in Amazon Textract Core](limits-quotas-explained.md).


| **Limit** | **Description** | 
| --- | --- | 
| Accepted File Formats | Operations support JPEG, PNG, PDF, and TIFF files. (JPEG 2000-encoded images within PDFs are supported). Amazon Textract Core does not support XFA-based PDFs. | 
| File Size and Page Count Limits | For synchronous operations, JPEG, PNG, PDF, and TIFF files have a limit of 10 MB in memory. PDF and TIFF files also have a limit of 1 page. For asynchronous operations, JPEG and PNG files have a limit of 10 MB in memory. PDF and TIFF files have a limit of 500 MB in memory and a limit of 3,000 pages. | 
| PDF-Specific Limits | The maximum height and width are 40 inches and 9000 points. PDFs cannot be password-protected. PDFs can contain JPEG 2000-formatted images. | 
| Document Rotation and Image Size | Amazon Textract Core supports all in-plane document rotations, for example 45-degree in-plane rotation.<br />Amazon Textract Core supports images with a resolution less than or equal to 10,000 pixels on all sides. | 
| Query-Specific Limits | Amazon Textract Core supports up to 15 queries per page for synchronous operations and up to 30 queries per page for asynchronous operations.  | 
| Text Alignment | Text can be aligned horizontally within the document. Horizontally arrayed text can be read regardless of the degree of rotation of a document. | 
| Languages | Amazon Textract Core supports more than 40 languages. Language support varies by API operation and feature. For more information, see [Supported languages](supported-languages.md). | 
| Character Size | The minimum height for text to be detected is 15 pixels. At 150 DPI, this would be the same as 8-point font. | 
| Character Type | Amazon Textract Core supports both handwritten and printed character recognition. Handwritten character recognition is only supported in English.  | 
| Characters | Amazon Textract Core detects the following characters:+  a-z <br />+  A-Z <br />+  0-9 <br />+  ä Ä ö Ö ü Ü ç Ç é É â Â ê Ê î Î ô Ô û Û à À è È ù Ù ë Ë ï Ï ü Ü á Á é É í Í ó Ó ú Ú ü Ü ñ Ñ ì Ì ò Ò ã Ã õ Õ <br />+  \! " \# $ % ' & ( ) \* \+ , - . / : ; = ? @ [ \\ ] ^ \_ ` { \| } \~ > < ° € £ ¥ ₹ ß ẞ ¿ ¡ € £ ¥ ₹ ø Ø œ Œ © ® ™ § ¹ ² ³ '  | 
|  AnalyzeID-Specific Limits  |  AnalyzeID only supports U.S. passports and U.S. driver's licenses.  | 
| Adapter-Specific Limits |  +   Accepted dataset configuration for adapter training – Training: 5-2500, Test: 5-1000.  <br />+   Training/testing file format and size – JPG, PNG, PDF, TIFF.  <br />+   Maximum size of training/testing file – 10 MB.  <br />+   Maximum size of annotation/pre-labeling file – 25 MB.  <br />+   Maximum length of pre-labeling file array – 15.  <br />+   Max query response length – 128 characters  <br />+   Max number of queries per page – 30    | 