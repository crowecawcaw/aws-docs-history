# Access: Bastions, SSH and RDP

- SSH Bastion settings

AMS provides SSH bastions in your Shared Services account to access hosts in the AMS environment.
In order to access the AMS network as an SSH user, you must use SSH Bastions as the entry point.
The network path originates from the On-Prem network, goes through DX/VPN to the transit gateway (TGW), and then is routed to the Shared Services VPC.
Once you are able to access the bastion, you can jump to other hosts in your AMS environment, provided that the proper access request has been granted.

    + Desired instance count (2 recommended)
    + Maximum instances (4 recommended)
    + Minimum instances (2 recommended)
    + Instance type (m5.large recommended)
    + Ingress CIDRs: IP address ranges from which users in
     your network will access SSH Bastions (ip range 1, ip range 2, ip range 3, ... etc)

- RDP Bastion settings

AMS optionally provides RDP bastions in your Shared Services account to access hosts in the AMS environment.
In order to access the AMS network as an RDP user, you must use RDP Bastions as the entry point.
The network path originates from the On-Prem network, goes through DX/VPN to the TGW, and then is routed to Shared Services VPC.
Once you are able to access the bastion, you can jump to other hosts in the AMS environment, provided that the proper access request has been granted.

    + Instance type (t3.medium recommended)
    + Desired minimum sessions (2 recommended)
    + Desired maximum sessions (10 recommended)

- RDP Bastion Configuration Type, Shared Standard or Shared HA (default is Shared Standard)

SecureStandard = A user receives one bastion and only one user can connect to the bastion.

SecureHA = A user receives two bastions in two different AZ's to connect to and only one user can connect to the bastion.

SharedStandard = A user receives one bastion to connect to and two users can connect to the same bastion at once.

SharedHA = A user receives two bastions in two different AZ's to connect to and two users
can connect to the same bastion at once.
