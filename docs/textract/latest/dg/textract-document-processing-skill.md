

# Amazon Textract document processing skill

The Amazon Textract document processing skill helps you extract content from documents by making a request to your AI coding agent in natural language. You can extract text, tables, form fields, receipts, and identity documents. You identify a document and describe the output you want, and the agent returns structured results. You don't run any commands directly.

The skill is a way to use Amazon Textract through your AI coding agent, not a new API. The skill returns reading-order text, Markdown or CSV tables, key-value pairs, identity document fields, document answers, and confidence routing.

## Why it matters
<a name="textract-dps-why-it-matters"></a>

In practice, an agent can do any of the following:
+ Read a scanned multipage claim packet in reading order.
+ Pull line items off a receipt.
+ Extract fields from a driver's license.
+ Answer a direct question about an invoice.
+ Route a form into auto-accepted and needs-review fields by confidence.

Each result names the Amazon Textract operation that produced it.

Several coding assistants can already read a document by writing a custom SDK call or building a service wrapper. What they don't provide is a single Amazon-owned document-processing path that behaves consistently across all of them. That path is also auditable and least-privilege by default.

Consider the gap that the skill closes. The Amazon Textract API doesn't return linearized, reading-order text. It returns detected elements, such as words, lines, tables, and key-value pairs, each with its position on the page. The caller must reconstruct the reading order, stitch multi-column layouts back together, and render tables. The skill does this reconstruction and formatting for you. An agent gets clean reading-order text and Markdown or CSV tables directly, instead of raw geometry that it would have to reassemble.

Previously, adding document processing to an agent meant writing and maintaining the Amazon Textract calls, the asynchronous polling, the page reassembly, and the confidence logic in each team. It now means invoking one reviewed skill that already does all of that.

## How the skill is delivered
<a name="textract-dps-how-delivered"></a>

You don't install the skill manually. We distribute it as part of the Agent Toolkit for AWS, the AWS layer that your AI coding agent connects to. Your agent loads the skill automatically when your request involves processing a document. The skill can reach your agent through several methods, all of which operate through the same AWS service. The two most common methods are the following:
+ **Runtime discovery through the AWS Model Context Protocol (MCP) Server** – Your agent connects to the AWS MCP Server and retrieves the skill on demand, without any local installation. Agents such as Kiro connect to the server directly.
+ **Bundled with a plugin** – For agents such as Claude Code, Codex, and Devin, a single-install plugin (for example, aws-core) configures the connection and includes a curated set of skills. The skill is available immediately after installation.

Regardless of the method, your agent discovers the skill automatically, and you don't need a separate download or copy step. Document processing runs on AWS using your own AWS permissions. For the full set of installation methods, including local installation and the AWS CLI, see [Getting started with the Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html).

## Installing the Agent Toolkit for AWS
<a name="textract-dps-installing"></a>

You install the skill through the Agent Toolkit for AWS once, typically as an administrator. If you have the AWS CLI (version 2.35.0 or later), the fastest path is the interactive setup wizard. It detects your installed agents, installs the default skills, and configures the AWS MCP Server connection:

```
aws configure agent-toolkit
```

For other installation methods and per-agent instructions, see [Getting started with the Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html). The source for the toolkit is available in the [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website.

## Confirming that the skill is available
<a name="textract-dps-confirming"></a>

You aren't required to locate the skill yourself. When your request involves extracting content from a document, your agent identifies and loads the appropriate skill automatically. To confirm that the skill is available, ask your agent a question such as "What AWS skills do you have available?" or "Do you have a skill for reading documents?" When your agent connects through the AWS MCP Server, it searches the available skills and selects the one that matches your request.

To confirm that the connection to the AWS MCP Server is working, ask your agent "What AWS Regions are available?" If the agent returns a list of Regions, the connection is established.

If you prefer to verify from the command line and have the AWS CLI installed, you can list your installed skills and search the catalog:

```
aws agent-toolkit list-installed-skills
aws agent-toolkit search-skills --search-query document
```

For the full set of skill-management commands, see [AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

## Prerequisites
<a name="textract-dps-prerequisites"></a>

No per-request configuration is required. Before first use, confirm the following:
+ **The skill is enabled in your AI coding agent** – The skill must be available to the agent you use. Your administrator enables it once during setup.
+ **AWS access is configured** – Your agent requires permission to call Amazon Textract and to read your document from Amazon S3, with an AWS Region configured. An administrator grants this access once.
+ **The document is in a supported format** – Supported formats are PDF, PNG, JPEG, and TIFF. You can submit single-page images and PDF files directly. You must store multipage PDF and TIFF files in Amazon S3 first. Upload the file to a bucket in the same AWS Region that your agent uses, and confirm that the agent has permission to read it. The skill returns a single combined result with the pages in order. Larger files require more processing time, because the agent waits for the background job to complete.

## Regions and availability
<a name="textract-dps-regions"></a>

You don't select an AWS Region for each request. Your administrator configures the Region that your agent uses, and the skill operates in any Region where Amazon Textract is available. The skill isn't restricted to a single Region.

Note the following:
+ **Store your document in the same Region as your agent** – Upload the document to an Amazon S3 bucket in the Region that your agent is configured to use, so that the skill can read it.
+ **The connection Region is independent of the processing Region** – If your agent connects through the AWS MCP Server, that server is available in its own set of AWS Regions, and additional Regions are added over time. The Region through which you connect doesn't determine where your document is processed. Your document is always processed in the Region that your agent uses.

## Data handling
<a name="textract-dps-data-handling"></a>

Your document remains within your control. It stays in your own AWS account and Region. The skill reads the document from your Amazon S3 bucket and submits it to Amazon Textract using your AWS permissions. Amazon Textract performs the extraction and returns the content to your agent.

The skill doesn't retain your data. The AWS service through which your agent connects operates as a pass-through: it runs the request and returns the result without storing your document or the extracted text. Because all operations run under your AWS permissions, the skill can't provide access to a document that you aren't already authorized to read.

## Using the skill
<a name="textract-dps-using"></a>

Make a request in natural language and identify the document. For example:
+ "Extract the text from s3://amzn-s3-demo-bucket/contracts/nda.pdf in reading order."
+ "Extract the tables from this invoice as CSV."
+ "What is the total and due date on this utility bill?"
+ "Extract the fields from this driver's license."
+ "Extract the vendor, date, and line items from this receipt."
+ "Process this 40-page claim packet and return the text."
+ "From this form, automatically accept the high-confidence fields and flag the remainder for review."

The agent selects the appropriate operation, runs it, and returns only the information you requested.

## Single-page and multipage documents
<a name="textract-dps-single-multipage"></a>

A single-page image or PDF returns a result immediately. The skill processes a multipage PDF, such as a 40-page contract, asynchronously in the background, and it reassembles the pages in order, so you receive a single combined result. Processing a multipage document takes longer. You don't need to choose the processing mode. The skill determines it based on the document.

## Processing multiple files
<a name="textract-dps-multiple-files"></a>

You can request processing of multiple files in a single prompt. For example, you can point the skill at a folder of receipts in Amazon S3 with the prompt "Process every receipt under s3://amzn-s3-demo-bucket/receipts/ and summarize each." The skill returns one line for each file:

```
lunch-01.jpg    OK             Blue Bottle Coffee   USD $18.40
lunch-02.jpg    OK             Sweetgreen           USD $14.25
blurry-03.jpg   Needs review   (low confidence)
```

## Examples
<a name="textract-dps-examples"></a>

The following examples show representative input and output.

**Receipt to structured fields** – For a photograph of a lunch receipt, use the prompt "Extract the vendor, date, total, and line items." In this example, assume the total shown is USD $18.40.

```
Vendor: Blue Bottle Coffee
Date:   2026-03-14
Total:  USD $18.40
Line items:
Latte           USD $5.50
Avocado toast  USD $11.00
Tax             USD $1.90
```

**Invoice table to CSV** – For an invoice PDF, use the prompt "Return the line-item table as CSV."

```
Description,Quantity,UnitPrice,Amount
"Widget A",10,2.50,25.00
"Widget B",4,7.00,28.00
```

**Document question answering** – For a utility bill, use the prompt "What is the total amount due and the due date?"

```
Total amount due: USD $142.67
Payment due date: 2026-04-01
```

**Confidence routing** – For an intake form, use the prompt "Automatically accept fields above 80% confidence and flag the remainder." Confidence is a score from 0 to 100 percent that indicates how certain the system is that it read a value correctly. A high score indicates that the value is very likely correct. A low score indicates that the text was difficult to read. You set the threshold. Values at or above the threshold are accepted, and values below it are set aside for human review.

```
Auto-accepted:
Name: Jordan Lee (99%)
Date of birth: 1990-05-12 (97%)

Needs review:
Policy number: EXAMPLE-1234 (62%)
```

Low-confidence and sensitive values are flagged for human review rather than accepted automatically.

**Form fields to key-value pairs** – For a completed application form, use the prompt "Extract the form fields."

```
Full name: Jordan Lee
Email: jordan.lee@example.com
Position: Warehouse Associate
Start date: 2026-04-01
```

**Table to Markdown** – For a report PDF that contains a table, use the prompt "Return the table in Markdown."

```
| Region | Q1  | Q2  |
| ------ | --- | --- |
| West   | 120 | 135 |
| East   | 98  | 110 |
```

**Identity document to fields** – For a passport image, use the prompt "Extract the fields from this passport."

```
Document type: Passport
Surname: Lee
Given names: Jordan
Document number: X1234567
Date of birth: 1990-05-12
Expiration: 2030-08-01
```

## Troubleshooting
<a name="textract-dps-troubleshooting"></a>

Most issues fall into one of the following categories:
+ **The file can't be read** – Confirm that the file is in a supported format (PDF, PNG, JPEG, or TIFF) and that it isn't unusually large. Store large or multipage files in Amazon S3 rather than submitting them directly.
+ **Fields are blank, incorrect, or low-confidence** – This result typically indicates that the source scan was difficult to read, for example, blurred, skewed, low-resolution, or a photograph of a printed page. Rescan the document straight and at a higher resolution, and then submit it again. The skill flags low-confidence values intentionally rather than inferring them.
+ **The document can't be found** – The file must be in an Amazon S3 bucket in the same Region that your agent uses, and your agent must have permission to read it. Confirm that the bucket, file name, and Region are correct.

If a result still appears incorrect, review the values that the skill identified as low-confidence first, because those are the values it flags for review.