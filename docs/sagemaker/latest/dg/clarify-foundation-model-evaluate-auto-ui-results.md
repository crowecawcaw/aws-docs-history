# Understand the

results of an automatic evaluation job

When you automatic model evaluation job completes the results are saved in Amazon S3. The sections below describe the files generated and how to interpret them.

## Interpreting the `output.json` file's structure

The `output.json` file contains aggregate scores for your selected datasets and metrics.

The following is an example output

```
{
    "evaluations": [{
        "evaluation_name": "factual_knowledge",
        "dataset_name": "trex",
		## The structure of the prompt template changes based on the foundation model selected
		"prompt_template": "<s>[INST] <<SYS>>Answer the question at the end in as few words as possible. Do not repeat the question. Do not answer in complete sentences.<</SYS> Question: $feature [/INST]",
        "dataset_scores": [{
            "name": "factual_knowledge",
            "value": 0.2966666666666667
        }],
        "category_scores": [{
                "name": "Author",
                "scores": [{
                    "name": "factual_knowledge",
                    "value": 0.4117647058823529
                }]
            },
				....
            {
                "name": "Capitals",
                "scores": [{
                    "name": "factual_knowledge",
                    "value": 0.2857142857142857
                }]
            }
        ]
    }]
}
```

## Interpreting the instance-wise results file's structure

One`evaluation_name`\_`dataset_name`.jsonl file containing instance-wise results for each jsonlines request. If you had `300` requests in your jsonlines input data, this jsonlines output file contains `300` responses. The output file contains the request made to your model followed by the score for that evaluation. An example instance-wide output follows.

## Interpreting the report

An **Evaluation Report** contains the results of your foundation model evaluation job. The content of the evaluation report depends on the kind of task you used to evaluate your model. Each report contains the following sections:

1. The **overall scores** for
   each successful evaluation under the evaluation task. As an
   example of one evaluation with one dataset, if you evaluated
   your model for a classification task for Accuracy and
   Semantic Robustness, then a table summarizing the evaluation
   results for Accuracy and Accuracy Semantic Robustness
   appears at the top of your report. Other evaluations with
   other datasets may be structured differently.
2. The configuration for your evaluation job including the
   model name, type, which evaluation methods were used and
   what datasets your model was evaluated against.
3. A **Detailed Evaluation Results** section
   that summarizes the evaluation algorithm, provides
   information about and links to any built-in datasets, how
   scores are calculated, and tables showing some sample data
   with their associated scores.
4. A **Failed Evaluations** section that
   contains a list of evaluations that did not complete. If no
   evaluations failed, this section of the report is
   omitted.
