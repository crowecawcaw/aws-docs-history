# MLCOST03-BP01 Use managed data labeling

Use managed labeling tools that provide automation and access to
cost-effective teams of human data labelers. These tools should
offer flexibility to choose a variable number of labelers for each
input, include a user-friendly interface, and incorporate learning
capabilities to improve labeling efficiency over time.

**Desired outcome:** You have access
to high-quality labeled datasets for your machine learning models
without building and managing your own labeling infrastructure. Your
data labeling process is streamlined, cost-efficient, and scales
according to your needs, allowing you to focus on model development
rather than data preparation logistics.

**Common anti-patterns:**

- Building custom data labeling infrastructure from scratch.
- Relying solely on in-house teams for labeling tasks regardless
  of scale.
- Using labeling solutions that don't improve through machine
  learning.
- Managing inconsistent labeling quality without proper oversight
  tools.

**Benefits of establishing this best
practice:**

- Reduce time-to-market for ML models by accelerating the data
  labeling process.
- Lower total labeling costs through efficient automation and
  on-demand workforce.
- Improve labeling quality and consistency through specialized
  tools and workflows.
- Scale labeling operations up or down based on project
  requirements.
- Focus your team's effort on model development rather than
  labeling infrastructure.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To build effective machine learning models, you need large,
high-quality labeled datasets. Creating these datasets manually is
time-consuming, expensive, and difficult to scale. By using
managed data labeling services, you can accelerate this critical
step in the ML development process while controlling costs and
maintaining quality.

Managed data labeling combines human intelligence with machine
learning to improve efficiency over time. As your models process
more data, they can begin to automate parts of the labeling
process, reducing costs and time required. These services also
provide quality control mechanisms through consensus models, where
multiple labelers evaluate the same data to check accuracy.

When selecting a managed data labeling solution, consider factors
like the types of data you need to label (like images, text, and
video), the complexity of your labeling tasks, integration with
your existing ML workflow, and cost structure. The right solution
will scale with your needs and provide consistent, high-quality
labeled data.

### Implementation steps

1. **Assess your data labeling
   requirements**. Define what types of data you need
   labeled (images, text, audio, or video), the complexity of
   annotations required, expected volume, and quality
   standards. Determine whether you need specialized domain
   expertise for your labeling tasks.
2. **Use Amazon SageMaker Ground Truth**. To train a machine learning model, you
   need a large, high-quality, labeled dataset.
   [Amazon SageMaker Ground Truth](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md") assists you to build
   high-quality training datasets for your ML models. With
   Ground Truth, you can use ML along with workers from a
   vendor company that you choose, or an internal, private
   workforce to create a labeled dataset. You can use the
   labeled dataset output from Ground Truth to train your own
   models. You can also use the output as a training data set
   for an Amazon SageMaker AI model.
3. **Use Amazon SageMaker Ground Truth
   Plus**. Ground Truth Plus is a turn-key service
   that uses an expert workforce to deliver high-quality
   training datasets fast, and reduces costs by up to 40
   percent.
   [Amazon SageMaker Ground Truth Plus](../../../sagemaker/latest/dg/gtp.md "../../../sagemaker/latest/dg/gtp.md") enables you to create
   high-quality training datasets without having to build
   labeling applications and manage the labeling workforce on
   your own. By using this approach, you don't need to have
   deep ML expertise or extensive knowledge of workflow design
   and quality management. You simply provide data along with
   labeling requirements and Ground Truth Plus sets up the data
   labeling workflows and manages them on your behalf in
   accordance with your requirements.
4. **Configure active learning
   workflows**. Set up your labeling projects to use
   active learning, where the system learns from human
   annotations and begins to automate labeling for similar
   items. This reduces the number of items requiring manual
   labeling over time, improving efficiency and reducing costs.
   Amazon SageMaker Ground Truth provides built-in support for
   active learning.
5. **Implement quality control
   mechanisms**. Configure your labeling jobs to use
   multiple workers per data item and determine consensus
   approaches based on your quality requirements. Monitor
   labeling performance and adjust your quality control
   parameters as needed.
6. **Set up real-time data labeling
   pipelines**. For ongoing ML projects, establish
   continuous data labeling pipelines that can process new data
   as it becomes available. This way, your models can be
   regularly retrained with fresh data.
7. **Create custom labeling interfaces
   when needed**. For specialized labeling tasks, use
   Ground Truth's custom template capabilities to create
   tailored labeling interfaces that make the process more
   efficient for your specific use case.
8. **Use enhanced Ground Truth
   capabilities**. Use improved Ground Truth Plus
   features that provide up to 40% cost reduction through
   expert workforce management and automated quality control
   mechanisms.
9. **Use foundation models for
   pre-labeling**. Use generative AI models through
   Amazon Bedrock to assist with initial data labeling, which
   can then be verified by human labelers. This hybrid approach
   can significantly accelerate the labeling process while
   maintaining quality control.

## Resources

**Related documents:**

- [Training
  data labeling using humans with Amazon SageMaker Ground Truth](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md")
- [Use
  Amazon SageMaker Ground Truth Plus to Label Data](../../../sagemaker/latest/dg/gtp.md "../../../sagemaker/latest/dg/gtp.md")
- [Using
  the Amazon Mechanical Turk Workforce](../../../sagemaker/latest/dg/sms-workforce-management-public.md "../../../sagemaker/latest/dg/sms-workforce-management-public.md")
- [Automate
  data labeling](../../../sagemaker/latest/dg/sms-automated-labeling.md "../../../sagemaker/latest/dg/sms-automated-labeling.md")
- [Custom
  labeling workflows](../../../sagemaker/latest/dg/sms-custom-templates.md "../../../sagemaker/latest/dg/sms-custom-templates.md")
- [Annotation
  consolidation](../../../sagemaker/latest/dg/sms-annotation-consolidation.md "../../../sagemaker/latest/dg/sms-annotation-consolidation.md")
- [Ground
  Truth streaming labeling jobs](../../../sagemaker/latest/dg/sms-streaming-labeling-job.md "../../../sagemaker/latest/dg/sms-streaming-labeling-job.md")
- [Implementing
  a custom labeling GUI with built-in processing logic with
  Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/")

**Related examples:**

- [Bring
  your own model for SageMaker AI labeling workflows with active
  learning](https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb")
- [SageMaker AI
  Ground Truth recipe](https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe "https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe")
