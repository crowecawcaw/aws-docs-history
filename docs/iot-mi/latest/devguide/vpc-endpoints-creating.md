

# Creating an interface VPC endpoint for AWS IoT Managed Integrations
<a name="vpc-endpoints-creating"></a>

You can create a VPC endpoint for the AWS IoT Managed Integrations service using either the Amazon VPC Console or the AWS CLI (AWS CLI).

## To create an interface VPC endpoint for AWS IoT Managed Integrations (console)
<a name="vpc-endpoints-creating-console"></a>

1. Open the Amazon VPC Console at [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, choose **AWS services**.

1. For **Service name**, select the service name that corresponds to your AWS Region. For example:
   + `com.amazonaws.ca-central-1.iotmanagedintegrations.api`
   + `com.amazonaws.eu-west-1.iotmanagedintegrations.api`

1. For **VPC**, select the VPC from which you'll access AWS IoT Managed Integrations.

1. For **Additional settings**, **Enable DNS name** is selected by default. We recommend that you keep this setting. This ensures that requests to the AWS IoT Managed Integrations public service endpoints resolve to your Amazon VPC endpoint.

1. For **Subnets**, select the subnets in which to create endpoint network interfaces. You can select one subnet per Availability Zone.

1. For **IP address type**, choose from the following options:
   + **IPv4**: Assign IPv4 addresses to the endpoint network interfaces
   + **IPv6**: Assign IPv6 addresses to the endpoint network interfaces (supported only if all selected subnets are IPv6-only)
   + **Dualstack**: Assign both IPv4 and IPv6 addresses to the endpoint network interfaces

1. For **Security groups**, select the security groups to associate with the endpoint network interfaces. The security group rules must allow communication between the endpoint network interface and the resources in your VPC that communicate with the service.

1. For **Policy**, choose **Full access** to allow all operations by all principals on all resources over the interface endpoint. To restrict access, choose **Custom** and specify a policy.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and value.

1. Choose **Create endpoint**.

## To create an interface VPC endpoint for IoT Managed Integrations (AWS CLI)
<a name="vpc-endpoints-creating-cli"></a>

Use the [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) command and specify the VPC ID, VPC endpoint type (interface), service name, subnets that will use the endpoint, and security groups to associate with the endpoint network interfaces.

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --route-table-ids rtb-12345678 \
  --service-name com.amazonaws.ca-central-1.iotmanagedintegrations.api \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-12345678 subnet-87654321 \
  --security-group-ids sg-12345678
```