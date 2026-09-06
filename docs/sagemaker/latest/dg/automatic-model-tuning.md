

# Automatic model tuning with SageMaker AI
<a name="automatic-model-tuning"></a>

Amazon SageMaker AI automatic model tuning (AMT) finds the best version of a model by running many training jobs on your dataset. Amazon SageMaker AI automatic model tuning (AMT) is also known as hyperparameter tuning. To do this, AMT uses the algorithm and ranges of hyperparameters that you specify. It then chooses the hyperparameter values that creates a model that performs the best, as measured by a metric that you choose.

For example, running a *[binary classification](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#binary-classification-model)* problem on a marketing dataset. Your goal is to maximize the *[area under the curve (AUC)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#AUC)* metric of the algorithm by training an [XGBoost algorithm with Amazon SageMaker AI](xgboost.md) model. You want to find which values for the `eta`, `alpha`, `min_child_weight`, and `max_depth` hyperparameters that will train the best model. Specify a range of values for these hyperparameters. Then, SageMaker AI hyperparameter tuning searches within the ranges to find a combination that creates a training job that creates a model with the highest AUC. To conserve resources or meet a specific model quality expectation, set up completion criteria to stop tuning after the criteria have been met.

You can use SageMaker AI AMT with built-in algorithms, custom algorithms, or SageMaker AI pre-built containers for machine learning frameworks.

SageMaker AI AMT can use an Amazon EC2 Spot instance to optimize costs when running training jobs. For more information, see [Managed Spot Training in Amazon SageMaker AI](model-managed-spot-training.md).

Before you start using hyperparameter tuning, you should have a well-defined machine learning problem, including the following:
+ A dataset
+ An understanding of the type of algorithm that you need to train
+ A clear understanding of how you measure success

Prepare your dataset and algorithm so that they work in SageMaker AI and successfully run a training job at least once. For information about setting up and running a training job, see [Guide to getting set up with Amazon SageMaker AI](gs.md).

**Topics**
+ [Understand the hyperparameter tuning strategies available in Amazon SageMaker AI](automatic-model-tuning-how-it-works.md)
+ [Define metrics and environment variables](automatic-model-tuning-define-metrics-variables.md)
+ [Define Hyperparameter Ranges](automatic-model-tuning-define-ranges.md)
+ [Track and set completion criteria for your tuning job](automatic-model-tuning-progress.md)
+ [Tune Multiple Algorithms with Hyperparameter Optimization to Find the Best Model](multiple-algorithm-hpo.md)
+ [Example: Hyperparameter Tuning Job](automatic-model-tuning-ex.md)
+ [Stop Training Jobs Early](automatic-model-tuning-early-stopping.md)
+ [Run a Warm Start Hyperparameter Tuning Job](automatic-model-tuning-warm-start.md)
+ [Resource Limits for Automatic Model Tuning](automatic-model-tuning-limits.md)
+ [Best Practices for Hyperparameter Tuning](automatic-model-tuning-considerations.md)