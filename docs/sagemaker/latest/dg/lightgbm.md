# LightGBM

[LightGBM](https://lightgbm.readthedocs.io/en/latest/ "https://lightgbm.readthedocs.io/en/latest/") is a popular and
efficient open-source implementation of the Gradient Boosting Decision Tree (GBDT)
algorithm. GBDT is a supervised learning algorithm that attempts to accurately predict a
target variable by combining an ensemble of estimates from a set of simpler and weaker
models. LightGBM uses additional techniques to significantly improve the efficiency and
scalability of conventional GBDT. This page includes information about Amazon EC2 instance
recommendations and sample notebooks for LightGBM.

## Amazon EC2 instance recommendation for the LightGBM

algorithm

SageMaker AI LightGBM currently supports single-instance and multi-instance CPU training. For
multi-instance CPU training (distributed training), specify an
`instance_count` greater than 1 when you define your Estimator. For more
information on distributed training with LightGBM, see [Amazon SageMaker AI LightGBM Distributed training using Dask](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/sagemaker_lightgbm_distributed_training_dask/sagemaker-lightgbm-distributed-training-dask.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/sagemaker_lightgbm_distributed_training_dask/sagemaker-lightgbm-distributed-training-dask.html").

LightGBM is a memory-bound (as opposed to compute-bound) algorithm. So, a
general-purpose compute instance (for example, M5) is a better choice than a
compute-optimized instance (for example, C5). Further, we recommend that you have enough
total memory in selected instances to hold the training data.

## LightGBM sample notebooks

The following table outlines a variety of sample notebooks that address different use cases of Amazon SageMaker AI LightGBM algorithm.

| **Notebook Title**                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Description**                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tabular classification with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Classification_LightGBM_CatBoost.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Classification_LightGBM_CatBoost.html")                              | This notebook demonstrates the use of the Amazon SageMaker AI LightGBM algorithm to train and host a tabular classification model. |
| [Tabular regression with Amazon SageMaker AI LightGBM and CatBoost algorithm](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Regression_LightGBM_CatBoost.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/lightgbm_catboost_tabular/Amazon_Tabular_Regression_LightGBM_CatBoost.html")                                          | This notebook demonstrates the use of the Amazon SageMaker AI LightGBM algorithm to train and host a tabular regression model.     |
| [Amazon SageMaker AI LightGBM Distributed training using Dask](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/sagemaker_lightgbm_distributed_training_dask/sagemaker-lightgbm-distributed-training-dask.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/sagemaker_lightgbm_distributed_training_dask/sagemaker-lightgbm-distributed-training-dask.html") | This notebook demonstrates distributed training with the Amazon SageMaker AI LightGBM algorithm using the Dask framework.          | For instructions on how to create and access Jupyter notebook instances that you can use to run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have created a notebook instance and opened it, choose the **SageMaker AI Examples** tab to see a list of all of the SageMaker AI samples. To open a notebook, choose its **Use** tab and choose **Create copy**. |
