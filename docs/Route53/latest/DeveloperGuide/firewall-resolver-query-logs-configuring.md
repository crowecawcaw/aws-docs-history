# Configuring logging for

DNS Firewall

You can evaluate your DNS Firewall rules by using Amazon CloudWatch metrics and the Resolver
query logs. The logs provide the domain list name for all alerts and blocking
actions. For more information about Amazon CloudWatch, see [Monitoring Route 53 Resolver DNS Firewall rule
groups with Amazon CloudWatch](monitoring-resolver-dns-firewall-with-cloudwatch.md "monitoring-resolver-dns-firewall-with-cloudwatch.md").

When you enable DNS Firewall, associate it to a VPC, and you have logging enabled,
`firewall_rule_group_id`, `firewall_rule_action`, and
`firewall_domain_list_id` are the DNS Firewall specific fields provided
within your logs.

###### Note

The query logs will show the additional DNS Firewall fields for only the queries that are blocked
by DNS Firewall rules.

To start logging the DNS queries that are filtered by DNS Firewall rules that
originate in your VPCs, you perform the following tasks in the Amazon Route 53
console:

###### To configure

Resolver query logging for DNS Firewall

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. Expand the Route 53 console menu. In the upper left corner of the console,
   choose the three horizontal bars (
   ![Menu icon](images/menu-icon.png)
   ) icon.
3. Within the Resolver menu, choose **Query
   logging**.
4. In the Region selector, choose the AWS Region where you want to create
   the query logging configuration.

This must be the same Region where you created the VPCs that are associated with DNS Firewall
that you want to log queries for. If you have VPCs in multiple Regions, you
must create at least one query logging configuration for each Region. 5. Choose **Configure query logging**. 6. Specify the following values:

**Query logging configuration name**

Enter a name for your query logging configuration. The name
appears in the console in the list of query logging
configurations. Enter a name that will help you find this
configuration later.

**Query logs destination**

Choose the type of AWS resource that you want Resolver to send
query logs to. For information about how to choose among the
options (CloudWatch Logs log group, S3 bucket, and Firehose delivery stream),
see [AWS resources that you
can send Resolver query logs to](resolver-query-logs-choosing-target-resource.md "resolver-query-logs-choosing-target-resource.md").

After you choose the type of resource, you can either create
another resource of that type or choose an existing resource
that was created by the current AWS account.

###### Note

You can choose only resources that were created in the
AWS Region that you chose in step 4, the Region where
you're creating the query logging configuration. If you
choose to create a new resource, that resource will be
created in the same Region.

**VPCs to log queries for**

This query logging configuration will log DNS queries that
originate in the VPCs that you choose. Check the check box for
each VPC in the current Region that you want Resolver to log
queries for, then choose **Choose**.

###### Note

VPC log delivery can be enabled only once for a specific
destination type. The logs can't be delivered to multiple
destinations of the same type. For example, VPC logs can't
be delivered to two Amazon S3 destinations. 7. Choose **Configure query logging**.

###### Note

You should start to see DNS queries made by resources in your VPC in the logs
within a few minutes of successfully creating the query logging
configuration.
