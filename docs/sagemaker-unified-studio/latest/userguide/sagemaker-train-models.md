# Train models

Using Amazon SageMaker Unified Studio, you can train foundation models or custom models.

Follow these steps to train a foundation model:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. Choose a model to train.
   1. From the main menu, choose **Build**.
   2. From the drop-down menu, choose **Jumpstart
      Models**.

   The JumpStart page lists the model providers. 3. Choose a model provider. The page displays the models for that provider. 4. Under **Action**, choose **Trainable**.
   The page displays the trainable models for that provider. 5. From the provider's list of models, choose the model you want to train.

3. From the model details page,
   choose **Train** to create a training job.

If the model is pretrained, you can fine-tune the model by adjusting the model parameters. 4. In the **Fine-tuning model** page, update the hyperparameters you
want to change. 5. Enter **Submit** to submit the training job. You can view the training job
from the **Training jobs** page.
You can also train the model in a Jupyterlab notebook using the SageMaker AI python SDK.

For more information about training models in JumpStart, see [JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
in the _Amazon SageMaker AI Developer Guide_.
