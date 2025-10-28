# Overview

Instructions in this document are based on recommendations provided by SAP and IBM on Db2 deployment on Linux via the SAP notes and KB articles listed in Table 1.

###### Note

When deploying IBM Db2 version 11.5 Mod Pack 6 (11.5.6) or higher, refer to the option recommended by IBM. For more information, see [Integrated solution using Pacemaker](https://www.ibm.com/docs/en/db2/11.5?topic=feature-integrated-solution-using-pacemaker "https://www.ibm.com/docs/en/db2/11.5?topic=feature-integrated-solution-using-pacemaker").

_Table 1 - SAP NetWeaver on IBM Db2 OSS Notes_

| SAP OSS Note | Description                                                      |
| ------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1656099**  | SAP Applications on AWS: Supported DB/OS and Amazon EC2 products |
| **1656250**  | SAP on AWS: Supported instance types                             |
| **1612105**  | DB6: FAQ on Db2 High Availability Disaster Recovery (HADR)       |
| **101809**   | DB6: Supported Db2 Versions and Fix Pack Levels                  |
| **1168456**  | SAP Db2 support info                                             |
| **1600156**  | SAP Db2 support on AWS                                           | **What this guide doesn’t do** This document doesn’t provide guidance on how to set up network and security constructs like Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables, access control lists (ACLs), Network Address Translation (NAT) Gateway, AWS Identity and Access Management (IAM) Roles, or AWS Security Groups. It doesn’t cover the high availability (HA) setup for the SAP Application Server Central Services/Enqueue Replication Server (ASCS/ERS), and focuses only on the database (DB) layer when covering the single points of failure (SPOF) for the SAP applications. |
