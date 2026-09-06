

# Db2 on Amazon RDS versions
<a name="Db2.Concepts.VersionMgmt"></a>

For Db2, version numbers take the form of *major.minor.build.revision*, for example, 11.5.9.0.sb00000000.r1. Our version implementation matches that of Db2.

**major**  
The major version number is both the integer and the first fractional part of the version number, for example, 11.5. A version change is considered major if the major version number changes—for example, going from version 11.5 to 12.1.

**minor**  
The minor version number is both the third and fourth parts of the version number, for example, 9.0 in 11.5.9.0. The third part indicates the Db2 modpack, for example, 9 in 9.0. The fourth part indicates the Db2 fixpack, for example, 0 in 9.0. A version change is considered minor if either the Db2 modpack or the Db2 fixpack changes—for example, going from version 11.5.9.0 to 11.5.9.1, or from 11.5.9.0 to 11.5.10.0, with exceptions to provide catalog table updates. (Amazon RDS takes care of these exceptions.)

**build**  
The build number is the fifth part of the version number, for example, sb00000000 in 11.5.9.0.sb00000000. A build number where the number portion is all zeroes indicates a standard build. A build number where the number portion isn't all zeroes indicates a special build. A build number changes if there is a security fix or special build of an existing Db2 version. A build number change also indicates that Amazon RDS automatically applied a new minor version.

**revision**  
The revision number is the sixth part of the version number, for example, r1 in 11.5.9.0.sb00000000.r1. A revision is an Amazon RDS revision to an existing Db2 release. A revision number change indicates that Amazon RDS automatically applied a new minor version.

**Topics**
+ [Upgrade management for Amazon RDS Db2 instances](Db2.Concepts.VersionMgmt.Supported.md)
+ [Supported Db2 major versions on Amazon RDS](#Db2.Concepts.VersionMgmt.ReleaseCalendar)

## Supported Db2 major versions on Amazon RDS
<a name="Db2.Concepts.VersionMgmt.ReleaseCalendar"></a>

RDS for Db2 major versions are available under standard support at least until IBM end of support (base) for the corresponding IBM version. The following table shows the dates that you can use to plan your testing and upgrade cycles. If Amazon extends support for an RDS for Db2 version for longer than originally stated, we plan to update this table to reflect the later date.

You can use the following dates to plan your testing and upgrade cycles. 

**Note**  
Dates with only a month and a year are approximate and are updated with an exact date when it’s known.  
You can view the major versions of your Db2 databases by running the [describe-db-major-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-major-engine-versions.html) AWS CLI command or by using the [DescribeDBMajorEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBMajorEngineVersions.html) RDS API operation.


| Db2 major version  | IBM release date  | RDS release date  | IBM end of support (Standard and Advanced Edition) | IBM end of support (extended) | 
| --- | --- | --- | --- | --- | 
| Db2 11.5 | 27 June 2019 | 27 November 2023 | 30 April 2027 | 30 April 2031 | 
| Db2 12.1 | 14 November 2024 | 29 May 2026 | TBD | TBD | 

**Note**  
Major version upgrade through API or console is not currently supported. This capability will be available in a near future release.  
To manually perform a major version upgrade from RDS Db2 v11.5.9 to RDS Db2 v12.1.4, perform a full OFFLINE backup using the [rdsadmin.backup\_database](db2-sp-managing-databases.md#db2-sp-backup-database) stored procedure, then restore it to an existing RDS for Db2 v12.1.4 instance using the [rdsadmin.restore\_database](db2-sp-managing-databases.md#db2-sp-restore-database) stored procedure.