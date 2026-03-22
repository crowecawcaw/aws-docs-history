# Guidelines and limitations for RDS Custom for Oracle replication

When you create RDS Custom for Oracle replicas, not all RDS Oracle replica options are supported.

###### Topics

- [General guidelines for RDS Custom for Oracle replication](#custom-rr.guidelines "#custom-rr.guidelines")
- [General limitations for RDS Custom for Oracle replication](#custom-rr.limitations "#custom-rr.limitations")
- [Networking requirements and limitations for RDS Custom for Oracle replication](#custom-rr.network "#custom-rr.network")
- [External replica limitations for RDS Custom for Oracle](#custom-rr.external-replica-reqs "#custom-rr.external-replica-reqs")

## General guidelines for RDS Custom for Oracle replication

When working with RDS Custom for Oracle, follow these guidelines:

- You can use RDS Custom for Oracle replication only in Oracle Enterprise Edition.
  Standard Edition 2 isn't supported.
- We strongly recommend that you implement a VPN tunnel to encrypt
  communication between your primary and standby instances. For more
  information, see [Configuring a VPN tunnel between RDS Custom for Oracle primary and replica instances](cfo-standby-vpn-tunnel.md "cfo-standby-vpn-tunnel.md").
- Don't modify the `RDS_DATAGUARD` user. This user is reserved
  for RDS Custom for Oracle automation. Modifying this user can result in undesired
  outcomes, such as an inability to create Oracle replicas for your RDS Custom for Oracle
  DB instance.
- Don't change the replication user password. It is required to administer
  the Oracle Data Guard configuration on the RDS Custom host. If you change the
  password, RDS Custom for Oracle might put your Oracle replica outside the support
  perimeter. For more information, see [RDS Custom support perimeter](custom-concept.md#custom-troubleshooting.support-perimeter "custom-concept.md#custom-troubleshooting.support-perimeter").

The password is stored in AWS Secrets Manager, tagged with the DB resource ID. Each
Oracle replica has its own secret in Secrets Manager. The secret uses either of
the following naming formats.

```
do-not-delete-rds-custom-db-`DB_resource_id`-`uuid`-dg
rds-custom!oracle-do-not-delete-`DB_resource_id`-`uuid`-dg
```

- Don't change the `DB_UNIQUE_NAME` for the primary DB instance.
  Changing the name causes any restore operation to become stuck.
- Don't specify the clause `STANDBYS=NONE` in a `CREATE
PLUGGABLE DATABASE` command in an RDS Custom CDB. This way, if a
  failover occurs, your standby CDB contains all PDBs.

## General limitations for RDS Custom for Oracle replication

RDS Custom for Oracle replicas have the following limitations:

- You can't create RDS Custom for Oracle replicas in read-only mode. However, you can
  manually change the mode of mounted replicas to read-only, and from
  read-only to mounted. For more information, see the documentation for the
  [create-db-instance-read-replica](../../../cli/latest/reference/rds/create-db-instance-read-replica.md "../../../cli/latest/reference/rds/create-db-instance-read-replica.md") AWS CLI command.
- You can't create cross-Region RDS Custom for Oracle replicas.
- You can't change the value of the Oracle Data Guard `CommunicationTimeout` parameter. This parameter is set to 15
  seconds for RDS Custom for Oracle DB instances.

## Networking requirements and limitations for RDS Custom for Oracle replication

Make sure that your network configuration supports RDS Custom for Oracle replicas. Consider
the following:

- Make sure to enable port 1140 for both inbound and outbound communication
  within your virtual private cloud (VPC) for the primary DB instance and all of its
  replicas. This is required for Oracle Data Guard communication between read
  replicas.
- RDS Custom for Oracle validates the network while creating a Oracle replica. If the primary DB instance and the new replica can't connect
  over the network, RDS Custom for Oracle doesn't create the replica and places it in the `INCOMPATIBLE_NETWORK` state.
- For external Oracle replicas, such as those you create on Amazon EC2 or on-premises, use another port and listener for Oracle Data
  Guard replication. Trying to use port 1140 could cause conflicts with RDS Custom automation.
- The `/rdsdbdata/config/tnsnames.ora` file contains network service names mapped to listener protocol
  addresses. Note the following requirements and recommendations:
  - Entries in `tnsnames.ora` prefixed with `rds_custom_` are reserved for RDS Custom
    when handling Oracle replica operations.

  When creating manual entries in `tnsnames.ora`, don't use this prefix.
  - In some cases, you might want to switch over or fail over manually, or use failover technologies such as Fast-Start
    Failover (FSFO). If so, make sure to manually synchronize `tnsnames.ora` entries from the primary
    DB instance to all of the standby instances. This recommendation applies to both Oracle replicas managed by RDS Custom and
    to external Oracle replicas.

  RDS Custom automation updates `tnsnames.ora` entries on only the primary DB instance. Make sure also
  to synchronize when you add or remove a Oracle replica.

  If you don't synchronize the `tnsnames.ora` files and switch over or fail over manually,
  Oracle Data Guard on the primary DB instance might not be able to communicate with the Oracle replicas.

## External replica limitations for RDS Custom for Oracle

RDS Custom for Oracle external replicas, which include on-premises replicas, have the following limitations:

- RDS Custom for Oracle doesn't detect instance role changes upon manual failover, such
  as FSFO, for external Oracle replicas.

RDS Custom for Oracle does detect changes for managed replicas. The role change is
noted in the event log. You can also see the new state by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command.

- RDS Custom for Oracle doesn't detect high replication lag for external Oracle
  replicas.

RDS Custom for Oracle does detect lag for managed replicas. High replication lag
produces the `Replication has stopped` event. You can also see
the replication status by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command, but there might be a delay
for it to be updated.

- RDS Custom for Oracle doesn't promote external Oracle replicas automatically if you
  delete your primary DB instance.

The automatic promotion feature is available only for managed Oracle
replicas. For information about promoting Oracle replicas manually, see the
white paper [Enabling high availability with Data Guard on
Amazon RDS Custom for Oracle](https://d1.awsstatic.com/whitepapers/enabling-high-availability-with-data-guard-on-amazon-rds-custom-for-oracle.pdf "https://d1.awsstatic.com/whitepapers/enabling-high-availability-with-data-guard-on-amazon-rds-custom-for-oracle.pdf").
