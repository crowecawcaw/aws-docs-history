

# Data transformation

## What it is
<a name="ai-data-preparation-dt-overview"></a>

With data transformation (DT), you apply an operator to a dataset that you already have, and SageMaker AI publishes the result as a dataset in your hub. You can remove duplicate records, filter records by text quality or language, redact or remove personal information, split a dataset into training and test sets, merge two datasets, and convert records between dataset formats. When no operator fits, you can run your own Python code, or describe the change in plain language and have a model write the code.

Before you start, you need an execution role, a default Amazon S3 bucket, and a dataset registered in a hub. For setup steps, see [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup).

Use DT when:
+ Your dataset has duplicate or near-duplicate records.
+ You want to drop low-quality records, or records that aren't in the languages that you train on.
+ Your records contain personal information, such as email addresses or phone numbers, that you need to redact or remove.
+ You need separate training and test sets, or need to combine two datasets.
+ Your records are in one format, such as prompt and completion pairs, and your training job expects another, such as chat messages.

## How it works
<a name="ai-data-preparation-dt-how"></a>

A DT job reads a dataset by its ARN, applies one operator, and publishes the output in your hub. A `CodeGen` preview is the exception: it doesn't publish a dataset. Most operators publish the output as a new version of the input dataset. `Split` and `Merge` publish new datasets. The input dataset version that you pass isn't changed.

A job takes one operator. To apply several, run one job for each operator and pass each job's output ARN to the next job.

A job request has the following parts:

Input datasets  
One dataset, referenced by ARN. `Merge` takes two.

Operation  
One operator name and its configuration. Each operator accepts its own set of configuration keys.

Output location  
An Amazon S3 path where the job writes its output records and a report.

You describe the change in one of three ways:
+ **Built-in operators** – Use these for deduplication, filtering, PII redaction, splitting, merging, and format conversion.
+ **`BYOC` (bring your own code)** – Run a Python function that you write.
+ **`CodeGen`** – Describe the change in a plain-language specification, and a model writes the Python code. You can review the code, and then run it again as a `BYOC` job.

### Operators
<a name="ai-data-preparation-dt-operators"></a>

Each entry shows an example `Operations` item. The operators that read record text take the field name in `TextField`. Set it explicitly. For the deduplication and text quality operators, it defaults to `text`. If your records don't have that field, the operator can remove the wrong records, or the job can fail. `PiiRedaction` takes either `TextField` or `MessagesField`.

`TextQualityFilter`  
Drops records that fail one text quality check. Set `FilterType` to one of `Alphanumeric`, `AverageLineLength`, `CharacterLength`, `CharRepetition`, `Mojibake`, `Urls`, or `WordRepetition`, and then set the thresholds for that check. The following example drops records whose prompt is shorter than 20 characters.  

```python
{"Operator": "TextQualityFilter",
 "Config": {"FilterType": "CharacterLength", "TextField": "prompt", "MinLength": 20}}
```

`ExactDedup`  
Removes records whose text field matches another record's. How it matches depends on the input size:  
+ Inputs smaller than 500 MiB – Text must match exactly. Don't set `Normalize` to `True`. The job fails with an `InternalServerError` reason.
+ Inputs of 500 MiB or more – By default, the match ignores case and extra whitespace. For an exact match, set `Normalize` to `False`.

```python
{"Operator": "ExactDedup", "Config": {"TextField": "prompt"}}
```

`FuzzyDedup`  
Removes near-duplicate records by using MinHash similarity. `JaccardThreshold` sets the approximate similarity, from 0 to 1, at which two records count as near-duplicates. `NgramSize` is measured in words. Records with fewer than 5 words aren't checked for near-duplicates.  

```python
{"Operator": "FuzzyDedup",
 "Config": {"TextField": "prompt", "JaccardThreshold": 0.7, "NumPerm": 128, "NgramSize": 5}}
```

`LanguageFilter`  
Keeps records whose text is in one of the languages that you list, and drops the rest. `TextField` is required and must name a field that holds plain text. The job fails if the field holds a chat messages array. `Languages` takes lowercase language codes, such as `en`. When you set `Languages`, records with empty text are dropped.  

```python
{"Operator": "LanguageFilter", "Config": {"TextField": "text", "Languages": ["en"]}}
```

`PiiRedaction`  
Uses Amazon Bedrock models to find personally identifiable information (PII) in each record, and then keeps, redacts, or drops the records that contain it. Set exactly one of these fields:  
+ `TextField` – A field that holds plain text.
+ `MessagesField` – A field that holds a chat messages array. The operator checks the content of each message.
`PiiRedaction` finds direct identifiers only: information that identifies an individual on its own, such as a name or an account number. It does not find quasi-identifiers: information that identifies an individual only in combination with other information.  
The categories it detects are the following:  
+ Names and contact details – private names, public names, email addresses, and phone numbers.
+ Addresses and locations – full addresses, partial addresses, and GPS coordinates.
+ Government and financial numbers – card numbers, card codes and expiry dates, bank account numbers, PINs, Social Security numbers, driver's license numbers, passport numbers, and other government IDs.
+ Account, device, and network identifiers – IP addresses, MAC addresses, user names, device and tracking IDs, and account and membership numbers.
+ Vehicle identifiers – license plates and vehicle identification numbers.
+ Passwords and credentials – passwords and other credentials.
+ Dates and age – personal dates, such as a date of birth, and age.
+ Web addresses – public URLs and private URLs.
`DefaultAction` sets what happens to a record that contains PII:  
+ `tag` (default) – Keeps the record unchanged. To see what was found, set `EmitEvidence` to `True`.
+ `redact` – Replaces each piece of PII with its entity type in brackets, such as `[EMAIL]` or `[PHONE]`.
+ `drop` – Removes the record.
To handle some entity types differently, set `ActionMap`. Its keys are uppercase entity types, such as `EMAIL`, `PHONE`, `SSN`, `PRIVATE_NAMES`, or `FULL_ADDRESSES`, and its values are actions. Entity types that aren't in the map use `DefaultAction`. A record that contains an entity type mapped to `drop` is removed, even if it also contains other types. The following example redacts email addresses, drops records that contain a phone number, and keeps other records unchanged.  

```python
{"Operator": "PiiRedaction",
 "Config": {"TextField": "text", "ActionMap": {"EMAIL": "redact", "PHONE": "drop"}}}
```
When `DefaultAction` or any `ActionMap` value is `redact` or `drop`, records that the operator can't fully check are removed, even if they contain no PII. For example, these records are removed:  
+ A record whose `TextField` value is longer than 40,000 characters.
+ A chat record with a message field that the operator doesn't check, such as `tool_call_id`.
When `EmitEvidence` is `True`, `report.json` lists each record's outcome, the entity types found, and the start and end character offsets of up to 10 pieces of PII. To identify records in that list by one of their fields, set `RowIdField` to that field's name.  

```python
{"Operator": "PiiRedaction",
 "Config": {"TextField": "text", "EmitEvidence": True, "RowIdField": "id"}}
```
`PiiRedaction` calls Amazon Bedrock models with the execution role's credentials. The role needs permission to invoke them. For size and record limits, see [Limits and quotas](#ai-data-preparation-dt-limits).

`Split`  
Divides one dataset into several, such as training and test sets. `Ratios` is required. It needs at least two entries, and the values must sum to 1.0. Each part is published as its own dataset, named from the job name and the ratio key, for example `{{job-name}}-train`. Ratio keys are converted to lowercase. They can contain only letters, numbers, and hyphens, and must start and end with a letter or number. A key such as `train_set` fails the job.  

```python
{"Operator": "Split", "Config": {"Ratios": {"train": 0.8, "test": 0.2}, "Seed": 42}}
```
`Method` sets how records are assigned to parts:  
+ `random` (default) – Assigns records at random.
+ `stratified` – Keeps the share of each value of `StratifyField` the same in every part. For example, if 60% of the input records have the label `a`, about 60% of each part does too. `StratifyField` is required.
+ `cluster` – Groups records whose text in `TextField` is similar, and then divides each group across the parts by `Ratios`. A small group can end up in only one part. To set the maximum number of groups, set `NumClusters` to an integer of 2 or more. If the dataset is too small for that number, SageMaker AI uses fewer groups. If you leave it out, SageMaker AI chooses the number. To also keep the share of each label about the same, set `StratifyField`.
`TextField` and `NumClusters` are valid only with `cluster`, and `StratifyField` isn't valid with `random`. The following examples split by label and by topic.  

```python
{"Operator": "Split",
 "Config": {"Method": "stratified", "StratifyField": "label", "Ratios": {"train": 0.8, "test": 0.2}}}

{"Operator": "Split",
 "Config": {"Method": "cluster", "TextField": "prompt", "NumClusters": 3, "Ratios": {"train": 0.8, "test": 0.2}}}
```

`Merge`  
Combines two datasets into a new dataset named from the job name, for example `{{job-name}}-merged`. Pass exactly two datasets in `input_data_config`. Leave `Config` empty. Any key fails the job.  

```python
{"Operator": "Merge", "Config": {}}
```

`SchemaConversion`  
Converts records into another dataset format. Set `TargetFormat` to `Bedrock_Converse`, `HF_Prompt_Completion`, or `OpenAI_Messages`. It must differ from the input dataset's format. One input record can produce more than one output record. For example, a multi-turn conversation becomes one prompt and completion pair for each turn.  

```python
{"Operator": "SchemaConversion", "Config": {"TargetFormat": "HF_Prompt_Completion"}}
```

`SchemaFilter`  
Drops records that don't match a dataset format. Use it to clean up a dataset that mixes formats. `ExpectedFormat` takes the same values as `TargetFormat`. If you leave it out, records are checked against the input dataset's format.  

```python
{"Operator": "SchemaFilter", "Config": {"ExpectedFormat": "HF_Prompt_Completion"}}
```

`BYOC`  
Runs a Python module that you upload to Amazon S3. A `BYOC` job takes one input dataset. In the following example, replace {{amzn-s3-demo-bucket}} with your bucket name.  

```python
{"Operator": "BYOC", "Config": {"TransformationCodeS3Uri": "s3://{{amzn-s3-demo-bucket}}/code/transformer.py"}}
```
The module must define a function named `transform_dataset`. The following Python module strips whitespace from each completion.  

```python
import json
import os

def transform_dataset(inputs: dict[str, str], output_dir: str) -> dict:
    input_path = next(iter(inputs.values()))
    output_path = os.path.join(output_dir, "dataset.jsonl")
    total = 0
    with open(input_path) as fin, open(output_path, "w") as fout:
        for line in fin:
            record = json.loads(line)
            record["completion"] = record["completion"].strip()
            fout.write(json.dumps(record) + "\n")
            total += 1
    return {"outputs": ["dataset.jsonl"], "total_records": total,
            "transformed_records": total, "errors": 0}
```
The function works with the following values:  
+ `inputs` – Maps a key based on the input dataset's name to the path of its local file.
+ `output_dir` – The local directory where the function writes its output files, such as `dataset.jsonl`.
+ The returned dictionary – Lists the files that the function wrote in `outputs`, and the record counts in `total_records`, `transformed_records`, and `errors`.
The code runs in a restricted Python environment. It can import `pandas`, `numpy`, and `scipy`, in addition to some standard library modules. Some submodules aren't available, and you can't install other packages. The code can't read attributes whose names start with an underscore, such as `__version__`.

`CodeGen`  
Has a model write the transformation code from a specification, a text or Markdown file that you upload to Amazon S3. In the following example, replace {{amzn-s3-demo-bucket}} with your bucket name.  

```python
{"Operator": "CodeGen",
 "Config": {"SpecificationS3Uri": "s3://{{amzn-s3-demo-bucket}}/specs/transform-spec.md",
            "AutoExecute": True}}
```
With `AutoExecute` set to `True`, the job runs the code on the whole dataset and publishes the output. If you leave `AutoExecute` out, the job runs a preview: it runs the code on a sample of records, writes the results to Amazon S3, and doesn't publish a dataset. To set the preview size, add `"ExecutionConfig": {"SampleSize": {{n}}}` to `transformation_config`, from 1 to 1,000. The default is 10. For how to read a preview, see [Results](#ai-data-preparation-dt-results).  
`CodeGen` calls Amazon Bedrock models through cross-Region inference profiles, with the execution role's credentials. The role needs permission to invoke them. The generated code runs under the same restrictions as `BYOC` code. Specifications that need a model to process each record, such as translating text, can be rejected.

## Inputs
<a name="ai-data-preparation-dt-inputs"></a>

DT reads datasets that are registered in a hub, referenced by ARN in `input_data_config`. Input records can be in JSON Lines or Parquet format. Built-in operators write output records in JSON Lines format. `CodeGen` and `BYOC` jobs write the format that the code produces.

To transform your own data, upload it to Amazon S3 and register it as a dataset with `DataSet.create()`. Pass the dataset's format in `dataset_file_format`, such as `HF_Prompt_Completion`. If you leave the format out, the dataset is registered as `Custom`. `SchemaConversion` and `SchemaFilter` read the format from the dataset. For more information, see [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets).

## Use data transformation
<a name="ai-data-preparation-dt-use"></a>

You can run DT in the Amazon SageMaker Python SDK directly, or through a coding assistant directed by the core AI and ML skill in the Agent Toolkit for AWS.

------
#### [ Amazon SageMaker Python SDK ]

The following example removes exact duplicates from a dataset, and then splits the result into training and test sets. It assumes that you've configured an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup). Replace {{your-dataset-arn}} with the ARN of your dataset, and {{amzn-s3-demo-bucket}} with your bucket name.

```python
from sagemaker.core.helper.session_helper import Session
from sagemaker.ai_registry import DataPreparer, DatasetJobConfig, JobCategory

session = Session()
preparer = DataPreparer(sagemaker_session=session)
input_arn = "{{your-dataset-arn}}"
output_path = "s3://{{amzn-s3-demo-bucket}}/dt-output/"

# 1. Remove exact duplicates.
deduped = preparer.transform(DatasetJobConfig(
    job_category=JobCategory.DATA_TRANSFORMATION,
    input_data_config=[{"DatasetArn": input_arn}],
    output_data_config={"S3OutputPath": output_path},
    transformation_config={
        "Operations": [{"Operator": "ExactDedup", "Config": {"TextField": "prompt"}}],
    },
))
print(deduped[0].arn, deduped[0].source)

# 2. Split the deduplicated dataset into training and test sets.
splits = preparer.transform(DatasetJobConfig(
    job_category=JobCategory.DATA_TRANSFORMATION,
    input_data_config=[{"DatasetArn": deduped[0].arn}],
    output_data_config={"S3OutputPath": output_path},
    transformation_config={
        "Operations": [{
            "Operator": "Split",
            "Config": {"Ratios": {"train": 0.8, "test": 0.2}, "Seed": 42},
        }],
    },
))
for ds in splits:
    print(ds.arn, ds.source)
```

The example works as follows:
+ `transform()` submits the job, waits until it finishes, and returns a list of `DataSet` objects, one for each output. Most operators return a list with one item, so step 1 reads `deduped[0]`. `Split` returns one item for each ratio key. To submit a job and return immediately, pass `wait=False`. `transform()` then returns a `Job` object.
+ Step 2 passes the output ARN of the first job to the second job.
+ The SDK doesn't check operator names or `Config` keys. A misspelled name or key fails the job after you submit it. `transform()` then raises `DataPreparerJobFailedError`.
+ For a `CodeGen` preview, pass `wait=False`. A preview doesn't publish a dataset, so with `wait=True`, `transform()` raises `DataPreparerJobError` after the preview completes.

------
#### [ Coding assistant with the AI and ML skill ]

With a coding assistant, you can build and run a transformation through a guided conversation, directed by the core AI and ML skill (`aws-ai-ml`) in the Agent Toolkit for AWS. To install it, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/). Start with a prompt that describes your data and what you want to change, for example:

```
My training data is a JSON Lines file in S3. Remove the duplicate records,
and then split it 80/20 into training and test sets.
```

The agent works through the following steps, and asks you to confirm before it runs anything:

1. Turns your request into a list of operations, and confirms the list with you.

1. Chooses where to run the transformation. For data in Amazon S3 or in a hub, it runs DT jobs through the Amazon SageMaker Python SDK, unless you ask to run it locally. For a file on your computer, it asks whether to run the transformation there or as DT jobs. It recommends running it locally for files of 50 MB or less. `LanguageFilter` always runs as a DT job.

1. Writes the code as a script that it runs, or as a notebook that you run.

1. Shows you sample records from the output and the record count.

The agent doesn't run datasets larger than 10 GB. A transformation that runs on your computer registers its output as a dataset only if you ask the agent to.

------

## Results
<a name="ai-data-preparation-dt-results"></a>

When a job finishes, `transform()` returns a list of `DataSet` objects. Each object's `source` attribute is the Amazon S3 URI of its output records. Each output is registered in your hub, so you can pass its ARN to another job.

The job writes its files under `{{S3OutputPath}}/data-transformation/{{job-name}}/{{timestamp}}/`. A `Split` job writes each part's records in a subfolder named after its ratio key. The following table lists the main files.


| File | Contents | 
| --- | --- | 
| dataset.jsonl | The output records. When CodeGen code writes another format, such as CSV, the file uses that format's extension, for example dataset.csv. | 
| report.json | A summary of the job, including the number of input and output records for the operation. For a PiiRedaction job with EmitEvidence set to True, it also lists the outcome for each record. | 
| transformer.py | The code that the model wrote. Only CodeGen jobs write this file. | 
| sample\_output.jsonl | The output of the generated code on a sample of the input records. Only CodeGen jobs write this file. For another output format, the file uses that format's extension. | 

A `CodeGen` preview doesn't publish a dataset, so read its files from Amazon S3. The job's description lists where they are. Run `DescribeJob`, and read `TransformationCodeS3Uri` (the location of `transformer.py`) and `TransformationReportS3Uri` from its `JobConfigDocument`. `sample_output.jsonl` is in the same folder.

When the preview looks right, pass the `transformer.py` location as the `TransformationCodeS3Uri` of a `BYOC` job. That job runs the reviewed code on the whole dataset.

## Limits and quotas
<a name="ai-data-preparation-dt-limits"></a>

The following limits apply to DT jobs.


| Limit | Value | 
| --- | --- | 
| Concurrent DT jobs per account in each Region | 3. You can request an increase. | 
| Operations per job | 1 | 
| Input datasets per job | 1. Merge requires 2. | 
| Total input size per job | Less than 10 GiB | 
| Total input size for a PiiRedaction job | Less than 1 GiB | 
| Records in a PiiRedaction input dataset | 10,000 or fewer | 
| Records in a CodeGen preview (SampleSize) | 1–1,000. The default is 10. | 

To run more DT jobs at the same time, request an increase to the **Maximum number of concurrent data transformation jobs** quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home).

For supported Regions and the quotas that apply to every capability, see [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md).

`CodeGen` and `PiiRedaction` jobs call Amazon Bedrock models with your execution role, so the Amazon Bedrock quotas in your account can limit how fast they run. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) in the *Amazon Bedrock User Guide*.

## Troubleshooting
<a name="ai-data-preparation-dt-troubleshoot"></a>

Most configuration errors don't stop `transform()` from submitting the job. The job fails without publishing a dataset, and its `FailureReason` usually starts with `ClientError:` followed by the cause. A few errors return `InternalServerError` instead, as described later in this section. Some failed jobs also write a `report.json` with the failure details. `transform()` raises the reason as a `DataPreparerJobFailedError`.

`CreateJob` fails with "array is too long: must have at most 1 elements"  
`Operations` has more than one operator. Put one operator in each job, and pass each job's output ARN to the next job.

The job fails with "Unknown operator"  
The reason lists the supported operators. Check the spelling and capitalization of the operator name.

The job fails with "Unknown {{operator}} config keys"  
The reason lists the keys that the operator accepts. For example, `FuzzyDedup` accepts `JaccardThreshold`, not `Threshold`.

The job fails with "Merge operator does not accept Config parameters"  
Set `Config` to an empty object.

The job fails with "Merge operator requires at least 2 input datasets"  
Pass two datasets in `input_data_config`.

The job fails with "BYOC mode supports exactly one input dataset" or "Dedup accepts exactly one input"  
Pass one dataset in `input_data_config`. Only `Merge` takes two.

A `Split` job fails with "Invalid output name"  
A key in `Ratios` has a character other than a letter, number, or hyphen, starts or ends with a hyphen, or is too long. Rename the key, for example to `train-set`.

A `Split` job fails because of `Method`, `StratifyField`, `TextField`, or `NumClusters`  
Check these rules:  
+ `Method` is `random`, `stratified`, or `cluster`.
+ `stratified` requires `StratifyField`.
+ `StratifyField` isn't valid with `random`.
+ `TextField` is valid only with `cluster`.
+ `NumClusters` is valid only with `cluster`, and must be an integer of 2 or more.

A `PiiRedaction` job fails with "requires exactly one of Config.MessagesField or Config.TextField"  
Set exactly one field: `TextField` for plain text records or `MessagesField` for chat records.

A `PiiRedaction` job fails because of `ActionMap` or `DefaultAction`  
Use uppercase entity types with no surrounding spaces as `ActionMap` keys, such as `EMAIL`, not `email`. The reason names any entity type that isn't supported. Set `DefaultAction` and each `ActionMap` value to `tag`, `redact`, or `drop`.

A `PiiRedaction` job fails because the input is too large  
The input has more than 10,000 records or is 1 GiB or larger. Divide it into smaller datasets, and run a job on each.

A `LanguageFilter` job fails because of `Languages` or `TextField`  
Use lowercase language codes, such as `en`, and set `TextField` to a field that holds plain text. For chat records, which hold their text in a messages array, the job fails.

A `CodeGen` job fails because the specification needs a model  
`CodeGen` can reject specifications that need a model to process each record, such as translating text. Describe a change that code can make on its own.

The job fails because the output bucket "does not exist or is not accessible"  
Check the bucket name in `S3OutputPath`, and make sure that the execution role can write to it.

The job fails because the bucket is in another Region  
The output bucket must be in the same Region as the job. Use a bucket in that Region.

The job fails with an `InternalServerError` reason  
Check for these causes:  
+ `ExactDedup` – For inputs smaller than 500 MiB, remove `Normalize` from the configuration.
+ `SchemaConversion` – Make sure that `TargetFormat` differs from the input dataset's format.
+ `TextQualityFilter` – Set `TextField` to a field that your records have.

Deduplication removes far more records than expected  
`TextField` defaults to `text`. If your records don't have a `text` field, `ExactDedup` can treat every record as a duplicate and keep only one. Set `TextField` to the field to compare.

`transform()` raises `DataPreparerJobError` after a `CodeGen` job completes  
The job was a preview, which doesn't publish a dataset. Read its output from Amazon S3, as described in [Results](#ai-data-preparation-dt-results). To process the whole dataset, set `AutoExecute` to `True`.

## Where you go next
<a name="ai-data-preparation-dt-next"></a>

Each job's output is a dataset that you pass by ARN to the next step:
+ [Auto-labeling](ai-data-preparation-autolabel.md) – Add labels to the transformed records.
+ [Data quality evaluation](ai-data-preparation-dq.md) – Evaluate the transformed dataset to confirm that the change fixed the problems that you found.
+ [Model customization](customizing-models.md) – Fine-tune a model with the training set, and evaluate it with the test set.

## Related information
<a name="ai-data-preparation-dt-related"></a>
+ [Synthetic data generation](ai-data-preparation-sdg.md)
+ [Data quality evaluation](ai-data-preparation-dq.md)
+ [Auto-labeling](ai-data-preparation-autolabel.md)
+ [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets)
+ [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup)
+ [Model customization](customizing-models.md)
+ [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/)