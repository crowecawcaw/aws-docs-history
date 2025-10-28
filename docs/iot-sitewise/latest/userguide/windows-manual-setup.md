# Set up open source integrations manually

(Windows)

Use this guide to manually create a time series bucket for wind speed data that connects
with Grafana® and Node-RED®.

Manually install and configure Node-RED, InfluxDB®, and Grafana on
Microsoft Windows to control your deployment configuration. You can store and
manage time series data from your devices using InfluxDB.

## Manual setup prerequisites

Before you begin, complete these requirements:

###### Note

Run all services (SiteWise Edge, InfluxDB, Node-RED, and Grafana) on the same
host.

- Install an MQTT-enabled, V3 gateway. For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md").
- Install and run these services locally:
  - InfluxDB OSS v2. For installation steps, see [Install
    InfluxDB](https://docs.influxdata.com/influxdb/v2/install/ "https://docs.influxdata.com/influxdb/v2/install/").
  - Node-RED. For installation steps, see [Install Node-RED
    locally](https://nodered.org/docs/getting-started/local "https://nodered.org/docs/getting-started/local").
  - Grafana. For installation steps, see [Install
    Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/ "https://grafana.com/docs/grafana/latest/setup-grafana/installation/").
