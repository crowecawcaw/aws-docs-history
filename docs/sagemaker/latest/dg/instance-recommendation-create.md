# Create an inference

recommendation

Create an inference recommendation programmatically using the AWS SDK for Python (Boto3) or
the AWS CLI, or interactively using Studio Classic or the SageMaker AI console. Specify a job
name for your inference recommendation, an AWS IAM role ARN, an input
configuration, and either a model package ARN when you registered your model
with the model registry, or your model name and a `ContainerConfig`
dictionary from when you created your model in the
**Prerequisites** section.

AWS SDK for Python (Boto3)
Use the [`CreateInferenceRecommendationsJob`](../APIReference/API_CreateInferenceRecommendationsJob.md "../APIReference/API_CreateInferenceRecommendationsJob.md") API
to start an inference recommendation job. Set the
`JobType` field to `'Default'` for
inference recommendation jobs. In addition, provide the
following:

- The Amazon Resource Name (ARN) of an IAM role that
  enables Inference Recommender to perform tasks on your behalf. Define this
  for the `RoleArn` field.
- A model package ARN or model name. Inference Recommender supports either
  one model package ARN or a model name as input. Specify one
  of the following:
  - The ARN of the versioned model package you created
    when you registered your model with SageMaker AI model
    registry. Define this for
    `ModelPackageVersionArn` in the
    `InputConfig` field.
  - The name of the model you created. Define this for
    `ModelName` in the
    `InputConfig` field. Also, provide the
    `ContainerConfig` dictionary, which
    includes the required fields that need to be
    provided with the model name. Define this for
    `ContainerConfig` in the
    `InputConfig` field. In the
    `ContainerConfig`, you can also
    optionally specify the
    `SupportedEndpointType` field as either
    `RealTime` or `Serverless`.
    If you specify this field, Inference Recommender returns
    recommendations for only that endpoint type. If you
    don't specify this field, Inference Recommender returns
    recommendations for both endpoint types.

- A name for your Inference Recommender recommendation job for the
  `JobName` field. The Inference Recommender job name must be
  unique within the AWS Region and within your AWS
  account.

Import the AWS SDK for Python (Boto3) package and create a SageMaker AI client object
using the client class. If you followed the steps in the
**Prerequisites** section, only specify one of
the following:

- Option 1: If you would like to create an inference
  recommendations job with a model package ARN, then store the
  model package group ARN in a variable named
  `model_package_arn`.
- Option 2: If you would like to create an inference
  recommendations job with a model name and
  `ContainerConfig`, store the model name in a
  variable named `model_name` and the
  `ContainerConfig` dictionary in a variable
  named `container_config`.

```
# Create a low-level SageMaker service client.
import boto3
aws_region = `'<INSERT>'`
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Provide only one of model package ARN or model name, not both.
# Provide your model package ARN that was created when you registered your
# model with Model Registry
model_package_arn = '<INSERT>'
## Uncomment if you would like to create an inference recommendations job with a
## model name instead of a model package ARN, and comment out model_package_arn above
## Provide your model name
# model_name = '<INSERT>'
## Provide your container config
# container_config = '<INSERT>'

# Provide a unique job name for SageMaker Inference Recommender job
job_name = `'<INSERT>'`

# Inference Recommender job type. Set to Default to get an initial recommendation
job_type = 'Default'

# Provide an IAM Role that gives SageMaker Inference Recommender permission to
# access AWS services
role_arn = `'arn:aws:iam::<account>:role/*'`

sagemaker_client.create_inference_recommendations_job(
    JobName = job_name,
    JobType = job_type,
    RoleArn = role_arn,
    # Provide only one of model package ARN or model name, not both.
    # If you would like to create an inference recommendations job with a model name,
    # uncomment ModelName and ContainerConfig, and comment out ModelPackageVersionArn.
    InputConfig = {
        'ModelPackageVersionArn': model_package_arn
        # 'ModelName': model_name,
        # 'ContainerConfig': container_config
    }
)
```

See the [Amazon SageMaker API
Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md") for a full list of optional and required
arguments you can pass to [`CreateInferenceRecommendationsJob`](../APIReference/API_CreateInferenceRecommendationsJob.md "../APIReference/API_CreateInferenceRecommendationsJob.md").

AWS CLI
Use the `create-inference-recommendations-job` API to
start an inference recommendation job. Set the `job-type`
field to `'Default'` for inference recommendation jobs.
In addition, provide the following:

- The Amazon Resource Name (ARN) of an IAM role that
  enables Amazon SageMaker Inference Recommender to perform tasks on your behalf. Define
  this for the `role-arn` field.
- A model package ARN or model name. Inference Recommender supports either
  one model package ARN or a model name as input. Specify one
  of the following
  - The ARN of the versioned model package you created
    when you registered your model with Model Registry.
    Define this for `ModelPackageVersionArn`
    in the `input-config` field.
  - The name of the model you created. Define this for
    `ModelName` in the
    `input-config` field. Also, provide the
    `ContainerConfig` dictionary which
    includes the required fields that need to be
    provided with the model name. Define this for
    `ContainerConfig` in the
    `input-config` field. In the
    `ContainerConfig`, you can also
    optionally specify the
    `SupportedEndpointType` field as either
    `RealTime` or `Serverless`.
    If you specify this field, Inference Recommender returns
    recommendations for only that endpoint type. If you
    don't specify this field, Inference Recommender returns
    recommendations for both endpoint types.

- A name for your Inference Recommender recommendation job for the
  `job-name` field. The Inference Recommender job name must be
  unique within the AWS Region and within your AWS
  account.

To create an inference recommendation jobs with a model package
ARN, use the following example:

```
aws sagemaker create-inference-recommendations-job
    --region `<region>`\
    --job-name `<job_name>`\
    --job-type Default\
    --role-arn arn:aws:iam::`<account:role/*>`\
    --input-config "{
        \"ModelPackageVersionArn\": \"arn:aws:sagemaker:`<region:account:role/*>`\",
        }"
```

To create an inference recommendation jobs with a model name and
`ContainerConfig`, use the following example. The
example uses the `SupportedEndpointType` field to specify
that we only want to return real-time inference
recommendations:

```
aws sagemaker create-inference-recommendations-job
    --region `<region>`\
    --job-name `<job_name>`\
    --job-type Default\
    --role-arn arn:aws:iam::`<account:role/*>`\
    --input-config "{
        \"ModelName\": \"model-name\",
        \"ContainerConfig\" : {
                \"Domain\": \"COMPUTER_VISION\",
                \"Framework\": \"PYTORCH\",
                \"FrameworkVersion\": \"1.7.1\",
                \"NearestModelName\": \"resnet18\",
                \"PayloadConfig\":
                    {
                        \"SamplePayloadUrl\": \"s3://{bucket}/{payload_s3_key}\",
                        \"SupportedContentTypes\": [\"image/jpeg\"]
                    },
                \"SupportedEndpointType\": \"RealTime\",
                \"DataInputConfig\": \"[[1,3,256,256]]\",
                \"Task\": \"IMAGE_CLASSIFICATION\",
            },
        }"
```

Amazon SageMaker Studio Classic
Create an inference recommendation job in Studio Classic.

1. In your Studio Classic application, choose the home icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
2. In the left sidebar of Studio Classic, choose
   **Models**.
3. Choose **Model Registry** from the
   dropdown list to display models you have registered with the
   model registry.

The left panel displays a list of model groups. The list
includes all the model groups registered with the model
registry in your account, including models registered
outside of Studio Classic. 4. Select the name of your model group. When you select your
model group, the right pane of Studio Classic displays column
heads such as **Versions** and
**Setting**.

If you have one or more model packages within your model
group, you see a list of those model packages within the
**Versions** column. 5. Choose the **Inference recommender**
column. 6. Choose an IAM role that grants Inference Recommender permission to
access AWS services. You can create a role and attach the
`AmazonSageMakerFullAccess` IAM managed
policy to accomplish this. Or you can let Studio Classic create
a role for you. 7. Choose **Get recommendations**.

The inference recommendation can take up to 45
minutes.

###### Warning

Do not close
this
tab. If you close this tab, you
cancel the instance recommendation job.

SageMaker AI console
Create an instance recommendation job through the SageMaker AI console by
doing the following:

1. Go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose
   **Inference**, and then choose
   **Inference recommender**.
3. On the **Inference recommender jobs**
   page, choose **Create job**.
4. For **Step 1: Model configuration**, do
   the following:
   1. For **Job type**, choose
      **Default recommender
      job**.
   2. If you’re using a model registered in the SageMaker AI
      model registry, then turn on the **Choose a
      model from the model registry** toggle
      and do the following:
      1. From the **Model group**
         dropdown list, choose the model group in SageMaker AI
         model registry where your model is located.
      2. From the **Model version**
         dropdown list, choose the desired version of your
         model.

   3. If you’re using a model that you’ve created in
      SageMaker AI, then turn off the **Choose a model
      from the model registry toggle** and do
      the following:
      1. For the **Model name**
         field, enter the name of your SageMaker AI model.

   4. From the **IAM role** dropdown
      list, you can select an existing AWS IAM role
      that has the necessary permissions to create an
      instance recommendation job. Alternatively, if you
      don’t have an existing role, you can choose
      **Create a new role** to open the
      role creation pop-up, and SageMaker AI adds the necessary
      permissions to the new role that you create.
   5. For **S3 bucket for benchmarking
      payload**, enter the Amazon S3 path to your
      sample payload archive, which should contain sample
      payload files that Inference Recommender uses to benchmark your
      model on different instance types.
   6. For **Payload content type**,
      enter the MIME types of your sample payload
      data.
   7. (Optional) If you turned off the **Choose
      a model from the model registry toggle**
      and specified a SageMaker AI model, then for
      **Container configuration**, do
      the following:
      1. For the **Domain** dropdown
         list, select the machine learning domain of the
         model, such as computer vision, natural language
         processing, or machine learning.
      2. For the **Framework**
         dropdown list, select the framework of your
         container, such as TensorFlow or XGBoost.
      3. For **Framework version**,
         enter the framework version of your container
         image.
      4. For the **Nearest model
         name** dropdown list, select the
         pre-trained model that mostly closely matches your
         own.
      5. For the **Task** dropdown
         list, select the machine learning task that the
         model accomplishes, such as image classification
         or regression.

   8. (Optional) For **Model compilation using
      SageMaker Neo**, you can configure the
      recommendation job for a model that you’ve compiled
      using SageMaker Neo. For **Data input
      configuration**, enter the correct input
      data shape for your model in a format similar to
      `{'input':[1,1024,1024,3]}`.
   9. Choose **Next**.

5. For **Step 2: Instances and environment
   parameters**, do the following:
   1. (Optional) For **Select instances for
      benchmarking**, you can select up to 8
      instance types that you want to benchmark. If you
      don’t select any instances, Inference Recommender considers all
      instance types.
   2. Choose **Next**.

6. For **Step 3: Job parameters**, do the
   following:
   1. (Optional) For the **Job name**
      field, enter a name for your instance recommendation
      job. When you create the job, SageMaker AI appends a
      timestamp to the end of this name.
   2. (Optional) For the **Job
      description** field, enter a description
      for the job.
   3. (Optional) For the **Encryption
      key** dropdown list, choose an AWS KMS key
      by name or enter its ARN to encrypt your
      data.
   4. (Optional) For **Max test duration
      (s)**, enter the maximum number of
      seconds you want each test to run for.
   5. (Optional) For **Max invocations per
      minute**, enter the maximum number of
      requests per minute the endpoint can reach before
      stopping the recommendation job. After reaching this
      limit, SageMaker AI ends the job.
   6. (Optional) For **P99 Model latency
      threshold (ms)**, enter the model latency
      percentile in milliseconds.
   7. Choose **Next**.

7. For **Step 4: Review job**, review your
   configurations and then choose
   **Submit**.
