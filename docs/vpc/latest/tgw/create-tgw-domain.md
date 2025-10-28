# Create a static source multicast domain in AWS Transit Gateway

If you have not already done so, review the available multicast domain attributes. For
more information, see [Multicast domains in AWS Transit Gateway](multicast-domains-about.md "multicast-domains-about.md").

###### To create a static multicast domain using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Choose **Create transit gateway multicast domain**.
4. For **Name tag**, enter a name to identify the domain.
5. For **Transit gateway ID**, choose the transit gateway that processes the
   multicast traffic.
6. For **IGMPv2 support**, clear the checkbox.
7. For **Static sources support**, select the checkbox.
8. To automatically accept cross-account subnet associations for this multicast
   domain, select **Auto accept shared associations**.
9. Choose **Create transit gateway multicast domain**.

###### To create a static multicast domain using the AWS CLI

Use the [create-transit-gateway-multicast-domain](../../../cli/latest/reference/ec2/create-transit-gateway-multicast-domain.md "../../../cli/latest/reference/ec2/create-transit-gateway-multicast-domain.md") command.

```
aws ec2 create-transit-gateway-multicast-domain --transit-gateway-id `tgw-0xexampleid12345` --options StaticSourcesSupport=enable,Igmpv2Support=disable
```
