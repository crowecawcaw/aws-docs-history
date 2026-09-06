

# Set up Studio to run with subnets without internet access within a VPC
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access"></a>

This guide shows you how to connect to Amazon SageMaker Studio spaces from your Remote IDE when your Amazon SageMaker AI domain runs in private subnets without internet access. You’ll learn about connectivity requirements and setup options to establish secure remote connections in isolated network environments.

You can configure Amazon SageMaker Studio to run in VPC only mode with subnets without internet access. This setup enhances security for your machine learning workloads by operating in an isolated network environment where all traffic flows through the VPC. To enable external communications while maintaining security, use VPC endpoints for AWS services and configure VPC PrivateLink for required AWS dependencies.

**IDE support for private subnet connections**

The following table shows the supported connection methods for each Remote IDE when connecting to Studio spaces in private subnets without internet access.


| Connection method | VS Code | Kiro | Cursor | 
| --- | --- | --- | --- | 
| HTTP Proxy support | Supported | Supported | Not supported | 
| Pre-packaged remote server and extensions | Supported | Not supported | Not supported | 

**Important**  
Cursor is not supported for connecting to Studio spaces in private subnets without outbound internet access.

**Topics**
+ [Studio remote access network requirements](#remote-access-remote-setup-vpc-subnets-without-internet-access-network-requirements)
+ [Setup Studio remote access network](#remote-access-remote-setup-vpc-subnets-without-internet-access-setup)

## Studio remote access network requirements
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access-network-requirements"></a>

**VPC mode limitations** Studio in VPC mode only supports private subnets. Studio cannot work with subnets directly attached with an Internet Gateway (IGW). Remote IDE connections share the same limitations as SageMaker AI. For more information, see [Connect Studio notebooks in a VPC to external resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html).

### VPC PrivateLink requirements
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access-vpc-privatelink-requirements"></a>

When SageMaker AI runs in private subnets, configure these SSM VPC endpoints in addition to standard VPC endpoints required for SageMaker. For more information, see [Connect Studio Through a VPC Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-interface-endpoint.html).
+ `com.amazonaws.{{REGION}}.ssm`
+ `com.amazonaws.{{REGION}}.ssmmessages`

**VPC endpoint policy recommendations**

The following are the recommended VPC endpoint policies that allow the necessary actions for remote access while using the `aws:PrincipalIsAWSService` condition to ensure only AWS services like Amazon SageMaker AI can make the calls. For more information about the `aws:PrincipalIsAWSService` condition key, see [the documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalisawsservice).

**SSM endpoint policy**

Use the following policy for the `com.amazonaws.{{REGION}}.ssm` endpoint:

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

Use the following policy for the `com.amazonaws.{{REGION}}.ssmmessages` endpoint:

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

Remote VS Code connection requires VS Code remote development, which needs specific network access to install the remote server and extensions. See the [remote development FAQ](https://code.visualstudio.com/docs/remote/faq) in the Visual Studio Code documentation for full network requirements. The following is a summary of the requirements:
+ Access to Microsoft’s VS Code server endpoints is needed to install and update the VS Code remote server.
+ Access to Visual Studio Marketplace and related CDN endpoints is required for installing VS Code extensions through the extension panel (alternatively, extensions can be installed manually using VSIX files without internet connection).
+ Some extensions may require access to additional endpoints for downloading their specific dependencies. See the extension’s documentation for their specific connectivity requirements.

**Kiro specific network requirements**

Remote Kiro connection requires Kiro remote development, which needs specific network access to install the remote server and extensions. For firewall and proxy server configuration, see [Kiro firewall configuration](https://kiro.dev/docs/privacy-and-security/firewalls/). The requirements are similar to VS Code:
+ Access to Kiro server endpoints is needed to install and update the Kiro remote server.
+ Access to extension marketplace and related CDN endpoints is required for installing Kiro extensions through the extension panel.
+ Some extensions may require access to additional endpoints for downloading their specific dependencies. See the extension’s documentation for their specific connectivity requirements.

## Setup Studio remote access network
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access-setup"></a>

You have the following options to connect your Remote IDE to Studio spaces in private subnets:
+ HTTP Proxy (supported for VS Code and Kiro)
+ Pre-packaged remote server and extensions (VS Code only)

### Set up HTTP Proxy with controlled allow-listing
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access-setup-http-proxy-with-controlled-allow-listing"></a>

When your Studio space is behind a firewall or proxy, allow access to your IDE server and extension-related CDNs and endpoints.

1. Set up a public subnet to run the HTTP proxy (such as Squid), where you can configure which websites to allow. Ensure that the HTTP proxy is accessible by SageMaker spaces.

1. The public subnet can be in the same VPC used by the Studio or in separate VPC peered with all the VPCs used by Amazon SageMaker AI domains.

### Set up Pre-packaged remote server and extensions (VS Code only)
<a name="remote-access-remote-setup-vpc-subnets-without-internet-access-setup-pre-packaged-vs-code-remote-server-and-extensions"></a>

**Note**  
This option is only available for Visual Studio Code. Kiro and Cursor do not support pre-packaged remote server setup.

When your Studio spaces can’t access external endpoints to download VS Code remote server and extensions, you can pre-package them. With this approach, you export a tarball containing the `.VS Code-server` directory for a specific version of VS Code. Then, you use a SageMaker AI Lifecycle Configuration (LCC) script to copy and extract the tarball into the home directory (`/home/sagemaker-user`) of the Studio spaces. This LCC-based solution works with both AWS-provided and custom images. Even when you’re not using private subnets, this approach accelerates the setup of the VS Code remote server and pre-installed extensions.

**Instructions for pre-packaging your VS Code remote server and extensions**

1. Install VS Code on your local machine.

1. Launch a Linux-based (x64) Docker container with SSH enabled, either locally or via a Studio space with internet access. We recommend using a temporary Studio space with remote access and internet enabled for simplicity.

1. Connect your installed VS Code to the local Docker container via Remote SSH or connect to the Studio space via the Studio remote VS Code feature. VS Code installs the remote server into `.VS Code-server` in the home directory in the remote container during connection. See [Example Dockerfile usage for pre-packaging your VS Code remote server and extensions](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-dockerfile) for more information.

1. After connecting remotely, ensure you use the VS Code Default profile.

1. Install the required VS Code extensions and validate their functionality. For example, create and run a notebook to install Jupyter notebook-related extensions in the VS Code remote server.

   Ensure you [install the AWS Toolkit for Visual Studio Code extension](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup.html) after connecting to the remote container.

1. Archive the `$HOME/.VS Code-server` directory (for example, `VS Code-server-with-extensions-for-1.100.2.tar.gz`) in either the local Docker container or in the terminal of the remotely connected Studio space.

1. Upload the tarball to Amazon S3.

1. Create an [LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html) ([Example LCC script (LCC-install-VS Code-server-v1.100.2)](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc)) that:
   + Downloads the specific archive from Amazon S3.
   + Extracts it into the home directory when a Studio space in a private subnet launches.

1. (Optional) Extend the LCC script to support per-user VS Code server tarballs stored in user-specific Amazon S3 folders.

1. (Optional) Maintain version-specific LCC scripts ([Example LCC script (LCC-install-VS Code-server-v1.100.2)](remote-access-local-ide-setup-vpc-no-internet.md#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions-example-lcc)) that you can attach to your spaces, ensuring compatibility between your local VS Code client and the remote server.