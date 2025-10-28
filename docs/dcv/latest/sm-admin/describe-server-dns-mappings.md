# describe-server-dns-mappings

Describe the currently available DCV Servers - DNS names mappings.

## Syntax

```
sudo -u root dcv-session-manager-broker describe-server-dns-mappings
```

## Output

**`serverIdType`**

The type of the server Id.

**`serverId`**

The unique ID of the Server.

**`dnsNames`**

The internal and external dns names

**`internalDnsNames`**

The internal dns names

**`externalDnsNames`**

The external dns names

## Example

The following example lists the registered DCV Servers - DNS names mappings.

**Command**

```
`sudo -u root dcv-session-manager-broker describe-server-dns-mappings`
```

**Output**

```
 [
	{
		"serverIdType" : "Id",
		"serverId" : "192.168.0.1",
		"dnsNames" : {
			"internalDnsName" : "internal1",
			"externalDnsName" : "external1"
		}
	},
	{
		"serverIdType" : "Host.Aws.Ec2InstanceId",
		"serverId" : "i-0648aee30bc78bdff",
		"dnsNames" : {
			"internalDnsName" : "internal2",
			"externalDnsName" : "external2"
		}
	}
 ]
```
