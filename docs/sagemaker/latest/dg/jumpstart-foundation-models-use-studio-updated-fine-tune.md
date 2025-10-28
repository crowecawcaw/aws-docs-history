# Fine-tune a model in Studio

Fine-tuning trains a pre-trained model on a new dataset without training from
scratch. This process, also known as transfer learning, can produce accurate
models with smaller datasets and less training time. To fine-tune JumpStart
foundation models, navigate to a model detail card in the Studio UI. For
more information on how to open JumpStart in Studio, see [Open and use JumpStart in Studio](studio-jumpstart.md#jumpstart-open-use-studio "studio-jumpstart.md#jumpstart-open-use-studio"). After navigating to the model
detail card of your choice, choose **Train** in the upper right
corner. Note that not all models have fine-tuning available.

###### Important

Some foundation models require explicit acceptance of an end-user license
agreement (EULA) before fine-tuning. For more information, see [EULA acceptance
in Amazon SageMaker Studio](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-studio "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-studio").

## Model settings

When using a pre-trained JumpStart foundation model in Amazon SageMaker Studio, the
**Model artifact location (Amazon S3 URI)** is populated by
default. To edit the default Amazon S3 URI, choose **Enter model artifact
location**. Not all models support changing the model artifact
location.

## Data settings

In the **Data** field, provide an Amazon S3 URI point to your
training dataset location. The default Amazon S3 URI points to an example
training dataset. To edit the default Amazon S3 URI, choose **Enter
training dataset** and change the URI. Be sure to review the
model detail card in Amazon SageMaker Studio for information on formatting training
data.

## Hyperparameters

You can customize the hyperparameters of the training job that are used to
fine-tune the model. The hyperparameters available for each fine-tunable
model differ depending on the model.

The following hyperparameters are common among models:

- **Epochs** – One epoch is one
  cycle through the entire dataset. Multiple intervals complete a
  batch, and multiple batches eventually complete an epoch. Multiple
  epochs are run until the accuracy of the model reaches an acceptable
  level, or when the error rate drops below an acceptable level.
- **Learning rate** – The amount
  that values should be changed between epochs. As the model is
  refined, its internal weights are being nudged and error rates are
  checked to see if the model improves. A typical learning rate is 0.1
  or 0.01, where 0.01 is a much smaller adjustment and could cause the
  training to take a long time to converge, whereas 0.1 is much larger
  and can cause the training to overshoot. It is one of the primary
  hyperparameters that you might adjust for training your model. Note
  that for text models, a much smaller learning rate (5e-5 for BERT)
  can result in a more accurate model.
- **Batch size** – The number of
  records from the dataset that is to be selected for each interval to
  send to the GPUs for training.

Review the tool tip prompts and additional information in the model detail
card in the Studio UI to learn more about hyperparameters specific to
the model of your choice.

For more information on available hyperparameters, see [Commonly supported fine-tuning hyperparameters](jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters "jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters").

## Deployment

Specify the training instance type and output artifact location for your
training job. You can only choose from instances that are compatible with
the model of your choice within the fine-tuning the Studio UI. The
default output artifact location is the SageMaker AI default bucket. To change the
output artifact location, choose **Enter output artifact
location** and change the Amazon S3 URI.

## Security

Specify the security settings to use for your training job, including the
IAM role that SageMaker AI uses to train your model, whether your training job
should connect to a virtual private cloud (VPC), and any encryption
keys to secure your data.

## Additional information

In the **Additional Information** field you can edit the
training job name. You can also add and remove tags in the form of key-value
pairs to help organize and categorize your fine-tuning training jobs.

After providing information for your fine-tuning configuration, choose
**Submit**. If the pre-trained foundation model that you
chose to fine-tune requires explicit agreement of an end-user license agreement
(EULA) before training, the EULA is provided in a pop-up window. To accept the
terms of the EULA, choose **Accept**. You are responsible for
reviewing and complying with any applicable license terms and making sure they
are acceptable for your use case before downloading or using a model.
