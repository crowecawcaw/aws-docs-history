# 5 Messaging

## 5.1 Messaging topic model

The ExpressLink messaging system relies on a list of topics defined in the
configuration dictionary (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ). Each topic is assigned an index that can be used to
dereference the assigned string value. Index 0 has a special meaning, while all
other index values up to an implementation-specific maximum index can be used by the
host to define additional topics. Messaging topics defined in this list are managed
independently from other topics eventually used by ExpressLink to handle Jobs, OTA,
and shadow updates.

`5.1.1.1`  

Topic Index 0 is reserved as a catch-all for messages that do not match other
existing topics. An attempt to send or subscribe to a topic with index 0 will
return `ERR7 OUT OF RANGE`.

`5.1.1.2`  

Topic _Index{MaxTopic}_ is an implementation detail
documented in the module manufacturer's datasheet.

### 5.1.2 Topic usage rules

Topics are defined to be compatible with the MQTT 3.1.1 standard

### 5.1.3 SEND*[#] message*   »Publish msg on a topic selected from topic list«

Send a message on a topic provided in the configuration dictionary. The
configuration parameter QoS value (see [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3 "elpg-configuration-dictionary.md#elpg-table3") ) at the time the command is issued determines the
applicable Quality of Service (only QoS levels 0 and 1 are supported!).

###### Where:

_[#]_

The index of a topic in CONFIG dictionary (1..MaxTopic).

_message_

The message to publish (string).

###### Returns:

`5.1.3.1`   `OK*{EOL}*`

If the message is sent successfully, then the module returns 'OK'.

Example 1:

```
AT+SEND2 Hello World    # Publish 'Hello World' on Topic2
OK                      # The message will be sent
```

`5.1.3.2`   `ERR6 NO CONNECTION`

If no connection has been made, then the module returns 'NO CONNECTION'.

Example 2:

```
AT+SEND1 Hello World    # Publish Hello World on Topic1
ERR6 NO CONNECTION      # A connection has not been established
```

`5.1.3.3`   `ERR7 OUT OF RANGE`

If the supplied topic index is larger than the maximum allowed topic
number, the module returns 'OUT OF RANGE'.

Example 3:

```
AT+SEND99 Hello World      # Publish Hello World on Topic99
ERR7 OUT OF RANGE    # Topic 99 is not within the available range of topics for this device
```

`5.1.3.4`   `ERR8 PARAMETER UNDEFINED`

If the supplied topic index points to a topic entry that has
not been defined (empty), the module returns 'PARAMETER UNDEFINED'.

Example 4:

```
AT+CONF Topic3={EOL}      # Define Topic3 as empty
OK

AT+SEND3 Hello World      # Publish Hello World on Topic3
ERR8 PARAMETER UNDEFINED  # The selected topic was undefined
```

### 5.1.4 GET   »Request next message pending on any topic«

Retrieve the next message received in the order of arrival.

###### Returns:

`5.1.4.1`   `OK1*{separator}{topic}{EOL}{message}{EOL}*`

If a message is available on any topic, the module responds with 'OK' followed by the
topic and the message.

Example:

```
AT+GET            # poll for messages received on any topic
OK1 data{EOL}     # a message was received from topic 'data' (expect another line)
Hello World{EOL}  # the actual message received
```

`5.1.4.2`   `OK*{EOL}*`

If no message was received on any topic, the module responds with 'OK'
followed by _{EOL}_.

### 5.1.5 GET0   »Request next message pending on an unassigned topic«

Retrieve the next message received on a topic that was not in the topic list.
This acts as a catch-all option and can be useful when the host subscribes to a
topic then modifies the topic string in the configuration dictionary without
first unsubscribing. This can also be used in combination with the AWS IoT Device
Shadow features (see entry 8.2.1.3 under section [10.2 AWS IoT Device Shadow](elpg-iot-services.md#elpg-device-shadow "elpg-iot-services.md#elpg-device-shadow")).

Note that the response to this command always produces two output lines, an exception
to the general format defined in [4.6.1 General response formats](elpg-commands.md#elpg-responses-formats "elpg-commands.md#elpg-responses-formats").

###### Returns:

`5.1.5.1`   `OK1*{separator}{topic}{EOL}{message}{EOL}*`

Example:

```
AT+GET0            # poll for messages received on any unassigned topic
OK1 data{EOL}      # a message was received from topic 'data' (expect another line)
Hello World{EOL}   # the actual message received
```

`5.1.5.2`   `OK*{EOL}*`

If no message was received on any unassigned topic, the module
returns 'OK' followed by _{EOL}_.

### 5.1.6 GET*[#]*   »Request next message pending on the indicated topic«

Retrieve the next message received on a topic at the specified index (1..MaxTopic)
in the topic list.

###### Returns:

`5.1.6.1`   `OK*{separator}{message}{EOL}*`

If a message is available on the indicated topic, the module
responds with 'OK' followed immediately by the message.

Example:

```
AT+GET2           # select messages received on Topic2
OK Hello World    # a message received on the topic at index 2 in the list of topics
```

`5.1.6.2`   `OK*{EOL}*`

If a message is NOT available matching the requested topic, the
module responds with 'OK' followed by _{EOL}_.

`5.1.6.3`   `OK*{message}{EOL}*`

Even if there is no active connection, a normal read from the message queue
takes place and might return a valid message.

`5.1.6.4`   `ERR7 OUT OF RANGE`

If the supplied topic index is larger than the maximum allowed
topic number, then the module returns 'OUT OF RANGE'.

`5.1.6.5`   `ERR8 PARAMETER UNDEFINED`

If the requested topic is not defined (empty), then the module
returns 'PARAMETER UNDEFINED'.

`5.1.6.6`   Message queue overflow conditions

If the host fails to retrieve a message in time and so does not free up
space and the buffer capacity is exceeded, an overrun occurs and
_new messages arriving from the cloud may be lost_.
The condition will be reported as an OVERFLOW event (see
[Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4 "elpg-event-handling.md#elpg-table4"))
and added to the event queue. It is then accessible to the host
processor by means of the EVENT? command. If there is an overflow,
the number of messages-received events in the queue will exceed the
actual number of messages that are present. The depth of the message
queue is an implementation detail that is documented in the module
manufacturer's datasheet.

### 5.1.7 SUBSCRIBE*[#]*   »Subscribe to Topic#«

The module subscribes to the topic and starts receiving messages. Incoming
messages trigger events. The messages can be read with a GET*[#]*
command.

Note that this is a stateless feature; the ExpressLink module will request
a subscription to the MQTT broker, but will not retain information about its
current state.

`5.1.7.1`   If a topic number (_[#]_)
is provided, use the topic at the specified index.

###### Note

Sending a message to a topic to which a module is subscribed results in the
broker sending a copy back to the module.

Example:

```
AT+CONF Topic1=sensor1/state
OK

AT+SUBSCRIBE1    # The module will subscribe to the topic sensor1/state
OK
```

###### Returns:

`5.1.7.2`   `OK`

The subscription request was sent to the MQTT broker for the
topic specified in the configuration dictionary as Topic#.

`5.1.7.3`   `ERR6 NO CONNECTION`

If no connection has been made, then the module returns 'NO CONNECTION'.

`5.1.7.4`   `ERR8 PARAMETER UNDEFINED`

If the requested topic is not defined (empty), then the module
returns 'PARAMETER UNDEFINED'.

`5.1.7.5`   `ERR7 OUT OF RANGE`

If the supplied topic index is larger than the maximum allowed topic
number, then the module returns 'OUT OF RANGE'.

`5.1.7.6`   A SUBACK or SUBNACK event is generated
when the request is accepted or rejected by the MQTT broker.

###### Warning

The host should not issue an UNSUBSCRIBE command immediately following
a SUBSCRIBE command before the acknowledgment event is received. This might result
in a race condition and unpredictable MQTT broker behavior.

`5.1.7.7`   If the topic referred to by a subscription
is altered (AT+CONF), before an acknowledgment is received, the corresponding event
is NOT generated.

`5.1.7.8`   If a new SUBSCRIBE command is issued
for the same topic (before an acknowledgment is received), the previous acknowledgment
event is NOT generated.

###### Note

When in the "staging" state (the device is connected to the staging account,
see [4.7.1 CONNECT?   »Request the connection status«](elpg-commands.md#elpg-connectq-command "elpg-commands.md#elpg-connectq-command") for details)
restrictive policies apply, including not being able to subscribe to topics that do
not begin with the device's _ThingName_. An attempt to subscribe to such topics may
result in the connection being immediately dropped.

### 5.1.8 UNSUBSCRIBE*[#]*   »Unsubscribe from Topic#«

The device unsubscribes from the selected topic and stops receiving its
messages/events.

###### Returns:

`5.1.8.1`   `OK`

A request to unsubscribe from the topic specified in the configuration
dictionary as Topic# was sent.

###### Warning

The host should not issue an UNSUBSCRIBE command immediately
following a SUBSCRIBE command before the acknowledgment event is received.
This would result in a race condition and unpredictable MQTT broker
behavior.

`5.1.8.2`   `ERR6 NO CONNECTION`

If no connection has been made, then the module returns 'NO CONNECTION'.

`5.1.8.3`   `ERR8 PARAMETER UNDEFINED`

If the requested topic is not defined (empty), then the module returns
'PARAMETER UNDEFINED'.

`5.1.8.4`   `ERR7 OUT OF RANGE`

If the supplied topic index is larger than the maximum allowed
topic number, then the module returns 'OUT OF RANGE'.

Example:

```
AT+CONF Topic1=sensor1/state
OK

AT+SUBSCRIBE1      # The module will subscribe to topic sensor1/state
OK
...
AT+UNSUBSCRIBE1    # The module will unsubscribe from topic sensor1/state
OK
```
