

# Create an interface VPC endpoint for AWS IoT SiteWise
<a name="vpc-endpoint-create"></a>

To create a VPC endpoint for the AWS IoT SiteWise service, use either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for AWS IoT SiteWise by using one of the following service names:
+ For the **data plane** API operations, use the following service name: 

  ```
  com.amazonaws.{{region}}.iotsitewise.data
  ```
+ For the **control plane** API operations, use the following service name: 

  ```
  com.amazonaws.{{region}}.iotsitewise.api
  ```