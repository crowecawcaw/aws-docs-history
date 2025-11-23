# Creating a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support

When you create a DB instance or a Multi-AZ DB cluster, select **Enable
RDS Extended Support** in the console, or use the Extended Support option in the AWS CLI or the
parameter in the RDS API. When you enroll a DB instance or a
Multi-AZ DB cluster in
Amazon RDS Extended Support, it is permanently enrolled in RDS Extended Support for the life of the DB instance or Multi-AZ DB cluster.

If you use the console, you must select **Enable RDS Extended Support**. The
setting isn't selected by default.

If you use the AWS CLI or the RDS API and don't specify the RDS Extended Support setting, Amazon RDS
defaults to enabling RDS Extended Support. When you automate by using [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance-return-values:~:text=EngineLifecycleSupport "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance-return-values:~:text=EngineLifecycleSupport") or other services, this default behavior maintains the availability of
your database past the RDS end of standard support date.

You can prevent enrollment in RDS Extended Support by using the [AWS CLI](#extended-support-creating-db-instance-create-cli "#extended-support-creating-db-instance-create-cli") or the [RDS API](#extended-support-creating-db-instance-create-api "#extended-support-creating-db-instance-create-api") to create
a DB instance or a Multi-AZ DB cluster.

###### Topics

- [RDS Extended Support
  behavior](#extended-support-creating-db-instance-behavior "#extended-support-creating-db-instance-behavior")
- [Considerations
  for RDS Extended Support](#extended-support-creating-db-instance-considerations "#extended-support-creating-db-instance-considerations")
- [Create a DB instance or a Multi-AZ DB cluster with
  RDS Extended Support](#extended-support-creating-db-instance-create "#extended-support-creating-db-instance-create")

## RDS Extended Support

behavior

The following table summarizes what happens when a major engine version reaches the
RDS
end of standard support.

| RDS Extended Support status\* | Behavior                                                                                                                                                                               |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                       | Amazon RDS charges you for RDS Extended Support.                                                                                                                                       |
| Disabled                      | Amazon RDS upgrades your DB instance or<br>Multi-AZ DB cluster to a supported engine version. This upgrade<br>takes place on or shortly after the RDS end of<br>standard support date. |

\* In the RDS console, the RDS Extended Support status appears as Yes or No. In the AWS CLI or
RDS API, the RDS Extended Support status appears as `open-source-rds-extended-support`
or `open-source-rds-extended-support-disabled`.

## Considerations

for RDS Extended Support

Before creating a DB instance or a Multi-AZ DB cluster, consider the following
items:

- _After_ the RDS end of standard
  support date has passed, you can prevent the creation of a new DB instance or a new Multi-AZ DB cluster and avoid
  RDS Extended Support charges. To do this, use the AWS CLI or the RDS API. In the AWS CLI,
  specify `open-source-rds-extended-support-disabled` for the
  `--engine-lifecycle-support` option. In the RDS API, specify
  `open-source-rds-extended-support-disabled` for the
  `LifeCycleSupport` parameter. If you specify
  `open-source-rds-extended-support-disabled` and the RDS
  end of standard support date has passed, creating a DB instance or a Multi-AZ DB cluster will always fail.
- RDS Extended Support is set at the cluster level. Members of a cluster will always have
  the same setting for RDS Extended Support in the RDS console,
  `--engine-lifecycle-support` in the AWS CLI, and
  `EngineLifecycleSupport` in the RDS API.

For more information, see [MySQL versions](MySQL.Concepts.md "MySQL.Concepts.md") and [Release calendars for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md "../PostgreSQLReleaseNotes/postgresql-release-calendar.md").

## Create a DB instance or a Multi-AZ DB cluster with

RDS Extended Support

You can create a DB instance or a Multi-AZ DB cluster with an RDS Extended Support version
using the AWS Management Console, the AWS CLI, or the RDS API.

When you create a DB instance or a
Multi-AZ DB cluster, in the **Engine options** section, select
**Enable RDS Extended Support**. This setting isn't selected by
default.

The following image shows the **Enable RDS Extended Support**
setting:

![The Enable RDS Extended Support setting in the Engine options section.](images/extended-support-enable.png)
When you run the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") or [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") (Multi-AZ DB cluster) AWS CLI command,
select RDS Extended Support by specifying `open-source-rds-extended-support`
for the `--engine-lifecycle-support` option. By default, this option
is set to `open-source-rds-extended-support`.

To prevent the creation of a new DB instance or
a Multi-AZ DB cluster after the RDS end of standard support date, specify
`open-source-rds-extended-support-disabled` for the
`--engine-lifecycle-support` option. By doing so, you will avoid
any associated RDS Extended Support charges.

When you use the
[CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") or [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") (Multi-AZ DB cluster) Amazon RDS API
operation, select RDS Extended Support by setting the `EngineLifecycleSupport`
parameter to `open-source-rds-extended-support`. By default, this
parameter is set to `open-source-rds-extended-support`.

To prevent the creation of a new DB instance or
a Multi-AZ DB cluster after the RDS end of standard support date, specify
`open-source-rds-extended-support-disabled` for the
`EngineLifecycleSupport` parameter. By doing so, you will avoid
any associated RDS Extended Support charges.

For more information, see the following topics:

- To create a DB instance, follow the instructions for your DB engine in [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- To create a Multi-AZ DB cluster, follow the instructions for your DB engine in [Creating a Multi-AZ DB cluster for Amazon RDS](create-multi-az-db-cluster.md "create-multi-az-db-cluster.md").
