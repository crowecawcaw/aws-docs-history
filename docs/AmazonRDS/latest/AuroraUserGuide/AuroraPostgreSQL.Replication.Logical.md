# Example: Logical

replication using Aurora PostgreSQL and AWS Database Migration Service

You can use the AWS Database Migration Service (AWS DMS) to replicate a database or a portion of a database.
Use AWS DMS to migrate your data from an Aurora PostgreSQL database to another open source or
commercial database. For more information about AWS DMS, see the [AWS Database Migration Service User Guide](../../../dms/latest/userguide.md "../../../dms/latest/userguide.md").

The following example shows how to set up logical replication from an Aurora PostgreSQL
database as the publisher and then use AWS DMS for migration. This example uses the same
publisher and subscriber that were created in [Example: Using
logical replication with Aurora PostgreSQL DB clusters](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md").

To set up logical replication with AWS DMS, you need details about your publisher and
subscriber from Amazon RDS. In particular, you need details about the publisher's writer
DB instance and the subscriber's DB instance.

Get the following information for the publisher's writer DB instance:

- The virtual private cloud (VPC) identifier
- The subnet group
- The Availability Zone (AZ)
- The VPC security group
- The DB instance ID
  Get the following information for the subscriber's DB instance:

- The DB instance ID
- The source engine

###### To use AWS DMS for logical replication with Aurora PostgreSQL

1. Prepare the publisher database to work with AWS DMS.

To do this, PostgreSQL 10.x and later databases require that you apply AWS DMS
wrapper functions to the publisher database. For details on this and later
steps, see the instructions in [Using PostgreSQL version 10.x and later as a source for AWS DMS](../../../dms/latest/userguide/CHAP_Source.md#CHAP_Source.PostgreSQL.v10 "../../../dms/latest/userguide/CHAP_Source.md#CHAP_Source.PostgreSQL.v10") in
the _AWS Database Migration Service User Guide._ 2. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2"). At top right, choose the same AWS Region in which the
publisher and subscriber are located. 3. Create an AWS DMS replication instance.

Choose values that are the same as for your publisher's writer DB
instance. These include the following settings:

    * For **VPC**, choose the same VPC as for the writer DB
     instance.
    * For **Replication Subnet Group**, choose a subnet
     group with the same values as the writer DB instance. Create a new one
     if necessary.
    * For **Availability zone**, choose the same zone as
     for the writer DB instance.
    * For **VPC Security Group**, choose the same group as
     for the writer DB instance.

4. Create an AWS DMS endpoint for the source.

Specify the publisher as the source endpoint by using the following settings:

    * For **Endpoint type**, choose **Source
     endpoint**.
    * Choose **Select RDS DB Instance**.
    * For **RDS Instance**, choose the DB identifier of the
     publisher's writer DB instance.
    * For **Source engine**, choose
     **postgres**.

5. Create an AWS DMS endpoint for the target.

Specify the subscriber as the target endpoint by using the following
settings:

    * For **Endpoint type**, choose **Target
     endpoint**.
    * Choose **Select RDS DB Instance**.
    * For **RDS Instance**, choose the DB identifier of the
     subscriber DB instance.
    * Choose a value for **Source engine**. For example, if
     the subscriber is an RDS PostgreSQL database, choose
     **postgres**. If the subscriber is an Aurora PostgreSQL
     database, choose **aurora-postgresql**.

6. Create an AWS DMS database migration task.

You use a database migration task to specify what database tables to migrate,
to map data using the target schema, and to create new tables on the target
database. At a minimum, use the following settings for **Task
configuration**:

    * For **Replication instance**, choose the replication
     instance that you created in an earlier step.
    * For **Source database endpoint**, choose the
     publisher source that you created in an earlier step.
    * For **Target database endpoint**, choose the
     subscriber target that you created in an earlier step.

The rest of the task details depend on your migration project. For more
information about specifying all the details for DMS tasks, see [Working with AWS DMS tasks](../../../dms/latest/userguide/CHAP_Tasks.md "../../../dms/latest/userguide/CHAP_Tasks.md") in
the _AWS Database Migration Service User Guide._
After AWS DMS creates the task, it begins migrating data from the publisher to the
subscriber.
