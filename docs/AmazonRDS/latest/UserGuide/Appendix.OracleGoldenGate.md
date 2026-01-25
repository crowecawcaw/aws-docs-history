# Oracle GoldenGate architecture

The Oracle GoldenGate architecture for use with Amazon RDS consists of the following decoupled modules:

Source database

Your source database can be either an on-premises Oracle database, an Oracle database on an Amazon EC2
instance, or an Oracle database on an Amazon RDS DB instance.

Oracle GoldenGate hub

An Oracle GoldenGate hub moves transaction information from the source database to the target
database. Your hub can be either of the following:

- An Amazon EC2 instance with Oracle Database and Oracle GoldenGate installed
- An on-premises Oracle installation

You can have more than one Amazon EC2 hub. We recommend that you use two hubs if you use Oracle GoldenGate for
cross-Region replication.

Target database

Your target database can be on either an Amazon RDS DB instance, an Amazon EC2 instance, or an on-premises
location.

The following sections describe common scenarios for Oracle GoldenGate on Amazon RDS.

###### Topics

- [On-premises source database and Oracle GoldenGate hub](#Appendix.OracleGoldenGate.on-prem-source-gg-hub "#Appendix.OracleGoldenGate.on-prem-source-gg-hub")
- [On-premises source database and Amazon EC2
  hub](#Appendix.OracleGoldenGate.on-prem-source-ec2-hub "#Appendix.OracleGoldenGate.on-prem-source-ec2-hub")
- [Amazon RDS source database and Amazon EC2 hub](#Appendix.OracleGoldenGate.rds-source-ec2-hub "#Appendix.OracleGoldenGate.rds-source-ec2-hub")
- [Amazon EC2 source database and Amazon EC2 hub](#Appendix.OracleGoldenGate.ec2-source-ec2-hub "#Appendix.OracleGoldenGate.ec2-source-ec2-hub")
- [Amazon EC2 hubs in different AWS Regions](#Appendix.OracleGoldenGate.cross-region-hubs "#Appendix.OracleGoldenGate.cross-region-hubs")

## On-premises source database and Oracle GoldenGate hub

In this scenario, an on-premises Oracle source database and on-premises Oracle GoldenGate hub provides data
to a target Amazon RDS DB instance.

![Oracle GoldenGate configuration 0 using Amazon RDS](images/oracle-gg0.png)

## On-premises source database and Amazon EC2

hub

In this scenario, an on-premises Oracle database acts as the source database. It's connected to an Amazon EC2 instance hub. This hub provides data
to a target RDS for Oracle DB instance.

![Oracle GoldenGate configuration 1 using Amazon RDS](images/oracle-gg1.png)

## Amazon RDS source database and Amazon EC2 hub

In this scenario, an RDS for Oracle DB instance acts as the source database. It's connected to an Amazon EC2 instance hub. This hub provides data to a
target RDS for Oracle DB instance.

![Oracle GoldenGate configuration 2 using Amazon RDS](images/oracle-gg2.png)

## Amazon EC2 source database and Amazon EC2 hub

In this scenario, an Oracle database on an Amazon EC2 instance acts as the source database. It's connected to an Amazon EC2 instance hub. This hub
provides data to a target RDS for Oracle DB instance.

![Oracle GoldenGate configuration 3 using Amazon RDS](images/oracle-gg3.png)

## Amazon EC2 hubs in different AWS Regions

In this scenario, an Oracle database on an Amazon RDS DB instance is connected to an Amazon EC2 instance hub in the same AWS Region. The hub is
connected to an Amazon EC2 instance hub in a different AWS Region. This second hub provides data to the target RDS for Oracle DB instance in the
same AWS Region as the second Amazon EC2 instance hub.

![Oracle GoldenGate configuration 4 using Amazon RDS](images/oracle-gg4.png)

###### Note

Any issues that affect running Oracle GoldenGate on an on-premises environment also affect running Oracle GoldenGate
on AWS. We strongly recommend that you monitor the Oracle GoldenGate hub to ensure that
`EXTRACT` and `REPLICAT` are resumed if a failover occurs. Because the
Oracle GoldenGate hub is run on an Amazon EC2 instance, Amazon RDS does not manage the Oracle GoldenGate hub and cannot
ensure that it is running.
