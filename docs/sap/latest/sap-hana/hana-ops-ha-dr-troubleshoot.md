# Troubleshoot high availability SAP HANA deployments

This section provides guidance for troubleshooting SAP HANA high availability deployments.

A healthy status of SAP HANA system replication is a foundational requirement for the cluster solution to maintain stability. If SAP HANA system replication doesn’t have any dependencies on cluster solution, it can be independently verified using [SAP Note 2518979 - HANA : how to check system replication status](https://me.sap.com/notes/2518979 "https://me.sap.com/notes/2518979").

For manual deployment, there must not be any underlying issues within the cluster member systems for their continuous system replication and takeover procedures. This must be independently verified before integrating a cluster solution for automation. SAP HANA system replication depends on various factors for functioning smoothly. To troubleshoot any issues, see [Troubleshoot System Replication.](https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/782a0583f3af4a0992c5075b2ee7bd98.html?locale=en-US "https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/782a0583f3af4a0992c5075b2ee7bd98.html?locale=en-US")

Alternatively, you can use guided troubleshooting provided by SAP. For more information, see [SAP HANA Troubleshooting](https://ga.support.sap.com/index.html#/tree/1623/actions/21021:21032 "https://ga.support.sap.com/index.html#/tree/1623/actions/21021:21032"). You can also chat with experts or open an incident with SAP. For a speedy resolution, collect the relevant SAP HANA logs as per [SAP Note 2934640 - HANA and Replication - Collecting Support Data for Replication / Network related Tickets](https://me.sap.com/notes/2934640 "https://me.sap.com/notes/2934640"). The _fullsysteminfo-dumps_ log must be collected from all the cluster member systems for a complete analysis.

For troubleshooting issues with AWS Launch Wizard, see [Troubleshoot AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap-troubleshooting.md "../../../launchwizard/latest/userguide/launch-wizard-sap-troubleshooting.md").

For troubleshooting issues with high availability SAP HANA setup on SLES, see [Indepth HANA Cluster Debug Data Collection (PACEMAKER, SAP).](https://www.suse.com/support/kb/doc/?id=000019142 "https://www.suse.com/support/kb/doc/?id=000019142")

For troubleshooting issues with high availability SAP HANA setup on RHEL, see [How can I debug the SAPHana and SAPHanaTopology resource agents in a Pacemaker cluster?](https://access.redhat.com/solutions/4191201 "https://access.redhat.com/solutions/4191201")
