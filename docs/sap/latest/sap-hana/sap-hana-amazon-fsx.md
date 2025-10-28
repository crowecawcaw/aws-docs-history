# Configure storage (FSx for ONTAP)

Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp’s popular ONTAP file system. You can now deploy and operate SAP HANA on AWS with Amazon FSx for NetApp ONTAP. For more information, see [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/").

SAP HANA stores and processes all of its data in memory and provides protection against data loss by saving the data in persistent storage locations. To achieve optimal performance, the storage solution used for SAP HANA data and log volumes must meet SAP’s storage KPI. As a fully managed service, Amazon FSx for NetApp ONTAP makes it easier to launch and scale reliable, high-performing, and secure shared file storage in the cloud.

If you are a first-time user, see [How Amazon FSx for NetApp ONTAP works](../../../fsx/latest/ONTAPGuide/how-it-works-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/how-it-works-fsx-ontap.md").

This guide covers the following topics.

- [Supported configurations](instances-sizing-sap-hana-amazon-fsx.md "instances-sizing-sap-hana-amazon-fsx.md")
- [Set up FSx for ONTAP file system SVMs and volumes](amazon-fsx-sap-hana.md "amazon-fsx-sap-hana.md")
- [Set up host](host-setup-fsx-sap-hana.md "host-setup-fsx-sap-hana.md")
  For SAP specifications, refer to [SAP Note 2039883 - FAQ: SAP HANA database and data snapshots](https://launchpad.support.sap.com/#/notes/2039883 "https://launchpad.support.sap.com/#/notes/2039883") and [SAP Note 3024346 - Linux Kernel Settings for NetApp NFS](https://launchpad.support.sap.com/#/notes/3024346 "https://launchpad.support.sap.com/#/notes/3024346").
