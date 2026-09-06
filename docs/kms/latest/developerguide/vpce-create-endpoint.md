

# Create a VPC endpoint for AWS KMS
<a name="vpce-create-endpoint"></a>

You can create a VPC endpoint for AWS KMS by using the Amazon VPC console or the Amazon VPC API. Follow the procedures to [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) using one of the following values.
+ To create a VPC endpoint for AWS KMS, use the following service name: 

  ```
  com.amazonaws.{{region}}.kms
  ```

  For example, in the US West (Oregon) Region (`us-west-2`), the service name would be:

  ```
  com.amazonaws.us-west-2.kms
  ```
+ To create a VPC endpoint that connects to an [AWS KMS FIPS endpoint](https://docs.aws.amazon.com/general/latest/gr/kms.html), use the following service name:

  ```
  com.amazonaws.{{region}}.kms-fips
  ```

  For example, in the US West (Oregon) Region (`us-west-2`), the service name would be:

  ```
  com.amazonaws.us-west-2.kms-fips
  ```

To make it easier to use the VPC endpoint, you can enable a [private DNS name](https://docs.aws.amazon.com/vpc/latest/privatelink/verify-domains.html) for your VPC endpoint. If you select the **Enable DNS Name** option, the standard AWS KMS DNS hostname resolves to your VPC endpoint. For example, `https://kms.us-west-2.amazonaws.com` would resolve to a VPC endpoint connected to service name `com.amazonaws.us-west-2.kms`.

This option makes it easier to use the VPC endpoint. The AWS SDKs and AWS CLI use the standard AWS KMS DNS hostname by default, so you do not need to specify the VPC endpoint URL in applications and commands.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.