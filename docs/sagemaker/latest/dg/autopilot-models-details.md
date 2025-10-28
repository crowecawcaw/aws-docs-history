# View model details

Autopilot generates details about the candidate models that you can obtain. These details
include the following:

- A plot of the aggregated SHAP values that indicate the importance of each
  feature. This helps explain your models predictions.
- The summary statistics for various training and validation metrics, including
  the objective metric.
- A list of the hyperparameters used to train and tune the model.
  To view model details after running an Autopilot job, follow these steps:

1. Choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ) from the left navigation pane to view the top-level
   **Amazon SageMaker Studio Classic** navigation menu.
2. Select the **AutoML** card from the main working area. This
   opens a new **Autopilot** tab.
3. In the **Name** section, select the Autopilot job that has the
   details that you want to examine. This opens a new **Autopilot
   job** tab.
4. The **Autopilot job** panel lists the metric values including
   the **Objective** metric for each model under **Model
   name**. The **Best model** is listed at the top of
   the list under **Model name** and is also highlighted in the
   **Models** tab.
   1. To review model details, select the model that you are interested in
      and select **View model details**. This opens a new
      **Model Details** tab.

5. The **Model Details** tab is divided into four
   subsections.
   1. The top of the **Explainability** tab contains a plot
      of aggregated SHAP values that indicate the importance of each feature.
      Following that are the metrics and hyperparameter values for this model.
   2. The **Performance** tab contains metrics statistics a
      confusion matrix.
   3. The **Artifacts** tab contains information about
      model inputs, outputs, and intermediate results.
   4. The **Network** tab summarizes your network isolation
      and encryption choices.

###### Note

Feature importance and information in the **Performance**
tab is only generated for the **Best model**.

For more information about how the SHAP values help explain predictions based
on feature importance, see the whitepaper [Understanding the model explainability](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf"). Additional information is
also available in the [Model Explainability](clarify-model-explainability.md "clarify-model-explainability.md") topic in the SageMaker AI Developer
Guide.
