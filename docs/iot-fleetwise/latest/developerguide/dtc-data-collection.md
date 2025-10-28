# Create a data collection campaign for diagnostic trouble codes

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

This topic describes how to create a data collection campaign for diagnostic trouble codes (DTC).

1. Define a custom signal on the Edge. You need to define the decoding rules for the DTC signal on the Edge as a custom decoded signal. For more information, see [Tutorial: Configure network agnostic data collection using a custom decoding interface](network-agnostic-data-collection.md "network-agnostic-data-collection.md").
2. Define custom function on the Edge. You need to define a custom function for collecting DTC signals on the Edge at a compiled time.

For more information, see the [custom function guide](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/custom-function-dev-guide.md "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/custom-function-dev-guide.md ") and the [DTC data collection reference implementation](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md#dtc_query-function-implementation "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md#dtc_query-function-implementation") in the _Edge Agent Developer Guide_.

###### Note

An example custom defined function is `DTC_QUERY` as shown in the [demo script](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md"). 3. Create a signal catalog that models a DTC signal as a string type.

```
[
 {
    "branch": {
        "fullyQualifiedName": "Vehicle",
        "description": "Vehicle"
        }
      },
      {
    "branch": {
        "fullyQualifiedName": "Vehicle.ECU1",
        "description": "Vehicle.ECU1"
        }
      },
      {
    "sensor": {
        "fullyQualifiedName": "Vehicle.ECU1.DTC_INFO",
        "description": "Vehicle.ECU1.DTC_INFO",
        "dataType": "STRING"
      }
   }
 ]
```

4. Create and activate a vehicle model with the DTC signal added.
5. Create and activate a decoder manifest with the DTC signal added. The DTC signal should be a `CUSTOM_DECODING_SIGNAL` signal decoder type with a `CUSTOM_DECODING_INTERFACE` network interface type.

###### Example signal decoder

```
[
  {
    "fullyQualifiedName": "Vehicle.ECU1.DTC_INFO",
    "interfaceId": "UDS_DTC",
    "type": "CUSTOM_DECODING_SIGNAL",
    "customDecodingSignal": {
      "id": "Vehicle.ECU1.DTC_INFO"
    }
  }
 ]
```

###### Example network interface

```
[
  {
    "interfaceId": "UDS_DTC",
    "type": "CUSTOM_DECODING_INTERFACE",
    "customDecodingInterface": {
      "name": "NamedSignalInterface"
    }
  }
]
```

###### Note

Controller Area Network (CAN) signals don't support the string data type. 6. Provision and create vehicles. The vehicles must utilize a vehicle model (model manifest) and decoder manifest that were activated in the previous steps. 7. Create and approve the campaign. You need to create a campaign by defining DTC signals (optionally with telemetry signals) and deploy it to vehicles. 8. Access the data in the defined destination. DTC data includes the `DTCCode`, `DTCSnapshot`, and `DTCExtendedDatastrings` as a raw string in the data destination defined in the campaign.
