

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Supported configurations
<a name="supported-configs"></a>

These are the configurations AWS Managed Services (AMS) supports:
+ Language: AMS is available in English.
+ Security software: Deep Security from Trend Micro (Required). AWS Marketplace: [Trend Micro Deep Security](https://aws.amazon.com/marketplace/pp/B01AVYHVHO?ref_=srh_res_product_title)
+ Approved directory services: Microsoft Active Directory (AD)
+ [Supported AWS services](supported-services.md).
+ Supported AWS Regions:

  AMS operates in a subset of all AWS Regions; however, the AMS API/CLI runs out of the "USA East (N. Virginia)" Region only. If you run either the AMS change management API (`amscm`) or the AMS service knowledge management API (`amsskms)`, in a non-USA East Region, you must add `--region us-east-1` to the command.<a name="what-is-ams-regions-note"></a>
  + US East (Virginia)
  + US West (N. California)
  + US West (Oregon)
  + US East (Ohio)
  + Canada (Central)
  + South America (São Paulo)
  + EU (Ireland)
  + EU (Frankfurt)
  + EU (London)
  + EU West (Paris)
  + Asia Pacific (Mumbai)
  + Asia Pacific (Seoul)
  + Asia Pacific (Singapore)
  + Asia Pacific (Sydney)
  + Asia Pacific (Tokyo)
+ Amazon machine images (AMIs): AMS provides security enhanced images (AMIs) based on the CIS Level 1 benchmark for a subset of operating systems supported by AMS. The following operating systems have a security enhanced AMI available:
  + Amazon Linux 2
  + Amazon Linux 2023
  + Red Hat Enterprise Linux 8
  + Red Hat Enterprise Linux 9
  + Windows Server 2016
  + Windows Server 2019
  + Windows Server 2022
  + Windows Server 2025
+ Supported operating systems:

  **Supported operating systems (x86-64)**
  + Amazon Linux 2023
  + Amazon Linux 2 (**expected AMS support end date June 30, 2026**)
  + Oracle Linux 9.x, 8.x
  + Red Hat Enterprise Linux (RHEL) 9.x, 8.x
  + SUSE Linux Enterprise Server 15 SP6
  + SUSE Linux Enterprise Server for SAP 15 SP3 and later
  + Microsoft Windows Server 2025, 2022, 2019, 2016
  + Ubuntu 20.04, 22.04, 24.04

  **Supported operating systems (ARM64)**
  + Amazon Linux 2023
  + Amazon Linux 2 (**expected AMS support end date June 30, 2026**)
+ Supported End of Support (EOS) operating systems:
**Note**  
End of Support (EOS) operating systems are outside of the general support period of the operating system manufacturer and have increased security risk. EOS operating systems are considered supported configurations only if AMS-required agents support the operating system and the following are true:  
you have extended support with the operating system vendor that allows you to receive updates, or 
any instances using an EOS operating system follow the [ security controls](https://docs.aws.amazon.com/managedservices/latest/userguide/key-terms.html#CritRec) as specified by AMS in the Advanced User Guide, or
you comply with any other compensating security controls required by AMS.
In the event AMS is no longer able to support an EOS operating system, AMS issues a [Critical Recommendation](https://docs.aws.amazon.com/managedservices/latest/userguide/key-terms.html#CritRec) to upgrade the operating system.  
AMS-required agents may include but are not limited to: AWS Systems Manager, Amazon CloudWatch, Endpoint Security (EPS) agent, and Active Directory (AD) Bridge (Linux only).
  + Ubuntu Linux 18.04
  + SUSE Linux Enterprise Server 15 SP3, SP4, and SP5
  + SUSE Linux Enterprise Server for SAP 15 SP2
  + SUSE Linux Enterprise Server 12 SP5
  + SUSE Linux Enterprise Service for SAP 12 SP5
  + Microsoft Windows Server 2012/2012 R2