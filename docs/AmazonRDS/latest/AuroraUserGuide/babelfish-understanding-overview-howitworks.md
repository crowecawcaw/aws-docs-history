# Understanding Babelfish architecture and configuration

You manage the Aurora PostgreSQL-Compatible Edition DB cluster running Babelfish much as you would any
Aurora DB cluster. That is, you benefit from the scalability, high-availability with failover
support, and built-in replication provided by an Aurora DB cluster. To learn more about these
capabilities, see [Managing performance and scaling for Aurora DB clusters](Aurora.Managing.md "Aurora.Managing.md"), [High availability for Amazon Aurora](Concepts.md "Concepts.md"), and [Replication with Amazon Aurora](Aurora.md "Aurora.md"). You also have access
to many other AWS tools and utilities, including the following:

- Amazon CloudWatch is a monitoring and observability
  service that provides you with data and actionable insights. For more information,
  see [Monitoring Amazon Aurora metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Performance Insights is a database performance tuning and monitoring
  feature that helps you quickly assess the load on your database. To learn more,
  see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").
- Aurora global
  databases span multiple AWS Regions, enabling low latency
  global reads and providing fast recovery from the rare outage that might affect an entire AWS Region.
  For more information, see [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md").
- Automatic software patching keeps your database up-to-date with the latest security and
  feature patches when they become available.
- Amazon RDS events notify you by email or SMS message of important database
  events, such as an automated failover. For more information, see
  [Monitoring Amazon Aurora events](working-with-events.md "working-with-events.md").
  Following, you can learn about Babelfish architecture and how the SQL Server databases that you migrate are
  handled by Babelfish. When you create your Babelfish DB cluster, you need to make some decisions
  up front about single database or multiple databases, collations, and other details.

###### Topics

- [Babelfish architecture](babelfish-architecture.md "babelfish-architecture.md")
- [DB cluster parameter group settings for Babelfish](babelfish-configuration.md "babelfish-configuration.md")
- [Understanding Collations in Babelfish for Aurora PostgreSQL](babelfish-collations.md "babelfish-collations.md")
- [Managing Babelfish error handling with escape hatches](babelfish-strict.md "babelfish-strict.md")
