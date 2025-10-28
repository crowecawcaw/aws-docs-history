# Custom Amazon Machine Images (AMIs) for SageMaker HyperPod

clusters

Using base Amazon Machine Images (AMIs) provided and made public by Amazon SageMaker HyperPod,
you can build custom AMIs. With a custom AMI, you can create specialized environments for
AI workloads with pre-configured software stacks, driver customizations, proprietary
dependencies, and security agents. This capability eliminates the need for complex
post-launch bootstrapping using lifecycle configuration scripts.

With custom AMIs, you can standardize environments across different stages,
accelerate startup times, and have full control over your runtime environment
while leveraging SageMaker HyperPod's infrastructure capabilities and scaling advantages. This
helps you maintain control over your AI infrastructure while still benefiting
from SageMaker HyperPod's optimized base runtime.

You can build upon the SageMaker HyperPod performance-tuned base images by adding
security agents, compliance tools, and specialized libraries while preserving all the
distributed training benefits. This capability removes the previously required choice between infrastructure
optimization and organizational security policies.

The custom AMI experience integrates seamlessly with established enterprise security
workflows. Security teams build hardened images using SageMaker HyperPod's public AMIs as a
base, and AI platform teams can specify these custom AMIs when creating or updating
clusters through the SageMaker HyperPod APIs. The APIs validate image compatibility, handle
necessary permissions, and maintain backwards compatibility so existing workflows
continue functioning. Organizations with stringent security protocols can eliminate the error-prone
alternative of installing security agents at runtime through lifecycle scripts. By
aligning with enterprise security practices rather than forcing organizations to adapt
their protocols to SageMaker HyperPod's limitations, custom AMIs remove a common
barrier to adoption for security-conscious organizations running critical AI
workloads.

For release notes on updates to the public AMIs, see [Public AMI releases](sagemaker-hyperpod-release-public-ami.md "sagemaker-hyperpod-release-public-ami.md").
To learn how to get started with building a custom AMI and using it in your HyperPod clusters,
see the following topics.

###### Topics

- [Build a custom AMI](hyperpod-custom-ami-how-to.md "hyperpod-custom-ami-how-to.md")
- [Cluster management with custom AMIs](hyperpod-custom-ami-cluster-management.md "hyperpod-custom-ami-cluster-management.md")
