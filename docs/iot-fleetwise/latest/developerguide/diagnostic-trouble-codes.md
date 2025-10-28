# Collect diagnostic trouble code data using AWS IoT FleetWise

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

When a vehicle detects an error, it generates a diagnostic trouble code (DTC) and records a snapshot of the affected sensors or actuators. DTCs help you learn about errors in near real-time, understand what is causing them, and take corrective actions. AWS IoT FleetWise supports the collection of DTCs, including corresponding DTC snapshots and extended data through a data collection campaign. This topic introduces the concepts, workflows, and keywords that facilitate DTC data collection, illustrated with examples.

The following shows key concepts for using DTC.

**Custom defined functions**

A custom defined function is the ability to invoke and execute your own functions predefined on the Edge Agent, extending the [custom decoding](network-agnostic-data-collection.md "network-agnostic-data-collection.md") concept. These functions are used in coordination with the AWS IoT FleetWise Agent. The Edge Agent for AWS IoT FleetWise software provides built-in functions for calculating signal statistics like minimum, maximum, and average values. A custom-defined function extends this capability by allowing you to create tailored logic for specific use cases. For diagnostic trouble code (DTC) data collection, developers can leverage custom functions to implement advanced data retrieval mechanisms, such as fetching DTC codes, snapshots, and extended data directly from the vehicle's Edge through Unified Diagnostic Services (UDS) or alternative diagnostic interfaces.

For more information, see the [custom function guide](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/custom-function-dev-guide.md "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/custom-function-dev-guide.md") and the [DTC data collection reference implementation](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md#dtc_query-function-implementation "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md#dtc_query-function-implementation") in the _Edge Agent Developer Guide_.

**Signal fetching**

In data collection campaigns, signals are typically collected continuously from a device and buffered on the Edge Agent software. Signals are then uploaded or stored periodically in time-based campaigns or triggered by specific conditions in condition-based campaigns. However, due to concerns about device traffic congestion, DTC signals can't be collected from devices and buffered continuously. To address this, AWS IoT FleetWise provides signal fetching, which ensures that the target signal is fetched discontinuously from a device.

Signal fetching supports both periodic and condition-driven actions. You can define the fetching driven method, conditions, and exact actions using custom defined functions for each signal that should not be collected from a device continuously. For signals managed by the signal fetching mechanism, the trigger type and conditions for local storage or cloud upload are still governed by the `CollectionScheme`, both `timeBasedCollectionScheme` and `conditionBasedCollectionScheme` are supported, which is the same as regular signals.

The following topics show you how you can create and use DTCs.

###### Topics

- [Diagnostic trouble code keywords](dtc-keywords.md "dtc-keywords.md")
- [Create a data collection campaign for diagnostic trouble codes](dtc-data-collection.md "dtc-data-collection.md")
- [Diagnostic trouble code use cases](dtc-use-cases.md "dtc-use-cases.md")
