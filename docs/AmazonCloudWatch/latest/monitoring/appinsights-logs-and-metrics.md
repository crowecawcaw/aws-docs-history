# Logs and metrics supported by
 Amazon CloudWatch Application Insights

The following lists show the supported logs and metrics for Amazon CloudWatch Application Insights. 

**CloudWatch Application Insights supports the following logs:**


* Microsoft Internet Information Services (IIS) logs
* Error log for SQL Server on EC2
* Custom .NET application logs, such as Log4Net
* Windows Event logs, including Windows logs (System, Application, and Security)
 and Applications and Services log
* Amazon CloudWatch Logs for AWS Lambda
* Error log and slow log for RDS MySQL, Aurora MySQL, and MySQL on EC2
* Postgresql log for PostgreSQL RDS and PostgreSQL on EC2
* Amazon CloudWatch Logs for AWS Step Functions
* Execution logs and access logs (JSON, CSV, and XML, but not CLF) for API Gateway
 REST API stages
* Prometheus JMX exporter logs (EMF)
* Alert logs and listener logs for Oracle on Amazon RDS and Oracle on Amazon
 EC2
* Container logs routing from Amazon ECS containers to CloudWatch using [`awslogs` log driver](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html").
* Container logs routing from Amazon ECS containers to CloudWatch using [FireLens container
 log router](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html").
* Container logs routing from Amazon EKS or Kubernetes running on Amazon EC2 to CloudWatch using
 [Fluent Bit or Fluentd log processor](Container-Insights-EKS-logs.md "Container-Insights-EKS-logs.md") with Container Insights.
* SAP HANA trace and error logs
* HA Pacemaker logs
* SAP ASE server logs
* SAP ASE backup server logs
* SAP ASE Replication server logs
* SAP ASE RMA agent logs
* SAP ASE Fault Manager logs
* SAP NetWeaver dev trace logs
* Process metrics for Windows processes using [proctstat plugin for
 CloudWatch agent](CloudWatch-Agent-procstat-process-metrics.md "CloudWatch-Agent-procstat-process-metrics.md")
* Public DNS query logs for hosted zone
* Amazon Route 53 Resolver DNS query logs
**CloudWatch Application Insights supports the following log classes:**


* **Standard** – Amazon CloudWatch Application Insights requires that log
 groups are configured with the [CloudWatch Logs
 Standard log class](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html") to enable monitoring.
###### CloudWatch Application Insights supports metrics for the following application components:

* [Amazon Elastic Compute Cloud (EC2)](appinsights-metrics-ec2.md "appinsights-metrics-ec2.md") 


	+ [CloudWatch built-in metrics](appinsights-metrics-ec2.md#appinsights-metrics-ec2-built-in "appinsights-metrics-ec2.md#appinsights-metrics-ec2-built-in")
	+ [CloudWatch agent metrics (Windows
	 server)](appinsights-metrics-ec2.md#appinsights-metrics-ec2-windows "appinsights-metrics-ec2.md#appinsights-metrics-ec2-windows")
	+ [CloudWatch agent process
	 metrics (Windows server)](appinsights-metrics-ec2.md#appinsights-metrics-procstat-ec2-windows "appinsights-metrics-ec2.md#appinsights-metrics-procstat-ec2-windows")
	+ [CloudWatch agent metrics (Linux
	 server)](appinsights-metrics-ec2.md#appinsights-metrics-ec2-linux "appinsights-metrics-ec2.md#appinsights-metrics-ec2-linux")
* [Elastic Block Store (EBS)](appinsights-metrics-ebs.md "appinsights-metrics-ebs.md")
* [Amazon Elastic File System (Amazon EFS)](appinsights-metrics-efs.md "appinsights-metrics-efs.md")
* [Elastic Load Balancer (ELB)](appinsights-metrics-elb.md "appinsights-metrics-elb.md")
* [Application ELB](appinsights-metrics-app-elb.md "appinsights-metrics-app-elb.md")
* [Amazon EC2 Auto Scaling groups](appinsights-metrics-as.md "appinsights-metrics-as.md")
* [Amazon Simple Queue Server (SQS)](appinsights-metrics-sqs.md "appinsights-metrics-sqs.md")
* [Amazon Relational Database Service (RDS)](appinsights-metrics-rds.md "appinsights-metrics-rds.md") 


	+ [RDS Database
	 instances](appinsights-metrics-rds.md#appinsights-metrics-rds-instances "appinsights-metrics-rds.md#appinsights-metrics-rds-instances")
	+ [RDS Database clusters](appinsights-metrics-rds.md#appinsights-metrics-rds-clusters "appinsights-metrics-rds.md#appinsights-metrics-rds-clusters")
* [AWS Lambda function](appinsights-metrics-lambda.md "appinsights-metrics-lambda.md")
* [Amazon DynamoDB table](appinsights-metrics-dyanamodb.md "appinsights-metrics-dyanamodb.md")
* [Amazon S3 bucket](appinsights-metrics-s3.md "appinsights-metrics-s3.md")
* [AWS Step Functions](appinsights-metrics-step-functions.md "appinsights-metrics-step-functions.md")


	+ [Execution-level](appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-execution "appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-execution")
	+ [Activity](appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-activity "appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-activity")
	+ [Lambda
	 function](appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-lambda "appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-lambda")
	+ [Service
	 integration](appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-service-integration "appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-service-integration")
	+ [Step Functions API](appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-api "appinsights-metrics-step-functions.md#appinsights-metrics-step-functions-api")
* [API Gateway REST API stages](appinsights-metrics-api-gateway.md "appinsights-metrics-api-gateway.md")
* [SAP HANA](appinsights-metrics-sap-hana.md "appinsights-metrics-sap-hana.md")
* [SAP ASE](appinsights-metrics-sap-ase.md "appinsights-metrics-sap-ase.md")
* [SAP ASE High Availability on Amazon EC2](appinsights-metrics-sap-ase-ha.md "appinsights-metrics-sap-ase-ha.md")
* [SAP NetWeaver](appinsights-metrics-sap-netweaver.md "appinsights-metrics-sap-netweaver.md")
* [HA Cluster](appinsights-metrics-ha-cluster.md "appinsights-metrics-ha-cluster.md")
* [Java](appinsights-metrics-java.md "appinsights-metrics-java.md")
* [Amazon Elastic Container Service (Amazon ECS)](appinsights-metrics-ecs.md "appinsights-metrics-ecs.md")


	+ [CloudWatch built-in
	 metrics](appinsights-metrics-ecs.md#appinsights-metrics-ecs-built-in-metrics "appinsights-metrics-ecs.md#appinsights-metrics-ecs-built-in-metrics")
	+ [Container
	 Insights metrics](appinsights-metrics-ecs.md#appinsights-metrics-ecs-container-insights-metrics "appinsights-metrics-ecs.md#appinsights-metrics-ecs-container-insights-metrics")
	+ [Container Insights Prometheus metrics](appinsights-metrics-ecs.md#appinsights-metrics-ecs-container-insights-prometheus "appinsights-metrics-ecs.md#appinsights-metrics-ecs-container-insights-prometheus")
* [Kubernetes on AWS](appinsights-metrics-kubernetes.md "appinsights-metrics-kubernetes.md")


	+ [Container Insights metrics](appinsights-metrics-kubernetes.md#appinsights-metrics-kubernetes-container-insights-metrics "appinsights-metrics-kubernetes.md#appinsights-metrics-kubernetes-container-insights-metrics")
	+ [Container Insights Prometheus metrics](appinsights-metrics-kubernetes.md#appinsights-metrics-kubernetes-container-insights-prometheus "appinsights-metrics-kubernetes.md#appinsights-metrics-kubernetes-container-insights-prometheus")
* [Amazon FSx](appinsights-metrics-fsx.md "appinsights-metrics-fsx.md")
* [Amazon VPC](appinsights-metrics-vpc.md "appinsights-metrics-vpc.md")
* [Amazon VPC NAT gateways](appinsights-metrics-nat-gateways.md "appinsights-metrics-nat-gateways.md")
* [Amazon Route 53 health check](appinsights-metrics-health-check.md "appinsights-metrics-health-check.md")
* [Amazon Route 53 hosted zone](appinsights-metrics-hosted-zone.md "appinsights-metrics-hosted-zone.md")
* [Amazon Route 53 Resolver endpoint](appinsights-metrics-resolver-endpoint.md "appinsights-metrics-resolver-endpoint.md")
* [AWS Network Firewall rule group](appinsights-metrics-firewall-rule-group.md "appinsights-metrics-firewall-rule-group.md")
* [AWS Network Firewall rule group association](appinsights-metrics-firewall-rule-group-assoc.md "appinsights-metrics-firewall-rule-group-assoc.md")
* [Metrics with data
 points requirements](appinsights-metrics-datapoint-requirements.md "appinsights-metrics-datapoint-requirements.md") 


	+ [AWS/ApplicationELB](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-app-elb "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-app-elb")
	+ [AWS/AutoScaling](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-autoscaling "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-autoscaling")
	+ [AWS/EC2](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-ec2 "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-ec2")
	+ [Elastic Block
	 Store (EBS)](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-ebs "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-ebs")
	+ [AWS/ELB](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-elb "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-elb")
	+ [AWS/RDS](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-rds "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-rds")
	+ [AWS/Lambda](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-lambda "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-lambda")
	+ [AWS/SQS](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-sqs "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-sqs")
	+ [AWS/CWAgent](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-cwagent "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-cwagent")
	+ [AWS/DynamoDB](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-dynamo "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-dynamo")
	+ [AWS/S3](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-s3 "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-s3")
	+ [AWS/States](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-states "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-states")
	+ [AWS/ApiGateway](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-api-gateway "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-api-gateway")
	+ [AWS/SNS](appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-sns "appinsights-metrics-datapoint-requirements.md#appinsights-metrics-datapoint-requirements-sns")
* [Recommended
 metrics](application-insights-recommended-metrics.md "application-insights-recommended-metrics.md")
* [Performance Counter
 metrics](application-insights-performance-counter.md "application-insights-performance-counter.md")
