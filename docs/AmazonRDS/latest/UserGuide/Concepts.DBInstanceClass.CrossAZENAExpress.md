

# Cross-Availability Zone ENA Express support for Multi-AZ deployments
<a name="Concepts.DBInstanceClass.CrossAZENAExpress"></a>

Amazon RDS supports Cross-Availability Zone ENA Express for eligible DB instance classes in Multi-AZ deployments using AWS's Scalable Reliable Datagram (SRD) protocol. Cross-Availability Zone ENA Express increases single-flow network bandwidth enabling faster block-level data replication between primary and standby DB instances.

For more details on SRD and for a list of instance classes that support Cross-Availability Zone ENA Express, see [ENA Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html) in the Amazon EC2 documentation.

**Note**  
Cross-Availability Zone ENA Express is not supported for Amazon RDS for SQL Server.

## Benefits
<a name="Concepts.DBInstanceClass.CrossAZENAExpress.Benefits"></a>

With Cross-Availability Zone ENA Express enabled, Multi-AZ deployments see an increase in single-flow bandwidth for data replication between Availability Zones. With advanced congestion control and multi-pathing capabilities, Cross-Availability Zone ENA Express reduces replication latency and replication latency variability and improves failover reliability for write-intensive workloads.

Actual throughput depends on the aggregate bandwidth limit of the DB instance class, the database engine, and your database configuration.

## Enabling Cross-Availability Zone ENA Express
<a name="Concepts.DBInstanceClass.CrossAZENAExpress.Enabling"></a>

Cross-Availability Zone ENA Express is enabled by default on all newly created Multi-AZ DB instances that use eligible instance classes.

To enable Cross-Availability Zone ENA Express on an existing Multi-AZ DB instance, do one of the following:
+ Stop and start the DB instance. For more information, see [Stopping an Amazon RDS DB instance temporarily](USER_StopInstance.md).
+ Modify the DB instance to use an eligible instance class. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).
+ Use Scale Compute on an eligible instance class. For more information, see [Scale Compute](https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/scaling-ha.html).