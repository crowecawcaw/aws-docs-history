

# Update an evaluation job (Studio)
<a name="model-registry-details-studio-evaluate-update"></a>

Complete the following steps to update the details of an evaluation job, created externally or with SageMaker AI, associated with your model.

**To update (and view) details related to the evaluation job:**

1. On the **Evaluate** tab, view the status of the evaluation job. The status is `Complete` if you added an evaluation job to your model package and `Undefined` if not.

1. To view details related to your evaluation job, such as performance and artifacts location, choose the **Evaluate** tab.

1. To update and view details related to model performance during evaluation, complete the following steps.

   1. Choose **Performance** in the **Evaluate** tab sidebar.

   1. View metrics related to your evaluation job in the **Metrics** list. The **Metrics** list displays the individual metrics by name, value, and any notes you added related to the metric.

   1. In the **Observations** text box, view any notes you added related to the performance of your evaluation job.

   1. To update any of the **Notes** fields for any metric or the **Observations** field, complete the following steps.

      1. Choose the vertical ellipsis in the top right of the model version page, and choose **Edit**.

      1. Enter notes for any metric or in the **Observations** text box.

      1. At the top of the model version page, choose **Save** in the **Editing Model Version...** banner.

1. To update and view details related to your evaluation job datasets, complete the following steps.

   1. Choose **Artifacts** in the left sidebar of the **Evaluate** page.

   1. View datasets used in your evaluation job.

   1. (Optional) To add a dataset, choose **Add** and enter an Amazon S3 URI to the dataset.

   1. (Optional) To remove a dataset, choose the **Trash** icon next to the dataset you want to remove.

1. To view the job name and evaluation job ARN, choose **Details**.