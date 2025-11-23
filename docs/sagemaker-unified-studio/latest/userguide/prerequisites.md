# Prerequisites

Before connecting VS Code remotely to a SageMaker Unified Studio Space, ensure you
have the following prerequisites:

- Access to an existing domain in Amazon SageMaker Unified Studio.
- AWS Toolkit for VS Code extension. For more details, see [Installing the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md "../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md").
  - Install the AWS Toolkit: Open VS Code, navigate to Extensions and
    search for **AWS Toolkit**. Choose
    **Install** to install the latest
    version of the official AWS Toolkit extension. The AWS Toolkit
    extension will appear on the VS Code sidebar.

  ###### Note

  For the best experience, use AWS Toolkit version 3.87.0 or
  higher when connecting to Amazon SageMaker Unified Studio in VS Code.

- System Requirements
  - **VS Code Version**: v1.90 or later
    (latest stable version recommended)

- Operating Systems
  - macOS 13+
  - Windows 10/11
  - Linux (official Microsoft VS Code distribution required)

- Space Instance Requirements
  - **Memory**: Minimum 8GB RAM
  - **Unsupported Instance Types**:
    ml.t3.medium, ml.c7i.large, ml.c6i.large, ml.c6id.large,
    ml.c5.large
  - **Recommended**: Use instances with 8GB+
    memory for optimal performance

- Image Compatibility
  - **SageMaker Distribution**: Version 2.8
    or later
  - **Custom Images**: Must follow SageMaker
    custom image specifications

- **Extension Compatibility**: Not all VS Code
  extensions support remote development

###### Important

Remote Space connections are currently not supported for TIP (Trusted Identity
Propagation) enabled Projects. For instructions on how to set the
`enableTrustedIdentityPropagationPermissions` to false to use remote
connection for Spaces, see [Trusted identity propagation](../adminguide/trusted-identity-propagation.md "../adminguide/trusted-identity-propagation.md").
