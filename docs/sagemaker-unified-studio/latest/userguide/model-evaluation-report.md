# Review a model model evaluation job in Amazon Bedrock

The results of a model evaluation job are presented in a report, and include key metrics
that can help you assess the model performance and effectiveness. In your model evaluation
report, you will see an evaluation summary and sections for each of the metrics that you
chose for the evaluation job. responses.

###### Topics

- [Viewing a model evaluation report](#model-evaluation-report-procedure "#model-evaluation-report-procedure")
- [Understanding a model evaluation report](#model-evaluation-report-understanding "#model-evaluation-report-understanding")

## Viewing a model evaluation report

###### To view a model evaluation report

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. From the navigation pane, choose **Build** and then
   **Model evaluations**.
7. In the **Model evaluation jobs** table choose the name of
   the model evaluation job you want to review. The model evaluation card opens.

## Understanding a model evaluation report

In the **Evaluation summary** you can see the task type and tasks metrics that the
evaluation job calculated.

For each metric, the report contains the dataset, the calculated metric value for the dataset, the total number of prompts in
the dataset, and how many of those prompts received. How the metric value is
calculated changes based on the task type and the metrics you selected.

In all semantic robustness related metrics, Amazon Bedrock in SageMaker Unified Studio perturbs prompts in the following
ways: convert text to all lower cases, keyboard typos, converting numbers to words,
random changes to upper case and random addition/deletion of whitespaces.

###### How each available metric is calculated when applied to the general text

generation task type

- **Accuracy**: For this metric, the value is
  calculated using real world knowledge score (RWK score). RWK score examines
  the model’s ability to encode factual knowledge about the real world. A high
  RWK score indicates that your model is being accurate.
- **Robustness**: For this metric, the value is
  calculated using semantic robustness. Which is calculated using word error
  rate. Semantic robustness measures how much the model output changes as a
  result of minor, semantic preserving perturbations, in the input. Robustness
  to such perturbations is a desirable property, and thus a low semantic
  robustness score indicated your model is performing well.

The perturbation types we will consider are: convert text to all lower
cases, keyboard typos, converting numbers to words, random changes to upper
case and random addition/deletion of whitespaces. Each prompt in your
dataset is perturbed approximately 5 times. Then, each perturbed response is
sent for inference, and used to calculate robustness scores
automatically.

- **Toxicity**: For this metric, the value is
  calculated using toxicity from the detoxify algorithm. A low toxicity value
  indicates that your selected model is not producing large amounts of toxic
  content. To learn more about the detoxify algorithm and see how toxicity is
  calculated, see the [detoxify algorithm](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify") on GitHub.

###### How each available metric is calculated when applied to the text

summarization task type

- **Accuracy**: For this metric, the value is
  calculated using BERT Score. BERT Score is calculated using pre-trained
  contextual embeddings from BERT models. It matches words in candidate and
  reference sentences by cosine similarity.
- **Robustness**: For this metric, the value
  calculated is a percentage. It calculated by taking (Delta BERTScore /
  BERTScore) x 100. Delta BERTScore is the difference in BERT Scores between a
  perturbed prompt and the original prompt in your dataset. Each prompt in
  your dataset is perturbed approximately 5 times. Then, each perturbed
  response is sent for inference, and used to calculate robustness scores
  automatically. A lower score indicates the selected model is more
  robust.
- **Toxicity**: For this metric, the value is
  calculated using toxicity from the detoxify algorithm. A low toxicity value
  indicates that your selected model is not producing large amounts of toxic
  content. To learn more about the detoxify algorithm and see how toxicity is
  calculated, see the [detoxify algorithm](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify") on GitHub.

###### How each available metric is calculated when applied to the question and

answer task type

- **Accuracy**: For this metric, the value
  calculated is F1 score. F1 score is calculated by dividing the precision
  score (the ratio of correct predictions to all predictions) by the recall
  score (the ratio of correct predictions to the total number of relevant
  predictions). The F1 score ranges from 0 to 1, with higher values indicating
  better performance.
- **Robustness**: For this metric, the value
  calculated is a percentage. It is calculated by taking (Delta F1 / F1) x

100.  Delta F1 is the difference in F1 Scores between a perturbed prompt and
      the original prompt in your dataset. Each prompt in your dataset is
      perturbed approximately 5 times. Then, each perturbed response is sent for
      inference, and used to calculate robustness scores automatically. A lower
      score indicates the selected model is more robust.

- **Toxicity**: For this metric, the value is
  calculated using toxicity from the detoxify algorithm. A low toxicity value
  indicates that your selected model is not producing large amounts of toxic
  content. To learn more about the detoxify algorithm and see how toxicity is
  calculated, see the [detoxify algorithm](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify") on GitHub.

###### How each available metric is calculated when applied to the text

classification task type

- **Accuracy**: For this metric, the value
  calculated is accuracy. Accuracy is a score that compares the predicted
  class to its ground truth label. A higher accuracy indicates that your model
  is correctly classifying text based on the ground truth label
  provided.
- **Robustness**: For this metric, the value
  calculated is a percentage. It is calculated by taking (delta classification
  accuracy score / classification accuracy score) x 100. Delta classification
  accuracy score is the difference between the classification accuracy score
  of the perturbed prompt and the original input prompt. Each prompt in your
  dataset is perturbed approximately 5 times. Then, each perturbed response is
  sent for inference, and used to calculate robustness scores automatically. A
  lower score indicates the selected model is more robust.

In the **Job configuration summary**, you can see the model and the inference
parameters that the job used.
