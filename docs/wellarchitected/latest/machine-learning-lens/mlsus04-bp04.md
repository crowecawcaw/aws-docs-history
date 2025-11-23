# MLSUS04-BP04 Use efficient model tuning methods

Optimize your machine learning model's hyperparameters with
resource-efficient strategies that minimize computational needs
while improving performance. Efficient tuning methods can
significantly reduce costs, energy consumption, and time-to-market
compared to resource-intensive brute force approaches.

**Desired outcome:** You can
systematically find optimal hyperparameters for your machine
learning models while minimizing computational resource consumption.
By implementing intelligent search strategies and following best
practices for optimization, you achieve better model performance
with fewer resources, reduce your environmental footprint, and
accelerate time-to-market for your ML solutions.

**Common anti-patterns:**

- Using grid search, which tests the most possible combinations of
  hyperparameters.
- Running many concurrent training jobs without considering how
  results from previous jobs can inform later ones.
- Specifying excessively broad hyperparameter ranges without
  proper understanding of their impact.
- Using random search when more efficient options like Bayesian or
  Hyperband are available.

**Benefits of establishing this best
practice:**

- Reduce computational resources required for hyperparameter
  tuning by up to 10x compared to random search.
- Decrease energy consumption and associated carbon emissions from
  ML training.
- Find optimal hyperparameters faster, accelerating
  time-to-market.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hyperparameter tuning is a crucial step in machine learning model
development that directly impacts both model performance and
resource utilization. Efficient tuning strategies can dramatically
reduce the computational resources required while finding optimal
or near-optimal parameter settings.

When approaching hyperparameter tuning, consider the relationship
between tuning strategy and resource consumption. Grid search,
which exhaustively tests the most possible combinations, is the
most resource-intensive approach and should generally be avoided.
Random search provides better resource efficiency but lacks
intelligence in selecting which configurations to test. More
sophisticated approaches like Bayesian optimization and Hyperband
can find optimal hyperparameters with significantly fewer training
jobs, reducing both time and resource usage.

The efficiency of your hyperparameter tuning is also affected by
how you configure concurrent jobs and specify parameter ranges.
Running too many concurrent jobs can waste resources when using
methods that benefit from sequential exploration. Similarly,
specifying unnecessarily wide parameter ranges increases the
search space complexity without adding value.

### Implementation steps

1. **Choose an efficient search
   strategy**. Implement Bayesian optimization or
   Hyperband search strategies instead of random or grid
   search. Bayesian search uses information from previous
   trials to make intelligent guesses about promising
   hyperparameter configurations, typically requiring 10 times
   fewer jobs than random search to find optimal parameters.
   For large models like deep neural networks addressing
   computer vision problems,
   [Amazon SageMaker AI Hyperband](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md") can find optimal hyperparameters
   up to three times faster than Bayesian search.
2. **Optimize job concurrency
   settings**. Configure your hyperparameter tuning
   jobs with appropriate concurrency settings. With Bayesian
   optimization, running fewer concurrent jobs often yields
   better results since the algorithm benefits from information
   gathered in previous iterations. Balance the tradeoff
   between parallelism (which speeds up overall completion
   time) and sequential learning (which improves optimization
   efficiency) based on your specific requirements for
   time-to-completion versus resource efficiency.
3. **Define thoughtful parameter
   ranges**. Carefully select which hyperparameters to
   tune and their corresponding value ranges. Focus on
   parameters that significantly impact model performance and
   limit ranges to reasonable values based on domain knowledge
   or prior experiments. For parameters known to be log-scaled
   (learning rates, regularization strengths), convert them to
   log space to improve optimization efficiency. This focused
   approach reduces the search space complexity, discovering
   optimal configurations with fewer resources.
4. **Leverage early stopping
   capabilities**. Implement mechanisms to terminate
   underperforming training jobs early to avoid wasting
   resources on unpromising hyperparameter configurations. Use
   Amazon SageMaker AI's built-in early stopping functionality
   that automatically terminates training jobs that are
   unlikely to produce better models than previously completed
   jobs.
5. **Monitor resource
   utilization**. Track metrics related to resource
   provisioning and utilization for your hyperparameter tuning
   jobs. Use Amazon SageMaker AI's integration with Amazon CloudWatch to monitor CPU utilization, GPU utilization,
   memory usage, and other resource metrics. Analyze these
   metrics to identify optimization opportunities in your
   tuning strategy.
6. **Integrate with your MLOps
   pipeline**. Incorporate efficient hyperparameter
   tuning as a standard component of your MLOps workflow.
   Automate the process of selecting optimal hyperparameters
   and retraining models when necessary. This verifies the
   consistent application of efficient tuning practices across
   your machine learning projects.
7. **Leverage pre-trained models to
   reduce tuning scope**. Start with pre-trained
   models from the expanded
   [SageMaker AI
   JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md") catalog or
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") foundation models, which often require
   minimal hyperparameter tuning for your use case,
   significantly reducing computational resources compared to
   training from scratch.
8. **Leverage AI-powered code generation
   for tuning automation**. Use AI-powered development
   tools like
   [Amazon Q Developer](https://aws.amazon.com/q/developer/ "https://aws.amazon.com/q/developer/") and
   [Kiro](https://kiro.ai/ "https://kiro.ai/") to generate
   efficient hyperparameter tuning scripts, automate
   optimization workflows, and accelerate the implementation of
   resource-efficient tuning strategies.
9. **Consider warm-starting tuning
   jobs**. Use the results from previous
   hyperparameter tuning jobs to initialize new jobs when
   incrementally improving models or adapting to changing data
   patterns. This approach reduces the resources required to
   find good hyperparameters compared to starting from scratch.

## Resources

**Related documents:**

- [Best
  Practices for Hyperparameter Tuning](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md")
- [Automatic
  model tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Managed
  Spot Training in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md")
- [Amazon SageMaker AI Training Compiler](../../../sagemaker/latest/dg/training-compiler.md "../../../sagemaker/latest/dg/training-compiler.md")
- [Choosing
  the Best Number of Concurrent Training Jobs](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-parallelism "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-parallelism")
- [Choosing
  Hyperparameter Ranges](../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-choosing-ranges "../../../sagemaker/latest/dg/automatic-model-tuning-considerations.md#automatic-model-tuning-choosing-ranges")
- [Amazon SageMaker AI Hyperband Search Strategy](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-sagemaker-automatic-model-tuning-provides-faster-hyperparameter-tuning-hyperband-search-strategy/ "https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-sagemaker-automatic-model-tuning-provides-faster-hyperparameter-tuning-hyperband-search-strategy/")
