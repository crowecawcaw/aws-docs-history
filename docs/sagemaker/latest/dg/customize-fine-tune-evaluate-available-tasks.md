# Available benchmark

tasks

A sample code package is available that demonstrates how to calculate benchmark metrics
using the SageMaker AI model evaluation feature for Amazon Nova. To access the code packages, see [sample-Nova-lighteval-custom-task](https://github.com/aws-samples/sample-Nova-lighteval-custom-task/ "https://github.com/aws-samples/sample-Nova-lighteval-custom-task/").

Here is a list of the supported, available industry standard benchmarks. You can specify
the following benchmarks in the `eval_task` parameter:

| Benchmark     | Modality            | Description                                                                                                                                                                                                          | Metrics     | Strategy | Subtask Available |
| ------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | ----------------- |
| mmlu          | Text                | Multi-task Language Understanding – Tests knowledge across 57<br>subjects.                                                                                                                                           | accuracy    | zs_cot   | Yes               |
| mmlu_pro      | Text                | MMLU – Professional Subset – Focuses on professional domains such as law,<br>medicine, accounting, and engineering.                                                                                                  | accuracy    | zs_cot   | No                |
| bbh           | Text                | Advanced Reasoning Tasks – A collection of challenging problems that test<br>higher-level cognitive and problem-solving skills.                                                                                      | accuracy    | zs_cot   | Yes               |
| gpqa          | Text                | General Physics Question Answering – Assesses comprehension of physics<br>concepts and related problem-solving abilities.                                                                                            | accuracy    | zs_cot   | No                |
| math          | Text                | Mathematical Problem Solving – Measures mathematical reasoning across topics<br>including algebra, calculus, and word problems.                                                                                      | exact_match | zs_cot   | Yes               |
| strong_reject | Text                | Quality-Control Task – Tests the model’s ability to detect and reject<br>inappropriate, harmful, or incorrect content.                                                                                               | deflection  | zs       | Yes               |
| IFEval        | Text                | Instruction-Following Evaluation – Gauges how accurately a model follows given<br>instructions and completes tasks to specification.                                                                                 | accuracy    | zs       | No                |
| gen_qa        | Text                | Custom Dataset Evaluation – Lets you bring your own dataset for benchmarking,<br>comparing model outputs to reference answers with metrics such as ROUGE and<br>BLEU.                                                | all         | gen_qa   | No                |
| mmmu          | Multi-modal         | Massive Multidiscipline Multimodal Understanding (MMMU) – College-level<br>benchmark comprising multiple-choice and open-ended questions from 30<br>disciplines.                                                     | accuracy    | zs_cot   | Yes               |
| llm_judge     | Text                | LLM-as-a-Judge Preference Comparison – Uses a Nova Judge model to determine<br>preference between paired responses (B compared with A) for your prompts,<br>calculating the probability of B being preferred over A. | all         | judge    | No                |
| humaneval     | Text                | HumanEval<br>• A benchmark dataset designed to evaluate the code generation<br>capabilities of large language models                                                                                                 | pass@1      | zs       | No                |
| mm_llm_judge  | Multi-modal (image) | This new benchmark behaves the same as the text-based `llm_judge`<br>above. The only difference is that it supports image inference.                                                                                 | all         | judge    | No                |

The following `mmlu` subtasks are available:

```
`MMLU_SUBTASKS = [
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
]`
```

The following `bbh` subtasks are available:

```
`BBH_SUBTASKS = [
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
]`
```

The following `math` subtasks are available:

```
`MATH_SUBTASKS = [
 "algebra",
 "counting_and_probability",
 "geometry",
 "intermediate_algebra",
 "number_theory",
 "prealgebra",
 "precalculus",
]`
```
