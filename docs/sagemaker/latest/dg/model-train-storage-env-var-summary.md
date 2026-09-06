

# SageMaker AI environment variables and the default paths for training storage locations
<a name="model-train-storage-env-var-summary"></a>

The following table summarizes the input and output paths for training datasets, checkpoints, model artifacts, and outputs, managed by the SageMaker training platform.


| Local path in SageMaker training instance | SageMaker AI environment variable | Purpose | Read from S3 during start | Read from S3 during Spot-restart | Writes to S3 during training | Writes to S3 when job is terminated | 
| --- | --- | --- | --- | --- | --- | --- | 
| `/opt/ml/input/data/{{channel_name}}`1  | SM\_CHANNEL\_{{CHANNEL\_NAME}} | Reading training data from the input channels specified through the SageMaker AI Python SDK [ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) class or the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API operation. For more information about how to specify it in your training script using the SageMaker Python SDK, see [Prepare a Training script](https://sagemaker.readthedocs.io/en/stable/). | Yes | Yes | No | No | 
| `/opt/ml/output/data`2 | SM\_OUTPUT\_DIR | Saving outputs such as loss, accuracy, intermediate layers, weights, gradients, bias, and TensorBoard-compatible outputs. You can also save any arbitrary output you’d like using this path. Note that this is a different path from the one for storing the final model artifact `/opt/ml/model/`. | No | No | No | Yes | 
| `/opt/ml/model`3 | SM\_MODEL\_DIR | Storing the final model artifact. This is also the path from where the model artifact is deployed for [Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) in SageMaker AI Hosting. | No | No | No | Yes | 
| `/opt/ml/checkpoints`4 | - | Saving model checkpoints (the state of model) to resume training from a certain point, and recover from unexpected or [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) interruptions. | Yes | Yes | Yes | No | 
| `/opt/ml/code` | SAGEMAKER\_SUBMIT\_DIRECTORY | Copying training scripts, additional libraries, and dependencies. | Yes | Yes | No | No | 
| `/tmp` | - | Reading or writing to `/tmp` as a scratch space. | No | No | No | No | 

1 `channel_name` is the place to specify user-defined channel names for training data inputs. Each training job can contain several data input channels. You can specify up to 20 training input channels per training job. Note that the data downloading time from the data channels is counted to the billable time. For more information about data input paths, see [How Amazon SageMaker AI Provides Training Information](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-running-container.html). Also, there are three types of data input modes that SageMaker AI supports: file, FastFile, and pipe mode. To learn more about the data input modes for training in SageMaker AI, see [Access Training Data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data.html).

2 SageMaker AI compresses and writes training artifacts to TAR files (`tar.gz`). Compression and uploading time is counted to the billable time. For more information, see [How Amazon SageMaker AI Processes Training Output](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html).

3 SageMaker AI compresses and writes the final model artifact to a TAR file (`tar.gz`). Compression and uploading time is counted to the billable time. For more information, see [How Amazon SageMaker AI Processes Training Output](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html).

4 Sync with Amazon S3 during training. Write as is without compressing to TAR files. For more information, see [Use Checkpoints in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html).