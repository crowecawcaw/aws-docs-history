# View scheduled monitors

Use SageMaker Model Monitor to continuously monitor your machine learning models for data drift, model quality, bias, and other issues that might impact model performance.
After you've set up monitoring schedules, you can view the details of these scheduled monitors through the SageMaker AI console. The following procedure outlines the steps to access and review the scheduled monitors for a particular model, including their current status:

###### To view a model’s scheduled monitors

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Governance** in the left panel.
3. Choose **Model Dashboard**.
4. In the **Models** section of the Model Dashboard, select the model name of the
   scheduled monitors you want to view.
5. View the scheduled monitors in the **Monitor schedule** section.
   You can review the status for each monitor in the **Status schedule**
   column, which is one of the following values:
   - **Failed**: The monitoring schedule failed due to a problem
     with the configuration or settings (such as incorrect user permissions).
   - **Pending**: The monitor is in the process of becoming
     scheduled.
   - **Stopped**: The schedule is stopped by the user.
   - **Scheduled**: The schedule is created and runs at the
     frequency you specified.
