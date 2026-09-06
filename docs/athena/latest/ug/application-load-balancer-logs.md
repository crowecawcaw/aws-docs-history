

# Query Application Load Balancer logs
<a name="application-load-balancer-logs"></a>

An Application Load Balancer is a load balancing option for Elastic Load Balancing that enables traffic distribution in a microservices deployment using containers. Querying Application Load Balancer logs allows you to see the source of traffic, latency, and bytes transferred to and from Elastic Load Balancing instances and backend applications. For more information, see [Access logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) and [Connection logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html) in the *User Guide for Application Load Balancers*.

## Prerequisites
<a name="application-load-balancer-logs-prerequisites"></a>
+ Enable [access logging](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) or [connection logging ](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html) so that Application Load Balancer logs can be saved to your Amazon S3 bucket.
+ A database to hold the table that you will create for Athena. To create a database, you can use the Athena or AWS Glue console. For more information, see [Create databases in Athena](creating-databases.md) in this guide or [Working with databases on the AWS glue console](https://docs.aws.amazon.com/glue/latest/dg/console-databases.html) in the *AWS Glue Developer Guide*. 

**Topics**
+ [Prerequisites](#application-load-balancer-logs-prerequisites)
+ [Create the table for ALB access logs](create-alb-access-logs-table.md)
+ [Create the table for ALB access logs in Athena using partition projection](create-alb-access-logs-table-partition-projection.md)
+ [Example queries for ALB access logs](query-alb-access-logs-examples.md)
+ [Create the table for ALB connection logs](create-alb-connection-logs-table.md)
+ [Create the table for ALB connection logs in Athena using partition projection](create-alb-connection-logs-table-partition-projection.md)
+ [Example queries for ALB connection logs](query-alb-connection-logs-examples.md)
+ [Additional resources](application-load-balancer-logs-additional-resources.md)