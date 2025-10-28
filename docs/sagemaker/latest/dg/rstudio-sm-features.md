# Amazon SageMaker AI feature integration with RStudio on Amazon SageMaker AI

One of the benefits of using RStudio on Amazon SageMaker AI is the integration of Amazon SageMaker AI features.
This includes integration with Amazon SageMaker Studio Classic and Reticulate. The following gives information
about these integrations and examples for using them.

**Use Amazon SageMaker Studio Classic and RStudio on Amazon SageMaker AI**

Your Amazon SageMaker Studio Classic and RStudio instances share the same Amazon EFS file system. This means that
files that you import and create using Studio Classic can be accessed using RStudio and vice versa.
This allows you to work on the same files using both Studio Classic and RStudio without having to
move your files between the two. For more information on this workflow, see the [Announcing Fully Managed RStudio on Amazon SageMaker AI for Data Scientists](https://aws.amazon.com/blogs/aws/announcing-fully-managed-rstudio-on-amazon-sagemaker-for-data-scientists "https://aws.amazon.com/blogs/aws/announcing-fully-managed-rstudio-on-amazon-sagemaker-for-data-scientists") blog.

**Use Amazon SageMaker SDK with reticulate**

The [reticulate](https://rstudio.github.io/reticulate "https://rstudio.github.io/reticulate") package is used as
an R interface to [Amazon
SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") to make API calls to Amazon SageMaker. The reticulate package
translates between R and Python objects, and Amazon SageMaker AI provides a serverless data science
environment to train and deploy Machine Learning (ML) models at scale. For general information about the reticulate
package, see [R Interface to
Python](https://rstudio.github.io/reticulate/ "https://rstudio.github.io/reticulate/").

For a blog that outlines how to use the reticulate package with Amazon SageMaker AI, see [Using R with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/using-r-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/using-r-with-amazon-sagemaker/").

The following examples show how to use reticulate for specific use cases.

- For a notebook that describes how to use reticulate to do batch transform to make predictions,
  see [Batch Transform Using R with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_batch_transform/r_xgboost_batch_transform.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_batch_transform/r_xgboost_batch_transform.html").
- For a notebook that describes how to use reticulate to conduct hyperparameter tuning and generate predictions,
  see [Hyperparameter Optimization Using R with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_xgboost_hpo_batch_transform/r_xgboost_hpo_batch_transform.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_xgboost_hpo_batch_transform/r_xgboost_hpo_batch_transform.html").
