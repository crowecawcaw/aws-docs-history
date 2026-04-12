# Deploy your models to an endpoint

In Amazon SageMaker Canvas, you can deploy your models to an endpoint to make predictions. SageMaker AI provides
the ML infrastructure for you to host your model on an endpoint with the compute instances
that you choose. Then, you can _invoke_ the endpoint (send
a prediction request) and get a real-time prediction from your model. With this
functionality, you can use your model in production to respond to incoming requests, and you
can integrate your model with existing applications and workflows.

To get started, you should have a model that you'd like to deploy. You can deploy
custom model versions that you've built, Amazon SageMaker JumpStart foundation
models, and fine-tuned JumpStart foundation models.
For more information about building a model in Canvas, see [How custom models work](canvas-build-model.md "canvas-build-model.md"). For more information about JumpStart
foundation models in Canvas, see [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md").

Review the following **Permissions management** section, and
then begin creating new deployments in the **Deploy a model**
section.

## Permissions management

By default, you have permissions to deploy models to SageMaker AI Hosting
endpoints. SageMaker AI grants these permissions for all new and existing Canvas user
profiles through the [AmazonSageMakerCanvasFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md") policy, which is attached to the AWS
IAM execution role for the SageMaker AI domain that hosts your Canvas
application.

If your Canvas administrator is setting up a new domain or user profile, when
they're setting up the domain and following the prerequisite instructions in the
[Prerequisites for setting up Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"), SageMaker AI
turns on the model deployment permissions through the **Enable direct deployment
of Canvas models** option, which is enabled by default.

The Canvas administrator can manage model deployment permissions at the user
profile level as well. For example, if the administrator doesn't want to grant model deployment
permissions to all user profiles when setting up a domain, they can grant
permissions to specific users after creating the domain.

The following procedure shows how to modify the model deployment permissions for a
specific user profile:

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the list of domains, select the user profile’s domain.
5. On the **Domain details** page, select the **User
   profiles** tab.
6. Choose your **User profile**.
7. On the user profile's page, select the **App Configurations**
   tab.
8. In the **Canvas** section, choose **Edit**.
9. In the **ML Ops configuration** section, turn on
   the **Enable direct deployment of Canvas models**
   toggle to enable deployment permissions.
10. Choose **Submit** to save the changes to your domain
    settings.

The user profile should now have model deployment permissions.

After granting permissions to the domain or user profile, make sure that the user
logs out of their Canvas application and logs back in to apply the permission changes.

## Deploy a model

To get started with deploying your model, you create a new deployment in Canvas
and specify the model version that you want to deploy along with the ML infrastructure,
such as the type and number of compute instances that you would like to use for hosting
the model.

Canvas suggests a default type and number of instances based on your model type,
or you can learn more about the various SageMaker AI instance types on the [Amazon SageMaker pricing page](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/"). You are
charged based on the SageMaker AI instance pricing while your endpoint is active.

When deploying JumpStart foundation models, you also have the option to specify
the length of the deployment time. You can deploy the model to an endpoint indefinitely
(meaning the endpoint is active until you delete the deployment). Or, if you only need
the endpoint for a short period of time and would like to reduce costs, you can deploy
the model to an endpoint for a specified amount of time, after which SageMaker AI shuts down the
endpoint for you.

###### Note

If you deploy a model for a specified amount of time, stay logged in to the Canvas
application for the duration of the endpoint. If you log out of or delete the application,
then Canvas is unable to shut down the endpoint at the specified time.

After your model is deployed to a SageMaker AI Hosting [real-time inference
endpoint](realtime-endpoints.md "realtime-endpoints.md"), you can begin making predictions by _invoking_ the endpoint.

There are several different ways for you to deploy a model from the Canvas
application. You can access the model deployment option through any of the following
methods:

- On the **My models** page of the Canvas application,
  choose the model that you want to deploy. Then, from the model’s
  **Versions** page, choose the **More
  options** icon (
  ![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
  ) next to a model version and select
  **Deploy**.
- When on the details page for a model version, on the
  **Analyze** tab, choose the
  **Deploy** option.
- When on the details page for a model version, on the
  **Predict** tab, choose the **More
  options** icon (
  ![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
  ) at the top of the page and select
  **Deploy**.
- On the **ML Ops** page of the Canvas application, choose
  the **Deployments** tab and then choose **Create
  deployment**.
- For JumpStart foundation models and fine-tuned foundation models, go to
  the **Ready-to-use models** page of the Canvas application.
  Choose **Generate, extract and summarize content**. Then, find
  the JumpStart foundation model or fine-tuned foundation model that you want
  to deploy. Choose the model, and on the model's chat page, choose the
  **Deploy** button.

All of these methods open the **Deploy model** side panel, where you
specify the deployment configuration for your model. To deploy the model from this
panel, do the following:

1. (Optional) If you’re creating a deployment from the **ML
   Ops** page, you’ll have the option to **Select model and
   version**. Use the dropdown menus to select the model and model
   version that you want to deploy.
2. Enter a name in the **Deployment name** field.
3. (For JumpStart foundation models and fine-tuned foundation models only)
   Choose a **Deployment length**. Select
   **Indefinite** to leave the endpoint active until you shut
   it down, or select **Specify length** and then enter the period
   of time for which you want the endpoint to remain active.
4. For **Instance type**, SageMaker AI detects a default instance type
   and number that is suitable for your model. However, you can change the instance
   type that you would like to use for hosting your model.

###### Note

If you run out of the instance quota for the chosen instance type
on your AWS account, you can request a quota increase. For more information
about the default quotas and how to request an increase, see
[Amazon SageMaker AI endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md")
in the _AWS General Reference guide_. 5. For **Instance count**, you can set the number of active
instances that are used for your endpoint. SageMaker AI detects a default number that is
suitable for your model, but you can change this number. 6. When you’re ready to deploy your model, choose
**Deploy**.

Your model should now be deployed to an endpoint.
