# MLCOST04-BP11 Use hyperparameter optimization

technologies

Optimize your machine learning models through automatic
hyperparameter tuning to find the optimal model configuration with
minimal manual effort, reducing the time and resources needed to
achieve peak model performance.

**Desired outcome:** You achieve
better performing machine learning models by using automatic
hyperparameter optimization technologies that run multiple training
jobs in parallel. You can efficiently explore a wide range of
hyperparameter combinations to find the optimal configuration that
maximizes model performance according to your specified metrics,
ultimately delivering better business results while reducing the
time and resources spent on manual tuning.

**Common anti-patterns:**

- Manually tuning hyperparameters through trial and error.
- Using a narrow range of hyperparameter values that don't
  adequately explore the solution space.
- Selecting arbitrary hyperparameter values without considering
  the specific requirements of your business problem.
- Running one training job at a time instead of using parallel
  capabilities.

**Benefits of establishing this best
practice:**

- Reduced time to develop high-performing machine learning models.
- Lower computational costs by efficiently exploring the
  hyperparameter space.
- Consistent and repeatable approach to model optimization.
- Ability to scale hyperparameter tuning efforts across multiple
  algorithms.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

_Hyperparameter optimization (HPO)_ is a
critical aspect of developing effective machine learning models.
Unlike model parameters that are learned during training,
hyperparameters are configuration variables that govern the
training process itself and significantly impact model
performance. Finding the optimal combination of hyperparameters
manually is time-consuming and inefficient.

By implementing automatic hyperparameter tuning, you can
systematically explore the hyperparameter space and identify the
configuration that maximizes model performance. SageMaker AI's
automatic model tuning service employs techniques like Bayesian
optimization to intelligently search through the hyperparameter
space, focusing computational resources on the most promising
regions and accelerating the discovery of the optimal
configuration.

When implementing hyperparameter optimization, you should define
appropriate search spaces for your hyperparameters based on domain
knowledge and previous experiments. You also need to select
relevant evaluation metrics that align with your business
objectives. For classification problems, this might include
accuracy, F1 score, or AUC-ROC, while for regression problems, it
could be mean squared error or mean absolute error.

### Implementation steps

1. **Identify key hyperparameters for
   your model**. Begin by determining which
   hyperparameters have the greatest impact on your model's
   performance. For neural networks, this might include
   learning rate, batch size, and network architecture
   parameters. For tree-based models, this could include tree
   depth, number of trees, and minimum samples per leaf.
2. **Define appropriate hyperparameter
   ranges**. Establish meaningful ranges for each
   hyperparameter based on domain knowledge and best practices
   for your chosen algorithm. Use logarithmic scales for
   parameters that span multiple orders of magnitude (like
   learning rate) for efficient exploration.
3. **Select relevant evaluation
   metrics**. Choose metrics that align with your
   business requirements and the problem you're solving. Check
   that these metrics provide a meaningful assessment of model
   performance in the context of your specific application.
4. **Configure SageMaker AI automatic model
   tuning**. Create a hyperparameter tuning job using
   the
   [SageMaker AI
   Python SDK](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md") or the SageMaker AI console. Specify the
   algorithm or framework you're using, the hyperparameter
   ranges, and the evaluation metric to optimize.
5. **Implement early stopping for
   efficiency**. Enable early stopping features to
   automatically terminate poorly performing training jobs,
   saving computational resources. SageMaker AI can monitor the
   evaluation metric during training and stop jobs that are
   unlikely to produce competitive models.
6. **Use warm start for incremental
   tuning**. Use the warm start feature to accelerate
   new hyperparameter tuning jobs by using information from
   previous tuning jobs, reducing the time and resources needed
   to find optimal configurations.
7. **Implement parallel training
   jobs**. Configure SageMaker AI to run multiple
   training jobs concurrently to explore different
   hyperparameter combinations simultaneously, dramatically
   reducing the time required to find optimal values.
8. **Analyze tuning job
   results**. Review the performance of different
   hyperparameter combinations to understand how each parameter
   affects model performance. Use this information to refine
   your hyperparameter ranges for future tuning jobs.
9. **Select the best model for
   deployment**. After the tuning job completes,
   identify the best-performing model based on your evaluation
   metric and deploy it using SageMaker AI's deployment
   capabilities.
10. **Use no-code hyperparameter
    optimization**. Use
    [SageMaker AI
    Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md") with enhanced capabilities for business users
    to perform hyperparameter optimization through natural
    language interfaces without requiring deep technical
    expertise.
11. **Document hyperparameter
    configurations**. Maintain comprehensive
    documentation of hyperparameter configurations, tuning
    strategies, and results to facilitate knowledge sharing and
    reproducibility.

## Resources

**Related documents:**

- [Automatic
  model tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Stop
  Training Jobs Early](../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md "../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md")
- [Best
  Practices for Hyperparameter Tuning](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md")
- [Create
  a Hyperparameter Optimization Tuning Job for One or More
  Algorithms (Console)](../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md "../../../sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.md")
- [Run
  a Warm Start Hyperparameter Tuning Job](../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md "../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md")

**Related examples:**

- [SageMaker AI
  examples - hyperparameter tuning](https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning "https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning")
