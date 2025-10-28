# Security

AWS provides security capabilities and services to securely run your SAP applications on the AWS platform. In the context of IBM Db2 for SAP applications, you can use network services and features such as [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"), [AWS Virtual Private Network](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/") (AWS VPN), [AWS Direct Connect](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.md"), [Amazon EC2 Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md"), [network access controls lists (NACLs)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md"), [route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md"), and more to restrict the access to your database.

## Network Security

The databases of SAP applications don’t usually require direct user access. The end users access the application using SAP Graphical User Interface (GUI), SAP Web Dispatcher, or SAP Fiori. We recommend that you limit direct access to the EC2 instances to administrators only, for maintenance purpose.

IBM Db2 listens on TCP port 5912 by default. Depending on your VPC design, you should configure Amazon EC2 Security Groups, Network Access Control List (NaCls), and route tables to allow traffic to TCP Port 5912 from SAP primary application servers and additional application servers (PAS/AAS) and ABAP SAP Central Services/SAP Central Services (ASCS/SCS). To learn more about configuring the security group, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").

## Encryption

Encryption is a security mechanism that converts plain text (readable data) into ciphertext. AWS offers [built-in encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md") for Amazon EBS data volumes, boot volumes, and snapshots. The encryption process occurs automatically, and you don’t need to manage encryption keys. This mechanism protects your EBS volumes at rest, and data in transit that passes between EC2 servers. This encryption level is offered at no additional cost.

You also can use the native [IBM Db2 native database encryption feature](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.1.0/com.ibm.db2.luw.admin.sec.doc/doc/c0061758.html "https://www.ibm.com/support/knowledgecenter/SSEPGG_11.1.0/com.ibm.db2.luw.admin.sec.doc/doc/c0061758.html") if required.

## Sizing

[SAP Quick Sizer](https://www.sap.com/about/benchmark/measuring.html "https://www.sap.com/about/benchmark/measuring.html") is used to size SAP environment for new implementations. However, if you are migrating your existing SAP applications based on IBM Db2 to AWS, consider using the following tools to right-size your SAP environment based on current utilization.

- **SAP Early Watch Alerts (EWA)**:--SAP EWA reports are provided by SAP regularly. These reports provide an overview of historical system utilization. Analyze these reports to see if your existing SAP system is over-utilized or under-utilized. Use this information to right-size your environment.
- **Linux native tools**:--Gather and analyze historical utilization data for CPU/Memory to right-size your environment. In case your source is [IBM AIX](https://www.ibm.com/it-infrastructure/power/os/aix "https://www.ibm.com/it-infrastructure/power/os/aix"), you can make use of [nmon](https://www.ibm.com/support/knowledgecenter/ssw_aix_72/n_commands/nmon.html "https://www.ibm.com/support/knowledgecenter/ssw_aix_72/n_commands/nmon.html") reports as well.
- **AWS Services**-- Use services such as AWS Migration Evaluator or AWS Application Discovery Services that help with collecting usage and configuration data about your on-premises servers. Use this information to analyze and right-size your environment.

Because it’s easy to scale up or scale down your Amazon EC2 instances on AWS, consider the following while sizing your SAP environment on AWS.

- You don’t need to over-provision storage to meet future demand.
- SAP Quick Sizer tools provide sizing guidance based on assumptions that on 100% load (as per your inputs to tool), system utilization will not be more than 65%, so there is some buffer built into SAP Quick Sizer recommendation. See SAP’s [Quick Sizer guidance](<https://apps.support.sap.com/sap(bD1lbiZjPTAwMQ==)/bc/bsp/sap/qs_oberflaeche/pdf1.htm?area=QSDOC&filename=QS_for_beg_classic.pdf> "https://apps.support.sap.com/sap(bD1lbiZjPTAwMQ==)/bc/bsp/sap/qs_oberflaeche/pdf1.htm?area=QSDOC&filename=QS_for_beg_classic.pdf") for details. (Login required.)
