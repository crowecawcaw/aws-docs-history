

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.58 release
<a name="infra-release-notes-6.58"></a>

The following release notes include information for infrastructure release 6.58. For information on the release timeline, see [Change log](#infra-release-notes-6.58-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.58<br />Replicated KOTS (2614) | 

**New features:**
+ **Calling Ingress** - Wickr Enterprise supports a calling ingress setting, allowing a client to connect to any calling node within the cluster and have the call route to the correct calling server. Users can now isolate the Wickr calling workload behind a single ingress point. For more information, see [Calling ingress settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/calling-ingress-settings.html).
+ **Enhanced Security Context** - Wickr Enterprise provides configuration settings to enforce an enhanced security context for your deployment. This higher security standard is applied at the pod and container level, and is required for compliance with the Security Technical Implementation Guide (STIG). For more information, see [Security settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/security-settings.html).
+ **Multi-Node Embedded Cluster** - Wickr Enterprise provides this option to allow Embedded Cluster users to separate the Wickr Calling and Wickr Messaging workloads onto different physical machines. For more information, see [Multi-Node installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/multi-node-installation.html).

**Changes, enhancements, and resolved issues:**

General enhancements and bug fixes.

**Required update**: Database schema changes in this version enable future MySQL 8 upgrade compatibility.

## Change log
<a name="infra-release-notes-6.58-change-log"></a>

**Change log for 6.58 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Infrastructure update | Initial release of August release notes | August 26, 2025 | 