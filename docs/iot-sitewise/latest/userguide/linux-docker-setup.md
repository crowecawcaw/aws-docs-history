# Set up open-source integrations with Docker

(Linux)

For a streamlined deployment process, you can use Docker to set up Node-RED®,
InfluxDB®, and Grafana® on a Linux environment. This method uses pre-configured
containers, allowing for rapid deployment and easier management of the components.

## Docker setup prerequisites

Before you begin, verify that have the following:

- An MQTT-enabled, V3 gateway. For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md").
- The Docker Compose plugin. For installation steps, see [Install the Docker
  Compose plugin](https://docs.docker.com/compose/install/linux/ "https://docs.docker.com/compose/install/linux/") in the _Docker_ Manuals
  documentation.

## Deploy the services

This deployment runs SiteWise Edge, InfluxDB, Node-RED, and Grafana on the same
host.

### Set up the environment

1. Gain root access:

```
sudo -i
```

2. Create a .env file or export these environment variables:

```
export INFLUXDB_PASSWORD=`your-secure-influxdb-password`
export INFLUXDB_TOKEN=`your-secure-influxdb-token`
export GRAFANA_PASSWORD=`your-secure-grafana-password`
```

### Configure the Docker network

- Create a bridge network using the name
  `SiteWiseEdgeNodeRedDemoNetwork`.

```
docker network create --driver=bridge SiteWiseEdgeNodeRedDemoNetwork
```

### Prepare the Docker Compose

file

Copy the contents of the following YAML file to your SiteWise Edge gateway device.

```
services:
  influxdb:
    image: influxdb:latest
    container_name: influxdb
    ports:
      - "127.0.0.1:8086:8086"
    volumes:
      - influxdb-storage:/.influxdbv2
    environment:
      - DOCKER_INFLUXDB_INIT_MODE=setup
      - DOCKER_INFLUXDB_INIT_USERNAME=admin
      - DOCKER_INFLUXDB_INIT_PASSWORD=${INFLUXDB_PASSWORD}
      - DOCKER_INFLUXDB_INIT_ORG=iot-sitewise-edge
      - DOCKER_INFLUXDB_INIT_BUCKET=WindFarmData
      - DOCKER_INFLUXDB_INIT_RETENTION=0
      - DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=${INFLUXDB_TOKEN}
    networks:
      - SiteWiseEdgeNodeRedDemoNetwork
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "127.0.0.1:3000:3000"
    volumes:
      - grafana-storage:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
      - GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource
      - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
      - GF_PATHS_CONFIG=/etc/grafana/grafana.ini
      - GF_LOG_LEVEL=info
    configs:
      - source: grafana_datasource
        target: /etc/grafana/provisioning/datasources/influxdb.yaml
      - source: grafana_preload_dashboard_config
        target: /etc/grafana/provisioning/dashboards/dashboard.yml
      - source: grafana_preload_dashboard
        target: /etc/grafana/provisioning/dashboards/demo_dashboard.json
    depends_on:
      - influxdb
    networks:
      - SiteWiseEdgeNodeRedDemoNetwork
    restart: unless-stopped

  nodered:
    build:
      context: .
      dockerfile_inline: |
        FROM nodered/node-red:latest
        RUN npm install node-red-contrib-influxdb
    container_name: nodered
    ports:
      - "127.0.0.1:1880:1880"
    volumes:
      - node_red_data:/data
    environment:
      - NODE_RED_ENABLE_SAFE_MODE=false
      - NODE_RED_ENABLE_PALETTE_EDIT=true
      - NODE_RED_AUTO_INSTALL_MODULES=true
    configs:
      - source: nodered_flows
        target: /data/flows.json
      - source: nodered_settings
        target: /data/settings.js
      - source: nodered_flows_cred
        target: /data/flows_cred.json
    depends_on:
      - influxdb
    networks:
      - SiteWiseEdgeNodeRedDemoNetwork
    restart: unless-stopped

volumes:
  influxdb-storage:
  grafana-storage:
  node_red_data:

networks:
  SiteWiseEdgeNodeRedDemoNetwork:
    external: true

configs:
  grafana_datasource:
    content: |
      apiVersion: 1
      datasources:
        - name: windfarm-demo
          type: influxdb
          access: proxy
          url: http://influxdb:8086
          jsonData:
            version: Flux
            organization: iot-sitewise-edge
            defaultBucket: WindFarmData
            tlsSkipVerify: true
          secureJsonData:
            token: ${INFLUXDB_TOKEN}
          editable: false

  grafana_preload_dashboard_config:
    content: |
      apiVersion: 1
      providers:
        - name: "Dashboard provider"
          orgId: 1
          type: file
          options:
            path: /etc/grafana/provisioning/dashboards

  grafana_preload_dashboard:
    content: |
      {
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
        "id": 1,
        "links": [],
        "panels": [
          {
            "datasource": {
              "type": "influxdb",
              "uid": "PEB0DCBF338B3CEB2"
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
            "pluginVersion": "11.6.0",
            "targets": [
              {
                "datasource": {
                  "type": "influxdb",
                  "uid": "PEB0DCBF338B3CEB2"
                },
                "query": "from(bucket: \"WindFarmData\")\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n  |> filter(fn: (r) => r[\"_measurement\"] == \"TurbineData\")\n  |> filter(fn: (r) => r[\"_field\"] == \"value\")\n  |> filter(fn: (r) => r[\"name\"] == \"/Renton/WindFarm/Turbine/WindSpeed\")\n  |> filter(fn: (r) => r[\"quality\"] == \"GOOD\")\n  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\n  |> yield(name: \"mean\")",
                "refId": "A"
              }
            ],
            "title": "Wind Speed",
            "type": "timeseries"
          }
        ],
        "preload": false,
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
        "title": "Demo Dashboard",
        "uid": "eejtureqjo9a8c",
        "version": 2
      }

  nodered_flows:
    content: |
      [
        {
          "id": "95fce448fdd43b47",
          "type": "tab",
          "label": "Demo Flow",
          "disabled": false,
          "info": ""
        },
        {
          "id": "5f63740b66af3386",
          "type": "mqtt out",
          "z": "95fce448fdd43b47",
          "name": "Publish to MQTT broker",
          "topic": "/Renton/WindFarm/Turbine/WindSpeed",
          "qos": "1",
          "retain": "",
          "respTopic": "",
          "contentType": "",
          "userProps": "",
          "correl": "",
          "expiry": "",
          "broker": "5744207557fa19be",
          "x": 830,
          "y": 200,
          "wires": []
        },
        {
          "id": "8f2eb590d596679b",
          "type": "function",
          "z": "95fce448fdd43b47",
          "name": "Translate to SiteWise payload",
          "func": "let input = msg.payload;\nlet output = {};\n\noutput[\"propertyAlias\"] = input.name;\n\nlet propertyVal = {}\n\nlet timeInSeconds = Math.floor(input.timestamp / 1000);\nlet offsetInNanos = (input.timestamp % 1000) * 1000000;\n\npropertyVal[\"timestamp\"] = {\n    \"timeInSeconds\": timeInSeconds,\n    \"offsetInNanos\": offsetInNanos,\n};\n\npropertyVal[\"quality\"] = input.quality\n\nlet typeNameConverter = {\n    \"number\": (x) => Number.isInteger(x) ? \"integerValue\" : \"doubleValue\",\n    \"boolean\": (x) => \"booleanValue\",\n    \"string\": (x) => \"stringValue\", \n}\nlet typeName = typeNameConverter[typeof input.value](input.value)\npropertyVal[\"value\"] = {}\npropertyVal[\"value\"][typeName] = input.value;\n\noutput[\"propertyValues\"] = [propertyVal]\n\nreturn {\n    payload: JSON.stringify(output)\n};",
          "outputs": 1,
          "timeout": "",
          "noerr": 0,
          "initialize": "",
          "finalize": "",
          "libs": [],
          "x": 530,
          "y": 200,
          "wires": [
            [
              "5f63740b66af3386"
            ]
          ]
        },
        {
          "id": "4b78cbdea5e3258c",
          "type": "inject",
          "z": "95fce448fdd43b47",
          "name": "Turbine Simulator",
          "props": [
            {
              "p": "payload.timestamp",
              "v": "",
              "vt": "date"
            },
            {
              "p": "payload.quality",
              "v": "GOOD",
              "vt": "str"
            },
            {
              "p": "payload.value",
              "v": "$$random()",
              "vt": "jsonata"
            },
            {
              "p": "payload.name",
              "v": "/Renton/WindFarm/Turbine/WindSpeed",
              "vt": "str"
            }
          ],
          "repeat": "1",
          "crontab": "",
          "once": false,
          "onceDelay": "",
          "topic": "",
          "x": 270,
          "y": 200,
          "wires": [
            [
              "8f2eb590d596679b"
            ]
          ]
        },
        {
          "id": "b658bf337ea2e316",
          "type": "influxdb out",
          "z": "95fce448fdd43b47",
          "influxdb": "2f1c38495035d2e4",
          "name": "Store data in InfluxDB",
          "measurement": "TurbineData",
          "precision": "",
          "retentionPolicy": "",
          "database": "",
          "retentionPolicyV18Flux": "",
          "org": "iot-sitewise-edge",
          "bucket": "WindFarmData",
          "x": 840,
          "y": 340,
          "wires": []
        },
        {
          "id": "9432d39af35b202f",
          "type": "function",
          "z": "95fce448fdd43b47",
          "name": "Translate to InfluxDB payload",
          "func": "let data = msg.payload;\n\nlet timeInSeconds = data.propertyValues[0].timestamp.timeInSeconds;\nlet offsetInNanos = data.propertyValues[0].timestamp.offsetInNanos;\nlet timestampInMilliseconds = (timeInSeconds * 1000) + (offsetInNanos / 1000000);\n\nmsg.payload = [\n    {\n        \"timestamp(milliseconds_since_epoch)\": timestampInMilliseconds,\n        \"value\": data.propertyValues[0].value.doubleValue\n    },\n    {\n        \"name\": data.propertyAlias,\n        \"quality\": data.propertyValues[0].quality\n    }\n]\n\nreturn msg",
          "outputs": 1,
          "timeout": "",
          "noerr": 0,
          "initialize": "",
          "finalize": "",
          "libs": [],
          "x": 560,
          "y": 340,
          "wires": [
            [
              "b658bf337ea2e316"
            ]
          ]
        },
        {
          "id": "b689403d2c80816b",
          "type": "mqtt in",
          "z": "95fce448fdd43b47",
          "name": "Subscribe to MQTT broker",
          "topic": "/Renton/WindFarm/Turbine/WindSpeed",
          "qos": "1",
          "datatype": "auto-detect",
          "broker": "5744207557fa19be",
          "nl": false,
          "rap": true,
          "rh": 0,
          "inputs": 0,
          "x": 290,
          "y": 340,
          "wires": [
            [
              "9432d39af35b202f"
            ]
          ]
        },
        {
          "id": "4f59bed8e829fc35",
          "type": "comment",
          "z": "95fce448fdd43b47",
          "name": "Data Publish Flow",
          "info": "dfgh",
          "x": 270,
          "y": 160,
          "wires": []
        },
        {
          "id": "b218c7fc58c8b6e7",
          "type": "comment",
          "z": "95fce448fdd43b47",
          "name": "Data Retention flow",
          "info": "",
          "x": 270,
          "y": 300,
          "wires": []
        },
        {
          "id": "5744207557fa19be",
          "type": "mqtt-broker",
          "name": "emqx",
          "broker": "emqx",
          "port": "1883",
          "clientid": "",
          "autoConnect": true,
          "usetls": false,
          "protocolVersion": "5",
          "keepalive": 15,
          "cleansession": true,
          "autoUnsubscribe": true,
          "birthTopic": "",
          "birthQos": "0",
          "birthPayload": "",
          "birthMsg": {},
          "closeTopic": "",
          "closePayload": "",
          "closeMsg": {},
          "willTopic": "",
          "willQos": "0",
          "willPayload": "",
          "willMsg": {},
          "userProps": "",
          "sessionExpiry": ""
        },
        {
          "id": "2f1c38495035d2e4",
          "type": "influxdb",
          "hostname": "influxdb",
          "port": 8086,
          "protocol": "http",
          "database": "",
          "name": "InfluxDB",
          "usetls": false,
          "tls": "",
          "influxdbVersion": "2.0",
          "url": "http://influxdb:8086",
          "timeout": "",
          "rejectUnauthorized": false
        }
      ]

  nodered_flows_cred:
    content: |
      {
        "2f1c38495035d2e4": {
          "token": "${INFLUXDB_TOKEN}"
        }
      }

  nodered_settings:
    content: |
      module.exports = {
        flowFile: 'flows.json',
        credentialSecret: false,
        adminAuth: null,
        editorTheme: {
          projects: {
            enabled: false
          }
        }
      }
```

### Update the SiteWise Edge deployment

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/")
2. Choose **Greengrass devices** in the left navigation menu
   under the **Manage** section, then **Core
   devices**.
3. Select the core device connected to your SiteWise Edge Gateway.
4. Choose the **Deployments** tab, then select the
   **Deployment ID** value.
5. Choose **Actions**, then select **Revise**.
6. Read the pop up message and then choose **Revise
   Deployment**.
7. In **Step 2 - Select components**, select the following
   components and then choose **Next**.
   - `aws.greengrass.clientdevices.mqtt.EMQX`
   - `aws.iot.SiteWiseEdgePublisher`

8. In **Step 3 - Configure components**, select the
   `aws.greengrass.clientdevices.mqtt.EMQX` component value and add the
   following network configuration:

```
{
    "emqxConfig": {
        "authorization": {
            "no_match": "allow"
        },
        "listeners": {
            "tcp": {
                "default": {
                    "enabled": true,
                    "enable_authn": false
                }
            }
        }
    },
    "authMode": "bypass",
    "dockerOptions": "-p 127.0.0.1:1883:1883 --network=SiteWiseEdgeNodeRedDemoNetwork",
    "requiresPrivilege": "true"
}
```

9. Choose **Next**.
10. In **Step 4 - Configure advanced settings**, choose
    **Next**.
11. Choose **Deploy**

### Launch the services

1. Start the services using the Docker Compose file. Run the following command under
   the directory containing the `compose.yaml` file.

```
docker compose up -d
```

2. Create an SSH tunnel to access the services:

```
ssh -i `path_to_your_ssh_key` -L 1880:127.0.0.1:1880 -L 3000:127.0.0.1:3000 -L 8086:127.0.0.1:8086 `username`@`gateway_ip_address`
```

This deployment creates the following services in the
`SiteWiseEdgeNodeRedDemoNetwork network`:

**InfluxDB v2 (port 8086)**

Includes pre-configured organization (iot-sitewise-edge), WindFarmData
InfluxDB bucket, and admin credentials

**Node-RED (port 1880)**

Includes InfluxDB nodes and pre-configured flows for AWS IoT SiteWise integration

**Grafana (port 3000)**

Includes admin user, InfluxDB datasource, and monitoring dashboard

### Access the services

After deployment, access the services using the following URLs and credentials:

###### Note

You can access each service from your host or the gateway machine.

| Service access details | Service                                                                | URL                                             | Credentials |
| ---------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- | ----------- |
| Node-RED               | [http://127.0.0.1:1880](http://127.0.0.1:1880 "http://127.0.0.1:1880") | No credentials required                         |
| InfluxDB               | [http://127.0.0.1:8086](http://127.0.0.1:8086 "http://127.0.0.1:8086") | Username: admin<br>Password: $INFLUXDB_PASSWORD |
| Grafana                | [http://127.0.0.1:3000](http://127.0.0.1:3000 "http://127.0.0.1:3000") | Username: admin<br>Password: $GRAFANA_PASSWORD  |

## Verify the deployment

To ensure your deployment is successful, perform the following checks:

1. For Node-RED, verify the presence of two preloaded flows:
   - Data publish flow
   - Data retention flow

2. For AWS IoT SiteWise, in the AWS IoT SiteWise console, confirm the presence of a data stream with the
   alias `/Renton/WindFarm/Turbine/WindSpeed`.
3. For InfluxDB, use the Data Explorer to verify data storage in the
   `TurbineData` measurement within the `WindFarmData`
   bucket.
4. For Grafana, view the dashboard to confirm the display of time series data
   generated from Node-RED.
