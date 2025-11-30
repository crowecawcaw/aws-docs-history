# Considerations for Database Insights for Amazon RDS

Following are considerations for Database Insights for Amazon RDS.

- You can't manage Database Insights for a DB instance in a Multi-AZ DB cluster.
- To enable the Advanced mode of Database Insights, you must enable Performance Insights and set the Performance Insights retention period to at least 465 days (15 months). There is no additional cost to set the Performance Insights retention period to 15
  months besides the cost of Database Insights. For information about pricing for Database Insights, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
- To enable Database Insights, each DB instance in a Multi-AZ DB cluster must have the same Performance Insights and Enhanced Monitoring settings.
- Modifying a DB instance to enable either mode of Database Insights doesn't cause downtime.
