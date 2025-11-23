# Configuring Amazon SageMaker Unified Studio for

Remote Access

## Prerequisites

###### Note

Certain features in Amazon SageMaker Unified Studio may maintain active sessions even after you log out of Amazon SageMaker Unified Studio or the associated IAM Identity Center/SSO session. Sometimes, these disconnected sessions can persist for up to 12 hours. Affected features include:

- Spaces
- Local IDE (Visual Studio Code) Support
- Workflows
- ML Experiments (MLFlow)
- Connections
- Hyperpod
- Amazon SageMaker partner applications
  To ensure the security of your environment, administrators must review and adjust session
  duration settings where possible and be cautious when using shared workstations or public
  networks.

To establish a remote connection from VS Code to a Amazon SageMaker Unified Studio Space, you must have the
following prerequisites:

- Access to a Amazon SageMaker Unified Studio Domain with proper network connectivity and AWS Identity Center
  setup. To create an Amazon SageMaker Unified Studio domain, see [Domains](working-with-domains.md "working-with-domains.md").
  - By default, Amazon SageMaker Unified Studio Projects create Spaces in VpcOnly mode. To support remote
    connection, you have three network configuration options:
    - **Public Internet Access**: Configure your Amazon SageMaker Unified Studio
      Projects to allow public internet access by setting
      `sagemakerDomainNetworkType` to `PublicInternetOnly`.
    - **VPC with NAT Gateway**: Keep Spaces in
      `VpcOnly` mode and attach a NAT gateway to your VPC to provide internet
      access. This is the default configuration with Unified Studio Quick Setup for manually
      setting it up. For more details, see [Internet
      gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md").
    - **Isolated VPC with VPC Endpoints**: Keep your domain
      completely isolated from the internet by configuring VPC endpoints. See [Configuring Isolated VPC for Remote Access](configuring-isolated-vpc-remote-access.md "configuring-isolated-vpc-remote-access.md") for detailed setup
      instructions.

- Project role permissions to call SageMaker StartSession. This is the API that enables
  remote connectivity to a Space. The Amazon SageMaker Unified Studio managed policy has already been updated to
  provide you access to call this API for the Spaces they own. If you are managing your own
  roles, ensure the role has the following policy:

```
{
    "Sid": "AllowStartSessionForSpaceRemoteConnection",
    "Effect": "Allow",
    "Action": [
        "sagemaker:StartSession"
    ],
    "Resource": "arn:aws:sagemaker:*:*:space/*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/AmazonDataZoneProject": "${aws:PrincipalTag/AmazonDataZoneProject}",
            "aws:ResourceTag/AmazonDataZoneUser": "${aws:PrincipalTag/datazone:userId}"
        }
    }
}
```

- VS Code with Microsoft Remote SSH (version 0.74.0 or higher), and AWS Toolkit (version 3.87.0 or higher) extension installed on your local machine.

###### Important

Remote Space connections are currently not supported for TIP (Trusted Identity
Propagation) enabled project profiles. For instructions on how to set the
`enableTrustedIdentityPropagationPermissions` to false to use remote connection for
Spaces, see [Trusted identity propagation](trusted-identity-propagation.md "trusted-identity-propagation.md").

### VS Code specific network requirements

Remote VS Code connection requires VS Code remote development, which needs specific
network access to install the remote server and extensions. See the [remote development FAQ](https://code.visualstudio.com/docs/remote/faq "https://code.visualstudio.com/docs/remote/faq") in the VS
Code documentation for full network requirements. The following is a summary of the
requirements:

- Access to Microsoft's VS Code server endpoints is required to install and update the VS
  Code remote server.
- Access to VS Marketplace and related CDN endpoints is required for installing VS Code
  extensions through the extension panel (alternatively, extensions can be installed manually
  using VSIX files without internet connection).
- Some extensions may require access to additional endpoints for downloading their
  specific dependencies. See the extension's documentation for their specific connectivity
  requirements.
