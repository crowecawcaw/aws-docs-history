

# Capabilities for unsupported operating systems in Accelerate
<a name="acc-unsupported-os"></a>

An *unsupported* operating system is any operating system not listed in the [Supported configurations](acc-sd.md#supported-configs). AMS considers instances with unsupported operating systems to be "Customer-Requested Configurations" that are subject to the [AWS Betas and Previews service terms](https://aws.amazon.com/service-terms/#2._Betas_and_Previews).

The following limited set of AMS capabilities are available to instances with unsupported operating systems:


| **Capability** | **Notes** | 
| --- | --- | 
| Incident management | AMS provides incident response. | 
| Service request management | AMS responds to service requests. | 
| Monitoring | AMS monitors and responds to Amazon EC2 system status checks and instance status checks. System status checks include: loss of network connectivity, loss of system power, software issues on the physical host, and hardware issues on the physical host that impact network reachability.<br />Instance status checks include: incorrect networking or startup configuration, exhausted memory, corrupted file system, and incompatible kernel. | 
| Security management | AMS monitors and responds to Amazon EC2 [GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html) and [AWS Config rules](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-compliance.html). | 
| Backup management | AMS provides [Continuity management in Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup.html) for EC2 using AMS-customized AWS Backup plans and vaults. | 