

# Infrastructure protection
<a name="infrastructure-protection"></a>


| HCL\_SEC5. How does your organization protect critical systems? | 
| --- | 
|   | 

 Follow Well-Architected best practices for [infrastructure protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) when designing and managing your transactional systems of record. 

 **Implement security controls necessary to protect the infrastructure within the AWS account** 

 Migrated healthcare workloads may have dependencies on technologies, older software applications, and host operating systems. For such systems, limit network access to sensitive hosts, apply the latest available security patches, and the employ monitoring practices described above. 

 Enable [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) in accounts that host and process PHI to add intelligent threat detection to your environment. GuardDuty continuously monitors your AWS accounts and workloads for malicious activity and provides detailed security findings. You can also create custom, automated [responses to GuardDuty findings using Amazon CloudWatch Events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html). 

 For details on workload protection, see the [security pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html). 