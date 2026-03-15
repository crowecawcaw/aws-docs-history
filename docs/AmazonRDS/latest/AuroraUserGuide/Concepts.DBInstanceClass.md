# Determining DB instance class support in AWS Regions

To determine the DB instance classes supported by each DB engine in a specific
AWS Region, you can take one of several approaches. You can use the AWS Management Console, the [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/") page, or the [describe-orderable-db-instance-options](../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md "../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md") AWS CLI command.

###### Note

When you perform operations with the AWS Management Console, it automatically shows the supported DB
instance classes for a specific DB engine, DB engine version, and AWS Region. Examples
of the operations that you can perform include creating and modifying a DB
instance.

###### Contents

- [Using the Amazon RDS pricing page to determine DB instance class support in AWS Regions](Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.PricingPage "Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.PricingPage")
- [Using the AWS CLI to determine DB instance class support in AWS Regions](Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI "Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI")
  - [Listing the DB instance classes that are supported by a specific DB engine version in an AWS Region](Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example1 "Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example1")
  - [Listing the DB engine versions that support a specific DB instance class in an AWS Region](Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example2 "Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example2")

## Using the Amazon RDS pricing page to determine DB instance class support in AWS Regions

You can use the [Amazon Aurora Pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/")
page to determine the DB instance classes supported by each DB engine in a specific
AWS Region.

###### To use the pricing page to determine the DB instance classes supported by each engine in a Region

1. Go to [Amazon Aurora Pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").
2. Choose an Amazon Aurora engine in the **AWS Pricing Calculator** section.
3. In **Choose a Region**, choose an AWS Region.
4. In **Cluster Configuration Option**, choose a configuration option.
5. Use the section for compatible instances to view the supported DB instance classes.
6. (Optional) Choose other options in the calculator, and then choose **Save and view summary**
   or **Save and add service**.

## Using the AWS CLI to determine DB instance class support in AWS Regions

You can use the AWS CLI to determine which DB instance classes are supported for
specific DB engines and DB engine versions in an AWS Region.

To use the AWS CLI examples following, enter valid values for the DB engine, DB engine
version, DB instance class, and AWS Region. The following table shows the valid DB
engine values.

| Engine name                                    | Engine value in CLI commands | More information about versions                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MySQL 5.7-compatible and 8.0-compatible Aurora | `aurora-mysql`               | [Database engine updates for Amazon Aurora MySQL version 2](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md")<br>and [Database engine updates for Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md")<br>in the _Release Notes for Aurora MySQL_ |
| Aurora PostgreSQL                              | `aurora-postgresql`          | [_Release Notes for Aurora PostgreSQL_](../AuroraPostgreSQLReleaseNotes/Welcome.md "../AuroraPostgreSQLReleaseNotes/Welcome.md")                                                                                                                                                                                                                                                        |

For information about AWS Region names, see [AWS Regions](Concepts.md#Concepts.RegionsAndAvailabilityZones.Regions "Concepts.md#Concepts.RegionsAndAvailabilityZones.Regions").

The following examples demonstrate how to determine DB instance class support in an
AWS Region using the [describe-orderable-db-instance-options](../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md "../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md") AWS CLI command.

###### Topics

- [Listing the DB instance classes that are supported by a specific DB engine version in an AWS Region](#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example1 "#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example1")
- [Listing the DB engine versions that support a specific DB instance class in an AWS Region](#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example2 "#Concepts.DBInstanceClass.RegionSupportAurora.CLI.Example2")

### Listing the DB instance classes that are supported by a specific DB engine version in an AWS Region

To list the DB instance classes that are supported by a specific DB engine version
in an AWS Region, run the following command.

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options --engine `engine` --engine-version `version` \
    --query "OrderableDBInstanceOptions[].{DBInstanceClass:DBInstanceClass,SupportedEngineModes:SupportedEngineModes[0]}" \
    --output table \
    --region `region`
```

For Windows:

```
aws rds describe-orderable-db-instance-options --engine `engine` --engine-version `version` ^
    --query "OrderableDBInstanceOptions[].{DBInstanceClass:DBInstanceClass,SupportedEngineModes:SupportedEngineModes[0]}" ^
    --output table ^
    --region `region`
```

The output also shows the engine modes that are supported for each DB instance
class.

For example, the following command lists the supported DB instance classes for
version 13.6 of the Aurora PostgreSQL DB engine in US East (N. Virginia).

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options --engine aurora-postgresql --engine-version 15.3 \
    --query "OrderableDBInstanceOptions[].{DBInstanceClass:DBInstanceClass,SupportedEngineModes:SupportedEngineModes[0]}" \
    --output table \
    --region us-east-1
```

For Windows:

```
aws rds describe-orderable-db-instance-options --engine aurora-postgresql --engine-version 15.3 ^
    --query "OrderableDBInstanceOptions[].{DBInstanceClass:DBInstanceClass,SupportedEngineModes:SupportedEngineModes[0]}"  ^
    --output table ^
    --region us-east-1
```

### Listing the DB engine versions that support a specific DB instance class in an AWS Region

To list the DB engine versions that support a specific DB instance class in an
AWS Region, run the following command.

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options --engine `engine` --db-instance-class `DB_instance_class` \
    --query "OrderableDBInstanceOptions[].{EngineVersion:EngineVersion,SupportedEngineModes:SupportedEngineModes[0]}" \
    --output table \
    --region `region`
```

For Windows:

```
aws rds describe-orderable-db-instance-options --engine `engine` --db-instance-class `DB_instance_class` ^
    --query "OrderableDBInstanceOptions[].{EngineVersion:EngineVersion,SupportedEngineModes:SupportedEngineModes[0]}" ^
    --output table ^
    --region `region`
```

The output also shows the engine modes that are supported for each DB engine
version.

For example, the following command lists the DB engine versions of the
Aurora PostgreSQL DB engine that support the db.r5.large DB instance class in
US East (N. Virginia).

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options --engine aurora-postgresql --db-instance-class db.r7g.large \
    --query "OrderableDBInstanceOptions[].{EngineVersion:EngineVersion,SupportedEngineModes:SupportedEngineModes[0]}" \
    --output table \
    --region us-east-1
```

For Windows:

```
aws rds describe-orderable-db-instance-options --engine aurora-postgresql --db-instance-class db.r7g.large ^
    --query "OrderableDBInstanceOptions[].{EngineVersion:EngineVersion,SupportedEngineModes:SupportedEngineModes[0]}" ^
    --output table ^
    --region us-east-1
```
