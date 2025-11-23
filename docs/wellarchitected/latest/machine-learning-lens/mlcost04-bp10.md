# MLCOST04-BP10 Use warm start and checkpointing hyperparameter

tuning

When training machine learning models, you can significantly reduce
time and costs by using previous training efforts. This practice
shows how to use warm start and checkpointing techniques in
hyperparameter tuning to accelerate your model development process
and optimize resource utilization.

**Desired outcome:** You can create
more efficient hyperparameter tuning jobs by using knowledge from
previous tuning efforts and saved model states. By implementing warm
start capabilities, you can initialize new tuning jobs with
information from previous runs, avoiding unnecessary repetition.
With checkpointing, you can save intermediate model states during
training, allowing you to resume jobs from the last checkpoint
rather than starting from scratch. These techniques enable you to
accelerate your model development process, reduce computational
costs, and find optimal hyperparameter configurations more
efficiently.

**Common anti-patterns:**

- Starting every hyperparameter tuning job from scratch without
  using previous knowledge.
- Not saving model checkpoints during lengthy training jobs,
  risking complete loss of progress if interrupted.
- Using unnecessarily wide hyperparameter search ranges when
  previous jobs have already identified promising areas.

**Benefits of establishing this best
practice:**

- Lower computational costs through more efficient resource
  utilization.
- Accelerated convergence to optimal model configurations.
- Improved resilience to training interruptions through checkpoint
  recovery.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hyperparameter tuning is an essential but computationally
intensive part of machine learning model development. Without warm
start capabilities, each tuning job begins with no prior
knowledge, potentially wasting resources by exploring
already-evaluated hyperparameter combinations. Without
checkpointing, an interrupted training job must restart from the
beginning, losing progress.

You can overcome these inefficiencies by implementing warm start
and checkpointing strategies in your ML workflow. Warm start
allows you to use knowledge from previous hyperparameter tuning
jobs, focusing the search on promising areas of the hyperparameter
space. Checkpointing enables you to save model states periodically
during training, providing a recovery point if training is
interrupted.

Amazon SageMaker AI offers built-in support for both warm start and
checkpointing capabilities. For warm start, you can specify one or
more parent tuning jobs whose results inform the new job's
hyperparameter search. SageMaker AI offers two warm start types:
TRANSFER_LEARNING for adapting knowledge to new
datasets and IDENTICAL_DATA_AND_ALGORITHM for
continuing tuning with the same dataset. For checkpointing, you
can configure your training jobs to periodically save model states
to Amazon S3, which can be used to resume training if needed.

### Implementation steps

1. **Configure warm start for
   hyperparameter tuning jobs**. Set up a new
   hyperparameter tuning job that builds upon the knowledge
   gained from previous tuning jobs. In Amazon SageMaker AI, you
   can configure this by specifying one or more parent tuning
   jobs and selecting an appropriate warm start type. This
   approach is particularly effective when you want to refine
   hyperparameter search after initial exploration or adapt a
   model to a similar dataset.
2. **Select appropriate parent jobs for
   warm start**. Choose parent jobs that are relevant
   to your current tuning objective. The best parent jobs are
   those that used similar datasets, algorithms, or
   optimization objectives. In SageMaker AI, you can specify up to
   five parent jobs when configuring a warm start tuning job.
3. **Choose the right warm start
   type**. Select
   IDENTICAL_DATA_AND_ALGORITHM when
   continuing tuning with the same dataset and algorithm, or
   TRANSFER_LEARNING when adapting knowledge
   to a new but related dataset or problem. The warm start type
   determines how SageMaker AI will use information from the
   parent jobs.
4. **Configure checkpointing for training
   jobs**. Enable checkpointing in your training
   script by saving model states at regular intervals. In
   SageMaker AI, specify a checkpoint S3 location where these
   model states will be stored. This allows you to resume
   training from the last saved checkpoint if a job is
   interrupted or if you want to extend training later.
5. **Implement checkpoint saving in your
   training code**. Add callback functions in your ML
   framework (such as TensorFlow, PyTorch, or MXNet) to
   periodically save model states during training. These
   frameworks typically provide built-in checkpoint
   functionality that you can configure with minimal code
   changes.
6. **Set up checkpoint recovery
   mechanisms**. Configure your training jobs to check
   for existing checkpoints at startup and resume from the
   latest checkpoint if available. In SageMaker AI, you can
   specify the checkpoint configuration when creating a
   training job, including the S3 location where checkpoints
   are stored.
7. **Optimize hyperparameter search
   ranges based on previous results**. When using warm
   start, refine your hyperparameter search ranges based on
   promising values identified in parent jobs. Narrowing search
   ranges around previously successful values can significantly
   improve tuning efficiency.
8. **Run parallel hyperparameter tuning
   jobs strategically**. Use warm start to distribute
   the hyperparameter tuning workload across multiple jobs that
   can share knowledge. This approach is particularly effective
   for exploring large hyperparameter spaces efficiently.
9. **Monitor and evaluate warm start
   efficiency**. Track the performance and efficiency
   gains from warm start by comparing with cold-start
   approaches. This analysis refines your warm start strategy
   for future jobs.
10. **Use enhanced hyperparameter tuning
    capabilities**. Use improved SageMaker AI
    hyperparameter tuning with better algorithms and support for
    multi-objective optimization to find optimal configurations
    more efficiently.
11. **Use generative AI for hyperparameter
    selection**. Use large language models to suggest
    promising hyperparameter ranges based on model architecture
    and dataset characteristics. Generative AI can identify
    sensible starting points for hyperparameter tuning jobs,
    especially for new model architectures.

## Resources

**Related documents:**

- [Run
  a Warm Start Hyperparameter Tuning Job](../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md "../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md")
- [Checkpoints
  in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-checkpoints.md "../../../sagemaker/latest/dg/model-checkpoints.md")
- [Automatic
  model tuning in Amazon SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [HyperparameterTuner](https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html "https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html")

**Related examples:**

- [Automatic
  Model Tuning: Warm Starting Tuning Jobs](https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb")
- [Hyperparameter
  Optimization with Checkpointing Example](https://github.com/aws/amazon-sagemaker-examples/tree/master/hyperparameter_tuning "https://github.com/aws/amazon-sagemaker-examples/tree/master/hyperparameter_tuning")
