This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.58 release

The following release notes include information for infrastructure release 6.58. For
information on the release timeline, see [Change log](#infra-release-notes-6.58-change-log "#infra-release-notes-6.58-change-log").

**Platform version**

|                |                                |
| -------------- | ------------------------------ |
| Infrastructure | 6.58<br>Replicated KOTS (2614) |

**New features:**

- **Calling Ingress** - Wickr Enterprise supports a calling
  ingress setting, allowing a client to connect to any calling node within the cluster and have
  the call route to the correct calling server. Users can now isolate the Wickr calling
  workload behind a single ingress point. For more information, see [Calling ingress
  settings](../wickrenterpriseinstall/calling-ingress-settings.md "../wickrenterpriseinstall/calling-ingress-settings.md").
- **Enhanced Security Context** - Wickr Enterprise provides
  configuration settings to enforce an enhanced security context for your deployment. This higher
  security standard is applied at the pod and container level, and is required for compliance
  with the Security Technical Implementation Guide (STIG). For more information, see [Security
  settings](../wickrenterpriseinstall/security-settings.md "../wickrenterpriseinstall/security-settings.md").
- **Multi-Node Embedded Cluster** - Wickr Enterprise provides
  this option to allow Embedded Cluster users to separate the Wickr Calling and Wickr
  Messaging workloads onto different physical machines. For more information, see [Multi-Node installation](../wickrenterpriseinstall/multi-node-installation.md "../wickrenterpriseinstall/multi-node-installation.md").
  **Changes, enhancements, and resolved issues:**

General enhancements and bug fixes.

**Required update**: Database schema changes in this version enable future
MySQL 8 upgrade compatibility.

## Change log

**Change log for 6.58 release and release notes**

| Change                | Description                             | Date            |
| --------------------- | --------------------------------------- | --------------- |
| Infrastructure update | Initial release of August release notes | August 26, 2025 |
