

# Debugging training failures
<a name="textract-debugging-failures-adapters"></a>

If you are notified on the adapter details page that training has failed, refer to the status message to understand the error and correct it. There are two types of errors: creation errors and file errors. Some status messages are returned in the console, while others are displayed in a validation file. 

The validation file that is created alongside a training job contains information on the types of errors encountered when training. If the error message states that the error is a validation error ("Status message = Manifest file contains invalid records. Consult validation error file at OutputConfig path for more details."), refer to the validation file located in the S3 output bucket you chose during adapter training. The generated validation file is named `validation_errors.jsonl`. Each line in the file corresponds to a line in the manifest file, with errors yielded for each line in the manifest file that produces an error.

The following is a list of all creation errors and possible causes:


|  |  | 
| --- |--- |
| Error name | Error description | 
| CREATION\_ERROR | Manifest file contains invalid records. Consult validation error file at OutputConfig path for more details. | 
| CREATION\_ERROR | No manifest file found. Ensure manifest file is provided. | 
| CREATION\_ERROR | Unable to access manifest file in specified S3 bucket. | 
| CREATION\_ERROR | Manifest file located in an unsupported cross-Region S3 bucket. | 
| CREATION\_ERROR | Contents of manifest file are empty. | 
| CREATION\_ERROR | The manifest file size exceeds the maximum supported size. | 
| CREATION\_ERROR | The manifest file has too many training documents. | 
| CREATION\_ERROR | The manifest file has too many testing documents. | 
| CREATION\_ERROR | The manifest file has too few training documents. | 
| CREATION\_ERROR | The manifest file has too few testing documents. | 
| CREATION\_ERROR | The manifest file has too few training, and testing documents. | 
| CREATION\_ERROR | The manifest file has too many training, and testing documents. | 
| CREATION\_ERROR | The manifest file has invalid encoding. | 
| CREATION\_ERROR | Manifest file contains more training records than allowed limits. | 
| CREATION\_ERROR | Manifest file contains more testing records than allowed limits. | 
| CREATION\_ERROR | Unable to access the specified KMS key. | 
| CREATION\_ERROR | Unable to access the S3 output bucket. | 
| CREATION\_ERROR | Amazon Textract does not support cross-Region Amazon S3 resources. | 

The following is a list of file-related errors:


|  |  | 
| --- |--- |
| Error name | Error description | 
| ERROR\_PAGE\_COUNT\_EXCEEDS\_MAXIMUM | Number of pages for the same document exceeds maximum limit.(This happens when customer specified origin-ref and page\_number in source-ref metadata.) | 
| ERROR\_INVALID\_FILE | The {source-ref\|annotations-ref\|prelabeling-refs} file(s) is invalid. Check S3 path and/or file properties. | 
| ERROR\_INVALID\_JSON\_LINE | The JSON line format is invalid | 
| ERROR\_MANIFEST\_JSON\_DECODE\_ERROR | The record is not a valid JSON object. | 
| ERROR\_DUPLICATE\_SOURCE\_REF | A record with this source-ref already exists in the manifest. | 
| ERROR\_IMAGE\_TOO\_LARGE | The image resolution is too large. | 
| ERROR\_INVALID\_PAGE\_COUNT | The file is invalid. Expected number of pages to be 1. | 
| ERROR\_INVALID\_IMAGE | Unsupported source reference file format. | 
| ERROR\_INVALID\_PDF | Unsupported PDF file. | 
| ERROR\_INVALID\_PDF\_PAGE\_TOO\_LARGE | Unsupported PDF file. PDF page exceeds max dimensions. | 
| ERROR\_INVALID\_TIFF | Unsupported TIFF file. | 
| ERROR\_INVALID\_TIFF\_COMPRESSION | Unsupported TIFF compression type. | 
| ERROR\_INVALID\_ANNOTATIONS | Invalid annotation or prelabeling file. | 
| ERROR\_INVALID\_ANNOTATIONS\_FILE\_FORMAT | Invalid annotations file format. | 
| ERROR\_MISSING\_ANNOTATION\_BLOCKS | Missing {PAGE\|QUERY\|QUERY\_RESULT} block(s). | 
| ERROR\_INVALID\_BLOCK | Invalid {QUERY\|QUERY\_RESULT} block(s) found. | 
| ERROR\_FILE\_SIZE\_LIMIT\_EXCEEDED | The size of the {ref\_file\_type} file(s) exceeds the limit: {size\_limit} MB. | 
| ERROR\_INVALID\_PERMISSIONS\_DATASET\_S3\_BUCKET | Unable to access the {ref\_file\_type} file(s). | 
| ERROR\_FILE\_NOT\_FOUND | The {ref\_file\_type} file(s) is not found. | 
| ERROR\_FILE\_NOT\_FOUND\_IN\_REGION | Amazon Textract does not support cross-Region Amazon S3 resources. | 
| ERROR\_QUERY\_RESULT\_TEXT\_LENGTH\_LIMIT\_EXCEEDED | QUERY\_RESULT text length is greater than the maximum length. | 
| ERROR\_QUERY\_PER\_PAGE\_LIMIT\_EXCEEDED | Number of QUERY blocks is greater than the maximum allowed. | 
| ERROR\_INVALID\_DATA\_FORMAT | "Invalid data format in {filename}." | 
| ERROR\_BLOCK\_LIMIT\_EXCEEDED | "Number of {block\_type} blocks is greater than the maximum allowed." | 
| ERROR\_DUPLICATE\_ORIGIN\_REF\_PAGE\_NUMBER\_COMBINATION | "A record with this origin-ref and page-number already exists in the manifest." | 
| ERROR\_INVALID\_BLOCK\_RELATIONSHIP | "Invalid block relationship(s) found." | 
| ERROR\_DUPLICATED\_BLOCK\_ID | "Blocks Id should be unique." | 

To see API error descriptions, see the *Amazon Textract API Reference* for the appropriate operation. If an error occurs when you try to create a new adapter with the [CreateAdapterVersion](https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateAdapterVersion.html) operation, see the API Reference page. If an error occurs when using the Amazon Textract console, read the error pop-up for information on why the operation failed.