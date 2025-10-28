# Create a VPC endpoint for AWS KMS

You can create a VPC endpoint for AWS KMS by using the Amazon VPC console or the Amazon VPC API. Follow the procedures to [Create an interface
endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") using one of the following values.

- To create a VPC endpoint for AWS KMS, use the following service name:

```
com.amazonaws.`region`.kms
```

For example, in the US West (Oregon) Region (`us-west-2`), the service
name would be:

```
com.amazonaws.us-west-2.kms
```

- To create a VPC endpoint that connects to an [AWS KMS FIPS
  endpoint](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md"), use the following service name:

```
com.amazonaws.`region`.kms-fips
```

For example, in the US West (Oregon) Region (`us-west-2`), the service
name would be:

```
com.amazonaws.us-west-2.kms-fips
```

To make it easier to use the VPC endpoint, you can enable a [private DNS name](../../../vpc/latest/privatelink/verify-domains.md "../../../vpc/latest/privatelink/verify-domains.md") for your VPC
endpoint. If you select the **Enable DNS Name** option, the standard AWS KMS
DNS hostname resolves to your VPC endpoint. For example,
`https://kms.us-west-2.amazonaws.com` would resolve to a VPC endpoint connected
to service name `com.amazonaws.us-west-2.kms`.

This option makes it easier to use the VPC endpoint. The AWS SDKs and AWS CLI use the
standard AWS KMS DNS hostname by default, so you do not need to specify the VPC endpoint URL in
applications and commands.

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the
_AWS PrivateLink Guide_.
