# Understand the hyperparameter tuning

strategies available in Amazon SageMaker AI

When you build complex machine learning systems like deep learning neural networks,
exploring all of the possible combinations is impractical. Hyperparameter tuning can
accelerate your productivity by trying many variations of a model. It looks for the best model
automatically by focusing on the most promising combinations of hyperparameter values within
the ranges that you specify. To get good results, you must choose the right ranges to explore.
This page provides a brief explanation of the different hyperparameter tuning strategies that
you can use with Amazon SageMaker AI.

Use the [API reference
guide](../APIReference/Welcome.md "../APIReference/Welcome.md") to understand how to interact with hyperparameter tuning. You can use the tuning
strategies described on this page with the [HyperParameterTuningJobConfig](../APIReference/API_HyperParameterTuningJobConfig.md "../APIReference/API_HyperParameterTuningJobConfig.md") and [HyperbandStrategyConfig](../APIReference/API_HyperbandStrategyConfig.md "../APIReference/API_HyperbandStrategyConfig.md") APIs.

###### Note

Because the algorithm itself is stochastic, the hyperparameter tuning model may fail to
converge on the best answer. This can occur even if the best possible combination of values
is within the ranges that you choose.

## Grid search

When using grid search, hyperparameter tuning chooses combinations of values from the
range of categorical values that you specify when you create the job. Only categorical
parameters are supported when using the grid search strategy. You do not need to specify the
`MaxNumberOfTrainingJobs`. The number of training jobs created by the tuning
job is automatically calculated to be the total number of distinct categorical combinations
possible. If specified, the value of `MaxNumberOfTrainingJobs` should equal the
total number of distinct categorical combinations possible.

## Random search

When using random search, hyperparameter tuning chooses a random combination of
hyperparameter values in the ranges that you specify for each training job it launches. The
choice of hyperparameter values doesn't depend on the results of previous training jobs. As
a result, you can run the maximum number of concurrent training jobs without changing the
performance of the tuning.

For an example notebook that uses random search, see the [Random search and hyperparameter scaling with SageMaker XGBoost and Automatic Model
Tuning](https://github.com/aws/amazon-sagemaker-examples-community/blob/215215eb25b40eadaf126d055dbb718a245d7603/training/sagemaker-automatic-model-tuning/hpo_xgboost_random_log.ipynb "https://github.com/aws/amazon-sagemaker-examples-community/blob/215215eb25b40eadaf126d055dbb718a245d7603/training/sagemaker-automatic-model-tuning/hpo_xgboost_random_log.ipynb") notebook.

## Bayesian optimization

Bayesian optimization treats hyperparameter tuning like a _[regression](../../../glossary/latest/reference/glos-chap.md#[regression] "../../../glossary/latest/reference/glos-chap.md#[regression]")_ problem. Given a
set of input features (the hyperparameters), hyperparameter tuning optimizes a model for the
metric that you choose. To solve a regression problem, hyperparameter tuning makes guesses
about which hyperparameter combinations are likely to get the best results. It then runs
training jobs to test these values. After testing a set of hyperparameter values,
hyperparameter tuning uses regression to choose the next set of hyperparameter values to
test.

Hyperparameter tuning uses an Amazon SageMaker AI implementation of Bayesian optimization.

When choosing the best hyperparameters for the next training job, hyperparameter tuning
considers everything that it knows about this problem so far. Sometimes it chooses a
combination of hyperparameter values close to the combination that resulted in the best
previous training job to incrementally improve performance. This allows hyperparameter
tuning to use the best known results. Other times, it chooses a set of hyperparameter values
far removed from those it has tried. This allows it to explore the range of hyperparameter
values to try to find new areas that are not yet well understood. The explore/exploit
trade-off is common in many machine learning problems.

For more information about Bayesian optimization, see the following:

###### Basic Topics on Bayesian Optimization

- [A Tutorial on Bayesian Optimization of
  Expensive Cost Functions, with Application to Active User Modeling and Hierarchical
  Reinforcement Learning](https://arxiv.org/abs/1012.2599 "https://arxiv.org/abs/1012.2599")
- [Practical Bayesian Optimization of
  Machine Learning Algorithms](https://arxiv.org/abs/1206.2944 "https://arxiv.org/abs/1206.2944")
- [Taking the
  Human Out of the Loop: A Review of Bayesian Optimization](https://ieeexplore.ieee.org/document/7352306?reload=true "https://ieeexplore.ieee.org/document/7352306?reload=true")

###### Speeding up Bayesian Optimization

- [Google Vizier: A Service for
  Black-Box Optimization](https://dl.acm.org/doi/10.1145/3097983.3098043 "https://dl.acm.org/doi/10.1145/3097983.3098043")
- [Learning Curve Prediction
  with Bayesian Neural Networks](https://openreview.net/forum?id=S11KBYclx "https://openreview.net/forum?id=S11KBYclx")
- [Speeding up automatic
  hyperparameter optimization of deep neural networks by extrapolation of learning
  curves](https://dl.acm.org/doi/10.5555/2832581.2832731 "https://dl.acm.org/doi/10.5555/2832581.2832731")

###### Advanced Modeling and Transfer Learning

- [Scalable Hyperparameter Transfer Learning](https://papers.nips.cc/paper_files/paper/2018/hash/14c879f3f5d8ed93a09f6090d77c2cc3-Abstract.html "https://papers.nips.cc/paper_files/paper/2018/hash/14c879f3f5d8ed93a09f6090d77c2cc3-Abstract.html")
- [Bayesian Optimization
  with Tree-structured Dependencies](http://proceedings.mlr.press/v70/jenatton17a.html "http://proceedings.mlr.press/v70/jenatton17a.html")
- [Bayesian Optimization with Robust Bayesian Neural Networks](https://papers.nips.cc/paper_files/paper/2016/hash/291597a100aadd814d197af4f4bab3a7-Abstract.html "https://papers.nips.cc/paper_files/paper/2016/hash/291597a100aadd814d197af4f4bab3a7-Abstract.html")
- [Scalable Bayesian
  Optimization Using Deep Neural Networks](http://proceedings.mlr.press/v37/snoek15.pdf "http://proceedings.mlr.press/v37/snoek15.pdf")
- [Input Warping for Bayesian
  Optimization of Non-stationary Functions](https://arxiv.org/abs/1402.0929 "https://arxiv.org/abs/1402.0929")

## Hyperband

Hyperband is a multi-fidelity based tuning strategy that dynamically reallocates
resources. Hyperband uses both intermediate and final results of training jobs to
re-allocate epochs to well-utilized hyperparameter configurations and automatically stops
those that underperform. It also seamlessly scales to using many parallel training jobs.
These features can significantly speed up hyperparameter tuning over random search and
Bayesian optimization strategies.

Hyperband should only be used to tune iterative algorithms that publish results at
different resource levels. For example, Hyperband can be used to tune a neural network for
image classification which publishes accuracy metrics after every epoch.

For more information about Hyperband, see the following links:

- [Hyperband: A Novel Bandit-Based
  Approach to Hyperparameter Optimization](http://arxiv.org/pdf/1603.06560 "http://arxiv.org/pdf/1603.06560")
- [Massively Parallel
  Hyperparameter Tuning](https://liamcli.com/assets/pdf/asha_arxiv.pdf "https://liamcli.com/assets/pdf/asha_arxiv.pdf")
- [BOHB: Robust
  and Efficient Hyperparameter Optimization at Scale](http://proceedings.mlr.press/v80/falkner18a/falkner18a.pdf "http://proceedings.mlr.press/v80/falkner18a/falkner18a.pdf")
- [Model-based Asynchronous
  Hyperparameter and Neural Architecture Search](https://openreview.net/pdf?id=a2rFihIU7i "https://openreview.net/pdf?id=a2rFihIU7i")

### Hyperband with early

stopping

Training jobs can be stopped early when they are unlikely to improve the objective
metric of the hyperparameter tuning job. This can help reduce compute time and avoid
overfitting your model. Hyperband uses an advanced internal mechanism to apply early
stopping. The parameter `TrainingJobEarlyStoppingType` in the
`HyperParameterTuningJobConfig` API must be set to `OFF` when
using the Hyperband internal early stopping feature.

###### Note

Hyperparameter tuning might not improve your model. It is an advanced tool for building
machine solutions. As such, it should be considered part of the scientific development
process.
