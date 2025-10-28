# Amazon DCV Session Manager Amazon DCV server - DNS mapping reference

The Amazon DCV Connection Gateway requires the Amazon DCV servers’ DNS names in order to connect to the DCV server instances.
This section illustrates how you can define a JSON file containing the mapping between each DCV Server
and its associated DNS name.

## File structure

The mapping consists of a list of JSON objects with the following fields:

```
[
	{
		“ServerIdType”: "Ip",
		“ServerId”: "192.168.0.1",
		“DnsNames”:
		{
			“InternalDnsName”: "internal"
		}
	},
	...
]
```

Where:

**`ServerIdType:`**

Identifies which type of id the value refers to; currently the available values are ipAddress, agentServerId, and instanceId:

**`Ip:`**

Available for both Amazon EC2 and on premise infrastructures; can be quickly retrieved by system administrators with an ifconfig (Linux)
or ipconfig (Windows) command. This info is also available in the DescribeServers API response.

**`Id:`**

Available for both Amazon EC2 and on premise infrastructures; the Session Manager Agent creates a new UUID every time the hostname
or the ip address changes. This info is available in the DescribeServers API response.

**`Host.Aws.Ec2InstanceId:`**

Available only for Amazon EC2 instances, it uniquely identifies a machine; it does not change after an instance reboot.
Can be retrieved on the host by contacting http://169.254.169.254/latest/meta-data/instance-id. This info is also available in the DescribeServers API response.

**`ServerId:`**

An Id of the specified type that uniquely identifies each Amazon DCV server in the network.

**`DnsNames:`**

The object containing the DNS names associated with the Amazon DCV server this object will contain:

**`InternalDnsNames:`**

The DNS name used by the Amazon DCV Connection Gateway to connect to the instance.

Please use the Session Manager Broker CLI commands `register-server-dns-mapping` to load the mapping from a file
(command page reference: [register-server-dns-mapping](register-server-dns-mappings.md "register-server-dns-mappings.md"))
and `describe-server-dns-mappings` to list the mappings currently loaded in the Session Manager Broker
(command page reference: [describe-server-dns-mappings](describe-server-dns-mappings.md "describe-server-dns-mappings.md")).

## Persistence

We strongly recommend that you enable the persistence feature of the Session Manager Broker, to protect against the mapping loss when multiple brokers or the entire cluster go down.
For more information about enabling data persistence, see [Configure Broker Persistence](configure_broker_persistence.md "configure_broker_persistence.md")
