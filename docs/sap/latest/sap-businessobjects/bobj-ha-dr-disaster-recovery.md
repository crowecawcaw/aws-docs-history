# Disaster Recovery

The DR approach you take for SAP BusinessObjects BI Platform, as for any other enterprise application, depends on your RTO and RPO requirements. As discussed in [SAP Note 2056228](https://launchpad.support.sap.com/#/notes/2056228 "https://launchpad.support.sap.com/#/notes/2056228"), there are two options for building a DR site for SAP BusinessObjects BI Platform:

- Fully or selectively using SAP Lifecycle Manager (LCM) or Data Federation Services to promote or distribute the content from the primary system.
- Periodically copying over the CMS database and FRS contents, and using that to start a secondary system when required.
