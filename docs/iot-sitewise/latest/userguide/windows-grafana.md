# Set up Grafana for SiteWise Edge

Grafana® lets you create local real-time monitoring dashboards for your industrial
data. By visualizing the data stored in InfluxDB®, you can provide operators with
immediate insights into equipment performance, process efficiency, and potential issues.
This visibility at the edge is important for time-sensitive operations and maintaining
continuity during network disruptions.

## Configure the data source

Connecting Grafana to your InfluxDB database creates a powerful visualization
layer for your industrial data. This connection enables real-time monitoring dashboards
that operators can use to make informed decisions without cloud dependencies.

1. Access your Grafana instance locally by navigating to [http://127.0.0.1:3000](http://127.0.0.1:3000 "http://127.0.0.1:3000") in your browser. If
   enabling TLS is required, you can refer to [Set up
   Grafana HTTPS for secure web traffic](https://grafana.com/docs/grafana/latest/setup-grafana/set-up-https/ "https://grafana.com/docs/grafana/latest/setup-grafana/set-up-https/") in the _Grafana Labs Documentation_.
2. Add an InfluxDB data source pointing to the InfluxDB time series bucket where
   Node-RED writes data. For example, `WindFarmData`. This connection
   establishes the link between your stored data and the visualization platform.
3. For detailed instructions, see [Configure the InfluxDB data source](https://grafana.com/docs/grafana/latest/datasources/influxdb/configure-influxdb-data-source/ "https://grafana.com/docs/grafana/latest/datasources/influxdb/configure-influxdb-data-source/") in the _Grafana Labs Documentation_.

### Create a Grafana dashboard for

SiteWise Edge data

Creating a dashboard is the final step in building your local monitoring solution.
Dashboards provide visual representations of your industrial data, making it easier to
identify trends, anomalies, and potential issues at a glance.

- Follow the guide to create a dashboard. For more information, see [Build your first dashboard](https://grafana.com/docs/grafana/latest/getting-started/build-first-dashboard/ "https://grafana.com/docs/grafana/latest/getting-started/build-first-dashboard/") in the _Grafana Labs Documentation_. This template assumes
  your bucket is named `WindFarmData` and measurement is
  `TurbineData`.

You can also use the quick start guide by importing the provided example
dashboard template to quickly create a dashboard with a time series plot for the
data that Node-RED generates in previous section. This template provides a starting
point that you can customize to meet your specific monitoring needs.

```
{
  "__inputs": [
    {
      "name": "DS_WINDFARM-DEMO",
      "label": "windfarm-demo",
      "description": "",
      "type": "datasource",
      "pluginId": "influxdb",
      "pluginName": "InfluxDB"
    }
  ],
  "__elements": {},
  "__requires": [
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "11.6.0-pre"
    },
    {
      "type": "datasource",
      "id": "influxdb",
      "name": "InfluxDB",
      "version": "1.0.0"
    },
    {
      "type": "panel",
      "id": "timeseries",
      "name": "Time series",
      "version": ""
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": null,
  "links": [],
  "panels": [
    {
      "datasource": {
        "type": "influxdb",
        "uid": "${DS_WINDFARM-DEMO}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.6.0-pre",
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_WINDFARM-DEMO}"
          },
          "query": "from(bucket: \"`WindFarmData`\")\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n  |> filter(fn: (r) => r[\"_measurement\"] == \"`TurbineData`\")\n  |> filter(fn: (r) => r[\"_field\"] == \"value\")\n  |> filter(fn: (r) => r[\"name\"] == \"/Renton/WindFarm/Turbine/WindSpeed\")\n  |> filter(fn: (r) => r[\"quality\"] == \"GOOD\")\n  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\n  |> yield(name: \"mean\")",
          "refId": "A"
        }
      ],
      "title": "Panel Title",
      "type": "timeseries"
    }
  ],
  "schemaVersion": 41,
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "browser",
  "title": "demo dashboard",
  "uid": "fejc0t08o6d4wb",
  "version": 1,
  "weekStart": ""
}
```
