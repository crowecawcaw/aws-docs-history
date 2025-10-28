# Amazon SageMaker notebook instances

An Amazon SageMaker notebook instance is a machine learning (ML) compute instance running the
Jupyter Notebook application. One of the best ways for machine learning (ML) practitioners
to use Amazon SageMaker AI is to train and deploy ML models using SageMaker notebook instances. The SageMaker
notebook instances help create the environment by initiating Jupyter servers on Amazon Elastic Compute Cloud
(Amazon EC2) and providing preconfigured kernels with the following packages: the Amazon SageMaker Python
SDK, AWS SDK for Python (Boto3), AWS Command Line Interface (AWS CLI), Conda, Pandas, deep learning framework libraries, and
other libraries for data science and machine learning.

Use Jupyter notebooks in your notebook instance to:

- prepare and process data
- write code to train models
- deploy models to SageMaker hosting
- test or validate your models
  For information about pricing with Amazon SageMaker notebook instance, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

## Maintenance

SageMaker AI updates the underlying software for Amazon SageMaker Notebook Instances at least once
every 90 days. Some maintenance updates, such as operating system upgrades, may require
your application to be taken offline for a short period of time. It is not possible to
perform any operations during this period while the underlying software is being
updated. We recommend that you restart your notebooks at least once every 30 days to
automatically consume patches.

For more information, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Machine Learning with the SageMaker Python

SDK

To train, validate, deploy, and evaluate an ML model in a SageMaker notebook instance, use
the SageMaker Python SDK. The SageMaker Python SDK abstracts AWS SDK for Python (Boto3) and SageMaker API
operations. It enables you to integrate with and orchestrate other AWS services, such
as Amazon Simple Storage Service (Amazon S3) for saving data and model artifacts, Amazon Elastic Container Registry (ECR) for importing
and servicing the ML models, Amazon Elastic Compute Cloud (Amazon EC2) for training and inference.

You can also take advantage of SageMaker AI features that help you deal with every stage of a
complete ML cycle: data labeling, data preprocessing, model training, model deployment,
evaluation on prediction performance, and monitoring the quality of model in
production.

If you're a first-time SageMaker AI user, we recommend you to use the SageMaker Python SDK,
following the end-to-end ML tutorial. To find the open source documentation, see the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

###### Topics

- [Tutorial for building models with Notebook Instances](gs-console.md "gs-console.md")
- [AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md")
- [Amazon Linux 2 notebook instances](nbi-al2.md "nbi-al2.md")
- [JupyterLab versioning](nbi-jl.md "nbi-jl.md")
- [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md "howitworks-create-ws.md")
- [Access Notebook Instances](howitworks-access-ws.md "howitworks-access-ws.md")
- [Update a Notebook Instance](nbi-update.md "nbi-update.md")
- [Customization of a SageMaker notebook instance
  using an LCC script](notebook-lifecycle-config.md "notebook-lifecycle-config.md")
- [Set the Notebook Kernel](howitworks-set-kernel.md "howitworks-set-kernel.md")
- [Git repositories with SageMaker AI Notebook Instances](nbi-git-repo.md "nbi-git-repo.md")
- [Notebook Instance Metadata](nbi-metadata.md "nbi-metadata.md")
- [Monitor Jupyter Logs in Amazon CloudWatch Logs](jupyter-logs.md "jupyter-logs.md")
