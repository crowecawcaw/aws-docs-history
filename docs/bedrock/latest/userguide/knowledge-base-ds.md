# Prerequisites for your Amazon Bedrock knowledge base data

A data source contains files or content with information that can be retrieved when
your knowledge base is queried. You must store your documents or content in at least one
of the [supported data
sources](data-source-connectors.md "data-source-connectors.md").

## Supported document formats and limits for knowledge base data

When you connect to a [supported data
source](data-source-connectors.md "data-source-connectors.md"), the content is ingested into your knowledge base.

If you use Amazon S3 to store your files or your data source includes attached files,
then you first must check that each source document file adheres to the
following:

- The source files are of the following supported formats:

| Format                                    | Extension  |
| ----------------------------------------- | ---------- |
| Plain text (UTF-8 encoded)                | .txt       |
| Markdown (UTF-8 encoded)                  | .md        |
| HyperText Markup Language (UTF-8 encoded) | .html      |
| Microsoft Word document                   | .doc/.docx |
| Comma-separated values                    | .csv       |
| Microsoft Excel spreadsheet               | .xls/.xlsx |
| Portable Document Format                  | .pdf       |

- Each file size doesn't exceed the quota of 50 MB.

###### Note

The maximum chunk size quota (measured in KB) refers to the size of individual text chunks after your documents are split by the chunking strategy — not the maximum size of the source document itself. Documents larger than the chunk size are automatically split into multiple chunks. For approximately 1 KB of plain text, expect roughly 1,000 characters or 200–250 English words.

If you use an Amazon S3 or custom data source, you can use multimodal data, including
JPEG (.jpeg) or PNG (.png) images or files that contain tables, charts,
diagrams, or other images.

###### Note

The maximum size of .JPEG and .PNG files is 3.75 MB.
