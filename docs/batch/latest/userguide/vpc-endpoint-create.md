

# Create an interface endpoint for AWS Batch
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for AWS Batch using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create an interface endpoint for AWS Batch using the following service names:
+ **com.amazonaws.**{{region}} **.batch**
+ **com.amazonaws.**{{region}} **.batch-fips** *(For FIPS-compliant endpoints, see [AWS Batch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/batch.html))*

For example:

```
com.amazonaws.{{us-east-2}}.batch
```

```
com.amazonaws.{{us-east-2}}.batch-fips
```

In the `aws-cn` partition, the format is different:

```
cn.com.amazonaws.{{region}}.batch
```

For example:

```
cn.com.amazonaws.cn-northwest-1.batch
```

## Private DNS names for AWS Batch interface endpoints
<a name="vpc-endpoint-service-names"></a>

If you enable private DNS for the interface endpoint, you can use specific DNS names to connect to AWS Batch, We provide these options:
+ **batch.**{{region}} **.amazonaws.com**
+ **batch.**{{region}} **.api.aws**

For FIPS-compliant endpoints:
+ **batch-fips.**{{region}} **.api.aws**
+ **fips.batch.**{{region}} **.amazonaws.com** *is not supported*

For more information, see [Access a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.