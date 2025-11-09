# Factual Knowledge

Evaluates the ability of language models to reproduce facts about the real world. Foundation
Model Evaluations (FMEval) can measure your model against your own custom dataset or use a
built-in dataset based on the [T-REx](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") open source dataset.

Amazon SageMaker AI supports running a factual knowledge evaluation from Amazon SageMaker Studio or using
the `fmeval` library.

- **Running evaluations in Studio:** Evaluation jobs
  created in Studio use pre-selected defaults to quickly evaluate model performance.
- **Running evaluations using the `fmeval` library:**
  Evaluation jobs created using the `fmeval` library offer expanded options to
  configure the model performance evaluation.

## Supported task type

The factual knowledge evaluation is supported for the following task types with their
associated built-in datasets. Users can also bring their own dataset. By default, SageMaker AI samples
100 random datapoints from the dataset for factual knowledge evaluation. When using
the `fmeval` library, this can be adjusted by passing the
`num_records` parameter to the `evaluate` method. For information
about customizing the factual knowledge evaluation using the `fmeval` library, see
[Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md").

| Task type             | Built-in datasets                                                                    | Notes                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Open-ended generation | [T-REx](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") | This dataset only supports the English language. To run this evaluation in any other<br>language, you must upload your own dataset. |

## Computed values

This evaluation averages a single binary metric across every prompt in the dataset. For
information about the prompt structure required for the evaluation,
see [Create an automatic model evaluation job in Studio](clarify-foundation-model-evaluate-auto-ui.md "clarify-foundation-model-evaluate-auto-ui.md"). For each prompt, the values correspond with the
following:

- `0`: The lower-cased expected answer is not part of the model response.
- `1`: The lower-cased expected answer is part of the model response. Some
  subject and predicate pairs can have more than one expected answer. In that case, either
  of the answers are considered correct.

## Example

- **Prompt**: `Berlin is the capital of`
- **Expected answer**: `Germany`.
- **Generated text**: `Germany, and is also its most
populous city`
- **Factual knowledge evaluation**: 1
