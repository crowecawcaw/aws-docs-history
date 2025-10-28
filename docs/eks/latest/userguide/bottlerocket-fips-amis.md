**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Make your worker nodes FIPS ready with Bottlerocket FIPS AMIs

The Federal Information Processing Standard (FIPS) Publication 140-3 is a United States and Canadian government standard that specifies the security requirements for cryptographic modules that protect sensitive information. Bottlerocket makes it easier to adhere to FIPS by offering AMIs with a FIPS kernel.

These AMIs are preconfigured to use FIPS 140-3 validated cryptographic modules. This includes the Amazon Linux 2023 Kernel Crypto API Cryptographic Module and the AWS-LC Cryptographic Module.

Using Bottlerocket FIPS AMIs makes your worker nodes "FIPS ready" but not automatically "FIPS-compliant". For more information, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

## Considerations

- If your cluster uses isolated subnets, the Amazon ECR FIPS endpoint may not be accessible. This can cause the node bootstrap to fail. Make sure that your network configuration allows access to the necessary FIPS endpoints. For more information, see [Access a resource through a resource VPC endpoint](../../../vpc/latest/privatelink/use-resource-endpoint.md "../../../vpc/latest/privatelink/use-resource-endpoint.md") in the _AWS PrivateLink Guide_.
- If your cluster uses a subnet with [PrivateLink](vpc-interface-endpoints.md "vpc-interface-endpoints.md"), image pulls will fail because Amazon ECR FIPS endpoints are not available through PrivateLink.

## Create a managed node group with a Bottlerocket FIPS AMI

The Bottlerocket FIPS AMI comes in two variants to support your workloads:

- `BOTTLEROCKET_x86_64_FIPS`
- `BOTTLEROCKET_ARM_64_FIPS`

To create a managed node group with a Bottlerocket FIPS AMI, choose the applicable AMI type during the creation process. For more information, see [Create a managed node group for your cluster](create-managed-node-group.md "create-managed-node-group.md").

For more information on selecting FIPS-enabled variants, see [Retrieve recommended Bottlerocket AMI IDs](retrieve-ami-id-bottlerocket.md "retrieve-ami-id-bottlerocket.md").

## Disable the FIPS endpoint for non-supported AWS Regions

Bottlerocket FIPS AMIs are supported directly in the United States, including AWS GovCloud (US) Regions. For AWS Regions where the AMIs are available but not supported directly, you can still use the AMIs by creating a managed node group with a launch template.

The Bottlerocket FIPS AMI relies on the Amazon ECR FIPS endpoint during bootstrap, which are not generally available outside of the United States. To use the AMI for its FIPS kernel in AWS Regions that don’t have the Amazon ECR FIPS endpoint available, do these steps to disable the FIPS endpoint:

1. Create a new configuration file with the following content or incorporate the content into your existing configuration file.

```
[default]
use_fips_endpoint=false
```

1. Encode the file content as Base64 format.
2. In your launch template’s `UserData`, add the following encoded string using TOML format:

```
[settings.aws]
config = "<your-base64-encoded-string>"
```

For other settings, see Bottlerocket’s [Description of settings](https://github.com/bottlerocket-os/bottlerocket?tab=readme-ov-file#description-of-settings "https://github.com/bottlerocket-os/bottlerocket?tab=readme-ov-file#description-of-settings") on GitHub.

Here is an example of `UserData` in a launch template:

```
[settings]
motd = "Hello from eksctl!"
[settings.aws]
config = "W2RlZmF1bHRdCnVzZV9maXBzX2VuZHBvaW50PWZhbHNlCg==" # Base64-encoded string.
[settings.kubernetes]
api-server = "<api-server-endpoint>"
cluster-certificate = "<cluster-certificate-authority>"
cluster-name = "<cluster-name>"
...<other-settings>
```

For more information on creating a launch template with user data, see [Customize managed nodes with launch templates](launch-templates.md "launch-templates.md").
