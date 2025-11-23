# MLCOST04-BP09 Start training with small datasets

Start experimentation with smaller datasets on a small compute
instance or local system. This approach allows you to iterate
quickly at low cost. After the experimentation period, scale up to
train with the full dataset available on a separate compute cluster.
Choose the appropriate storage layer for training data based on the
performance requirements.

**Desired outcome:** You can develop
your machine learning models cost-effectively by starting with small
datasets for rapid iteration and experimentation. When you're
confident in your approach, you scale up to the full dataset on
appropriate compute resources. This progressive scaling methodology
optimizes both development time and infrastructure costs while
maintaining the flexibility to refine your models before committing
to full-scale training.

**Common anti-patterns:**

- Immediately training with the full dataset on large instances,
  leading to excessive costs during experimentation.
- Using the same compute resources for both experimentation and
  full-scale training.
- Not planning for the transition from small-scale to large-scale
  training.

**Benefits of establishing this best
practice:**

- Reduced costs during the experimentation phase.
- Faster iteration cycles for model development.
- More efficient use of compute resources.
- Ability to identify and fix issues early in the development
  process.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning development often requires multiple iterations to
achieve optimal results. Using smaller, representative samples of
your dataset during initial experimentation can significantly
reduce costs and increase productivity. This approach lets you
rapidly test various model architectures, hyperparameters, and
preprocessing techniques without the expense and time required to
process the full dataset.

When implementing this approach, check that your smaller dataset
properly represents the characteristics of your full dataset to
avoid developing models that don't generalize well. Once you've
established effective approaches using the smaller dataset, you
can scale up your training to use the complete dataset on
appropriately sized compute resources.

The cloud makes this approach particularly powerful, as you can
scale your compute resources to match your current phase of
development. For example, you might use a notebook instance with
modest resources during experimentation, then transition to
distributed training on a cluster of more powerful instances when
you're ready for full-scale training.

### Implementation steps

1. **Create a representative subset of
   your data**. Extract a small but representative
   sample of your full dataset that maintains the same
   distribution of features and classes as your original data.
   Aim for 10-20% of your data or a size that can be processed
   on your local machine or small instance.
2. **Set up SageMaker AI notebook instances
   for experimentation**.
   [Amazon SageMaker AI notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md") provide a hosted Jupyter
   environment ideal for exploring and experimenting with your
   sample dataset. Choose a smaller instance type to keep costs
   low during experimentation.
3. **Configure notebook lifecycle
   management**. Use
   [lifecycle
   configuration scripts](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples "https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples") to automate the setup of your
   development environment, including installing necessary
   libraries and dependencies when your notebook instance
   starts.
4. **Develop and iterate on your
   model**. Use the notebook environment to build,
   train and evaluate your models on the sample data. Take
   advantage of this faster iteration cycle to explore
   different approaches, hyperparameters, and preprocessing
   techniques.
5. **Test scaling
   considerations**. Before moving to full-scale
   training, test your code with slightly larger data samples
   to identify scaling issues that might arise when processing
   the full dataset.
6. **Prepare for distributed
   training**. Once your approach is validated with
   the sample data, refactor your code as needed to support
   distributed training using SageMaker AI's distributed training
   capabilities.
7. **Scale up compute resources for full
   training**. Launch appropriately sized training
   instances or clusters for your full-scale training job.
   SageMaker AI training jobs allow you to select the instance
   type and count that matches your workload requirements.
8. **Monitor training metrics and
   costs**. Use Amazon CloudWatch to track the
   performance and resource utilization of your training jobs
   to check that they're running efficiently.

## Resources

**Related documents:**

- [Amazon SageMaker AI notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [Amazon SageMaker AI Studio Lab](../../../sagemaker/latest/dg/studio-lab.md "../../../sagemaker/latest/dg/studio-lab.md")
- [Customization
  of a SageMaker AI notebook instance using an LCC script](../../../sagemaker/latest/dg/notebook-lifecycle-config.md "../../../sagemaker/latest/dg/notebook-lifecycle-config.md")
- [Distributed
  training in Amazon SageMaker AI](../../../sagemaker/latest/dg/distributed-training.md "../../../sagemaker/latest/dg/distributed-training.md")

**Related examples:**

- [SageMaker AI
  Notebook Instance Lifecycle Config Samples](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples "https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples")
- [SageMaker AI
  Local Mode](https://github.com/aws-samples/amazon-sagemaker-local-mode "https://github.com/aws-samples/amazon-sagemaker-local-mode")
