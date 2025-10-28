# Get started fine-tuning foundation

models in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio provides a large collection of state-of-the-art foundation models. These models
support use cases such as content writing, code generation, question answering, copywriting,
summarization, classification, information retrieval, and more. You can find and deploy
these foundation models in the JumpStart model catalog. In some cases, you can also
customize them. You can use the foundation models to build your own generative AI solutions
for a wide range of applications.

A foundation model is a large pre-trained model that is adaptable to many downstream tasks
and often serves as the starting point for developing more specialized models. Examples of
foundation models include Meta Llama 4 Maverick 17B, DeepSeek-R1, or Stable Diffusion 3.5
Large. These models are pre-trained on massive amounts of data.

## Model customization

You might need to customize a base foundation model to better align it with your
specific use cases. The recommended way to first customize a foundation model is through
prompt engineering. Providing your foundation model with well-engineered, context-rich
prompts can help achieve desired results without any fine-tuning or changing of model
weights. For more information, see [Prompt engineering for foundation models](../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-prompt-engineering.md "../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-prompt-engineering.md") in the _Amazon SageMaker AI Developer Guide_.

If prompt engineering alone is not enough to customize your foundation model to a
specific task, you can fine-tune a foundation model on additional domain-specific data.
The fine-tuning process involves changing model weights.

To help you learn how to fine-tune foundation models, Amazon SageMaker Unified Studio provides an
example training dataset for each model that's eligible for training. You can also
choose to fine-tune the model with your own data set. Before you can do that, you must
prepare your data set and store it in an Amazon S3 bucket. The required format for the data
set varies between models. You can learn about the required format in the model details
page in Amazon SageMaker Unified Studio.

## Fine-tuning a foundation model

One way to fine-tune a model in Amazon SageMaker Unified Studio is to use JumpStart. First, you browse the
model catalog to find a model that's eligible for fine-tuning. Then, you train the model
with a training data set. Follow these steps to learn how to fine-tune with this
approach.

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. Choose a model to train by doing the following:
   1. From the main menu, choose **Build**.
   2. From the drop-down menu, under **Model Development**,
      choose **Jumpstart Models**.
   3. If the **Select or create project to continue**
      window appears, select a project that you've created, and choose
      **Continue**.

   The JumpStart page lists the model providers. 4. Choose a provider to see the available models.

   Not all providers have models that you can fine-tune in JumpStart. If
   you want to quickly find an eligible model so that you can get familiar
   with fine-tuning, choose **Meta**. It has many
   trainable models to choose from.

   ###### Tip

   For some providers, you can filter the list of models so that you
   see only the trainable ones. Choose the
   **Trainable** checkbox if it's present. 5. From the provider's list of models, choose the model you want to
   train.

   Amazon SageMaker Unified Studio shows the model details page, which provides information from
   the model provider. If you want to prepare a custom fine-tuning data
   set, use this page to learn the required format.

3. From the model details page, if the model is trainable, choose
   **Train** to create a training job.

If the model isn't trainable, the button is disabled. In that case, return to
the JumpStart page, find a different model that's trainable, and try
again. 4. On the **Fine-tune model** page, under
**Artifacts**, do one of the following:

    1. Keep the default selection of **Example training
     dataset**. This dataset is useful when you want to learn
     how to fine-tune with Amazon SageMaker Unified Studio. However, it won't be effective for
     customizing the model for your specific needs.
    2. If you've prepared a custom training dataset, choose **Enter
     training dataset**, and provide the URI that locates it in
     Amazon S3.

5. For **Output artifact location (S3 URI)**, specify where
   Amazon SageMaker Unified Studio uploads the fine-tuned model. You can choose to use the default bucket,
   or you can specify a custom location in Amazon S3.
6. (Optional) Under **Hyperparameters**, update the
   hyperparameters you want to change.

The hyperparameters available for each trainable model differ depending on the
model. Review the help text and additional information in the model details
pages in Amazon SageMaker Unified Studio to learn more about hyperparameters specific to the model of
your choice.

For more information on available hyperparameters, see [Commonly supported fine-tuning hyperparameters](../../../sagemaker/latest/dg/jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters "../../../sagemaker/latest/dg/jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters") in the _Amazon SageMaker AI Developer Guide_. 7. Under **Compute**, for **Training
Instance**, specify the training instance type for your training job.
You can choose only from instances that are compatible with the chosen
model.

###### Important

Choose an instance type that fits within the service quotas for your
AWS account.

When you submit your training job, Amazon SageMaker Unified Studio attempts to provision the chosen
instance type in your account. This attempt succeeds only if your quotas
have remaining capacity for the instance type.

To see the quotas for your account, open the Service Quotas console at
[https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

If you want to use a specific instance type but lack the required quota
capacity, you can request a quota increase with Support. For more information,
see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. 8. (Optional) Under **Information**, for **Training Job
Name**, you can edit the default name. 9. (Optional) For **Tags**, you can add and remove tags in the
form of key-value pairs to help organize and categorize your fine-tuning
training jobs. 10. Enter **Submit** to submit the training job.

###### Note

Some models require acceptance of an end-user license agreement (EULA). If
this applies to the model that you choose to fine-tune, Amazon SageMaker Unified Studio prompts you
with a window that contains the EULA content. You are responsible for
reviewing and complying with any applicable license terms and making sure
they are acceptable for your use case before using the model.

Amazon SageMaker Unified Studio shows a page with details about the training job. Here, you can observe
the status of the job as it executes.

The training job might take a long time to complete. You can view it at any
time from the **Training jobs** page.

When the training job completes, the status becomes
**Completed**. After the job completes, you can choose
**Deploy** to deploy the fine-tuned model to an inference
endpoint.
