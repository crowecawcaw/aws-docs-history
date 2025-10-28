End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create an AWS IoT Events detector for two states using CLI

In this example, we call the AWS IoT Events APIs using AWS CLI commands to create a detector that
models two states of an engine: a normal state and an over-pressure condition.

When the measured pressure in the engine exceeds a certain threshold, the model
transitions to the over-pressure state and sends an Amazon Simple Notification Service (Amazon SNS) message to alert a
technician to the condition. When the pressure drops below the threshold for three consecutive
pressure readings, the model returns to the normal state and sends another Amazon SNS message as a
confirmation that the condition has cleared. We require three consecutive readings below the
pressure threshold to eliminate possible stuttering of over-pressure/normal messages in case
of a nonlinear recovery phase or a one-off anomalous recovery reading.

The following is an overview of the steps to create the detector.

**Create _inputs_.**

To monitor your devices and processes, they must have a way to get telemetry data
into AWS IoT Events. This is done by sending messages as _inputs_ to AWS IoT Events.
You can do this in several ways:

- Use the [BatchPutMessage](../apireference/API_iotevents-data_BatchPutMessage.md "../apireference/API_iotevents-data_BatchPutMessage.md") operation. This method is easy but requires that your
  devices or processes are able to access the AWS IoT Events API through an SDK or the
  AWS CLI.
- In AWS IoT Core, write an [AWS IoT Events action](../../../iot/latest/developerguide/iot-rule-actions.md#iotevents-rule "../../../iot/latest/developerguide/iot-rule-actions.md#iotevents-rule") rule
  for the AWS IoT Core rules engine that forwards your message data into AWS IoT Events. This
  identifies the input by name. Use this method if your devices or processes can, or
  already are, sending messages through AWS IoT Core. This method generally requires less
  computing power from a device.
- In AWS IoT Analytics, use the [CreateDataset](../../../iotanalytics/latest/userguide/automate.md#aws-iot-analytics-automate-create-dataset "../../../iotanalytics/latest/userguide/automate.md#aws-iot-analytics-automate-create-dataset") operation to create a data set with
  `contentDeliveryRules` that specify the AWS IoT Events input, where data set
  contents are sent automatically. Use this method if you want to control your devices
  or processes based on data aggregated or analyzed in AWS IoT Analytics.

Before your devices can send data in this way, you must define one or more inputs.
To do so, give each input a name and specify which fields in the incoming message data
that the input monitors.

**Create a detector model**

Create a _detector model_ (a model of your equipment or process)
using _states_. For each state, define conditional (Boolean) logic
that evaluates the incoming inputs to detect significant events. When an event is
detected, it can change the state or initiate custom-built or predefined actions using
other AWS services. You can define additional events that initiate actions when
entering or exiting a state and, optionally, when a condition is met.

**Monitor several devices or processes**

If you're monitoring several devices or processes and you want to keep track of each
of them separately, specify a field in each input that identifies the particular device
or process the input comes from. See the `key` field in
`CreateDetectorModel`. When a new device is identified (a new value is seen
in the input field identified by the `key`), a detector instance is created.
The new detector instance continues to respond to inputs coming from that particular
device until its detector model is updated or deleted. You have as many unique detectors
(instances) as there are unique values in input `key` fields.

**Monitor a single device or process**

If you're monitoring a single process (even if several devices or subprocesses are
sending inputs), you don't specify a unique identifying `key` field. In this
case, a single detector (instance) is created when the first input arrives. For example,
you might have temperature sensors in each room of a house, but only one HVAC unit to
heat or cool the entire house. So you can only control this as a single process, even if
each room occupant wants their vote (input) to prevail.

**Send messages from your devices or processes as inputs to your detector model**

We described the several ways to send a message from a device or process as an input
into an AWS IoT Events detector in _inputs_. After you created the inputs and
build the detector model, you're ready to start sending data.

###### Note

When you create a detector model, or update an existing one, it takes several
minutes before the new or updated detector model begins receiving messages and
creating detectors (instances). If the detector model is updated, during this time you
might continue to see behavior based on the previous version.

###### Topics

- [Create an AWS IoT Events input to capture device data](iotevents-create-input.md "iotevents-create-input.md")
- [Create a detector model to represent device
  states in AWS IoT Events](iotevents-create-detector.md "iotevents-create-detector.md")
- [Send messages as inputs to a detector in
  AWS IoT Events](iotevents-batch-put-messages.md "iotevents-batch-put-messages.md")
