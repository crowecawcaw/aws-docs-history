# Accessing instances using bastions

All access to resources inside AMS-managed accounts, for both customers and AMS operators, is gated by the use of
bastion hosts. We maintain both Linux and Windows RDP bastions for access for both Multi-account landing zone (MALZ) and Single-account landing zone (SALZ) AMS Advanced accounts.

Your bastions are accessible only over your private connection (VPN or AWS Direct Connect)DX.
In addition to firewalling to prevent inbound traffic, bastions are regularly re-provisioned (with existing credentials) on a fixed schedule.

###### Note

For information on moving files to an EC2 instance, see
[File transfer: Local Windows or MAC PC to Linux Amazon EC2](../appguide/qs-file-transfer.md "../appguide/qs-file-transfer.md").

MALZ
You access your account instances by logging in to a bastion instance with your Active Directory (AD) credentials. Amazon uses bastions located in the
perimeter network VPC (networking account), and you use your customer bastions, located in your Customer Bastions subnet in the shared services account.

When your AMS environment is initially onboarded, you have two SSH bastions and two RDP bastions depending on your choice.

SALZ
You access your account instances by logging in to a bastion instance with your Active Directory (AD) credentials. AMS uses bastions located in the
perimeter network subnets, and you use bastions located in your private subnets.

When your account is initially onboarded, you have two RDP and two SSH bastions, by default.

###### Note

As part of the single-account landing zone, AMS provides both RDP (Windows) and SSH (Linux) bastions to access your stacks; however, you can
choose whether you want only RDP bastions or only SSH bastions. To request that only RDP, or only SSH bastions are maintained, submit a service request.

In order to access an instance, you need:

- Access granted to the stack. To get access granted to a stack, see
  [Stack Admin Access | Grant](../ctref/management-access-stack-admin-access-grant.md "../ctref/management-access-stack-admin-access-grant.md") or
  [Stack Read-Only Access | Grant](../ctref/management-access-stack-read-only-access-grant.md "../ctref/management-access-stack-read-only-access-grant.md").
- The stack ID that you want to access so you can be granted access to the instance. To find a stack ID, see
  [Find stack IDs in AMS](find-stack.md "find-stack.md").
- The instance IP that you want to access. To find an instance IP, see
  [Find instance IDs or IP addresses in AMS](find-instance-id.md "find-instance-id.md").
- The DNS friendly bastion name or the bastion IP. How to use DNS friendly bastion names and how to find a bastion IP are described next.
