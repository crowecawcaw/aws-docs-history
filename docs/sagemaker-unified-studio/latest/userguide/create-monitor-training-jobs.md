# Create and monitor custom training

jobs

You can use Jupyter Notebooks or SageMaker AI Notebooks to train your ML jobs. Refer to
SageMaker AI documents on how to train ML jobs.

```

model_trainer = ModelTrainer(
    training_image=image_uri,
    source_code=source_code,
    base_job_name=job_name,
    compute=compute_configs,
    distributed=Torchrun(),
    stopping_condition=StoppingCondition(
        max_runtime_in_seconds=7200
    ),
    hyperparameters={
        "config": "/opt/ml/input/data/config/args.yaml" # sample path
    },
    output_data_config=OutputDataConfig(
        s3_output_path=output_path
    ),
)
# starting the train job with our uploaded datasets as input
model_trainer.train(input_data_config=data, wait=True)

```

You can monitor the results of the training job by selecting **Training
Jobs** on the left panel

You can stop the jobs, monitor the artifacts, hyper parameters, security
configurations and tags that you have setup during the training.
