# Enable training

When adding a model to share, you can optionally provide a training environment and
allow collaborators in your organization to train the shared model.

###### Note

If you are adding a tabular model, you also need to specify a column format and target
column to enable training.

After providing the basic details about your model, you'll need to configure the
settings for the training job that will be used to train your model. This involves
specifying the container environment, code scripts, datasets, output locations, and various
other parameters to control how the training job is executed. To configure the training job
settings, follow these steps:

1. Add a container to use for model training. You can select a container used for an
   existing training job, bring your own container in Amazon ECR, or use an Amazon SageMaker Deep
   Learning Container.
2. Add environment variables.
3. Provide a training script location.
4. Provide a script mode entry point.
5. Provide an Amazon S3 URI for model artifacts generated during
   training.
6. Provide the Amazon S3 URI to the default training dataset.
7. Provide a model output path. The model output path should be the Amazon S3 URI path for
   any model artifacts generated from training. SageMaker AI saves the model artifacts as a single
   compressed TAR file in Amazon S3.
8. Provide a validation dataset to use for evaluating your model during training.
   Validation datasets must contain the same number of columns and the same feature headers
   as the training dataset.
9. Turn on network isolation. Network isolation isolates the model container so that no
   inbound or outbound network calls can be made to or from the model container.
10. Provide training channels through which SageMaker AI can access your data. For example, you
    might specify input channels named `train` or `test`. For each
    channel, specify a channel name and a URI to the location of your data. Choose
    **Browse** to search for Amazon S3 locations.
11. Provide hyperparameters. Add any hyperparameters with which collaborators should
    experiment during training. Provide a range of valid values for these hyperparameters.
    This range is used for training job hyperparameter validation. You can define ranges
    based on the datatype of the hyperparameter.
12. Select an instance type. We recommend a GPU instance with more memory for training
    with large batch sizes. For a comprehensive list of SageMaker training instances across AWS
    Regions, see the **On-Demand Pricing** table in [Amazon SageMaker Pricing.](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
13. Provide metrics. Define metrics for a training job by specifying a name and a
    regular expression for each metric that your training monitors. Design the regular
    expressions to capture the values of metrics that your algorithm emits. For example, the
    metric `loss` might have the regular expression `"Loss
=(.*?);"`.
