# Using prompt datasets and available evaluation dimensions in model evaluation jobs

The following sections provide an overview of how to use automatic and human-based
model evaluation jobs.

## Model evaluation

tasks

In a model evaluation job, an evaluation task is a task you want the model to
perform based on information found in the prompts.

You can choose one task type per model evaluation job. Use the following sections
to learn more about each task type. Each section also includes a list of available
built-in datasets and their corresponding metrics that can be used only in automatic
model evaluation jobs.

### Open-ended

generation

Open-ended text generation is a foundation model task that generates natural
language responses to prompts that don't have a pre-defined structure, such as
general-purpose queries to a chatbot. For open-ended text generation, Foundation Model Evaluations
(FMEval) can evaluate your model along the following dimensions.

- **Factual knowledge** – Evaluates
  how well your model encodes factual knowledge. FMEval can measure your
  model against your own custom dataset or use a built-in dataset based on
  the [TREX](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") open source dataset.
- **Semantic robustness** –
  Evaluates how much your model output changes as the result of small,
  semantic-preserving changes in the input. FMEval measures how your model
  output changes as a result of keyboard typos, random changes to
  uppercase, and random additions or deletions of white spaces.
- **Prompt stereotyping** – Measures
  the probability of your model encoding biases in its response. These
  biases include those for race, gender, sexual orientation, religion,
  age, nationality, disability, physical appearance, and socioeconomic
  status. FMEval can measure your model responses against your own custom
  dataset or use a built-in dataset based on the [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs "https://github.com/nyu-mll/crows-pairs") open source challenge
  dataset.
- **Toxicity** – Evaluates text
  using toxicity detection models. FMEval checks your model for sexual
  references, rude, unreasonable, hateful or aggressive comments,
  profanity, insults, flirtations, attacks on identities, and threats.
  FMEval can measure your model against your own custom dataset or use
  built-in datasets based on the [RealToxicityPrompts](https://arxiv.org/abs/2009.11462 "https://arxiv.org/abs/2009.11462"),
  RealToxicityPromptsChallenging, and [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold") datasets.

RealToxicityPromptsChallenging is a subset of
RealToxicityPrompts that is used to test the limits
of a large language model (LLM). It also identifies areas where LLMs are
vulnerable to generating toxic text.

You can evaluate your model with the following toxicity
detectors:

    + [UnitaryAI Detoxify-unbiased](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify")
     – A multi-label text classifier trained on [Toxic Comment Classification
     Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge "https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge") and [Jigsaw Unintended Bias in Toxicity
     Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification "https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification"). The model provides
     `7` scores for the following classes: toxicity,
     severe toxicity, obscenity, threat, insult, sexual explicit and
     identity attack.
    + [Toxigen-roberta](https://github.com/microsoft/TOXIGEN "https://github.com/microsoft/TOXIGEN") – A
     binary RoBERTa-based text classifier fine-tuned
     on the ToxiGen dataset. The
     ToxiGen dataset contains sentences with
     subtle and implicit toxicity pertaining to minority
     groups.

### Text

summarization

Text summarization is used for tasks, such as creating summaries of news,
legal documents, academic papers, content previews, and content curation. The
following can influence the quality of responses: ambiguity, coherence, bias,
fluency of the text used to train the foundation model, and information loss,
accuracy, relevance, or context mismatch. FMEval can evaluate your model against
your own custom dataset or use built-in datasets based on the [Government Report
Dataset](https://gov-report-data.github.io/ "https://gov-report-data.github.io/"), and [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") datasets. For text summarization, FMEval can
evaluate your model for the following:

- _Accuracy_ – A numerical score
  indicating the similarity of the summarization to a reference summary
  that is accepted as a gold standard. A high numerical score indicates
  that the summary is of high quality. A low numerical score indicates a
  poor summary. The following metrics are used to evaluate the accuracy of
  a summarization:
  - [ROUGE-N](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge") – Computes
    N-gram overlaps between the reference and
    model summary.
  - [Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor") – Computes the
    word overlap between the reference and model summary while also
    accounting for rephrasing.
  - [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore") – Computes and
    compares sentence embeddings for the summarization and
    reference. FMEval uses the [roberta-large-mnli](https://huggingface.co/roberta-large-mnli "https://huggingface.co/roberta-large-mnli") or [microsoft/deberta-xlarge-mnli](https://huggingface.co/microsoft/deberta-xlarge-mnli "https://huggingface.co/microsoft/deberta-xlarge-mnli") models to compute the
    embeddings.

- _Toxicity_ – Scores for
  generated summaries that are calculated using a toxicity detector model.
  For additional information, see the _Toxicity_ section in the previous for _Open-ended generation_ task for
  details.
- _Semantic robustness_ – A
  measure of how much the quality of your model’s text summary changes as
  the result of small, semantic-preserving changes in the input. Examples
  of these changes include typos, random changes to uppercase, and random additions or
  deletions of white spaces. Semantic robustness uses the absolute
  difference in accuracy between a text summary that is unperturbed and
  one that is perturbed. The accuracy algorithm uses the [ROUGE-N](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge"), [Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor"), and [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore") metrics, as detailed
  previously in this section.

### Question

answering

Question answering is used for tasks such as generating automatic help-desk
responses, information retrieval, and e-learning. FMEval can evaluate your model
against your own custom dataset or use built-in datasets based on the [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions"), [TriviaQA](http://nlp.cs.washington.edu/triviaqa/ "http://nlp.cs.washington.edu/triviaqa/"), and [Natural Questions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") datasets. For question
answering, FMEval can evaluate your model for the following:

- _Accuracy_ – An average score
  comparing the generated response to the question answer pairs given in
  the references. The score is averaged from the following methods:
  - _Exact match_ – A binary
    score of `1` is assigned to an exact match, and
    `0` otherwise.
  - _Quasi-exact match_ – A
    binary score of `1` is assigned to a match after punctuation and grammatical articles (such as the, a, and) have been removed (normalization).
  - _F1 over words_ – The F1
    score, or harmonic mean of precision and recall between the
    normalized response and reference. The F1 score is equal to
    twice precision multiplied by recall divided by the sum of
    precision (P) and recall (R), or F1 = (2\*P\*R) / (P + R).

  In the previous calculation, precision is defined as the
  number of true positives (TP) divided by the sum of true
  positives and false positives (FP), or P = (TP)/(TP+FP).

  Recall is defined as the number of true positives divided by
  the sum of true positives and false negatives (FN), or R =
  (TP)/(TP+FN).

  A higher F1 over words score indicates higher quality
  responses.

- _Semantic robustness_ – A
  measure of how much the quality of your model’s text summary changes as
  the result of small, semantic-preserving changes in the input. Examples
  of these changes include keyboard typos, the inaccurate conversion of
  numbers to words, random changes to uppercase, and random additions or
  deletions of white spaces. Semantic robustness uses the absolute
  difference in accuracy between a text summary that is unperturbed and
  one that is perturbed. Accuracy is measured using exact-match,
  quasi-exact match and F1 over words, as described previously.
- _Toxicity_ – Scores evaluate
  generated answers using a toxicity detector model. For additional
  information, see the _Toxicity_ section
  in the previous for _Open-ended
  generation_ task for details.

### Classification

Classification is used to categorize text into pre-defined categories.
Applications that use text classification include content recommendation, spam
detection, language identification and trend analysis on social media.
Imbalanced, ambiguous, noisy data, bias in labeling are some issues that can
cause errors in classification. FMEval evaluates your model against a built-in
dataset based on the [Women’s ECommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") dataset,
and/or against your own prompt datasets for the following.

- **Accuracy** – A score that
  compares the predicted class to its label. Accuracy is measured using
  the following metrics:
  - **Classification accuracy**
    – A binary score of `1` if the predicted label
    equals the true label, and `0` otherwise.
  - **Precision** – The ratio
    of true positives to all positives, calculated over the entire
    dataset. Precision is an appropriate measure when reducing false
    positives is important. The score for each data point can be
    aggregated using the following values for the
    `multiclass_average_strategy` parameter. Each parameter is listed in the following example.
  - **Recall** – the ratio of
    true positives to the sum of true positives and false negatives,
    calculated over the entire dataset. Recall is an appropriate
    measure when reducing false negatives is important. The scores
    for each data point can be aggregated using the following values
    for the `multiclass_average_strategy`
    parameter.
    - **`micro`**
      (default) – The sum of the true positives divided
      by the sum of true positives and false negatives for all
      classes. This aggregation type gives a measure of the
      overall predictive accuracy of your model, while
      considering all classes equally. For example, this
      aggregation can assess your model’s ability to correctly
      classify patients with any disease including rare
      diseases, because it gives equal weight to all
      classes.
    - **`macro`**
      – The sum of recall values calculated for each
      class divided by the number of classes. This aggregation
      type gives a measure of the predictive accuracy of your
      model for each class, with equal weight to each class.
      For example, this aggregation can assess your model’s
      ability to predict all diseases, regardless of the
      prevalence or rarity of each condition.
    - **`samples`**
      (multi-class classification only) – The ratio of
      the sum of true positives over all samples to the sum of
      true positives and false negatives for all samples. For
      multi-class classification, a sample consists of a set
      of predicted responses for each class. This aggregation
      type gives a granular measure of each sample’s recall
      for multi-class problems. For example, because
      aggregating by samples treats each sample equally, this
      aggregation can assess your model’s ability to predict a
      correct diagnosis for a patient with a rare disease
      while also minimizing false negatives.
    - **`weighted`**
      – The weight for one class multiplied by the
      recall for the same class, summed over all classes. This
      aggregation type provides a measure of overall recall
      while accommodating varying importances among classes.
      For example, this aggregation can assess your model’s
      ability to predict a correct diagnosis for a patient and
      give a higher weight to diseases that are
      life-threatening.
    - **`binary`**
      – The recall calculated for the class that is
      specified by the value `pos_label`. This
      aggregation type ignores the unspecified class, and
      gives overall predictive accuracy for a single class.
      For example, this aggregation can assess your model’s
      ability to screen a population for a specific highly
      contagious life-threatening disease.
    - **`none`**
      – The recall calculated for each class.
      Class-specific recall can help you address class
      imbalances in your data when the penalty for error
      varies significantly between classes. For example, this
      aggregation can assess how well your model can identify
      all patients that may have a specific disease.

  - **Balanced classification
    accuracy** (BCA) – The sum of recall and the
    true negative rate divided by `2` for binary
    classification. The true negative rate is the number of true
    negatives divided by the sum of true negatives and false
    positives. For multi-class classification, BCA is calculated as
    the sum of recall values for each class divided by the number of
    classes. BCA can help when the penalty for predicting both false
    positives and false negatives is high. For example, BCA can
    assess how well your model can predict a number of highly
    contagious lethal diseases with intrusive treatments.

- **Semantic robustness** –
  Evaluates how much your model output changes as the result of small,
  semantic-preserving changes in the input. FMEval measures your model
  output as a result of keyboard typos, random changes to uppercase, and
  random additions or deletions of white spaces. Semantic robustness
  scores the absolute difference in accuracy between a text summary that
  is unperturbed and one that is perturbed.

## Types of

foundation model evaluations

The following sections provide details about both human and algorithmic types of
evaluations for your foundation model.

### Human

evaluations

To evaluate your model by a human, you must define the metrics and associated
metric types. If you want to evaluate more than one model, you can use a
comparative or individual rating mechanism. If you want to evaluate one model,
you must use an individual rating mechanism. The following rating mechanisms can
be applied to any text-related task:

- (Comparative) **Likert scale - comparison** –
  A human evaluator will indicate their preference between two responses
  on a 5-point Likert scale according to your instructions. In the final
  report, the results will be shown as a histogram of ratings by
  preference strength over your whole dataset. Define the important points
  of the 5-point scale in your instructions so that your evaluators know
  how to rate the responses according to your expectations.
- (Comparative) **Choice buttons** – Allows a
  human evaluator to indicate one preferred response over another response
  using radio buttons, according to your instructions. The results in the
  final report will be shown as a percentage of responses that workers
  preferred for each model. Explain your evaluation method clearly in the
  instructions.
- (Comparative) **Ordinal rank** – Allows a
  human evaluator to rank their preferred responses to a prompt in order,
  starting at 1, and according to your instructions. In the final report,
  the results display as a histogram of the rankings from the evaluators
  over the whole dataset. Make sure that you define what a rank of
  `1` means in your instructions.
- (Individual) **Thumbs up/down** – Allows a
  human evaluator to rate each response from a model as acceptable or
  unacceptable according to your instructions. In the final report, the
  results show a percentage of the total number of ratings by evaluators
  that received a thumbs up rating for each model. You can use this rating
  method to evaluate one or more models. If you use this in an evaluation
  that contains two models, the UI presents your work team with a thumbs
  up or down option for each model response. The final report will show
  the aggregated results for each model individually. Define what is an
  acceptable response in your instructions to your work team.
- (Individual) **Likert scale - individual** –
  Allows a human evaluator to indicate how strongly they approve of the
  model response, based on your instructions, on a 5-point Likert scale.
  In the final report, the results display a histogram of the 5-point
  ratings from the evaluators over your whole dataset. You can use this
  rating method for an evaluation containing one or more models. If you
  select this rating method in an evaluation that contains more than one
  model, a 5-point Likert scale is presented to your work team for each
  model response. The final report will show the aggregated results for
  each model individually. Define the important points on the 5-point
  scale in your instructions so that your evaluators know how to rate the
  responses according to your expectations.

### Automatic evaluations

Automatic evaluations can leverage built-in datasets and algorithms, or you
can bring your own dataset of prompts that are specific to your use case. The
built-in datasets vary for each task and are listed in the following sections.
For a summary of tasks and their associated metrics and datasets, see the table
in the following **Foundation model summary
evaluation** section.

## Foundation model

evaluation summary

The following table summarizes all of the evaluation tasks, metrics, and built-in
datasets for both human and automatic evaluations.

| Task                  | Human evaluations                                                               | Human metrics                                                                              | Automatic evaluations | Automatic metrics                | Automatic built-in datasets        |
| --------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------- | -------------------------------- | ---------------------------------- |
| Open-ended generation | Fluency, Coherence, Toxicity, Accuracy, Consistency,<br>Relevance, User-defined | Preference rate, Preference strength, Preference rank,<br>Approval rate, Approval strength | Factual knowledge     |                                  | TREX                               |
|                       |                                                                                 |                                                                                            | Semantic robustness   |                                  | TREX                               |
|                       |                                                                                 |                                                                                            |                       |                                  | BOLD                               |
|                       |                                                                                 |                                                                                            |                       |                                  | WikiText                           |
|                       |                                                                                 |                                                                                            | Prompt stereotyping   |                                  | CrowS-Pairs                        |
|                       |                                                                                 |                                                                                            | Toxicity              |                                  | RealToxicityPrompts                |
|                       |                                                                                 |                                                                                            |                       |                                  | BOLD                               |
| Text summarization    |                                                                                 |                                                                                            | Accuracy              | ROUGE-N                          | Government Report Dataset          |
|                       |                                                                                 |                                                                                            |                       | BERTScore                        | Gigaword                           |
|                       |                                                                                 |                                                                                            |                       |                                  | Government Report Dataset          |
|                       |                                                                                 |                                                                                            |                       |                                  | Gigaword                           |
|                       |                                                                                 |                                                                                            |                       |                                  | Government Report Dataset          |
|                       |                                                                                 |                                                                                            |                       |                                  | Gigaword                           |
| Question answering    |                                                                                 |                                                                                            | Accuracy              | Exact match                      | BoolQ                              |
|                       |                                                                                 |                                                                                            |                       | Quasi exact match                | NaturalQuestions                   |
|                       |                                                                                 |                                                                                            |                       | F1 over words                    | TriviaQA                           |
|                       |                                                                                 |                                                                                            | Semantic robustness   |                                  | BoolQ                              |
|                       |                                                                                 |                                                                                            |                       |                                  | NaturalQuestions                   |
|                       |                                                                                 |                                                                                            |                       |                                  | TriviaQA                           |
|                       |                                                                                 |                                                                                            | Toxicity              |                                  | BoolQ                              |
|                       |                                                                                 |                                                                                            |                       |                                  | NaturalQuestions                   |
|                       |                                                                                 |                                                                                            |                       |                                  | TriviaQA                           |
| Text classification   |                                                                                 |                                                                                            | Accuracy              | Classification accuracy          | Women's Ecommerce Clothing Reviews |
|                       |                                                                                 |                                                                                            |                       | Precision                        | Women's Ecommerce Clothing Reviews |
|                       |                                                                                 |                                                                                            |                       | Recall                           | Women's Ecommerce Clothing Reviews |
|                       |                                                                                 |                                                                                            |                       | Balanced classification accuracy | Women's Ecommerce Clothing Reviews |
|                       |                                                                                 |                                                                                            | Semantic robustness   |                                  | Women's Ecommerce Clothing Reviews |
