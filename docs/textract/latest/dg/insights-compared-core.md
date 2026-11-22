

# Amazon Textract Insights compared with Amazon Textract Core APIs

The Amazon Textract Core APIs return raw building blocks or fixed fields. `DetectDocumentText` and `AnalyzeDocument` return words, lines, tables, and key-value pairs as linked blocks that you assemble yourself. Analyze Expense, Analyze ID, and Analyze Lending return normalized fields, but only for a predetermined list of document types and fields. You can't change the schema or how values are normalized.

Amazon Textract Insights does all of that in **one API call**. It returns each document as Markdown and HTML that you can pass straight to an LLM, and extracts the exact fields you define in your own schema. It also summarizes documents, captions figures, and redacts personal data. And it can split a file into separate documents and recognize each one, for any document type you create a blueprint for.

## At a glance
<a name="insights-compared-at-a-glance"></a>

The following table summarizes the differences between the two approaches.


|  | **Amazon Textract Core APIs** | **Amazon Textract Insights** | 
| --- | --- | --- | 
| Number of APIs | One per task (`DetectDocumentText`, `AnalyzeDocument`, `AnalyzeExpense`, `AnalyzeID`, `StartLendingAnalysis`) | One: `StartDocumentInsights`. | 
| Text ready for an LLM | You build it from the response | Included as Markdown, HTML, and plain text. | 
| Fields you get | A fixed set chosen by AWS for each supported document type, normalized in a fixed way | Any fields you define in your own schema, on any document type. | 
| Output format | Different for each API | The same for every job. | 
| Choosing the document type | You choose, by picking the API. Analyze Lending recognizes the type for you, but only from its fixed list of lending document types. | Recognized automatically from the blueprints in your project, including blueprints you create. | 
| Files with several documents | Processed as one document, except in Analyze Lending, which splits a file into its fixed lending document types | Split into separate documents of any type you have a blueprint for, each processed on its own. | 
| Summaries and figure captions | Not available | Available. | 
| Personal data (PII) | Not detected | Detected, and optionally redacted. | 
| Settings | Sent with every request | Saved once in a project and reused. | 
| Response time | Synchronous calls for single pages, plus asynchronous jobs | Asynchronous jobs only. | 

## Step 1: Combine the Core features into one call
<a name="insights-compared-step1"></a>

Many Core features have a direct equivalent in Amazon Textract Insights. Instead of calling several APIs, you turn on the matching settings in one project.


| **Core feature** | **Equivalent Amazon Textract Insights setting** | 
| --- | --- | 
| `DetectDocumentText` to read text | Extraction with `LINE` and `WORD` granularity, or plain text for each page or the whole document. | 
| `AnalyzeDocument` with `LAYOUT` and `TABLES` | Extraction with `ELEMENT` granularity. Titles, paragraphs, headers, footers, and tables come back as elements, already rendered as Markdown, HTML, and CSV. | 
| `AnalyzeDocument` with `QUERIES` | Custom extraction. Each question becomes a field in a blueprint. | 
| `AnalyzeExpense` | Custom extraction with the `public-invoice` or `public-receipt` blueprint. | 
| `AnalyzeID` | Custom extraction with the `public-us-driver-license` or `public-us-passport` blueprint. | 
| Analyze Lending | Splitting plus blueprint matching, with the document types and fields you define instead of a fixed lending list. | 

Take a brokerage's consolidated 1099 statement: one PDF that holds a 1099-INT, a 1099-DIV, and a 1099-B with pages of sale transactions. Analyze Lending recognizes some of these forms, but not the 1099-B, and it returns only its own fixed fields. So with the Core APIs you would have to build and maintain this pipeline:

1. Split the file into its separate forms.

1. Work out which form each one is.

1. Extract each form's fields, for example with `AnalyzeDocument` queries, and rebuild the 1099-B transaction table from its cell blocks.

1. Convert the different responses into one data model.

With Amazon Textract Insights, you describe that pipeline once in a project. The 1099-INT has a public blueprint. For the 1099-DIV and 1099-B, you create blueprints with exactly the fields you need, such as a list of transactions with proceeds and cost basis for each sale.

```
# Blueprints in this project:
#   public-form-1099-int  - public blueprint for Form 1099-INT
#   a1b2c3d4e5f6          - your custom blueprint for Form 1099-DIV
#   f6e5d4c3b2a1          - your custom blueprint for Form 1099-B
aws textract create-project \
  --region us-east-1 \
  --project-name "consolidated-1099" \
  --splitter-configuration '{"State": "ENABLED"}' \
  --custom-configuration '{
    "Blueprints": [
      {"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-form-1099-int"},
      {"BlueprintArn": "arn:aws:textract:us-east-1:111122223333:blueprint/a1b2c3d4e5f6"},
      {"BlueprintArn": "arn:aws:textract:us-east-1:111122223333:blueprint/f6e5d4c3b2a1"}
    ]
  }'\
  --extraction-configuration '{
    "BoundingBox": {"State": "ENABLED"},
    "Granularity": {"Types": ["PAGE", "ELEMENT"]},
    "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}
  }'
```

Then each file is a single call:

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/consolidated-1099.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

The service splits the file, recognizes each form, and applies the matching blueprint. Each form gets its own results folder in the same format. To handle another form later, for example a 1099-OID, you add a blueprint to the project. Your code doesn't change.

For the consolidated 1099, the results look like this in your output bucket:

```
results/<job-id>/
|-- job_metadata.json              # lists every result file below
`-- 0/
    |-- extraction/
    |   |-- 0/result.json          # 1099-INT: text, layout, tables
    |   |-- 1/result.json          # 1099-DIV
    |   `-- 2/result.json          # 1099-B
    `-- custom/
        |-- 0/result.json          # 1099-INT fields from public-form-1099-int
        |-- 1/result.json          # 1099-DIV fields from your custom 1099-DIV blueprint
        `-- 2/result.json          # 1099-B transactions from your custom 1099-B blueprint
```

Every document has the same two files, whatever its type: one extraction result and one custom extraction result. For the full layout, see [Output location and file structure](insights-output-location.md).

## Step 2: Go further than the Core APIs
<a name="insights-compared-step2"></a>

The same project can also do things that no Core API offers. Each one is a setting you add to the project.


| **Capability** | **What it gives you** | **Add this to the project** | 
| --- | --- | --- | 
| Your own fields | Extract exactly the fields you need from any document type, each with a confidence score and its location on the page | A custom blueprint in `--custom-configuration`. See [Custom extraction with blueprints](insights-custom-extraction.md). | 
| Fallback blueprint | A blueprint to use when a document matches none of the others | `FallbackBlueprints` in `--custom-configuration`. See [Blueprint matching and fallback blueprints](insights-blueprint-matching.md). | 
| LLM-ready text | Markdown, HTML, plain text, and CSV for each element, page, and the whole document, ready for a RAG pipeline | `OutputFormat` in `--extraction-configuration`. See [Output formats for LLM and RAG workflows](insights-output-formats.md). | 
| Summaries and figure captions | A summary of each document, and a written description of each chart or image | `--generative-configuration`. See [Document summarization and figure captioning](insights-summarization-captioning.md). | 
| PII redaction | Personal data found and masked, in a separate redacted copy of the results | `--sensitive-data-configuration`. See [Detecting and redacting sensitive data](insights-detecting-redacting.md). | 

For example, adding these two settings to the consolidated 1099 project also summarizes each form and masks names and Social Security numbers:

```
  --generative-configuration '{"Summarization": {"State": "ENABLED"}}' \
  --sensitive-data-configuration '{
    "DetectionMode": "DETECTION_AND_REDACTION",
    "PiiEntitiesConfiguration": {
      "PiiEntityTypes": ["NAME", "US_SOCIAL_SECURITY_NUMBER"],
      "RedactionMaskMode": "ENTITY_TYPE"
    }
  }'
```

## Example: one table, two APIs
<a name="insights-compared-example"></a>

Here we run the same five-page invoice through `AnalyzeDocument` and through Amazon Textract Insights. Both find the same text, about 1,600 words. The difference is how much work it takes to use the result.

`AnalyzeDocument` returns a table as a chain of linked blocks. To rebuild a small four-row table, you follow IDs from the table to 8 cells, then to 11 words:

```json
{ "BlockType": "TABLE", "Id": "ed27538d-...",
  "Relationships": [ { "Type": "CHILD", "Ids": [ "a9b31de7-...", "d1238ce6-...", "..." ] } ] }
{ "BlockType": "CELL", "Id": "a9b31de7-...", "RowIndex": 1, "ColumnIndex": 1,
  "Relationships": [ { "Type": "CHILD", "Ids": [ "660245ed-...", "7844ee2b-..." ] } ] }
{ "BlockType": "WORD", "Id": "660245ed-...", "Text": "Invoice", "Confidence": 100.0 }
```

Amazon Textract Insights returns the same table as one element, already rendered:

```json
{
  "type": "TABLE",
  "reading_order": 4,
  "representation": {
    "markdown": "|                |            |\n|----------------|------------|\n| Invoice Number | #000009    |\n| Issue Date     | 2018-04-11 |\n| Due Date       | 2018-04-11 |\n| PAID           | $685.35    |",
    "csv": ",0,1\n0,Invoice Number,#000009\n1,Issue Date,2018-04-11\n2,Due Date,2018-04-11\n3,PAID,$685.35"
  }
}
```

The same is true for fields. `AnalyzeExpense` on this invoice returns `TOTAL` three times with three different values, and leaves it to you to pick one. Custom extraction can instead return one value for each field you define, with its confidence score.

## When to use the Core APIs instead
<a name="insights-compared-when-core"></a>

Amazon Textract Insights trades some low-level detail for output you can use directly. Use the Core APIs when you need:
+ **A synchronous response.** Amazon Textract Insights runs only as an asynchronous job.
+ **Cell-level table detail.** Amazon Textract Insights gives each table's cell values by row and column (in CSV and HTML), but not each cell's own location or confidence score. If you highlight individual cells in a review screen, use `AnalyzeDocument`.
+ **Every key-value pair on a form.** `AnalyzeDocument` with `FORMS` returns all of them. Amazon Textract Insights returns only the fields you list in a blueprint.
+ **Only raw text.** If all you need is the words on the page, `DetectDocumentText` is simpler.

Also note that custom extraction without splitting has a maximum number of pages per document insights job. See [Limits and quotas](insights-quotas.md).

## Which should I use?
<a name="insights-compared-which"></a>

Use the following table to decide between the two approaches.


| **When to choose Amazon Textract Insights** | **When to choose the Core APIs** | 
| --- | --- | 
| Feed documents into an LLM or RAG pipeline | Need a synchronous response. | 
| Need specific fields, in your own schema, that no fixed API returns | Need each table cell's location or confidence score. | 
| Process files that contain several documents of types you define | Need every key-value pair on a form. | 
| Handle many document types and don't want to route them yourself | Only need the raw text. | 
| Need to redact personal data before it reaches other systems |  | 
| Would otherwise call more than one Core API |  | 

For the languages that Amazon Textract Core and Amazon Textract Insights support, see [Supported languages](supported-languages.md).

## Next steps
<a name="insights-compared-next-steps"></a>
+ To understand projects, blueprints, and jobs, see [How Amazon Textract Insights works](insights-how-it-works.md).
+ To set up access, see [Prerequisites and setup](insights-prerequisites.md).