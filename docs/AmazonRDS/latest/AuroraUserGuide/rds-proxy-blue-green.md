

# Using RDS Proxy with Blue/Green Deployments
<a name="rds-proxy-blue-green"></a>

Amazon RDS Proxy can be used with Blue/Green Deployments to reduce switchover downtime. RDS Proxy eliminates DNS propagation delays that typically occur during database transitions by maintaining awareness of the switchover process and automatically redirecting connections to the Green environment once it becomes the active production environment. RDS Proxy works seamlessly with Aurora database engines, and requires no application code changes or custom client drivers.

## Switchover when using RDS Proxy
<a name="rds-proxy-blue-green-switchover"></a>

When your blue cluster is attached to RDS Proxy, the following process occurs during switchover:
+ Switchover Guardrails
  + Amazon RDS runs additional guardrail checks to validate that the proxy can successfully reach both blue and green environments and is ready for switchover.
+ Application Traffic Routing During Switchover

  For the list of switchover actions, see [Switchover actions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-switching.html#blue-green-deployments-switching-actions). When the switchover happens through RDS Proxy, note the following considerations:
  + During switchover, the Blue database enters read-only mode before Green environment is promoted. RDS Proxy continues routing connections to the blue database during this transitional period.
  + Write operations on Aurora MySQL during this period may return read-only errors. For example `1290 (HY000): The MySQL server is running with the —read-only option` so it cannot execute this statement. On Aurora PostgreSQL read and write queries will return AdminShutdown terminating connection due to administrator command.
  + Once the switchover is detected, the proxy automatically routes traffic to the newly promoted green environment.
  + When the Green environment is promoted as the new writer, existing connections to the proxy are dropped. Applications must re-establish connections after the promotion is complete.
  + You can review CloudWatch logs for RDS Proxy to see when this transitional behavior occurred.
+ RDS Proxy API Behavior
  + Proxy APIs such as `describe-db-proxy-targets` reflect the updated targets only after the switchover is fully complete, even though traffic routing occurs earlier.

## Limitations
<a name="rds-proxy-blue-green-limitations"></a>
+ Your blue cluster must already be a target of the proxy before you create the blue/green deployment. You cannot add a blue cluster to an RDS Proxy after a blue/green deployment has been created for that cluster.
+ RDS Proxy with blue/green deployments is not supported for Aurora Global Databases.