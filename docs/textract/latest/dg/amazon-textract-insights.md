

# Amazon Textract Insights

Amazon Textract Insights uses generative AI to turn unstructured documents into structured data. A single asynchronous API call can split a multi-document file, classify each document, extract structured data against a schema, generate LLM-ready output, and detect or redact sensitive data. It builds on Amazon Textract text and layout extraction, so you can automate intelligent document processing (IDP) workflows without building and orchestrating separate steps for splitting, classification, and extraction yourself. Amazon Textract Insights is currently available through the API only, with plans to expand to the Amazon Textract console in the future.

## Overview
<a name="insights-overview"></a>

You submit a document to one asynchronous operation, `StartDocumentInsights`. Amazon Textract Insights processes it according to a configuration you define, and writes the results to an Amazon S3 location that you choose. The configuration controls two kinds of extraction:
+ Extraction, configured through the `extraction configuration`: the document's text, layout elements, tables, and reading order, at the granularity and in the text formats you choose. It can also include a generated document summary and figure captions.
+ Custom extraction, configured through the `custom configuration`: exactly the fields you define in a blueprint, such as the employer ID on a W-2 or the line items on an invoice. Each field comes with a confidence score.

You store these configurations in a project and reference it when you start a job, so every document you process gets the same treatment. Built-in safeguards such as bounding boxes and per-field confidence scores help you check where each value came from and decide which results need human review.

## Example use cases
<a name="insights-example-use-cases"></a>
+ **Intelligent document processing** – Split, classify, and extract data from large volumes of mixed documents such as loan packets, claims files, and onboarding packages.
+ **Business data extraction** – Turn invoices, tax forms, bank statements, pay stubs, and identity documents into structured records that flow into downstream systems.
+ **Generative AI assistants and RAG** – Give retrieval-augmented generation (RAG) applications clean Markdown, HTML, or plain-text representations of your documents, with document summaries and figure captions, to improve answer quality.
+ **Sensitive data handling** – Detect and redact personally identifiable information (PII) before extracted content reaches downstream consumers.

## Capabilities
<a name="insights-capabilities"></a>

Each capability is a setting on your project. Turn on only the ones you need.


| **Capability** | **What it does** | **Configure it with** | **Learn more** | 
| --- | --- | --- | --- | 
| Extraction | Extracts text, layout elements, tables, and reading order as plain text, Markdown, HTML, or CSV. Always on. | `Extraction configuration` | [Extraction results](insights-extraction-results.md) | 
| Generative: Summaries and figure captions | Writes a summary of each document and a caption for each chart, graph, or image. | `Generative configuration` | [Document summarization and figure captioning](insights-summarization-captioning.md) | 
| Custom extraction | Extracts the fields you define in a blueprint, each with a confidence score. | `Custom configuration` | [Custom extraction with blueprints](insights-custom-extraction.md) | 
| Blueprint matching | Picks the right blueprint for each document, with an optional fallback blueprint. | `Custom configuration` (two or more blueprints) | [Blueprint matching and fallback blueprints](insights-blueprint-matching.md) | 
| Document splitting | Splits a file that holds several documents, such as a loan packet, into separate documents. | `Splitter configuration` | [Splitting multi-document files](insights-splitting.md) | 
| Sensitive data detection and redaction | Finds PII such as names, addresses, and Social Security numbers, and can write a redacted copy. | `Sensitive data configuration` | [Detecting and redacting sensitive data](insights-detecting-redacting.md) | 

You can combine them. For example, one job can split a loan packet, match each document to a blueprint, extract its fields, and redact PII.

## How you work with the service
<a name="insights-how-you-work-with-the-service"></a>

Amazon Textract Insights has two groups of operations:
+ Configuration operations manage projects (`CreateProject`, `GetProject`, `UpdateProject`, `DeleteProject`, `ListProjects`) and blueprints (`CreateBlueprint`, `CreateBlueprintVersion`, `GetBlueprint`, `UpdateBlueprint`, `DeleteBlueprint`, `ListBlueprints`). These operations are synchronous.
+ Runtime operations process documents. `StartDocumentInsights` starts an asynchronous job and returns a job ARN. `GetDocumentInsights` returns the job's status and, on success, the location of its results.

For request parameters, response fields, and errors, see the Amazon Textract Insights API Reference.

## Next steps
<a name="insights-next-steps"></a>
+ To learn how projects, the extraction configuration, and the custom configuration fit together, see [How Amazon Textract Insights works](insights-how-it-works.md).
+ To decide between Amazon Textract Insights and the Amazon Textract Core operations, see [Amazon Textract Insights compared with Amazon Textract Core APIs](insights-compared-core.md).
+ To set up access and process a document, see [Prerequisites and setup](insights-prerequisites.md) and [Tutorial: Process your first document](insights-tutorial.md).