# Version policy for Amazon RDS for Microsoft SQL Server

This topic describes the version policy for Amazon RDS for SQL Server, including supported
major and minor versions, release timelines, deprecation procedures, and upgrade guidance.

## Amazon RDS for SQL Server major versions

Amazon RDS supports several major versions of Microsoft SQL Server, including
SQL Server 2014, 2016, 2017, 2019, 2022, and 2025.

Microsoft SQL Server major version support| Microsoft SQL Server major version | RDS for SQL Server support |
| --- | --- |
| 2008 | No longer supported |
| 2012 | No longer supported |
| 2014 | No longer supported |
| 2016 | Supported |
| 2017 | Supported |
| 2019 | Supported |
| 2022 | Supported |
| 2025 | Supported |

## Amazon RDS for SQL Server minor versions

RDS for SQL Server customers can specify any currently supported Microsoft SQL Server
version when creating a new DB instance. You can specify the Microsoft SQL Server
major version (such as Microsoft SQL Server 2022), and any supported minor version
for the specified major version. If no version is specified, Amazon RDS defaults to
a supported version, typically the most recent version. If a major version is
specified but a minor version is not, Amazon RDS defaults to a recent release of
the major version you have specified.

The following table shows the supported versions for all editions and all
AWS Regions, except where noted. You can also use the
`describe-db-engine-versions`
CLI command to see a list of supported versions, as well as defaults for newly created DB instances.

Supported minor versions for Amazon RDS for SQL Server| Major version | Minor version | RDS API `EngineVersion` and CLI `engine-version` |
| --- | --- | --- |
| SQL Server 2025 | 17.00.4045.5 (CU5) | `17.00.4045.5.v1` |
| SQL Server 2022 | 16.00.4245.2 (CU24)<br>16.00.4236.2 (CU23 v2)<br>16.00.4230.2 (GDR)<br>16.00.4225.2 (CU22)<br>16.00.4215.2 (CU21)<br>16.00.4210.1 (GDR)<br>16.00.4205.1 (CU20)<br>16.00.4195.2 (CU19)<br>16.00.4185.3 (CU18)<br>16.00.4175.1 (CU17)<br>16.00.4165.4 (CU16)<br>16.00.4150.1 (GDR)<br>16.00.4145.4 (CU15)<br>16.00.4140.3 (GDR)<br>16.00.4135.4 (CU14)<br>16.00.4131.2 (CU13)<br>16.00.4125.3 (CU13)<br>16.00.4120.1 (GDR)<br>16.00.4115.5 (CU12)<br>16.00.4105.2 (CU11)<br>16.00.4095.4 (CU10)<br>16.00.4085.2 (CU9) | `16.00.4245.2.v1`<br>`16.00.4236.2.v1`<br>`16.00.4230.2.v1`<br>`16.00.4225.2.v1`<br>`16.00.4215.1.v1`<br>`16.00.4210.1.v1`<br>`16.00.4205.1.v1`<br>`16.00.4195.2.v1`<br>`16.00.4185.3.v1`<br>`16.00.4175.1.v1`<br>`16.00.4165.4.v1`<br>`16.00.4150.1.v1`<br>`16.00.4145.4.v1`<br>`16.00.4140.3.v1`<br>`16.00.4135.4.v1`<br>`16.00.4131.2.v1`<br>`16.00.4125.3.v1`<br>`16.00.4120.1.v1`<br>`16.00.4115.5.v1`<br>`16.00.4105.2.v1`<br>`16.00.4095.4.v1`<br>`16.00.4085.2.v1` |
| SQL Server 2019 | 15.00.4460.4 (GDR)<br>15.00.4455.2 (GDR)<br>15.00.4445.1 (GDR)<br>15.00.4440.1 (GDR)<br>15.00.4435.7 (GDR)<br>15.00.4430.1 (CU32)<br>15.00.4420.2 (CU31)<br>15.00.4415.2 (CU30)<br>15.00.4410.1 (GDR)<br>15.00.4405.4 (CU29)<br>15.00.4395.2 (GDR)<br>15.00.4390.2 (GDR)<br>15.00.4385.2 (CU28)<br>15.00.4382.1 (CU27)<br>15.00.4375.4 (CU27)<br>15.00.4365.2 (CU26)<br>15.00.4355.3 (CU25)<br>15.00.4345.5 (CU24)<br>15.00.4335.1 (CU23)<br>15.00.4322.2 (CU22)<br>15.00.4316.3 (CU21)<br>15.00.4312.2 (CU20)<br>15.00.4236.7 (CU16 SU)<br>15.00.4198.2 (CU15)<br>15.00.4153.1 (CU12)<br>15.00.4073.23 (CU8)<br>15.00.4043.16 (CU5) | `15.00.4460.4.v1`<br>`15.00.4455.2.v1`<br>`15.00.4445.1.v1`<br>`15.00.4440.1.v1`<br>`15.00.4435.7.v1`<br>`15.00.4430.1.v1`<br>`15.00.4420.2.v1`<br>`15.00.4415.2.v1`<br>`15.00.4410.1.v1`<br>`15.00.4405.4.v1`<br>`15.00.4395.2.v1`<br>`15.00.4390.2.v1`<br>`15.00.4385.2.v1`<br>`15.00.4382.1.v1`<br>`15.00.4375.4.v1`<br>`15.00.4365.2.v1`<br>`15.00.4355.3.v1`<br>`15.00.4345.5.v1`<br>`15.00.4335.1.v1`<br>`15.00.4322.2.v1`<br>`15.00.4316.3.v1`<br>`15.00.4312.2.v1`<br>`15.00.4236.7.v1`<br>`15.00.4198.2.v1`<br>`15.00.4153.1.v1`<br>`15.00.4073.23.v1`<br>`15.00.4043.16.v1` |
| SQL Server 2017 | 14.00.3520.4 (GDR)<br>14.00.3515.1 (GDR)<br>14.00.3505.1 (GDR)<br>14.00.3500.1 (GDR)<br>14.00.3495.9 (GDR)<br>14.00.3485.1 (GDR)<br>14.00.3480.1 (GDR)<br>14.00.3475.1 (GDR)<br>14.00.3471.2 (GDR)<br>14.00.3465.1 (GDR)<br>14.00.3460.9 (CU31)<br>14.00.3451.2 (CU30)<br>14.00.3421.10 (CU27)<br>14.00.3401.7 (CU25)<br>14.00.3381.3 (CU23)<br>14.00.3356.20 (CU22)<br>14.00.3294.2 (CU20)<br>14.00.3281.6 (CU19) | `14.00.3520.4.v1`<br>`14.00.3515.1.v1`<br>`14.00.3505.1.v1`<br>`14.00.3500.1.v1`<br>`14.00.3495.9.v1`<br>`14.00.3485.1.v1`<br>`14.00.3480.1.v1`<br>`14.00.3475.1.v1`<br>`14.00.3471.2.v1`<br>`14.00.3465.1.v1`<br>`14.00.3460.9.v1`<br>`14.00.3451.2.v1`<br>`14.00.3421.10.v1`<br>`14.00.3401.7.v1`<br>`14.00.3381.3.v1`<br>`14.00.3356.20.v1`<br>`14.00.3294.2.v1`<br>`14.00.3281.6.v1` |
| SQL Server 2016 | 13.00.6480.4 (GDR)<br>13.00.6475.1 (GDR)<br>13.00.6470.1 (GDR)<br>13.00.6465.1 (GDR)<br>13.00.6460.7 (GDR)<br>13.00.6455.2 (GDR)<br>13.00.6450.1 (GDR)<br>13.00.6445.1 (GDR)<br>13.00.6441.1 (GDR)<br>13.00.6435.1 (SP3 GDR)<br>13.00.6430.49 (SP3 GDR)<br>13.00.6419.1 (SP3 GDR)<br>13.00.6300.2 (SP3) | `13.00.6480.4.v1`<br>`13.00.6475.1.v1`<br>`13.00.6470.1.v1`<br>`13.00.6465.1.v1`<br>`13.00.6460.7.v1`<br>`13.00.6455.2.v1`<br>`13.00.6450.1.v1`<br>`13.00.6445.1.v1`<br>`13.00.6441.1.v1`<br>`13.00.6435.1.v1`<br>`13.00.6430.49.v1`<br>`13.00.6419.1.v1`<br>`13.00.6300.2.v1` |

## When does Amazon RDS for SQL Server introduce support for new major versions

Amazon RDS for SQL Server typically introduces support for new major SQL Server
database versions within 6–12 months after Microsoft's general availability release
date. When adding support for a new major version, Amazon RDS selects the first
minor version that has undergone comprehensive testing to ensure stability.

## How long Amazon RDS for SQL Server major versions remain available

Amazon RDS for SQL Server maintains support for major versions until Microsoft's
Extended End Date, which serves as the End of Support (EOS) date. (See
[Microsoft
Documentation](https://learn.microsoft.com/en-us/lifecycle/products/ "https://learn.microsoft.com/en-us/lifecycle/products/").) Below are the key dates to help plan your testing and
upgrade cycles. Note that these dates indicate the earliest possible required
upgrade timeline, and may be extended later by Amazon.

Amazon RDS for SQL Server major version end of support dates| SQL Server major version | Microsoft End Of Support date | Expected date for upgrading to a newer version |
| --- | --- | --- |
| 2025 | 1/6/2036 | 1/6/2036 |
| 2016 | 7/14/2026 | 7/14/2026 |
| 2017 | 10/12/2027 | 10/12/2027 |
| 2019 | 1/8/2030 | 1/8/2030 |
| 2022 | 1/11/2033 | 1/11/2033 |

## How often Amazon RDS for SQL Server minor versions are released

In general, Amazon RDS for SQL Server minor versions are released within 30 days
after they are made available by Microsoft. The release schedule may vary to include
additional features or fixes.

## How long Amazon RDS for SQL Server minor versions remain available

In general, Amazon RDS for SQL Server supports the latest three minor versions for
each major version. The exact number of minor versions for each major version may
vary due to Microsoft support timeline of each minor version, Amazon RDS maintenance
schedule, and other factors.

Amazon RDS for SQL Server minor version end of support dates| Major version | Minor version | Microsoft End Of Support date | Expected date for upgrading to a newer version |
| --- | --- | --- | --- |
| SQL Server 2022 | 16.00.4245.2 (CU24)<br>16.00.4236.2 (CU23 v2)<br>16.00.4230.2 (GDR)<br>16.00.4225.2 (CU22)<br>16.00.4215.2 (CU21)<br>16.00.4210.1 (GDR)<br>16.00.4205.1 (CU20)<br>16.00.4195.2 (CU19)<br>16.00.4185.3 (CU18)<br>16.00.4175.1 (CU17)<br>16.00.4165.4 (CU16)<br>16.00.4150.1 (GDR)<br>16.00.4145.4 (CU15)<br>16.00.4140.3 (GDR)<br>16.00.4135.4 (CU14)<br>16.00.4131.2 (CU13)<br>16.00.4125.3 (CU13)<br>16.00.4120.1 (GDR)<br>16.00.4115.5 (CU12)<br>16.00.4105.2 (CU11)<br>16.00.4095.4 (CU10)<br>16.00.4085.2 (CU9) | 1/11/2033 | 1/11/2033 |
| SQL Server 2019 | 15.00.4460.4 (GDR)<br>15.00.4455.2 (GDR)<br>15.00.4445.1 (GDR)<br>15.00.4440.1 (GDR)<br>15.00.4435.7 (GDR)<br>15.00.4430.1 (CU32)<br>15.00.4420.2 (CU31)<br>15.00.4415.2 (CU30)<br>15.00.4410.1 (GDR)<br>15.00.4405.4 (CU29)<br>15.00.4395.2 (GDR)<br>15.00.4390.2 (GDR)<br>15.00.4385.2 (CU28)<br>15.00.4382.1 (CU27)<br>15.00.4375.4 (CU27)<br>15.00.4365.2 (CU26)<br>15.00.4355.3 (CU25)<br>15.00.4345.5 (CU24)<br>15.00.4335.1 (CU23)<br>15.00.4322.2 (CU22)<br>15.00.4316.3 (CU21)<br>15.00.4312.2 (CU20)<br>15.00.4236.7 (CU16 SU)<br>15.00.4198.2 (CU15)<br>15.00.4153.1 (CU12)<br>15.00.4073.23 (CU8)<br>15.00.4043.16 (CU5) | 1/8/2030 | 1/8/2030 |
| SQL Server 2017 | 14.00.3520.4 (GDR)<br>14.00.3515.1 (GDR)<br>14.00.3505.1 (GDR)<br>14.00.3500.1 (GDR)<br>14.00.3495.9 (GDR)<br>14.00.3485.1 (GDR)<br>14.00.3480.1 (GDR)<br>14.00.3475.1 (GDR)<br>14.00.3471.2 (GDR)<br>14.00.3465.1 (GDR)<br>14.00.3460.9 (CU31)<br>14.00.3451.2 (CU30)<br>14.00.3421.10 (CU27)<br>14.00.3401.7 (CU25)<br>14.00.3381.3 (CU23)<br>14.00.3356.20 (CU22)<br>14.00.3294.2 (CU20)<br>14.00.3281.6 (CU19) | 10/12/2027 | 10/12/2027 |
| SQL Server 2016 | 13.00.6480.4 (GDR)<br>13.00.6475.1 (GDR)<br>13.00.6470.1 (GDR)<br>13.00.6465.1 (GDR)<br>13.00.6460.7 (GDR)<br>13.00.6455.2 (GDR)<br>13.00.6450.1 (GDR)<br>13.00.6445.1 (GDR)<br>13.00.6441.1 (GDR)<br>13.00.6435.1 (SP3 GDR)<br>13.00.6430.49 (SP3 GDR)<br>13.00.6419.1 (SP3 GDR)<br>13.00.6300.2 (SP3) | 7/14/2026 | 7/14/2026 |

## What happens when an Amazon RDS for SQL Server database version is deprecated

When a major version of the database engine is deprecated in Amazon RDS, we provide
a minimum six (6) month period after the announcement of a deprecation for you to
initiate a manual upgrade to a supported major version. At the end of this period,
an automatic upgrade to the next major version will be applied to any instances still
running the deprecated version during their scheduled maintenance windows.

When a minor version of a database engine is deprecated in Amazon RDS, we provide a
three (3) month period after the announcement before beginning automatic upgrades.
At the end of this period, all instances still running the deprecated minor version
will be scheduled for automatic upgrade to the latest supported minor version during
their scheduled maintenance windows.

Once a major or minor database engine version is deprecated in Amazon RDS, any DB
instance restored from a DB snapshot created with the unsupported version will
automatically and immediately be upgraded to a currently supported version.

## Mandatory Amazon RDS for SQL Server upgrades

Amazon RDS for SQL Server may require mandatory upgrades to newer minor versions
when critical fixes are necessary. Before implementing these upgrades, Amazon
communicates a detailed plan that includes timing of key milestones, impact on
your database instances, and recommended actions. These mandatory upgrades are
automated and scheduled to begin during your instance's designated maintenance
window.

## Testing your DB instance with a new SQL Server version before upgrading

You can test the upgrade process and how the new version works with your application
and workload. Restore from an instance snapshot to create a new RDS for SQL Server instance. You can
create an instance snapshot yourself from an existing Amazon RDS instance. Amazon RDS also
automatically creates periodic snapshots for your instance. You can then initiate a
version upgrade for the new instance. You can experiment on the upgraded copy of your
instance before deciding whether to upgrade your original instance.
