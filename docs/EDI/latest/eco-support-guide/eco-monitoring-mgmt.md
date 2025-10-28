# Monitoring and event management for EDI

The ECO monitors your EDI resources, including Amazon EKS resources for failures, performance degradation, and security issues.

As a managed account, ECO conﬁgures and deploys alarms for applicable EDI resources and Amazon Managed Service for Prometheus alert manager rules. ECO
monitors these resources and performs incident management and remediation when needed.

ECO also relies on internal tools, such as AMS Accelerate
[Resource Tagger](../../../managedservices/latest/accelerate-guide/acc-resource-tagger.md "../../../managedservices/latest/accelerate-guide/acc-resource-tagger.md") and
[Alarm Manager](../../../managedservices/latest/accelerate-guide/acc-mem-tag-alarms.md "../../../managedservices/latest/accelerate-guide/acc-mem-tag-alarms.md"). ECO also uses native AWS services, such as
AWS AppConfig, Amazon CloudWatch, Amazon EventBridge, Amazon GuardDuty, Amazon Macie, AWS Health, Amazon Managed Grafana and AWS Lambda.
