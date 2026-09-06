

# Evaluation
<a name="customizing-models-evaluation"></a>

After training, evaluation confirms that your customized model improves on the metrics that matter for your use case, helping you catch regressions before deployment and compare techniques objectively. Evaluation is available through both [Serverless](customize-model.md) and [Recipes](customizing-models-infrastructure.md) paths.

## Serverless evaluation
<a name="evaluation-serverless"></a>

Submit evaluation jobs through the same [Serverless](customize-model.md) infrastructure used for training. Available via **Studio UI** (Jobs → Model evaluation) or Python SDK.

For detailed instructions, see the evaluation workflows in [Serverless model customization](customize-model.md).

## SageMaker AI Training Jobs and HyperPod evaluation
<a name="evaluation-self-managed"></a>

Run evaluation using **Recipes** with the following evaluation types:

Deterministic evaluation  
Benchmark your model on standard tasks including *MMLU*, *MMLU Pro*, *BBH*, *GPQA*, *MATH*, and *IFEval*. Supports zero-shot, few-shot, and chain-of-thought strategies.

LLM-as-Judge evaluation  
Use another LLM to evaluate your model's outputs on subjective criteria such as correctness, completeness, faithfulness, and helpfulness.

Custom dataset evaluation  
Evaluate on your own dataset using custom metrics or preset reward functions (`prime_math`, `prime_code`).

For evaluation recipes and configuration, see [SageMaker AI Recipes documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html).