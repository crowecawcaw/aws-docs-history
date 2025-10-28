# Process and visualize data with SiteWise Edge and

open-source tools

Configure AWS IoT SiteWise Edge MQTT-enabled gateways with open-source tools for local processing and
visualization to enhance your industrial data management capabilities.

With SiteWise Edge, you can create a local data processing pipeline using external, open-source
tools. Use [Node-RED®](https://nodered.org/ "https://nodered.org/") to store time-series data
with [InfluxDB®](https://www.influxdata.com/lp/influxdb-database/ "https://www.influxdata.com/lp/influxdb-database/"), and
monitor operations through [Grafana®](https://grafana.com/ "https://grafana.com/")
dashboards.

Node-RED processes and transforms your data flows, while InfluxDB provides time-series
data storage. Grafana displays your real-time operational data. Use these tools with SiteWise Edge
to synchronize data between your local environment and the AWS Cloud, giving you both
immediate local insights and long-term cloud-based analytics capabilities.

###### Note

Node-RED®, InfluxDB®, and Grafana® are not vendors or suppliers for SiteWise Edge.

![A diagram that shows a few data sources and the turbine simulator connecting to the EMQX Broker to publish. Then the EMQX broker subscribes to the AWS IoT SiteWise Gateway and Node-RED. Node-RED feeds into InfluxDB, and then Influx DB into the Grafana Dashboard.](images/gateway-open-source-overview.png)

###### Note

In this guide, we're using the open-source version of [Grafana](https://grafana.com/ "https://grafana.com/") for SiteWise Edge as opposed to the [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md")
service.

## Deployment options

You can deploy this solution using one of two approaches. With a Microsoft
Windows manual setup, you control component configuration and integration with your
infrastructure. With Linux, you can use Docker to deploy pre-configured
components in containers.

Choose the method that meets your operational requirements.

- [Set up open source integrations manually
  (Windows)](windows-manual-setup.md "windows-manual-setup.md") –
  For custom configurations or existing infrastructure
- [Set up open-source integrations with Docker
  (Linux)](linux-docker-setup.md "linux-docker-setup.md") – For
  rapid deployment with pre-configured components

## Wind farm example overview

This guide uses a wind farm example to demonstrate how you can monitor wind speed for a
turbine on a wind farm. This practical scenario illustrates common industrial monitoring needs
where both local and cloud-based visibility are valuable for operational efficiency.

With this integration, you can:

- Collect data from industrial equipment using an AWS IoT SiteWise Edge gateway
- Process data locally with Node-RED, InfluxDB, and Grafana
- Store data locally using InfluxDB
- Monitor data in real time using Grafana dashboards

Throughout this guide, we use the example of a windfarm. We use Node-RED to simulate a
turbine that generates wind speed data. Node-RED translates the data payload, publishes the
data to the SiteWise Edge MQTT broker, subscribes to receive data from the broker, and stores the
data locally in InfluxDB. This approach ensures that all of the operational data is
available both locally for immediate access and in the cloud for further analytics. By
implementing this pattern, you gain resilience against network disruptions while maintaining
the ability to perform advanced analytics in the AWS Cloud. Grafana connects to InfluxDB
for local monitoring, providing operators with real-time visibility into metrics without cloud
dependencies. A SiteWise Edge MQTT-enabled gateway connects to the same MQTT broker to send data to
AWS IoT SiteWise, creating a bridge between your edge operations and cloud-based services.

You can use your own data and configurations to create a similar workflow tailored to your
specific industrial requirements, whether you're monitoring manufacturing equipment, utility
infrastructure, or other industrial assets.

## Requirements for open-source integrations

Before implementing open-source integrations with SiteWise Edge, ensure your environment meets
the necessary requirements.

- **Hardware requirements** - Your gateway hardware must
  meet the requirements for SiteWise Edge gateways. For more information, see [AWS IoT SiteWise Edge self-hosted gateway
  requirements](configure-gateway-ggv2.md "configure-gateway-ggv2.md") for
  MQTT-enabled, V3 gateways and [Requirements for the AWS IoT SiteWise Edge
  application](siemens-app-gateway-requirements.md "siemens-app-gateway-requirements.md").

###### Important

When deploying additional open-source components, ensure your hardware meets the
requirements for [InfluxDB](https://docs.influxdata.com/influxdb/v2/install/ "https://docs.influxdata.com/influxdb/v2/install/"), [Node-RED](https://nodered.org/docs/getting-started/ "https://nodered.org/docs/getting-started/"), and [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/ "https://grafana.com/docs/grafana/latest/setup-grafana/installation/").

- Your network configuration must support both local communication between components
  and cloud connectivity for SiteWise Edge.
- All services must run on the same host.

## Security considerations

We recommend that you encrypt all communications between components, especially when
accessing interfaces from non-local networks. Implement proper access controls for each
component and follow AWS best practices for AWS IoT SiteWise Edge gateway configuration and AWS
account security.

**Development environment**

This guide demonstrates Node-RED, InfluxDB, and Grafana running and accessed
locally on a gateway host. For production deployments that require external access,
implement security measures including TLS encryption, authentication, and authorization.
Follow each application's security best practices.

**Third-party software**

This solution uses third-party software not maintained by AWS, including
InfluxDB, Node-RED, Grafana, and the `node-red-contrib-influxdb` plugin.
Before deployment, ensure these components comply with your organization's security
requirements, compliance standards, and governance policies.

###### Important

This guide references and uses third-party software not owned or maintained by AWS.
Before implementation, ensure that all components meet your security, compliance, and
governance requirements. Keep all software updated with the latest security patches and
follow best practices for securing your edge deployment.

InfluxDB, Node-RED, Grafana are not vendors or suppliers for SiteWise Edge.

## Other considerations

Consider these additional factors when implementing open-source integrations with
SiteWise Edge.

- Use the latest versions of all services, tools, and components.
- Filter and aggregate data locally before cloud transmission to reduce AWS IoT SiteWise data
  ingestion costs. Configure appropriate data retention periods in InfluxDB and properly
  size your gateway hardware. For more information, see [AWS IoT SiteWise pricing](https://aws.amazon.com/iot-sitewise/pricing/ "https://aws.amazon.com/iot-sitewise/pricing/").
- Implement regular backup procedures for all data.
- Monitor resource usage on your gateway and configure appropriate resource limits for
  each component. Implement data retention policies in InfluxDB to manage disk
  usage.

## Troubleshooting open-source integrations

For more information on troubleshooting topics related to open source integrations for
SiteWise Edge gateways, see [Troubleshooting open-source integrations at the Edge](troubleshooting-gateway.md#open-source-troubleshooting "troubleshooting-gateway.md#open-source-troubleshooting").
