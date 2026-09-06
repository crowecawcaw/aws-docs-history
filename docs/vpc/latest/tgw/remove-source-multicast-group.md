

# Deregister sources from a multicast group in AWS Transit Gateway
<a name="remove-source-multicast-group"></a>

You don't need to follow this procedure unless you manually added a source to the multicast group.

**To remove a source using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Groups** tab.

1. Select the sources, and then choose **Remove source**.

**To remove a source using the AWS CLI**  
Use the [deregister-transit-gateway-multicast-group-sources](https://docs.aws.amazon.com/cli/latest/reference/ec2/deregister-transit-gateway-multicast-group-sources.html) command.