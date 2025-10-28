# MLSUS-13: Optimize models for inference

Improve efficiency of your models and thus use less resources
for inference by compiling the models into optimized forms. 

## Implementation plan

- **Use open-source model
  compilers** - Libraries such as
  [Treelite](https://treelite.readthedocs.io/en/latest/ "https://treelite.readthedocs.io/en/latest/")
  (for decision tree ensembles) improve the prediction
  throughput of models, due to more efficient use of compute
  resources.
- **Use third-party tools** -
  Solutions like
  [Hugging
  Face Infinity](https://aws.amazon.com/marketplace/pp/prodview-vprkfzlr3xljo "https://aws.amazon.com/marketplace/pp/prodview-vprkfzlr3xljo") allow you to accelerate transformer
  models and run inference not only on GPUs but also on
  CPUs.
- **Use Amazon SageMaker AI
  Neo** -
  [SageMaker AI
  Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/") enables developers to optimize ML models for
  inference on SageMaker AI in the cloud and supported devices
  at the edge. SageMaker AI Neo runtime consumes as little as
  one-tenth the footprint of a deep learning framework while
  optimizing models to perform up to 25 times faster with no
  loss in accuracy.

## Documents

- [Optimize
  model performance using Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 3, deployment and
  monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/")
- [Unlock
  near 3x performance gains with XGBoost and Amazon SageMaker AI Neo](https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/ "https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/")
