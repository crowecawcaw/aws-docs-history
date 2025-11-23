# Modify a transit gateway in AWS Transit Gateway

You can modify the configuration options for a transit gateway. When you modify a transit
gateway, any existing transit gateway attachments don't experience any service
interruptions.

You cannot modify a transit gateway that has been shared with you.

You cannot remove a CIDR block for the transit gateway if any of the IP addresses
are currently used for a [Connect peer](tgw-connect.md "tgw-connect.md").

###### Note

You must enable Encryption Support on a Transit Gateway explicitly to encrypt traffic between your VPCs
that have encryption controls turned on.

Traffic between two VPCs in enforce mode (without exclusions) is end-to-end encrypted via the TGW.
Encryption on Transit Gateway also allows you to connect two VPCs that are in different Encryption Controls
modes. Traffic between VPCs (one in enforce mode and another in Monitor or OFF mode) is guaranteed to be
encrypted only between the VPC running in enforce mode, up to the Transit Gateway. Beyond that, it depends
on the resource that is running in the non-enforced VPC and is not guaranteed to be encrypted between the
Transit Gateway and the non-enforced VPC.

For more detailed information, see [Encryption Support for AWS Transit Gateway](tgw-encryption-support.md "tgw-encryption-support.md").

###### To modify a transit gateway

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit
   Gateways**.
3. Choose the transit gateway to modify.
4. Choose **Actions**, **Modify transit
   gateway**.
5. Modify the options as needed, and choose **Modify transit
   gateway**.

###### To modify your transit gateway using the AWS CLI

Use the [modify-transit-gateway](../../../cli/latest/reference/ec2/modify-transit-gateway.md "../../../cli/latest/reference/ec2/modify-transit-gateway.md") command.
