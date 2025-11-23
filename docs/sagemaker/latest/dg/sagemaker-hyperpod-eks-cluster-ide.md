# IDEs and Notebooks

Amazon SageMaker is introducing a new capability for SageMaker HyperPod EKS clusters,
which allows AI developers to run their interactive machine learning workloads directly on
the HyperPod EKS cluster. This feature introduces a new add-on called Amazon SageMaker
Spaces, that enables AI developers to create and manage self-contained environments for
running notebooks.

Administrators can use SageMaker HyperPod Console to install the add-on on their cluster,
and define default space configurations such as images, compute resources, local storage for
notebook settings (additional storage to be attached to their dev spaces), file systems, and
initialization scripts. A one-click installation option will be available with default
settings to simplify the admin experience. Admins can use the SageMaker HyperPod Console,
kubectl, or HyperPod CLI to install the operator, create default settings, and manage all
spaces in a centralized location.

AI developers can use HyperPod CLI to create, update, and delete dev spaces. They have the
flexibility to use default configurations provided by admins or customize settings. AI
developers can access their spaces on HyperPod using their local VS Code IDEs, and/or their
web browser that hosts their JupyterLab or CodeEditor IDE on custom DNS domain configured by
their admins. They can also use kubernetes’ port forwarding feature to access spaces in
their web browsers.

## Admin

- [Set up permissions](permission-setup.md "permission-setup.md")
- [Install SageMaker AI Spaces Add-on](operator-install.md "operator-install.md")
- [Customize add-on](customization.md "customization.md")
- [Add users and set up service accounts](add-user.md "add-user.md")
- [Limits](ds-limits.md "ds-limits.md")
- [Task governance for Interactive Spaces on HyperPod](task-governance.md "task-governance.md")
- [Observability](observability.md "observability.md")

## Data scientist

- [Create and manage spaces](browser-access.md "browser-access.md")
- [Remote access to SageMaker Spaces](vscode-access.md "vscode-access.md")

## SageMaker Spaces Managed Instance Pricing

The SageMaker Spaces Add-on/Operator does not incur any additional charge to the
customer. However, to support the SSH-over-SSM tunneling required for the _Remote IDE Connection_ feature, SageMaker Spaces uses an
AWS-managed instance. This instance is registered as an Advanced On-Premises Instance
under SSM, and therefore is billed per compute hour.

Please refer to the “On-Premises Instance Management” rate on the AWS Systems Manager
pricing page: AWS Systems Manager Pricing: [https://aws.amazon.com/systems-manager/pricing/](https://aws.amazon.com/systems-manager/pricing.com "https://aws.amazon.com/systems-manager/pricing.com")
