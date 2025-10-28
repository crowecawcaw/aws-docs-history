# MLSEC-01: Validate ML data permissions, privacy, software, and license terms

ML libraries and packages handle data processing, model
development, training, and hosting. Establish a process to
review the privacy and license agreements for all software and
ML libraries needed throughout the ML lifecycle. Ensure these
agreements comply with your organization’s legal, privacy, and
security terms and conditions. These terms should not add any
limitations on your organization’s business plans.

## Implementation plan

- **Ensure data permissions for
  ML** - Verify whether the intended data can be
  used for machine learning, that it’s a legitimate purpose,
  and whether you require additional consent from the data
  owner or data subjects. Have a plan to handle data
  subjects that subsequently withdraw their consent. Ensure
  documentation of data permissions is maintained for
  compliance purposes.
- **Bootstrap instances with lifecycle
  management policies** - Create a lifecycle
  configuration with a reference to your package repository,
  and a script to install required packages.
- **Evaluate package integrations that
  require external lookup services** - Based on your
  data privacy requirements, opt out of data collection when
  necessary. Minimize data exposure through trusted
  relationships. Evaluate the privacy policies and the
  license terms for ML packages that might collect data.
- **Use prebuilt containers** - Start with pre-packaged and verified containers to
  quickly provide support for commonly used dependencies.
  For
  example, [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers "https://aws.amazon.com/machine-learning/containers") contain several deep
  learning framework libraries and tools including
  TensorFlow, PyTorch, and Apache MXNet.

## Documents

- [Amazon
  Well-Architected Security Pillar for Software
  Integrity](../security-pillar/protecting-compute.md "../security-pillar/protecting-compute.md")
- [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers "https://aws.amazon.com/machine-learning/containers")
- [Installing
  External Libraries and Kernels on Notebook
  Instances](../../../sagemaker/latest/dg/nbi-add-external.md "../../../sagemaker/latest/dg/nbi-add-external.md")
- [AWS License Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/")
- [Lifecycle
  Configuration Best Practices](../../../sagemaker/latest/dg/nbi-lifecycle-config-install.md "../../../sagemaker/latest/dg/nbi-lifecycle-config-install.md")

## Blogs

- [Private
  package installation in Amazon SageMaker AI running in
  internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/ "https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/")
- [Machine
  Learning Best Practices in Financial Services](https://aws.amazon.com/blogs/machine-learning/machine-learning-best-practices-in-financial-services/ "https://aws.amazon.com/blogs/machine-learning/machine-learning-best-practices-in-financial-services/")

## Videos

- [Machine
  Learning Best Practices in Financial Services](https://youtu.be/HlSEUvApDZE?t=578 "https://youtu.be/HlSEUvApDZE?t=578")
