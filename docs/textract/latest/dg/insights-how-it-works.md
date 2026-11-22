

# How Amazon Textract Insights works

Amazon Textract Insights processes each document according to two configurations: the extraction configuration, which controls extraction, and the optional custom configuration, which controls custom extraction through blueprints. You store both in a project and reference the project when you start a job. If you're new to the service, start with extraction, then add blueprints when you need specific fields.

## Extraction configuration
<a name="insights-how-it-works-extraction-configuration"></a>

The extraction configuration defines how Amazon Textract Insights extracts the general content of a document: its text, layout elements, tables, and reading order. Every project has one, and every job that uses a project produces extraction results.

You control extraction with these settings:
+ **Granularity** (`Granularity.Types`) sets how finely the text is divided in the result:
  + `DOCUMENT` returns the text of the whole document.
  + `PAGE` returns the text of each page.
  + `ELEMENT` returns logical layout elements (titles, paragraphs, headers, footers, tables, figures) in reading order.
  + `LINE` and `WORD` return individual lines and words, each with a confidence score and location.

  You can request any combination; each type adds a section to the result.
+ **Bounding boxes** (`BoundingBox.State`) adds the location of each element, line, or word on the page.
+ **Text format** (`OutputFormat.TextFormat.Types`) chooses the representations: `PLAIN_TEXT`, `MARKDOWN`, `HTML`, and `CSV` (for tables only).
+ **Additional files** (`OutputFormat.AdditionalFileFormat.State`) also writes standalone `result.md`, `result.html`, `result.txt`, and per-table CSV files next to the JSON result.

The generative configuration (`GenerativeConfiguration`) adds AI-generated content to extraction: a document summary (`Summarization`) and a caption for each detected figure (`FigureCaption`).

For the result structure, see [Extraction results](insights-extraction-results.md). For format choices, see [Output formats for LLM and RAG workflows](insights-output-formats.md).

## Custom configuration (custom extraction)
<a name="insights-how-it-works-custom-configuration"></a>

The custom configuration defines exactly which fields to extract, using blueprints. A blueprint is a schema that lists the fields you need from one type of document, such as a W-2 or an invoice. Each field has a name, a data type, and a natural-language description that tells the model what to find and how to format it. You can use public blueprints that AWS provides or create your own.

The custom configuration (`CustomConfiguration`) holds:
+ **Blueprints** – The candidate blueprints. When there is more than one, Amazon Textract Insights matches each document to the best-fitting blueprint.
+ **Fallback blueprints** – A blueprint to use when a document matches none of the candidates.

Custom extraction results contain the extracted value of each field, the matched blueprint, and, for each field, a confidence score and its location in the document. See [Custom extraction with blueprints](insights-custom-extraction.md).

## Projects
<a name="insights-how-it-works-projects"></a>

A project is the resource that stores your configuration. It always contains an extraction configuration and can also contain:
+ A generative configuration (summaries and figure captions)
+ A custom configuration (blueprints and a fallback blueprint)
+ A splitter configuration (`SplitterConfiguration`) that splits multi-document files; it applies to custom extraction, so it takes effect only when the project has blueprints
+ A sensitive data configuration (`SensitiveDataConfiguration`) that detects and optionally redacts PII
+ An encryption configuration (`EncryptionConfiguration`) with your own AWS KMS key

You pass the project ARN to `StartDocumentInsights`, and the job applies everything configured on the project. To change how future jobs behave, update the project; you don't need to change your job submission code. See [Working with projects](insights-working-with-projects.md).

You can also start a job without a project by passing blueprints inline. Use this approach to test blueprints quickly, without creating a project first. Inline jobs perform custom extraction only and use the default settings; a generative, splitter, or sensitive data configuration, as well as a fallback blueprint, requires a project. You can still pass an encryption configuration with an inline job. See [Running jobs with inline blueprints](insights-inline-blueprints.md). A job must specify either a project or inline blueprints.

## What happens during a job
<a name="insights-how-it-works-job-lifecycle"></a>

A job proceeds through the following stages:

1. **Start.** You call `StartDocumentInsights` with the input S3 URI, an output S3 prefix, and a project ARN or inline blueprints. The call returns a job ARN, and the job runs asynchronously.

1. **Extraction.** OCR, text, layout, and reading order are extracted according to the extraction configuration, along with any generated summary and figure captions.

1. **Split (optional).** If the project enables splitting and has blueprints, Amazon Textract Insights divides the file into logical documents. Each document is processed independently.

1. **Match and run custom extraction.** If the project has blueprints, each document is matched to a blueprint, and that blueprint's fields are extracted with confidence scores.

1. **Detect and redact sensitive data (optional).** The output is scanned for the configured PII types. In redaction mode, a separate redacted copy of the results is written.

1. **Read the results.** Poll `GetDocumentInsights` until the status is `SUCCEEDED` or `FAILED`. On success, `OutputConfiguration.S3Uri` points to `job_metadata.json`, which lists the location of every result. On failure, the response includes `ErrorType` and `ErrorMessage`.

Extraction results are written under `extraction/<n>/` and custom extraction results under `custom/<n>/`, where `<n>` is the document index. Your input and output buckets must be in the same AWS Region as the request. See [Output location and file structure](insights-output-location.md).

## Next steps
<a name="insights-how-it-works-next-steps"></a>

To continue, see the following topics:
+ Create and manage projects in [Working with projects](insights-working-with-projects.md).
+ Run a complete job in [Tutorial: Process your first document](insights-tutorial.md).