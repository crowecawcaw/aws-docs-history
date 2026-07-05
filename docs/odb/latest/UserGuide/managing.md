# Managing Oracle Database@AWS

You can modify and delete some Oracle Database@AWS resources after you create them.

## Updating an ODB network in Oracle Database@AWS

You can update the following ODB network resources:

- The ODB network name
- The Amazon VPC to use for establishing an ODB peering connection to the ODB network
- The VPC CIDR ranges that can access Exadata resources in the ODB network

###### Note

By specifying CIDR ranges, you limit connectivity to the necessary VPC subnets instead of
making the entire VPC available to the ODB network.

This section assumes that you have already created an ODB network in [Step 1: Create an ODB network in Oracle Database@AWS](getting-started.md#getting-started-odb "getting-started.md#getting-started-odb").

###### To update an ODB network

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **ODB networks**.
3. Select the network that you want to modify.
4. Choose **Modify**.
5. (Optional) For **ODB network name**, enter a new network name. The name must
   be 1–255 characters and begin with an alphabetic character or underscore. It can't
   contain consecutive hyphens.
6. (Optional) For **Peered CIDRs**, specify CIDR ranges from the peered VPC
   that need connectivity to the ODB network. To limit access, we recommend that you specify the
   minimum required CIDR ranges.
7. (Optional) For **Configure service integrations**, select or deselect
   **Amazon S3** or **Zero-ETL**.
8. Choose **Continue**, and then choose **Modify**.

## Deleting an ODB network in Oracle Database@AWS

You can delete an ODB network. This section assumes that you have already created an ODB network in
[Step 1: Create an ODB network in Oracle Database@AWS](getting-started.md#getting-started-odb "getting-started.md#getting-started-odb"). You can't delete an
ODB network that is currently in use by a VM cluster.

###### To delete an ODB network

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **ODB networks**.
3. Select the network that you want to delete.
4. Choose **Delete**.
5. (Optional) Choose **Delete associated OCI resources** to delete the OCI
   resources that were created along with the ODB network.
6. In the text box, enter `delete me`.
7. Choose **Delete**.

## Deleting a VM cluster in Oracle Database@AWS

You can delete an Exadata VM cluster or Autonomous VM cluster. This section assumes that you have already
created a VM cluster in [Step 3: Create an Exadata VM cluster or Autonomous VM cluster in Oracle Database@AWS](getting-started.md#getting-started-vm "getting-started.md#getting-started-vm").

###### To delete a VM cluster

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **Exadata VM clusters** or **Autonomous
   VM clusters**.
3. Choose a VM cluster to delete.
4. Choose **Delete**.
5. When prompted, enter `delete me` and then choose
   **Delete**.

## Deleting an Oracle Exadata infrastructure in Oracle Database@AWS

You can delete an Oracle Exadata infrastructure. This section assumes that you have already created an Oracle Exadata infrastructure
in [Step 2: Create an Oracle Exadata infrastructure in Oracle Database@AWS](getting-started.md#getting-started-infra "getting-started.md#getting-started-infra"). You can't
delete an Exadata infrastructure that is currently in use by a VM cluster.

###### To delete an Oracle Exadata infrastructure

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **Exadata infrastructures**.
3. Choose an Exadata infrastructure to delete.
4. Choose **Delete**.
5. When prompted, enter `delete me` and then choose
   **Delete**.

## Deleting an ODB peering connection

When you no longer need an ODB peering connection, you can delete it. You must delete all ODB peering connections before you can delete an ODB network.

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. In the navigation pane, choose **ODB peering connections**.
3. Select the ODB peering connection to delete.
4. Choose **Delete**.
5. To confirm deletion, enter `delete me` and choose
   **Delete**.
   To delete an ODB peering connection, use the `delete-odb-peering-connection`
   command.

```
aws odb delete-odb-peering-connection \
    --odb-peering-connection-id `odbpcx-1234567890abcdef`
```

## Managing Autonomous Database Serverless instances

You can perform the following lifecycle operations on Autonomous Database Serverless (ADB-S)
instances from the Oracle Database@AWS console, CLI, or APIs.

###### Note

Some operations may also be available from the OCI console. Check the OCI documentation
for additional management options.

**Start and stop**

Start and stop an ADB-S instance to reduce cost when the database is not in use. When
stopped, compute charges stop while storage charges continue.

**Scaling**

Scale ECPUs and storage independently. You can also enable or disable auto-scaling to
allow the database to automatically use up to three times the base ECPU count during peak
workloads.

**Switchover**

Initiate a switchover to the standby database for planned maintenance or testing.

**Failover**

Perform a manual failover for disaster recovery scenarios.

**Clone**

Create a full clone or metadata clone of an ADB-S instance.

**Restart**

Restart the database instance without stopping and starting it manually.

**Delete**

Permanently delete an ADB-S instance. This action cannot be undone.

## Encryption using AWS Key Management Service

To use AWS Key Management Service encryption with ADB-S, you need the following:

- An IAM role with a trust policy that allows the OCI service account role to assume
  this role, and permission to perform `kms:ListKeys` and
  `kms:ListAliases` actions. This trust policy can be updated to include an
  `sts:ExternalId` condition.
- An AWS Key Management Service key with a key policy that allows the above IAM role to perform
  `kms:Encrypt`, `kms:Decrypt`, and `kms:DescribeKey`
  actions.

Additional permissions required for the caller:

- `iam:PassRole` scoped to the above IAM role
- `kms:DescribeKey` on the AWS Key Management Service key being used
