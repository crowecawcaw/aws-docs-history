# Find serverless models with the Amazon Bedrock model

catalog

The Amazon Bedrock in SageMaker Unified Studio model catalog is where you can find the serverless Amazon Bedrock foundation
models that you have access to. You can group models by their modality or by their provider. The
modality of a model represents the type of input data that the model is trained on and is
able to process, such as text or image data. For more information, see [Supported
foundation models in Amazon Bedrock](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md").

If you can't find a specific model, ask your administrator if you have permissions to access the model.

To find out information about a model, such as supported use cases, select the model tile
in the model catalog. When choosing a model, consider the following:

- Amazon Bedrock models support differing inference parameters and capabilities. For more
  information, see [Amazon Bedrock
  foundation model information](../../../bedrock/latest/userguide/foundation-models-reference.md "../../../bedrock/latest/userguide/foundation-models-reference.md") in the _Amazon Bedrock user
  guide_.
- Amazon Bedrock in SageMaker Unified Studio supports Amazon Bedrock foundation models with on-demand throughput and
  [cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md").

Models that support cross-region inference throughput can increase throughput and improve
resiliency by sending requests to different AWS Regions during peak utilization
bursts. In the model catalog (and the model selector in app configuration), the text
_Cross-region_ identifies such a model.

- Amazon Bedrock in SageMaker Unified Studio doesn't support [Provisioned throughput](../../../bedrock/latest/userguide/throughput.md "../../../bedrock/latest/userguide/throughput.md"),
  [custom models](../../../bedrock/latest/userguide/custom-models.md "../../../bedrock/latest/userguide/custom-models.md") or [imported
  models](../../../bedrock/latest/userguide/model-customization-import-model.md "../../../bedrock/latest/userguide/model-customization-import-model.md").
  If the model is suitable for your needs, you can choose the menu button to start using the
  model. Depending on the model, you can choose from the following actions:

- [Build chat agent app](create-chat-app.md "create-chat-app.md") – Create an
  app in which users can chat with a model.
- [Build flow app](create-flows-app.md "create-flows-app.md") – Visually create
  the workflow for an app.
- [Build prompt](prompt-mgmt.md "prompt-mgmt.md") – Create resuable prompts
  for use in a flow app.
- [Evaluate model](evaluation.md "evaluation.md") – Evaluate the performance
  of a model for your use case.
  The following procedure shows how to open the model catalog from the Amazon Bedrock in SageMaker Unified Studio
  playground. You can also access the model catalog from your projects. Your administrator
  might give you access to different models in your projects. To check the models that you can
  access in a project, open or create a project, and then select **Models**
  in the navigation pane to open the model catalog.

###### To open the model catalog in the playground

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. At the top of the page, choose **Discover**.
4. Under **Data and model catalog**, choose **Amazon Bedrock
   models**. The Amazon Bedrock in SageMaker Unified Studio playground opens at the model
   catalog.
5. (Optional) Choose **Group by: Modality** and select
   **Provider** to sort the list by model provider.
6. Choose a model to get information about the model.
7. If you're ready to build with the app, choose **Action**
   and select the appropriate action. You can also choose an action from the model tile
   on the model catalog page.
8. Choose **Amazon Bedrock model catalog** to go back to the model catalog page.
