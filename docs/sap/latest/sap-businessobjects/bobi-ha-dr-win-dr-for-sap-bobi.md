# DR for SAP BusinessObjects BI Platform on AWS

DR for SAP BusinessObjects BI Platform on the AWS Cloud refers to a scenario in which the primary AWS Region where SAP BusinessObjects BI Platform application is running is unavailable. The goal of setting up a DR site is to be able to recover the application within your acceptable RTO and RPO.

There are no restrictions in AWS for using LCM or Data Federation Services for your DR environment. Note that using LCM requires either consuming resources on the source system or provisioning an additional system to run promotion management jobs. This option might also result in a higher RPO depending on the frequency of promotion management jobs. See [Promotion Management Architecture](https://wiki.scn.sap.com/wiki/display/BOBJ/Promotion+Management+Architecture+%3A+processes+at+play+in+a+BI4+landscape "https://wiki.scn.sap.com/wiki/display/BOBJ/Promotion+Management+Architecture+%3A+processes+at+play+in+a+BI4+landscape") on the SAP Community Wiki for the high-level architecture for this option.

In this guide, we’ll discuss the second option for handling DR, which is to copy the CMS database and FRS contents. Using variants of this option, you can build the complete primary system within your recovery time limits. This option doesn’t require resources from the primary system except for the backup copy of the database and file system.
