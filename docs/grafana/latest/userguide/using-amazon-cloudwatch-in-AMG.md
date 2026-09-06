

# Connect to an Amazon CloudWatch data source
<a name="using-amazon-cloudwatch-in-AMG"></a>

With Amazon Managed Grafana, you can add Amazon CloudWatch as a data source by using the AWS data source configuration option in the Grafana workspace console. This feature simplifies adding CloudWatch as a data source by discovering your existing CloudWatch accounts and manages the configuration of the authentication credentials that are required to access CloudWatch. You can use this method to set up authentication and add CloudWatch as a data source. Alternatively, you can manually set up the data source and the necessary authentication credentials using the same method that you would on a self-managed Grafana server.

**Tip**  
You can also query CloudWatch metrics using PromQL through the Amazon Managed Service for Prometheus data source. For more information, see [Query Amazon CloudWatch metrics using PromQL](cloudwatch-promql.md).

**Topics**
+ [Use AWS data source configuration to add CloudWatch as a data source](adding-CloudWatch-AWS-config.md)
+ [Manually add CloudWatch as a data source](adding--CloudWatch-manual.md)
+ [Using the query editor](CloudWatch-using-the-query-editor.md)
+ [Curated dashboards](CloudWatch-curated-dashboards.md)
+ [Templated queries](cloudwatch-templated-queries.md)
+ [Using ec2\_instance\_attribute examples](cloudwatch-ec2-instance-attribute-examples.md)
+ [Using JSON format template variables](cloudwatch-using-json-format-template-variables.md)
+ [Pricing](cloudwatch-pricing.md)
+ [Service quotas](cloudwatch-service-quotas.md)
+ [Cross-account observability](cloudwatch-cross-account.md)