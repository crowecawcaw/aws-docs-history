# Semantic Robustness

Evaluates how much your model output changes as the result of small, semantic-preserving changes
in the input. Foundation Model Evaluations (FMEval) measure how your model output changes as a
result of keyboard typos, random changes to uppercase, and random additions or deletions of white
spaces.

Amazon SageMaker AI supports running a semantic robustness evaluation from Amazon SageMaker Studio or using
the `fmeval` library.

- **Running evaluations in Studio:** Evaluation jobs
  created in Studio use pre-selected defaults to quickly evaluate model performance.
  Semantic robustness evaluations for open-ended generation cannot be created in Studio.
  They must be created using the `fmeval` library.
- **Running evaluations using the `fmeval`
  library:** Evaluation jobs created using the `fmeval` library offer
  expanded options to configure the model performance evaluation.

## Supported task type

The semantic robustness evaluation is supported for the following task types with their
associated built-in datasets. Users can also bring their own dataset. By default, SageMaker AI samples
100 random datapoints from the dataset for toxicity evaluation. When using
the `fmeval` library, this can be adjusted by passing the
`num_records` parameter to the `evaluate` method. For information
about customizing the factual knowledge evaluation using the `fmeval` library, see
[Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md").

| Task type             | Built-in datasets                                                                                                                                                                                                                                                                                                                                                                      | Notes |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Text summarization    | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3"),<br>[Government Report<br>Dataset](https://gov-report-data.github.io/ "https://gov-report-data.github.io/")                                                                                                                                                                |       |
| Question answering    | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions"), [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions"), [TriviaQA](http://nlp.cs.washington.edu/triviaqa/ "http://nlp.cs.washington.edu/triviaqa/") |       |
| Classification        | [Women's E-Commerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews")                                                                                                                                                                                     |       |
| Open-ended generation | [T-REx](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/"), [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold"), [WikiText-2](https://huggingface.co/datasets/wikitext/viewer/wikitext-2 "https://huggingface.co/datasets/wikitext/viewer/wikitext-2")                                                                   |       |

## Perturbation types

The semantic robustness evaluation makes one of the following three perturbations. You can select
the perturbation type when configuring the evaluation job. All three perturbations are adapted
from NL-Augmenter.

Example model input: `A quick brown fox jumps over the lazy dog`. 

- [Butter
  Fingers](https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/butter_fingers_perturbation "https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/butter_fingers_perturbation"): Typos introduced due to hitting adjacent keyboard key.

```
W quick brmwn fox jumps over the lazy dig
```

- [Random
  Upper Case](https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/random_upper_transformation/ "https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/random_upper_transformation/"): Changing randomly selected letters to upper-case.

```
A qUick brOwn fox jumps over the lazY dog
```

- [Whitespace
  Add Remove](https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/whitespace_perturbation "https://github.com/GEM-benchmark/NL-Augmenter/blob/c591130760b453b3ad09516849dfc26e721eeb24/nlaugmenter/transformations/whitespace_perturbation"): Randomly adding and removing whitespaces from the input.

```
A q uick bro wn fox ju mps overthe lazy dog
```

## Computed values

This evaluation measures the performance change between model output based on the original,
unperturbed input and model output based on a series of perturbed versions of the input. For
information about the prompt structure required for the evaluation,
see [Create an automatic model evaluation job in Studio](clarify-foundation-model-evaluate-auto-ui.md "clarify-foundation-model-evaluate-auto-ui.md").

The performance change is the average difference between the score of the original input and
the scores of the perturbed inputs. The scores measured to evaluate this performance change
depend on the task type:

### Summarization

For summarization tasks, semantic robustness measures the following scores when using the
perturbed input, as well as the Delta for each score. The Delta score represents the average
absolute difference between the score of the original input and the scores of the perturbed input.

- **Delta ROUGE score:** The average absolute difference in ROUGE
  score for original and perturbed inputs. The ROUGE scores are computed the same way as the ROUGE score in [Summarization](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization").
- **Delta METEOR score:** The average absolute difference
  in METEOR score for original and perturbed inputs. The METEOR scores are computed the
  same way as the METEOR score in [Summarization](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization").
- **Delta BERTScore:** The average absolute difference in
  BERTScore for original and perturbed inputs. The BERTScores are computed the same way as
  the BERTScore in [Summarization](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-summarization").

### Question answering

For question answering tasks, semantic robustness measures the following scores when using the
perturbed input, as well as the Delta for each score. The Delta score represents the average
absolute difference between the score of the original input and the scores of the perturbed input.

- **Delta F1 Over Words score:** The average absolute
  difference in F1 Over Words scores for original and perturbed inputs. The F1 Over Words
  scores are computed the same way as the F1 Over Words score in [Question answering](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa").
- **Delta Exact Match score:** The average absolute
  difference in Exact Match scores for original and perturbed inputs. The Exact Match
  scores are computed the same way as the Exact Match score in [Question answering](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa").
- **Delta Quasi Exact Match score:**The average absolute
  difference in Quasi Exact Match scores for original and perturbed inputs. The Quasi
  Exact Match scores are computed the same way as the Quasi Exact Match score in [Question answering](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa")
- **Delta Precision Over Words score:**The average
  absolute difference in Precision Over Words scores for original and perturbed inputs.
  The Precision Over Words scores are computed the same way as the Precision Over Words
  score in [Question answering](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa").
- **Delta Recall Over Words score:** The average absolute
  difference in Recall Over Words scores for original and perturbed inputs. The Recall
  Over Words scores are computed the same way as the Recall Over Words score in [Question answering](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-qa").

### Classification

For classification tasks, semantic robustness measures the accuracy when using the perturbed
input, as well as the Delta for each score. The Delta score represents the average absolute
difference between the score of the original input and the scores of the perturbed input.

- **Delta Accuracy score:**The average absolute difference
  in Accuracy scores for original and perturbed inputs. The Accuracy scores are computed
  the same way as the Accuracy score in [Classification](clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-classification "clarify-accuracy-evaluation.md#clarify-accuracy-evaluation-classification").

### Open-ended generation

Semantic robustness evaluations for open-ended generation cannot be created in Studio.
They must be created using the `fmeval` library with [GeneralSemanticRobustness](https://github.com/aws/fmeval/blob/91e675be24800a262faf8bf6e59f07522b5314ea/src/fmeval/eval_algorithms/general_semantic_robustness.py#L81C7-L81C32 "https://github.com/aws/fmeval/blob/91e675be24800a262faf8bf6e59f07522b5314ea/src/fmeval/eval_algorithms/general_semantic_robustness.py#L81C7-L81C32"). Instead of computing the difference in scores for
open-ended generation, the semantic robustness evaluation measures the dissimilarity in
model generations between original input and perturbed input. This dissimilarity is measured
using the following strategies:

- **\*[Word error
  rate](https://huggingface.co/spaces/evaluate-metric/wer "https://huggingface.co/spaces/evaluate-metric/wer")** (WER):\* Measures the syntactic difference between
  the two generations by computing the percentage of words that must be changed to convert
  the first generations into the second generation. For more information on the
  computation of WER, see the [HuggingFace article on Word
  Error Rate](https://huggingface.co/spaces/evaluate-metric/wer "https://huggingface.co/spaces/evaluate-metric/wer").
  - For example:
    - **Input 1**: “This is a cat”
    - **Input 2**: “This is a dog”
    - **Number of words that must be changed**: 1/4, or
      25%
    - **WER**: 0.25

- **BERTScore Dissimilarity (BSD):** Measures the semantic
  differences between the two generations by subtracting the BERTScore from 1. BSD may
  account for additional linguistic flexibility that isn’t included in WER because
  semantically similar sentences may be embedded closer to each other.
  - For example, while the WER is the same when generation 2 and generation 3 are individually
    compared to generation 1, the BSD score differs to account for the semantic meaning.
    - **gen1 (original input)**: `"It is pouring
down today"`
    - **gen2 (perturbed input 1)**: `"It is my
birthday today"`
    - **gen3 (perturbed input 2)** : `"It is very
rainy today"`
    - `WER(gen1, gen2)=WER(gen2, gen3)=0.4`
    - `BERTScore(gen1, gen2)=0.67`
    - `BERTScore(gen1, gen3)=0.92`
    - `BSD(gen1, gen2)= 1-BERTScore(gen1, gen2)=0.33`
    - `BSD(gen2 ,gen3)= 1-BERTScore(gen2, gen3)=0.08`

  - The following options are supported as part of the
    [GeneralSemanticRobustnessConfig](https://github.com/aws/fmeval/blob/91e675be24800a262faf8bf6e59f07522b5314ea/src/fmeval/eval_algorithms/general_semantic_robustness.py#L54C7-L54C38 "https://github.com/aws/fmeval/blob/91e675be24800a262faf8bf6e59f07522b5314ea/src/fmeval/eval_algorithms/general_semantic_robustness.py#L54C7-L54C38")
    parameter: 
    - `model_type_for_bertscore`: Name of the model to be used for scoring.
      BERTScore Dissimilarity currently only supports the following models:
      - "`microsoft/deberta-xlarge-mnli`"  (default)
      - "`roberta-large-mnli`"

**Non-deterministic models**

When the model generation strategy is non-deterministic, such as in LLMs with non-zero
temperature, the output can change even if the input is the same. In these cases, reporting
differences between the model output for the original and perturbed inputs could show artificially
low robustness. To account for the non-deterministic strategy, the semantic robustness evaluation
normalizes the dissimilarity score by subtracting the average dissimilarity between model output
based on the same input. 

`max(0,d−dbase​)`

- `d`: the dissimilarity score (Word Error Rate or BERTScore Dissimilarity)
  between the two generations.
- `dbase​`: dissimilarity between the model output on the same input.
