

# Qualys Policy Audit integration configuration
<a name="qualys-policy-audit-setup"></a>

Qualys Policy Audit (PA) is a cloud-native configuration assessment and compliance monitoring solution. It evaluates IT assets against security benchmarks, such as CIS, DISA STIG, and vendor hardening guides, and regulatory frameworks, such as PCI-DSS, HIPAA, SOX, and NIST.

As part of the Qualys Cloud Platform, it uses lightweight Cloud Agents and Scanner Appliances to assess on-premises, cloud, and hybrid environments. It includes out-of-the-box compliance policies, continuous assessment scheduling, and evidence-based reporting.

Compliance posture findings report whether each host passed or failed a policy control. CloudWatch pipelines use the Policy Compliance Reporting Service (PCRS) streaming API to ingest these findings. The connector uses the following retrieval flow:

1. Authenticate through OAuth 2.0 by exchanging credentials for a JSON Web Token (JWT).

1. Resolve all host IDs with their `policyId` and `subscriptionId`.

1. Retrieve per-host compliance posture findings within time-partitioned windows.

The following table lists the supported API and platform versions.


| Component | Version | Notes | 
| --- | --- | --- | 
| Qualys PCRS API | v5.0 | Policy Compliance Reporting Service posture endpoints under /pcrs/5.0/posture/\* | 
| Qualys Cloud Platform | Platform-specific | Regional gateways such as qg1, qg2, and qg3. See [Qualys Platform Identification](https://www.qualys.com/platform-identification). | 
| OCSF schema | v1.5.0 | Open Cybersecurity Schema Framework mapping | 
| OAuth 2.0 | 2 | Form-urlencoded username and password JWT token exchange | 

**Topics**
+ [Source configuration for Qualys Policy Audit](qualys-policy-audit-source-config.md)
+ [CloudWatch pipelines configuration for Qualys Policy Audit](qualys-policy-audit-pipeline-setup.md)