

# Monitoring and incident management for Amazon EKS in AMS Accelerate
<a name="acc-mon-inc-mgmt-eks"></a>

Monitoring and Incident Management for Amazon EKS monitors your Amazon EKS resources for failures, performance degradation, and security issues. AMS Accelerate configures and deploys Amazon Managed Service for Prometheus alert manager rules, monitors the alerts, and then performs incident management when these alerts are triggered. Monitoring and incident management for Amazon EKS relies on AMS Alarm Manager and leverages native AWS services, such as [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html), [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html). 

**Important**  
Monitoring and incident management for Amazon EKS doesn't support the Asia Pacific (Malaysia) Region, AWS GovCloud (US), Windows nodes, or Windows containers.