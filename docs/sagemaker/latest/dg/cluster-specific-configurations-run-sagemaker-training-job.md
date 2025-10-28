# Running

a SageMaker training job

SageMaker HyperPod Recipes supports submitting a SageMaker training job. Before you submit
the training job, you must update the cluster configuration,
`sm_job.yaml`, and install corresponding environment.

## Use

your recipe as a SageMaker training job

You can use your recipe as a SageMaker training job if you aren't hosting a
cluster. You must modify the SageMaker training job configuration file,
`sm_job.yaml`, to run your recipe.

```
sm_jobs_config:
  output_path: null
  tensorboard_config:
    output_path: null
    container_logs_path: null
  wait: True
  inputs:
    s3:
      train: null
      val: null
    file_system:
      directory_path: null
  additional_estimator_kwargs:
    max_run: 1800

```

1. `output_path`: You can specify where you're saving your
   model to an Amazon S3 URL.
2. `tensorboard_config`: You can specify a TensorBoard related
   configuration such as the output path or TensorBoard logs path.
3. `wait`: You can specify whether you're waiting for the job
   to be completed when you submit your training job.
4. `inputs`: You can specify the paths for your training and
   validation data. The data source can be from a shared filesystem such as
   Amazon FSx or an Amazon S3 URL.
5. `additional_estimator_kwargs`: Additional estimator
   arguments for submitting a training job to the SageMaker training job
   platform. For more information, see [Algorithm Estimator](https://sagemaker.readthedocs.io/en/stable/api/training/algorithm.html "https://sagemaker.readthedocs.io/en/stable/api/training/algorithm.html").
