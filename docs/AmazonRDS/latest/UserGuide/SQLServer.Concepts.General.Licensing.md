

# Licensing Microsoft SQL Server on Amazon RDS
<a name="SQLServer.Concepts.General.Licensing"></a>

RDS for SQL Server supports two licensing models: License Included and Bring Your Own Media.

## License Included
<a name="SQLServer.Concepts.General.Licensing.LI"></a>

With the License Included (LI) model, you don't need to purchase a separate SQL Server license. Amazon RDS pricing includes the SQL Server software license, underlying hardware resources, and Amazon RDS management capabilities.

Amazon RDS supports License Included for the following SQL Server editions:
+ Enterprise
+ Standard
+ Web
+ Express

## Bring Your Own Media
<a name="SQLServer.Concepts.General.Licensing.BYOM"></a>

If you prefer to use your own Microsoft SQL Server licenses, Amazon RDS supports Bring Your Own Media (BYOM). With BYOM, Amazon RDS does not charge SQL Server license fees. Instead, you use your existing SQL Server licenses with License Mobility through Software Assurance.

You pay for AWS infrastructure (compute, storage, I/O, and data transfer), Windows OS license fees, and any additional RDS features you enable. You must have a valid SQL Server license with active Software Assurance and License Mobility rights. See [AWS License Mobility](https://aws.amazon.com/windows/resources/licensemobility/).

Amazon RDS supports BYOM for the following Microsoft SQL Server editions:
+ Enterprise
+ Standard
+ Developer

**Note**  
BYOM for Developer Edition is a free edition for development and testing purposes only and cannot be used in production environments - see below for more information.

For more information about setting up and using BYOM, see [Bring Your Own Media (BYOM) for RDS for SQL Server](sqlserver-byom.md).

## Development and testing
<a name="SQLServer.Concepts.General.Licensing.DevTest"></a>

For development and testing scenarios, you have two options:
+ **Express Edition** A free edition suitable for many development, testing, and non-production workloads. Available with the License Included model.
+ **Developer Edition** Includes all SQL Server Enterprise Edition features but is licensed for non-production use only. Available with the BYOM model.

You can download and install SQL Server Developer Edition on RDS for SQL Server using a BYOM engine version. For more information, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md).

For details about the differences between SQL Server editions, see [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15) in the Microsoft documentation.

## Multi-AZ deployments
<a name="SQLServer.Concepts.General.Licensing.MultiAZ"></a>

Amazon RDS supports Multi-AZ deployments for DB instances running Microsoft SQL Server using SQL Server Database Mirroring (DBM), Always On Availability Groups (AGs), and block-level replication for SQL Server Web Edition. There are no additional licensing requirements for Multi-AZ deployments. For more information, see [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md).

## SQL Server Web Edition usage requirements
<a name="SQLServer.Concepts.General.Licensing.WebEdition"></a>

SQL Server Web Edition is designed for web hosting providers and web value-added providers (VAPs) to host public, internet-accessible web pages, websites, web applications, and web services. These usage restrictions are imposed by Microsoft's licensing terms via Section 10.5 of the [AWS Service Terms](http://aws.amazon.com/serviceterms).

## Restoring license-terminated DB instances
<a name="SQLServer.Concepts.General.Licensing.Restoring"></a>

Amazon RDS takes snapshots of license-terminated DB instances. If your instance is terminated for licensing issues, you can restore it from the snapshot to a new DB instance. The new DB instance uses the License Included model.

For more information, see [Restoring license-terminated DB instances for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.RestoreLTI.md).