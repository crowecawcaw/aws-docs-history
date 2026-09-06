

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Capabilities for unsupported operating systems in AMS
<a name="ams-unsupported-os"></a>

An *unsupported* operating system is any operating system not listed in the [Supported configurations](supported-configs.md). AMS considers instances with unsupported operating systems to be "Customer-Requested Configurations" that are subject to the [AWS Betas and Previews service terms](https://aws.amazon.com/service-terms/#2._Betas_and_Previews).

The following limited set of AMS capabilities are available to instances with unsupported operating systems:


| **Capability** | **Notes** | 
| --- | --- | 
| Incident management | AMS provides incident response. | 
| Service request management | AMS responds to service requests. | 
| Requests for change (RFCs) | AMS evaluates RFCs for execution. Unsupported operating systems may impact the ability to execute RFCs. | 
| Monitoring | AMS monitors and responds to Amazon EC2 system status checks and instance status checks. System status checks include: loss of network connectivity, loss of system power, software issues on the physical host, and hardware issues on the physical host that impact network reachability.<br />Instance status checks include: incorrect networking or startup configuration, exhausted memory, corrupted file system, and incompatible kernel. | 
| Security management | AMS monitors and responds to Amazon EC2 [GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html). | 
| Backup management | AMS provides [Continuity management in AMS Advanced](https://docs.aws.amazon.com/managedservices/latest/userguide/continuity-mgmt.html) for EC2 using AMS-customized AWS Backup plans and vaults. | 