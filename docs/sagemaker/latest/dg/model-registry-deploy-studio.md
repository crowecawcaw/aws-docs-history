# Deploy a Model in Studio

After you register a model version and approve it for deployment, deploy it to a
Amazon SageMaker AI endpoint for real-time inference. You can [Deploy a Model from the Registry with
Python](model-registry-deploy.md "model-registry-deploy.md") or
deploy your model in Amazon SageMaker Studio. The following provides instructions on how to
deploy your model in Studio.

This feature is not available in Amazon SageMaker Studio Classic.

- If Studio is your default experience, the UI is similar to the images
  found in [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").
- If Studio Classic is your default experience, the UI is similar to the images
  found in [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
  Before you can deploy a model package, the following requirements must be met for
  the model package:

- A valid inference specification available. See [InferenceSpecification](../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-InferenceSpecification "../APIReference/API_CreateModelPackage.md#sagemaker-CreateModelPackage-request-InferenceSpecification") for more information.
- Model with approved status. See [Update the Approval Status of a
  Model](model-registry-approve.md "model-registry-approve.md") for more information.
  The following provides instructions on how to deploy a model in
  Studio.

###### To deploy a model in Studio

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Models** from the left navigation pane.
3. Choose the **Registered models** tab, if not selected
   already.
4. Immediately below the **Registered models** tab label,
   choose **Model Groups**, if not selected already.
5. (Optional) If you have models that are shared with you, you can choose
   between **My models** or **Shared with
   me**.
6. Select the checkboxes for the registered models. If the above requirements
   are met, the **Deploy** button becomes available to
   choose.
7. Choose **Deploy** to open the **Deploy model to
   endpoint** page.
8. Configure the deployment resources in the **Endpoint
   settings**.
9. Once you have verified the settings, choose **Deploy**.
   The model will then be deployed to the endpoint with the **In
   service** status.
   For `us-east-1`, `us-west-2`,
   `ap-northeast-1`, and `eu-west-1` regions,
   you can use the following instructions to deploy models:

###### To deploy a model in Studio

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Models** from the left navigation pane.
3. Choose the **My models** tab.
4. Choose the Logged **models** tab, if not
   selected already.
5. Select a model and choose **View Latest
   Version**.
6. Choose **Deploy** and select between SageMaker AI or Amazon Bedrock.
7. Once you have verified the settings, choose **Deploy**.
   The model will then be deployed to the endpoint with the **In
   service** status.
