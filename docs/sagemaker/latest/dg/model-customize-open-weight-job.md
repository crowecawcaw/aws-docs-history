# AI model customization job submission

The SageMaker AI model customization capability can be accessed from Amazon SageMaker Studio’s Models page in the left hand panel. You can also find the
Assets page where you can create and manage your model customization Datasets and Evaluators.

![An image containing the access to model customization.](images/screenshot-open-model-12.png)
To begin a model customization job submission, select the Models option to access
the Jumpstart Base Models tab:

![An image containing how to choose the base model.](images/screenshot-open-model-11.png)
You can directly click Customize model in the model card or you can search for any model from Meta that is the one that your interested to customize.

![An image containing the model card and how to choose the model to customize.](images/screenshot-open-model-10.png)
Upon clicking the model card, you can access the model details page and launch the customization job by clicking Customize model and then selecting Customize with UI
to kick-off configuring your RLVR job.

![An image containing how to launch the customization job.](images/screenshot-open-model-9.png)
You can then enter your custom model name, select the model customization
technique to use and configure your job hyperparameters:

![An image containing selection of model customization techniques.](images/screenshot-open-model-8.png)

![An image containing selection of model customization techniques.](images/screenshot-open-model-7.png)

## AI model customization job submission using SDK

You can also use the SageMaker AI Python SDK to submit a model customization job:

```
# Submit a DPO model customization job

from sagemaker.modules.train.dpo_trainer import DPOTrainer
from sagemaker.modules.train.common import TrainingType

trainer = DPOTrainer(
    model=BASE_MODEL,
    training_type=TrainingType.LORA,
    model_package_group_name=MODEL_PACKAGE_GROUP_NAME,
    training_dataset=TRAINING_DATASET,
    s3_output_path=S3_OUTPUT_PATH,
    sagemaker_session=sagemaker_session,
    role=ROLE_ARN
)
```

## Monitoring your customization job

Immediately after submitting your job, you will be re-directed to your model customization training job page.

![An image containing selection of model customization techniques.](images/screenshot-open-model-6.png)

Once the job completes you can go to your custom model details page by clicking the Go to **Custom Model** button in the upper right corner.

![An image containing selection of model customization techniques.](images/screenshot-open-model-5.png)

In the custom model details page you can further work with your custom model
by:

1. Checking information about performance, generated artifacts location,
   training configuration hyper-parameters and training logs.
2. Launch an evaluation job with a different dataset (Continued
   customization).
3. Deploy the model using SageMaker AI Inference endpoints or Amazon Bedrock Custom
   Model Import.

![An image containing selection of model customization techniques.](images/screenshot-open-model-4.png)
