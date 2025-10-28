# Identify a shared multicast domain in AWS Transit Gateway

Owners and consumers can identify shared multicast domains using the Amazon Virtual Private Cloud and
AWS CLI

###### To identify a shared multicast domain using the \*Amazon Virtual Private Cloud Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Multicast Domains**.
3. Select your multicast domain.
4. On the **Transit Multicast Domain Details** page, view the
   **Owner ID** to identify the AWS account ID of
   the multicast domain.

###### To identify a shared multicast domain using the AWS CLI

Use the [describe-transit-gateway-multicast-domains](../../../cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.md "../../../cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.md") command. The command returns
the multicast domains that you own and multicast domains that are shared with you.
`OwnerId` shows the AWS account ID of the multicast domain owner.
