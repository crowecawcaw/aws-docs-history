# MLCOST-10: Use managed build environments

Consider using managed notebooks instead of local ones, or
notebooks hosted on a server. Managed notebooks come bundled
with security, network, storage, compute capabilities that take
a lot of time and resources to develop locally. Managed ML build
environment also makes it easy to decide the type of machine you
prefer so you don’t need to manage any complex AMIs or security
groups-this makes it very easy to get started. It can also
provide access to GPUs and big machines with large amounts of
RAM that might not be possible on a local setup. 

## Implementation plan

- **Use Amazon SageMaker AI
  Notebooks** - An Amazon SageMaker AI notebook
  instance is a ML compute instance running the Jupyter
  Notebook App. SageMaker AI manages creating the instance and
  related resources. Use Jupyter notebooks in your notebook
  instance to prepare and process data, write code to train
  models, deploy models to SageMaker AI hosting, and test or
  validate your models. SageMaker AI provides hosted Jupyter
  notebooks that require no setup, so you can begin
  processing your training data sets immediately. With a few
  clicks in the SageMaker AI console, you can create a fully
  managed notebook instance, pre-loaded with useful
  libraries for machine learning. You only need to add your
  data.
- **Use Amazon SageMaker AI
  Studio** - Amazon SageMaker AI Studio provides a
  single, web-based visual interface where you can perform
  all ML development steps, improving data science team
  productivity. SageMaker AI Studio gives you complete access,
  control, and visibility into each step required to build,
  train, and deploy models. You can quickly upload data,
  create new notebooks, train and tune models, move back and
  forth between steps to adjust experiments, compare
  results, and deploy models to production all in one place,
  making you much more productive. All ML development
  activities including notebooks, experiment management,
  automatic model creation, debugging, and model and data
  drift detection can be performed with SageMaker AI Studio.
- **Use SageMaker AI Canvas**
  - Amazon SageMaker AI Canvas, a new visual, no code
  capability that allows business analysts to build ML
  models and generate accurate predictions without writing
  code or requiring ML expertise. Its intuitive user
  interface lets you browse and access disparate data
  sources in the cloud or on premises, combine datasets with
  the click of a button, train accurate models, and then
  generate new predictions once new data is available.

## Documents

- [Amazon SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [Amazon SageMaker AI Studio](../../../sagemaker/latest/dg/studio.md "../../../sagemaker/latest/dg/studio.md")
- [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md")

## Blogs

- [Amazon SageMaker AI Studio and SageMaker AI Notebook Instance now come
  with JupyterLab 3 notebooks to boost developer
  productivity](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-studio-and-sagemaker-notebook-instance-now-come-with-jupyterlab-3-notebooks-to-boost-developer-productivity/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-studio-and-sagemaker-notebook-instance-now-come-with-jupyterlab-3-notebooks-to-boost-developer-productivity/")
- [Build,
  Share, Deploy: how business analysts and data scientists
  achieve faster time-to-market using no-code ML and Amazon SageMaker AI Canvas](https://aws.amazon.com/blogs/machine-learning/build-share-deploy-how-business-analysts-and-data-scientists-achieve-faster-time-to-market-using-no-code-ml-and-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/build-share-deploy-how-business-analysts-and-data-scientists-achieve-faster-time-to-market-using-no-code-ml-and-amazon-sagemaker-canvas/")
- [Amazon SageMaker AI Canvas – a Visual, No Code Machine Learning
  Capability for Business Analysts](https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-canvas-a-visual-no-code-machine-learning-capability-for-business-analysts/ "https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-canvas-a-visual-no-code-machine-learning-capability-for-business-analysts/")

## Examples

- [SageMaker AI
  Example Notebooks](../../../sagemaker/latest/dg/howitworks-nbexamples.md "../../../sagemaker/latest/dg/howitworks-nbexamples.md")
