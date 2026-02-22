# Evaluating your trained model

An evaluation recipe is a YAML configuration file that defines how your Amazon Nova model
evaluation job is executed. With this recipe, you can assess the performance of a base or
trained model against common benchmarks or your own custom datasets. Metrics can be stored in
Amazon S3 or TensorBoard. The evaluation provides quantitative metrics that help you assess model
performance across various tasks to determine if further customization is needed.

Model evaluation is an offline process, where models are tested against fixed benchmarks
with predefined answers. They are not assessed in real-time or against live user interactions.
For real-time evaluations, you can evaluate the model after it is deployed to Amazon Bedrock by calling
the Amazon Bedrock runtime APIs.

###### Topics

- [Available benchmark
  tasks](customize-fine-tune-evaluate-available-tasks.md "customize-fine-tune-evaluate-available-tasks.md")
- [Understanding the recipe
  parameters](customize-fine-tune-evaluate-understand-modify.md "customize-fine-tune-evaluate-understand-modify.md")
- [Evaluation recipe
  examples](customize-fine-tune-evaluate-recipe-examples.md "customize-fine-tune-evaluate-recipe-examples.md")
- [Starting an evaluation job](customize-fine-tune-evaluate-start-job.md "customize-fine-tune-evaluate-start-job.md")
- [Accessing and analyzing
  evaluation results](customize-fine-tune-evaluate-access-results.md "customize-fine-tune-evaluate-access-results.md")
