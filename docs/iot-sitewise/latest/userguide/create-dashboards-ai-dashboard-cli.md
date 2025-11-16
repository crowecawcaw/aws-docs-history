# Create dashboards with AWS CLI

###### Note

The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](../appguide/iotsitewise-monitor-availability-change.md "../appguide/iotsitewise-monitor-availability-change.md").

When you define visualizations (or widgets) in dashboards using the AWS CLI, you must
specify the following information in the `dashboardDefinition` JSON document. This
definition is a parameter of the [CreateDashboard](../APIReference/API_CreateDashboard.md "../APIReference/API_CreateDashboard.md") and [UpdateDashboard](../APIReference/API_UpdateDashboard.md "../APIReference/API_UpdateDashboard.md") operations.

`displaySettings`

The display settings with the following parameters:

- `numRows` – Number of rows in the dashboard layout. Each row is **cellSize** wide.
- `numColumbs` – Number of columns in the dashboard layout. Each column is **cellSize** wide.
- `cellSize` – (Optional) The size of a cell in the layout in pixels. It must be a positive number. Default is 10.
- `significantDigits` – (Optional) Number of significan digits to display in the dashboard. Default is 4.

`querySettings`

The query information with the following parameter:

- `refreshRate` – (Optional) The rate at which data refreshes in milliseconds. Accepts the following values - 1000, 5000, 10000, 60000, 300000.

`defaultViewport`

If not supplied, defaults to the last five minutes. Contains the following parameters:

- `duration` – (Optional) Determines how far into the past to query data starting from the present time.
- `start` – (Optional) It is of type Date. The start time range to query data. Needs an `end` date specified.
- `end` – (Optional) It is of type Date. The end time range to query data. Needs an `start` date specified.

`widgets`

A list of widget definition structures that contain the following
information:

`type`

The type of widget. AWS IoT SiteWise provides the following widget types:

- `xy-plot` – A line chart or a scatter plot depending on the configuration.
- `bar-chart` – A bar chart.
- `kpi-chart` – A key performance indicator chart.
- `status-timeline` – A status widget that visualizes and navigates
  time series data from one or more data sources.
- `text` – A text widget.
- `table` – A table widget.

`id`

An unique identifier for the widget.

`x`

The horizontal position of the widget, starting from the left of the dashboard.
This value refers to the widget's position in the dashboard's grid.

`y`

The vertical position of the widget, starting from the top of the dashboard. This
value refers to the widget's position in the dashboard's grid.

`z`

The relative ordering of the widgets. A larger Z value widget is displayed in front of the lower Z value
widget, if they overlap.

`width`

The width of the widget, expressed in number of cells on the dashboard.

`height`

The height of the widget, expressed in number of cells on the dashboard.

`properties`

A list of properties of the widget. It varies by the type of widget.
See [IoT App Kit](https://awslabs.github.io/iot-app-kit/?path=/docs/components-statustimeline--docs "https://awslabs.github.io/iot-app-kit/?path=/docs/components-statustimeline--docs") for details.

###### Example dashboard definition

The following example defines a dashboard from a payload stored in a JSON file.

```
aws iotsitewise create-dashboard \
  --project-id a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE \
  --dashboard-name "Example Dashboard" \
  --dashboard-definition file://dashboard-definition.json
```

The following JSON example for `dashboard-definition.json` defines dashboard
with the following visualization widgets:

```

{
    "displaySettings": {
        "numColumns": 200,
        "numRows": 1000,
        "cellSize": 20,
        "significantDigits": 4
    },
    "widgets": [{
        "id": "Ot73JcxUoc6oEXAMPLE",
        "type": "xy-plot",
        "width": 33,
        "height": 20,
        "x": 0,
        "y": 0,
        "z": 0,
        "properties": {
            "aggregationType": "AVERAGE",
            "queryConfig": {
                "source": "iotsitewise",
                "query": {
                    "assets": [{
                        "assetId": "97c97abf-e883-47bb-a3f4-EXAMPLE",
                        "properties": [{
                            "propertyId": "97cc61f4-57a4-4c5f-a82c-EXAMPLE",
                            "refId": "692ce941-f3d9-4074-a297-EXAMPLE",
                            "aggregationType": "AVERAGE",
                            "color": "#7d2105",
                            "resolution": "1m"
                        }]
                    }],
                    "properties": [],
                    "assetModels": [],
                    "alarms": [],
                    "alarmModels": []
                }
            },
            "line": {
                "connectionStyle": "linear",
                "style": "solid"
            },
            "symbol": {
                "style": "filled-circle"
            },
            "axis": {
                "yVisible": true,
                "xVisible": true
            },
            "legend": {
                "visible": true,
                "position": "right",
                "width": "30%",
                "height": "30%",
                "visibleContent": {
                    "unit": true,
                    "asset": true,
                    "latestValue": true,
                    "latestAlarmStateValue": true,
                    "maxValue": false,
                    "minValue": false
                }
            }
        }
    }, {
        "id": "fto7rF40Ny1EXAMPLE-G",
        "type": "bar-chart",
        "width": 33,
        "height": 20,
        "x": 0,
        "y": 20,
        "z": 0,
        "properties": {
            "aggregationType": "AVERAGE",
            "queryConfig": {
                "source": "iotsitewise",
                "query": {
                    "assets": [{
                        "assetId": "97c97abf-e883-47bb-a3f4-EXAMPLE",
                        "properties": [{
                            "propertyId": "c84ca8f3-3dea-478a-afec-EXAMPLE",
                            "aggregationType": "AVERAGE",
                            "refId": "2960b958-2034-4d6e-bcc2-EXAMPLE"
                        }]
                    }],
                    "properties": [],
                    "assetModels": [],
                    "alarms": [],
                    "alarmModels": [],
                    "requestSettings": {
                        "aggregation": "AVERAGE"
                    }
                }
            },
            "axis": {
                "showX": true,
                "showY": true
            },
            "styleSettings": {
                "2960b958-2034-4d6e-bcc2-360f1f02e505": {
                    "color": "#7d2105"
                }
            }
        }
    }],
    "querySettings": {
        "refreshRate": 5000
    }
}

```
