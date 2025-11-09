# MIDAOPS03-BP02 Implement real-time monitoring and alerting capabilities

Establish comprehensive monitoring of your industrial data infrastructure with automated
alerts to quickly identify and respond to operational issues before they impact manufacturing
processes. Configure appropriate thresholds and notification channels to quickly alert the
right teams about system health, data quality, and performance anomalies.

**Desired outcome:** Your organization has established a clear,
quantifiable understanding of industrial data workload performance through well-defined
metrics and KPIs that align with business objectives and operational requirements.

**Benefits of establishing this best practice:** Monitoring and
alerting capabilities allow the manufacturing team to quickly identify issues or impending
problems that could impact production, quality, or maintenance.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Develop and implement a comprehensive metrics monitoring framework that captures both
technical and business aspects of your industrial data workload.

### Implementation steps

- Use AWS IoT Greengrass for device software to collect, process, and export data
  streams, including when devices are offline. It can act as an industrial data gateway
  between the shop floor and your AWS environment.
- For pre-built industrial connectors, implement the [AWS Shop Floor Connectivity (SFC)](https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/ "https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/") open-source solution either as a
  stand-alone application or as an AWS IoT Greengrass component. SFC is a data ingestion
  enabler that delivers customizable greenfield and brownfield connectivity solutions.
  It addresses limitations and unifies data collection from existing IoT data collection
  services, allowing customers to consistently collect data from equipment across
  different vendors for use with various AWS services.
- Consider AWS IoT SiteWise to collect data from disparate data sources using OPCUA
  and MQTT connectors. AWS IoT SiteWise Monitor provides near real-time dashboard
  visualization of your key metrics and can be configured for alerting workflows.
- Use Amazon Managed Grafana to deliver integrated live dashboards for monitoring
  your production KPIs, operations, machine status, and alerts. The dashboards can use
  Grafana's native data source connectors to visualize data from multiple AWS services,
  including AWS IoT SiteWise, Amazon Timestream, Amazon RDS, and Amazon Aurora. This
  provides a unified visualization layer for your industrial data, enabling real-time
  monitoring and analysis of your manufacturing operations.
- Configure custom Amazon CloudWatch dashboards and alarms to track critical
  metrics, such as data ingestion rates and latency resource utilization (like CPU,
  memory, and storage) for edge gateways and cloud services, anomalies or deviations in
  key operational KPIs, security events and access patterns*.*

## Key AWS services

- Amazon CloudWatch
- Amazon Managed Grafana
- AWS IoT Greengrass
- AWS IoT SiteWise

## Resources

**Related documents:**

- [Collecting data from industrial devices to AWS Services](https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/ "https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/")
