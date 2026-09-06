

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Single-account landing zone (SALZ) onboarding
<a name="og-intro-salz"></a>

## AMS SALZ onboarding process
<a name="sent-onboard-process"></a>

To onboard AMS single-account landing zone (SALZ) accounts, you'll need to take the following steps:

1. Create a new AWS account that AMS configures as the networking account to host the firewall. Create the new account within your AWS organization, if you have one. AMS will follow the procedure of creating a normal AMS account, so all the information required must be gathered (for example CIDR, EPS licenses, and users). Note: A CIDR allocation of /24 is good.

1. Specify whether or not you want to remove the Internet gateways (IGWs) from the egress traffic accounts.

1. Determine your approved domains. AMS enables destination filtering by maintaining an approved domain list; the list can be modified later.

1. Confirm the instance size you want to use based on your expected throughput. By default, the instance is created in a m4.xlarge instance where we have found that the firewall throughput is 350Mbps. AMS can increase the size to a c4.8xLarge instance where the expected throughput is 1.25 Gbps.

1. Set up networking between AMS and your private network. This involves several tasks:

   1. Allocate IP space

   1. Establish private network connectivity to AWS

   1. Set up your firewall

   1. Set up access management

   1. Schedule backups

1. Provide access to the created account to AMS.

1. Validate that the AMS service is operating properly.

AMS will be able to perform the account build-out (onboarding) of your account within 2 weeks (10 business days) from the initial request date. Any follow-up activity can be performed by using [AMS Planned Event Management (PEM)](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-pem.html).

**Note**  
US East (Virginia)
US West (N. California)
US West (Oregon)
US East (Ohio)
Canada (Central)
South America (São Paulo)
EU (Ireland)
EU (Frankfurt)
EU (London)
EU West (Paris)
Asia Pacific (Mumbai)
Asia Pacific (Seoul)
Asia Pacific (Singapore)
Asia Pacific (Sydney)
Asia Pacific (Tokyo)
New regions are added frequently. For the most current list, see [ AWS regions and availability zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html).