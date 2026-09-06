

# Create an IGMP multicast domain in AWS Transit Gateway
<a name="create-tgw-igmp-domain"></a>

If you have not already done so, review the available multicast domain attributes. For more information, see [Multicast domains in AWS Transit Gateway](multicast-domains-about.md).

**To create an IGMP multicast domain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Choose **Create transit gateway multicast domain**.

1. For **Name tag**, enter a name for the domain.

1. For **Transit gateway ID**, choose the transit gateway that processes the multicast traffic.

1. For **IGMPv2 support**, select the checkbox.

1. For **Static sources support**, clear the checkbox.

1. To automatically accept cross-account subnet associations for this multicast domain, select **Auto accept shared associations**.

1. Choose **Create transit gateway multicast domain**.

**To create an IGMP multicast domain using the AWS CLI**  
Use the [create-transit-gateway-multicast-domain](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-multicast-domain.html) command.

```
aws ec2 create-transit-gateway-multicast-domain --transit-gateway-id {{tgw-0xexampleid12345}} --options StaticSourcesSupport=disable,Igmpv2Support=enable
```