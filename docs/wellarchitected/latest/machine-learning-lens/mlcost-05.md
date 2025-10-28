# MLCOST-05: Use managed data labeling

Choose a managed labeling tool that provides automation and
access to cost-effective teams of human data labelers . It should
also provide flexibility to choose a variable number of labelers
for a given input. The tool should have a user interface, and
learn to label data by itself over time.

## Implementation plan

- **Use Amazon SageMaker Ground Truth** - To train a machine learning model, you
  need a large, high quality, labeled dataset.
  [Amazon SageMaker Ground Truth](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md") helps you build high-quality
  training datasets for your ML models. With Ground Truth,
  you can use ML along with workers from Amazon Mechanical
  Turk, a vendor company that you choose, or an internal,
  private workforce to create a labeled dataset. You can use
  the labeled dataset output from Ground Truth to train your
  own models. You can also use the output as a training data
  set for an Amazon SageMaker AI model.
- **Use Amazon SageMaker Ground Truth
  Plus** – Ground Truth Plus is a turn-key service
  that uses an expert workforce to deliver high-quality
  training datasets fast, and reduces costs by up to 40
  percent. Amazon SageMaker Ground Truth Plus enables you to
  easily create high-quality training datasets without
  having to build labeling applications and manage the
  labeling workforce on your own. By using this approach,
  you don’t need to have deep ML expertise or extensive
  knowledge of workflow design and quality management. You
  simply provide data along with labeling requirements and
  Ground Truth Plus sets up the data labeling workflows and
  manages them on your behalf in accordance with your
  requirements.

## Documents

- [Use
  Amazon SageMaker Ground Truth to Label Data](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md")
- [Use
  Amazon SageMaker Ground Truth Plus to Label Data](../../../sagemaker/latest/dg/gtp.md "../../../sagemaker/latest/dg/gtp.md")

## Blogs

- [Real-time
  data labeling pipeline for ML workflows using Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/real-time-data-labeling-pipeline-for-ml-workflows-using-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/real-time-data-labeling-pipeline-for-ml-workflows-using-amazon-sagemaker-ground-truth/")
- [Implementing
  a custom labeling GUI with built-in processing logic with
  Amazon SageMaker AI Ground](https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/")
  [Truth](https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/")
- [Amazon SageMaker Ground Truth Plus – Create Training Datasets
  Without Code or In-house Resources](https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-ground-truth-plus/ "https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-ground-truth-plus/")
- [Get
  Started with Amazon SageMaker Ground Truth Plus](https://pages.awscloud.com/GLOBAL_PM_LA_AmazonSageMaker AIGroundTruthPlus_20210820_7014z000000rQlg-registration.html "https://pages.awscloud.com/GLOBAL_PM_LA_AmazonSageMaker AIGroundTruthPlus_20210820_7014z000000rQlg-registration.html")

## Videos

- [Amazon SageMaker Ground Truth Plus](https://www.youtube.com/watch?v=HzuUKzV4bAg "https://www.youtube.com/watch?v=HzuUKzV4bAg")

## Examples

- [Bring
  your own model for SageMaker AI labeling workflows with active
  learning](https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb")
- [SageMaker AI
  Ground Truth recipe](https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe "https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe")
