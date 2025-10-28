# Creating an interface VPC endpoint for AWS IoT Managed integrations

You can create a VPC endpoint for the AWS IoT Managed integrations service using either the Amazon VPC Console or the AWS CLI (AWS CLI).

## To create an interface VPC endpoint for AWS IoT Managed integrations (console)

1. Open the Amazon VPC Console at
   [Amazon VPC Console](https://console.aws.amazon.com/https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, choose **AWS services**.
5. For **Service name**, select the service name that corresponds to your AWS Region. For example:
   - `com.amazonaws.ca-central-1.iotmanagedintegrations.api`
   - `com.amazonaws.eu-west-1.iotmanagedintegrations.api`

6. For **VPC**, select the VPC from which you'll access AWS IoT Managed integrations.
7. For **Additional settings**, **Enable DNS name** is selected by default. We recommend that you keep this setting.
   This ensures that requests to the AWS IoT Managed integrations public service endpoints resolve to your Amazon VPC endpoint.
8. For **Subnets**, select the subnets in which to create endpoint network interfaces.
   You can select one subnet per Availability Zone.
9. For **IP address type**, choose from the following options:
   - **IPv4**: Assign IPv4 addresses to the endpoint network interfaces
   - **IPv6**: Assign IPv6 addresses to the endpoint network interfaces (supported only if all selected subnets are IPv6-only)
   - **Dualstack**: Assign both IPv4 and IPv6 addresses to the endpoint network interfaces

10. For **Security groups**, select the security groups to associate with the endpoint network interfaces.
    The security group rules must allow communication between the endpoint network interface and the resources in your
    VPC that communicate with the service.
11. For **Policy**, choose **Full access**
    to allow all operations by all principals on all resources over the interface endpoint. To restrict access,
    choose **Custom** and specify a policy.
12. (Optional) To add a tag, choose **Add new tag** and enter the tag key and value.
13. Choose **Create endpoint**.

## To create an interface VPC endpoint for IoT Managed Integrations (AWS CLI)

Use the
[create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md")
command and specify the VPC ID, VPC endpoint type (interface), service name, subnets that will use the endpoint, and
security groups to associate with the endpoint network interfaces.

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --route-table-ids rtb-12345678 \
  --service-name com.amazonaws.ca-central-1.iotmanagedintegrations.api \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-12345678 subnet-87654321 \
  --security-group-ids sg-12345678
```
