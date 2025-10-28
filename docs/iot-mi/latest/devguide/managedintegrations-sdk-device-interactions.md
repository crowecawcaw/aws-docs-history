# Feature and device interactions

in managed integrations

This section describes the role of the C-Function implementation and the interaction
between the device and the managed integrations device feature.

###### Topics

- [Handling remote
  commands](#managedintegrations-sdk-interactions-commands "#managedintegrations-sdk-interactions-commands")
- [Handling unsolicited
  events](#managedintegrations-sdk-interactions-unsolicited "#managedintegrations-sdk-interactions-unsolicited")

## Handling remote

commands

Remote commands are handled by the interaction
between the End device SDK and the feature. The following actions describe an example of how you
can turn on a light bulb using this interaction.

**MQTT client receives payload and passes to Data Model Handler**

When you send a remote command, the MQTT client receives the message from
managed integrations in JSON format. It then passes the payload to the data model handler. For
example, say you want to use managed integrations to turn on a light bulb. The light bulb has an
endpoint#1 that supports the OnOff cluster. In this case, when you send
the command to turn on the light bulb, managed integrations sends a request over MQTT to the
device, which says that it wants to invoke the On command on endpoint#1.

**Data Model Handler checks for callback functions and invokes them**

The Data Model Handler parses the JSON request. If the request contains properties
or actions, the Data Model Handler finds the endpoints and sequentially invokes the
corresponding callback functions. For example, in the case of the light bulb, when the
Data Model Handler receives the MQTT message, it checks whether the callback function
corresponding to the On command defined in the OnOff cluster is
registered on endpoint#1.

**Handler and C-Function implementation execute the command**

The Data Model Handler calls the appropriate callback functions that it found and
invokes them. The C-Function implementation then calls the corresponding hardware
functions to control the physical hardware and returns the execution result. For
example, in the case of the light bulb, the Data Model Handler calls the callback
function and stores the execution result. The callback function then turns on the
light bulb as a result.

**Data Model Handler returns execution result**

Once all callback functions have been called, the Data Model Handler combines all
results. It then packs the response in JSON format and publishes the result to the
managed integrations cloud using the MQTT client. In the case of the light bulb, the MQTT message
in the response will contain the result that the light bulb was turned on by the
callback function.

## Handling unsolicited

events

Unsolicited events are also handled by the
interaction between the End device SDK and the feature. The following actions describe how.

**Device sends notification to Data Model Handler**

When a property change or event occurs, such as when a physical button has been
pushed on the device, the C-Function implementation generates an unsolicited event
notification and calls the corresponding notify function to send the notification to
the Data Model Handler.

**Data Model Handler translates notification**

The Data Model Handler handles the notification received and translates it to the
AWS data model.

**Data Model Handler publishes notification to the Cloud**

The Data Model Handler then publishes an unsolicited event to the managed integrations cloud
using the MQTT client.
