# Best Practice 3.4 – Use runbooks to

perform SAP landscape operations

Runbooks are documented procedures to achieve specific outcomes. Enable consistent
and prompt responses to well-understood events by documenting procedures in runbooks.
Understand common SAP operations that are run and create specific, versioned documentation
with a review cycle.

- AWS Well-Architected Framework [Operational Excellence]: [Operational Readiness](../operational-excellence-pillar/operational-readiness.md "../operational-excellence-pillar/operational-readiness.md")
- AWS Documentation: [Runbooks and automation using AWS Incident Manager](../../../incident-manager/latest/userguide/runbooks.md "../../../incident-manager/latest/userguide/runbooks.md")

**Suggestion 3.4.1 - Create specific runbooks for SAP security
operations**

Consider creating runbooks for common SAP security operations:

- User provisioning and identity management
- Firefighter access
- Authorization changes
- Security and authorization audits
- Encryption key rotation
- TLS certificate management

**Suggestion 3.4.2 - Create specific runbooks for SAP scaling and
performance operations**

Consider creating runbooks for common scaling and performance operations:

- Disk volume re-sizing
- Horizontal and vertical scaling of SAP application servers
- Re-sizing of database server
- Addition or removal of servers from load balancing

**Suggestion 3.4.3 - Create specific runbooks for SAP operations
during faults**

Consider creating runbooks for operations during faults:

- System restarts and order of restarting systems
- SAP backups and restores
- Cluster failover
- Storage failure
- Critical interface restarts and replays
- DNS and network routing changes
- Ransomware recovery

- SAP Lens [Reliability]: [Best Practice 10.3 –
  Define an approach to help ensure the availability of critical SAP data](best-practice-10-3.md "best-practice-10-3.md")

**Suggestion 3.4.4 - Create specific runbooks for SAP maintenance
operations**

Consider creating runbooks for maintenance operations:

- Starting and stopping SAP
- Refreshing / System Copy of SAP
- Daily health checks
- Error management / ABAP dumps
- Patching SAP application, operating system, and database
- Log rotation, clean up, and archival
  Consider database and application log and trace files cleanups for your SAP
  environment, for example, SAP Note: [2399996 - Automating SAP HANA
  Cleanup](https://launchpad.support.sap.com/#/notes/2399996 "https://launchpad.support.sap.com/#/notes/2399996") [Requires SAP Portal Access]
