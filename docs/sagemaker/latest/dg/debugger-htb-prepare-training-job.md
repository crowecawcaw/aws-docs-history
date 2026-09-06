

# Prepare a training job to collect TensorBoard output data
<a name="debugger-htb-prepare-training-job"></a>

A typical training job for machine learning in SageMaker AI consists of two main steps: preparing a training script and configuring a SageMaker AI ModelTrainer (formerly estimator in PySDK v2) object of the SageMaker AI Python SDK. In this section, you'll learn about the required changes to collect TensorBoard-compatible data from SageMaker training jobs.

## Prerequisites
<a name="debugger-htb-prerequisites"></a>

The following list shows the prerequisites to start using SageMaker AI with TensorBoard.
+ A SageMaker AI domain that's set up with Amazon VPC in your AWS account. 

  For instructions on setting up a domain, see [Onboard to Amazon SageMaker AI domain using quick setup](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html). You also need to add domain user profiles for individual users to access the TensorBoard on SageMaker AI. For more information, see [Add user profiles](domain-user-profile-add.md).
+ Amazon EFS must be enabled on your domain. TensorBoard requires an Amazon EFS file system to function. For domains created through quick setup after June 1, 2026, EFS is not created by default during domain creation. To enable EFS after domain creation, see [Amazon EFS creation and auto-mounting in Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-automount.html).
+ Amazon EFS must be enabled on your domain. TensorBoard requires an Amazon EFS file system to function. For domains created through quick setup after June 1, 2026, EFS is not created by default during domain creation. To enable EFS after domain creation, see [Amazon EFS creation and auto-mounting in Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-automount.html).
+ The following list is the minimum set of permissions for using TensorBoard on SageMaker AI.
  + `sagemaker:CreateApp`
  + `sagemaker:DeleteApp`
  + `sagemaker:DescribeTrainingJob`
  + `sagemaker:Search`
  + `s3:GetObject`
  + `s3:ListBucket`

## Step 1: Modify your training script with open-source TensorBoard helper tools
<a name="debugger-htb-prepare-training-job-1"></a>

Make sure you determine which output tensors and scalars to collect, and modify code lines in your training script using any of the following tools: TensorBoardX, TensorFlow Summary Writer, PyTorch Summary Writer, or SageMaker Debugger.

Also make sure that you specify the TensorBoard data output path as the log directory (`log_dir`) for callback in the training container. 

For more information about callbacks per framework, see the following resources.
+ For PyTorch, use [torch.utils.tensorboard.SummaryWriter](https://pytorch.org/docs/stable/tensorboard.html#module-torch.utils.tensorboard). See also the [Using TensorBoard in PyTorch](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html#using-tensorboard-in-pytorch) and [Log scalars](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html#log-scalars) sections in the *PyTorch tutorials*. Alternatively, you can use [TensorBoardX Summary Writer](https://tensorboardx.readthedocs.io/en/latest/tutorial.html).

  ```
  LOG_DIR="/opt/ml/output/tensorboard"
  tensorboard_callback=torch.utils.tensorboard.writer.SummaryWriter(log_dir=LOG_DIR)
  ```
+ For TensorFlow, use the native callback for TensorBoard, [tf.keras.callbacks.TensorBoard](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard).

  ```
  LOG_DIR="/opt/ml/output/tensorboard"
  tensorboard_callback=tf.keras.callbacks.TensorBoard(
      log_dir=LOG_DIR, histogram_freq=1)
  ```
+ For Transformers with PyTorch, you can use [transformers.integrations.TensorBoardCallback](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.TensorBoardCallback). 

  For Transformers with TensorFlow, use the `tf.keras.tensorboard.callback`, and pass that to the keras callback in transformers.
**Tip**  
You can also use a different container local output path. However, in [Step 2: Create a SageMaker training ModelTrainer object with the TensorBoard output configuration](#debugger-htb-prepare-training-job-2), you must map the paths correctly for SageMaker AI to successfully search the local path and save the TensorBoard data to the S3 output bucket.
+ For guidance on modifying training scripts using the SageMaker Debugger Python library, see [Adapting your training script to register a hook](debugger-modify-script.md).

## Step 2: Create a SageMaker training ModelTrainer object with the TensorBoard output configuration
<a name="debugger-htb-prepare-training-job-2"></a>

Use the `sagemaker.debugger.TensorBoardOutputConfig` while configuring a SageMaker AI ModelTrainer. This configuration API maps the S3 bucket you specify for saving TensorBoard data with the local path in the training container (`/opt/ml/output/tensorboard`). Pass the object of the module to the `tensorboard_output_config` parameter of the ModelTrainer class. The following code snippet shows an example of preparing a TensorFlow ModelTrainer with the TensorBoard output configuration parameter.

**Note**  
This example assumes that you use the SageMaker Python SDK. If you use the low-level SageMaker API, you should include the following to the request syntax of the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API.  

```
"TensorBoardOutputConfig": { 
  "LocalPath": "/opt/ml/output/tensorboard",
  "S3OutputPath": "{{s3_output_bucket}}"
}
```

```
import os
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import SourceCode
from sagemaker.core.debugger import TensorBoardOutputConfig
from sagemaker.train.configs import Compute

# Set variables for training job information, 
# such as s3_out_bucket and other unique tags.
... 

LOG_DIR="/opt/ml/output/tensorboard"

output_path = os.path.join(
    "{{s3_output_bucket}}", "{{sagemaker-output}}", "{{date_str}}", "{{your-training_job_name}}"
)

tensorboard_output_config = TensorBoardOutputConfig(
    s3_output_path=os.path.join(output_path, '{{tensorboard}}'),
    container_local_output_path=LOG_DIR
)

model_trainer = ModelTrainer(
    source_code=SourceCode(entry_script="{{train.py}}", source_dir="{{src}}"),
    role={{role}},
    training_image={{image_uri}},
    compute=Compute(instance_count={{1}}, instance_type="{{ml.c5.xlarge}}"),
    base_job_name="{{your-training_job_name}}",
    tensorboard_output_config=tensorboard_output_config,
    hyperparameters=hyperparameters
)
```

**Note**  
The TensorBoard application does not provide out-of-the-box support for SageMaker AI hyperparameter tuning jobs, as the [`CreateHyperParameterTuningJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) API is not integrated with the TensorBoard output configuration for the mapping. To use the TensorBoard application for hyperparameter tuning jobs, you need to write code for uploading metrics to Amazon S3 in your training script. Once the metrics are uploaded to an Amazon S3 bucket, you can then load the bucket into the TensorBoard application on SageMaker AI.