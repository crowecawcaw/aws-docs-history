

# Synthetic data generation

With synthetic data generation (SDG), you describe the dataset that you need in a dataset specification, and SageMaker AI generates records that meet that specification. SDG produces large language model (LLM) data in JSON Lines format and tabular data in formats such as CSV, for training, evaluating, and testing models.

Use SDG when:
+ You have a use case for model customization but no data, or not enough data, to fine-tune with.
+ You need evaluation or test data that covers specific scenarios, formats, or difficulty levels.
+ Your existing data under-represents some classes or cases, and you want samples that target those gaps.

## How it works
<a name="ai-data-preparation-sdg-how"></a>

SDG is specification-driven. Instead of prompting a model to write records directly, SageMaker AI uses a model to write Python code that generates records and verifies them against your specification. The service refines that code until samples consistently pass verification, and then runs it at the scale that you request.

An SDG job works with the following:

Dataset specification  
A Markdown (`.md`) or text (`.txt`) file that describes the data that you want: the task type (for example, classification or question answering), the fields in each record, the domain, and any constraints or quality criteria. You can write it yourself or author it with an agent.  
For how to structure a specification, choose how records are verified, and write one for LLM or tabular data, see [Write a dataset specification](#ai-data-preparation-sdg-spec-write).

Generation code  
A job that starts from a specification returns the final code that it used, `generation.py` and `verifiers.py`, alongside the dataset. You can download, review, and modify this code, and then submit it to later jobs so that they skip code generation and only produce records. For more information about the code, see [Understand the generation code](#ai-data-preparation-sdg-code).

Contextual data (optional)  
Domain data that the generated records draw on. Without it, SageMaker AI generates from the specification alone. For more information about contextual data, see [Inputs](#ai-data-preparation-sdg-inputs).

Output dataset  
Each completed job writes the records to Amazon S3 in the format that your specification names, such as JSON Lines for LLM training data or CSV for tabular data. The job also registers them as hub content of type `DataSet` in a hub in your account. The job returns a `DataSet` object whose `arn` identifies the dataset when you pass it to other capabilities, and whose `source` is its Amazon S3 location. The dataset record also stores the location of the specification that produced it, so later jobs, such as data quality evaluation, can reuse that specification. For more information about datasets, see [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets).  
A dataset ARN has the following format, where {{region}} and {{account-id}} are the Region and account of the job, {{hub-name}} is the hub that holds the dataset, and {{dataset-name}} and {{version}} identify the dataset version:  

```
arn:aws:sagemaker:{{region}}:{{account-id}}:hub-content/{{hub-name}}/DataSet/{{dataset-name}}/{{version}}
```
For example:  

```
arn:aws:sagemaker:us-east-1:111122223333:hub-content/my-hub/DataSet/product-reviews/1.0.0
```
For JSON Lines output, each line of the output file is one record in the format that your specification's output schema names. For CSV output, each row after the header is one record. For examples, see [Write a dataset specification](#ai-data-preparation-sdg-spec-write).

Most SDG work follows this loop:

1. **Sample** – Generate a small number of records (for example, 10) to confirm that the generation is heading in the right direction. This step also creates the generation code that later jobs reuse to generate data at scale.

1. **Review and refine** – Inspect the sample records and the generation code. Then refine the specification or edit the code.

1. **Generate at scale** – Run the full job with the number of records that you need, reusing the refined code.

## Write a dataset specification
<a name="ai-data-preparation-sdg-spec-write"></a>

SageMaker AI turns your specification into Python code, so the specification is where you control what the job generates and how it checks each record. You write it in plain language, organized into the following sections. The examples for [LLM training data](#ai-data-preparation-sdg-spec-write-llm) and [tabular data](#ai-data-preparation-sdg-spec-write-tabular) later in this section use the same headings.


<table>
<thead>
  <tr><th>Section</th><th>What it describes</th><th>Where the generated code uses it</th></tr>
</thead>
<tbody>
  <tr><td><code>Use Case Context</code></td><td>The task, who uses the data, and how.</td><td rowspan="2">Guides the rest of the specification and the code as a whole</td></tr>
  <tr><td><code>Quality Standards</code></td><td>What good data looks like, such as accuracy, diversity, and consistency.</td></tr>
  <tr><td><code>Input Data</code> (required if the job has input data)</td><td>Each input file and the schema of its records. Optionally, add <code>Input Data Preparation</code> for preprocessing steps.</td><td><code>prepare_batch</code> in <code>generation.py</code></td></tr>
  <tr><td><code>Output Schema</code></td><td>The format of each record.</td><td rowspan="2"><code>generator</code> in <code>generation.py</code> (<code>prepare_batch</code> sets up the categorical value lists)</td></tr>
  <tr><td><code>Data Generation</code></td><td>How each field is generated (<code>Data Fields</code>), and optionally rules that apply across fields or records (<code>Generation Constraints</code>).</td></tr>
  <tr><td><code>Data Verification</code></td><td>The verification mode and the checks that each record must pass.</td><td><code>verify_sample</code> in <code>verifiers.py</code></td></tr>
</tbody>
</table>


For more information about each function in the generated code, see [Understand the generation code](#ai-data-preparation-sdg-code). The generated code can use only a fixed set of Python modules, so don't specify anything that requires other libraries or network access. For more information about the allowed modules, see [Modules that the code can use](#ai-data-preparation-sdg-code-env).

### Define how fields are generated
<a name="ai-data-preparation-sdg-spec-write-generation"></a>

In the `Data Fields` part of `Data Generation`, define each field on one line, in the form `field_name (Priority): description`. The priority is `Core` for a field that directly serves the use case, or `Auxiliary` for a supporting field that adds realism or variation. Group the fields by type. Each type maps to a different way that the generated code produces the value:


| Field type | How the value is produced | In the examples | 
| --- | --- | --- | 
| Categorical | Sampled from a finite set of values, uniformly or with weights. | sentiment, product\_category, region | 
| LLM-generated | Written by an LLM call, conditioned on other fields. | review\_text, city, known\_for | 
| Programmatic | Computed by code with no LLM call, such as a template, a copy of another field, Faker, or custom logic. | prompt, completion, id | 

Categorical and programmatic fields are faster and cheaper than LLM-generated fields. When a value can be derived from other fields or from your contextual data, define it as programmatic and reserve LLM-generated fields for content that needs to be written.

### Choose how records are verified
<a name="ai-data-preparation-sdg-spec-write-verification"></a>

In `Data Verification`, define the checks that each record must pass. There are two kinds of checks:
+ **Structural checks** – Python checks of format, field presence, value ranges, text length, and cross-field consistency. Always include these.
+ **Semantic checks** – An LLM judges content that code can't check, such as whether a review's sentiment matches its label or whether text is supported by the contextual data.

Set `Verification Mode` to choose which checks run:


| Mode | What runs | Use when | 
| --- | --- | --- | 
| deterministic | Structural checks only, in pure Python with no LLM calls. Generation is faster, and verification has no LLM cost. | Structural rules can fully validate quality, as in the tabular example. | 
| llm-augmented (default) | Structural checks plus an LLM call for each record. More thorough, but slower and more expensive. | Quality depends on semantic judgment, as in the LLM training data example, where the review's sentiment must match its label. | 

Choose one mode, and state it in the specification. When you choose `deterministic`, also state that verification must not call an LLM. When you choose `llm-augmented`, also state that verification must call an LLM for each record. Keep the semantic checks in a single LLM call, and accept a record when most of the semantic checks pass rather than all of them. Checks that are too strict can cause the job to fail.

### Add seed and contextual data
<a name="ai-data-preparation-sdg-spec-write-input"></a>

To shape records with your own data, give the job the data and describe it in the specification. You need both:

1. Upload the files to Amazon S3, as one file or under one prefix. Do any preprocessing that needs other tools before you upload. For more information about supported formats and limits, see [Inputs](#ai-data-preparation-sdg-inputs).

1. Set `InputDataS3Uri` in the job's `generation_config` to that file or prefix.

1. Describe each file in the specification's `Input Data` section.

The `Input Data` section is required whenever the job has input data. The generated code receives only a file path, so this section is the only way it learns what your files contain. If you don't name a file and its record keys, the code guesses them. For each file, give the following:
+ Its name, and its path relative to the prefix if it's in a subfolder.
+ Its format and the keys or columns of each record.
+ Its role in generation. Input data usually plays one of these roles:
  + **Seed examples** – Example records that show the quality and format that you want, used as examples or style references.
  + **Context documents** – Content that the job generates records from, such as documents to ask questions about or text to label.
  + **Reference material** – Domain knowledge or large value sets for fields to draw from, such as a list of product names.

To clean or filter the data before generation, for example to drop incomplete records or remove duplicates, add an `Input Data Preparation` section.

The following `Input Data` section is from a specification for question answering over product manuals. It uses seed examples and context documents:

```txt
## Input Data
The input prefix contains:
- seed_qa.jsonl - seed examples. JSONL, one record per line, with the keys
  question and answer. Use them as style references.
- sections_index.json - an index of the manual sections:
  {"sections": [{"section_id", "section_title", "file"}]}. file is the path
  of the section's text file, relative to the input prefix.
- sections/*.txt - context documents, one text file per section. Generate
  each question and answer from the text of one section.
```

The generated `prepare_batch` function reads these files and stores them in `auxiliary_datastore` for `generator` to use. Its `input_data` parameter is the path of one file in the prefix, so the code finds each file by the name that `Input Data` gives it. The following code is shortened from a job that used this kind of specification:

```python
def prepare_batch(batch_size, generator_llm, input_data):
    # input_data is the path of one file in the input prefix.
    root = os.path.dirname(input_data)

    # Seed examples, by the name in Input Data.
    with open(os.path.join(root, "seed_qa.jsonl")) as f:
        seeds = [json.loads(line) for line in f if line.strip()]

    # Context documents, listed in the index.
    with open(os.path.join(root, "sections_index.json")) as f:
        index = json.load(f)
    sections = []
    for entry in index["sections"]:
        with open(os.path.join(root, entry["file"])) as f:
            sections.append({"section_id": entry["section_id"], "text": f.read()})

    return {"seeds": seeds, "sections": sections}
```

### Example: LLM training data
<a name="ai-data-preparation-sdg-spec-write-llm"></a>

For data to train or evaluate an LLM, name a supported dataset format in `Output Schema`, and show the JSON structure with field placeholders. Each record is one line of JSON Lines output in that format. The supported formats are the following:
+ `Bedrock_Converse`
+ `HF_Prompt_Completion`
+ `HF_Preference`
+ `OpenAI_Messages`
+ `Nova_CPT`
+ `Nova_PPO`
+ `Nova_RLVR`
+ `SageMaker_Eval`
+ `Verl`

Records that match none of these formats are registered with the `Custom` format, which is how tabular output is registered.

The following example, shortened from a full specification, describes a supervised fine-tuning (SFT) dataset for teaching an open-weight LLM to classify product-review sentiment. It generates records from the specification alone, so it has no `Input Data` section.

```txt
# Product Review Sentiment Classification Dataset

## Use Case Context
An online retailer wants to fine-tune an open-weight LLM with SFT to classify
the sentiment of product reviews. Each record is a prompt-completion pair: the
prompt asks for the sentiment of a review, and the completion is the label
(positive, negative, or neutral).

## Quality Standards
- Authenticity: reviews read like real customer experiences
- Sentiment accuracy: each label matches the sentiment in the review
- Diversity: a range of product categories, lengths, and writing styles

## Output Schema
HF_Prompt_Completion (JSONL):
{
  "prompt": "Classify the sentiment of the following product review as positive, negative, or neutral:\n\n{review_text}",
  "completion": "{sentiment}"
}

## Data Generation
### Data Fields
1. Sample categorical attributes:
   - product_category (Auxiliary): weighted (25% Electronics, 20% Home & Kitchen, 15% Clothing, 40% other)
   - sentiment (Core): weighted (40% positive, 30% negative, 30% neutral)
2. LLM-generated fields:
   - review_text (Core): Use product_category and sentiment. Write an authentic
     review, 20-100 words, that expresses the sentiment.
3. Compute programmatic fields:
   - prompt (Core): the template in Output Schema, with review_text inserted
   - completion (Core): Copy value from sentiment

## Data Verification
### Verification Mode
llm-augmented
Verification must include an LLM call to check each record.

### Checks
1. Structural checks: the record has exactly prompt and completion; prompt
   starts with the template in Output Schema; completion is one of positive,
   negative, or neutral
2. Semantic checks (LLM-based): the sentiment of review_text matches completion
```

For this specification, a record looks like the following:

```json
{"prompt": "Classify the sentiment of the following product review as positive, negative, or neutral:\n\nThe headphones stopped charging after two days.", "completion": "negative"}
```

### Example: tabular data
<a name="ai-data-preparation-sdg-spec-write-tabular"></a>

For structured rows, such as data for traditional machine learning models, test data, or database seeding, list the columns in order in `Output Schema`, and name the output format: CSV (the default), Parquet, or SQLite. For multiple related tables, describe each table and its keys. To generate rows that match existing data, set `InputDataS3Uri` to seed data in CSV, Parquet, SQLite, JSON, or JSON Lines format, and describe its schema in `Input Data`, as described in [Add seed and contextual data](#ai-data-preparation-sdg-spec-write-input).

The following example extends a CSV seed file of cities. Its checks are all structural, so it uses `deterministic` verification.

```txt
# City Reference Table

## Use Case Context
A travel app team needs a table of world cities to seed a test database. Each
record is one row that describes a real city.

## Quality Standards
- Realism: each row describes a real city, and its fields agree with each other
- Diversity: cities from every world region
- Consistency: values follow the types and formats in the seed data

## Input Data
- seed_data.csv - CSV file of example rows with the columns
  id, city, country, population, avg_temp_c, known_for. Use it as the schema
  and style reference.

## Output Schema
CSV, one row per record, with the columns in this order:
id,city,country,population,avg_temp_c,known_for

## Data Generation
### Data Fields
1. Sample categorical attributes:
   - region (Auxiliary): one of [East Asia, South Asia, Europe, Americas,
     Africa and Middle East, Oceania]
2. LLM-generated fields:
   - city (Core): Use region. A real city in that region.
   - country (Core): the country of city
   - population (Core): the approximate population of city, as an integer
   - avg_temp_c (Core): the average annual temperature of city in degrees
     Celsius, with one decimal place
   - known_for (Core): a short phrase that describes what city is known for
3. Compute programmatic fields:
   - id (Core): sequential integers, starting after the largest id in
     seed_data.csv, unique across all records

### Generation Constraints
- No two rows have the same city and country

## Data Verification
### Verification Mode
deterministic
Do not use an LLM to verify samples. All verification must be pure Python.

### Checks
1. Structural checks: each row has exactly 6 fields in the column order;
   id is a unique positive integer; population is a positive integer;
   avg_temp_c is a number from -30 to 40; city, country, and known_for are
   non-empty
```

Run this specification with `InputDataS3Uri` set to the Amazon S3 location of `seed_data.csv`. For this specification, a record looks like the following row:

```
4,Bologna,Italy,390635,13.2,Cuisine and university
```

## Inputs
<a name="ai-data-preparation-sdg-inputs"></a>

An SDG job takes either a specification or refined generation code, and optionally contextual data. You set these in the job's `generation_config`. The following snippets show only that part of the job configuration. In the snippets on this page, replace {{amzn-s3-demo-bucket}} with the name of your Amazon S3 bucket. For a complete example, see [Generate a dataset](#ai-data-preparation-sdg-use).

Specification (to start a new dataset)  
Start from a specification when you create a new dataset. SageMaker AI writes the generation code from your specification, runs it, and returns the code with the records. Write the specification as described in [Write a dataset specification](#ai-data-preparation-sdg-spec-write), and pass its Amazon S3 location as `SpecS3Uri`.  

```python
generation_config={
    "DatasetSpecification": {
        "SpecS3Uri": "s3://{{amzn-s3-demo-bucket}}/specs/reviews-spec.md",
    },
    "NumSamples": 10,
}
```
`NumSamples` sets how many records the job generates. Start with a small sample, such as 10 records.  
**Refine the specification and the code.** When the sample records aren't what you want, refine either or both before you generate at scale:  
+ **Tighten the specification** – Add constraints, adjust field distributions, or add verification checks, and then run a new sample from the specification. SageMaker AI writes new generation code to match.
+ **Edit the code** – A job that starts from a specification writes `generation.py` and `verifiers.py` to a `generation_code/` prefix next to its output. Edit copies of them when you need precise control over how the code generates or checks a field, and upload the copies to an Amazon S3 prefix of your own. Keep the file names `generation.py` and `verifiers.py`.

Refined generation code (to generate at scale)  
After you refine the code from a sample run, pass it to a new job to generate the full dataset. SageMaker AI skips code generation and runs your code directly, so the job scales from a small sample to the number of records that you need, using the logic that you reviewed. You can also pass an earlier job's code unchanged. Set `GenerationCodeS3Uri` and `VerifiersCodeS3Uri` to the Amazon S3 locations of your `generation.py` and `verifiers.py` files:  

```python
generation_config={
    "DatasetSpecification": {
        "CodeArtifacts": {
            "GenerationCodeS3Uri": "s3://{{amzn-s3-demo-bucket}}/sdg/generation_code/generation.py",
            "VerifiersCodeS3Uri": "s3://{{amzn-s3-demo-bucket}}/sdg/generation_code/verifiers.py",
        },
    },
    "NumSamples": 1000,
}
```
When you pass generation code, the code, not the original specification, defines what the job generates. The job also runs the code as is. A job that starts from a specification fixes problems in its code while it runs, but a job that starts from code can't, so a defect in the code can fail the run. After you edit the code, generate a small sample from it before you generate at scale.

Contextual data (optional)  
Contextual data, such as seed examples and context documents, gives the generated records the terminology and patterns of your domain. Set `InputDataS3Uri` to an Amazon S3 file or prefix, and describe the data in your specification's `Input Data` section. For details, see [Add seed and contextual data](#ai-data-preparation-sdg-spec-write-input).  
A prefix can hold up to 1,000 files of up to 10 MB each. Supported formats are CSV, DB, DOC, DOCX, HTML, JSON, JSON Lines, Markdown, Parquet, PDF, SQL, SQLite, and text. Set `InputDataS3Uri` at the top level of `generation_config`, alongside a specification or refined code:  

```python
generation_config={
    "DatasetSpecification": {
        "SpecS3Uri": "s3://{{amzn-s3-demo-bucket}}/specs/manual-qa-spec.md",
    },
    "InputDataS3Uri": "s3://{{amzn-s3-demo-bucket}}/sdg/contextual-data/",
    "NumSamples": 10,
}
```

## Generate a dataset
<a name="ai-data-preparation-sdg-use"></a>

You can run SDG in the Amazon SageMaker Python SDK directly, or through a coding assistant directed by the core AI and ML skill in the Agent Toolkit for AWS. Both run the same job and produce the same dataset.

------
#### [ Amazon SageMaker Python SDK ]

The following example generates a 10-record sample from a dataset specification, and then generates the full dataset from the sample job's generation code. It assumes that you've configured an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup). Before you run it, upload your specification to Amazon S3, for example:

```bash
aws s3 cp reviews-spec.md s3://{{amzn-s3-demo-bucket}}/specs/reviews-spec.md
```

Then run the following code:

```python
from sagemaker.core.helper.session_helper import Session
from sagemaker.ai_registry import DataPreparer, DatasetJobConfig, JobCategory

session = Session()
preparer = DataPreparer(sagemaker_session=session)

# 1. List every field that an SDG job accepts.
DatasetJobConfig.print_schema(JobCategory.SYNTHETIC_DATA_GENERATION)

# 2. Generate a small sample from the dataset specification.
sample = preparer.generate(DatasetJobConfig(
    dataset_name="product-reviews-sample",
    generation_config={
        "DatasetSpecification": {
            "SpecS3Uri": "s3://{{amzn-s3-demo-bucket}}/specs/reviews-spec.md",
        },
        "NumSamples": 10,
    },
))
print(sample.arn, sample.source)

# 3. Find the generation code that the sample job wrote, and review it.
code_uri = sample.source.rstrip("/").removesuffix("/output") + "/generation_code/"
#    To edit the code, download generation.py and verifiers.py from code_uri.
#    Change them, upload them to a prefix of your own (keep both file names),
#    and set code_uri to that prefix (ending in "/").

# 4. Generate the full dataset from the reviewed code.
dataset = preparer.generate(DatasetJobConfig(
    dataset_name="product-reviews",
    generation_config={
        "DatasetSpecification": {
            "CodeArtifacts": {
                "GenerationCodeS3Uri": code_uri + "generation.py",
                "VerifiersCodeS3Uri": code_uri + "verifiers.py",
            },
        },
        "NumSamples": 1000,
    },
))
print(dataset.arn, dataset.source)
```

In this example, set the following values for your job:
+ `dataset_name` – A name for the dataset. It must be 1–63 characters of letters, numbers, and hyphens, and must start and end with a letter or number.
+ `SpecS3Uri` – The Amazon S3 location of your dataset specification.
+ `NumSamples` – The number of records to generate.
+ `CodeArtifacts` – The Amazon S3 locations of the `generation.py` and `verifiers.py` files to run.

The example works as follows:
+ `print_schema()` lists the fields that the service currently accepts for an SDG job.
+ `generate()` waits until the job finishes and then returns a `DataSet`. During the wait, it shows the job's status and elapsed time, and it prints the job's ARN when it submits the job. To submit the job and return immediately, pass `wait=False`. Later, run `DataPreparer.attach("{{job-arn}}")` to wait for the job and get its `DataSet`. Use `wait=False` for large jobs, such as the 1,000-record job in step 4.
+ Step 3 in the example code derives `code_uri` from the sample job, because only a job that starts from a specification writes `generation_code/`. If you edit the code, generate a small sample from your edited code before step 4, the full run.

------
#### [ Coding assistant with the AI and ML skill ]

With a coding assistant, you can run SDG through a guided conversation, directed by the core AI and ML skill (`aws-ai-ml`) in the Agent Toolkit for AWS. To install it, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/). As with the SDK, you need an execution role and a default Amazon S3 bucket, as described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup). Start with a prompt that describes your use case, for example:

```
I want to fine-tune a model to classify the sentiment of product reviews,
but I don't have any training data. Help me generate a dataset.
```

The assistant then works through the same steps as the SDK example, and asks for your approval before each job:

1. Drafts a dataset specification with you, if you don't already have one.

1. Generates a small sample and shows you the records.

1. Refines the generation code based on your feedback.

1. Generates the full dataset, and saves the work as a notebook or script that you can rerun.

------

**Tip**  
**Plan for run time.** Run time depends on the number of records and on how they're generated and verified. A job that starts from a specification first writes and refines the generation code, so it takes longer than a job that reuses code. LLM-generated fields and `llm-augmented` verification make LLM calls for each record, so they take longer than programmatic fields and `deterministic` verification. For more information about verification modes, see [Choose how records are verified](#ai-data-preparation-sdg-spec-write-verification).

## Results
<a name="ai-data-preparation-sdg-results"></a>

When a job finishes, `generate()` returns a `DataSet` and prints a preview of the generated records. The dataset's `source` is the `output/` prefix of the job in Amazon S3. The job writes the following files under its output root, one level above `source`:


| File | Contents | 
| --- | --- | 
| output/output\_samples.jsonl | The generated records. For tabular data, the records are in output/output\_samples.csv or in the format that your specification names. | 
| report.json | A summary of the job, including its status and the output format that it detected. | 
| token\_usage\_report.json | The model tokens that the job used, in total and for each model. | 
| generation\_code/ | generation.py and verifiers.py. Only jobs that start from a specification write these files. | 

## Understand the generation code
<a name="ai-data-preparation-sdg-code"></a>

After it refines the generation code, a job that starts from a specification writes the final code to the `generation_code/` prefix. You can read, edit, and reuse this code. It has three functions, each of which implements part of your specification:


| Function | What it does | Specification sections | 
| --- | --- | --- | 
| prepare\_batch(batch\_size, generator\_llm, input\_data) in generation.py | Runs before the job generates records. It reads your contextual data, if any, and builds the values that every record draws on, such as the weighted value lists for categorical fields. It returns them as a dictionary, auxiliary\_datastore. | Input Data, Input Data Preparation, and categorical values from Data Fields | 
| generator(auxiliary\_datastore, generator\_llm) in generation.py | Generates one record. It samples categorical fields, calls generator\_llm for LLM-generated fields, computes programmatic fields, and returns the record in the output schema. | Output Schema and Data Generation | 
| verify\_sample(sample, auxiliary\_datastore, verifier\_llm) in verifiers.py | Checks one record. It returns whether the record passed, feedback that explains the result, and the record, to which it can add the check results. A record that fails isn't included in the output. | Data Verification | 

For example, for the [LLM training data example](#ai-data-preparation-sdg-spec-write-llm), `generation.py` looks like the following (shortened):

```python
# Imports and helper functions, such as weighted_sample and
# generate_review_text, are omitted.

def prepare_batch(batch_size, generator_llm, input_data):
    # This specification has no Input Data, so input_data isn't used.
    # Categorical values and weights, from Data Fields.
    product_category_weights = [
        ("Electronics", 0.25), ("Home & Kitchen", 0.20), ("Clothing", 0.15),
        # ...
    ]
    sentiment_weights = [("positive", 0.40), ("negative", 0.30), ("neutral", 0.30)]

    return {
        "product_category_weights": product_category_weights,
        "sentiment_weights": sentiment_weights,
    }


def generator(auxiliary_datastore, generator_llm):
    # Categorical fields: weighted sampling, using the weights from prepare_batch.
    product_category = weighted_sample(auxiliary_datastore["product_category_weights"])
    sentiment = weighted_sample(auxiliary_datastore["sentiment_weights"])

    # LLM-generated field: one LLM call for each record.
    review_text = generate_review_text(generator_llm, product_category, sentiment)

    # Programmatic fields: a template and a copy of another field.
    prompt = (
        "Classify the sentiment of the following product review as positive, "
        "negative, or neutral:\n\n" + review_text
    )
    completion = sentiment

    return json.dumps({"prompt": prompt, "completion": completion})
```

The matching `verifiers.py` runs the structural checks, and then, because the specification uses `llm-augmented` mode, one LLM call for the semantic check (shortened):

```python
# Imports and helper functions, such as extract_xml_tag, are omitted.

def verify_sample(sample, auxiliary_datastore, verifier_llm):
    record = json.loads(sample)
    prefix = (
        "Classify the sentiment of the following product review as positive, "
        "negative, or neutral:\n\n"
    )

    # Structural checks.
    issues = []
    if set(record) != {"prompt", "completion"}:
        issues.append("Record must contain exactly prompt and completion")
    if record.get("completion") not in {"positive", "negative", "neutral"}:
        issues.append("completion must be positive, negative, or neutral")
    if not str(record.get("prompt", "")).startswith(prefix):
        issues.append("prompt does not start with the instruction template")
    if issues:
        return False, "; ".join(issues), sample

    # Semantic check: one LLM call judges the review's sentiment.
    review_text = record["prompt"][len(prefix):]
    response = verifier_llm.invoke_model(
        "Classify the sentiment of this review. Reply with "
        f"<sentiment>positive, negative, or neutral</sentiment>.\n\n{review_text}",
        "You are an expert sentiment analysis judge for product reviews.",
    )
    judged = extract_xml_tag(response, "sentiment")
    passed = judged == record["completion"]

    feedback = "Sentiment matches." if passed else f"LLM judged '{judged}'."
    return passed, feedback, json.dumps(record)
```

When you review the code, check the following:
+ **Each field matches your specification** – Compare the values, weights, prompts, and templates in `prepare_batch` and `generator` to your `Data Fields`.
+ **The checks match your quality standards** – Confirm that `verify_sample` enforces the checks that you specified, and no stricter or looser ones.
+ **The code uses the verification mode that you chose** – In `deterministic` mode, confirm that `verify_sample` doesn't call `verifier_llm`, even though it takes it as a parameter.

When you edit the code, keep the following in mind:
+ Keep the function names and parameters, and keep the file names `generation.py` and `verifiers.py`.
+ The two files load into one namespace, and names defined at the top level of `verifiers.py` override the same names in `generation.py`. Don't define the same top-level name in both files, for example a value list in one and a set in the other.
+ A job that starts from your code runs it as written and doesn't read the specification. If you later change the specification, start a new job from the specification to get code that reflects the change.

### Modules that the code can use
<a name="ai-data-preparation-sdg-code-env"></a>

The code runs with a fixed set of Python modules: a subset of the Python standard library, such as `json`, `re`, `random`, `csv`, and `glob`, plus `faker`, `numpy`, and `pandas`. It can't make network calls, run other programs, or use embedding or vector search libraries. This applies to code that SageMaker AI writes from your specification and to code that you edit. In your specification, describe retrieval from contextual data as a keyword or text match, and do any preprocessing that needs other tools before you upload the data.

## Limits and quotas
<a name="ai-data-preparation-sdg-limits"></a>

The following quotas apply to SDG. Adjustable quotas can be increased through Service Quotas.


| Quota | Default | Adjustable | 
| --- | --- | --- | 
| Concurrent SDG jobs per account in each Region | 3 | Yes | 
| Records per job (NumSamples) | 1–50,000 | No | 
| Contextual data files per job | 1,000 | No | 
| Size of each contextual data file | 10 MB | No | 

For more information about supported Regions and the quotas that apply to every capability, such as the number of datasets in a hub, see [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md).

SDG jobs also depend on quotas in other services:
+ **Amazon Bedrock** – SDG jobs invoke Amazon Bedrock models to generate and verify records. The on-demand quotas for those models, such as tokens per minute and requests per minute, can limit how fast a job runs. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) in the *Amazon Bedrock User Guide*.
+ **SageMaker AI** – For more information about SageMaker AI quotas, see [SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *AWS General Reference*.

To run more SDG jobs at the same time, request an increase to the **Maximum number of concurrent synthetic data generation jobs** quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home).

## Troubleshooting
<a name="ai-data-preparation-sdg-troubleshoot"></a>

The job fails with `HUB_FINALIZATION_FAILED`  
SageMaker AI generated the records but couldn't register them as a dataset. The records are still in Amazon S3. Make sure that the execution role has the `sagemaker:ImportHubContent` permission on the hub and on its `DataSet` hub content. For more information about the required permissions, see [Required permissions](ai-data-preparation-getting-started.md#ai-data-preparation-setup-iam).

The job fails with a Region mismatch error  
Move the specification, contextual data, generation code, and output location to buckets in the same Region as the job. For more information about this requirement, see [Limits for all capabilities](ai-data-preparation-regions-limits.md#ai-data-preparation-regions-limits-shared).

The first sample takes a long time  
This is expected. A job that starts from a specification writes and refines the generation code before it produces records.

The sample succeeds, but the full run from its code fails  
A job that starts from code runs that code as is and can't repair it. As a result, a defect that a specification-based job would fix can fail the run. Generate a small sample from the same code to reproduce the failure, and fix the code. Or start a new job from the specification so that SageMaker AI writes fresh code.

Changes to the specification have no effect  
A job that starts from code doesn't read the specification. After you change the specification, start a new job from the specification to get new generation code.

Your session ends before the job finishes  
The job keeps running. `generate()` prints the job's ARN when it submits the job. To reconnect and get the `DataSet` when the job completes, run `dataset = DataPreparer.attach("{{job-arn}}")`.

## Where you go next
<a name="ai-data-preparation-sdg-next"></a>

The job's output is a dataset that you pass by ARN to the next step:
+ [Data quality evaluation](ai-data-preparation-dq.md) – Check that the records meet your quality criteria. The evaluation can reuse the specification stored with the dataset.
+ [Data transformation](ai-data-preparation-dt.md) – Deduplicate, filter, split into training and test sets, or convert the dataset to another format.
+ [Model customization](customizing-models.md) – Fine-tune a model with the dataset as training data.

## Related information
<a name="ai-data-preparation-sdg-related"></a>
+ [Data quality evaluation](ai-data-preparation-dq.md)
+ [Data transformation](ai-data-preparation-dt.md)
+ [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets)
+ [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup)
+ [Model customization](customizing-models.md)
+ [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/)