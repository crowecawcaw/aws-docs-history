# Network locations for SRT Listener inputs

SRT Listener inputs support the following network locations:

- **AWS**: Standard cloud deployment. MediaLive
  allocates Elastic IP addresses for the input destinations.
- **VPC**: Deployment in your Amazon Virtual Private Cloud. MediaLive
  allocates Elastic Network Interfaces (ENI) in your VPC for the input
  destinations. When you create an SRT Listener input in a VPC, you must specify
  the VPC subnets and security groups.
- **ON_PREMISES**: MediaLive Anywhere deployment. For
  on-premises deployments, you must specify the IP addresses and network
  configuration when you create the input.
