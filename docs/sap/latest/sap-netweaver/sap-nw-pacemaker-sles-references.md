# Deployment Guidance

The following section details the documentation and deployment guidance from SUSE.

###### Topics

- [Deployment Patterns](#deployments-sles "#deployments-sles")
- [Automated Deployment](#automation-nw-sles "#automation-nw-sles")
- [Pacemaker - simple-mount and classic architecture](#simple-classic-nw-sles "#simple-classic-nw-sles")

## Deployment Patterns

The following table outlines the supported SAP deployment types and their corresponding AWS configuration patterns for high availability clustering.

| SAP Deployment Type            | Support Status                | AWS Configuration Patterns                      | Notes                      |
| ------------------------------ | ----------------------------- | ----------------------------------------------- | -------------------------- |
| SAP NetWeaver ASCS/ERS (ENSA1) | AWS Documented & Supported    | SAPNetweaver-Classic, SAPNetweaver-Simple-mount |                            |
| SAP NetWeaver ASCS/ERS (ENSA2) | AWS Documented & Supported    | SAPNetweaver-Classic, SAPNetweaver-Simple-mount |                            |
| SAP S/4HANA ASCS/ERS           | AWS Documented & Supported    | SAPNetweaver-Classic, SAPNetweaver-Simple-mount | S/4HANA only supports ERS2 |
| SAP SCS (Java)                 | Vendor Documented & Supported |                                                 | Follows SAP Documentation  |

## Automated Deployment

You can set up a cluster manually using the instructions provided here. You can also automate parts of this process to ensure consistency and repeatability.

Use AWS Launch Wizard for SAP for automated deployments of SAP NetWeaver, SAP S/4 HANA, SAP B/4HANA, and Solution Manager. Launch Wizard uses AWS CloudFormation scripts to quickly provision the resources needed to deploy SAP NetWeaver and S/4 HANA. The automation performs SAP enqueue replication and pacemaker setup so that only validation and testing are required. For more information, see [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

To ensure that the behavior and operation of your cluster is well understood regardless of how your system is set up, we recommend a thorough test cycle. See [Testing](testing.md "testing.md") for more details.

## Pacemaker - simple-mount and classic architecture

This guide covers two architectures for SAP cluster solutions on SLES for SAP – simple-mount and classic (previous standard). Simple-mount was certified as the SLES for SAP Applications cluster solution in late 2021. It is now the recommended architecture for both ENSA1 and ENSA2 deployments running on SLES for SAP 15 and above. For more details, see SUSE blog [Simple Mount Structure for SAP Application Platform](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform/ "https://www.suse.com/c/simple-mount-structure-for-sap-application-platform/").

If you are configuring a new SAP installation, we recommend the simple-mount architecture. If you already have the classic architecture, and wish to migrate to the simple-mount architecture, see [Switching architecture to simple-mount](#switching-architecture-sles "#switching-architecture-sles").

The following are the differences between the classic and simple-mount architectures.

- Removing file system resources from cluster – a file system is required but it is not mounted and unmounted by the cluster. The executable directory for the ASCS and ERS can be permanently mounted on both nodes.
- Addition of SAPStartSrv – SAPStartSrv controls the matching SAPStartSrv framework process.
- Sapping and sappong services – these services manage the start of SAPStartSrv services with sapinit.

See the [Architecture diagrams](sles-netweaver-ha-diagrams.md "sles-netweaver-ha-diagrams.md") for more details.

### Switching architecture to simple-mount

Follow along these steps if you want to switch an existing cluster with classic architecture to use the recommended configuration of simple-mount architecture.

These steps must be performed in an outage window, allowing stop/start of services and basic testing.

1. Put the cluster in maintenance mode. See [Maintenance mode](planned-maintenance-nw-sles.md#maintenance-mode-nw-sles "planned-maintenance-nw-sles.md#maintenance-mode-nw-sles")
2. Stop SAP services, including application servers connected to the cluster as well as ASCS and ERS.
3. Install any missing operating system packages. See [Install Missing Operating System Packages](sap-nw-pacemaker-sles-os-settings.md#packages-nw-sles "sap-nw-pacemaker-sles-os-settings.md#packages-nw-sles").

It might be necessary to install `sapstartsrv-resource-agents`. However, all operating system prerequisites must be checked and updated to ensure that versions are compatible. 4. Add entries for ASCS and ERS mount point on both nodes (if not already added). See [Update /etc/fstab](sap-shared-filesystems-nw-sles.md#update-fstab-nw-sles "sap-shared-filesystems-nw-sles.md#update-fstab-nw-sles") 5. Enable `sapping`/`sappong` services. See [Enable sapping and sappong Services (Simple-Mount Only)](sap-ascs-service-control-nw-sles.md#sapping-sappong-services-nw-sles "sap-ascs-service-control-nw-sles.md#sapping-sappong-services-nw-sles") 6. Align and disable `systemd` services. See [Ensure ASCS and ERS SAP Services can run on either node (systemd)](sap-ascs-service-control-nw-sles.md#modify-sapservices-nw-sles "sap-ascs-service-control-nw-sles.md#modify-sapservices-nw-sles") 7. Backup the configuration with the following command.

```
# crm config show >> /tmp/classic_ha_setup.txt
```

See [Prepare for Resource Creation](cluster-config-nw-sles.md#prepare-resource-nw-sles "cluster-config-nw-sles.md#prepare-resource-nw-sles") 8. _Optional_ – delete the configuration. You can edit in place but we recommend starting with a blank configuration. This ensures that latest timeout and priority parameters are in place. See [Reset Configuration – Optional](cluster-config-nw-sles.md#reset-config-nw-sles "cluster-config-nw-sles.md#reset-config-nw-sles")

```
# crm config erase
# crm config show
```

9. Configure cluster resources again.
10. Check the cluster and perform some tests.
11. Resume standard operations by starting any additional services, including application servers.
