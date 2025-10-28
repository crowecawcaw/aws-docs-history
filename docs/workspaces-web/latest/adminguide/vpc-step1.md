# Allocating an Elastic IP address

Before you create your VPC, you must allocate an Elastic IP address in your WorkSpaces Secure Browser
Region. Once allocated, you can associate the Elastic IP address with your NAT gateway.
With an Elastic IP address, you can mask a failure of your streaming instance by rapidly
remapping the address to another streaming instance in your VPC. For more information,
see [Elastic IP
addresses](../../../vpc/latest/userguide/vpc-eips.md "../../../vpc/latest/userguide/vpc-eips.md").

###### Note

Charges might apply to Elastic IP addresses that you use. For more information,
see the [Elastic IP
addresses pricing page](https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses "https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses").

If you don't already have an Elastic IP address, complete the following steps. If
you want to use an existing Elastic IP address, you must first verify that it isn't
currently associated with another instance or network interface.

###### To allocate an Elastic IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**,
   choose **Elastic IPs**.
3. Choose **Allocate New Address**, and then choose
   **Allocate**.
4. Note the Elastic IP address shown on the console.
5. In the upper-right corner of the **Elastic IPs** pane, click
   the **×** icon to close the pane.
