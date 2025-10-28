# Deregister sources from a multicast group in AWS Transit Gateway

You don't need to follow this procedure unless you manually added a source to the
multicast group.

###### To remove a source using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Select the multicast domain.
4. Choose the **Groups** tab.
5. Select the sources, and then choose **Remove source**.

###### To remove a source using the AWS CLI

Use the [deregister-transit-gateway-multicast-group-sources](../../../cli/latest/reference/ec2/deregister-transit-gateway-multicast-group-sources.md "../../../cli/latest/reference/ec2/deregister-transit-gateway-multicast-group-sources.md") command.
