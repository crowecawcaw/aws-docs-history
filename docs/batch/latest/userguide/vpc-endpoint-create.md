# Create an interface endpoint for AWS Batch

You can create an interface endpoint for AWS Batch using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For
more information, see [Create an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS Batch using the following service name:

```
com.amazonaws.`region`.batch
```

For example:

```
com.amazonaws.`us-east-2`.batch
```

In the `aws-cn` partition, the format is different:

```
cn.com.amazonaws.`region`.batch
```

For example:

```
cn.com.amazonaws.`cn-northwest-1`.batch
```

If you enable private DNS for the interface endpoint, you can make API requests to AWS Batch using its default
Regional DNS name. For example, `batch.us-east-1.amazonaws.com`.

For more information, see [Access a service through an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the _AWS PrivateLink Guide_.
