

# Data quality evaluation

## What it is
<a name="ai-data-preparation-dq-overview"></a>

With data quality evaluation, you measure the quality of a text or tabular dataset before you use it to train or evaluate a model. You run a job on a dataset that is registered in your hub and choose the evaluations in the job's evaluation configuration. SageMaker AI reports the results for the whole dataset and for each row. The job reads the dataset and never modifies it.

The job writes an aggregate report for the whole dataset and a row-level report, a copy of your rows with results that the job adds as columns. Some evaluations write more files, such as the findings file of the exploratory analysis.

You can evaluate dataset quality in three ways, and you can combine them in one job:
+ Built-in metrics: metrics that the service provides and that you choose by name, such as `word_count` or `pii_detection`, for length and format, duplicates, personally identifiable information (PII), language, topics, and diversity.
+ Data quality rules: Boolean conditions that each row must pass. A rule can check the fields of each row or the dataset as a whole. You write your rules in a data quality specification file, which can also ask for a label or a score for each row. A large language model (LLM) can judge a rule with a prompt that you write, a custom LLM-as-a-judge criterion, on its own or against documents that you provide.
+ Exploratory analysis: an agent that reads the dataset and writes the problems it finds, each with a title and the rows that show it, to a findings file, for a dataset where you do not yet know what to check. To act on the findings, see [Reading the results for a decision](#ai-data-preparation-dq-results-decision).

Only data quality rules use a specification file. You choose built-in metrics and exploratory analysis by name in the job's evaluation configuration. Data quality rules are the recommended way, because they check your rows against conditions that you define and name the rules that each row failed.

### When to use it
<a name="ai-data-preparation-dq-overview-when"></a>

Use data quality evaluation when:
+ You want to check the quality of a dataset that you generated with synthetic data generation (SDG) before you use it for training or customization.
+ You want to bring your own dataset (BYOD) for training and have its format validated and its quality measured first.
+ You want every row checked against data quality rules that you have written.
+ You want to check for duplicate rows.
+ You want the dataset explored for problems, because you do not yet know what to check.
+ You want to know which topics the dataset covers.

## How it works
<a name="ai-data-preparation-dq-how"></a>

A data quality evaluation is a data preparation job with the job category `DataQualityEvaluation`, created with the same `CreateJob` operation as the other data preparation jobs.

### The job
<a name="ai-data-preparation-dq-how-job"></a>

A job has five parts:
+ The job name, a name that no existing job has.
+ The execution role, the IAM role that the job uses to read the dataset and write its files.
+ The input dataset, one registered dataset.
+ The output location, an Amazon S3 location in the job's AWS Region.
+ The evaluation configuration, the list of operations to run, each an operator and its settings.

### The dataset
<a name="ai-data-preparation-dq-how-dataset"></a>

A job evaluates one dataset, named by its ARN in `InputDataConfig`. The dataset is hub content of type `DataSet` in a hub in your account. Its registry entry names the file format in `DatasetFileFormat`, which decides the columns that the operators read when you name none.

### The job lifecycle
<a name="ai-data-preparation-dq-how-lifecycle"></a>

`CreateJob` returns the job ARN. `DescribeJob` reports a `JobStatus` and a `SecondaryStatus` with a message for each status the job passed through. The `JobStatus` is `InProgress`, `Stopping`, `Completed`, `Failed`, or `Stopped`. The secondary statuses of a successful job, in order, are the following.


| Secondary status | What the job is doing | 
| --- | --- | 
| Validating | Validates the Region, the Amazon S3 locations, and the data quality specification or code artifact named for the job. | 
| Preparing | Prepares the evaluation artifacts. | 
| Executing | Executes the operations. | 
| Publishing | Writes the output files to the output location. | 
| Finalizing | Adds the job's entry to the dataset's registry entry. | 
| Completed | Done, with MetadataS3Uri, the location of the job's metadata.json, inside the returned configuration of the DescribeJob response. | 

A `Failed` job has a `FailureReason`. A job that has reached `Publishing` can no longer be stopped. A stopped job has no `FailureReason`, writes nothing under its own folder, and adds no entry to the dataset.

### The output location
<a name="ai-data-preparation-dq-how-output"></a>

Every job writes to its own folder in the output location, so several jobs can share one `S3OutputPath`. The job also records its evaluation on the dataset: it adds an entry that points to its output to the `JobMetadata` list of the dataset's entry in your hub. It creates no new dataset and no new version, so the dataset's ARN and version do not change.

### The operations
<a name="ai-data-preparation-dq-how-operations"></a>

`EvaluationConfig.Operations` lists the operations of the job. Each operation names an `Operator`, a built-in metric or an evaluation from the table under [Operators](#ai-data-preparation-dq-how-operators), and an optional `Config` with its settings. The following operation counts the words of the `prompt` column. In the following example, replace `prompt` with the name of your text column:

```json
{"Operator": "word_count", "Config": {"View": [{"Role": "Text", "Column": "prompt"}]}}
```

`Config.View` names the columns that the operator reads, one entry for each column, each a role and a column name. The roles are the following:
+ `Text`, a column of text, read by the text metrics.
+ `Column`, a numeric or categorical column, read by the column statistics, with one result for each column.
+ `Label`, a label column, read by the balance metrics.
+ `Messages`, a column of conversation turns.

The other keys of `Config` are the operator's settings, and the service refuses a key that the operator does not define when you submit the job. The following operation detects the language of the `prompt` column and flags the rows that are not English, with the accepted languages and the lowest accepted score as settings:

```json
{"Operator": "language_detection", "Config": {"View": [{"Role": "Text", "Column": "prompt"}], "languages": ["en"], "min_score": 0.5}}
```

Without a `View`, an operator reads the default text columns of the dataset's format: the prompt column and, where the format has one, the completion column. You can run the same operator on two columns as two operations in one job. The service refuses the same operator with the same `Config` twice as a duplicate.

### Operators
<a name="ai-data-preparation-dq-how-operators"></a>

An operator is a measurement, a check, or an analysis that the job runs on your dataset. Every built-in metric writes its summary to the aggregate report, and some also write a column for each row to the row-level report. The following table lists each operator group, what it does, the columns it reads, and its operators: 41 built-in metrics and the four evaluations `default_metrics`, `spec_eval`, `exploratory_analysis`, and `data-validation`.


| Operator group | What it does | Columns read | Operator | 
| --- | --- | --- | --- | 
| Data quality rules | Evaluation of every row, or a sample, and the whole dataset against the rules in your data quality specification file. | The whole row. | spec\_eval | 
| Exploratory analysis | An agent that explores the dataset and writes its findings. | The whole row. | exploratory\_analysis | 
| Text quality | The length, format, and variety of the text. effectiveness: one score for the size of the dataset, no column read. | One text column, role Text. | word\_count, character\_count, compression\_ratio, format\_distribution, plain\_text\_ratio, content\_structures, uniqueness, ngram\_diversity, mif\_score, effectiveness | 
| Text filters | Flags on the rows to filter out, with no row removed: text that is mostly URLs, text with few letters and digits, repeated words or characters, broken character encoding, text that is too short or too long, and lines that are too short. | One text column, role Text. | urls\_filter, alphanumeric\_filter, word\_repetition\_filter, char\_repetition\_filter, mojibake\_filter, character\_length\_filter, average\_line\_length\_filter | 
| Keyword topics | The rows for each topic from a keyword list that you provide, and the share of your topics that the dataset covers. | One text column, role Text. | keyword\_topic\_counts, keyword\_topic\_coverage | 
| Column statistics | A statistic for each numeric column, and the counts of null values, non-numeric values, the most frequent value, and the frequency of each value. | One or more columns, role Column. | min, max, mean, median, std\_dev, skewness, kurtosis, percentiles, count\_zero, count\_null, count\_non\_numeric, mode, value\_frequency | 
| Label balance | How evenly the label values are distributed, as a balance score and as a ratio, over all labels and for each label column. | One or more columns, role Label. | data\_balance, data\_balance\_ratio, field\_balance, field\_balance\_ratio | 
| Language | The language of each row, and a flag on the rows whose language is not in your list. | One text column, role Text, required on every format. | language\_detection | 
| PII | Flags on the sampled rows that contain personally identifiable information (PII). | One column, role Text or Messages, required on every format. | pii\_detection | 
| Duplicates | Flags on the rows whose text repeats another row's, byte for byte or by similarity, with no row removed. | One text column, role Text. | exact\_dedup, fuzzy\_dedup | 
| Taxonomy | A three-level taxonomy of the rows for each framing that you request, task, domain, or quality. | One text column, role Text. | taxonomy | 
| Default metrics | Nine of the text quality metrics at once on the format's default text columns. | The format's default text columns. | default\_metrics | 
| Format validation | Every record checked against the file format that you declared when you registered the dataset. | The whole record. | data-validation | 

#### Metric settings
<a name="ai-data-preparation-dq-ops-settings"></a>

The following built-in metrics take settings in `Config`, beside the `View`.


| Operator | Setting | Values | 
| --- | --- | --- | 
| uniqueness | CaseSensitive | true by default. | 
| ngram\_diversity | N | 1 to 8, with 1 the default. | 
| mif\_score | mode | corpus or per\_row. | 
| character\_length\_filter | min\_length, max\_length | The shortest and the longest accepted text, in characters. | 
| keyword\_topic\_counts, keyword\_topic\_coverage | topic\_keywords | A map from each topic to its keywords. | 
| keyword\_topic\_counts, keyword\_topic\_coverage | default\_topic | The topic for the rows that no keyword matches. | 
| language\_detection | languages | A list of language codes. | 
| language\_detection | min\_score | The lowest accepted score for the detected language, with the rows below it flagged. | 
| taxonomy | framings | A list from task, domain, and quality, with all three the default. | 
| exact\_dedup | Normalize | false by default. | 
| fuzzy\_dedup | JaccardThreshold | The similarity at which two rows count as duplicates, with 0.7 the default. | 
| fuzzy\_dedup | Lowercase | true by default. | 

#### Data quality specification evaluation
<a name="ai-data-preparation-dq-ops-spec-eval"></a>

`spec_eval` evaluates each row, or a sample of the rows, and the whole dataset against the data quality specification file named in its `Config`. It reads whole rows and takes no `View`. Its `Config` takes the following keys.


| Key | What it is | Required | 
| --- | --- | --- | 
| SpecS3Uri | The Amazon S3 location of your data quality specification file, a .md or .txt file in the prose or the structured form. | Exactly one of SpecS3Uri and CodeArtifactS3Uri. | 
| CodeArtifactS3Uri | The spec\_eval/ folder that an earlier job wrote, as it is or with a judge\_code.py that you modified. The job runs that code and reads no specification file. | Exactly one of SpecS3Uri and CodeArtifactS3Uri. | 
| ContextDocumentsS3Uri | An Amazon S3 folder of context documents that your criteria are judged against. The folder also adds the service's own faithfulness check. | Optional. | 
| DownSampleRecordCount | The number of rows to judge instead of all of them. The rows outside the sample carry null in the four specification columns of the row-level report. | Optional. | 
| ModelConfig.JudgeModelConfig.ModelId | The model that judges the rows, us.anthropic.claude-sonnet-5 by default. The accepted ids are us.anthropic.claude-sonnet-5, us.anthropic.claude-sonnet-4-6, us.anthropic.claude-opus-4-6-v1, us.anthropic.claude-sonnet-4-5-20250929-v1:0, us.anthropic.claude-sonnet-4-20250514-v1:0, us.anthropic.claude-haiku-4-5-20251001-v1:0, and openai.gpt-oss-120b-1:0, and the service refuses another id. | Optional. | 

#### Exploratory analysis
<a name="ai-data-preparation-dq-ops-exploratory"></a>

`exploratory_analysis` runs an agent that reads the dataset and writes a list of findings, each with a title and the rows that show it, to the findings file `aggregate/exploratory/findings.json`. It takes no `Config` and writes no row column.

#### PII detection
<a name="ai-data-preparation-dq-ops-pii"></a>

`pii_detection` uses Amazon Bedrock models to find personally identifiable information (PII). It reads a sample of the rows of one `Text` or `Messages` column, so its `View` has exactly one entry and is required on every format. It flags each sampled row that contains PII and records the kinds found. It takes no other setting and never writes a detected value to the output.

PII detection finds direct identifiers only: information that identifies an individual on its own, such as a name or an account number. It does not find quasi-identifiers: information that identifies an individual only in combination with other information.

The categories it detects are the following:
+ Names and contact details: private names, public names, email addresses, and phone numbers.
+ Addresses and locations: full addresses, partial addresses, and GPS coordinates.
+ Government and financial numbers: card numbers, card codes and expiry dates, bank account numbers, PINs, Social Security numbers, driver's license numbers, passport numbers, and other government IDs.
+ Account, device, and network identifiers: IP addresses, MAC addresses, user names, device and tracking IDs, and account and membership numbers.
+ Vehicle identifiers: license plates and vehicle identification numbers.
+ Passwords and credentials: passwords and other credentials.
+ Dates and age: personal dates, such as a date of birth, and age.
+ Web addresses: public URLs and private URLs.

#### Taxonomy
<a name="ai-data-preparation-dq-ops-taxonomy"></a>

`taxonomy` groups the rows of one text column into a three-level taxonomy for each framing that you request, `task`, `domain`, or `quality`. It writes the three levels of each framing to the row-level report and an HTML report.

#### Deduplication
<a name="ai-data-preparation-dq-ops-dedup"></a>

`exact_dedup` and `fuzzy_dedup` flag the duplicates in one text column and remove no row. Each flagged row carries a reason and the id of the first row of its group.

#### Default metrics and format validation
<a name="ai-data-preparation-dq-ops-default"></a>

`default_metrics` runs `word_count`, `character_count`, `format_distribution`, `plain_text_ratio`, `compression_ratio`, `uniqueness`, `ngram_diversity`, `mif_score`, and `effectiveness` on the format's default text columns and takes no `Config`. On a format without default columns, list the metrics yourself with a `View`.

`data-validation` checks every record against the format that you declared, and it reads JSON Lines and Parquet datasets. It takes no `Config` and must be the only operation in its job.

### How a data quality specification works
<a name="ai-data-preparation-dq-spec-write"></a>

A data quality specification file states your data quality rules, the conditions that each row or the whole dataset must pass, and any measurements that you want taken. You write the rules in your own words, such as that a reply must answer the question or that a completion must have at least eight words. The job turns the file into criteria, runs them on every row or on a sample, and reports which rows failed which rule and the value of each measurement.

#### The two forms
<a name="ai-data-preparation-dq-spec-forms"></a>

You write a data quality specification in one of two forms:
+ The prose form: rules written as sentences, with no special syntax, for a first specification or for rules that are still changing.
+ The structured form: a `## Criteria` section whose entries name each criterion and state how it is decided, for an evaluation that you repeat with stable criterion ids.

The `## Criteria` heading is what makes a file structured, and both forms are read the same way whether the file name ends in `.md` or `.txt`.

#### Rules and measurements
<a name="ai-data-preparation-dq-spec-kinds"></a>

Each rule or measurement that you write becomes a criterion, the unit that the job evaluates. A criterion is a rule, with a pass or fail verdict, or a measurement, with a value and no verdict, for every row or once for the whole dataset. From a prose file, a model derives one criterion for each rule or measurement and takes a threshold from the sentence when it states one. From a structured file, the job reads the ids and the descriptions as written.

#### How a criterion is decided
<a name="ai-data-preparation-dq-spec-decided"></a>

The job decides a criterion from your description, with your own prompt, or against your context documents, and a criterion can combine the last two. In the prose form the job chooses from your sentences, and in the structured form you choose with the keys of the entry:
+ From your description. The service turns the description into generated code or into a judge prompt for a model, whichever fits the criterion. This is the default.
+ With your own prompt. A `prompt` line sends your text to the model as written, in place of the judge prompt that the service would write. This is a custom LLM-as-a-judge criterion: the model judges each row with your prompt, as a rule or as a measurement.
+ Against your context documents. The documents that you give the job are the reference for the criterion. In the structured form a criterion marked `context: documents` is judged this way, and in the prose form a rule or a measurement that refers to the documents is judged this way.

The following structured data quality specification shows one criterion decided from its description, one judged with your prompt, and one judged with your prompt against the documents:

**Example Data quality specification using three evaluation methods**  

```
# Replies judged three ways

## Criteria
- id: completion_present
  description: The completion field is present and is not blank or whitespace only.
- id: reply_is_actionable
  prompt: You are reviewing a customer-support reply. Read the PROMPT (the customer's message) and the COMPLETION (the agent's reply). Answer PASS if the reply tells the customer exactly what will happen next or what they must do next. Answer FAIL if the reply only acknowledges the problem, restates it, or gives no next step.
  description: The reply tells the customer what happens next or what to do next.
- id: reply_follows_guide
  context: documents
  prompt: You are reviewing a customer-support reply against the reference documents. Read the COMPLETION (the agent's reply) and the documents. Answer PASS if the reply follows every rule that the documents state for replies. Answer FAIL if it breaks one, and name the rule.
  description: The reply follows the rules in the style guide.
```

The service decides `completion_present` from its description, judges `reply_is_actionable` with your prompt, and judges `reply_follows_guide` with your prompt against the documents.

#### Context documents
<a name="ai-data-preparation-dq-spec-documents"></a>

You can give the job context documents in an Amazon S3 folder, named by `ContextDocumentsS3Uri` in the `spec_eval` operation. When you do, the service adds its own check, `builtin_faithfulness`, which judges whether each row is grounded in the documents: every factual claim in the row must be stated by the documents or follow from them. A row that fails this check counts as failed, so give the job documents that state the facts that your rows rely on. The pass rate of a criterion judged against the documents, the service's own or yours, is under `context_criteria` in the aggregate report.

**Important**  
The data quality specification and the context documents control how your rows are judged. The job sends your specification, and your context documents when you give them, to the model as written, and the service does not detect or remove instructions in that text. The model also follows text that you did not write as a rule, such as instructions inside a document that you downloaded, and such text can change the verdicts. Before you submit a job, review the specification and the documents, and use only files that you wrote or that you trust.

#### What the job writes
<a name="ai-data-preparation-dq-spec-output"></a>

A `spec_eval` operation writes the following to the output folder, the same for both forms:
+ The criteria that the job derived or read, in `spec_eval/extracted_criteria.json` in the output folder, so that you can check how it read your rules.
+ A `spec_eval` entry in the aggregate report, with the counts and the pass rates over the dataset.
+ Four columns for each row in the row-level report: the verdict, the rules that the row failed, the criteria that could not be evaluated, and each criterion's result.

#### Data quality specification examples
<a name="ai-data-preparation-dq-spec-write-example"></a>

##### Structured data quality specification example
<a name="ai-data-preparation-dq-spec-structured"></a>

The following structured data quality specification was run on the 200-row customer-support dataset of the [Use example](#ai-data-preparation-dq-use). It holds a rule decided by code, a rule decided by a model, a label, a score, and a rule over the whole dataset, five of the file's seven criteria, with the description of `tone` shortened. The table at the end of this section explains each key.

```
# Data quality rules for the customer-support training dataset

## Stratify by
- category

## Criteria
- id: completion_min_length
  type: code!
  threshold: {"min_words": 8}
  description: The completion contains at least min_words words, counted by splitting on whitespace.
- id: answers_the_question
  type: llm!
  description: The completion answers what the customer asked in the prompt. A reply that restates the question, changes the subject, or refuses without a reason fails.
- id: tone
  kind: metric
  values: [formal, friendly, curt]
  description: Classify the tone of the completion as formal, friendly, or curt.
- id: helpfulness
  kind: metric
  values: 0 to 1
  description: Score how completely the completion resolves the customer's problem, from 0.0 (does not help) to 1.0 (fully resolves it), in steps of 0.25. 0.5 means a partial answer that leaves the customer with a next step to find on their own.
- id: answer_rate
  scope: aggregate
  inputs: [answers_the_question]
  threshold: {"min_rate": 0.9}
  description: At least min_rate of the rows pass answers_the_question.
```

The job judged all 200 rows, of which 173 passed and 27 failed. `completion_min_length` had a pass rate of 0.96 and `answers_the_question` of 0.87, with a pass rate for each value of `category`, such as 0.84 on the `billing` rows. `answer_rate` returned one verdict, a fail, with the reason `174/200 rows passed answers_the_question (rate=0.870), threshold=0.9`. The labels of `tone` and the scores of `helpfulness` appear per row as the `value` of their entries, with no pass rate and no distribution in the aggregate report.

##### Sections and keys of a structured data quality specification
<a name="ai-data-preparation-dq-spec-grammar"></a>

The following table lists the sections and the keys of a structured data quality specification.


| Section or key | What it is | 
| --- | --- | 
| \#\# Stratify by | An optional section before \#\# Criteria with one column name on each line. Every row rule then reports its pass rate for each value of that column. | 
| \#\# Criteria | The section that holds the criteria, one entry each, and the heading that makes the file structured. | 
| id | The name of the criterion, which starts its entry and keys its result in the report and in every row. | 
| kind | rule, the default, for a pass or fail verdict, or metric for a measurement with a value and no verdict. | 
| type | What decides the criterion: auto, the default, lets the job choose, code and llm request generated code or a model, and code\! and llm\! lock that choice, which the report records. On a criterion with a prompt or a context: documents line, leave the type line out, because the model always judges such a criterion. | 
| scope | row, the default, for a result per row, or aggregate for one result over the whole dataset. | 
| values | The results that a measurement may return, as labels in brackets such as [formal, friendly, curt] or as a range such as 0 to 1. | 
| threshold | A JSON object with the numbers that a rule compares against, such as {"min\_words": 8}, on rules only. | 
| inputs | The row criteria that an aggregate criterion reads, such as the row rule whose pass rate it requires. | 
| reads | The fields of your rows that the criterion uses, such as [completion], echoed in the report. A field that your rows do not have makes the criterion not evaluable on any row. | 
| context: documents | The model judges the criterion against the documents that you provide. In the row-level report such a criterion has the source context, its result in outcome instead of verdict, such as fail, measured, not\_applicable, or not\_evaluable, and the passage it relied on in quote and evidence. | 
| prompt | The exact text that the model judges with, one paragraph for each line, sent as written in place of the judge prompt that the service writes from the description. The description stays for the report. With a context: documents line as well, the model judges with your prompt against the documents. | 
| description | What the criterion evaluates, in words, which the generated code or the model follows. | 

## Inputs
<a name="ai-data-preparation-dq-inputs"></a>

A job takes one registered dataset, often the dataset that [Synthetic data generation](ai-data-preparation-sdg.md) produced and registered as hub content of type `DataSet`, whose `arn` you pass to the job unchanged. You can also bring your own dataset (BYOD), register it in a hub, and evaluate it the same way. For data quality rules, you also need the data quality specification file and, if your criteria refer to documents, the context documents.

In the snippets on this page, replace {{amzn-s3-demo-bucket}} with the name of your Amazon S3 bucket.

### The dataset file and its format
<a name="ai-data-preparation-dq-inputs-format"></a>

The job reads one dataset from one Amazon S3 location, a single file or a folder of Parquet shards with identical columns. The file's extension decides how it is read:
+ `.jsonl`: JSON Lines, one JSON object per line.
+ `.csv`: CSV with a header row that names every column.
+ `.parquet`: Parquet.
+ `.sqlite` or `.db`: a SQLite database with one table.

A file with any other extension fails the job. The job reads text and tabular data, not image, audio, or video data. The location must be in the job's Region and in your account. Column names that start with `dq_input__` are reserved for the job's own derived columns. The dataset's files total at most 18 GB for a job that runs `exploratory_analysis`, 30 GB for a job that runs `spec_eval`, and 90 GB for every other job. A job with several operations takes the smallest of their limits.

When you register the dataset, you name its format in `DatasetFileFormat`, and most training formats give the job default text columns to read when an operation has no `View`. The row shape of each format is described in [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets). Without a `View`, an operator reads the format's prompt column and, where the format has one, its completion column, such as `prompt` and `completion` for `HF_Prompt_Completion`. `Nova_RLVR`, `Nova_DPO`, `MTRL`, and a `Custom` dataset whose columns are not named `prompt` and `completion` have no default columns, so every operator needs a `View` on them. When your rows fit no named format, register the dataset as `Custom` and name the column that each operator reads in a `View`.

### Registering your own data
<a name="ai-data-preparation-dq-inputs-register"></a>

To bring your own dataset (BYOD), upload the file to a prefix of its own in Amazon S3 and register that prefix as a dataset in a hub in your account. In the Amazon SageMaker Python SDK, `DataSet.create` registers the dataset and returns the `DataSet` whose `arn` you pass to the job. The registry entry it writes has the `DatasetType` `BYOD`, the `DatasetFileFormat`, and the data's location:

```json
{
    "DatasetType": "BYOD",
    "DatasetFileFormat": "HF_Prompt_Completion",
    "DatasetS3Uri": "s3://{{amzn-s3-demo-bucket}}/datasets/support-conversations/"
}
```

A dataset that `DataSet.create` registers has the document schema that the job requires.

### The data quality specification file
<a name="ai-data-preparation-dq-inputs-spec"></a>

Upload your data quality specification file, with a name that ends in `.md` or `.txt`, to Amazon S3. To judge rows against your own documents, upload them to a folder of their own. You name both locations in the `spec_eval` operation, with `SpecS3Uri` and `ContextDocumentsS3Uri`. If the dataset came from synthetic data generation, you can pass the specification that generated it as `SpecS3Uri`, because a generation specification is also a valid specification for this job, which reads only the file that you name. Review the specification and the documents before you upload them, as the Important note under [How a data quality specification works](#ai-data-preparation-dq-spec-write) says.

## Use data quality evaluation
<a name="ai-data-preparation-dq-use"></a>

You can run data quality evaluation in the Amazon SageMaker Python SDK directly, or through a coding assistant with the core AI and ML skill of the Agent Toolkit for AWS. Both run the same job and write the same result files.

------
#### [ Amazon SageMaker Python SDK ]

In the following example, you evaluate a dataset of 200 customer-support conversations prepared for training a reply model, with the customer's message in `prompt` and the agent's reply in `completion`. One job runs three operations:
+ The built-in default metrics.
+ The rules in your data quality specification file.
+ An exploratory analysis, for problems that your specification does not cover.

For another evaluation, change the `Operations` list.

The example assumes an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup), and a registered dataset, as described under Inputs. The file `support-spec.md` is a structured specification in the form that [How a data quality specification works](#ai-data-preparation-dq-spec-write) shows. Upload it to Amazon S3 with the following AWS CLI command:

```bash
aws s3 cp support-spec.md s3://{{amzn-s3-demo-bucket}}/dq/support-spec.md
```

Then run the following Python code:

```python
from sagemaker.core.helper.session_helper import Session
from sagemaker.ai_registry import DataPreparer, DatasetJobConfig, JobCategory

session = Session()
preparer = DataPreparer(
    sagemaker_session=session,
    role="arn:aws:iam::123456789012:role/{{role-name}}",
)

# 1. List every field that a data quality evaluation job accepts.
DatasetJobConfig.print_schema(JobCategory.DataQualityEvaluation)

# 2. Describe the job: the registered dataset, where to write the results,
#    and the three operations to run on every record.
config = DatasetJobConfig(
    schema_version="3.0.0",  # selects the request format this page documents
    input_data_config=[{
        "DatasetArn": "arn:aws:sagemaker:{{region}}:123456789012:hub-content/"
                      "{{hub-name}}/DataSet/support-conversations/0.0.1",
    }],
    output_data_config={
        "S3OutputPath": "s3://{{amzn-s3-demo-bucket}}/dq/support-conversations/out/",
    },
    evaluation_config={
        "Operations": [
            {"Operator": "default_metrics"},
            {"Operator": "spec_eval", "Config": {
                "SpecS3Uri": "s3://{{amzn-s3-demo-bucket}}/dq/support-spec.md",
            }},
            {"Operator": "exploratory_analysis"},
        ],
    },
)

# 3. Submit the job and wait for it. The call prints the job ARN when it
#    submits, shows the job's status while it waits, and returns the dataset
#    with job_arn set when the job completes.
dataset = preparer.evaluate(config, base_job_name="support-conversations-dq", wait=True)
print(dataset.arn, dataset.job_arn)

# 4. If your session ends while the job runs, reconnect with the job ARN
#    that step 3 printed.
# dataset = DataPreparer.attach("{{job-arn}}")
```

The fields of the example are the following. The keys of the `spec_eval` operation are in its entry under [Operators](#ai-data-preparation-dq-how-operators).


| Field | What it is | Required | 
| --- | --- | --- | 
| role on DataPreparer | The execution role. Without it, the SDK reads the role from your SageMaker AI configuration or from get\_execution\_role(). | Optional when a role resolves from your configuration, otherwise the SDK refuses to submit. | 
| schema\_version on DatasetJobConfig | The request format that this page documents, in which EvaluationConfig holds an Operations list. Without it, the SDK sends a request format that does not accept Operations. | Required for the request shown here. | 
| InputDataConfig[].DatasetArn | The ARN of the registered dataset to evaluate. | Required. | 
| OutputDataConfig.S3OutputPath | The Amazon S3 prefix for the result files. Without it, the SDK fills s3://{{default-bucket}}/DataPreparer/DataQualityEvaluation/{{base-job-name}}. | Required in the request, supplied by the SDK when you omit it. | 
| EvaluationConfig.Operations[].Operator | The operator to run. | At least one operation. | 
| base\_job\_name on evaluate() | The prefix of the job name, to which the SDK appends a timestamp. To name the job yourself, pass job\_name instead, a name that no existing job has. | Optional. | 

The `evaluate()` call polls the job's status every 30 seconds and prints the first 10 rows of the row-level report when the job completes. The returned object carries the dataset and the job ARN and no results, which the job writes to the output location. To submit the job and return at once, pass `wait=False`, which returns a handle on the job, and later run `DataPreparer.attach("{{job-arn}}")` to wait for the job and receive its `DataSet`.

The job ARN has the form `arn:aws:sagemaker:{{region}}:{{account-id}}:job/DataQualityEvaluation/{{job-name}}`. You manage a submitted job with `DescribeJob`, `ListJobs`, `StopJob` (or `DataPreparer.stop("{{job-arn}}")` in the SDK), and `DeleteJob`, which the Amazon SageMaker AI API Reference documents. A deleted job's entry stays on the dataset.

------
#### [ Coding assistant with the AI and ML skill ]

With a coding assistant and the core AI and ML skill of the Agent Toolkit for AWS, the assistant runs data quality evaluation for you through a guided conversation. To install it, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/). As with the SDK, use an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup).

Start with a prompt for the coding assistant that describes your data and the use you intend for it:

```
I have 200 customer-support conversations in s3://{{amzn-s3-demo-bucket}}/dq/support-conversations.jsonl
that I want to train a reply model on. My data quality rules are in support-spec.md.
Tell me whether the dataset passes those rules, and which records do not.
```

The assistant then works through the same steps as the SDK example, and asks for your approval before each job:

1. The assistant gets your data quality rules, by asking what the data must satisfy and turning your answers into rules, or by reading the data quality specification that you already have.

1. It checks the file's format and registers the dataset, then tells you which built-in metrics apply to that format.

1. It shows you the plan, with the dataset, the specification, the metrics, the exploratory analysis, the output location, and the Region, and tells you that the job is billed to your account. Nothing is uploaded, registered, or submitted until you confirm.

1. It submits the job and waits for it, or it saves the work as a notebook or script that you can run and rerun yourself.

1. It reads the result files, writes a report with the findings, the records that failed your rules, and the tokens used, and offers the next steps, such as transforming the flagged records.

------

### Permissions and billing
<a name="ai-data-preparation-dq-use-permissions"></a>

A data quality evaluation job needs the following permissions, whichever entry point submits it.


| Who | Permissions | 
| --- | --- | 
| The execution role | bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream, s3:GetBucketLocation, read and write access to the input and output locations, and sagemaker:ImportHubContent on the hub that holds the dataset. | 
| The identity that manages jobs | sagemaker:DescribeJob and sagemaker:StopJob on the job ARN, sagemaker:DeleteJob, and sagemaker:ListJobs. | 
| The identity that submits the job | sagemaker:CreateJob on the job ARN, iam:PassRole for the execution role to job.sagemaker.amazonaws.com, and sagemaker:ImportHubContent and sagemaker:UpdateHubContent on the dataset and its hub, so that the job can record its result on the dataset. | 
| The trust policy of the execution role | sagemaker.amazonaws.com allowed to assume the role. This is a different service name from the one in the iam:PassRole condition above, and the job needs both as written. | 

**Note**  
The job calls Amazon Bedrock models on your behalf, so the execution role needs permission to call them, and the models' pricing and on-demand quotas apply to the job. The following evaluations call a model:  
The data quality specification evaluation calls a model once to derive the criteria from your specification. Then, for every row, it calls a model on each criterion that a model decides. Criteria that generated code decides cost no model calls. To try a specification on a sample first, set `DownSampleRecordCount`.
The exploratory analysis, PII detection, and taxonomy call a model on the rows they read.
The file `token_usage_report.json` in the output folder records the models the job called and the tokens it used.

## Results
<a name="ai-data-preparation-dq-results"></a>

A completed job writes the following files under its own folder in the output location, `{{S3OutputPath}}data-quality-evaluation/{{job-name}}/{{created-at}}/`. The following table lists each file, what it holds, and when the job writes it.


| File | What it holds | When the job writes it | 
| --- | --- | --- | 
| The index file metadata.json | The starting point of a run: the job, the dataset, the evaluation configuration you sent, the time, and under Reports the locations of the aggregate report, the row-level report, and the findings and data quality specification evaluation files when the job writes them. Its own location is MetadataS3Uri on the dataset's entry and in the DescribeJob response. It does not list token\_usage\_report.json or the taxonomy report. | Every completed job. | 
| The aggregate report aggregate/quality\_report.json | One entry per measurement over the whole dataset. | Every completed job except a data-validation job, which writes its own report under validation/. | 
| The row-level report record\_level/evaluated\_data.jsonl | A copy of your rows, unchanged, with the metric values and the rule verdicts added as columns whose names start with dq\_. | Every completed job, unless its only operation is exploratory\_analysis or it is a data-validation job. | 
| The usage file token\_usage\_report.json | The models the job called and the tokens it used, in total and for each model. | Every completed job. | 
| The folder spec\_eval/ | extracted\_criteria.json, the criteria the job derived or read. judge\_code.py, the program that judged the rows. judge\_config.json, the model id, the token cap, and the Region of the judging. reproduce.py, a script that replays the judging on your own machine. judge\_texts.json, for a job that judged against your documents. | A job that ran spec\_eval. | 
| The findings file aggregate/exploratory/findings.json | The problems the analysis found, each with a title and evidence, the counts and example rows it rests on. The same list is under the exploratory\_analysis key of the aggregate report. | A job that ran exploratory\_analysis. | 
| The taxonomy report aggregate/taxonomy/{{run-id}}/taxonomy\_report.html | The taxonomy of the rows, where {{run-id}} is the run identifier the job assigns. Its location is taxonomy\_report\_path in the taxonomy entry of the aggregate report. | A job that ran taxonomy. | 
| The files under validation/ | The validation set's metadata file, a report with the counts of valid and failed records, the failure rate, and the record shape the job detected, one line for each record that failed, and the indices of those records, beside the job's own metadata.json and token\_usage\_report.json. | A data-validation job. | 

### The columns that the operators write
<a name="ai-data-preparation-dq-results-columns"></a>

The following table lists the columns that each operator writes to the row-level report, where `<column>` stands for the column that the operator read.


| Metrics | Row columns | Notes | 
| --- | --- | --- | 
| Text quality: word\_count, character\_count, compression\_ratio, content\_structures, and mif\_score in its per\_row mode | One column for each metric, named after the column read, such as dq\_word\_count\_\_prompt. | The other five text quality metrics write report entries only. | 
| Text filters | dq\_<name>\_flagged\_\_<column> and dq\_<name>\_score\_\_<column>. | The stem of average\_line\_length\_filter is avg\_line\_length\_filter, and the score column of mojibake\_filter is dq\_mojibake\_filter\_regex\_score\_\_<column>. | 
| Keyword topics | None. | Report entries only. | 
| Column statistics | None. | One result for each column named, no setting. percentiles reports the 5th, 25th, 50th, 75th, and 95th percentiles. | 
| Label balance | None. | No setting. | 
| Language | dq\_lang\_\_<column>, dq\_lang\_score\_\_<column>, and dq\_language\_detection\_flagged\_\_<column>. | You need a View on every format. | 
| PII detection | dq\_pii\_status\_\_<column> (pii\_found or clean), dq\_pii\_types\_\_<column> (the kinds of PII found), and dq\_pii\_flagged\_\_<column>. | A sample of the rows is read. | 
| Taxonomy | dq\_taxonomy\_<framing>\_l1\_\_<column>, \_l2, \_l3, and \_margin for each framing. | The HTML report is listed above. | 
| Deduplication | dq\_<name>\_row\_id\_\_<column>, dq\_<name>\_flagged\_\_<column>, dq\_<name>\_reason\_\_<column>, and dq\_<name>\_representative\_row\_id\_\_<column>. | The reason is exact\_duplicate or near\_duplicate on a flagged row, representative on the first row of a group, and unique on every other row. | 
| Data quality specification evaluation | dq\_spec\_eval\_pass (true when the row passed every rule, false when it failed one, null when the row was not judged), dq\_spec\_eval\_failed\_criteria (the ids of the rules the row failed), dq\_spec\_eval\_errored\_criteria (the ids of the criteria that could not be evaluated), and dq\_spec\_eval\_criteria (one entry per criterion, keyed by its id, with the verdict or the value, the reason, a confidence, and source, which is code, llm, prompt, or context). | The rows outside a DownSampleRecordCount sample carry null in all four. | 
| Exploratory analysis | None. | The findings are in aggregate/exploratory/findings.json. | 

### What the example job wrote
<a name="ai-data-preparation-dq-results-example"></a>

The following excerpts come from the job of the Use example. The aggregate report opens with `total_volume` and `total_samples`, the number of rows read, and `derived_inputs` when an operation ran without a `View`. Each measurement's key holds one entry per `View`, with `view`, the columns read, and `result`.

On a job without a `View`, the column read is a derived column, so the row-level report names its columns in the form `dq_word_count__dq_input__completion` and carries the derived text in `dq_input__prompt` and `dq_input__completion`. The following row of the example job passed every criterion, shown with two of its five criterion entries, one decided by code and one by a model:

```json
{
 "ticket_id": "T10005",
 "prompt": "Can I share the annual plan with a colleague?",
 "completion": "Yes. Go to Members, choose Invite, and enter their email. They get an invitation that stays valid for seven days.",
 "category": "feature",
 "dq_input__prompt": "Can I share the annual plan with a colleague?",
 "dq_input__completion": "Yes. Go to Members, choose Invite, and enter their email. They get an invitation that stays valid for seven days.",
 "dq_word_count__dq_input__prompt": 9,
 "dq_word_count__dq_input__completion": 20,
...
 "dq_spec_eval_pass": true,
 "dq_spec_eval_failed_criteria": [],
 "dq_spec_eval_errored_criteria": [],
 "dq_spec_eval_criteria": {
  "answers_the_question": {
   "verdict": true,
   "value": null,
   "reason": "The completion directly explains how to share the plan by inviting a colleague, which answers the question asked.",
   "confidence": 0.9,
   "source": "llm",
   "error_type": null
  },
  "completion_min_length": {
   "verdict": true,
   "value": null,
   "reason": "completion has 20 word(s), threshold is 8",
   "confidence": 1.0,
   "source": "code",
   "error_type": null
  },
...
 }
}
```

### Reading the results for a decision
<a name="ai-data-preparation-dq-results-decision"></a>
+ The `spec_eval` entry of `aggregate/quality_report.json` gives the counts of rows judged, passed, and failed, and the `pass_rate` and `top_failure_modes` of each criterion tell you which criterion the dataset fails most often and why. The criteria over the whole dataset are under `aggregate_criteria`, each with its value and its verdict.
+ The entries of the built-in metrics tell you whether the rows have the length and the variety that you expect.
+ The exploratory findings name problems that your data quality specification does not cover. A finding that matters becomes a criterion in your specification or a filter in data transformation.
+ The rows to act on are in `record_level/evaluated_data.jsonl`, filtered on the `dq_` columns, such as every row where `dq_spec_eval_pass` is `false`.

## Limits and quotas
<a name="ai-data-preparation-dq-limits"></a>

The following limits apply to data quality evaluation.


| Limit | Value | 
| --- | --- | 
| Concurrent DQ jobs per account in each Region | 3. Every job of the account counts, from any entry point. When three jobs run, a new CreateJob call fails with ResourceLimitExceeded. You can request an increase to the Maximum number of concurrent data quality evaluation jobs quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas). | 
| Datasets per job | 1 | 
| Input dataset size | 18 GB in total for a job that runs exploratory\_analysis, 30 GB for a job that runs spec\_eval, and 90 GB for every other job. A job with several operations takes the smallest of their limits. A larger dataset fails the job. | 
| Operations per job | 1 to 50. default\_metrics, spec\_eval, data-validation, and exploratory\_analysis at most once each. | 
| Rows that spec\_eval judges | Every row, or DownSampleRecordCount rows, a positive integer. | 
| Context documents for spec\_eval | At most 1,000 files, each at most 10 MiB and 200 MiB in total, with the extensions .txt, .md, .html, .htm, .json, .jsonl, .ndjson, .csv, .tsv, .pdf, and .docx. | 
| Rows for taxonomy | At least 10, none longer than 49,000 characters. | 
| Job duration | 24 hours | 
| Evaluation entries per dataset | The newest 100 | 
| Regions | See [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md). | 

See [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md) for the Regions and the quotas that apply to every capability. For SageMaker AI quotas, see [SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *AWS General Reference*.

## Troubleshooting
<a name="ai-data-preparation-dq-troubleshoot"></a>

A problem appears in one of three places:
+ The `CreateJob` call refuses the request, and no job exists.
+ You create the job, and it later reports the `JobStatus` `Failed` with a `FailureReason`.
+ A call on an existing job is refused.

A malformed request returns `ValidationException` with a text that names the field at fault and what the service accepts there. Fix the request as the text says and submit it again. A `ThrottlingException` with the text `Rate exceeded` means that too many `CreateJob` calls arrived from one account in a short time, so retry with exponential backoff and submit jobs one at a time. An `AccessDeniedException` that names `sagemaker:ImportHubContent` means that the caller lacks the hub permissions that [Permissions and billing](#ai-data-preparation-dq-use-permissions) lists for the identity that submits the job. A `DescribeJob` or `StopJob` call within a few seconds of `CreateJob` can return `ResourceNotFound` before the job becomes readable, so retry it for a few seconds. The Amazon SageMaker Python SDK raises the same texts, and with `wait=True` it raises `DataPreparerJobFailedError` with the text `Job <arn> failed: <FailureReason>` when the job fails. The following entries cover the cases whose text does not say what to do, and the files that a failed job writes.

### `ClientError` during `Validating` or `Preparing`
<a name="ai-data-preparation-dq-troubleshoot-client-error"></a>

The job fails after `Validating` or `Preparing` with a `FailureReason` that starts with `ClientError:` and says what is wrong and what to do. A job that fails here writes nothing to its output folder. Two causes need more than the text gives:
+ The service could not assume the execution role because its trust policy does not allow `sagemaker.amazonaws.com` to assume it, which a role that trusts only `job.sagemaker.amazonaws.com` fails on.
+ The dataset is larger than the size limit for the job's evaluations.

To resolve the failure:

1. Fix the cause that the text names.

1. Submit the job again.

### The dataset has an older document schema
<a name="ai-data-preparation-dq-troubleshoot-schema"></a>

The job reports `Failed` after it starts, with a `FailureReason` that names the dataset ARN, the dataset's document schema version, and the version that the job requires. To resolve the failure:

1. Register the data as a dataset with `DataSet.create`, which writes a document that meets the requirement.

1. Submit the job again on that dataset.

### `ClientError` that points to CloudWatch Logs
<a name="ai-data-preparation-dq-troubleshoot-client-error-logs"></a>

The job reports `Failed`. The following `FailureReason` message shows this error:

```
ClientError: The job failed due to invalid input or configuration. Verify your request parameters and input data.. Check CloudWatch Logs: log-group=/aws/sagemaker/Job/DataQualityEvaluation/, stream={{job-name}}/evaluation-{{created-at}}
```

The text is the same for every input that the job could not read or evaluate. To resolve the failure:

1. Find the cause. For a `spec_eval` job that was given context documents, open `spec_eval/context_documents.json` in the output folder, whose `failure` entry names the document at fault and what to change. For every other cause, open the CloudWatch Logs stream that the text names.

1. Fix the cause. The following table lists the causes recorded in the log, each with its fix.

1. Submit the job again.


| Cause | Fix | 
| --- | --- | 
| A dataset without default columns (Nova\_RLVR, or Custom without prompt and completion columns) was evaluated without a View. | Add a View to every operation. | 
| A line of the file is not a JSON object. | Repair the line. | 
| A SQLite file holds more than one table. | Keep one. | 
| The file's extension is not one that the job reads. | Rename the file with the extension of its format. | 
| The data quality specification produced no verdict for any row. | Revise it. | 

If an operator fails, the job ends, with the following outcomes:
+ The results of the operations that finished before that operator stay in the output folder.
+ The job writes no entry to the dataset.

A failed job might have no `metadata.json`, so list the output location to find its files.

### The job fails after it wrote every output file
<a name="ai-data-preparation-dq-troubleshoot-after-output"></a>

The output files are all in the output folder, but the job could not add its entry to the dataset's registry entry, and with `wait=True` the SDK logs `Compute succeeded but Hub finalization did not.` To resolve the failure:

1. Give the execution role `sagemaker:ImportHubContent` and `sagemaker:UpdateHubContent` permissions on the dataset's hub content and on its hub.

1. Submit the job again.

The failed job has no `MetadataS3Uri`, so list the `S3OutputPath` prefix for a key that contains the job name to find its files.

### Where the job's log is
<a name="ai-data-preparation-dq-troubleshoot-log-location"></a>

The job's log lines are in your account in CloudWatch Logs, in the log group `/aws/sagemaker/Job/DataQualityEvaluation/` and the stream `{{job-name}}/evaluation-{{created-at}}`. The `DescribeJob` response gives both names in the status message of the `Executing` transition, and every `FailureReason` written after that point repeats them. With `evaluate(..., logs=True)`, the SDK prints the stream while the job runs.

## Where you go next
<a name="ai-data-preparation-dq-next"></a>

You pass the same dataset ARN to the next step, because the job never creates a new dataset or a new version. The results lead to one of two steps:
+ [Data transformation](ai-data-preparation-dt.md) reads the `dq_` columns of the row-level report and drops, filters, or modifies rows on them, such as the rows where `dq_spec_eval_pass` is `false` or `dq_pii_status__<column>` is `pii_found`.
+ [Synthetic data generation](ai-data-preparation-sdg.md) is the next step when you generated the dataset: update the generation specification with what the findings showed and generate a new version of the dataset.

When you evaluate again, pass the job's `spec_eval/` folder as `CodeArtifactS3Uri` to the next job on the new dataset or version, and the same checks run again.

## Related information
<a name="ai-data-preparation-dq-related"></a>

The following pages of this guide describe the steps and the concepts around data quality evaluation:
+ [Preparing Data with SageMaker AI Data Preparation](ai-data-preparation.md) introduces the data preparation jobs and the hub that holds your datasets.
+ [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets) explains the dataset ARN, the row shape of each dataset format, and the registry entry to which this job adds its result.
+ [Get started with SageMaker AI Data Preparation](ai-data-preparation-getting-started.md) and [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup) describe the execution role, the default Amazon S3 bucket, and the permissions that the caller needs.
+ [How a data quality specification works](#ai-data-preparation-dq-spec-write) describes the data quality specification you write for a data quality evaluation job.
+ [Synthetic data generation](ai-data-preparation-sdg.md) is the step that produces a dataset that you evaluate here.
+ [Data transformation](ai-data-preparation-dt.md) is the step that drops, filters, or modifies the rows that this job flagged.
+ [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md) lists the Regions and the quotas that apply to every capability.

The following references document the SDK and the API:
+ The Amazon SageMaker Python SDK reference for the data preparation module, `sagemaker.ai_registry`, documents `DataPreparer`, `DatasetJobConfig`, and `JobCategory`.
+ The Amazon SageMaker AI API Reference documents `CreateJob`, `DescribeJob`, `ListJobs`, `StopJob`, and `DeleteJob`, and the schema discovery operations `ListJobSchemaVersions` and `DescribeJobSchemaVersion`.

The following guides explain the tools that this page uses:
+ The [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/) explains how to install the toolkit and its AI and ML skill, named under Use data quality evaluation.
+ The [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) explains how to read the job log.