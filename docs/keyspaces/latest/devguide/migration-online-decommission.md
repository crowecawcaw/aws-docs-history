# Decommissioning Cassandra after an online migration

After the application migration is complete with your application is fully running on Amazon Keyspaces and you have validated data
consistency over a period of time, you can plan to decommission your Cassandra cluster. During this phase, you can evaluate if
the data remaining in your Cassandra cluster needs to be archived or can be deleted. This depends on your organization’s policies
for data handling and retention.

By following this strategy and considering the recommended best practices described in this topic when planning your online
migration from Cassandra to Amazon Keyspaces, you can ensure a seamless transition to Amazon Keyspaces while maintaining read-after-write
consistency and availability of your application.

Migrating from Apache Cassandra to Amazon Keyspaces can provide numerous benefits, including reduced operational overhead,
automatic scaling, improved security, and a framework that helps you to reach your compliance goals.
By planning an online migration strategy with dual writes, historical data upload, data validation, and a gradual roll out,
you can ensure a smooth transition with
minimal disruption to your application and its users.

Implementing the online migration strategy discussed in this topic allows you to validate the migration results, identify
and
address any issues, and ultimately decommission your existing Cassandra deployment in favor of the fully managed Amazon Keyspaces
service.
