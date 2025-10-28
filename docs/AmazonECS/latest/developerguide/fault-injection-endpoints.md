# Amazon ECS fault injection endpoints

The Amazon ECS container agent automatically injects the `ECS_AGENT_URI` environment variable
into the containers of Amazon ECS tasks to provide a method to interact with the container agent API
endpoint. Each endpoint includes a `/start`, `/stop`, and `/status`
endpoint. The endpoints only accept requests from tasks that have enabled fault injection, and each
endpoint has a rate limit of **1** request per **5** seconds per container. Exceeding this limit results in an error.

###### Note

Amazon ECS Agent `version 1.88.0+` is required to use the fault injection endpoints.

The three endpoints for use with fault injection are:

- [Network blackhole port endpoint](#fis-endpoint-blackhole-ports "#fis-endpoint-blackhole-ports")
- [Network packet loss endpoint](#fis-endpoint-packet-loss "#fis-endpoint-packet-loss")
- [Network latency endpoint](#fis-endpoint-latency "#fis-endpoint-latency")
  A successful request results in a response code of `200` with a message of
  `running` when you call the `/start` endpoint, `stopped` for the
  `/stop` endpoint, and `running` or `not-running` for the
  `/status` endpoint.

```
{
    "Status": <string>
}
```

An unsuccessful request returns one of the follow error codes:

- `400` ‐ Bad request
- `409` ‐ Fault injection request conflicts with another running fault
- `429` ‐ Request was throttled
- `500` ‐ Server had an unexpected error

```
{
	"Error":  <string message>
}
```

###### Note

Either one network latency fault or one network packet loss fault can be injected at a time.
Trying to inject more than one results in the request being rejected.

## Network blackhole port endpoint

The `{ECS_AGENT_URI}/fault/v1/network-blackhole-port` endpoint drops inbound or
outbound traffic for a specific port and protocol in a task's network namespace and is compatible
with two modes:

- **awsvpc** ‐ the changes are applied to the task
  network namespace
- **host** ‐ the changes are applied to the default
  network namespace container instance

### {ECS_AGENT_URI}/fault/v1/network-blackhole-port/start

This endpoint starts the network blackhole port fault injections and has the following
parameters:

###### Port

The specified port to use for the blackhole port fault injection.

Type: Integer

Required: Yes

###### Protocol

The protocol to use for the blackhole port fault injection.

Type: String

Valid values: `tcp | udp`

Required: Yes

###### TrafficType

The traffic type used by the fault injection.

Type: String

Valid values: `ingress | egress`

Required: Yes

###### SourcesToFilter

A JSON array of IPv4 or IPv6 addresses or CIDR blocks that are protected from the fault.

Type: Array of strings

Required: No

The following is an example request for using the `start` endpoint (replace the
`red` values with your own):

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-blackhole-port/start

Http method:POST

Request payload:
{
    "Port": `1234`,
    "Protocol": "tcp|udp",
    "TrafficType": "ingress|egress"
    "SourcesToFilter": ["`${IP1}", "${IP2}`", ...],
}
```

### {ECS_AGENT_URI}/fault/v1/network-blackhole-port/stop

This endpoint stops the fault specified in the request. This endpoint has the following
parameters:

###### Port

The port impacted by the fault that should be stopped.

Type: Integer

Required: Yes

###### Protocol

The protocol to use to stop the fault.

Type: String

Valid values: `tcp | udp`

Required: Yes

###### TrafficType

The traffic type used by the fault injection.

Type: String

Valid values: `ingress | egress`

Required: Yes

The following is an example request for using the `stop` endpoint (replace the
`red` values with your own):

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-blackhole-port/stop

Http method: POST

Request payload:
{
    "Port": `1234`,
    "Protocol": "tcp|udp",
    "TrafficType": "ingress|egress",
}
```

### {ECS_AGENT_URI}/fault/v1/network-blackhole-port/status

This endpoint is used to check the status of the fault injection. This endpoint has the
following parameters:

###### Port

The impacted port to check for the fault's status.

Type: Integer

Required: Yes

###### Protocol

The protocol to use when checking for the fault's status.

Type: String

Valid values: `tcp | udp`

Required: Yes

###### TrafficType

The traffic type used by the fault injection.

Type: String

Valid values: `ingress | egress`

Required: Yes

The following is an example request for using the `status` endpoint (replace the
`red` values with your own):

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-blackhole-port/status

Http method: POST

Request payload:
{
   "Port": `1234`,
   "Protocol": "tcp|udp",
   "TrafficType": "ingress|egress",
}
```

## Network latency endpoint

The `{ECS_AGENT_URI}/fault/v1/network-latency` endpoint adds delay and jitter to the
task's network interface for traffic to a specific sources. The endpoint is compatible with two
modes:

- **awsvpc** ‐ the changes are applied to the task
  network interface
- **host** ‐ the changes are applied to the default
  network interface

### {ECS_AGENT_URI}/fault/v1/network-latency/start

This `/start` endpoint begins the network latency fault injection and has the
following parameters:

###### DelayMilliseconds

The number of milliseconds of delay to add to the network interface to use for the fault
injection.

Type: Integer

Required: Yes

###### JitterMilliseconds

The number of milliseconds of jitter to add to the network interface to use for the fault
injection.

Type: Integer

Required: Yes

###### Sources

A JSON array of IPv4 or IPv6 addresses or CIDR blocks that are destination for use with fault
injection.

Type: Array of strings

Required: Yes

###### SourcesToFilter

A JSON array of IPv4 or IPv6 addresses or CIDR blocks that are protected from the fault.
`SourcesToFilter` takes priority over `Sources`.

Type: Array of strings

Required: No

The following is an example request for using the `/start` endpoint (replace the
`red` values with your own):

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-latency/start

Http method: POST

Request payload:
{
    "DelayMilliseconds": `123`,
    "JitterMilliseconds": `123`,
    "Sources": ["`${IP1}", "${IP2}`", ...],
    "SourcesToFilter": ["`${IP1}`", "`${IP2}`", ...],
}
```

### {ECS_AGENT_URI}/fault/v1/network-latency/stop and /status

The `{ECS_AGENT_URI}/fault/v1/network-latency/stop` endpoint stops the fault, and
the `{ECS_AGENT_URI}/fault/v1/network-latency/status` checks the fault's
status.

The following are two example requests for using the `/stop` and the
`/status` endpoints. Both use the `POST HTTP` method.

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-latency/stop
```

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-latency/status
```

## Network packet loss endpoint

The `{ECS_AGENT_URI}/fault/v1/network-packet-loss` endpoint adds packet loss to the
given network interface. This endpoint is compatible with two modes:

- **awsvpc** ‐ the changes are applied to the task
  network interface
- **host** ‐ the changes are applied to the default
  network interface

### {ECS_AGENT_URI}/fault/v1/network-packet-loss/start

This `/start` endpoint begins the network packet loss fault injection and has the
following parameters:

###### LossPercent

The percentage of packet loss

Type: Integer

Required: Yes

###### Sources

A JSON array of IPv4 or IPv6 addresses or CIDR blocks to use for the fault injection
tests.

Type: Array of strings

Required: Yes

###### SourcesToFilter

A JSON array of IPv4 or IPv6 addresses or CIDR blocks that are protected from the fault.
`SourcesToFilter` takes priority over `Sources`.

Type: Array of strings

Required: No

The following is an example request for using the `start` endpoint (replace the
`red` values with your own):

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-packet-loss/start

Http method: POST

{
    "LossPercent": `6`,
    "Sources": ["`${IP1}", "${IP2}`", ...],
    "SourcesToFilter": ["`${IP1}`", "`${IP2}`", ...],
}
```

### {ECS_AGENT_URI}/fault/v1/network-packet-loss/stop and /status

The `{ECS_AGENT_URI}/fault/v1/network-packet-loss/stop` endpoint stops the fault,
and the `{ECS_AGENT_URI}/fault/v1/network-packet-loss/status` checks the fault's
status. Only one of each type of fault is supported at a time.

The following are two example requests for using the `/stop` and the
`/status` endpoints. Both use the `POST HTTP` method.

```
Endpoint: ${ECS_AGENT_URI}/fault/v1/network-packet-loss/stop
```

```
Endpoint: ${{ECS_AGENT_URI}/fault/v1/network-packet-loss/status
```
