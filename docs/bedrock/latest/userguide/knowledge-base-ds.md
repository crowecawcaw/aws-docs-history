# Prerequisites for your Amazon Bedrock knowledge base

data

A data source contains files or content with information that can be retrieved when
your knowledge base is queried. You must store your documents or content in at least one
of the [supported data
sources](data-source-connectors.md "data-source-connectors.md").

## Supported document formats and

limits for knowledge base data

When you connect to a [supported data
source](data-source-connectors.md "data-source-connectors.md"), the content is ingested into your knowledge base.

If you use Amazon S3 to store your files or your data source includes attached files,
then you first must check that each source document file adheres to the
following:

- The source files are of the following supported formats:

| Format                      | Extension  |
| --------------------------- | ---------- |
| Plain text (ASCII only)     | .txt       |
| Markdown                    | .md        |
| HyperText Markup Language   | .html      |
| Microsoft Word document     | .doc/.docx |
| Comma-separated values      | .csv       |
| Microsoft Excel spreadsheet | .xls/.xlsx |
| Portable Document Format    | .pdf       |

- Each file size doesn't exceed the quota of 50 MB.

If you use an Amazon S3 or custom data source, you can use multimodal data, including
JPEG (.jpeg) or PNG (.png) images or files that contain tables, charts,
diagrams, or other images.

###### Note

The maximum size of .JPEG and .PNG files is 3.75 MB.
