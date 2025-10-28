# Restrict with network ACL

A network access control list (NACL) is an optional layer of security for your VPC that
acts as a firewall for controlling traffic in and out of one or more subnets. You might
set up network ACLs with rules similar to your security groups in order to add an
additional layer of security to your VPC. For more information about the differences
between security groups and network ACLs, see
[Comparison of security groups and network ACLs](../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison "../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison").

However, in AMS Managed Multi-Account Landing Zone, in order for AMS to effectively manage
and monitor infrastructure, the use of NACLs is limited to following scope:

- NACLs are not supported in the Multi-Account Landing Zone Core accounts, i.e. Management account, Networking,
  Shared-Services, Logging and Security.
- NACLs are supported in Multi-Account Landing Zone Application accounts as long as they are only used as a "Deny"
  list and have "Allow All" to allow AMS monitoring and management operations.
  In large scale multi-account environments, you can also leverage features like
  centralized egress firewalls to control outbound traffic and/or AWS Transit Gateway routing tables
  in AMS Multi-Account Landing Zone to segregate network traffic among VPCs.
