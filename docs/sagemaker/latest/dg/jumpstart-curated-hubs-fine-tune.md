# Fine-tune curated hub models

In your private curated model hub, you can run fine-tuning training jobs using your
model references. Model references point to a publicly available JumpStart model in
the SageMaker AI public hub, but you can fine-tune the model on your own data for your specific
use case. After the fine-tuning job, you have access to the model weights that you can
then use or deploy to an endpoint.

You can fine-tune curated hub models in just a few lines of code using the SageMaker
Python SDK. For more general information on fine-tuning publicly available JumpStart
models, see [Foundation models and hyperparameters for fine-tuning](jumpstart-foundation-models-fine-tuning.md "jumpstart-foundation-models-fine-tuning.md").

## Prerequisites

In order to fine-tune a JumpStart model reference in your curated hub,
do the following:

1. Make sure that your user's IAM role has the SageMaker AI `TrainHubModel`
   permission attached. For more information, see
   [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
   _AWS IAM User Guide_.

You should attach a policy like the following example to your user's IAM role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "sagemaker:TrainHubModel",
 "Resource": "arn:aws:sagemaker:*:`111122223333`:hub/*"
 }
 ]
}`

```

###### Note

If your curated hub is shared across accounts and the hub content is owned
by another account, make sure that your `HubContent` (the model
reference resource) has a resource-based IAM policy that also grants the
`TrainHubModel` permission to the requesting account, as shown
in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountSageMakerAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "sagemaker:TrainHubModel"
 ],
 "Resource": [
 "`arn:aws:sagemaker:*:111122223333:hub/*`"
 ]
 }
 ]
}`

```

2. Have a private curated hub with a model reference to a JumpStart model
   that you want to fine-tune. For more information about creating a private hub, see
   [Create a private model hub](jumpstart-curated-hubs-admin-guide-create.md "jumpstart-curated-hubs-admin-guide-create.md"). To learn how to
   add publicly available JumpStart models to your private hub, see
   [Add models to a private hub](jumpstart-curated-hubs-admin-guide-add-models.md "jumpstart-curated-hubs-admin-guide-add-models.md").

###### Note

The JumpStart model you choose should be fine-tunable. You can verify
whether a model is fine-tunable by checking the [Built-in Algorithms with Pre-trained Models Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html"). 3. Have a training dataset that you want to use for fine-tuning the model.
The dataset should be in the appropriate training format for the model that
you want to fine-tune.

## Fine-tune a curated hub model reference

The following procedure shows you how to fine-tune a model reference in your
private curated hub using the SageMaker Python SDK.

1. Make sure that you have the latest version (at least `3.0.0`)
   of the SageMaker Python SDK installed. For more information, see
   [Use Version 3.x of the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/").

```
!pip install --upgrade sagemaker
```

2. Import the AWS SDK for Python (Boto3) and the modules you need from the SageMaker Python SDK.

```
import boto3
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.core.jumpstart.configs import JumpStartConfig
from sagemaker.core.helper.session_helper import Session
```

3. Initialize a Boto3 session, a SageMaker AI client, and a SageMaker Python SDK session.

```
sagemaker_client = boto3.Session(region_name=`<AWS-region>`).client("sagemaker")
sm_session = Session(sagemaker_client=sagemaker_client)
```

4. Create a `ModelTrainer` using `from_jumpstart_config` and provide the JumpStart model ID, the
   name of your hub that contains the model reference, and your SageMaker Python SDK session.
   For a list of model IDs, see the [Built-in Algorithms with Pre-trained Models Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html").

Optionally, you can specify the `instance_type` and `instance_count`
fields when creating the ModelTrainer. If you don't, the training job uses the default instance type and count for
the model you're using.

You can also optionally specify the `output_path` to the Amazon S3 location
where you want to store the fine-tuned model weights. If you don't specify the
`output_path`, then uses a default SageMaker AI Amazon S3 bucket for the region
in your account, named with the following format:
`sagemaker-`<region>`-`<account-id>``.

```

jumpstart_config = JumpStartConfig(
    model_id="meta-textgeneration-llama-3-2-1b",
    hub_name=`<your-hub-name>`,
    # Optional: specify your desired instance type and count for the training job
    # instance_type = "ml.g5.2xlarge"
    # instance_count = 1
)
model_trainer = ModelTrainer.from_jumpstart_config(jumpstart_config=jumpstart_config)
    # Optional: specify a custom S3 location to store the fine-tuned model artifacts
    # output_path: "s3://`<output-path-for-model-artifacts>`"

```

5. Create an `InputData` object. Set `channel_name` to
   `train` and `data_source` to the location of your fine-tuning
   dataset. In the following example, replace
   `<your-fine-tuning-dataset>` with the Amazon S3
   URI of your dataset. If you have additional considerations, such as using local mode or
   multiple training data channels, see [ModelTrainer.train()](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") in the SageMaker Python SDK documentation for more information.

```
training_input = InputData(
    channel_name="train",
    data_source="s3://`<your-fine-tuning-dataset>`",
)
```

6. Call the model trainer's `train()` method and pass in your training data
   and your EULA acceptance (if applicable).

###### Note

The following example sets `accept_eula=False.` You should manually
change the value to `True` in order to accept the EULA.

```
model_trainer.train(input_data_config=[training_input], accept_eula=False)
```

Your fine-tuning job should now begin.

You can check on your fine-tuning job by viewing your training jobs, either in the SageMaker AI console
or by using the [ListTrainingJobs](../APIReference/API_ListTrainingJobs.md "../APIReference/API_ListTrainingJobs.md") API.

You can access your fine-tuned model artifacts at the Amazon S3 `output_path`
that was specified in the `ModelTrainer` object (either the default SageMaker AI Amazon S3 bucket
for the region, or a custom Amazon S3 path you specified, if applicable).
