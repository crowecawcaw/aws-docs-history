# Include metadata in a data source to improve knowledge base query

When ingesting CSV (comma separate values) files, you have the ability to have the knowledge base treat certain columns
as content fields versus metadata fields. Instead of potentially having hundreds or thousands of content/metadata
file pairs, you can now have a single CSV file and a corresponding metadata.json file, giving the
knowledge base hints as to how to treat each column inside of your CSV.

There are limits for document metadata fields/attributes per chunk. See [Quotas for knowledge bases](quotas.md "quotas.md")

Before ingesting a CSV file, make sure:

- Your CSV is in RFC4180 format and is UTF-8 encoded.
- The first row of your CSV includes header information.
- Metadata fields provided in your metadata.json are present as columns in your CSV.
- You provide a fileName.csv.metadata.json file with the following format:

```
{
    "metadataAttributes": {
        "${attribute1}": "${value1}",
        "${attribute2}": "${value2}",
        ...
    },
    "documentStructureConfiguration": {
        "type": "RECORD_BASED_STRUCTURE_METADATA",
        "recordBasedStructureMetadata": {
            "contentFields": [
                {
                    "fieldName": "string"
                }
            ],
            "metadataFieldsSpecification": {
                "fieldsToInclude": [
                    {
                        "fieldName": "string"
                    }
                ],
                "fieldsToExclude": [
                    {
                        "fieldName": "string"
                    }
                ]
            }
        }
    }
}
```

The CSV file is parsed one row at a time and the chunking strategy and vector embedding
is applied to the content field. Amazon Bedrock knowledge bases currently supports one content field.
The content field is split into chunks, and the metadata fields (columns) that are
associated with each chunk are treated as string values.

For example, say there's a CSV with a column 'Description' and a column 'Creation_Date'.
The description field is the content field and the creation date is an associated metadata
field. The description text is split into chunks and converted into vector embeddings for
each row in the CSV. The creation date value is treated as string representation of the
date and is associated with each chunk for the description.

If no inclusion/exclusion fields are provided, all columns are treated as metadata columns, except the content column.
If only inclusion fields are provided, only the provided columns are treated as metadata.
If only exclusion fields are provided, all columns, except the exclusion columns are treated as metadata.
If you provide the same `fieldName` in both `fieldsToInclude` and `fieldsToExclude`,
Amazon Bedrock throws a validation exception. If there’s a conflict between inclusion and exclusion, it
will result in a failure.

Blank rows found inside a CSV are ignored or skipped.
