# MLCOST04-BP02 Use managed build environments

Using managed build environments for machine learning development
instead of local setups provides significant cost, time, and
resource advantages. Managed notebooks come pre-configured with
security, networking, storage, and compute capabilities that would
otherwise require extensive development and maintenance effort.
These environments also offer flexible machine selection, including
access to powerful GPUs and high-memory instances that may be
impractical in local setups.

**Desired outcome:** You can quickly
start machine learning development work without spending time
setting up infrastructure, managing dependencies, or configuring
development environments. You gain access to scalable compute
resources, including specialized hardware like GPUs, and benefit
from built-in security and collaboration features, allowing you to
focus on building ML models rather than managing infrastructure.

**Common anti-patterns:**

- Spending excessive time configuring local development
  environments for each project.
- Encountering hardware limitations when training complex models
  locally.
- Struggling with inconsistent development environments across
  team members.
- Managing security and networking configurations manually.
- Inability to scale resources up or down based on workload
  requirements.

**Benefits of establishing this best
practice:**

- Reduced time to start development with pre-configured
  environments.
- Access to powerful compute resources on demand.
- Consistent development environments for team members.
- Built-in security, networking, and storage capabilities.
- Simplified collaboration and sharing of notebooks and models.
- Cost optimization through pay-for-what-you-use model.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing machine learning projects, your development
environment plays a critical role in productivity and efficiency.
Local development environments often lead to inconsistencies
between team members, dependency conflicts, and hardware
limitations. Managed build environments address these challenges
by providing standardized, scalable, and secure solutions for ML
development.

Amazon SageMaker AI offers several managed environment options
tailored to different user needs and expertise levels. These
include SageMaker AI Notebook Instances for individual developers,
SageMaker AI Studio for comprehensive ML development, and SageMaker AI
Canvas for no-code ML solutions. These environments come
pre-configured with the necessary tools and libraries, saving
setup time and fostering consistency.

These managed environments integrate seamlessly with other AWS
services, making it simple to access data stored in Amazon S3, use
specialized hardware like GPUs, and deploy models to production
endpoints. They also provide built-in security features, version
control, and collaboration capabilities that would be difficult to
implement in a local setup.

### Implementation steps

1. **Evaluate your ML development
   needs**. Begin by assessing your team's
   requirements, including technical expertise, project
   complexity, and compute resource needs. Identify which
   SageMaker AI offering best matches these requirements.
2. **Use Amazon SageMaker AI Notebook
   Instances**. Set up SageMaker AI Notebook Instances
   which provide a fully managed Jupyter notebook environment.
   These instances come pre-loaded with popular ML frameworks
   and libraries, allowing you to start working immediately.
3. **Implement Amazon SageMaker AI
   Studio**. Deploy SageMaker AI Studio as your
   comprehensive ML development environment. SageMaker AI Studio
   provides a web-based visual interface where your team can
   perform ML development steps from data preparation to model
   deployment. Access Studio by creating a SageMaker AI domain
   through the SageMaker AI console, which enables team management
   and resource sharing capabilities.
4. **Deploy SageMaker AI Canvas for business
   users**. Implement SageMaker AI Canvas for business
   analysts and non-technical team members who need to create
   ML models without coding. Canvas provides an intuitive
   visual interface for importing data, creating models, and
   generating predictions.
5. **Set up proper IAM roles and
   permissions**. Configure appropriate IAM roles for
   your SageMaker AI environments to provide secure access to AWS
   resources. Create specific roles that follow the principle
   of least privilege, granting only the permissions necessary
   for your ML workflows.
6. **Configure data access and
   storage**. Set up connections between your
   SageMaker AI environments and data sources such as Amazon S3,
   Amazon Redshift, or Amazon RDS. Configure appropriate
   permissions to access these data sources securely.
7. **Implement version control and
   collaboration**. Integrate your managed
   environments with version control systems like Git to track
   changes to notebooks and code. Use SageMaker AI Studio's
   built-in collaboration features to share work among team
   members.
8. **Optimize for cost
   efficiency**. Configure auto-shutdown policies for
   notebook instances when they're idle to reduce costs.
   Monitor resource usage and adjust instance types as needed
   to balance performance and cost.
9. **Use SageMaker AI HyperPod for
   large-scale training**. For distributed training of
   large models, use
   [SageMaker AI
   HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md") which provides purpose-built infrastructure
   with automatic checkpoint storage and recovery, optimizing
   resource utilization for long-running training jobs.
10. **Enable SageMaker AI JupyterLab 3
    features**. Take advantage of the productivity
    improvements in JupyterLab 3, which is available in both
    SageMaker AI Studio and Notebook Instances, providing better
    performance and enhanced features for developers.

## Resources

**Related documents:**

- [Amazon SageMaker AI Studio](../../../sagemaker/latest/dg/studio.md "../../../sagemaker/latest/dg/studio.md")
- [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md")
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
- [Amazon SageMaker AI notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [SageMaker AI
  JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
- [Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
