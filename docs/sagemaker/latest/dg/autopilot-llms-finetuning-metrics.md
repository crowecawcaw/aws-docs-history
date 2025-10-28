# Metrics for fine-tuning large language

models in Autopilot

The following section describes the metrics that you can use to understand your fine-tuned
large language models (LLMs). Using your dataset, Autopilot directly fine-tunes a target LLM to enhance a
default objective metric, the cross-entropy loss.

Cross-entropy loss is a widely used metric to assess the dissimilarity between the
predicted probability distribution and the actual distribution of words in the training data.
By minimizing cross-entropy loss, the model learns to make more accurate and contextually
relevant predictions, particularly in tasks related to text generation.

After fine-tuning an LLM you can evaluate the quality of its generated text using a range
of ROUGE scores. Additionally, you can analyze the perplexity and cross-entropy training and
validation losses as part of the evaluation process.

- Perplexity loss measures how well the model can predict the next word in a sequence of
  text, with lower values indicating a better understanding of the language and context.
- Recall-Oriented Understudy for Gisting Evaluation (ROUGE) is a set of metrics used in
  the field of natural language processing (NLP) and machine learning to evaluate the
  quality of machine-generated text, such as text summarization or text generation. It
  primarily assesses the similarities between the generated text and the ground truth
  reference (human-written) text of a validation dataset. ROUGE measures are designed to
  assess various aspects of text similarity, including the precision and recall of n-grams
  (contiguous sequences of words) in the system-generated and reference texts. The goal is
  to assess how well a model captures the information present in the reference text.

There are several variants of ROUGE metrics, depending on the type of n-grams used and
the specific aspects of text quality being evaluated.

The following list contains the name and description of the ROUGE metrics available
after the fine-tuning of large language models in Autopilot.

**`ROUGE-1`, `ROUGE-2`**

ROUGE-N, the primary ROUGE metric, measures the overlap of n-grams between the
system-generated and reference texts. ROUGE-N can be adjusted to different values of
`n` (here `1` or `2`) to evaluate how well the
system-generated text captures the n-grams from the reference text.

**`ROUGE-L`**

ROUGE-L (ROUGE-Longest Common Subsequence) calculates the longest common
subsequence between the system-generated text and the reference text. This variant
considers word order in addition to content overlap.

**`ROUGE-L-Sum`**

ROUGE-L-SUM (Longest Common Subsequence for Summarization) is designed for the
evaluation of text summarization systems. It focuses on measuring the longest common
subsequence between the machine-generated summary and the reference summary.
ROUGE-L-SUM takes into account the order of words in the text, which is important in
text summarization tasks.
