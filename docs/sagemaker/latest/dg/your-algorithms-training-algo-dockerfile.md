

# How Amazon SageMaker AI Runs Your Training Image
<a name="your-algorithms-training-algo-dockerfile"></a>

You can use a custom entrypoint script to automate infrastructure to train in a production environment. If you pass your entrypoint script into your Docker container, you can also run it as a standalone script without rebuilding your images. SageMaker AI processes your training image using a Docker container entrypoint script. 

This section shows you how to use a custom entrypoint without using the training toolkit. If you want to use a custom entrypoint but are unfamiliar with how to manually configure a Docker container, we recommend that you use the [SageMaker training toolkit library](https://github.com/aws/sagemaker-training-toolkit) instead. For more information about how to use the training toolkit, see [Adapting your own training container](adapt-training-container.md). 

By default, SageMaker AI looks for a script called `train` inside your container. You can also manually provide your own custom entrypoint by using the `ContainerArguments` and `ContainerEntrypoint` parameters of the [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) API. 

You have the following two options to manually configure your Docker container to run your image.
+ Use the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API and a Docker container with an entrypoint instruction contained inside of it.
+ Use the `CreateTrainingJob` API, and pass your training script from outside of your Docker container.

If you pass your training script from outside your Docker container, you don't need to rebuild the Docker container when you update your script. You can also use several different scripts to run in the same container.

Your entrypoint script should contain training code for your image. If you use the optional `source_dir` parameter inside an [ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html), it should reference the relative Amazon S3 path to the folder containing your entrypoint script. You can reference multiple files using the `source_dir` parameter. If you do not use `source_dir`, you can specify the entrypoint using the `entry_point` parameter. For an example of a custom entrypoint script that contains a ModelTrainer, see [Bring Your Own Model with SageMaker AI Script Mode](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/sagemaker-script-mode.html).

SageMaker AI model training supports high-performance S3 Express One Zone directory buckets as a data input location for file mode, fast file mode, and pipe mode. You can also use S3 Express One Zone directory buckets to store your training output. To use S3 Express One Zone, provide the URI of an S3 Express One Zone directory bucket instead of an Amazon S3 general purpose bucket. You can only encrypt your SageMaker AI output data in directory buckets with server-side encryption with Amazon S3 managed keys (SSE-S3). Server-side encryption with AWS KMS keys (SSE-KMS) is not currently supported for storing SageMaker AI output data in directory buckets. For more information, see [S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html).

## Run a training job with an entrypoint script bundled inside the Docker container
<a name="your-algorithms-training-algo-dockerfile-api-ep-in"></a>

SageMaker AI can run an entrypoint script bundled inside your Docker container. 
+ By default, Amazon SageMaker AI runs the following container.

  ```
  docker run {{image}} train
  ```
+ SageMaker AI overrides any default [CMD](https://docs.docker.com/engine/reference/builder/#cmd) statements in a container by specifying the `train` argument after the image name. In your Docker container, use the following `exec` form of the `ENTRYPOINT` instruction.

  ```
  ENTRYPOINT ["{{executable}}", "{{param1}}", "{{param2}}", ...]
  ```

  The following example shows how to specify a python entrypoint instruction called `k-means-algorithm.py`.

  ```
  ENTRYPOINT ["python", "k-means-algorithm.py"]
  ```

  The `exec` form of the `ENTRYPOINT` instruction starts the executable directly, not as a child of `/bin/sh`. This enables it to receive signals like `SIGTERM` and `SIGKILL` from SageMaker APIs. The following conditions apply when using the SageMaker APIs. 
  + The [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API has a stopping condition that directs SageMaker AI to stop model training after a specific time. 
  + The following shows the [`StopTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopTrainingJob.html) API. This API issues the equivalent of the `docker stop`, with a 2-minute timeout command to gracefully stop the specified container.

    ```
    docker stop -t 120
    ```

    The command attempts to stop the running container by sending a `SIGTERM` signal. After the 2-minute timeout, the API sends `SIGKILL` and forcibly stops the containers. If the container handles the `SIGTERM` gracefully and exits within 120 seconds from receiving it, no `SIGKILL` is sent. 

  If you want access to the intermediate model artifacts after SageMaker AI stops the training, add code to handle saving artifacts in your `SIGTERM` handler.
+ If you plan to use GPU devices for model training, make sure that your containers are `nvidia-docker` compatible. Include only the CUDA toolkit on containers; don't bundle NVIDIA drivers with the image. For more information about `nvidia-docker`, see [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker).
+ You can't use the `tini` initializer as your entrypoint script in SageMaker AI containers because it gets confused by the `train` and `serve` arguments.
+ `/opt/ml` and all subdirectories are reserved by SageMaker training. When building your algorithm’s Docker image, make sure that you don't place any data that's required by your algorithm in this directory. Because if you do, the data may no longer be visible during training.

To bundle your shell or Python scripts inside your Docker image, or to provide the script in an Amazon S3 bucket or by using the AWS Command Line Interface (CLI), continue to the following section.

### Bundle your shell script in a Docker container
<a name="your-algorithms-training-algo-dockerfile-script-sh"></a>

 If you want to bundle a custom shell script inside your Docker image, use the following steps. 

1. Copy your shell script from your working directory to inside your Docker container. The following code snippet copies a custom entrypoint script `custom_entrypoint.sh` from the current working directory to a Docker container located in `mydir`. The following example assumes that the base Docker image has Python installed.

   ```
   FROM {{<base-docker-image>}}:{{<tag>}}
   
   # Copy custom entrypoint from current dir to /mydir on container
   COPY {{./custom_entrypoint.sh /mydir/ }}
   ```

1. Build and push a Docker container to the Amazon Elastic Container Registry ([Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)) by following the instructions at [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*.

1. Launch the training job by running the following AWS CLI command.

   ```
   aws --region {{<your-region>}} sagemaker create-training-job \
   --training-job-name {{<your-training-job-name>}} \
   --role-arn {{<your-execution-role-arn>}} \
   --algorithm-specification '{ \ 
       "TrainingInputMode": "File", \
       "TrainingImage": "{{<your-ecr-image>}}", \
       "ContainerEntrypoint": ["{{/bin/sh}}"], \
       "ContainerArguments": ["{{/mydir/custom_entrypoint.sh}}"]}' \
   --output-data-config '{"S3OutputPath": "{{s3://custom-entrypoint-output-bucket/}}"}' \
   --resource-config '{"VolumeSizeInGB":{{10}},"InstanceCount":{{1}},"InstanceType":"{{ml.m5.2xlarge}}"}' \
   --stopping-condition '{"MaxRuntimeInSeconds": {{180}}}'
   ```

### Bundle your Python script in a Docker container
<a name="your-algorithms-training-algo-dockerfile-script-py"></a>

To bundle a custom Python script inside your Docker image, use the following steps. 

1. Copy your Python script from your working directory to inside your Docker container. The following code snippet copies a custom entrypoint script `custom_entrypoint.py` from the current working directory to a Docker container located in `mydir`.

   ```
   FROM {{<base-docker-image>}}:{{<tag>}}
   # Copy custom entrypoint from current dir to /mydir on container
   COPY {{./custom_entrypoint.py /mydir/}}
   ```

1. Launch the training job by running the following AWS CLI command.

   ```
   --algorithm-specification '{ \ 
       "TrainingInputMode": "File", \
       "TrainingImage": "{{<your-ecr-image>}}", \
       "ContainerEntrypoint": ["{{python}}"], \
       "ContainerArguments": ["{{/mydir/custom_entrypoint.py}}"]}' \
   ```

## Run a training job with an entrypoint script outside the Docker container
<a name="your-algorithms-training-algo-dockerfile-api-pass-ep"></a>

You can use your own Docker container for training and pass in an entrypoint script from outside the Docker container. There are some benefits to structuring your entrypoint script outside the container. If you update your entrypoint script, you don't need to rebuild the Docker container. You can also use several different scripts to run in the same container. 

Specify the location of your training script using the `ContainerEntrypoint` and `ContainerArguments` parameters of the [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) API. These entrypoints and arguments behave in the same manner as Docker entrypoints and arguments. The values in these parameters override the corresponding `ENTRYPOINT` or `CMD` provided as part of the Docker container. 

When you pass your custom entrypoint script to your Docker training container, the inputs that you provide determine the behavior of the container.
+ For example, if you provide only `ContainerEntrypoint`, the request syntax using the CreateTrainingJob API is as follows.

  ```
  {
      "AlgorithmSpecification": {
          "ContainerEntrypoint": ["{{string}}"],   
          ...     
          }       
  }
  ```

  Then, the SageMaker training backend runs your custom entrypoint as follows.

  ```
  docker run --entrypoint {{<ContainerEntrypoint>}} image
  ```
**Note**  
If `ContainerEntrypoint` is provided, the SageMaker training backend runs the image with the given entrypoint and overrides the default `ENTRYPOINT` in the image.
+ If you provide only `ContainerArguments`, SageMaker AI assumes that the Docker container contains an entrypoint script. The request syntax using the `CreateTrainingJob` API is as follows.

  ```
  {
      "AlgorithmSpecification": {
          "ContainerArguments": ["{{arg1}}", "{{arg2}}"],
          ...
      }
  }
  ```

  The SageMaker training backend runs your custom entrypoint as follows.

  ```
  docker run image {{<ContainerArguments>}}
  ```
+ If your provide both the `ContainerEntrypoint` and `ContainerArguments`, then the request syntax using the `CreateTrainingJob` API is as follows.

  ```
  {
      "AlgorithmSpecification": {
          "ContainerEntrypoint": ["{{string}}"],
          "ContainerArguments": ["{{arg1}}", "{{arg2}}"],
          ...
      }
  }
  ```

   The SageMaker training backend runs your custom entrypoint as follows.

  ```
  docker run --entrypoint {{<ContainerEntrypoint>}} image {{<ContainerArguments>}}
  ```

You can use any supported `InputDataConfig` source in the `CreateTrainingJob` API to provide an entrypoint script to run your training image. 

### Provide your entrypoint script in an Amazon S3 bucket
<a name="your-algorithms-training-algo-dockerfile-script-s3"></a>

 To provide a custom entrypoint script using an S3 bucket, use the `S3DataSource` parameter of the [DataSource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataSource.html#sagemaker-Type-DataSource-S3DataSource) API to specify the location of the script. If you use the `S3DataSource` parameter, the following are required.
+ The [InputMode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html#sagemaker-Type-Channel-InputMode) must be of the type `File`.
+ The [S3DataDistributionType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataSource.html#sagemaker-Type-DataSource-S3DataSource) must be `FullyReplicated`.

The following example has a script called custom\_entrypoint.sh placed in a path to an S3 bucket `s3://<bucket-name>/<bucket prefix>/custom_entrypoint.sh`.

```
#!/bin/bash
echo "Running custom_entrypoint.sh"
echo "Hello you have provided the following arguments: " "$@"
```

Next, you must set the configuration of the input data channel to run a training job. Do this either by using the AWS CLI directly or with a JSON file.

#### Configure the input data channel using AWS CLI with a JSON file
<a name="your-algorithms-training-algo-dockerfile-script-s3-json"></a>

To configure your input data channel with a JSON file, use AWS CLI as shown in the following code structure. Ensure that all of the following fields use the request syntax defined in the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#API_CreateTrainingJob_RequestSyntax) API.

```
// run-my-training-job.json
{
 "[AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-AlgorithmSpecification)": { 
        "ContainerEntrypoint": ["{{/bin/sh}}"],
        "ContainerArguments": ["/opt/ml/input/data/{{<your_channel_name>}}/{{custom_entrypoint.sh}}"],
         ...
   },
  "[InputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-InputDataConfig)": [ 
    { 
        "[ChannelName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html#sagemaker-Type-Channel-ChannelName)": "{{<your_channel_name>}}",
        "[DataSource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html#sagemaker-Type-Channel-DataSource)": { 
            "[S3DataSource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataSource.html#sagemaker-Type-DataSource-S3DataSource)": { 
                "[S3DataDistributionType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3DataSource.html#sagemaker-Type-S3DataSource-S3DataDistributionType)": "FullyReplicated",
                "[S3DataType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3DataSource.html#sagemaker-Type-S3DataSource-S3DataType)": "S3Prefix",
                "[S3Uri](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3DataSource.html#sagemaker-Type-S3DataSource-S3Uri)": "s3://{{<bucket-name>}}/{{<bucket_prefix>}}"
            }
        },
        "[InputMode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html#sagemaker-Type-Channel-InputMode)": "File",
    },
    ...]
}
```

Next, run the AWS CLI command to launch the training job from the JSON file as follows.

```
aws sagemaker create-training-job --cli-input-json file:{{//run-my-training-job.json}}
```

#### Configure the input data channel using AWS CLI directly
<a name="your-algorithms-training-algo-dockerfile-script-s3-directly"></a>

To configure your input data channel without a JSON file, use the following AWS CLI code structure.

```
aws --region {{<your-region>}} sagemaker create-training-job \
--training-job-name {{<your-training-job-name>}} \
--role-arn {{<your-execution-role-arn>}} \
--algorithm-specification '{ \
    "TrainingInputMode": "File", \
    "TrainingImage": "{{<your-ecr-image>}}", \
    "ContainerEntrypoint": ["{{/bin/sh}}"], \
    "ContainerArguments": ["{{/opt/ml/input/data/<your_channel_name>/custom_entrypoint.sh"]}}}' \
--input-data-config '[{ \
    "ChannelName":"{{<your_channel_name>}}", \
    "DataSource":{ \
        "S3DataSource":{ \
            "S3DataType":"S3Prefix", \
            "S3Uri":"s3://{{<bucket-name>}}/{{<bucket_prefix>}}", \
            "S3DataDistributionType":"FullyReplicated"}}}]' \
--output-data-config '{"S3OutputPath": "{{s3://custom-entrypoint-output-bucket/}}"}' \
--resource-config '{"VolumeSizeInGB":{{10}},"InstanceCount":{{1}},"InstanceType":"{{ml.m5.2xlarge}}"}' \
--stopping-condition '{"MaxRuntimeInSeconds": {{180}}}'
```