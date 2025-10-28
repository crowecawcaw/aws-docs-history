# Create a training job

using the SageMaker AI console

You can use a SageMaker training plans for your training jobs using the SageMaker AI UI. When creating a
training job, the available plans are suggested to you if your instance choice and region
matches the available plans.

To create a training job using a training plan's reserved capacity in the SageMaker
console:

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Training**, and then
   **Training jobs**.
3. Choose the **Create training job** button.
4. When configuring the resources for your training job, look for the **Instance
   capacity** section. If there are plans available that match your chosen
   instance type and region, they are displayed here. Select a training plan that aligns with
   your compute capacity needs.

If no suitable plans are available, you can either adjust your instance type or
region, or proceed without using a training plan. 5. After selecting a training plan (or choosing to proceed without one), complete the
rest of your training job configuration and choose **Create training
job** to start the process.

![SageMaker AI console page for creating a new training job. The page displays various configuration options including job settings, algorithm options, resource configuration, training plan selection, and stopping conditions.](images/training-plans/tp-create-training-job.png)
Review and launch your job. Your job starts running as soon as the training plan becomes
`Active`, pending capacity.
