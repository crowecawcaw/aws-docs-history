

# Identify a shared multicast domain in AWS Transit Gateway
<a name="sharing-identify"></a>

Owners and consumers can identify shared multicast domains using the Amazon Virtual Private Cloud and AWS CLI

**To identify a shared multicast domain using the \*Amazon Virtual Private Cloud Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Multicast Domains**.

1. Select your multicast domain.

1. On the **Transit Multicast Domain Details **page, view the **Owner ID** to identify the AWS account ID of the multicast domain.

**To identify a shared multicast domain using the AWS CLI**  
Use the [describe-transit-gateway-multicast-domains](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-multicast-domains.html) command. The command returns the multicast domains that you own and multicast domains that are shared with you. `OwnerId` shows the AWS account ID of the multicast domain owner.