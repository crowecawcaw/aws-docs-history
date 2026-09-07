

# Best Practice 8.1 – Encrypt data at rest
<a name="best-practice-8-1"></a>

Data at rest refers to any data stored digitally. We use encryption to ensure that this data is only visible to authorized users and remains protected when access to the storage or database is compromised independently of the application.

 **Suggestion 8.1.1 – Define at which levels encryption will be applied** 

In general, the further up the stack you deploy encryption, the more secure your data is. This increased security is accompanied by additional complexity for deployment and management. AWS recommends using the encryption at rest options available within its services. Consider additional operating system or database encryption when required, as defined in [Security]: [Best Practice 5.3 - Assess the need for specific security controls for your SAP workloads](best-practice-5-3.md). 

 **Suggestion 8.1.2 – Understand AWS encryption options for SAP services and solutions** 

Many AWS services used by SAP support the encryption of data at rest. Refer to the following documentation for further details.
+  AWS Documentation: [Use encryption with EBS-backed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html) 
+  AWS Documentation: [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) 
+  AWS Documentation: [Amazon EFS encryption](https://docs.aws.amazon.com/efs/latest/ug/encryption.html) 
+  AWS Documentation: [Amazon FSx encryption](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption.html) 
+  AWS Documentation: [FSx for ONTAP encryption](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/encryption-at-rest.html) 
+  AWS Documentation: [Amazon S3 Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) 

Data stored in these services can be encrypted at rest using either AWS or customer managed keys from AWS KMS.

Operating system encryption options include BitLocker, DM-crypt and SuSE Remote Disk.

 The following links may assist with finding information about encryption options for your database: 


| Database | Guidance | 
| --- | --- | 
| SAP HANA |  +  SAP Documentation: [Server-Side Data Encryption Services](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/b30fda1483b34628802a8d62bd5d39df.html) <br />+  SAP Documentation:[HANA Local Secure Store (LSS)](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/5a43dc48190f4543b0d840952d3dec55.html?&locale=en-US)   | 
| SAP ASE |  SAP Documentation: [SAP ASE Overview of Encryption](https://help.sap.com/viewer/833788dd3e9c413799014a0fd002d0b2/LATEST/en-US/a7b86bb3bc2b1014b9b08178723a5ee2.html)  | 
| IBM Db2 |  IBM Documentation: [Db2 Encryption Overview](https://www.ibm.com/docs/en/db2/11.5?topic=encryption-overview)  | 
| Oracle | SAP Note: [2591575 - Using Oracle Transparent Data Encryption (TDE) with SAP NetWeaver](https://launchpad.support.sap.com/#/notes/2591575) [Requires SAP Portal Access]  | 
| Microsoft SQL Server |  SAP Note: [1380493 - SQL Server Transparent Data Encryption (TDE)](https://launchpad.support.sap.com/#/notes/1380493) [Requires SAP Portal Access]  | 
| SAP MaxDB |  SAP Documentation: [SAP MaxDB Database Administration - Encryption](https://help.sap.com/viewer/2c2effc99b6746019aeb1af52ad59f5d/LATEST/en-US/741a232db1754d1899d23f9837e6052c.html)  | 

 **Suggestion 8.1.3 – Define encryption methods and key management stores** 

 Typically, key management is defined at the enterprise level and this will determine which key management options are permitted for use with your SAP workloads. AWS KMS is a secure and resilient service to simplify the management of encryption keys for AWS services. If you have a requirement to manage your own hardware security modules (HSMs), you can use AWS CloudHSM. 
+  AWS Documentation: [AWS encryption tool and service options](https://docs.aws.amazon.com/crypto/latest/userguide/awscryp-choose-toplevel.html) 
+  AWS Documentation: [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) 
+  AWS Documentation: [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) 

 Also consider mechanisms to protect master keys. How do you restrict access, manage rotation, and ensure recoverability of the keys? 

 Be aware that HANA data at rest encryption root keys can only be stored securely in the instance secure store in the file system (Instance SSFS) or within the SAP Data Custodian SaaS Solution. If using instance store the master key could be stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) with a rotation policy. 
+  SAP Note: [2154997 - Migration of hdbuserstore entries to ABAP SSFS](https://launchpad.support.sap.com/#/notes/2154997) [Requires SAP Portal Access] 
+  SAP Note: [2755815 - How to Ensure Recoverability of Hana's Data-At-Rest Encryption](https://launchpad.support.sap.com/#/notes/2755815) [Requires SAP Portal Access] 