

# Configure the agent
<a name="configuring-agent"></a>

 After installing the agent you must update the agent configuration file at `/opt/aws/groundstation/etc/aws-gs-agent-config.json`. 

## Agent config file
<a name="agent-config-file"></a>

### Example
<a name="agent-config-file-example"></a>

```
{
  "capabilities": [
    "arn:aws:groundstation:eu-central-1:123456789012:dataflow-endpoint-group/bb6c19ea-1517-47d3-99fa-3760f078f100"
  ],
  "device": {
  "privateIps": [
    "127.0.0.1"
  ],
  "publicIps": [
    "1.2.3.4"
  ],
  "agentCpuCores": [ 24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92 ]
}
```

### Field breakdown
<a name="field-breakdown"></a>

#### capabilities
<a name="capabilities"></a>

Capabilities are specified as Dataflow Endpoint Group Amazon Resource Names.

**Required:** True

**Format:** String Array
+ Values: capability ARNs → String

Examples:

```
"capabilities": [
    "arn:aws:groundstation:${AWS::Region}:${AWS::AccountId}:dataflow-endpoint-group/${DataflowEndpointGroupId}"
]
```

#### device
<a name="device"></a>

This field contains additional fields necessary to enumerate the current EC2 “device”.

**Required:** True

**Format:** Object

Members:
+ privateIps
+ publicIps
+ agentCpuCores
+ networkAdapters

#### privateIps
<a name="private-ips"></a>

This field is currently not used, but is included for future use cases. If no value is included, it will default to [“127.0.0.1”]

**Required:** False

**Format:** String Array
+ Values: IP Addresses → String

Example:

```
"privateIps": [
    "127.0.0.1"
],
```

#### publicIps
<a name="public-ips"></a>

Elastic IP (EIP) per dataflow endpoint group.

**Required:** True

**Format:** String Array
+ Values: IP Addresses → String

Example:

```
"publicIps": [
    "9.8.7.6"
],
```

#### agentCPUCores
<a name="agent-cpu-cores"></a>

This specifies which virtual cores are reserved for the aws-gs-agent process. See [CPU core planning](agent-instance-selection.md#cpu-core-planning) for requirements to appropriately set this value. 

**Required:** True

**Format:** Int Array
+ Values: Core Numbers → int 

Example:

```
"agentCpuCores": [
    24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92
]
```

#### networkAdapters
<a name="network-adapters"></a>

This corresponds to the ethernet adapters, or interfaces attached to ENIs, that will receive data.

**Required:** False

**Format:** String Array
+ Values: ethernet adapter names (can find them by running `ip link show`) 

Example:

```
"networkAdapters": [
    "eth0"
]
```