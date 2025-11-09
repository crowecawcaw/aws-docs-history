# 10 AWS IoT Services

## 10.1 AWS IoT Device Defender

_(Support for this feature is required and tested for as of v1.1.1.)_

ExpressLink devices support the [AWS IoT Device
Defender](../../../iot/latest/developerguide/device-defender.md "../../../iot/latest/developerguide/device-defender.md") service. They can publish a basic set of metrics to AWS IoT Core at
a configurable interval, including the table below:

| Table 7 - ExpressLink Defender metrics | ExpressLink Custom Metric | Type                                                       | Description |
| -------------------------------------- | ------------------------- | ---------------------------------------------------------- | ----------- |
| Bytes Out                              | Count                     | Number of bytes sent since last update.                    |
| Messages sent                          | Count                     | Number of messages sent since last update.                 |
| Messages received                      | Count                     | Number of messages received since last update.             |
| Hard Reset Event                       | Flag                      | Set to 1 if a hardware reset occurred since last update.   |
| Reconnect Events                       | Flag                      | Set to 1 if a reconnect occurred since last update.        |
| Flash Memory Writes                    | Count                     | Number of writes to flash memory since last update.        |
| <Module-Name Prefix> Custom Metric(s)  |                           | One or more manufacturer/module specific custom metrics... |

All ExpressLink custom metrics are volatile in nature, as their values are reset
to 0 after each periodic update (or set to 1 upon a device reset/reboot for the
corresponding events).

The device defender feature is activated by setting the _DefenderPeriod_
configuration parameter (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") )
to a value greater than 0 in the configuration dictionary (using the AT+CONF command).

The _DefenderPeriod_ configuration parameter value indicates the
_number of seconds_ between successive updates of the Device Defender
metrics. The maximum period value is an implementation detail that must be documented by
the module manufacturer in the device data sheet. Note that the Device Defender service
may choose to throttle down (reject) metric updates if they are too frequent.

The latest metrics collected are sent to the Device Defender service as soon as the
device connects and at each successive interval. The internal timer continues counting
even when the device is disconnected. The internal timer is reset when the Device Defender
feature is turned off (when the _DefenderPeriod_ configuration parameter
is set to 0).

The _DefenderPeriod_ parameter is non-volatile, so an ExpressLink
device automatically resumes sending Device Defender metrics after a reset (using a RESET
command, power cycle or the RST pin).

Module manufacturers can offer additional custom metrics specific to their model.
They must prefix the metric with the distinctive **Model**
name and document the feature in the device datasheet. (See the "About" Configuration
parameter in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") .

###### Note

Access to the AWS IoT Device Defender service is available only when the device
is in the _onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")) and the customer/OEM AWS IoT account
is properly configured.

Examples:

```

AT+CONF DefenderPeriod=0     # Device Defender metrics are disabled
                             # NOTE: this is the initialized value after a factory reset (see Table 2 - Configuration Dictionary Persistent Keys

AT+CONF DefenderPeriod=60    # Device Defender metrics are updated every minute

AT+CONF DefenderPeriod=3600  # Device Defender metrics are updated every hour
```

## 10.2 AWS IoT Device Shadow

SHADOW commands are provided to facilitate use of the [AWS IoT Device
Shadow service](../../../iot/latest/developerguide/iot-device-shadows.md "../../../iot/latest/developerguide/iot-device-shadows.md"). Set the **EnableShadow** configuration
parameter to 1 to enable support for these commands. (See [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3 "elpg-configuration-dictionary.md#elpg-table3") .) To provide Shadow support, a module automatically handles
subscriptions to the various Device Shadow MQTT topics, and parses and reports
the responses provided by the service to the device in the form of SHADOW events.

###### Note

Access to the AWS IoT Device Shadow service is allowed only when the module
is in the _onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")), that is, when the module is
connected to the customer's AWS account.

The SHADOW INIT# command manages subscriptions to Shadow topics. It must be invoked,
and its actions completed, before you invoke any of the other SHADOW commands.

As the interaction with the Device Shadow service often requires a long
messaging round trip, the module implements an asynchronous API to avoid blocking
the host. SHADOW commands generate requests to the Device Shadow service and return
immediately, while SHADOW GET commands can be used later to poll, and eventually
retrieve, the responses of the service.

`10.2.1.1`  

Each ExpressLink manufacturer can choose
to simultaneously support a maximum number of named shadow documents
(**MaxShadow** ≥ 1). The chosen MaxShadow value will be
documented in the manufacturer's module datasheet.

The corresponding list of non-persistent parameters,
**Shadow1 .. Shadow\***{MaxShadow}\*,
will be pre-populated in the Configuration Dictionary and initialized to empty strings.
(See [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3 "elpg-configuration-dictionary.md#elpg-table3") .)

Device Shadow support requires a continuous connection with the AWS IoT Core Service.
Such a connection must be established before any SHADOW commands are issued and must
be maintained uninterrupted until the completion of any of the requests. If the
connection is lost at any point, the host has responsibility to re-initialize the
SHADOW interface, re-issue any interrupted commands and, eventually, re-subscribe to
shadows for which delta update notifications are expected.

`10.2.1.2`  

All SHADOW commands use a
_client-token_ defined by the non-volatile configuration parameter
_ShadowToken_ (factory default: "ExpressLink") to identify and
manage requests and responses received on the relevant Device Shadow service topics.
Any notifications received that do not match the client-token used in the request,
and not generated by the SHADOW commands, are discarded.

`10.2.1.3`  

If the _ShadowToken_
configuration parameter is set to an empty string, ANY subsequent notifications
received from the Shadow service will NOT be managed by the module but will be added
to the messaging queue for the host to handle with the GET0 command (see
[5.1.5 GET0   »Request next message pending on an unassigned topic«](elpg-messaging.md#elpg-get0-command "elpg-messaging.md#elpg-get0-command")).

### 10.2.2 SHADOW*[#]* INIT   »Initialize communication with the Device Shadow service«

Initialize the Device Shadow service communication interface for the specified
shadow. This subscribes to various topics that are managed by other SHADOW commands
such as SHADOW DOC, SHADOW UPDATE and SHADOW DELETE. Note that subscriptions to
Shadow Deltas are controlled separately by the
[SHADOW SUBSCRIBE](#elpg-shadow-subscribe-command "#elpg-shadow-subscribe-command") and
[SHADOW UNSUBSCRIBE](#elpg-shadow-unsubscribe-command "#elpg-shadow-unsubscribe-command")
commands.

`10.2.2.1`   When the INIT process is completed
successfully, a SHADOW INIT event is generated (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4 "elpg-event-handling.md#elpg-table4")) and further SHADOW commands can be issued.

`10.2.2.2`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow interface is initialized.

`10.2.2.3`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's
Named Shadows.

`10.2.2.4`   If a Shadow# entry is modified (AT+CONF)
before the corresponding SHADOW# INIT process is completed, the initialization is
aborted and no Shadow INIT event will be generated.

###### Returns:

`10.2.2.5`   `OK`

The Device Shadow service initialization process has started.

`10.2.2.6`   `ERR7 OUT OF RANGE`

The specified shadow (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.2.7`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the
configuration dictionary is empty.

`10.2.2.8`   `ERR6 NO CONNECTION`

The device is currently not connected and the request cannot be
performed.

`10.2.2.9`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0 or the device is not in the
_onboarded_ state, see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

### 10.2.4 SHADOW*[#]* DOC   »Request a Device Shadow document«

Send a request to the Device Shadow service to retrieve an entire shadow
document for the device.

`10.2.4.1`   A SHADOW DOC event is generated
when the request is accepted or rejected.

`10.2.4.2`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is requested.

`10.2.4.3`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's
Named Shadows.

###### Returns:

`10.2.4.4`   `OK`

A shadow document request was sent to the Device Shadow service.

`10.2.4.5`   `ERR7 OUT OF RANGE`

The specified shadow (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.4.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.4.7`   `ERR6 NO CONNECTION`

The device is currently not connected and the request cannot be performed.

`10.2.4.8`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the maximum number of simultaneous
asynchronous requests was exceeded, or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

### 10.2.5 SHADOW*[#]* GET DOC   »Retrieve a device shadow document«

Check if a (requested) Device Shadow document has arrived and retrieve its contents.

`10.2.5.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is requested.

`10.2.5.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's
Named Shadows.

###### Returns:

`10.2.5.3`   `OK`

The requested shadow document has not arrived yet.

`10.2.5.4`   `OK 1 *{document}*`

The requested shadow document has arrived.

`10.2.5.5`   `OK 0 *{detail}*`

The shadow document request was rejected (0), additional detail
is provided.

`10.2.5.6`   `ERR7 OUT OF RANGE`

The specified shadow (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.5.7`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.5.8`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

Example:

```
AT+SHADOW DOC{EOL}          # Request the entire (unnamed) device shadow document.
OK{EOL}                     # Request submitted.
AT+SHADOW GET DOC{EOL}      # Attempt to retrieve the entire device shadow document.
OK{EOL}                     # No document has arrived yet.

 ...later...

OK 1 {"state": { "lamp": { "switch": "ON" } }, "version": 11, "timestamp": 1234 }{EOL}
                            # The Device Shadow service response has arrived!
 ...or...
OK 0 {…} {EOL}              # The Device Shadow document request was rejected!
```

### 10.2.6 SHADOW*[#]* UPDATE *{new state}*   »Request a device shadow document update«

Send a request to the Device Shadow service to update a device shadow. The
_{new state}_ is a JSON document and should NOT contain a
"client-token" unless the _ShadowToken_ configuration parameter
is set to empty (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ),
in which case all shadow notifications are left for the host to manage.

`10.2.6.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is assumed.

`10.2.6.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

`10.2.6.3`   A SHADOW UPDATE event is generated when the
request is accepted (or rejected).

###### Returns:

`10.2.6.4`   `OK`

A shadow document update request was sent to the Device Shadow
service.

`10.2.6.5`   `ERR4 PARAMETER ERROR`

The _{new state}_ parameter provided is not a
valid JSON document.

`10.2.6.6`   `ERR7 OUT OF RANGE`

The specified shadow (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.6.7`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.6.8`   `ERR6 NO CONNECTION`

The device is currently not connected and the request cannot be performed.

`10.2.6.9`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0).

`10.2.6.10`   `ERR24 SHADOW ERROR`

If a client-token was present in the update document but
_ShadowToken_ is NOT empty (SHADOW notifications are
managed), or if the device is not in the _onboarded_
state (see [21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")), then the module
returns 'SHADOW ERROR'.

### 10.2.7 SHADOW*[#]* GET UPDATE   »Retrieve a device shadow update response«

Check if a response to a (requested) Device Shadow update has arrived and retrieve
the returned value.

`10.2.7.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is assumed.

`10.2.7.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

###### Returns:

`10.2.7.3`   `OK`

A shadow document update response has not arrived yet.

`10.2.7.4`   `OK *{0/1} {document}*`

A response to the shadow document update request has arrived. A
Boolean value indicates if it was accepted (1) or rejected (0). An
additional document containing the update details is appended.

`10.2.7.5`   `ERR7 OUT OF RANGE`

The shadow specified (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.7.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.7.7`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

Example:

```
AT+SHADOW1 UPDATE {"state":{"desired":{"switch": "off" } } }{EOL}
OK{EOL}                     # The request was sent.
AT+SHADOW1 GET UPDATE{EOL}  # Check if the update was accepted/rejected.
OK{EOL}                     # No response received yet.

 ...later...

AT+SHADOW1 GET UPDATE(EOL}  # Check if the update was accepted/rejected.
OK 1 {"switch": "off"){EOL} # The update was accepted.
 ...or...
OK 0 {..}{EOL}              # The update was rejected.
```

### 10.2.8 SHADOW*[#]* SUBSCRIBE   »Subscribe to a device shadow document«

Send a request to the Device Shadow service to receive Delta updates for a
shadow document.

`10.2.8.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is
requested.

`10.2.8.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

`10.2.8.3`   A SHADOW SUBACK or SHADOW SUBNACK event
are generated when the subscription is accepted or rejected. Note that if a Shadow#
(configuration string) is modified before the subscription confirmation (or rejection)
is received, the corresponding event will not be generated.

###### Returns:

`10.2.8.4`   `OK`

A shadow subscribe request was sent to the Device Shadow service.

`10.2.8.5`   `ERR7 OUT OF RANGE`

The specified shadow parameter (_[#]_) exceeds
the maximum number of shadows supported by this module.

`10.2.8.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the
configuration dictionary is empty.

`10.2.8.7`   `ERR6 NO CONNECTION`

The device is not currently connected and the request cannot be
performed.

`10.2.8.8`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

Example:

```
AT+SHADOW2 SUBSCRIBE{EOL}         # Request subscription to the device Shadow2.
OK{EOL}                           # Request submitted.

 ...later...

AT+EVENT?{EOL}                    # Check if the subscription was accepted.
OK{EOL}                           # No response has arrived yet.
 ...or...
OK 26 2{EOL}                      # SHADOW SUBACK The subscription to Shadow2 was accepted.
 ...or...
OK 27 2{EOL}                      # SHADOW SUBNACK The subscription to Shadow2 was rejected.
```

### 10.2.9 SHADOW*[#]* UNSUBSCRIBE   »Unsubscribe from a device shadow document«

Send a request to the Device Shadow service to stop receiving Delta updates
for a shadow document. Note that no SHADOW event is generated following this
request.

`10.2.9.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is
requested.

`10.2.9.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

###### Returns:

`10.2.9.3`   `OK`

A shadow document request was sent to the Device Shadow service.

`10.2.9.4`   `ERR7 OUT OF RANGE`

The shadow specified (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.9.5`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.9.6`   `ERR6 NO CONNECTION`

The device is currently not connected and the request cannot be performed.

`10.2.9.7`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

Example:

```
AT+SHADOW3 UNSUBSCRIBE{EOL}    # Request subscription to the device Shadow2.
OK{EOL}                        # Request submitted.
```

### 10.2.10 SHADOW*[#]* GET DELTA   »Retrieve a Shadow Delta message«

Query for the next pending shadow update message. This command can be used
after receiving a DELTA event, or to poll the delta queue (the queue depth is
implementation specific).

`10.2.10.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is
requested.

`10.2.10.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

###### Returns:

`10.2.10.3`   `OK`

An empty string indicates no delta pending.

`10.2.10.4`   `OK *{delta document}*`

A shadow delta update has arrived. A document containing the details
is appended.

`10.2.10.5`   `ERR7 OUT OF RANGE`

The shadow specified (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.10.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.10.7`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

### 10.2.11 SHADOW*[#]* DELETE   »Request the deletion of a Shadow document«

Requests the Device Shadow Service to delete a device shadow document.

`10.2.11.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is
requested.

`10.2.11.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

`10.2.11.3`   A SHADOW DELETE event is generated
when the request is accepted or rejected.

###### Returns:

`10.2.11.4`   `OK`

The request was sent to the Device Shadow service.

`10.2.11.5`   `ERR7 OUT OF RANGE`

The shadow specified (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.11.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.11.7`   `ERR6 NO CONNECTION`

The device is currently not connected and the request cannot be performed.

`10.2.11.8`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the maximum number of simultaneous
asynchronous requests was exceeded, or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

### 10.2.12 SHADOW*[#]* GET DELETE   »Request a Shadow delete response«

Check if a Device Shadow Delete request was accepted.

`10.2.12.1`   If the numerical shadow parameter
(_[#]_) is not provided, the Unnamed Shadow document is
requested.

`10.2.12.2`   Otherwise, the corresponding Shadow#
entry in the Configuration Dictionary is used to specify one of the object's Named
Shadows.

###### Returns:

`10.2.12.3`   `OK`

The request was sent to the Device Shadow service.

`10.2.12.4`   `OK *{0/1} {payload}*`

The shadow delete request was accepted (1) or rejected (0). Additional
detail may be present in the _{payload}_.

`10.2.12.5`   `ERR7 OUT OF RANGE`

The shadow specified (_[#]_) exceeds the maximum
number of shadows supported by this module.

`10.2.12.6`   `ERR8 PARAMETER UNDEFINED`

The specified shadow (_[#]_) entry in the configuration
dictionary is empty.

`10.2.12.7`   `ERR24 SHADOW ERROR`

Shadow support is disabled (the _EnableShadow_
configuration parameter set to 0), or the device is not in the
_onboarded_ state (see
[21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).

### 10.2.13 SHADOW EVENTS

When subscribing to shadow document messages, retrieving a shadow document, or
requesting updates, the module communicates with the Device Shadow service using
various MQTT topics. When it receives a response to a request or a shadow Delta
update to which it has subscribed, the module reports this to the host
_asynchronously_ by generating a Shadow event (see
[Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4 "elpg-event-handling.md#elpg-table4")). Each Shadow event
carries the _Shadow-Index_ parameter:

- **0**  indicates the unnamed
  Shadow
- **1..MaxShadow**  indicates
  the corresponding Shadow# entry in the configuration table

Example 1:

```
AT+EVENT?{EOL}                # Query events pending.
OK 24 1{EOL}                  # A SHADOW DELTA event was received for the Shadow1.
AT+SHADOW1 GET DELTA{EOL}     # Fetch the delta message.
OK {delta document}{EOL}      # Returns the delta document received.
```

Example 2:

```
AT+SHADOW SUBSCRIBE{EOL}      # Request a subscription to DELTA updates for the unnamed Shadow
OK{EOL}                       # Request sent successfully.

 ...later...

AT+EVENT?{EOL}
OK  26 0{EOL}                 # SHADOW SUBACK The subscription request was accepted.
 ...or...
OK 27 0{EOL}                  # SHADOW SUBNACK The subscription request was rejected.
```

## 10.3 AWS IoT Jobs

The JOB command is not implemented. It is reserved for the support of the AWS IoT Jobs service.
