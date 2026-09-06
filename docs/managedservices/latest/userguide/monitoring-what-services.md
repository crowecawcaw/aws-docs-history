

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# What does the AMS monitoring system monitor?
<a name="monitoring-what-services"></a>

In keeping with the AWS Managed Services (AMS) shared services responsibility model, the AMS monitoring system monitors your AWS infrastructure. For details on baseline monitoring in AMS, including AWS resources monitored and the type of alerts for each resource, see [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md). For Amazon EC2 instances, AMS monitors the operating system and provides baseline monitoring based on OS metrics such as CPU utilization and root volume usage. 

We recommend supplementing AMS monitoring with additional monitoring using AWS services tailored to your application. For guidance on monitoring for availability see the "Monitoring and Alarming" section in this whitepaper [Reliability Pillar](https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf). You can configure your own monitoring to suit your operational needs; how to do this is discussed in [Creating additional CloudWatch alarms in AMS](custom-cloudwatch-alarms.md) and [Creating custom CloudWatch metrics and alarms in AMS](custom-cloudwatch-events.md).