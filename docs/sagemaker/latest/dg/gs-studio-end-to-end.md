# Amazon SageMaker Studio Classic Tour

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

For a walkthrough that takes you on a tour of the main features of Amazon SageMaker Studio Classic, see the
[xgboost_customer_churn_studio.ipynb](https://sagemaker-examples.readthedocs.io/en/latest/aws_sagemaker_studio/getting_started/xgboost_customer_churn_studio.html "https://sagemaker-examples.readthedocs.io/en/latest/aws_sagemaker_studio/getting_started/xgboost_customer_churn_studio.html") sample notebook from the [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
GitHub repository. The code in the notebook trains multiple models and sets up the SageMaker Debugger and
SageMaker Model Monitor. The walkthrough shows you how to view the trials, compare the resulting
models, show the debugger results, and deploy the best model using the Studio Classic UI. You don't
need to understand the code to follow this walkthrough.

**Prerequisites**

To run the notebook for this tour, you need:

- An IAM account to sign in to Studio. For information,
  see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Basic familiarity with the Studio user interface and Jupyter notebooks. For information,
  see [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
- A copy of the
  [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
  repository in your Studio environment.

###### To clone the repository

1. Launch Studio Classic following the steps in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md") For users in IAM Identity Center, sign in using the URL from your
   invitation email.
2. On the top menu, choose **File**, then **New**, then
   **Terminal**.
3. At the command prompt, run the following command to clone the [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples") GitHub repository.

```
`$` git clone https://github.com/aws/amazon-sagemaker-examples.git
```

###### To navigate to the sample notebook

1. From the **File Browser** on the left menu, select **amazon-sagemaker-examples**.
2. Navigate to the example notebook with the following path.

`~/amazon-sagemaker-examples/aws_sagemaker_studio/getting_started/xgboost_customer_churn_studio.ipynb` 3. Follow the notebook to learn about Studio Classic's main features.

###### Note

If you encounter an error when you run the sample notebook, and some time has passed from
when you cloned the repository, review the notebook on the remote repository for updates.
