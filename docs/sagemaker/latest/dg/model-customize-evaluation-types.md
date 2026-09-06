

# Evaluation types and Job Submission
<a name="model-customize-evaluation-types"></a>

## Benchmarking with standardized datasets
<a name="model-customize-evaluation-benchmarking"></a>

Use the Benchmark Evaluation type to evaluate the quality of your model across standardized benchmark datasets including popular datasets like MMLU and BBH.


| Benchmark | Custom Dataset Supported | Modalities | Description | Metrics | Strategy | Subtask available | 
| --- | --- | --- | --- | --- | --- | --- | 
| mmlu | No | Text | Multi-task Language Understanding – Tests knowledge across 57 subjects. | accuracy | zs\_cot | Yes | 
| mmlu\_pro | No | Text | MMLU – Professional Subset – Focuses on professional domains such as law, medicine, accounting, and engineering. | accuracy | zs\_cot | No | 
| bbh | No | Text | Advanced Reasoning Tasks – A collection of challenging problems that test higher-level cognitive and problem-solving skills. | accuracy | fs\_cot | Yes | 
| gpqa | No | Text | General Physics Question Answering – Assesses comprehension of physics concepts and related problem-solving abilities. | accuracy | zs\_cot | No | 
| math | No | Text | Mathematical Problem Solving – Measures mathematical reasoning across topics including algebra, calculus, and word problems. | exact\_match | zs\_cot | Yes | 
| strong\_reject | No | Text | Quality-Control Task – Tests the model's ability to detect and reject inappropriate, harmful, or incorrect content. | deflection | zs | Yes | 
| ifeval | No | Text | Instruction-Following Evaluation – Gauges how accurately a model follows given instructions and completes tasks to specification. | accuracy | zs | No | 

For more information on BYOD formats, see [Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks](model-customize-evaluation-dataset-formats.md).

### Available Subtasks
<a name="model-customize-evaluation-benchmarking-subtasks"></a>

The following lists available subtasks for model evaluation across multiple domains including MMLU (Massive Multitask Language Understanding), BBH (Big Bench Hard), StrongReject, and MATH. These subtasks allow you to assess your model's performance on specific capabilities and knowledge areas.

**MMLU Subtasks**

```
MMLU_SUBTASKS = [
    "abstract_algebra",
    "anatomy",
    "astronomy",
    "business_ethics",
    "clinical_knowledge",
    "college_biology",
    "college_chemistry",
    "college_computer_science",
    "college_mathematics",
    "college_medicine",
    "college_physics",
    "computer_security",
    "conceptual_physics",
    "econometrics",
    "electrical_engineering",
    "elementary_mathematics",
    "formal_logic",
    "global_facts",
    "high_school_biology",
    "high_school_chemistry",
    "high_school_computer_science",
    "high_school_european_history",
    "high_school_geography",
    "high_school_government_and_politics",
    "high_school_macroeconomics",
    "high_school_mathematics",
    "high_school_microeconomics",
    "high_school_physics",
    "high_school_psychology",
    "high_school_statistics",
    "high_school_us_history",
    "high_school_world_history",
    "human_aging",
    "human_sexuality",
    "international_law",
    "jurisprudence",
    "logical_fallacies",
    "machine_learning",
    "management",
    "marketing",
    "medical_genetics",
    "miscellaneous",
    "moral_disputes",
    "moral_scenarios",
    "nutrition",
    "philosophy",
    "prehistory",
    "professional_accounting",
    "professional_law",
    "professional_medicine",
    "professional_psychology",
    "public_relations",
    "security_studies",
    "sociology",
    "us_foreign_policy",
    "virology",
    "world_religions"
]
```

**BBH Subtasks**

```
BBH_SUBTASKS = [
    "boolean_expressions",
    "causal_judgement",
    "date_understanding",
    "disambiguation_qa",
    "dyck_languages",
    "formal_fallacies",
    "geometric_shapes",
    "hyperbaton",
    "logical_deduction_five_objects",
    "logical_deduction_seven_objects",
    "logical_deduction_three_objects",
    "movie_recommendation",
    "multistep_arithmetic_two",
    "navigate",
    "object_counting",
    "penguins_in_a_table",
    "reasoning_about_colored_objects",
    "ruin_names",
    "salient_translation_error_detection",
    "snarks",
    "sports_understanding",
    "temporal_sequences",
    "tracking_shuffled_objects_five_objects",
    "tracking_shuffled_objects_seven_objects",
    "tracking_shuffled_objects_three_objects",
    "web_of_lies",
    "word_sorting"
]
```

**Math Subtasks**

```
MATH_SUBTASKS = [
    "algebra", 
    "counting_and_probability", 
    "geometry",
    "intermediate_algebra", 
    "number_theory", 
    "prealgebra", 
    "precalculus"
]
```

**StrongReject Subtasks**

```
STRONG_REJECT_SUBTASKS = [
    "gcg_transfer_harmbench", 
    "gcg_transfer_universal_attacks",
    "combination_3", 
    "combination_2", 
    "few_shot_json", 
    "dev_mode_v2",
    "dev_mode_with_rant",
    "wikipedia_with_title", 
    "distractors",
    "wikipedia",
     "style_injection_json", 
    "style_injection_short",
    "refusal_suppression", 
    "prefix_injection", 
    "distractors_negated",
    "poems", 
    "base64", 
    "base64_raw",
    "base64_input_only",
    "base64_output_only", 
    "evil_confidant", 
    "aim", 
    "rot_13",
    "disemvowel", 
    "auto_obfuscation", 
    "auto_payload_splitting", 
    "pair",
    "pap_authority_endorsement", 
    "pap_evidence_based_persuasion",
    "pap_expert_endorsement", 
    "pap_logical_appeal", 
    "pap_misrepresentation"
]
```

### Submit your benchmark job
<a name="model-customize-evaluation-benchmarking-submit"></a>

------
#### [ SageMaker Studio ]

![A minimal configuration for benchmarking through SageMaker Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/benchmark-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
from sagemaker.train.evaluate import get_benchmarks
from sagemaker.train.evaluate import BenchMarkEvaluator

Benchmark = get_benchmarks()

# Create evaluator with MMLU benchmark
evaluator = BenchMarkEvaluator(
benchmark=Benchmark.MMLU,
model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
s3_output_path="s3://<bucket-name>/<prefix>/",
evaluate_base_model=False
)

execution = evaluator.evaluate()
```

For more information on evaluation job submission through SageMaker Python SDK, see: [https://sagemaker.readthedocs.io/en/stable/model\_customization/evaluation.html](https://sagemaker.readthedocs.io/en/stable/model_customization/evaluation.html)

------

## Large Language Model as a Judge (LLMAJ) evaluation
<a name="model-customize-evaluation-llmaj"></a>

Use LLM-as-a-judge (LLMAJ) evaluation to leverage another frontier model to grade your target model responses. You can use AWS Bedrock models as judges by calling `create_evaluation_job` API to launch the evaluation job.
+ **SageMaker LLM as a Judge**: This feature is powered by Amazon Bedrock Evaluations. Your use of this feature is subject to pricing of Amazon Bedrock Evaluations, see the [Service Terms](https://aws.amazon.com/service-terms/) applicable to Amazon Bedrock, and the terms that apply to your usage of third-party models. Amazon Bedrock Evaluations may securely transmit data across AWS Regions within your geography for processing. For more information, access [Amazon Bedrock Evaluations documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html).

For more information on the supported judge models see: [https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)

You can use 2 different metric formats to define the evaluation:
+ **Builtin metrics:** Leverage AWS Bedrock builtin metrics to analyze the quality of your model's inference responses. For more information, see: [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html)
+ **Custom metrics:** Define your own custom metrics in Bedrock Evaluation custom metric format to analyze the quality of your model's inference responses using your own instruction. For more information, see: [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html)

### Submit a builtin metrics LLMAJ job
<a name="model-customize-evaluation-llmaj-builtin"></a>

------
#### [ SageMaker Studio ]

![A minimal configuration for LLMAJ benchmarking through SageMaker Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/llmaj-as-judge-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
from sagemaker.train.evaluate import LLMAsJudgeEvaluator

evaluator = LLMAsJudgeEvaluator(
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    evaluator_model="<bedrock-judge-model-id>",
    dataset="s3://<bucket-name>/<prefix>/<dataset-file>.jsonl",
    builtin_metrics=["<builtin-metric-1>", "<builtin-metric-2>"],
    s3_output_path="s3://<bucket-name>/<prefix>/",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

For more information on evaluation job submission through SageMaker Python SDK, see: [https://sagemaker.readthedocs.io/en/stable/model\_customization/evaluation.html](https://sagemaker.readthedocs.io/en/stable/model_customization/evaluation.html)

------

### Submit a custom metrics LLMAJ job
<a name="model-customize-evaluation-llmaj-custom"></a>

Define your custom metric(s):

```
{
    "customMetricDefinition": {
        "name": "PositiveSentiment",
        "instructions": (
            "You are an expert evaluator. Your task is to assess if the sentiment of the response is positive. "
            "Rate the response based on whether it conveys positive sentiment, helpfulness, and constructive tone.\n\n"
            "Consider the following:\n"
            "- Does the response have a positive, encouraging tone?\n"
            "- Is the response helpful and constructive?\n"
            "- Does it avoid negative language or criticism?\n\n"
            "Rate on this scale:\n"
            "- Good: Response has positive sentiment\n"
            "- Poor: Response lacks positive sentiment\n\n"
            "Here is the actual task:\n"
            "Prompt: {{prompt}}\n"
            "Response: {{prediction}}"
        ),
        "ratingScale": [
            {"definition": "Good", "value": {"floatValue": 1}},
            {"definition": "Poor", "value": {"floatValue": 0}}
        ]
    }
}
```

For more information, see: [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html)

------
#### [ SageMaker Studio ]

![Upload the custom metric via Custom metrics > Add custom metrics.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/custom-llmaj-metrics-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
evaluator = LLMAsJudgeEvaluator(
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    evaluator_model="<bedrock-judge-model-id>",
    dataset="s3://<bucket-name>/<prefix>/<dataset-file>.jsonl",
    custom_metrics=custom_metric_dict = {
        "customMetricDefinition": {
            "name": "PositiveSentiment",
            "instructions": (
                "You are an expert evaluator. Your task is to assess if the sentiment of the response is positive. "
                "Rate the response based on whether it conveys positive sentiment, helpfulness, and constructive tone.\n\n"
                "Consider the following:\n"
                "- Does the response have a positive, encouraging tone?\n"
                "- Is the response helpful and constructive?\n"
                "- Does it avoid negative language or criticism?\n\n"
                "Rate on this scale:\n"
                "- Good: Response has positive sentiment\n"
                "- Poor: Response lacks positive sentiment\n\n"
                "Here is the actual task:\n"
                "Prompt: {{prompt}}\n"
                "Response: {{prediction}}"
            ),
            "ratingScale": [
                {"definition": "Good", "value": {"floatValue": 1}},
                {"definition": "Poor", "value": {"floatValue": 0}}
            ]
        }
    },
    s3_output_path="s3://<bucket-name>/<prefix>/",
    evaluate_base_model=False
)
```

------

## Custom Scorers
<a name="model-customize-evaluation-custom-scorers"></a>

Define your own custom scorer function to launch an evaluation job. The system provides two built-in scorers: Prime math and Prime code. You can also bring your own scorer function. You can copy your scorer function code directly or bring your own Lambda function definition using the associated ARN. By default, both scorer types produce evaluation results which include standard metrics such as F1 score, ROUGE, and BLEU.

For more information on built-in and custom scorers and their respective requirements/contracts, see [Evaluate with Preset and Custom Scorers](model-customize-evaluation-preset-custom-scorers.md).

### Register your dataset
<a name="model-customize-evaluation-custom-scorers-register-dataset"></a>

Bring your own dataset for custom scorer by registering it as a SageMaker Hub Content Dataset.

------
#### [ SageMaker Studio ]

In Studio, upload your dataset using the dedicated Datasets page..

![Registered evaluation dataset in SageMaker Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/dataset-registration-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

In the SageMaker Python SDK, upload your dataset using the dedicated Datasets page..

```
from sagemaker.ai_registry.dataset import DataSet

dataset = DataSet.create(
    name="your-bring-your-own-dataset",
    source="s3://<bucket-name>/<prefix>/<dataset-file>.jsonl"
)
dataset.refresh()
```

------

### Submit a built-in scorer job
<a name="model-customize-evaluation-custom-scorers-builtin"></a>

------
#### [ SageMaker Studio ]

![Select from Code executions or Math answers for Built-In custom scoring.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/builtin-scorer-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
from sagemaker.train.evaluate import CustomScorerEvaluator
from sagemaker.train.evaluate import get_builtin_metrics

BuiltInMetric = get_builtin_metrics()

evaluator_builtin = CustomScorerEvaluator(
    evaluator=BuiltInMetric.PRIME_MATH,
    dataset="arn:aws:sagemaker:<region>:<account-id>:hub-content/<hub-content-id>/DataSet/your-bring-your-own-dataset/<version>",
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    s3_output_path="s3://<bucket-name>/<prefix>/",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

Select from `BuiltInMetric.PRIME_MATH` or `BuiltInMetric.PRIME_CODE` for Built-In Scoring.

------

### Submit a custom scorer job
<a name="model-customize-evaluation-custom-scorers-custom"></a>

Define a custom reward function. For more information, see [Custom Scorers (Bring Your Own Metrics)](model-customize-evaluation-preset-custom-scorers.md#model-customize-evaluation-custom-scorers-byom).

**Register the custom reward function**

------
#### [ SageMaker Studio ]

![Navigating to SageMaker Studio > Assets > Evaluator > Create evaluator > Create reward function.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/custom-scorer-submission-sagemaker-studio.png)


![Submit the Custom Scorer evaluation job referencing the registered preset reward function in Custom Scorer > Custom metrics.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/custom-scorer-benchmark-submission-sagemaker-studio.png)


------
#### [ SageMaker Python SDK ]

```
from sagemaker.ai_registry.evaluator import Evaluator
from sagemaker.ai_registry.air_constants import REWARD_FUNCTION

evaluator = Evaluator.create(
    name = "your-reward-function-name",
    source="/path_to_local/custom_lambda_function.py",
    type = REWARD_FUNCTION
)
```

```
evaluator = CustomScorerEvaluator(
    evaluator=evaluator,
    dataset="s3://<bucket-name>/<prefix>/<dataset-file>.jsonl",
    model="arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>/<version>",
    s3_output_path="s3://<bucket-name>/<prefix>/",
    evaluate_base_model=False
)

execution = evaluator.evaluate()
```

------