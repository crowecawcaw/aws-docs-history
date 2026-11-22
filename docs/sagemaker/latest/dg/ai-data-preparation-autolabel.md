

# Auto-labeling

## What it is
<a name="ai-data-preparation-autolabel-overview"></a>

With auto-labeling, you describe how to label your data in a labeling specification, and SageMaker AI labels every row of an unlabeled dataset with Amazon Bedrock models. For each row, the job also measures how confident it is in the label. When you give it rows that people already labeled, it measures the labels' accuracy and certifies the rows that it accepts. The accepted rows meet an accuracy target that you set, at 95% confidence. The job sends the rows that miss the bar to a separate review dataset for people to label.

Auto-labeling supports the following tasks:


| Task | Type | What each row gets | 
| --- | --- | --- | 
| Classification | labeling.classification | One label from the label set in your specification | 
| Named entity recognition | labeling.ner | Every entity span in the text, with its type | 
| Extractive question answering | labeling.qa | The answer, copied from the passage | 
| Ordinal scoring | labeling.ordinal | A score on the scale that your specification states | 
| LLM-as-a-judge | labeling.llm\_judge | A score against the rubric in your specification | 
| Summarization | labeling.summarization | A summary of the text, graded by other models | 

Use auto-labeling when:
+ You have unlabeled data, such as support tickets, reviews, or documents, and need labels to fine-tune or evaluate a model.
+ You can't afford to label every row by hand, but you need to know how accurate the labels are.
+ You want people to label only the rows that the models are unsure about.

## How it works
<a name="ai-data-preparation-autolabel-how"></a>

An auto-labeling job is a synthetic data generation (SDG) job in labeling mode. Instead of generating new records, it labels the rows of your input data. You start it the same way as an SDG job, with `generate()` and a `generation_config`, and you add `dataset_options` to say which task to run. The job works with the following:

Labeling specification  
A Markdown (`.md`) or text (`.txt`) file that describes the task: the use case, the labels and what each one means, and rules for the cases that are easy to confuse. The job sends the specification to the labeling models with each row, so it's the main way that you control label quality. For how to structure one, see [Write a labeling specification](#ai-data-preparation-autolabel-spec-write).

Input data  
The unlabeled rows, as a JSON Lines file in Amazon S3. Each row is a JSON object. You name the fields that the models read, such as `subject` and `body`, in `text_fields`. Give each row an `id`. The job uses it to join gold rows, predictions, and review answers back to the row.

Evaluation data (optional)  
Rows that people already labeled, called *gold* rows. A gold row either has the same `id` as an input row, or carries every field in `text_fields`. In the second case, the job labels it on its own. The job labels these rows like any other row, and then compares its labels with the gold labels to measure accuracy. The models never see the gold labels. Without evaluation data, the job can't measure accuracy, so a corpus run labels at a fixed confidence bar and certifies nothing.

Labeling models  
The Amazon Bedrock models that you list in `ModelConfig.SampleGenerationModelConfigs`. How the job measures confidence depends on the task. The following table shows the confidence and the number of models for each task.  


<table>
<thead>
  <tr><th>Task</th><th>Confidence</th><th>Models</th></tr>
</thead>
<tbody>
  <tr><td>Classification, named entity recognition, question answering</td><td>The share of models that agree on the label</td><td>2 or more, so that the models can vote</td></tr>
  <tr><td>Ordinal scoring, LLM-as-a-judge</td><td>How closely 5 samples from one model agree</td><td>1</td></tr>
  <tr><td>Summarization</td><td>No confidence for each row. Grader models score a sample of the summaries.</td><td>1 model labels each row, plus 1–3 graders</td></tr>
</tbody>
</table>

The voting and resampling run only on a run with routing, called a *corpus run*. Without routing, the first model labels each row alone.

Output datasets  
Each completed job registers the labeled rows as hub content of type `DataSet` in a hub in your account. A corpus run also registers a second `DataSet` that holds the rows to review. For more information about datasets, see [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets).

### How the job decides which labels to keep
<a name="ai-data-preparation-autolabel-how-certify"></a>

On a corpus run with evaluation data and an accuracy target, the job does the following for the tasks that it can certify: classification, named entity recognition, and question answering.

1. **Labels every row and scores each label.** Each row gets a label and a confidence from 0 to 1.

1. **Measures accuracy on the gold rows.** The job compares its labels on the gold rows with the people's labels.

1. **Picks the confidence cutoff.** The job searches for the lowest cutoff whose accepted gold rows still meet your target at 95% confidence. This way, it accepts as many rows as possible. A row is accepted only if its confidence is at or above the cutoff and at least 75% of the models agree on its label.

1. **Certifies or routes.** If a cutoff meets the target, the job accepts the rows at or above it and certifies them. It also draws a random *spot-check* sample from the accepted rows for people to confirm. For example, at a 0.90 target it draws 29 rows. Every other row goes to the review dataset. If no cutoff meets the target, the job accepts nothing and routes every row.

A certificate needs at least 50 scored gold rows, and they must be a random sample of the same data as the input rows. A corpus run of a certifiable task that can't certify, because it has no evaluation data or no target, accepts rows at a fixed confidence bar of 0.85. With a target but no evaluation data, it still draws a spot-check sample sized for your target. With evaluation data but no target, the sample is sized for 0.90. With neither, it draws no spot-check.

Ordinal scoring, LLM-as-a-judge, and summarization have no single correct answer to certify against. For ordinal scoring and LLM-as-a-judge, the job reports the measured score. It accepts rows at the fixed 0.85 bar and routes the rest. Summarization has no confidence for each row, so a summarization corpus run routes every summary, and the graders' scores are its quality measure.

On a corpus run, a row that is also a gold row ships with the person's label, not the model's.

### Labeling workflow
<a name="ai-data-preparation-autolabel-how-workflow"></a>

Most auto-labeling work follows this loop:

1. **Split your gold rows** – Split the rows that people labeled into development (dev), validation (val), and test sets, and keep the split fixed. Use dev to find mistakes, val to compare specification versions, and test only for the corpus run's certificate.

1. **Trial run** – Label the dev and val rows without routing, with each set as both the input and the evaluation data. Read the accuracy and the rows that the job got wrong.

1. **Refine the specification** – Add rules for the mistakes that you see on dev, and run the trial again. Keep the version with the best accuracy on val.

1. **Corpus run** – Label the full dataset with routing, an accuracy target, and the test rows as evaluation data.

1. **Review the routed rows** – Have people label the review dataset, including the spot-check rows. For instructions, see [Human-in-the-loop annotation](ai-data-preparation-hil.md).

### Start without labeled rows
<a name="ai-data-preparation-autolabel-how-coldstart"></a>

If you don't have rows that people labeled, start with a cold start. People label a random sample of your data first, and that sample becomes your gold rows:

1. Draw a random sample of about 200 rows from the input data. For a target of 0.95 or higher, draw 400 rows instead. Keep only the `id` and the text fields, so that the people who label the sample see no model label. Use a random split, not a stratified one. The certificate assumes that the test rows are a random sample of your data.

1. Have people label the sample. For instructions on labeling the sample, see [Human-in-the-loop annotation](ai-data-preparation-hil.md).

1. Split the labeled sample into dev, val, and test sets at random, and then follow the labeling workflow.

If your whole dataset is about the size of the sample, have people label all of it instead; you don't need a labeling job. A corpus run with no evaluation data at all still runs: it accepts rows at the fixed 0.85 bar, certifies nothing, and draws a spot-check only if you set a target.

## Write a labeling specification
<a name="ai-data-preparation-autolabel-spec-write"></a>

The job sends your specification to the labeling models before each row, so write it for a model that has never seen your data. Organize it into the following sections:


| Section | What it describes | 
| --- | --- | 
| Use Case Context | The task, who uses the labels, and how. | 
| Quality Standards | What a good label looks like, such as an accuracy goal and how to handle a row that fits more than one label. | 
| Input Data | The fields of each row and what they contain. | 
| Labelling Configuration | For classification and named entity recognition, the Label Set: every label or entity type, each with a one-line definition. For ordinal scoring and LLM-as-a-judge, Score Levels instead: one entry for each score, with what earns it. Then Labelling Rules: the deciding signal for each label, and how to choose between labels that are easy to confuse. | 
| Output Schema | The reply that the job asks for, which you restate. For example, {"reasoning": "...", "label": "..."} for classification. | 

Keep the following in mind:
+ **Make labels mutually exclusive.** If two labels can both apply to one row, the models disagree on it and the row is routed. Merge or redefine the labels, or add a rule that says which one wins.
+ **Spell labels exactly.** The job accepts a label only if it matches a name in the label set.
+ **State the scale for a numeric task.** For ordinal scoring and LLM-as-a-judge, add a line such as `Scale: 1 to 5`. A corpus run of these tasks fails if the specification states no scale.
+ **Put examples only from your dev rows in the specification.** The models read the specification with every row, so a val or test row in it inflates the accuracy that the job measures.
+ **Don't refer to the gold label field.** The gold labels are for scoring only. The models never see them.

### Example: classification
<a name="ai-data-preparation-autolabel-spec-write-example"></a>

The following specification, shortened, labels customer support messages by intent:

```
# Customer Support Intent Classification

## Use Case Context
Classify incoming customer support messages by intent so that they can be
routed to the right team. The labels are used to fine-tune a classification
model for real-time ticket routing.

## Quality Standards
- Label accuracy of 90% or higher on held-out data
- Messages with more than one intent are labeled by their primary intent

## Input Data
- message: the text of the support message

## Labelling Configuration
### Label Set
| Label | Definition |
|---|---|
| billing | Charges, invoices, payment methods, refunds, or pricing plans |
| technical_issue | Bugs, errors, outages, or unexpected behavior |
| account_management | Account settings, users, permissions, or subscriptions |
| feature_request | Suggestions for new features or improvements |
| general_inquiry | Questions that don't fit the other labels |

### Labelling Rules
- billing vs account_management: changing a plan tier that changes the
  price is billing; changing who has access, with no cost mentioned, is
  account_management.
- feature_request vs technical_issue: if the feature doesn't exist yet, it's
  feature_request; if it used to work or should work but is broken, it's
  technical_issue.

## Output Schema
{"reasoning": "<one short sentence explaining the label choice>",
 "label": "<one of the labels in the Label Set>"}
```

For this specification, an input row and its labeled row look like the following. The labeled row is shortened: the job also writes fields such as `source` and `provenance`, and on a corpus run the models' votes.

```
{"id": "t-1042", "message": "I was charged twice for my March invoice."}
{"id": "t-1042", "message": "I was charged twice for my March invoice.",
 "label": "billing", "reasoning": "The customer reports a duplicate charge.",
 "confidence": 1.0, "confidence_score": 1.0, "accepted": true, "routed": false}
```

## Inputs
<a name="ai-data-preparation-autolabel-inputs"></a>

The rows that you label usually come from the step before this one, [Data transformation](ai-data-preparation-dt.md), which you use to deduplicate and filter the data, and to split your gold rows into dev, val, and test sets. You can also bring your own JSON Lines file from Amazon S3.

An auto-labeling job takes the same `generation_config` as an SDG job, plus the task options in `dataset_options`. The following snippets show only those parts of the job configuration. In the snippets on this page, replace {{amzn-s3-demo-bucket}} with the name of your Amazon S3 bucket. For a complete example, see [Use auto-labeling](#ai-data-preparation-autolabel-use).

Input data, specification, and models  
Set `InputDataS3Uri` to the JSON Lines file of rows to label, `SpecS3Uri` to your labeling specification, and `SampleGenerationModelConfigs` to the labeling models. Leave out `NumSamples`: the job labels every row in the input. If you set it, it must equal the number of input rows.  

```python
generation_config={
    "InputDataS3Uri": "s3://{{amzn-s3-demo-bucket}}/labeling/tickets.jsonl",
    "DatasetSpecification": {
        "SpecS3Uri": "s3://{{amzn-s3-demo-bucket}}/labeling/label-spec.md",
    },
    "ModelConfig": {
        "SampleGenerationModelConfigs": [
            {"ModelId": "us.anthropic.claude-sonnet-4-5-20250929-v1:0"},
            {"ModelId": "openai.gpt-oss-120b-1:0"},
        ]
    },
}
```

Task options  
Pass a task class, such as `ClassificationLabelingOptions`, as `dataset_options`. Every task takes the following:  
+ `text_fields` – The input fields that the models read. Each name must be a field of the input rows, and can't be a field that the job writes, such as `label`, `confidence`, or `split`.
+ `demos` (optional) – A `Demos` object whose `s3_uri` points to a JSON Lines file of up to 100 labeled example rows that the job adds to every prompt, for example `demos=Demos(s3_uri="s3://{{amzn-s3-demo-bucket}}/labeling/demos.jsonl")`. Draw them from your dev rows, never from the evaluation data. A demo that is also an evaluation row fails the job.
+ `routing` (optional) – Runs the job as a corpus run. `review_dataset_name` names the review dataset, and must differ from the labeled dataset's name.
Every task except summarization also takes the following:  
+ `evaluation_data` (optional) – The gold rows, as an Amazon S3 JSON Lines file (`s3_uri`) or a dataset ARN (`dataset_arn`). `label_field` names the field that holds each gold label.
+ `scoring` (optional) – `target` is the accuracy to certify on the accepted rows, from 0.85 to 0.99.

```python
from sagemaker.ai_registry import (
    ClassificationLabelingOptions, EvaluationData, Routing, Scoring)

dataset_options=ClassificationLabelingOptions(
    text_fields=["message"],
    evaluation_data=EvaluationData(
        s3_uri="s3://{{amzn-s3-demo-bucket}}/labeling/splits/test.jsonl",
        label_field="gt_label",
    ),
    scoring=Scoring(target=0.90),
    routing=Routing(review_dataset_name="support-tickets-review"),
)
```
Summarization takes `graders` instead of evaluation data and a target: 1–3 models that score a sample of up to 100 summaries, each against its own source text. A grader can't be the labeling model.  

```python
from sagemaker.ai_registry import Grader, SummarizationLabelingOptions

dataset_options=SummarizationLabelingOptions(
    text_fields=["article"],
    graders=[Grader(model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0")],
)
```

**Tip**  
**Prepare the gold rows first.** People, not a model, must label the gold rows. For a certificate, the gold rows must be a random sample of the rows that you label. If you have no gold rows yet, see [Start without labeled rows](#ai-data-preparation-autolabel-how-coldstart).

## Use auto-labeling
<a name="ai-data-preparation-autolabel-use"></a>

You can run auto-labeling in the Amazon SageMaker Python SDK directly, or through a coding assistant directed by the core AI and ML skill in the Agent Toolkit for AWS. Both run the same job and produce the same datasets.

------
#### [ Amazon SageMaker Python SDK ]

The following example runs a trial on the dev rows to find the labeling mistakes, and then labels the full dataset with a certificate and a review dataset. It assumes that you've configured an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup), and that you've split your gold rows into `splits/dev.jsonl`, `splits/val.jsonl`, and `splits/test.jsonl`. Before you run it, upload your specification and data to Amazon S3, for example:

```bash
aws s3 cp label-spec.md s3://{{amzn-s3-demo-bucket}}/labeling/label-spec.md
aws s3 cp tickets.jsonl s3://{{amzn-s3-demo-bucket}}/labeling/tickets.jsonl
aws s3 cp splits/ s3://{{amzn-s3-demo-bucket}}/labeling/splits/ --recursive
```

Then run the following Python code:

```python
from sagemaker.core.helper.session_helper import Session
from sagemaker.ai_registry import (
    ClassificationLabelingOptions,
    DataPreparer,
    DatasetJobConfig,
    EvaluationData,
    LabelingSummary,
    Routing,
    Scoring,
)

session = Session()
preparer = DataPreparer(sagemaker_session=session)

bucket = "s3://{{amzn-s3-demo-bucket}}/labeling"
spec = {"SpecS3Uri": f"{bucket}/label-spec.md"}
models = [
    {"ModelId": "us.anthropic.claude-sonnet-4-5-20250929-v1:0"},
    {"ModelId": "openai.gpt-oss-120b-1:0"},
]

# 1. Trial run: label the dev rows and score them against their gold labels.
trial = preparer.generate(DatasetJobConfig(
    dataset_name="support-tickets-dev-trial",
    generation_config={
        "InputDataS3Uri": f"{bucket}/splits/dev.jsonl",
        "DatasetSpecification": spec,
        "ModelConfig": {"SampleGenerationModelConfigs": models[:1]},
    },
    dataset_options=ClassificationLabelingOptions(
        text_fields=["message"],
        evaluation_data=EvaluationData(
            s3_uri=f"{bucket}/splits/dev.jsonl", label_field="gt_label"),
    ),
))
summary = LabelingSummary.from_dataset(trial.arn)
print(summary.held_out_accuracy, summary.artifacts["Failures"])
#    Read the dev rows the job got wrong, refine label-spec.md, upload it, and
#    rerun step 1. Then run the same trial on splits/val.jsonl for each
#    candidate spec, and keep the one with the best accuracy on val.

# 2. Corpus run: label every row, certify the accepted rows, route the rest.
job = preparer.generate(DatasetJobConfig(
    dataset_name="support-tickets-labeled",
    generation_config={
        "InputDataS3Uri": f"{bucket}/tickets.jsonl",
        "DatasetSpecification": spec,
        "ModelConfig": {"SampleGenerationModelConfigs": models},
    },
    dataset_options=ClassificationLabelingOptions(
        text_fields=["message"],
        evaluation_data=EvaluationData(
            s3_uri=f"{bucket}/splits/test.jsonl", label_field="gt_label"),
        scoring=Scoring(target=0.90),
        routing=Routing(review_dataset_name="support-tickets-review"),
    ),
), wait=False)

# 3. Wait for the job, and read the certificate.
job.wait()
summary = job.labeling_summary
print(summary.status, summary.status_reason)
print(summary.rows_accepted, summary.rows_routed, summary.accepted_lower_bound95)
print(summary.review_dataset_arn)
```

In this example, set the following values for your job:
+ `dataset_name` – A name for the labeled dataset. It must be 1–63 characters of letters, numbers, and hyphens, and must start and end with a letter or number.
+ `InputDataS3Uri` – The Amazon S3 location of the rows to label.
+ `SpecS3Uri` – The Amazon S3 location of your labeling specification.
+ `text_fields` – The fields of each row that the models read.
+ `label_field` – The field of each gold row that holds the person's label.
+ `target` – The accuracy to certify, from 0.85 to 0.99.
+ `review_dataset_name` – A name for the review dataset.

The example works as follows:
+ Step 1 runs without routing, so one model labels each row and nothing is certified. It writes the gold rows that the job got wrong to `failures.jsonl`, which is what you read to refine the specification. The trial uses the dev rows as both the input and the evaluation data, so it measures accuracy on every row that it labels. Use the val rows only to compare specification versions, so that the val accuracy stays an honest measure.
+ Step 2 sets routing, so the job votes with both models, picks the cutoff on the test rows, and registers the review dataset. A corpus run can take much longer than a trial, so it passes `wait=False` and gets a job handle back. Step 3 waits for the job. If your session ends, run `DataPreparer.attach("{{job-arn}}", wait=False)` to get the handle again.
+ `labeling_summary` and `LabelingSummary.from_dataset()` read the job's summary report. `status` is `Certified`, `NotCertified`, or `Partial`, and `status_reason` says why. For the full list, see [Results](#ai-data-preparation-autolabel-results).

------
#### [ Coding assistant with the AI and ML skill ]

With a coding assistant, you can run auto-labeling through a guided conversation, directed by the core AI and ML skill (`aws-ai-ml`) in the Agent Toolkit for AWS. To install it, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/). As with the SDK, you need an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup). Start with a prompt that describes your data and what you want labeled, for example:

```
I have 20,000 support tickets in s3://{{amzn-s3-demo-bucket}}/labeling/tickets.jsonl
and 300 that my team labeled by intent. Label the rest with at least 90% accuracy.
```

The agent then works through the same steps as the SDK example, and asks for your approval before each job:

1. Checks the input fields and the label set, and drafts a labeling specification with you, if you don't already have one.

1. Splits your labeled rows into dev, val, and test sets, and keeps the split fixed. If you have no labeled rows, it draws a random sample for people to label first.

1. Runs trials on dev and val, shows you the mistakes, and refines the specification with you.

1. Runs the corpus job, and explains the certificate and the rows that it routed.

1. Hands the review dataset to human-in-the-loop annotation, and applies the people's labels to the labeled dataset when they're done.

1. Writes a report of the run, and saves the work as a notebook or script that you can rerun.

------

**Tip**  
**Plan for run time and cost.** Each row is at least one model call, and a corpus run of a voting task makes one call for each model. Ordinal scoring and LLM-as-a-judge sample one model 5 times for each row. Run trials on your dev and val rows, which are small, before you label the full dataset.

## Results
<a name="ai-data-preparation-autolabel-results"></a>

When a job finishes, `generate()` returns the labeled `DataSet`. Its `source` is the job's `output/` prefix in Amazon S3. The job writes the following files under its output root, one level above `source`:


| File | Contents | 
| --- | --- | 
| output/labels.jsonl | Every input row with its label, reasoning, and confidence, and whether it was accepted or routed. A row that is a gold row carries the person's label. | 
| review/review\_rows.jsonl | Corpus runs only. The rows to review: the routed rows, and the spot-check rows drawn from the accepted rows. Each row holds its id, its text fields, a split of low\_confidence or spot\_check, and a \_review\_reason that says why it's in the review set, but not the model's label, so that reviewers label it without bias. This file is the review dataset. | 
| labeling/labeling\_summary.json | The job's summary: its status, row counts, measured accuracy, cutoff, and certificate. LabelingSummary reads this file. | 
| labeling/held\_out\_report.json | Details of the accuracy on the gold rows, such as the score for each class and the labels that the job confused with each other. | 
| labeling/failures.jsonl | Every gold row that the job got wrong, with the gold label and the prediction, plus 2 that it got right for each gold label. For summarization, the summaries that the graders scored low. Use these to refine the specification. | 
| labeling/review\_rows.model\_output.jsonl | Corpus runs only. The model's answers for the review rows, kept apart so that reviewers don't see them. | 
| labeling/spec.md | The specification that produced the labels. | 
| labeling/report.html | A summary of the job that you can open in a browser. | 
| labeling/index.json | The Amazon S3 location of each file in this table. | 

The summary's `Status` and `StatusReason` tell you what the job promises about its labels:


| Status | StatusReason | What it means | 
| --- | --- | --- | 
| Certified | spot\_check\_pending | The accepted rows meet your target. The promise holds once people confirm the spot-check rows. If 7 or more of them are wrong, withdraw the certificate. | 
| NotCertified | target\_not\_met | No cutoff met the target. The job accepted nothing and routed every row except the gold rows. The gold rows keep the person's label. Refine the labeling specification, or lower the accuracy target. | 
| NotCertified | insufficient\_eval\_rows | The evaluation data had fewer than 50 gold rows to score, so the job accepted nothing and routed every row except the gold rows, which keep the person's label. Add more gold rows. | 
| NotCertified | no\_eval\_data, no\_target | The job had no evaluation data or no target, so it accepted rows at the fixed 0.85 bar. | 
| NotCertified | task\_not\_certifiable | The task is ordinal scoring, LLM-as-a-judge, or summarization, which the job scores but doesn't certify. | 
| NotCertified | refine\_round | The job ran without routing, as a trial. | 
| Partial | Any of the reasons in this table | The job couldn't label some rows. Those rows are counted in RowsMissing, and on a corpus run they're routed. | 

## Limits and quotas
<a name="ai-data-preparation-autolabel-limits"></a>

The following limits apply to auto-labeling. An auto-labeling job is an SDG job, so it also counts toward the SDG quotas, such as the number of concurrent jobs. For more information about those quotas, see [Limits and quotas](ai-data-preparation-sdg.md#ai-data-preparation-sdg-limits).


| Limit | Value | 
| --- | --- | 
| Rows per job | 50,000, counting the input rows and any gold rows that aren't input rows | 
| Input data format | JSON Lines | 
| Evaluation data format | JSON Lines, or a JSON array | 
| Labeling specification size | 64 KB | 
| Demo rows | 100 rows, 64 KB | 
| Accuracy target (Scoring.Target) | 0.85–0.99 | 
| Scored gold rows needed for a certificate | 50 | 
| Labeling models on a corpus run | 2 or more for classification, named entity recognition, and question answering. 1 for ordinal scoring and LLM-as-a-judge. | 
| Graders for summarization | 1–3 | 

For more information about supported Regions and the quotas that apply to every capability, see [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md).

Auto-labeling jobs invoke Amazon Bedrock models for every row, so the on-demand quotas for those models, such as tokens per minute and requests per minute, can limit how fast a job runs. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) in the *Amazon Bedrock User Guide*.

## Troubleshooting
<a name="ai-data-preparation-autolabel-troubleshoot"></a>

The job fails before it labels anything  
The job checks its inputs before it calls any model, and the error names the field to fix. Common causes:  
+ A field in `text_fields` is missing from the input rows, is repeated, or has the name of a field that the job writes.
+ The input data is a CSV, Parquet, or other file that isn't JSON Lines, or the evaluation data is neither JSON Lines nor a JSON array.
+ A corpus run of a voting task lists fewer than 2 models, or a corpus run of ordinal scoring or LLM-as-a-judge lists more than 1.
+ An ordinal scoring or LLM-as-a-judge specification states no scale. Add a line such as `Scale: 1 to 5`.
+ A classification or named entity recognition specification has no `Label Set`.
+ `NumSamples` is set and doesn't equal the number of input rows. Leave it out.
+ On a corpus run with a target, some gold rows can't be scored. This leaves fewer than 50 that can. A gold row is scored when its `id` matches an input row's `id`, or when it carries every field in `text_fields`. Fix the gold rows' `id` values, or add their text fields. If every gold row can be scored but there are fewer than 50, the job runs and ends with `insufficient_eval_rows`.
+ Two input rows share an `id`. A row with no `id` takes its position as its `id`.
+ A demo row is also an evaluation row, by `id` or by text.

The job certifies nothing and routes every row  
The status reason is `target_not_met`. Read `failures.jsonl` for the labels that the job confused, add rules for them to the specification, and run a trial on val again. A label set whose labels overlap is the most common cause.

The trial accuracy is high, but the corpus run doesn't certify  
Check that the test rows are a random sample of the input rows. Gold rows chosen because they were easy, or drawn from another source, measure a higher accuracy than the job gets on the full dataset.

Most rows are routed even though accuracy is high  
On a voting task, a row is accepted only when at least 75% of the models agree. Two models that often disagree send many rows to review. Make the label definitions sharper, or choose models that agree more often on your trial.

The job fails with `HUB_FINALIZATION_FAILED`  
SageMaker AI labeled the rows but couldn't register the dataset. The files are still in Amazon S3. Make sure that the execution role has the `sagemaker:ImportHubContent` permission on the hub and on its `DataSet` hub content. For the required permissions, see [Required permissions](ai-data-preparation-getting-started.md#ai-data-preparation-setup-iam).

Your session ends before the job finishes  
The job keeps running. `generate()` logs the job's ARN when it submits the job, and a job handle has it as `job.job_arn`. To reconnect, replace {{job-arn}} with the ARN of your job, and run `job = DataPreparer.attach("{{job-arn}}", wait=False)`. Then run `job.wait()`, and read `job.labeling_summary`.

## Where you go next
<a name="ai-data-preparation-autolabel-next"></a>

The job's output is a labeled dataset, and on a corpus run a review dataset, that you pass by ARN to the next step:
+ [Human-in-the-loop annotation](ai-data-preparation-hil.md) – Have people label the review dataset, including the spot-check rows. Then apply their labels to the labeled dataset by `id`.
+ [Data transformation](ai-data-preparation-dt.md) – Filter the accepted rows, or convert the labeled dataset to a training format.
+ [Model customization](customizing-models.md) – Fine-tune a model with the labeled dataset as training data.

## Related information
<a name="ai-data-preparation-autolabel-related"></a>
+ [Synthetic data generation](ai-data-preparation-sdg.md)
+ [Data transformation](ai-data-preparation-dt.md)
+ [Human-in-the-loop annotation](ai-data-preparation-hil.md)
+ [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets)
+ [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup)
+ [Model customization](customizing-models.md)
+ [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/)