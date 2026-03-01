# Query Application Load Balancer logs

An Application Load Balancer is a load balancing option for Elastic Load Balancing that enables traffic distribution in a
microservices deployment using containers. Querying Application Load Balancer logs allows you to see the source
of traffic, latency, and bytes transferred to and from Elastic Load Balancing instances and backend
applications. For more information, see [Access logs
for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md") and [Connection logs for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md") in the
_User Guide for Application Load Balancers_.

## Prerequisites

- Enable [access logging](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md") or [connection logging](../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md") so that Application Load Balancer logs can be saved to your Amazon S3
  bucket.
- A database to hold the table that you will create for Athena. To create a
  database, you can use the Athena or AWS Glue console. For more information, see
  [Create databases in Athena](creating-databases.md "creating-databases.md") in
  this guide or [Working with databases on the
  AWS glue console](../../../glue/latest/dg/console-databases.md "../../../glue/latest/dg/console-databases.md") in the _AWS Glue Developer Guide_.

###### Topics

- [Create the table for ALB access logs](create-alb-access-logs-table.md "create-alb-access-logs-table.md")
- [Create the table for ALB access logs in Athena using partition projection](create-alb-access-logs-table-partition-projection.md "create-alb-access-logs-table-partition-projection.md")
- [Example queries for ALB access logs](query-alb-access-logs-examples.md "query-alb-access-logs-examples.md")
- [Create the table for ALB connection logs](create-alb-connection-logs-table.md "create-alb-connection-logs-table.md")
- [Create the table for ALB connection logs in Athena using partition projection](create-alb-connection-logs-table-partition-projection.md "create-alb-connection-logs-table-partition-projection.md")
- [Example queries for ALB connection logs](query-alb-connection-logs-examples.md "query-alb-connection-logs-examples.md")
- [Additional resources](application-load-balancer-logs-additional-resources.md "application-load-balancer-logs-additional-resources.md")
