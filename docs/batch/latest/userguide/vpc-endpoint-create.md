# Create an interface endpoint for AWS Batch

You can create an interface endpoint for AWS Batch using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For
more information, see [Create an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS Batch using the following service names:

- **com.amazonaws.**`region`
  **.batch**
- **com.amazonaws.**`region`
  **.batch-fips**
  _(For FIPS-compliant endpoints, see [AWS Batch endpoints and quotas](../../../general/latest/gr/batch.md "../../../general/latest/gr/batch.md"))_
  For example:

```
com.amazonaws.`us-east-2`.batch
```

```
com.amazonaws.`us-east-2`.batch-fips
```

In the `aws-cn` partition, the format is different:

```
cn.com.amazonaws.`region`.batch
```

For example:

```
cn.com.amazonaws.cn-northwest-1.batch
```

## Private DNS names for AWS Batch interface endpoints

If you enable private DNS for the interface endpoint, you can use specific DNS names to connect to AWS Batch,
We provide these options:

- **batch.**`region`
  **.amazonaws.com**
- **batch.**`region`
  **.api.aws**

For FIPS-compliant endpoints:

- **batch-fips.**`region`
  **.api.aws**
- **fips.batch.**`region`
  **.amazonaws.com** _is not supported_

For more information, see [Access a service through an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the _AWS PrivateLink Guide_.
