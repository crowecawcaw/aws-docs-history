# GetDocumentContent Output Schema

When you use the [GetDocumentContent](../api-reference/API_GetDocumentContent.md "../api-reference/API_GetDocumentContent.md") API with `outputFormat`
set to `EXTRACTED`, the response returns extracted text content in JSON
format. The output schema is presented in JSON format:

```
{
   // always V1 for now
   schemaVersionId: string;

   // always JSON for now
   outputFormat: string;

   // content for plain-text documents
   plainTextDocumentContent: string;

   // content for non-plaintext documents such as PDF, DOCX, PPTX, Audio, Video
   nonPlainTextDocumentContent: List<ExtractedDocumentBodyElement>;
}
```

The schema for non-plaintext documents includes the
`ExtractedDocumentBodyElement` which includes:

```
{
   text: string;

  // Allowed values: TEXT, ARTICLE, SECTION, DIV, IMAGE_DESCRIPTION, CODE,
  // TABLE, LIST, URL, HEADER, FOOTER, FORM, MENU, AUDIO, VIDEO
   elementType: string;

   horizontalHeaderIndex: integer;
   verticalHeaderIndex: integer;
   htmlDocumentTitle: string;
   sectionTitle: string;
   sectionBody: string;
   tableCaption: string;
   tableFooter: string;
   tableRowHeaders: List<List<string>>;
   tableColumnHeaders: List<List<string>>;
   tableRows: List<List<string>>;
   tableRowsCount: integer;
   tableColumnsCount: integer;
   tableId: string;

   tokens: List<struct>;
   {
        value: string;
        startOffsets: integer;
        endOffsets: integer;
   }

   tableType: string;
   tableSummary: string;

   columnInfoList: List<struct>;
   {
        columnName: string;
        columnSummary: string;
        columnType: string;
        columnRepresentativeValues: List<string>
   }

   // Audio/Video specific fields below
   overallSummary: string;

   audioSummaryList: List<struct>;
   {
        summaryText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   videoSummaryList: List<struct>;
   {
        summaryText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   audioTranscriptList: List<struct>;
   {
        transcriptText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   videoTranscriptList: List<struct>;
   {
        transcriptText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }
}
```

## Example Output

### Plaintext Document Example

For plaintext documents, the extracted content is returned in the
`plainTextDocumentContent` field:

```
{
  "schemaVersionId": "V1",
  "outputFormat": "JSON",
  "plainTextDocumentContent": "This is the extracted text content from a plain text document."
}
```
