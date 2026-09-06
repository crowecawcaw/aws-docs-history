

# Query Amazon Route 53 resolver query logs
<a name="querying-r53-resolver-logs"></a>

You can create Athena tables for your Amazon Route 53 Resolver query logs and query them from Athena.

Route 53 Resolver query logging is for logging of DNS queries made by resources within a VPC, on-premises resources that use inbound resolver endpoints, queries that use an outbound Resolver endpoint for recursive DNS resolution, and queries that use Route 53 Resolver DNS firewall rules to block, allow, or monitor a domain list. For more information about Resolver query logging, see [Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html) in the *Amazon Route 53 Developer Guide*. For information about each of the fields in the logs, see [Values that appear in resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-format.html) in the *Amazon Route 53 Developer Guide*.

**Topics**
+ [Create the table for resolver query logs](querying-r53-resolver-logs-creating-the-table.md)
+ [Use partition projection](querying-r53-resolver-logs-partitioning-example.md)
+ [Example queries](querying-r53-resolver-logs-example-queries.md)