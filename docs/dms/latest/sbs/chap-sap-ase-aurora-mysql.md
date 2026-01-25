# Prerequisties for migrating from SAP AWS to Amazon Aurora MySQL

The following prerequisites are required to complete this walkthrough:

- Familiarity with Amazon Relational Database Service (Amazon RDS), the applicable database technologies, and SQL.
- Understand the supported features and limitations of AWS Database Migration Service (AWS DMS). For more information, see [What Is Database Migration Service?](../userguide/Welcome.md "../userguide/Welcome.md").
- Accomplish the prerequisites required for using an SAP ASE database as a source for AWS DMS. For more information, see [Prerequisites for using an SAP ASE database as a source](../userguide/CHAP_Source.md#CHAP_Source.SAP.Prerequisites "../userguide/CHAP_Source.md#CHAP_Source.SAP.Prerequisites").
- Understand the limitations on using SAP ASE as a source and MySQL as a target for AWS DMS. For more information, see [Limitations on using SAP ASE as a source](../userguide/CHAP_Source.md#CHAP_Source.SAP.Limitations "../userguide/CHAP_Source.md#CHAP_Source.SAP.Limitations") and [Limitations on using a MySQL-compatible database as a target](../userguide/CHAP_Target.md#CHAP_Target.MySQL.Limitations "../userguide/CHAP_Target.md#CHAP_Target.MySQL.Limitations").
- Accomplish the prerequisites required for using a MySQL-compatible database as a target for AWS DMS. For more information, see [Using a MySQL-compatible database as a target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md").
- Set up the network for AWS DMS replication. This includes configuring VPC, private subnets, availability zone, and adding connections on the source firewall if it exists. For more information, see [Setting up a network for a replication instance](../userguide/CHAP_ReplicationInstance.md "../userguide/CHAP_ReplicationInstance.md").
- Download and install AWS Schema Conversion Tool (AWS SCT) with the required SAP ASE and MySQL JDBC drivers. For more information, see [Installing, verifying, and updating the Schema Conversion Tool](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md").
- Know the recommendations on the most efficient way to use AWS DMS. For more information, see [Best practices](../userguide/CHAP_BestPractices.md "../userguide/CHAP_BestPractices.md").
