# Update training

job details (Studio)

Complete the following steps to update the details of a training job, created
externally or with SageMaker AI, associated with your model.

###### To update (and view) details related to the training job:

1. On the **Train** tab, view the status of the training
   job. The status is `Complete` if you added a training job to
   your model package and `Undefined` if not.
2. To view details related to your training job such as performance,
   hyperparameters, and identifying details, choose the
   **Train** tab.
3. To update and view details related to model performance, complete the
   following steps.
   1. Choose **Performance** in the left sidebar of
      the **Train** tab.
   2. View **Metrics** related to your training
      job. The **Performance** page lists metrics by
      name, value, and any notes you added related to the
      metric.
   3. (Optional) To add notes to existing metrics, complete the
      following steps.
      1. Choose the vertical ellipsis in the top right corner
         of the model version page, and choose
         **Edit**.
      2. Add notes to any of the listed metrics.
      3. At the top of the model version page, choose
         **Save** in the **Editing
         Model Version...** banner.

   4. View **Custom Metrics** related to your
      training job. Custom metrics are formatted similarly to
      metrics.
   5. (Optional) To add custom metrics, complete the following
      steps.
      1. Choose **Add**.
      2. Insert a name, value, and any optional notes for your
         new metric.

   6. (Optional) To remove custom metrics, choose the
      **Trash** icon next to the metric you want
      to remove.
   7. In the **Observations** text box, view any
      notes you added related to the performance of your training
      job.
   8. (Optional) To add or update observations, complete the
      following steps.
      1. Choose the vertical ellipsis in the top right corner
         of the model version page, and choose
         **Edit**.
      2. Add or update your notes in the
         **Observations** text box.
      3. At the top of the model version page, choose
         **Save** in the **Editing
         Model Version...** banner.

4. To update and view details related to model artifacts, complete the
   following steps.
   1. Choose **Artifacts** in the left sidebar of
      the **Train** tab.
   2. In the **Location (S3 URI)** field, view the
      Amazon S3 location of your training datasets.
   3. In the **Models** field, view the name and
      Amazon S3 locations of model artifacts from other models that you
      included in the training job.
   4. To update any of the fields in the
      **Artifacts** page, complete the following
      steps.
      1. Choose the vertical ellipsis in the top right of the
         model version page, and choose
         **Edit**.
      2. Enter new values in any of the fields.
      3. At the top of the model version page, choose
         **Save** in the **Editing
         Model Version...** banner.

5. To update and view details related to hyperparameters, complete the
   following steps.
   1. Choose **Hyperparameters** in the left
      sidebar of the **Train** tab.
   2. View the SageMaker AI provided and custom hyperparameters defined.
      Each hyperparameter is listed with its name and value.
   3. View the custom hyperparameters you added.
   4. (Optional) To add an additional custom hyperparameter,
      complete the following steps.
      1. Above the top right corner of the **Custom
         Hyperparameters** table, choose
         **Add**. A pair of new blank fields
         appears.
      2. Enter the name and value of the new custom
         hyperparameter. These values are automatically
         saved.

   5. (Optional) To remove a custom hyperparameter, choose the
      **Trash** icon to the right of the
      hyperparameter.

6. To update and view details related to the training job environment,
   complete the following steps.
   1. Choose **Environment** in the left sidebar of
      the **Train** tab.
   2. View the Amazon ECR URI locations for any training job containers
      added by SageMaker AI (for a SageMaker training job) or by you (for a custom
      training job).
   3. (Optional) To add an additional training job container, choose
      **Add**, and then enter the URI of the new
      training container.

7. To update and view the training job name and the Amazon Resource Names
   (ARN) for the training job, complete the following steps.
   1. Choose **Details** in the left sidebar of the
      **Train** tab.
   2. View the training job name and ARN of the training job.
