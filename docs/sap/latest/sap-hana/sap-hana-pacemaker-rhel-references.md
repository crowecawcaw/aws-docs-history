# Vendor Support

## SAP and Red Hat References

In addition to this guide, see the following references for more details:

- Red Hat Documentation: [Automating SAP HANA Scale-Up System Replication using the RHEL HA Add-On - Red Hat Enterprise Linux for SAP Solutions 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/index "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/automating_sap_hana_scale-up_system_replication_using_the_rhel_ha_add-on/index")
- Red Hat Documentation: [Deploying SAP HANA Scale-Up System Replication High Availability - Advanced Next Generation Interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/deploying_sap_hana_scale-up_system_replication_high_availability/index "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/deploying_sap_hana_scale-up_system_replication_high_availability/index")
- Red Hat Documentation: [Automating SAP HANA Scale-Out System Replication using the RHEL HA Add-On - Red Hat Enterprise Linux for SAP Solutions 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/automating_sap_hana_scale-out_system_replication_using_the_rhel_ha_add-on "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/html/automating_sap_hana_scale-out_system_replication_using_the_rhel_ha_add-on")
- SAP Note: [1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099 "https://me.sap.com/notes/1656099")
- SAP Note: [2777782 - SAP HANA DB: Recommended OS Settings for RHEL 8](https://me.sap.com/notes/2777782 "https://me.sap.com/notes/2777782")
- SAP Note: [3108302 - SAP HANA DB: Recommended OS Settings for RHEL 9](https://me.sap.com/notes/3108302 "https://me.sap.com/notes/3108302")

###### Note

SAP portal access is required to access SAP Notes.

## Deployment Guidance

AWS works in collaboration with Red Hat to support SAP HANA deployments on AWS. AWS provides detailed guidance on configuring EC2 instances and AWS-specific resources to meet SAP HANA requirements. While we strive to consolidate documentation to simplify the user experience, the underlying software components and resources owned by Pacemaker remain under the purview of the software vendor for development and support.

| SAP HANA Deployment Type                    | Support Status                | Notes                          | AWS Configuration Patterns                   |
| ------------------------------------------- | ----------------------------- | ------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAP HANA Scale-Up Standard                  | AWS Documented & Supported    | Covered in AWS SAP HANA guides | SAPHANAScaleUp-Classic, SAPHANAScaleUp-ANGI  |
| SAP HANA Scale-Up Secondary Read-Enabled    | Vendor Documented & Supported | Follows SAP documentation      |                                              |
| SAP HANA Scale-Up Multi-Tier Replication    | Vendor Documented & Supported | Follows SAP documentation      |                                              |
| SAP HANA Scale-Up Multi-Target Replication  | Vendor Documented & Supported | Follows SAP documentation      |                                              |
| SAP HANA Scale-Out Standard                 | AWS Documented & Supported    | Covered in AWS SAP HANA guides | SAPHANAScaleOut-Classic, SAPHANAScaleUp-ANGI |
| SAP HANA Scale-Out Secondary Read-Enabled   | Vendor Documented & Supported | Follows SAP documentation      |                                              |
| SAP HANA Scale-Out Multi-Tier Replication   | Vendor Documented & Supported | Follows SAP documentation      |                                              |
| SAP HANA Scale-Out Multi-Target Replication | Vendor Documented & Supported | Follows SAP documentation      |                                              | ###### Note AWS configuration patterns represent standardized deployment templates that have been validated for specific use cases. In the documentation we will highlight where instructions deviate according to the configuration pattern. ###### What is Angi? SAPHanaSR-angi (SAP HANA SR - Advanced Next Generation Interface) is the latest unified high availability solution for managing SAP HANA System Replication in Pacemaker clusters, supported on RHEL 9.6 and newer. The solution consolidates the management of both scale-up and scale-out deployments into a single package and introduces technical improvements such as faster takeover times during filesystem failures, unresponsive HANA instances, and node failures in scale-out configurations. This document covers new implementations using SAPHanaSR-angi. For migrations from existing SAPHanaSR or SAPHanaSR-ScaleOut installations to SAPHanaSR-angi, refer to the Red Hat documentation. |
