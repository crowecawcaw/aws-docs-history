

# Monitor your environment

You monitor an Amazon Elastic VMware Service environment with AWS tools and with VMware Cloud Foundation (VCF) tools. AWS tools report on the environment, the EC2 instances that run your hosts, and Amazon EVS API calls. VCF tools report on the VCF components and the workloads that run on them.

The following table shows each monitoring source, what it tells you, and where to read more.


| Source | What it tells you | More information | 
| --- | --- | --- | 
| Amazon EVS environment status | Whether Amazon EVS can reach your VCF management appliances, and the results of the environment status checks. |  [Monitor environment status](evs-env-status-check.md)  | 
|  AWS Health | Scheduled maintenance and retirement events for the EC2 instances that run your hosts, and other events that affect your environment. |  [Get notified about host events](monitor-notifications.md)  | 
| Amazon CloudWatch and VCF Operations | EC2 status checks and alarms for your hosts, Amazon EVS usage metrics, and the health of VCF components and workloads. |  [Monitor hosts and VCF](monitor-observability.md)  | 
|  AWS CloudTrail | Who called which Amazon EVS API operation, and when. |  [Log API calls with CloudTrail](logging-using-cloudtrail.md)  | 

**Topics**
+ [Monitor environment status](evs-env-status-check.md)
+ [Get notified about host events](monitor-notifications.md)
+ [Monitor hosts and VCF](monitor-observability.md)
+ [Log API calls with CloudTrail](logging-using-cloudtrail.md)