# TabTransformer

[TabTransformer](https://arxiv.org/abs/2012.06678 "https://arxiv.org/abs/2012.06678") is a novel deep
tabular data modeling architecture for supervised learning. The TabTransformer architecture
is built on self-attention-based Transformers. The Transformer layers transform the
embeddings of categorical features into robust contextual embeddings to achieve higher
prediction accuracy. Furthermore, the contextual embeddings learned from TabTransformer are
highly robust against both missing and noisy data features, and provide better
interpretability. This page includes information about Amazon EC2 instance recommendations and
sample notebooks for TabTransformer.

## Amazon EC2 instance recommendation for the TabTransformer

algorithm

SageMaker AI TabTransformer supports single-instance CPU and single-instance GPU training.
Despite higher per-instance costs, GPUs train more quickly, making them more cost
effective. To take advantage of GPU training, specify the instance type as one of the
GPU instances (for example, P3). SageMaker AI TabTransformer currently does not support
multi-GPU training.

## TabTransformer sample notebooks

The following table outlines a variety of sample notebooks that address different use
cases of Amazon SageMaker AI TabTransformer algorithm.

| **Notebook Title**                                                                                                                                                                                                                                                                                                                                                                                                          | **Description**                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tabular classification with Amazon SageMaker AI TabTransformer algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/tabtransformer_tabular/Amazon_Tabular_Classification_TabTransformer.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/tabtransformer_tabular/Amazon_Tabular_Classification_TabTransformer.ipynb") | This notebook demonstrates the use of the Amazon SageMaker AI TabTransformer<br>algorithm to train and host a tabular classification model. |
| [Tabular regression with Amazon SageMaker AI TabTransformer algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/tabtransformer_tabular/Amazon_Tabular_Regression_TabTransformer.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/tabtransformer_tabular/Amazon_Tabular_Regression_TabTransformer.ipynb")             | This notebook demonstrates the use of the Amazon SageMaker AI TabTransformer<br>algorithm to train and host a tabular regression model.     |

For instructions on how to create and access Jupyter notebook instances that you can use
to run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you
have created a notebook instance and opened it, choose the **SageMaker AI
Examples** tab to see a list of all of the SageMaker AI samples. To open a
notebook, choose its **Use** tab and choose **Create
copy**.
