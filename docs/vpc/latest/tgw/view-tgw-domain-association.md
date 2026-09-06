

# View multicast domain associations in AWS Transit Gateway
<a name="view-tgw-domain-association"></a>

View your multicast domains to verify that they are available, and that they contain the appropriate subnets and attachments.

**To view a multicast domain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Associations** tab.

**To view a multicast domain using the AWS CLI**  
Use the [describe-transit-gateway-multicast-domains](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.html) command.