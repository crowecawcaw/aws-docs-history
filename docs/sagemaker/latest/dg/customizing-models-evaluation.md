# Evaluation

After training, evaluation confirms that your customized model improves on the metrics
that matter for your use case, helping you catch regressions before deployment and compare
techniques objectively. Evaluation is available through both
[Serverless](customize-model.md "customize-model.md") and
[Recipes](customizing-models-infrastructure.md "customizing-models-infrastructure.md") paths.

## Serverless evaluation

Submit evaluation jobs through the same
[Serverless](customize-model.md "customize-model.md") infrastructure used for training.
Available via **Studio UI**
(Jobs → Model evaluation) or Python SDK.

For detailed instructions, see the evaluation workflows in
[Serverless model customization](customize-model.md "customize-model.md").

## SageMaker AI Training Jobs and HyperPod evaluation

Run evaluation using **Recipes** with the following
evaluation types:

Deterministic evaluation
Benchmark your model on standard tasks including
_MMLU_, _MMLU Pro_,
_BBH_, _GPQA_,
_MATH_, and _IFEval_. Supports
zero-shot, few-shot, and chain-of-thought strategies.

LLM-as-Judge evaluation
Use another LLM to evaluate your model's outputs on subjective
criteria such as correctness, completeness, faithfulness, and
helpfulness.

Custom dataset evaluation
Evaluate on your own dataset using custom metrics or preset
reward functions (`prime_math`,
`prime_code`).

For evaluation recipes and configuration, see
[SageMaker AI Recipes
documentation](sagemaker-hyperpod-recipes.md "sagemaker-hyperpod-recipes.md").
