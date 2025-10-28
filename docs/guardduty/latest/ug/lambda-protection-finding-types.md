# Lambda Protection finding types

This section describes the finding types that are specific to your AWS Lambda resources and
have the `resourceType` listed as `Lambda`. For all Lambda findings, we
recommend that you examine the resource in question and determine if it is behaving in an expected
manner. If the activity is authorized, you can use [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md") or [Trusted IP and threat
lists](guardduty_upload-lists.md "guardduty_upload-lists.md") to prevent false positive notifications for that resource.

If the activity is unexpected, the security best practice is to assume that Lambda has been
potentially compromised and follow the remediation recommendations.

###### Topics

- [Backdoor:Lambda/C&CActivity.B](#backdoor-lambda-ccactivity-b "#backdoor-lambda-ccactivity-b")
- [CryptoCurrency:Lambda/BitcoinTool.B](#cryptocurrency-lambda-bitcointool-b "#cryptocurrency-lambda-bitcointool-b")
- [Trojan:Lambda/BlackholeTraffic](#trojan-lambda-blackhole-traffic "#trojan-lambda-blackhole-traffic")
- [Trojan:Lambda/DropPoint](#trojan-lambda-drop-point "#trojan-lambda-drop-point")
- [UnauthorizedAccess:Lambda/MaliciousIPCaller.Custom](#unauthorized-access-lambda-maliciousIPcaller-custom "#unauthorized-access-lambda-maliciousIPcaller-custom")
- [UnauthorizedAccess:Lambda/TorClient](#unauthorized-access-lambda-tor-client "#unauthorized-access-lambda-tor-client")
- [UnauthorizedAccess:Lambda/TorRelay](#unauthorized-access-lambda-tor-relay "#unauthorized-access-lambda-tor-relay")

## Backdoor:Lambda/C&CActivity.B

### A Lambda function is querying an IP

address that is associated with a known command and control server.

**Default severity: High**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a listed Lambda function within your AWS environment is
querying an IP address that is associated with a known command and control (C&C) server.
The Lambda function associated to the generated finding is potentially compromised. C&C
servers are computers that issue commands to members of a botnet.

A botnet is a collection of internet-connected devices, which might include PCs, servers,
mobile devices, and Internet of Things devices, that is infected and controlled by a common
type of malware. Botnets are often used to distribute malware and gather misappropriated
information, such as credit card numbers. Depending on the purpose and structure of the botnet,
the C&C server might also issue commands to begin a distributed denial of service.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## CryptoCurrency:Lambda/BitcoinTool.B

### A Lambda function is querying

an IP address that is associated with a cryptocurrency-related activity.

**Default severity: High**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that the listed Lambda function in your AWS environment is
querying an IP address that is associated with a Bitcoin or other cryptocurrency-related
activity. Threat actors may seek to take control over Lambda functions in order to maliciously
repurpose them for unauthorized cryptocurrency mining.

**Remediation recommendations:**

If you use this Lambda function to mine or manage cryptocurrency, or this function is
otherwise involved in a blockchain activity, it is potentially an expected activity for your
environment. If this is the case in your AWS environment, we recommend that you set up a
suppression rule for this finding. The suppression rule should consist of two filter criteria.
The first criterion should use the finding type attribute with a value of
CryptoCurrency:Lambda/BitcoinTool.B. The second filter criterion should be the
Lambda function name of the function involved in blockchain activity. For information about
creating suppression rules, see [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

If this activity is unexpected, your Lambda function is potentially compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## Trojan:Lambda/BlackholeTraffic

### A Lambda function is attempting to

communicate with an IP address of a remote host that is a known black hole.

**Default severity: Medium**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a listed Lambda function within your AWS environment is
trying to communicate with an IP address of a black hole (or a sink hole). Black holes are
places in the network where incoming or outgoing traffic is silently discarded without
informing the source that the data didn't reach its intended recipient. A black hole IP address
specifies a host machine that is not running or an address to which no host has been assigned.
The listed Lambda function is potentially compromised.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## Trojan:Lambda/DropPoint

### A Lambda function is attempting to

communicate with an IP address of a remote host that is known to hold credentials and other
stolen data captured by malware.

**Default severity: Medium**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a listed Lambda function within your AWS environment is
trying to communicate with an IP address of a remote host that is known to hold credentials and
other stolen data captured by malware.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## UnauthorizedAccess:Lambda/MaliciousIPCaller.Custom

### A Lambda

function is making connections to an IP address on a custom threat list.

**Default severity: Medium**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a Lambda function in your AWS environment is communicating
with an IP address included on a threat list that you uploaded. In GuardDuty, a [threat list](guardduty_upload-lists.md "guardduty_upload-lists.md")
consists of known malicious IP addresses. GuardDuty generates findings based on the uploaded threat
lists. You can view the details of the threat list in the finding details on the GuardDuty
console.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## UnauthorizedAccess:Lambda/TorClient

### A Lambda function is making

connections to a Tor Guard or an Authority node.

**Default severity: High**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a Lambda function in your AWS environment is making
connections to a Tor Guard or an Authority node. Tor is
software
for enabling anonymous communication.
Tor
Guards and Authority node act as initial gateways into a Tor network. This
traffic can indicate that this Lambda function has been potentially compromised.
It
is now acting as a client on a Tor network.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").

## UnauthorizedAccess:Lambda/TorRelay

### A Lambda function is making

connections to a Tor network as a Tor relay.

**Default severity: High**

- **Feature:** Lambda Network Activity Monitoring

This finding informs you that a Lambda function in your AWS environment is making
connections to a Tor network in a manner that suggests that it's acting as a Tor relay. Tor is
software for enabling anonymous communication. Tor enables anonymous communication by
forwarding the client's potentially illicit traffic from one Tor relay to another.

**Remediation recommendations:**

If this activity is unexpected, your Lambda function may be compromised. For more
information, see [Remediating a potentially
compromised Lambda function](remediate-lambda-protection-finding-types.md "remediate-lambda-protection-finding-types.md").
