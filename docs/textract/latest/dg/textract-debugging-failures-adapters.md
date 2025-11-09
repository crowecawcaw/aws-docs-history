# Debugging training

failures

If you are notified on the adapter details page that training has failed, refer to the
status message to understand the error and correct it. There are two types of errors:
creation errors and file errors. Some status messages are returned in the console, while
others are displayed in a validation file.

The validation file that is created alongside a training job contains information on
the types of errors encountered when training. If the error message states that the
error is a validation error ("Status message = Manifest file contains invalid records.
Consult validation error file at OutputConfig path for more details."), refer to the
validation file located in the S3 output bucket you chose during adapter training. The
generated validation file is named `validation_errors.jsonl`. Each line in
the file corresponds to a line in the manifest file, with errors yielded for each line
in the manifest file that produces an error.

The following is a list of all creation errors and possible causes:

|                |                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------- |
| Error name     | Error description                                                                                               |
| CREATION_ERROR | Manifest file contains invalid records. Consult<br>validation error file at OutputConfig path for more details. |
| CREATION_ERROR | No manifest file found. Ensure manifest file is<br>provided.                                                    |
| CREATION_ERROR | Unable to access manifest file in specified S3<br>bucket.                                                       |
| CREATION_ERROR | Manifest file located in an unsupported cross-Region<br>S3 bucket.                                              |
| CREATION_ERROR | Contents of manifest file are empty.                                                                            |
| CREATION_ERROR | The manifest file size exceeds the maximum supported<br>size.                                                   |
| CREATION_ERROR | The manifest file has too many training<br>documents.                                                           |
| CREATION_ERROR | The manifest file has too many testing<br>documents.                                                            |
| CREATION_ERROR | The manifest file has too few training<br>documents.                                                            |
| CREATION_ERROR | The manifest file has too few testing<br>documents.                                                             |
| CREATION_ERROR | The manifest file has too few training, and testing<br>documents.                                               |
| CREATION_ERROR | The manifest file has too many training, and testing<br>documents.                                              |
| CREATION_ERROR | The manifest file has invalid encoding.                                                                         |
| CREATION_ERROR | Manifest file contains more training records than<br>allowed limits.                                            |
| CREATION_ERROR | Manifest file contains more testing records than<br>allowed limits.                                             |
| CREATION_ERROR | Unable to access the specified KMS key.                                                                         |
| CREATION_ERROR | Unable to access the S3 output bucket.                                                                          |
| CREATION_ERROR | Amazon Textract does not support cross-Region Amazon S3<br>resources.                                           |

The following is a list of file-related errors:

|                                                    |                                                                                                                                                             |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------ |
| Error name                                         | Error description                                                                                                                                           |
| ERROR_PAGE_COUNT_EXCEEDS_MAXIMUM                   | Number of pages for the same document exceeds<br>maximum limit.(This happens when customer specified origin-ref and<br>page_number in source-ref metadata.) |
| ERROR_INVALID_FILE                                 | The {source-ref                                                                                                                                             | annotations-ref               | prelabeling-refs}<br>file(s) is invalid. Check S3 path and/or file properties. |
| ERROR_INVALID_JSON_LINE                            | The JSON line format is invalid                                                                                                                             |
| ERROR_MANIFEST_JSON_DECODE_ERROR                   | The record is not a valid JSON object.                                                                                                                      |
| ERROR_DUPLICATE_SOURCE_REF                         | A record with this source-ref already exists in the<br>manifest.                                                                                            |
| ERROR_IMAGE_TOO_LARGE                              | The image resolution is too large.                                                                                                                          |
| ERROR_INVALID_PAGE_COUNT                           | The file is invalid. Expected number of pages to be<br>1.                                                                                                   |
| ERROR_INVALID_IMAGE                                | Unsupported source reference file format.                                                                                                                   |
| ERROR_INVALID_PDF                                  | Unsupported PDF file.                                                                                                                                       |
| ERROR_INVALID_PDF_PAGE_TOO_LARGE                   | Unsupported PDF file. PDF page exceeds max<br>dimensions.                                                                                                   |
| ERROR_INVALID_TIFF                                 | Unsupported TIFF file.                                                                                                                                      |
| ERROR_INVALID_TIFF_COMPRESSION                     | Unsupported TIFF compression type.                                                                                                                          |
| ERROR_INVALID_ANNOTATIONS                          | Invalid annotation or prelabeling file.                                                                                                                     |
| ERROR_INVALID_ANNOTATIONS_FILE_FORMAT              | Invalid annotations file format.                                                                                                                            |
| ERROR_MISSING_ANNOTATION_BLOCKS                    | Missing {PAGE                                                                                                                                               | QUERY                         | QUERY_RESULT} block(s).                                                        |
| ERROR_INVALID_BLOCK                                | Invalid {QUERY                                                                                                                                              | QUERY_RESULT} block(s) found. |
| ERROR_FILE_SIZE_LIMIT_EXCEEDED                     | The size of the {ref_file_type} file(s) exceeds the<br>limit: {size_limit} MB.                                                                              |
| ERROR_INVALID_PERMISSIONS_DATASET_S3_BUCKET        | Unable to access the {ref_file_type} file(s).                                                                                                               |
| ERROR_FILE_NOT_FOUND                               | The {ref_file_type} file(s) is not found.                                                                                                                   |
| ERROR_FILE_NOT_FOUND_IN_REGION                     | Amazon Textract does not support cross-Region Amazon S3<br>resources.                                                                                       |
| ERROR_QUERY_RESULT_TEXT_LENGTH_LIMIT_EXCEEDED      | QUERY_RESULT text length is greater than the maximum<br>length.                                                                                             |
| ERROR_QUERY_PER_PAGE_LIMIT_EXCEEDED                | Number of QUERY blocks is greater than the maximum<br>allowed.                                                                                              |
| ERROR_INVALID_DATA_FORMAT                          | "Invalid data format in {filename}."                                                                                                                        |
| ERROR_BLOCK_LIMIT_EXCEEDED                         | "Number of {block_type} blocks is greater than the<br>maximum allowed."                                                                                     |
| ERROR_DUPLICATE_ORIGIN_REF_PAGE_NUMBER_COMBINATION | "A record with this origin-ref and page-number<br>already exists in the manifest."                                                                          |
| ERROR_INVALID_BLOCK_RELATIONSHIP                   | "Invalid block relationship(s) found."                                                                                                                      |
| ERROR_DUPLICATED_BLOCK_ID                          | "Blocks Id should be unique."                                                                                                                               |

To see API error descriptions, see the _Amazon Textract API Reference_
for the appropriate operation. If an error occurs when you try to create a new adapter
with the [CreateAdapterVersion](API_CreateAdapterVersion.md "API_CreateAdapterVersion.md") operation, see the API Reference page. If
an error occurs when using the Amazon Textract console, read the error pop-up for information
on why the operation failed.
