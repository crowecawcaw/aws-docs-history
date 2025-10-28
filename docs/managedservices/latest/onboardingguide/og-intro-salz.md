# AMS Single-account landing zone (SALZ) onboarding

## AMS SALZ onboarding process

To onboard AMS single-account landing zone (SALZ) accounts, you'll need to take the following steps:

1. Create a new AWS account that AMS configures as the networking account to host the firewall.
   Create the new account within your AWS organization, if you have one. AMS will follow the procedure of creating a
   normal AMS account,
   so all the information required must be gathered (for example CIDR, EPS licenses, and users). Note: A CIDR
   allocation of /24 is good.
2. Specify whether or not you want to remove the Internet gateways (IGWs) from the egress traffic
   accounts.
3. Determine your approved domains. AMS enables destination filtering by maintaining an approved domain list;
   the list can be modified later.
4. Confirm the instance size you want to use based on your expected throughput. By default, the instance is
   created in a m4.xlarge instance
   where we have found that the firewall throughput is 350Mbps. AMS can increase the size to a c4.8xLarge instance
   where the expected throughput is 1.25 Gbps.
5. Set up networking between AMS and your private network. This involves several tasks:
   1. Allocate IP space
   2. Establish private network connectivity to AWS
   3. Set up your firewall
   4. Set up access management
   5. Schedule backups

6. Provide access to the created account to AMS.
7. Validate that the AMS service is operating properly.

AMS will be able to perform the account build-out (onboarding) of your account within 2 weeks (10 business days)
from the initial request date. Any follow-up activity can be performed by using
[AMS Planned Event Management (PEM)](../userguide/ams-pem.md "../userguide/ams-pem.md").

###### Note

- US East (Virginia)
- US West (N. California)
- US West (Oregon)
- US East (Ohio)
- Canada (Central)
- South America (São Paulo)
- EU (Ireland)
- EU (Frankfurt)
- EU (London)
- EU West (Paris)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
  New regions are added frequently. For the most current list,
  see [AWS regions and availability zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md").
