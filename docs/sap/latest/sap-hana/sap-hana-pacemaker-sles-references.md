# Vendor Support

## SAP and SUSE References

In addition to this guide, see the following references for more details:

- SUSE Documentation: [SLES for SAP - SAP HANA High Availability Cluster for the AWS Cloud](https://documentation.suse.com/en-us/sbp/sap-15/html/SLES4SAP-hana-sr-guide-perfopt-15-aws/index.html "https://documentation.suse.com/en-us/sbp/sap-15/html/SLES4SAP-hana-sr-guide-perfopt-15-aws/index.html")
- SUSE Documentation: [An overview of supported High Availability Solutions by SLES for SAP applications](https://documentation.suse.com/en-us/sles-sap/sap-ha-support/html/sap-ha-support/index.html "https://documentation.suse.com/en-us/sles-sap/sap-ha-support/html/sap-ha-support/index.html")
- SAP Note: [1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099 "https://me.sap.com/notes/1656099")
- SAP Note: [1984787 - SUSE Linux Enterprise Server 12: Installation Notes](https://me.sap.com/notes/1984787 "https://me.sap.com/notes/1984787")
- SAP Note: [2205917 - SAP HANA DB: Recommended OS settings for SLES 12 / SLES for SAP Applications 12](https://me.sap.com/notes/2205917 "https://me.sap.com/notes/2205917")
- SAP Note: [2578899 - SUSE Linux Enterprise Server 15: Installation Notes](https://me.sap.com/notes/2578899 "https://me.sap.com/notes/2578899")
- SAP Note: [2684254 - SAP HANA DB: Recommended OS settings for SLES 15 / SLES for SAP Applications 15](https://me.sap.com/notes/2684254 "https://me.sap.com/notes/2684254")
- SAP Note: [1275776 - Linux: Preparing SLES for SAP environments](https://me.sap.com/notes/1275776 "https://me.sap.com/notes/1275776")

###### Note

SAP portal access is required to access SAP Notes.

## Deployment Guidance

AWS works in collaboration with SUSE to support SAP HANA deployments on AWS. AWS provides detailed guidance on configuring EC2 instances and AWS-specific resources to meet SAP HANA requirements. While we strive to consolidate documentation to simplify the user experience, the underlying software components and resources owned by Pacemaker remain under the purview of the software vendor for development and support.

| SAP HANA Deployment Type                    | Support Status                | Notes                          | AWS Configuration Patterns                    |
| ------------------------------------------- | ----------------------------- | ------------------------------ | --------------------------------------------- |
| SAP HANA Scale-Up Standard                  | AWS Documented & Supported    | Covered in AWS SAP HANA guides | SAPHANAScaleUp-Classic, SAPHANAScaleUp-ANGI   |
| SAP HANA Scale-Up Secondary Read-Enabled    | Vendor Documented & Supported | Follows SAP documentation      |                                               |
| SAP HANA Scale-Up Multi-Tier Replication    | Vendor Documented & Supported | Follows SAP documentation      |                                               |
| SAP HANA Scale-Up Multi-Target Replication  | Vendor Documented & Supported | Follows SAP documentation      |                                               |
| SAP HANA Scale-Out Standard                 | AWS Documented & Supported    | Covered in AWS SAP HANA guides | SAPHANAScaleOut-Classic, SAPHANAScaleOut-ANGI |
| SAP HANA Scale-Out Secondary Read-Enabled   | Vendor Documented & Supported | Follows SAP documentation      |                                               |
| SAP HANA Scale-Out Multi-Tier Replication   | Vendor Documented & Supported | Follows SAP documentation      |                                               |
| SAP HANA Scale-Out Multi-Target Replication | Vendor Documented & Supported | Follows SAP documentation      |                                               |

###### Note

AWS configuration patterns represent standardized deployment templates that have been validated for specific use cases. In the documentation we will highlight where instructions deviate according to the configuration pattern.

###### What is Angi?

SAPHanaSR-angi (SAP HANA SR - Advanced Next Generation Interface) is the latest unified high availability solution for managing SAP HANA System Replication in Pacemaker clusters, supported on SLES-for-SAP 15 SP4 and newer. The solution consolidates the management of both scale-up and scale-out deployments into a single package and introduces technical improvements such as faster takeover times during filesystem failures, unresponsive HANA instances, and node failures in scale-out configurations.

This document covers new implementations using SAPHanaSR-angi. For migrations from existing SAPHanaSR or SAPHanaSR-ScaleOut installations to SAPHanaSR-angi, refer to the SUSE documentation for detailed upgrade procedures.
