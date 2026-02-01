Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Machine learning for novices and experts

With Amazon Redshift, you can leverage Machine Learning (ML) capabilities to gain insights from
your data, whether you are a novice or an expert in ML. Machine Learning is an Amazon Redshift
feature that enables you to create, train, and deploy ML models using SQL commands,
without the need for extensive ML expertise or complex data engineering.

The following sections guide you through the process of utilizing Machine Learning,
empowering you to unlock the full potential of your data with Amazon Redshift.

Amazon Redshift ML enables you to train models with one single SQL CREATE MODEL command. The
CREATE MODEL command creates a model that Amazon Redshift uses to generate model-based predictions
with familiar SQL constructs.

Amazon Redshift ML is especially useful when you don't have expertise in machine learning,
tools, languages, algorithms, and APIs. With Amazon Redshift ML, you don't have to perform
the undifferentiated heavy lifting required for integrating with an external machine
learning service. Amazon Redshift saves you the time to format and move data, manage permission
controls, or build custom integrations, workflows, and scripts. You can easily use popular
machine learning algorithms and simplify training needs that require frequent iteration
from training to prediction. Amazon Redshift automatically discovers the best algorithm and tunes
the best model for your problem. You can make predictions from within the Amazon Redshift cluster
without the need to move data out of Amazon Redshift nor to interface with and pay for another
service.

Amazon Redshift ML supports data analysts and data scientists in using machine learning. It
also makes it possible for machine learning experts to use their knowledge to guide the
CREATE MODEL statement to use only the aspects that they specify. By doing so, you can
speed up the time that CREATE MODEL needs to find the best candidate, improve the accuracy
of the model, or both.

The CREATE MODEL statement offers flexibility in how you can specify the parameters to
training job. Using this flexibility, both machine learning novices or experts can choose
their preferred preprocessors, algorithms, problem types, and hyperparameters. For example,
a user interested in customer churn might specify for the CREATE MODEL statement that the
problem type is a binary classification, which works well for customer churn. Then the
CREATE MODEL statement narrows down its search for the best model into binary
classification models. Even with the user choice of the problem type, there are still many
options that the CREATE MODEL statement can work with. For example, the CREATE MODEL
discovers and applies the best preprocessing transformations and discovers the best
hyperparameter settings.

Amazon Redshift ML makes training easier by automatically finding the best model using Amazon SageMaker AI
Autopilot. Behind the scenes, Amazon SageMaker AI Autopilot automatically trains and tunes the best
machine learning model based on your supplied data. Amazon SageMaker AI Neo then compiles the training
model and makes it available for prediction in your Redshift cluster. When you run a
machine learning inference query using a trained model, the query can use the massively
parallel processing capabilities of Amazon Redshift. At the same time, the query can use machine
learning–based prediction.

- As a _machine learning beginner_, with general
  knowledge of different aspects of machine learning such as preprocessors, algorithms,
  and hyperparameters, use the CREATE MODEL statement for only the aspects that you
  specify. Then you can shorten the time that CREATE MODEL needs to find the best
  candidate or improve the accuracy of the model. Also, you can increase the business
  value of the predictions by introducing additional domain knowledge such as the
  problem type or the objective. For example, in a customer churn scenario, if the
  outcome “customer is not active” is rare, then the F1 objective is often preferred to
  the Accuracy objective. Because high Accuracy models might predict “customer is
  active” all the time, this results in high accuracy but little business value. For
  information about F1 objectives, see [AutoMLJobObjective](../../../sagemaker/latest/APIReference/API_AutoMLJobObjective.md "../../../sagemaker/latest/APIReference/API_AutoMLJobObjective.md") in the _Amazon SageMaker AI API Reference_.

For more information about the basic options for the CREATE MODEL statement, see
[Simple CREATE MODEL](r_create_model_use_cases.md#r_simple_create_model "r_create_model_use_cases.md#r_simple_create_model").

- As a _machine learning advanced practitioner_,
  you can specify the problem type and preprocessors for certain (but not all)
  features. Then CREATE MODEL follows your suggestions on the specified aspects. At the
  same time, CREATE MODEL still discovers the best preprocessors for the remaining
  features and the best hyperparameters. For more information about how you can
  constrain one or more aspects of the training pipeline, see [CREATE MODEL with user
  guidance](r_create_model_use_cases.md#r_user_guidance_create_model "r_create_model_use_cases.md#r_user_guidance_create_model").
- As a _machine learning expert_, you can take
  full control of training and hyperparameter tuning. Then the CREATE MODEL statement
  doesn't attempt to discover the optimal preprocessors, algorithms, and
  hyperparameters because you make all the choices. For more information about how to
  use CREATE MODEL with AUTO OFF, see [CREATE XGBoost models with AUTO OFF](r_create_model_use_cases.md#r_auto_off_create_model "r_create_model_use_cases.md#r_auto_off_create_model").
- As a _data engineer_, you can bring a pretrained
  XGBoost model in Amazon SageMaker AI and import it into Amazon Redshift for local inference. With bring
  your own model (BYOM), you can use a model trained outside of Amazon Redshift with Amazon SageMaker AI
  for in-database inference locally in Amazon Redshift. Amazon Redshift ML supports using BYOM in
  either local or remote inference.

For more information about how to use the CREATE MODEL statement for local or
remote inference, see [Bring your own model (BYOM) - local
inference](r_create_model_use_cases.md#r_byom_create_model "r_create_model_use_cases.md#r_byom_create_model").
As an Amazon Redshift ML user, you can choose any of the following options to train and deploy
your model:

- Problem types, see [CREATE MODEL with user
  guidance](r_create_model_use_cases.md#r_user_guidance_create_model "r_create_model_use_cases.md#r_user_guidance_create_model").
- Objectives, see [CREATE MODEL with user
  guidance](r_create_model_use_cases.md#r_user_guidance_create_model "r_create_model_use_cases.md#r_user_guidance_create_model") or [CREATE XGBoost models with AUTO OFF](r_create_model_use_cases.md#r_auto_off_create_model "r_create_model_use_cases.md#r_auto_off_create_model").
- Model types, see [CREATE XGBoost models with AUTO OFF](r_create_model_use_cases.md#r_auto_off_create_model "r_create_model_use_cases.md#r_auto_off_create_model").
- Preprocessors, see [CREATE MODEL with user
  guidance](r_create_model_use_cases.md#r_user_guidance_create_model "r_create_model_use_cases.md#r_user_guidance_create_model").
- Hyperparameters, see [CREATE XGBoost models with AUTO OFF](r_create_model_use_cases.md#r_auto_off_create_model "r_create_model_use_cases.md#r_auto_off_create_model").
- Bring your own model (BYOM), see [Bring your own model (BYOM) - local
  inference](r_create_model_use_cases.md#r_byom_create_model "r_create_model_use_cases.md#r_byom_create_model").
