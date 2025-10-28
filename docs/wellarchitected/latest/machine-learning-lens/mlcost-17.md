# MLCOST-17: Start training with small datasets

Start experimentation with smaller datasets on a small compute
instance or local system. This approach allows you to iterate
quickly at low cost. After the experimentation period, scale up
to train with the full dataset available on a separate compute
cluster. Choose the appropriate storage layer for training data
based on the performance requirements.

## Implementation plan

- **Use SageMaker AI notebooks** - Notebooks are a popular way to explore and experiment with data in small quantities. Iterating with a small sample of the dataset locally and then scaling to train on the full dataset in a distributed manner is common in machine learning. [Amazon SageMaker AI](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md") [notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md") provide a hosted Jupyter environment that can be used to explore small samples of data.

## Documents

- [Use
  Amazon SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [Customize
  a Notebook Instance Using a Lifecycle Configuration
  Script](../../../sagemaker/latest/dg/notebook-lifecycle-config.md "../../../sagemaker/latest/dg/notebook-lifecycle-config.md")
