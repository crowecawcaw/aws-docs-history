# AWS IoT TwinMakercookie

factory example time-series connector

The complete [code of the cookie factory](https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/timestream_telemetry/lambda_function/udq_data_reader.py "https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/timestream_telemetry/lambda_function/udq_data_reader.py") Lambda function is available on GitHub.
Though you can still update the implementation after you link the connector to the
component type, we strongly recommend you verify the Lambda connector before
integrating with AWS IoT TwinMaker. You can test your Lambda function in the Lambda console or
locally in the AWS CDK. For more information on testing your Lambda functions, see
[Testing Lambda functions](../../../lambda/latest/dg/testing-functions.md "../../../lambda/latest/dg/testing-functions.md"), and [Locally testing AWS CDK applications](../../../serverless-application-model/latest/developerguide/serverless-cdk-testing.md "../../../serverless-application-model/latest/developerguide/serverless-cdk-testing.md").

## Example cookie factory

component types

In a component type, we define common properties that are shared across
components. For the cookie factory example, physical components of the same type
share the same measurements, so we can define the measurements schema in the
component type. As an example, the mixer type is defined in the following
example.

```
{
    "componentTypeId": "com.example.cookiefactory.mixer"
    "propertyDefinitions": {
        "RPM": {
            "dataType": { "type": "DOUBLE" },
            "isTimeSeries": true,
            "isRequiredInEntity": false,
            "isExternalId": false,
            "isStoredExternally": true
        },
        "Temperature": {
            "dataType": { "type": "DOUBLE" },
            "isTimeSeries": true,
            "isRequiredInEntity": false,
            "isExternalId": false,
            "isStoredExternally": true
        }
    }
}
```

For example, a physical component might have measurements in a Timestream database,
maintenance records in an SQL database, or alarm data in alarm systems. Creating
multiple components and associating them with an entity links different data
sources to the entity and populates the entity-component graph. In this context,
each component needs an `telemetryId` property to identify the unique
key of the component in the corresponding data source. Specifying the
`telemetryId` property has two benefits: the property can be used
in the data connector as a filter condition to only query values of the given
component and, if you include the `telemetryId` property value in the
data plane API response, then the client side takes the ID and can perform a
reverse lookup if necessary.

If you add the `TelemetryId` to the component type as an
external id, it identifies the component in the
`TimeStream` table.

```
{
    "componentTypeId": "com.example.cookiefactory.mixer"
    "propertyDefinitions": {
        "telemetryId": {
            "dataType": { "type": "STRING" },
            "isTimeSeries": false,
            "isRequiredInEntity": true,
            "isExternalId": true,
            "isStoredExternally": false
        },
        "RPM": {
            "dataType": { "type": "DOUBLE" },
            "isTimeSeries": true,
            "isRequiredInEntity": false,
            "isExternalId": false,
            "isStoredExternally": true
        },
        "Temperature": {
            "dataType": { "type": "DOUBLE" },
            "isTimeSeries": true,
            "isRequiredInEntity": false,
            "isExternalId": false,
            "isStoredExternally": true
        }
    }
}
```

Similarly we have the component type for the
`WaterTank`, as shown in the following JSON
example.

```
{
  "componentTypeId": "com.example.cookiefactory.watertank",
  "propertyDefinitions": {
    "flowRate1": {
      "dataType": { "type": "DOUBLE" },
      "isTimeSeries": true,
      "isRequiredInEntity": false,
      "isExternalId": false,
      "isStoredExternally": true
    },
    "flowrate2": {
      "dataType": { "type": "DOUBLE" },
      "isTimeSeries": true,
      "isRequiredInEntity": false,
      "isExternalId": false,
      "isStoredExternally": true
    },
    "tankVolume1": {
      "dataType": { "type": "DOUBLE" },
      "isTimeSeries": true,
      "isRequiredInEntity": false,
      "isExternalId": false,
      "isStoredExternally": true
    },
    "tankVolume2": {
      "dataType": { "type": "DOUBLE" },
      "isTimeSeries": true,
      "isRequiredInEntity": false,
      "isExternalId": false,
      "isStoredExternally": true
    },
    "telemetryId": {
      "dataType": { "type": "STRING" },
      "isTimeSeries": false,
      "isRequiredInEntity": true,
      "isExternalId": true,
      "isStoredExternally": false
    }
  }
}
```

The `TelemetryType` is an optional property in the component
type if it's aimed at querying property values in the entity scope. For an
example, see the defined component types in the [AWS IoT TwinMaker samples GitHub repository](https://github.com/aws-samples/aws-iot-twinmaker-samples/tree/main/src/workspaces/cookiefactory/component_types "https://github.com/aws-samples/aws-iot-twinmaker-samples/tree/main/src/workspaces/cookiefactory/component_types"). There are alarm types also
embedded into the same table, so the `TelemetryType` is defined
and you extract common properties like the `TelemetryId` and
`TelemetryType` to a parent component type for other child
types to share.

## Example Lambda

The Lambda connector needs to access the data source and generate the query
statement based on the input and forward it to the data source. An example
request sent to the Lambda is shown in the following JSON example.

```
{
    'workspaceId': 'CookieFactory',
    'selectedProperties': ['Temperature'],
    'startDateTime': 1648796400,
    'startTime': '2022-04-01T07:00:00.000Z',
    'endDateTime': 1650610799,
    'endTime': '2022-04-22T06:59:59.000Z',
    'properties': {
        'telemetryId': {
            'definition': {
                'dataType': { 'type': 'STRING' },
                'isTimeSeries': False,
                'isRequiredInEntity': True,
                'isExternalId': True,
                'isStoredExternally': False,
                'isImported': False,
                'isFinal': False,
                'isInherited': True,
            },
            'value': {
                'stringValue': 'Mixer_22_680b5b8e-1afe-4a77-87ab-834fbe5ba01e'
            }
        }
        'Temperature': {
            'definition': {
                'dataType': { 'type': 'DOUBLE' },
                'isTimeSeries': True,
                'isRequiredInEntity': False,
                'isExternalId': False,
                'isStoredExternally': True,
                'isImported': False,
                'isFinal': False,
                'isInherited': False
            }
        }
        'RPM': {
            'definition': {
                'dataType': { 'type': 'DOUBLE' },
                'isTimeSeries': True,
                'isRequiredInEntity': False,
                'isExternalId': False,
                'isStoredExternally': True,
                'isImported': False,
                'isFinal':False,
                'isInherited': False
            }
        },
    'entityId': 'Mixer_22_d133c9d0-472c-48bb-8f14-54f3890bc0fe',
    'componentName': 'MixerComponent',
    'maxResults': 100,
    'orderByTime': 'ASCENDING'
}
```

The goal of the Lambda function is to query historical measurement data for a given
entity. AWS IoT TwinMaker provides a component-properties map, and you should specify an
instantiated value for the component
ID. For example, to handle the component type-level query (which is common for alarm use
cases) and return the alarm status of all components in the workspace, then the
properties map has component type properties
definitions.

For the most straightforward case, as in the preceding request, we want a series
of temperature samples during the given time window for the given component, in
ascending time order. The query statement can be summarized as the
following:

```
...
SELECT measure_name, time, measure_value::double
    FROM {database_name}.{table_name}
    WHERE time < from_iso8601_timestamp('{request.start_time}')
    AND time >= from_iso8601_timestamp('{request.end_time}')
    AND TelemetryId = '{telemetry_id}'
    AND measure_name = '{selected_property}'
    ORDER BY time {request.orderByTime}
...
```
