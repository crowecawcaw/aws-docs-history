

# What is AWS Compute Optimizer?
<a name="what-is-compute-optimizer"></a>

With AWS Compute Optimizer, you can analyze the configuration and utilization metrics of your AWS resources to get rightsizing recommendations and find idle resources. You can see whether your resources are optimal, and apply recommendations that lower your costs and improve the performance of your workloads.

To compare recommendations, you can use utilization graphs that show your recent usage and the usage you can expect from each recommendation. Use them to choose the best balance of price and performance, and to decide when to move, resize, stop, or delete resources while still meeting your performance and capacity needs.

With Compute Optimizer, you can use the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer) or a [set of APIs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/Welcome.html) to view findings and recommendations for your resources. No coding is required to use the console. You can view findings across many AWS Regions, and if you opt in as the management account of an organization, across many accounts. You can also see the findings in the consoles of supported services, such as the Amazon EC2 console.

## Features of Compute Optimizer
<a name="intro-features"></a>

Compute Optimizer includes the following features:

Rightsizing recommendations  
Get recommendations to resize or move your resources so that they match your workload requirements.

Idle resource identification  
Find idle resources that you can stop or delete to reduce costs.

Utilization graphs  
Compare recommendations by using graphs of recent and projected utilization.

Cross-account and cross-Region visibility  
View findings and recommendations across multiple accounts and AWS Regions.

Recommendation preferences  
Tailor your recommendations with options such as enhanced infrastructure metrics and rightsizing recommendation preferences.

Exportable recommendations  
Export your recommendations to track them over time and share them.

## Supported resources
<a name="intro-supported-resources"></a>

Compute Optimizer generates recommendations for the following resources:
+ Amazon Elastic Compute Cloud (Amazon EC2) instances
+ Amazon EC2 Auto Scaling groups
+ Amazon Elastic Block Store (Amazon EBS) volumes
+ AWS Lambda functions
+ Amazon Elastic Container Service (Amazon ECS) services on AWS Fargate 
+ Commercial software licenses
+ Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases
+ NAT gateways
+ Amazon DynamoDB
+ Amazon ElastiCache
+ Amazon MemoryDB
+ Amazon DocumentDB
+ Amazon WorkSpaces
+ Amazon SageMaker

Compute Optimizer makes recommendations only for resources that meet certain requirements. The resources must also have enough metric data. For more information, see [Resource requirements](requirements.md).

## Opting in
<a name="intro-opting-in"></a>

Compute Optimizer doesn't analyze your resources or generate recommendations until you opt in. You can opt in a standalone AWS account, a member account of an organization, or the management account of an organization. For more information, see [Opting in to AWS Compute Optimizer](account-opt-in.md).

## Analyzing metrics
<a name="intro-metrics-analyzed"></a>

After you opt in, Compute Optimizer looks at the specifications of your resources. It also looks at their use metrics from Amazon CloudWatch for the last 14 days. For example, for Amazon EC2 instances, Compute Optimizer looks at the virtual CPUs (vCPUs), memory, storage, and other specifications. It also looks at CPU use, network in and out, disk read and write, and other metrics of running instances. For more information, see [Metrics analyzed by AWS Compute Optimizer](metrics.md).

## Enhancing recommendations
<a name="intro-enhanced-infrastructure-metrics"></a>

After you opt in, you can turn on recommendation preferences to improve your recommendations. One example is enhanced infrastructure metrics, a paid feature. It extends the lookback period for chosen resources to 93 days. The default is 14 days. For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md).

You can also use rightsizing recommendation preferences. With them, you can change CPU and memory headroom and thresholds. You can also set lookback periods and instance family preferences. You can set these for an organization, an account, or a Region. For more information, see [Rightsizing recommendation preferences](rightsizing-preferences.md).

Compute Optimizer can also use EC2 memory metrics from other tools, such as Datadog and Dynatrace. This helps it make more accurate EC2 rightsizing recommendations. For more information, see [External metrics ingestion](external-metrics-ingestion.md).

## Viewing findings and recommendations
<a name="intro-analyzing-data"></a>

The Compute Optimizer dashboard shows the findings for your resources. For more information, see [Using the AWS Compute Optimizer dashboard](viewing-dashboard.md).

The recommendations page lists the top recommendation for each of your resources. The resource details page lists the top 3 recommendations for one resource. It also shows its use graphs. For more information, see [Viewing resource recommendations](viewing-recommendations.md).

Export your optimization recommendations to record them over time, and share the data with others. For more information, see [Exporting AWS Compute Optimizer recommendations](exporting-recommendations.md).

## Pricing for Compute Optimizer
<a name="intro-pricing"></a>

Compute Optimizer provides recommendations based on the default metrics analysis at no additional cost. Enhanced infrastructure metrics is a paid feature that extends the metrics analysis lookback period. For more information, see [Compute Optimizer pricing](https://aws.amazon.com/compute-optimizer/pricing/).

## Availability
<a name="intro-availability"></a>

To view the currently supported AWS Regions and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/compute-optimizer.html) in the *AWS General Reference*.