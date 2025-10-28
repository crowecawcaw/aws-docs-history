# FAQ

**Q.** Can I use [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/ "https://aws.amazon.com/rds/sqlserver/") as a database to deploy SAP NetWeaver based applications?

**A.** No, Amazon RDS for SQL Server is not certified by SAP for SAP NetWeaver based applications. However, it is certified to be used as database for SAP Business Objects BI (BObj BI)

**Q.** Can I purchase and use a Microsoft SQL Server license from AWS, such as [Microsoft SQL Server 2019 Enterprise on Windows Server 2022](https://aws.amazon.com/marketplace/pp/prodview-hyy374htf4h2w "https://aws.amazon.com/marketplace/pp/prodview-hyy374htf4h2w"), Amazon Machine Image (AMI), to host my SAP NetWeaver based workloads, and other SAP workloads?

**A.** Yes, AWS provides a variety of options for Microsoft SQL Server license-included AMIs, as a pre-installed package with different combinations of Microsoft Windows Server and Microsoft SQL Server versions and editions available. For more information, see [Licensing options](../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing-options.md "../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing-options.md") and [Find a SQL Server license-included AMI](../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-amis.md "../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-amis.md").

There are some differences in how SAP manages technical support, when the support ticket is raised with SAP support, and if the issue raised is found to be with Microsoft SQL Server, when those licenses are from AWS. In that situation, you need to raise a separate ticket with Support for SQL Server technical support, following the terms of your Support plan.
