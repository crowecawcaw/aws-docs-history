# Stop a Training Job in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You can stop a training job with the Amazon SageMaker Studio Classic UI. When you stop a training job,
its status changes to `Stopping` at which time billing ceases. An algorithm can
delay termination in order to save model artifacts after which the job status changes to
`Stopped`. For more information, see the [stop_training_job](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job") method in the AWS SDK for Python (Boto3).

###### To stop a training job

1. Follow the [View experiments and runs](experiments-view-compare.md "experiments-view-compare.md") procedure on this page until you open
   the **Describe Trial Component** tab.
2. At the upper-right side of the tab, choose **Stop training job**. The
   **Status** at the top left of the tab changes to
   **Stopped**.
3. To view the training time and billing time, choose **AWS
   Settings**.
