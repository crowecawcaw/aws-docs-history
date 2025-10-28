# Create an interface VPC endpoint for

AWS IoT SiteWise

To create a VPC endpoint for the AWS IoT SiteWise service, use either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Access
an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

Create a VPC endpoint for AWS IoT SiteWise by using one of the following service names:

- For the **data plane** API operations, use the following
  service name:

```
com.amazonaws.`region`.iotsitewise.data
```

- For the **control plane** API operations, use the
  following service name:

```
com.amazonaws.`region`.iotsitewise.api
```
