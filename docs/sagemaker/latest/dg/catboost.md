# CatBoost

[CatBoost](https://catboost.ai/ "https://catboost.ai/") is a popular and high-performance
open-source implementation of the Gradient Boosting Decision Tree (GBDT) algorithm. GBDT is
a supervised learning algorithm that attempts to accurately predict a target variable by
combining an ensemble of estimates from a set of simpler and weaker models.

CatBoost introduces two critical algorithmic advances to GBDT:

1. The implementation of ordered boosting, a permutation-driven alternative to the
   classic algorithm
2. An innovative algorithm for processing categorical features
   Both techniques were created to fight a prediction shift caused by a special kind of
   target leakage present in all currently existing implementations of gradient boosting
   algorithms. This page includes information about Amazon EC2 instance recommendations and sample
   notebooks for CatBoost.

## Amazon EC2 instance recommendation for the CatBoost

algorithm

SageMaker AI CatBoost currently only trains using CPUs. CatBoost is a memory-bound (as opposed
to compute-bound) algorithm. So, a general-purpose compute instance (for example, M5) is
a better choice than a compute-optimized instance (for example, C5). Further, we
recommend that you have enough total memory in selected instances to hold the training
data.

## CatBoost sample notebooks

The following table outlines a variety of sample notebooks that address different use cases of Amazon SageMaker AI CatBoost algorithm.

| **Notebook Title**                                                                                                                                                                                                                                                                                                                                                                                                                             | **Description**                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tabular classification with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Classification_LightGBM_CatBoost.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Classification_LightGBM_CatBoost.ipynb") | This notebook demonstrates the use of the Amazon SageMaker AI CatBoost algorithm to train and host a tabular classification model. |
| [Tabular regression with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Regression_LightGBM_CatBoost.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Regression_LightGBM_CatBoost.ipynb")             | This notebook demonstrates the use of the Amazon SageMaker AI CatBoost algorithm to train and host a tabular regression model.     | For instructions on how to create and access Jupyter notebook instances that you can use to run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have created a notebook instance and opened it, choose the **SageMaker AI Examples** tab to see a list of all of the SageMaker AI samples. To open a notebook, choose its **Use** tab and choose **Create copy**. |
