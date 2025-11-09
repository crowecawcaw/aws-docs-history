# 4 ExpressLink commands

## 4.1 Introduction

`4.1.1.1`   These commands are sent to and from the UART.
The default UART configuration shall be 115200, 8, N, 1 (baud rate: 115200; data bits: 8;
parity: none; stop bits: 1). There is no hardware or software flow control for UART
communications.

`4.1.1.2`   The baud rate is NOT configurable.

`4.1.1.3`   No Local Echo is provided.

###### Note

Communication between the ExpressLink modules and the AWS Cloud are encrypted both
during transmission (using the TLS 1.2 protocol) and while at rest. However, the serial
interface (UART) between the host processor and the module isn't encrypted. If sensitive data
needs to be transmitted to and from the ExpressLink module, and unauthorized persons can
potentially gain physical control of the device, we recommend that the host processor and the
corresponding cloud application implement a suitable, additional end-to-end message encryption
scheme.

## 4.2 ExpressLink commands format

All ExpressLink commands assume the following general format:

`**AT+***{command}[#]{separator}[parameter]{EOL}*`

Where:

`4.2.1`   `*{command}*`

A short, alphabetical character string (including "\_", "!", and "?")
that matches one of the commands listed in the following sections (CONNECT,
TIME?, FACTORY_RESET).

###### Note

Commands are not case sensitive, although in this document, uppercase
is always used for consistency.

###### Returns:

`4.2.1.1`   `ERR3 COMMAND NOT FOUND`

If the command is unknown, then the module returns 'COMMAND NOT FOUND'.

`4.2.2`   `*[#]*Optional numerical suffix (first parameter)`

An optional decimal (0..N) suffix qualifier (multiple digits allowed)
is used by selected commands as a first numerical parameter.

###### Returns:

`4.2.2.1`   `ERR4 PARAMETER ERROR`

If a numerical suffix was provided but the command did not expect it, or
if a numerical suffix is missing but required, the module
returns 'ERR4 PARAMETER ERROR'.

`4.2.2.2`   `ERR7 OUT OF RANGE`

If the numeric suffix is out of the valid range for the
command, the module returns 'ERR7 OUT OF RANGE'.

`4.2.4`   `*{seperator}*`

A single ascii space character (0x20).

###### Returns:

`4.2.4.1`   `ERR2 PARSE ERROR`

Return ERR2 PARSE ERROR if ANY character other than 0x20 is present after the numerical suffix
or ‘?’ in the command string.

`4.2.5`   `*[parameter] optional parameter*`

An (escaped) ASCII string with the data required for the command.

###### Returns:

`4.2.5.1`   `ERR4 PARAMETER ERROR`

Return ERR4 PARAMETER ERROR if the command is unable to process the parameter supplied.

`4.2.6`   `*{EOL}*`

The ASCII _line feed_ character (0x0a) OR the ASCII carriage return character (0x0d).

`4.2.7`   Parameter string note

The parameter string includes all bytes from the separator to the
_{EOL}_, not including either the separator or the
_{EOL}_. ALL ASCII values from 0 - 0xFF are valid
in the parameter string which allows for binary payloads if proper
escaping is performed as detailed in [4.3 Delimiters and escaping](#elpg-delimiters "#elpg-delimiters").

## 4.3 Delimiters and escaping

The format described in the previous section, and the specific choice of
delimiters, removes the need for quotes surrounding parameters, and for other
delimiters between successive parameters. As a further benefit, this removes the
need for most escaping sequences with the exclusion of the ASCII characters
_{EOL}_ (0x0a or 0x0d) and backslash ('\').

`4.3.1`   _{EOL}_ in the parameter string (input escaping)

if a line feed character (0x0a) or carriage return character (0x0d) is
required in the parameter string, it must be replaced by the backslash escaped
sequence as follows:

`4.3.1.1`   Line feed is escaped as: 0x5C 0x41 or '\A'.

`4.3.1.2`   Carriage return is escaped as: 0x5C 0x44 or '\D'.

`4.3.2`   Backslash ('\') in the parameter string

Backslash (0x5C) in the parameter string is replaced by the escape sequence: 0x5C 0x5C ('\\').

`4.3.2.1`   All other combinations of the
escape sequence are illegal and the module returns 'ERR5 INVALID ESCAPE'.

`4.3.3`   Formatting and Parsing Errors

Parsing of a command is immediately terminated when the first formatting
error condition is detected. The module then discards the remainder of the
command input up to the closing EOL character and reports the appropriate
error code as indicated in [4.6 Command responses and error codes](#elpg-responses "#elpg-responses").

`4.3.4`   EOL in the command response (output escaping)

If a line feed character (0x0a) or a carriage return character (0x0d) is
present in a command response string, it is replaced by the backslash
escaped sequence as follows:

`4.3.4.1`   Line feed is escaped as: 0x5C 0x41 or '\A'.

`4.3.4.2`   Carriage return is escaped as: 0x5C 0x44 or '\D'.

`4.3.5`   Backslash ('\') in the command response

Backslash (0x5C, '\') in a command response is replaced by the escape
sequence: 0x5C, 0x5C or '\\'.

## 4.4 Maximum values

`4.4.1`   Maximum bytes in the formatted command string

The formatted command string as received by ExpressLink can be up to
9K bytes in length.

`**AT+**[ up to 9K bytes ]*{EOL}*`

`4.4.2`   Maximum command word size

The command word portion of the command string can be up to 32 bytes long.

## 4.5 Data processing

`4.5.1`   Data entry

The data entry for a command begins with the 'AT+' and ends with the
_{EOL}_. The module will not begin running a command
before it receives the _{EOL}_.

`4.5.2`   Data overflow

If the data buffer overflows during the data entry phase of a command,
the ExpressLink module continues to accept, but discards, the incoming
data until the next _{EOL}_ arrives.

`4.5.2.1`   The module returns 'ERR1 OVERFLOW'
and the entire message is discarded.

`4.5.3`   Data arriving after _{EOL}_

Any data that arrives after _{EOL}_ and before 'AT+'
will be ignored and discarded. Note that this includes multiple
_{EOL}_ characters–they will be ignored and discarded.

```
abcdefAT{EOL}         spurious characters preceding a command are ignored
OK{EOL}

AT{0x0a}{0x0d}{EOL}   line feed followed by carriage return
OK{EOL}

AT{0x0d}{0x0a}{EOL}   carriage return followed by line feed
OK{EOL}

AT{0x0d}{0x0d}{EOL}   multiple carriage returns
OK{EOL}

```

## 4.6 Command responses and error codes

All commands respond according to the response format described in section
[4.6.1 General response formats](#elpg-responses-formats "#elpg-responses-formats") when the
command is completed. In some cases, this can take a significant amount of time, but
under no circumstances longer than the _response timeout_ defined in
section [4.6.2 Response timeout](#elpg-response-timeout "#elpg-response-timeout").

### 4.6.1 General response formats

`**OK*[#]*|ERR***{#}{separator}[detail]{EOL}*`

Where:

**OK*[#]***

Indicates that the command was valid and ran correctly. The
optional numerical suffix `[#]`
indicates the number of additional output lines, with no additional
lines expected if this suffix is omitted.

**ERR*{#}***

Indicates the command was invalid or an error occurred while running
it. The required numerical suffix is an error code as defined in
[Table 1 - Error codes](#elpg-table1 "#elpg-table1") .

_{separator}_

Is a _single_ ASCII space character (ASCII 0x20).

_[detail]_

Is an optional ASCII string that contains the command response or
error description.

_{EOL}_

Is composed of a _carriage return_ (ASCII 0x0d)
followed by a _newline_ character (ASCII 0x0a).

`4.6.1.1`

A host application receiving an error response is recommended to
stop parsing any additional character (_detail_) past the error #
as those are meant to assist the user during debugging with a terminal
(unless it intends to present it on a user interface or display).

`4.6.1.2`

Similarly on a successful response, the _detail_ may consist of multiple parts.
To ensure future compatibility, a host application must stop parsing
past the required parts as documented in the current technical specification revision.

| Table 1 - Error codes | Code                     | ExpressLink text                                                                                                          | Description |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| 1                     | OVERFLOW                 | More bytes have been received than fit in the receive buffer.                                                             |
| 2                     | PARSE ERROR              | Message not formatted correctly.                                                                                          |
| 3                     | COMMAND NOT FOUND        | Invalid command.                                                                                                          |
| 4                     | PARAMETER ERROR          | Command does not recognize the parameters.                                                                                |
| 5                     | INVALID ESCAPE           | An incorrect escape sequence was detected.                                                                                |
| 6                     | NO CONNECTION            | Command requires an active connection to AWS IoT.                                                                         |
| 7                     | OUT OF RANGE             | The index provided is out of range (0 or greater than MaxTopic).                                                          |
| 8                     | PARAMETER UNDEFINED      | The key provided references an empty configuration parameter.                                                             |
| 9                     | INVALID KEY LENGTH       | Key is longer than 16 characters.                                                                                         |
| 10                    | INVALID KEY NAME         | A non-alphanumeric character was used in the key name.                                                                    |
| 11                    | UNKNOWN KEY              | The supplied key cannot be found in the system.                                                                           |
| 12                    | KEY READONLY             | The key cannot be written.                                                                                                |
| 13                    | KEY WRITEONLY            | The key cannot be read.                                                                                                   |
| 14                    | UNABLE TO CONNECT        | The module is unable to connect.                                                                                          |
| 15                    | TIME NOT AVAILABLE       | A time fix could not be obtained.                                                                                         |
| 16                    | LOCATION NOT AVAILABLE   | A location fix could not be obtained.                                                                                     |
| 17                    | MODE NOT AVAILABLE       | The requested mode is not available.                                                                                      |
| 18                    | ACTIVE CONNECTION        | An active connection prevents the command from running.                                                                   |
| 19                    | HOST IMAGE NOT AVAILABLE | A host OTA command was issued but no valid HOTA image is present in the<br>OTA buffer.                                    |
| 20                    | INVALID ADDRESS          | The OTA buffer pointer is out of bounds (> image size).                                                                   |
| 21                    | INVALID OTA UPDATE       | The OTA update failed.                                                                                                    |
| 22                    | [reserved]               |                                                                                                                           |
| 23                    | INVALID SIGNATURE        | A signature verification failed.                                                                                          |
| 24                    | SHADOW ERROR             | Shadow support disabled, not initialized, or request rejected.                                                            |
| 25                    | NOT ALLOWED              | The module cannot accept the command at this time (it is busy<br>or operating in a mode that conflicts with the request). |
| 26                    | INVALID CERTIFICATE      | The certificate was invalid or corrupted.                                                                                 |
| 27                    | BLE ERROR                | Any error related to failed execution of BLE commands.                                                                    |
| 28                    | CONFIGURATION ERROR      | When a command is entered but the correct configuration<br>is not set.                                                    |
| 29                    | INSUFFICIENT SECURITY    | When a subscription to a characteristic has insufficient security<br>levels.                                              |

###### Note

Refer to section [4.3 Delimiters and escaping](#elpg-delimiters "#elpg-delimiters")
for how special characters are escaped in the command response string.

### 4.6.2 Response timeout

The maximum runtime for every command must be listed in the module manufacturer's
datasheet. No command can take more than 120 seconds to complete (the maximum time
for a TCP connection timeout).

### 4.6.3 AT   »Communication test«

By sending only the 'AT' (attention) command, the host can verify the presence and readiness
of the module command parser.

Example:

```
AT*{EOL}*    # request the module's attention
```

###### Returns:

`OK*{EOL}*`

If the module is connected and the command parser active, then the
module returns 'OK'.

## 4.7 Power and connection control

### 4.7.1 CONNECT?   »Request the connection status«

Requests the current status of the connection to the AWS cloud and the device
onboarding state (see [21.3.2 ExpressLink onboarding
states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states "elpg-provisioning.md#elpg-provisioning-onboarding-states")).
The connection status indicates the completion of the entire sequence of actions
required for the module to connect and authenticate with the AWS cloud. The
onboarding state is determined by comparing the current Endpoint configuration
parameter (string) against the module default Endpoint (staging account) string
that is hardcoded as the factory reset value for the parameter (see the Endpoint
entry in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ).

###### Returns:

`OK *{status}{onboarded}*[CONNECTED/DISCONNECTED][STAGING/CUSTOMER]`

`4.7.1.1`   `OK 1 0 CONNECTED STAGING`

If the device is connected to the staging account, then the module returns
'OK 1 0 CONNECTED STAGING'.

`4.7.1.2`   `OK 0 0 DISCONNECTED STAGING`

If the device is not connected to the staging account, then the module returns
'OK 0 0 DISCONNECTED STAGING'.

`4.7.1.3`   `OK 1 1 CONNECTED CUSTOMER`

If the device is connected and onboarded (customer account), then the module returns
'OK 1 1 CONNECTED CUSTOMER'.

`4.7.1.4`   `OK 0 1 DISCONNECTED CUSTOMER`

If the device is not connected (customer account), then the module returns
'OK 0 1 DISCONNECTED CUSTOMER'.

### 4.7.2 CONNECT   »Establish a connection to an AWS IoT Core Endpoint«

Request a connection to the AWS IoT Core account, indicated by the endpoint configuration parameter.
This command activates the (wireless) connectivity features of the ExpressLink module and,
if successful, will bring the device to a higher power consumptions state.
If the configuration parameter LWTConfig is set (not empty) in the
[Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ,
a “last will and testament” is requested upon connecting to the MQTT broker using the LWTConfig options and the LWTMessage.

###### Note

This command is blocking. The connection process can require a long time during
which no further communication is possible with the module until one of the following
responses is returned to the host. (For a non-blocking option, see the asynchronous
command [4.7.8 CONNECT!   »Non-blocking request to connect to IoT Core«](#elpg-connect-nonblocking-command "#elpg-connect-nonblocking-command") .

###### Returns:

`4.7.2.1`   `OK 1 CONNECTED`

The module has successfully connected to AWS IoT Core.

`4.7.2.2`   `ERR14 *{#hint}* UNABLE TO CONNECT *[detail]*`

The module is unable to connect. Additional clues can be provided by
the mandatory _{#hint}_ numerical code and the
optional _[detail]_ field. The hint numerical codes
indicate the state of advancement of the connection process when the
failure occurred so that meaningful debugging tips can be provided in
the module documentation (including datasheets and FAQs). They are
numbered according to the following sequence of steps:

|     |                                                                                                                                                                                                                                                                                                                                                                                 |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  | **Backoff algorithm imposed delay**<br>(see 4.7.2.4)                                                                                                                                                                                                                                                                                                                            |
| 2.  | **Failed to access network**<br>– reported by a Wi-Fi module when it fails to<br>connect to a local access point/router or by a cellular<br>module if it fails to connect to the nearest cell tower.<br>TipCheck SSID/passphrase or local router state.<br>After this step the device is assumed to be able to<br>communicate over the network (it has obtained an IP address). |
| 3.  | **Failed to reach AWS endpoint**<br>– reported when the device fails to connect to an<br>AWS endpoint.<br>TipCheck the endpoint configuration parameter (URL)<br>After this step, the device is assumed to have reached an AWS server.                                                                                                                                          |
| 4.  | \*_Failed to securely authenticate with<br>AWS_<br>• – reported when the device fails<br>to upgrade the socket to a secure socket (TLS).<br>TipCheck if the AWS root certificate might have expired.<br>After this step, a secure socket is established with AWS.                                                                                                               |
| 5.  | **Failed to login AWS (MQTT) broker**<br>– reported when the MQTT login is unsuccessful<br>TipCheck if the device certificate is present in the customer<br>account registry.<br>After this step, the device should be able to issue MQTT commands.                                                                                                                             |
| 6.  | **Failed to register for Jobs**<br>– reported when the device fails to publish or<br>subscribe to standard AWS topics used for JOBS/OTA<br>(connection dropped by AWS server)<br>TipCheck policies attached to device certificate.<br>After this step, the device is connected and fully functional.                                                                            |

Different modules will interpret the hint codes according to the specific
wireless/networking stack that is applicable for the given technology and will
provide meaningful tips in the module documentation. Some of the steps might
not be applicable to all technologies (for example, the hint code for step 2
might not apply for a LoRA or Bluetooth module that transitions directly from
step 1 to 3). Similarly, additional intermediate hint codes can be provided using
dot notation, as applicable, to provide finer granularity (for example, a hint
code 5.1 can be added between step 5 and step 6).

`4.7.2.3`   `OK 1 CONNECTED`

If the ExpressLink module is _already connected_, issuing
a CONNECT command returns immediately with a success response ('OK 1 CONNECTED').

`4.7.2.4`   `ERR14 *{#hint}* UNABLE TO CONNECT *[detail]*`

In case of a connection failure, the ExpressLink module keeps a timestamp of
the event. This is used to ensure that a subsequent (repeated) connection
request complies with the correct _backoff timing_ limits.
If the request from the host is repeated too soon after the previous attempt
(the interval between requests is shorter than the prescribed minimum backoff
time), the ExpressLink module will return ERR14 with an appropriate hint code.
The necessary delay will increase according to the backoff algorithm until a
successful connection is established.

`4.7.2.5`   `ERR25 NOT ALLOWED*{EOL}*`

The CONNECT command cannot be issued when the device is in CONFMODE
or otherwise busy with activities that require conflicting resources.

Examples:

```
AT+CONNECT        # request to connect
OK 1 CONNECTED    # connection established successfully
```

Or

```
ERR14 3 UNABLE TO CONNECT Invalid Endpoint?    # Error detail and hint detail/tip provided
ERR14 5 UNABLE TO CONNECT                      # Hint code but no hint detail provided

```

Or

```
ERR25 NOT ALLOWED  # The command cannot be accepted until the asynchronous connection
                   #   attempt is completed successfully or otherwise
```

### 4.7.3 DISCONNECT   »Leave the connected state and enter the active state«

This command allows the host to prepare for a transition to low power (using
the SLEEP command), or to update the connection parameters before it attempts to
reconnect again with the changed parameters (using a new CONNECT
command).

###### Returns:

`4.7.3.1`   `OK 0 DISCONNECTED`

Note that if already disconnected, the command will return immediately with
a success value ('OK 0 DISCONNECTED').

`4.7.3.2`   Transitioning from a connected to a
not-connected state always produces a CONLOST event (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4 "elpg-event-handling.md#elpg-table4")) independently of the cause. For example, a CONLOST
event is produced as the result of the DISCONNECT command, when the server/endpoint
drops the connection, or when local wireless connectivity is lost.

### 4.7.4 SLEEP*[#] [duration]*   »Request to enter a low power mode«

This command forces the module to enter a low power mode. ExpressLink module
manufacturers can implement specific low power modes with different values
(_#_) that correspond to deeper sleep states (as capable)
to provide the lowest power consumption and longest possible battery life in
diverse applications and use cases. The
manufacturer documents the power consumption figures achievable in such modes
in the module datasheet.

`4.7.4.1`   The [duration] parameter

If present, this indicates the number of seconds before the module
awakes automatically.

`4.7.4.2`   Absence of duration

If the duration parameter is absent,
the module remains in low power mode until:

1. a hardware Reset is generated by the host lowering the
   **RST pin**.
2. a wakeup event is generated by the host lowering the
   **WAKE pin**.
3. a new AT command is sent by the host using the serial interface
   (this might not be possible in case of advanced (deep) sleep modes, see 4.7.4.4)

`4.7.4.3`   A SLEEP command without a numerical suffix defaults to mode 0.

Mode 0 is the default low power mode where the ExpressLink module reduces its power
consumption as much as possible while it still maintains the serial interface active and
preserves the contents of all configuration parameters.

`4.7.4.4`   Before entering SLEEP mode, the device will empty the event queue.

_Advanced low power modes_ can disable the
serial command interface. In these cases, in absence of the sleep duration
parameter, the only way to awaken the device is to apply an external reset
or wake signal. _Deep sleep_ states might cause loss of
part or all volatile (RAM) information, including all module state information
including configuration parameters that are not maintained in non-volatile
memory (for example, Topics). The host processor must _reconfigure_
such parameters as required by the application.

###### Returns:

`4.7.4.5`   `OK *{mode}*[*{detail}*]`

The device is ready and will proceed to the lower power mode selected
immediately after sending the reply (and flushing the serial port output).
{mode} indicates the sleep mode activated.

`4.7.4.6`   `ERR18 ACTIVE CONNECTION`

The device cannot transition to a low power mode because there is
an active cloud connection. Use the DISCONNECT command first to shut
down the connection.

`4.7.4.7`   Sleep mode fall back

When the host requests a SLEEP mode higher than any implemented on the
specific ExpressLink model, the module will fall back to the nearest/highest
mode available. (For example, SLEEP9, might fall back to SLEEP3 if mode 3 is
the highest available or simply SLEEP if no advanced modes are available.)
The actual sleep mode activated is reported in the response.

`4.7.4.8`   Upon returning to the active state,
a STARTUP event is generated and added to the event queue.

(See [8 Event handling](elpg-event-handling.md "elpg-event-handling.md").)

`4.7.4.9`   Sleep modes for devices supporting Bluetooth Low Energy (BLE)

Modules implementing the BLE API are expected to continue to offer
support for the BLE feature while in default low power mode (SLEEP,
SLEEP0)- BLE events are able to awaken the module. Advanced low power
modes (SLEEP1 and greater) can disable the BLE radio to further reduce
the power consumption of the device. Refer to the specific manufacturer’s
module datasheet to determine which modes are available and how they
affect the BLE functionality.

Example 1:

```
AT+SLEEP 100  # Disconnect and suspend all activities for 100 seconds
OK 0          # Enters sleep mode 0 (default)
AT+CONNECT    # Resume connection
```

Example 2:

```
AT+SLEEP9     # Request a deep sleep (proprietary mode) indefinitely
OK 3          # Enters nearest/deepest sleep mode available on this model
```

Note that the device might require a hardware reset/wake event to be re-awakened, and
all status (non-volatile) information might be lost requiring a new
initialization and configuration.

Example 3:

```
AT+SLEEP SOME TEXT
ERR4  PARAMETER ERROR     # a numerical value is expected for {duration}
```

Example 4:

```
AT+SLEEP9A
ERR4  PARAMETER ERROR     # a numerical value is expected for {mode}
```

### 4.7.5 CONFMODE *[parameter]*   »Activate modal credential entry«

Some ExpressLink modules require the user to enter private/local credentials
manually (for example, the Wi-Fi SSID and passphrase) or by means of a dedicated
(mobile) application. The host can request the ExpressLink module to enter a
special configuration mode (or CONFMODE, see [Figure 2](elpg-run-states.md#elpg-figure2 "elpg-run-states.md#elpg-figure2"))
to enable or repurpose an interface (such as BLE or Wi-Fi) to receive the user
input. Refer to the module manufacturer's datasheet for details specific to your
model.

**Example 1:** An ExpressLink Wi-Fi module could
use this command to enter a SoftAP mode, temporarily assume the role of an
Access Point, and serve an HTML form. This would allow the user to enter the
local Wi-Fi router credentials using a mobile device web browser. The optional
parameter could be used to provide a customized, unique SSID based on the device
UID.

**Example 2:** If a Bluetooth interface is
available, the ExpressLink module could receive the credentials using a serial
interface (SPP profile). For Bluetooth LE modules, this could be performed using
a dedicated (GATT) service using a custom mobile application.

###### Returns:

`4.7.5.1`   `OK CONFMODE ENABLED`

The device has entered CONFMODE and is ready to receive user input.

`4.7.5.2`   `ERR17 MODE NOT AVAILABLE`

This ExpressLink model/version does not support CONFMODE.

`4.7.5.3`   `ERR18 ACTIVE CONNECTION`

The device cannot enter CONFMODE because it is currently connected. The host must
disconnect first.

`4.7.5.4`   While in CONFMODE, an ExpressLink module can
still process all commands that do not require an active connection (for example,
'AT+CONF? Version').

`4.7.5.5`   Commands that require an active connection return
'ERR6 NO CONNECTION'. Attempting to issue a CONNECT command while in CONFMODE results in an
'ERR14 UNABLE TO CONNECT'.

`4.7.5.6`   The host may issue a RESET command at any time
to exit CONFMODE (see [Figure 2](elpg-run-states.md#elpg-figure2 "elpg-run-states.md#elpg-figure2")).

`4.7.5.7`   A CONFMODE notification event
(see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4 "elpg-event-handling.md#elpg-table4") is provided to the host
when the entry of new credentials has been completed. Only after that can the host issue
a new CONNECT command to attempt to establish a connection using the newly entered credentials.

### 4.7.6 RESET   »Request a full reset of the ExpressLink internal state«

This command disconnects the device (if connected) and resets its internal state. Non-persistent
configuration parameters (see [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3 "elpg-configuration-dictionary.md#elpg-table3") ) are
reinitialized, all subscriptions are terminated, and the message queue is emptied.

###### Returns:

`4.7.6.1`   `OK*{EOL}*`

If the command was successful, the module returns 'OK'.

`4.7.6.2`   A **STARTUP** event
is added to the event queue when the process is completed.

### 4.7.7 FACTORY_RESET   »Request a factory reset of the ExpressLink module«

This command performs a full factory reset of the ExpressLink module, including
re-initializing all non-persistent configuration parameters (see
[Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3 "elpg-configuration-dictionary.md#elpg-table3") ) and selected persistent
parameters (as indicated in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2")  
 in the Factory Reset column), and the message queue is emptied.

###### Returns:

`4.7.7.1`   `OK*{EOL}*`

If the command was successful, the module returns 'OK'.

`4.7.7.2`   A **STARTUP** event
is added to the event queue when the process is completed.

### 4.7.8 CONNECT!   »Non-blocking request to connect to IoT Core«

Request a connection to the AWS IoT Core account indicated by the endpoint configuration parameter.
This command activates the (wireless) connectivity features of the ExpressLink module and,
if successful, brings the device to a higher power consumptions state.
If the LWTConfig configuration parameter (see
[Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") )
is set (not empty), the “last will and testament” is requested
upon connecting to the MQTT broker using the LWTConfig options and LWTMessage.

###### Note

This command is non-blocking and immediately returns OK or an error as documented
below. However, it can take a long time for the connection process to complete, and until
it is complete, other power and connection control commands are rejected. Once the
connection is established, a CONNECT event is issued. (For a blocking option, see the
synchronous command [4.7.2 CONNECT   »Establish a connection to an AWS IoT Core Endpoint«](#elpg-connect-command "#elpg-connect-command") .

###### Returns:

`4.7.8.1`   `OK*{EOL}*`

The module has accepted the request and initiated the process to connect
to AWS IoT Core. Note that the connection process can require a significantly
long time.

`4.7.8.2`  

A CONNECT event is generated when
the process is completed or terminated with an error. A hint code is provided
as the event parameter (with the same interpretation provided in 4.7.2.2 for
the CONNECT ERR14 response). In case of success, the hint-code will be 0.

`4.7.8.3`  
If the ExpressLink module is already
connected, issuing a CONNECT! command will immediately produce a CONNECT event
with a success hint code (0).

`4.7.8.4`  

In case of a connection failure,
the ExpressLink module will keep a timestamp of the event. This will be used to
ensure that a subsequent (repeated) connection request will comply with the
correct backoff timing limits. If the request from the host is repeated too
soon after the previous attempt (a shorter interval than the prescribed minimum
backoff time) the ExpressLink module will produce a CONNECT event with the
Backoff hint code. Delays will increase according to the backoff algorithm
until a successful connection is established.

`4.7.8.5`   `ERR25 NOT ALLOWED*{EOL}*`

The device is in CONFMODE or a CONNECT! command is already in progress.
