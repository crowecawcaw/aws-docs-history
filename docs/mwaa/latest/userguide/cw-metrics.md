# Monitoring and metrics for Amazon Managed Workflows for Apache Airflow

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Managed Workflows for Apache Airflow and your AWS solution.
We recommend collecting monitoring data from all parts of your AWS solution so you can more easily debug a multi-point failure if one occurs.
This topic describes what resources AWS provides for monitoring your Amazon MWAA environment and responding to potential events.

###### Note

Apache Airflow metrics and logging are subject to standard [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For more information about monitoring Apache Airflow, refer to [Logging & Monitoring](https://airflow.apache.org/docs/apache-airflow/stable/logging-monitoring/index.html "https://airflow.apache.org/docs/apache-airflow/stable/logging-monitoring/index.html") in the Apache Airflow documentation website.

###### Sections

- [Monitoring overview on Amazon MWAA](monitoring-overview.md "monitoring-overview.md")
- [Accessing audit logs in AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md")
- [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md "monitoring-airflow.md")
- [Monitoring dashboards and alarms on Amazon MWAA](monitoring-dashboard.md "monitoring-dashboard.md")
- [Apache Airflow environment metrics in CloudWatch](access-metrics-cw.md "access-metrics-cw.md")
- [Container, queue, and database metrics for Amazon MWAA](accessing-metrics-cw-container-queue-db.md "accessing-metrics-cw-container-queue-db.md")
