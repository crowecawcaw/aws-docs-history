

# Monitoring and event management for EDI
<a name="eco-monitoring-mgmt"></a>

The ECO monitors your EDI resources, including Amazon EKS resources for failures, performance degradation, and security issues. 

As a managed account, ECO conﬁgures and deploys alarms for applicable EDI resources and Amazon Managed Service for Prometheus alert manager rules. ECO monitors these resources and performs incident management and remediation when needed. 

ECO also relies on internal tools, such as AMS Accelerate [Resource Tagger](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-tagger.html) and [Alarm Manager](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tag-alarms.html). ECO also uses native AWS services, such as AWS AppConfig, Amazon CloudWatch, Amazon EventBridge, Amazon GuardDuty, Amazon Macie, AWS Health, Amazon Managed Grafana and AWS Lambda.