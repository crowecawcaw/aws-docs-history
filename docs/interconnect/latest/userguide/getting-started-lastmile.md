

# Getting started with AWS Interconnect - last mile
<a name="getting-started-lastmile"></a>

This guide walks you through creating your first AWS Interconnect - last mile connection.

## Prerequisites
<a name="lastmile-prerequisites"></a>

Before creating a last mile Interconnect, ensure you have the following:
+ An active AWS account with appropriate IAM permissions for AWS Direct Connect and AWS Interconnect.
+ An existing Direct Connect gateway (or you can create a new one during setup) to serve as the attach point for your last mile Interconnect.
+ An existing relationship with an Interconnect — last mile partner.
+ Customer Premises Equipment (CPE) at your remote site connected to the partner’s connectivity fabric.

## Plan your network architecture
<a name="lastmile-plan-architecture"></a>
+ Decide whether to use a Virtual Private Gateway, Transit Gateway, or Cloud WAN.
+ Virtual Private Gateways and Transit Gateways are Regional networking services.
+ Cloud WAN is a global networking service that can reach any Interconnect globally.
+ Review your existing IP address allocations to ensure no conflicts.
+ Create a new Direct Connect gateway or repurpose an existing one for use with your new last mile Interconnect.
+ Determine your bandwidth requirements. Supported tiers: 1, 2, 5, 10, 25, 50, and 100 Gbps.

## Create your first last mile Interconnect starting from the AWS Console
<a name="lastmile-create-interconnect"></a>

Use this workflow if you are an existing subscriber of an Interconnect — last mile partner.

1. Go to the AWS Direct Connect Console and navigate to **Last mile Interconnect** on the left side navigation menu.

1. Select **Create new last mile Interconnect**.

1. Select the participating partner you have a relationship with (for example: **Lumen**).

1. Select the **Interconnect Metro** closest to your physical location (for example, New York, Chicago, Seattle). Based on your metro selection, the console will display the ** AWS Region** that has direct connectivity from that location. This is essentially where AWS and the partner have collocated Interconnect - last mile infrastructure. This determines the AWS edge location where your traffic enters the AWS network.

1. Provide a **name** or description for your new interconnect, select your required **bandwidth**, specify an existing **Direct Connect Gateway** (or create a new one during set up) to serve as the attach point for the new last mile Interconnect, and provide the **partner account ID**. The partner account ID may be an email address (for Lumen) or a unique alphanumeric string. You can optionally apply a tag to your new interconnect. Choose **Next** when you have provided all the necessary information.

1. On the following screen, you can review the details of your new last mile Interconnect. Choose **Finish** to request the new interconnect.

1. At this point AWS will request the creation of the new last mile Interconnect to your partner and display the activation key you will use to complete the process on the partner portal (for example, Lumen).

1. To complete the creation process use the **Activation key** following the instructions on the partner portal (for example, Lumen).

1. Once you have activated the new Interconnect on the partner portal, the creation process will complete with the attachment of the new Interconnect to the Direct Connect Gateway you specified.

1. Use the main AWS Interconnect view in the AWS Direct Connect Console to review a list of all your Interconnects.

## Accepting a new last mile Interconnect created on the partner console using the AWS Console
<a name="lastmile-accept-interconnect"></a>

1. Go to the AWS Direct Connect Console and navigate to **Last mile Interconnect** on the left side navigation menu.

1. Select **Accept last mile Interconnect**.

1. Enter into the text field the Activation key generated on the partner portal as part of create action and select **Next**.

1. Provide a name or description for your new interconnect. Specify an existing Direct Connect Gateway to serve as the attach point for the new last mile Interconnect. You can optionally apply a tag to your new interconnect. Choose **Next** to continue the accept action.

1. On the following screen, you can review the details of the new last mile Interconnect that was requested from the partner. Choose **Finish** to accept the new last mile Interconnect.

### What Happens Next
<a name="lastmile-what-happens-next"></a>

After you submit your request:
+ Automatic provisioning begins: The service automatically provisions four connections between four router-pairs across two distinct Interconnect - last mile sites.
+ Network configuration: BGP peering, VLANs, and ASN assignments are configured automatically.
+ MACsec encryption: 256-bit MACsec encryption is enabled by default on all connections.
+ Monitoring enabled: End-to-end monitoring becomes available, including availability, health, latency, and packet loss metrics.
+ Your connection typically becomes operational within the timeframe specified during the request process. You can monitor the provisioning status in the AWS Direct Connect Console.

## Other considerations
<a name="lastmile-other-considerations"></a>
+ Last mile Interconnects support IPv4 and IPv6 address families.
+ Last mile Interconnects use Border Gateway Protocol (BGP) for dynamic routing between your network and AWS. The service automatically establishes BGP sessions, configures AS numbers, and handles route advertisements. All BGP details are abstracted from you.
+ The MTU for last mile Interconnects is set automatically to 8500 (Jumbo Frames enabled by default).
+ MACsec encryption is enabled by default between AWS and partner devices at the Interconnect location.
+ Multiple first-mile connectivity options are supported depending on what the partner offers, such as Ethernet and MPLS.
+ You can attach a last mile Interconnect to an existing Direct Connect Gateway that already has Private Virtual Interfaces or Transit Virtual Interfaces attached to it.