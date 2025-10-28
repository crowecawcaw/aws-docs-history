# Monitoring and incident management for Amazon EKS in AMS Accelerate

Monitoring and Incident Management for Amazon EKS monitors your Amazon EKS resources for failures, performance degradation, and security issues. AMS Accelerate configures and
deploys Amazon Managed Service for Prometheus alert manager rules, monitors the alerts, and then performs incident management when these alerts are triggered.
Monitoring and incident management for Amazon EKS relies on AMS Alarm Manager and leverages native AWS services, such as
[Amazon Managed Service for Prometheus](../../../grafana/latest/userguide/prometheus-data-source.md "../../../grafana/latest/userguide/prometheus-data-source.md"),
[Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md"),
[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md"),
[AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md"), and
[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

###### Important

Monitoring and incident management for Amazon EKS doesn't support the Asia Pacific (Malaysia) Region, AWS GovCloud (US), Windows
nodes, or Windows containers.
