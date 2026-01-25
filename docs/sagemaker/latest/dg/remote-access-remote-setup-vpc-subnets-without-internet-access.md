# Set

up Studio to run with subnets without internet access within a VPC

This guide shows you how to connect to Amazon SageMaker Studio spaces from Visual Studio Code
when your Amazon SageMaker AI domain runs in private subnets without internet access. You’ll
learn about connectivity requirements and setup options to establish secure remote
connections in isolated network environments.

You can configure Amazon SageMaker Studio to run in VPC only mode with subnets without
internet access. This setup enhances security for your machine learning workloads by
operating in an isolated network environment where all traffic flows through the
VPC. To enable external communications while maintaining security, use VPC endpoints
for AWS services and configure VPC PrivateLink for required AWS
dependencies.

###### Topics

- [Studio remote access network requirements](#remote-access-remote-setup-vpc-subnets-without-internet-access-network-requirements "#remote-access-remote-setup-vpc-subnets-without-internet-access-network-requirements")
- [Setup Studio remote access network](#remote-access-remote-setup-vpc-subnets-without-internet-access-setup "#remote-access-remote-setup-vpc-subnets-without-internet-access-setup")

## Studio remote access network requirements

**VPC mode limitations** Studio in VPC mode
only supports private subnets. Studio cannot work with subnets directly
attached with an Internet Gateway (IGW). Remote VS Code connections share the
same limitations as SageMaker AI. For more information, see [Connect
Studio notebooks in a VPC to external resources](studio-notebooks-and-internet-access.md "studio-notebooks-and-internet-access.md").

### VPC PrivateLink requirements

When SageMaker AI runs in private subnets, configure these SSM VPC endpoints in addition to standard
VPC endpoints required for SageMaker. For more information, see [Connect Studio
Through a VPC Endpoint](studio-interface-endpoint.md "studio-interface-endpoint.md").

- `com.amazonaws.`REGION`.ssm`
- `com.amazonaws.`REGION`.ssmmessages`

**VPC endpoint policy recommendations**

The following are the recommended VPC endpoint policies that allow the necessary actions for remote access while using the `aws:PrincipalIsAWSService` condition to ensure only AWS services like Amazon SageMaker AI can make the calls. For more information about the `aws:PrincipalIsAWSService` condition key, see [the documentation](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalisawsservice "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalisawsservice").

**SSM endpoint policy**

Use the following policy for the `com.amazonaws.`REGION`.ssm` endpoint:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "ssm:CreateActivation",
                "ssm:RegisterManagedInstance",
                "ssm:DeleteActivation",
                "ssm:DeregisterManagedInstance",
                "ssm:AddTagsToResource",
                "ssm:UpdateInstanceInformation",
                "ssm:UpdateInstanceAssociationStatus",
                "ssm:DescribeInstanceInformation",
                "ssm:ListInstanceAssociations",
                "ssm:ListAssociations",
                "ssm:GetDocument",
                "ssm:PutInventory"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "true"
                }
            }
        }
    ]
}
```

**SSM Messages endpoint policy**

Use the following policy for the `com.amazonaws.`REGION`.ssmmessages` endpoint:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "ssmmessages:CreateControlChannel",
                "ssmmessages:CreateDataChannel",
                "ssmmessages:OpenControlChannel",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "true"
                }
            }
        }
    ]
}
```

**VS Code specific network requirements**

Remote VS Code connection requires VS Code remote development, which needs
specific network access to install the remote server and extensions. See the
[remote
development FAQ](https://code.visualstudio.com/docs/remote/faq "https://code.visualstudio.com/docs/remote/faq") in the Visual Studio Code documentation for full network
requirements. The following is a summary of the requirements:

- Access to Microsoft’s VS Code server endpoints is needed to install
  and update the VS Code remote server.
- Access to Visual Studio Marketplace and related CDN endpoints is required for
  installing VS Code extensions through the extension panel
  (alternatively, extensions can be installed manually using VSIX files
  without internet connection).
- Some extensions may require access to additional endpoints for
  downloading their specific dependencies. See the extension’s
  documentation for their specific connectivity requirements.

## Setup Studio remote access network

Your have two options to connect your local Visual Studio Code to Studio spaces
in private subnets:

- HTTP Proxy
- Pre-packaged VS Code remote server and extensions

### Set up HTTP Proxy with controlled allow-listing

When your Studio space is behind a firewall or proxy, allow access to
VS Code server and extension-related CDNs and endpoints.

1. Set up a public subnet to run the HTTP proxy (such as Squid),
   where you can configure which websites to allow. Ensure that the
   HTTP proxy is accessible by SageMaker spaces.
2. The public subnet can be in the same VPC used by the Studio
   or in separate VPC peered with all the VPCs used by
   Amazon SageMaker AI domains.

### Set up Pre-packaged Visual Studio Code remote server and extensions

When your Studio spaces can’t access external endpoints to download
VS Code remote server and extensions, you can pre-package them. With this
approach, you export a tarball containing the `.VS
 Code-server` directory for a specific version of VS Code.
Then, you use a SageMaker AI Lifecycle Configuration (LCC) script to copy and
extract the tarball into the home directory
(`/home/sagemaker-user`) of the Studio spaces.
This LCC-based solution works with both AWS-provided and custom images.
Even when you’re not using private subnets, this approach accelerates the
setup of the VS Code remote server and pre-installed extensions.

**Instructions for pre-packaging your VS Code remote
server and extensions**

1. Install VS Code on your local machine.
2. Launch a Linux-based (x64) Docker container with SSH enabled,
   either locally or via a Studio space with internet access. We
   recommend using a temporary Studio space with remote access and
   internet enabled for simplicity.
3. Connect your installed VS Code to the local Docker container via
   Remote SSH or connect to the Studio space via the Studio
   remote VS Code feature. VS Code installs the remote server into
   `.VS Code-server` in the home directory in
   the remote container during connection. See [Example Dockerfile usage for pre-packaging your VS Code remote server
   and extensions](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-dockerfile "remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-dockerfile") for more information.
4. After connecting remotely, ensure you use the VS Code Default
   profile.
5. Install the required VS Code extensions and validate their
   functionality. For example, create and run a notebook to install
   Jupyter notebook-related extensions in the VS Code remote
   server.

Ensure you [install the AWS Toolkit for Visual Studio Code extension](../../../toolkit-for-visual-studio/latest/user-guide/setup.md "../../../toolkit-for-visual-studio/latest/user-guide/setup.md") after connecting
to the remote container. 6. Archive the `$HOME/.VS Code-server` directory
(for example, `VS
 Code-server-with-extensions-for-1.100.2.tar.gz`) in
either the local Docker container or in the terminal of the remotely
connected Studio space. 7. Upload the tarball to Amazon S3. 8. Create an [LCC script](studio-lifecycle-configurations.md "studio-lifecycle-configurations.md") ([Example LCC script (LCC-install-VS Code-server-v1.100.2)](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc "remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc")) that:

    * Downloads the specific archive from Amazon S3.
    * Extracts it into the home directory when a Studio
     space in a private subnet launches.

9. (Optional) Extend the LCC script to support per-user VS Code
   server tarballs stored in user-specific Amazon S3 folders.
10. (Optional) Maintain version-specific LCC scripts ([Example LCC script (LCC-install-VS Code-server-v1.100.2)](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc "remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc")) that you can attach to your spaces, ensuring compatibility
    between your local VS Code client and the remote server.
