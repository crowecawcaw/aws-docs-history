# Install SAP

The following topics provide information about installing SAP on AWS Cloud in a highly available cluster. Review SAP Documentation for more details.

###### Topics

- [Final checks for software provisioning](#final-checks-software-provisioning-nw-rhel "#final-checks-software-provisioning-nw-rhel")
- [Install SAP ASCS and ERS instances](#install-sap-instances-nw-rhel "#install-sap-instances-nw-rhel")
- [Kernel upgrade and ENSA2 – optional](#kernel-ensa2-nw-rhel "#kernel-ensa2-nw-rhel")
- [Check SAP host agent version](#check-host-agent-nw-rhel "#check-host-agent-nw-rhel")

## Final checks for software provisioning

Before running SAP Software Provisioning Manager (SWPM), ensure that the following prerequisites are consistent across both cluster nodes:

- Collect any missing details and populate the [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md") section to ensure clarity on the specific values used in installation commands.
- **User and Group Configuration** - If operating system groups are pre-defined, ensure matching UID and GID values for `<sid>adm` and `sapsys` across both cluster nodes.
- **Installation Software** - Download the latest version of Software Provisioning Manager (SWPM) and SAP installation media for your SAP release from [Software Provisioning Manager](https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html "https://support.sap.com/en/tools/software-logistics-tools/software-provisioning-manager.html").
- **Network Configuration** - Verify both cluster nodes have identical configuration with all routes, overlay IPs, and virtual hostnames accessible. This ensures that either node can run ASCS or ERS roles.
- **File Systems** - Verify all shared file systems are mounted and accessible from both nodes with consistent mount points and permissions.

## Install SAP ASCS and ERS instances

Install the SAP ASCS and ERS instances using their virtual hostnames to ensure installation against the overlay IP addresses. This approach is required for proper cluster integration.

Install the ASCS instance on `<instance_id_1>` using virtual hostname `<ascs_virt_hostname>` with the `SAPINST_USE_HOSTNAME` parameter. This ensures the installation uses the overlay IP rather than the physical hostname:

_Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# <swpm location>/sapinst SAPINST_USE_HOSTNAME=<ascs_virt_hostname>
```

Install the ERS instance on `<instance_id_2>` using virtual hostname `<ers_virt_hostname>` with the `SAPINST_USE_HOSTNAME` parameter. This ensures the installation uses the overlay IP rather than the physical hostname:

```
# <swpm location>/sapinst SAPINST_USE_HOSTNAME=<ers_virt_hostname>
```

Once the ASCS and ERS installations are complete, you will need to install and configure the database and SAP Primary Application Server (PAS) - these components are not covered in this cluster setup documentation. Optionally, you can also install and configure Additional Application Server (AAS). For more details on installing these SAP NetWeaver components, refer to SAP Help Portal.

For additional information on unattended installation options, see [SAP Note 2230669 – System Provisioning Using an Input Parameter File](https://me.sap.com/notes/2230669 "https://me.sap.com/notes/2230669") (requires SAP portal access).

## Kernel upgrade and ENSA2 – optional

As of AS ABAP Release 7.53 (ABAP Platform 1809), the new Standalone Enqueue Server 2 (ENSA2) is installed by default. ENSA2 replaces the previous version – ENSA1.

If you have an older version of SAP NetWeaver, consider following the SAP guidance to upgrade the kernel and update the Enqueue Server configuration. An upgrade will allow you to take advantage of the features available in the latest version. For more information, see the following SAP Notes (require SAP portal access):

- [SAP Note 2630416 – Support for Standalone Enqueue Server 2](https://me.sap.com/notes/2630416 "https://me.sap.com/notes/2630416")
- [SAP Note 2711036 – Usage of the Standalone Enqueue Server 2 in an HA Environment](https://me.sap.com/notes/2711036 "https://me.sap.com/notes/2711036")

## Check SAP host agent version

This is applicable to both cluster nodes. The SAP host agent is used for system instance control and monitoring. This agent is used by SAP cluster resource agents and hooks. It is recommended that you have the latest version installed on both instances. For more details, see [SAP Note 2219592 – Upgrade Strategy of SAP Host Agent](https://me.sap.com/notes/2219592 "https://me.sap.com/notes/2219592").

Use the following command to check the version of the host agent:

```
# /usr/sap/hostctrl/exe/saphostexec -version
```
