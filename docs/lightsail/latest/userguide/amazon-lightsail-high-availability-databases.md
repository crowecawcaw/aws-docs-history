# High availability databases in

Lightsail

A Lightsail high availability managed database provides failover support with a primary
database in one Availability Zone, and a secondary standby database in another. We recommend
high availability databases for production workloads that experience heavy use and require data
redundancy. For development and test purposes, you can use a standard database that isn't high
availability.

To create a high availability database, select one of the high availability database plans
available in Lightsail when creating your managed database. For more information, see [Create a database](amazon-lightsail-creating-a-database.md "amazon-lightsail-creating-a-database.md") . You can also change
your standard database to a high availability database. Create a snapshot of your standard
database, create a new database from the snapshot, and choose a high availability plan. For more
information, see [Create a
database from a snapshot](amazon-lightsail-creating-a-database-from-snapshot.md "amazon-lightsail-creating-a-database-from-snapshot.md").
