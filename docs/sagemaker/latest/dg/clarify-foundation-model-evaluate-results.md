# Understand the results of your model

evaluation job

Use the following sections to learn how to interpret the results of your model evaluation job. The output JSON data saved in Amazon S3 for both automatic and human based model evaluation jobs are different. You can find where the results of a job are saved in Amazon S3 using Studio. To do so, open the **Model evaluations** home page in Studio, and choose your job from the table.

## Seeing the results of model evaluation in Studio

When your model evaluation job is complete, you can see how your model performed against the dataset that you provided using the following steps:

1. From the Studio navigation pane, select
   **Jobs**, and then select **Model
   Evaluation**.
2. In the **Model Evaluations** page, successfully
   submitted jobs appear in a list. The list includes job name, status,
   model name, evaluation type, and the date it was created.
3. If your model evaluation completed successfully, you can click on the
   job name to see a summary of the evaluation results.
4. To view your human analysis report, select the name of the job that
   you want to examine.

For information about interpreting the model evaluation results, see the topic that
corresponds to the type of model evaluation job whose results you want to interpret:

- [Understand the results
  of a human evaluation job](clarify-foundation-model-evaluate-results-human.md "clarify-foundation-model-evaluate-results-human.md")
- [Understand the
  results of an automatic evaluation job](clarify-foundation-model-evaluate-auto-ui-results.md "clarify-foundation-model-evaluate-auto-ui-results.md")
