

# Example: Using logical replication with Aurora PostgreSQL DB clusters
<a name="AuroraPostgreSQL.Replication.Logical.PostgreSQL-Example"></a>

The following procedure shows you how to start logical replication between two Aurora PostgreSQL DB clusters. Both the publisher and the subscriber must be configured for logical replication as detailed in [Setting up logical replication for your Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Replication.Logical.Configure.md).

The Aurora PostgreSQL DB cluster that's the designated publisher must also allow access to the replication slot. To do so, modify the security group associated with the Aurora PostgreSQL DB cluster 's virtual public cloud (VPC) based on the Amazon VPC service. Allow inbound access by adding the security group associated with the subscriber's VPC to the publisher's security group. For more information, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*. 

With these preliminary steps complete, you can use PostgreSQL commands `CREATE PUBLICATION` on the publisher and the `CREATE SUBSCRIPTION` on the subscriber, as detailed in the following procedure. 

**To start the logical replication process between two Aurora PostgreSQL DB clusters**

These steps assume that your Aurora PostgreSQL DB clusters have a writer instance with a database in which to create the example tables.

1. **On the publisher Aurora PostgreSQL DB cluster**

   1. Create a table using the following SQL statement.

      ```
      CREATE TABLE LogicalReplicationTest (a int PRIMARY KEY);
      ```

   1. Insert data into the publisher database by using the following SQL statement.

      ```
      INSERT INTO LogicalReplicationTest VALUES (generate_series(1,10000));
      ```

   1. Verify that data exists in the table by using the following SQL statement.

      ```
      SELECT count(*) FROM LogicalReplicationTest;
      ```

   1. Create a publication for this table by using the `CREATE PUBLICATION` statement, as follows.

      ```
      CREATE PUBLICATION testpub FOR TABLE LogicalReplicationTest;
      ```

1. **On the subscriber Aurora PostgreSQL DB cluster**

   1. Create the same `LogicalReplicationTest` table on the subscriber that you created on the publisher, as follows.

      ```
      CREATE TABLE LogicalReplicationTest (a int PRIMARY KEY);
      ```

   1. Verify that this table is empty.

      ```
      SELECT count(*) FROM LogicalReplicationTest;
      ```

   1. Create a subscription to get the changes from the publisher. You need to use the following details about the publisher Aurora PostgreSQL DB cluster.
      + **host** – The publisher Aurora PostgreSQL DB cluster's writer DB instance.
      + **port** – The port on which the writer DB instance is listening. The default for PostgreSQL is 5432.
      + **dbname** – The name of the database.

      ```
      CREATE SUBSCRIPTION testsub CONNECTION 
         'host={{publisher-cluster-writer-endpoint}} port=5432 dbname={{db-name}} user={{user}} password={{password}}' 
         PUBLICATION testpub;
      ```
**Note**  
Specify a password other than the prompt shown here as a security best practice.

      After the subscription is created, a logical replication slot is created at the publisher.

   1. To verify for this example that the initial data is replicated on the subscriber, use the following SQL statement on the subscriber database.

      ```
      SELECT count(*) FROM LogicalReplicationTest;
      ```

Any further changes on the publisher are replicated to the subscriber.

Logical replication affects performance. We recommend that you turn off logical replication after your replication tasks are complete. 