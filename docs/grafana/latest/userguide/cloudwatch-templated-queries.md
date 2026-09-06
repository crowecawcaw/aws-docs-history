

# Templated queries
<a name="cloudwatch-templated-queries"></a>

 Instead of hardcoding details such as servers, applications, and sensor names in your metric queries, you can use variables in their place. Variables are shown as dropdown select boxes at the top of the dashboard. You can use these dropdown boxes to change the data being displayed in your dashboard. 

 See [Templates](templates-and-variables.md#templates) for an introduction to the templating feature and the different types of template variables. 

## Query variable
<a name="cloudwatch-query-variable"></a>

 The CloudWatch data source provides the following queries that you can specify in the **Query** field in the **Variable** edit view. You can use these to fill a variable’s options list with things such as `region`, `namespaces`, `metric names`, and `dimension keys/values`. 

 In place of `region`, you can specify `default` to use the default Region configured in the data source for the query. 


|  Name  |  Description  | 
| --- | --- | 
|  regions()  |  Returns a list of all AWS Regions. | 
|  namespaces()  |  Returns a list of namespaces that CloudWatch supports.  | 
|  metrics(namespace, [region])  |  Returns a list of metrics in the namespace. (Specify the Region or use "default" for custom metrics.)  | 
|  dimension\_keys(namespace)  |  Returns a list of dimension keys in the namespace.  | 
|  dimension\_values(region, namespace, metric, dimension\_key, [filters])  |  Returns a list of dimension values matching the specified region, namespace, metric, or dimension\_key. ternatively, you can use dimension filters to get a more specific result.  | 
|  ebs\_volume\_ids(region, instance\_id)  |  Returns a list of volume IDs matching the specified region, instance\_id.  | 
|  ec2\_instance\_attribute(region, attribute\_name, filters)  |  Returns a list of attributes matching the specified region, attribute\_name, filters.  | 
|  resource\_arns(region, resource\_type, tags)  |  Returns a list of ARNs matching the specified region, resource\_type, and tags.  | 
|  statistics()  |  Returns a list of all the standard statistics.  | 

 For details about the metrics that CloudWatch provides, see [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html). 

### Examples of templated queries
<a name="cloudwatch-examples-templated-queries"></a>

 The following table shows example dimension queries that return a list of resources for individual AWS services. 


|  Query  |  Service  | 
| --- | --- | 
|  dimension\_values(us-east-1,AWS/ELB,RequestCount,LoadBalancerName)  |  Elastic Load Balancing  | 
|  dimension\_values(us-east-1,AWS/ElastiCache,CPUUtilization,CacheClusterId)  |  Amazon ElastiCache  | 
|  dimension\_values(us-east-1,AWS/Redshift,CPUUtilization,ClusterIdentifier)  |  Amazon Redshift  | 
|  dimension\_values(us-east-1,AWS/RDS,CPUUtilization,DBInstanceIdentifier)  |  Amazon RDS  | 
|  dimension\_values(us-east-1,AWS/S3,BucketSizeBytes,BucketName)  |  Amazon Simple Storage Service (Amazon S3)  | 
|  dimension\_values(us-east-1,CWAgent,disk\_used\_percent,device,{"InstanceId":"$instance\_id"})  |  CloudWatch Agent  | 
|  resource\_arns(eu-west-1,elasticloadbalancing:loadbalancer,{"elasticbeanstalk:environment-name":["myApp-dev","myApp-prod"]})  |  Elastic Load Balancing  | 
|  resource\_arns(eu-west-1,ec2:instance,{"elasticbeanstalk:environment-name":["myApp-dev","myApp-prod"]})  |  Amazon EC2  | 