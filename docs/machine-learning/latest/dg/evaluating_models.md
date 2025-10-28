We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Evaluating ML Models

You should always _evaluate a model_ to determine if it will do a good job of
predicting the target on new and future data. Because future instances have unknown target
values, you need to check the accuracy metric of the ML model on data for which you already know
the target answer, and use this assessment as a proxy for predictive accuracy on future data.

To properly evaluate a model, you hold out a sample of data that has been labeled with the
target (ground truth) from the training datasource. Evaluating the predictive
accuracy of an ML model with the same data that was used for training is not useful, because it
rewards models that can "remember" the training data, as opposed to generalizing from it. Once
you have finished training the ML model, you send the model the held-out observations for which
you know the target values. You then compare the predictions returned by the ML model against
the known target value. Finally, you compute a summary metric that tells you how well the
predicted and true values match.

In Amazon ML, you evaluate an ML model by _creating an evaluation_. To create
an evaluation for an ML model, you need an ML model that you want to evaluate, and you need
labeled data that was not used for training. First, create a datasource for evaluation by
creating an Amazon ML datasource with the held-out data. The data used in the evaluation must have
the same schema as the data used in training and include actual values for the target
variable.

If all your data is in a single file or directory, you can use the Amazon ML console to split the
data. The default path in the Create ML model wizard splits the input
datasource and uses the first 70% for a training datasource and the remaining 30% for an
evaluation datasource. You can also customize the split ratio by using the **Custom**
option in the Create ML model wizard, where you can choose to select a random 70%
sample for training and use the remaining 30% for evaluation. To further specify custom split
ratios, use the data rearrangement string in the [Create Datasource](../APIReference/API_CreateDataSourceFromS3.md "../APIReference/API_CreateDataSourceFromS3.md") API. Once you have
an evaluation datasource and an ML model, you can create an evaluation and review the results of
the evaluation.

###### Topics

- [ML Model Insights](ml-model-insights.md "ml-model-insights.md")
- [Binary Model Insights](binary-model-insights.md "binary-model-insights.md")
- [Multiclass Model Insights](multiclass-model-insights.md "multiclass-model-insights.md")
- [Regression Model Insights](regression-model-insights.md "regression-model-insights.md")
- [Preventing Overfitting](#overfitting "#overfitting")
- [Cross-Validation](cross-validation.md "cross-validation.md")
- [Evaluation Alerts](evaluation-alerts.md "evaluation-alerts.md")

## Preventing Overfitting

When creating and training an ML model, the goal is to select the model that makes the best predictions,
which means selecting the model with the best settings (ML model settings or hyperparameters). In Amazon Machine Learning,
there are four hyperparameters that you can set: number of passes, regularization, model size,
and shuffle type. However, if you select model parameter settings that produce the "best"
predictive performance on the evaluation data, you might
overfit your model. Overfitting occurs
when a model has memorized patterns that
occur in the training and evaluation datasources, but has failed to generalize
the patterns in the data. It often occurs
when the training data includes all of the data used in the evaluation. An overfitted model
does well during evaluations, but fails to make accurate predictions on unseen data.

To avoid selecting an overfitted model as the best model,
you can reserve additional data to validate the performance of the ML model. For example, you
can divide your data into 60 percent for training, 20 percent for evaluation, and an additional
20 percent for validation. After selecting the model parameters that work well for the evaluation
data, you run a second evaluation with
the validation data to see how well the ML model performs on the validation data. If
the model meets your expectations on the validation data, then the model is not overfitting the
data.

Using a third set of data for validation helps you select appropriate ML model parameters to
prevent overfitting. However, holding out data from the training process for both evaluation and
validation makes less data available for training. This is especially a problem with small data sets
because it's always best to use as much data as possible for training. To
solve this problem, you can perform cross-validation. For information on cross-validation,
see [Cross-Validation](cross-validation.md "cross-validation.md").
