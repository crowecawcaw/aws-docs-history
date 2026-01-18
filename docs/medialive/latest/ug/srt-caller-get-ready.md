# Plan for delivery using Amazon VPC

You might set up the MediaLive channel for the SRT output to have [output endpoints in Amazon Virtual Private Cloud](delivery-out-vpc.md "delivery-out-vpc.md") (Amazon VPC). Following
are some guidelines for setting up the secret in Secrets Manager and for delivery the output to
MediaConnect (if MediaConnect is the destination).

## Considerations for Secrets Manager

SRT outputs are always encrypted, therefore AWS Secrets Manager is always involved. There
are specific requirements for the VPC subnet where you will create the
channel:

- The subnet for the channel must have a Secrets Manager endpoint.
- The subnet for the channel and the Secrets Manager endpoint must use the same
  security group, which means that the same security group must be associated
  with the subnet and with the endpoint.

## Considerations

for MediaConnect

You might be delivering to a MediaConnect that also uses a VPC. This means that the SRT
output egress from the MediaLive channel is on your VPC and that the MediaConnect flow has a
VPC interface.

- The administrator for your VPC must ensure that there is an appropriate
  route between MediaLive and MediaConnect.
