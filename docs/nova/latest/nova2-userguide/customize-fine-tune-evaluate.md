# Evaluate your custom training jobs

An evaluation recipe is a YAML configuration file that defines how your Amazon Nova model
evaluation job is executed. With this recipe, you can assess the performance of a base or
trained model against common benchmarks or your own custom datasets. Metrics can be stored
in Amazon S3 or TensorBoard. The evaluation provides quantitative metrics that help you assess
model performance across various tasks to determine if further customization is
needed.

Model evaluation is an offline process, where models are tested against fixed benchmarks
with predefined answers. They are not assessed in real-time or against live user
interactions. For real-time evaluations, you can evaluate the model after it is deployed to
Amazon Bedrock by calling the Amazon Bedrock runtime APIs.

For detailed instructions about evaluating you trained Amazon Nova models, see the [Evaluating your trained model](../../../sagemaker/latest/dg/nova-hp-evaluate.md "../../../sagemaker/latest/dg/nova-hp-evaluate.md") section from SageMaker user guide.
