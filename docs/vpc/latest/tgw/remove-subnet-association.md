

# Disassociate a subnet from a multicast domain in AWS Transit Gateway
<a name="remove-subnet-association"></a>

Use the following procedure to disassociate subnets from a multicast domain.

**To disassociate subnets using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Associations** tab.

1. Select the subnet, and then choose **Actions**, **Delete association**.

**To disassociate subnets using the AWS CLI**  
Use the [disassociate-transit-gateway-multicast-domain](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-transit-gateway-multicast-domain.html) command.