# Automated operating system patching prerequisites

In addition to the prerequisites described in the [Automation prerequisites](sap-nw-automation.md#automation-prerequisites "sap-nw-automation.md#automation-prerequisites") section of this guide, verify the following prerequisites that are specific to automated operating system patching:

- Verify the Patch Manager prerequisites.

Because the solution described here uses AWS Systems Manager Patch Manager, you must verify that you have satisfied all of the Patch Manager prerequisites. For more information, see [Patch Manager prerequisites](../../../systems-manager/latest/userguide/patch-manager-prerequisites.md "../../../systems-manager/latest/userguide/patch-manager-prerequisites.md") in the _AWS Systems Manager User Guide_.

- Ensure you have a backup of your SAP system.

Before you make changes to the SAP system, verify that a backup is available to support rollback in case you encounter problems. You should have the following backups:

    + Operating system backup – You should have an Amazon Machine Image (AMI) backup of the Amazon EC2 instance that consists of the base operating file system (`root` for Linux and `C:\` for Microsoft Windows) and the SAP application and database file systems.
    + Database backup – If patching will occur on the database server, ensure you have the most recent database backup.

For data recovery recommendations, see [Plan for data recovery](../../../wellarchitected/latest/sap-lens/design-principle-12.md "../../../wellarchitected/latest/sap-lens/design-principle-12.md") in the _SAP Lens AWS Well-Architected Framework_.

## Supported operating systems

The following operating systems are supported by SAP and Patch Manager. Check the Patch Manager prerequisites for currently supported versions of the operating systems. For more information, see [Patch Manager prerequisites](../../../systems-manager/latest/userguide/patch-manager-prerequisites.md "../../../systems-manager/latest/userguide/patch-manager-prerequisites.md") in the _AWS Systems Manager User Guide_.

- Oracle Linux

###### Note

Oracle Linux is required if you are running an Oracle database.

- Red Hat Enterprise Linux (RHEL)
- SUSE Linux Enterprise Server (SLES)
- Microsoft Windows Server

###### Note

- SUSE Linux and Red Hat Linux have SAP versions of the Linux operating system. SAP recommends that you use RHEL for SAP Solutions/Applications or SLES for SAP Applications to run the SAP application.
- Oracle Linux operating system is required for Oracle Database Server and SAP NetWeaver Application Servers with Oracle client installed. For more information, see [SAP Note 2358420 - Oracle Database Support for Amazon Web Services EC2](https://me.sap.com/notes/2358420/E "https://me.sap.com/notes/2358420/E") (SAP portal access required).

For each of these operating systems, you can bring your own subscription to AWS or use the Amazon Machine Images (AMIs) from the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

## SAP Notes

Review the following SAP Notes. You require SAP portal access to check these references from SAP.

- SAP Note: [1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099")
- SAP Note: [2871484 - SAP supported variants of Red Hat Enterprise Linux](https://launchpad.support.sap.com/#/notes/2871484 "https://launchpad.support.sap.com/#/notes/2871484")
- SAP Note: [2358420 - Oracle Database Support for Amazon Web Services EC2](https://launchpad.support.sap.com/#/notes/2358420 "https://launchpad.support.sap.com/#/notes/2358420")
- SAP Note: [62988 - Service Packs for MS SQL Server](https://launchpad.support.sap.com/#/notes/62988 "https://launchpad.support.sap.com/#/notes/62988")
- SAP Note: [2235581 - SAP HANA: Supported Operating systems](https://launchpad.support.sap.com/#/notes/2235581 "https://launchpad.support.sap.com/#/notes/2235581")
