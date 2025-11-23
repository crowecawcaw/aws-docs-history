# Connect your local Visual Studio Code to Amazon SageMaker Unified Studio spaces with

remote access

You can connect remotely from Visual Studio Code (VS Code) to Amazon SageMaker Unified Studio Spaces. You can use
your customized local VS Code setup, including AI-assisted development tools and custom
extensions, with the scalable compute resources in Amazon SageMaker Unified Studio.

## Key Concepts

**VPC**

Amazon Virtual Private Cloud (VPC) is a fundamental building block, allowing you to
provision a logically isolated virtual network within the AWS Cloud.

**Amazon SageMaker Unified Studio Space**

Amazon SageMaker Unified Studio provides compute Spaces for integrated development environments (IDEs) that you
can use to author code. There are two IDE applications available in Amazon SageMaker Unified Studio: JupyterLab and
Code Editor. A JupyterLab Space is created in your project by default, and you can create
additional Spaces as desired.

**Remote Connection**

A secure SSH-over-SSM tunnel between your local VS Code and a SageMaker Unified Studio
Space. This connection enables interactive development and code execution in VS Code using
Amazon SageMaker Unified Studio compute resources.
