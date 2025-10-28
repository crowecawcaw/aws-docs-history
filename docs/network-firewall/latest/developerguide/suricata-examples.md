# Examples of stateful rules for

Network Firewall

This section lists examples of Suricata compatible rules that could be used with AWS Network Firewall.

###### Note

Examples are not intended to be used in your Network Firewall configuration exactly as they are listed.

The examples provide general information and sample rule specifications
for common use cases. Before using any rule from these
examples or elsewhere, test and adjust it carefully to be
sure that it fits your needs. It's your responsibility to
ensure that each rule that you use is suited to your
specific use case and functioning the way that you want it
to.

## Stateful rules examples: allow traffic

###### Note

Before using any example rule, test and adapt it to your needs.

The examples in this section contain examples that allow specified traffic.

###### Allow access to any `ssm.` Server Name Indication (SNI) ending with `.amazonaws.com`

Allows access to any domain that begins with `ssm.` and ends with `.amazonaws.com` (http://amazonaws.com/).

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"ssm."; startswith; content:".amazonaws.com"; endswith; nocase; flow: to_server; sid:202308311;)
```

###### JA3 hash

This rule allows outbound access using a specific JA3 hash

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (msg:"Only allow Curl 7.79.1 JA3"; ja3.hash; content:"27e9c7cc45ae47dc50f51400db8a4099"; sid:12820009;)
```

###### Outbound requests to `checkip.amazonaws.com`

These rules only allow outbound requests to the SNI `checkip.amazonaws.com` (http://checkip.amazonaws.com/) if the server certificate issuer is also Amazon. Requires that your firewall policy uses strict order rule evaluation order.

```
alert tls $HOME_NET any -> $EXTERNAL_NET 443 (ssl_state:client_hello; tls.sni; content:"checkip.amazonaws.com"; endswith; nocase; xbits:set, allowed_sni_destination_ips, track ip_dst, expire 3600; noalert; sid:238745;)
pass tcp $HOME_NET any -> $EXTERNAL_NET 443 (xbits:isset, allowed_sni_destination_ips, track ip_dst; flow: stateless; sid:89207006;)
pass tls $EXTERNAL_NET 443 -> $HOME_NET any (tls.cert_issuer; content:"Amazon"; msg:"Pass rules do not alert"; xbits:isset, allowed_sni_destination_ips, track ip_src; sid:29822;)
reject tls $EXTERNAL_NET 443 -> $HOME_NET any (tls.cert_issuer; content:"="; nocase; msg:"Block all other cert issuers not allowed by sid:29822"; sid:897972;)
```

###### Outbound SSH/SFTP servers with `AWS_SFTP` banner

These rules only allow outbound access to SSH/SFTP servers that have a banner that includes `AWS_SFTP`, which is the banner for AWS Transfer Family servers. To check for a different banner, replace `AWS_SFTP` with the banner you want to check for.

```
pass tcp $HOME_NET any -> $EXTERNAL_NET 22 (flow:stateless; sid:2221382;)
pass ssh $EXTERNAL_NET 22 -> $HOME_NET any (ssh.software; content:"AWS_SFTP"; flow:from_server; sid:217872;)
drop ssh $EXTERNAL_NET 22 -> $HOME_NET any (ssh.software; content:!"@"; pcre:"/[a-z]/i"; msg:"Block unauthorized SFTP/SSH."; flow: from_server; sid:999217872;)

```

###### Send DNS query including `.amazonaws.com` to external DNS servers

This rule allows any DNS query for domain names ending in `.amazonaws.com` (http://amazonaws.com/) to be sent to external DNS servers.

```
pass dns $HOME_NET any -> $EXTERNAL_NET any (dns.query; dotprefix; content:".amazonaws.com"; endswith; nocase; msg:"Pass rules do not alert"; sid:118947;)
```

## Stateful rules examples: block traffic

###### Note

Before using any example rule, test and adapt it to your needs.

The examples in this section contain examples that block specified traffic.

###### Connections using TLS versions 1.0 or 1.1

This rule blocks connections using TLS version 1.0 or 1.1.

```
reject tls any any -> any any (msg:"TLS 1.0 or 1.1"; ssl_version:tls1.0,tls1.1; sid:2023070518;)
```

###### Multiple CIDR ranges

This rule blocks outbound access to multiple CIDR ranges in a single rule.

```
drop ip $HOME_NET any-> [10.10.0.0/16,10.11.0.0/16,10.12.0.0/16] (msg:"Block traffic to multiple CIDRs"; sid:278970;)
```

###### Multiple SNIs

This rule blocks multiple SNIs with a single rule.

```
reject tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; pcre:"/(example1\.com|example2\.com)$/i"; flow: to_server; msg:"Domain blocked"; sid:1457;)
```

###### Multiple high-risk destination outbound ports

This rule blocks multiple high-risk destination outbound ports in a single rule.

```
drop ip $HOME_NET any -> $EXTERNAL_NET [1389,53,4444,445,135,139,389,3389] (msg:"Deny List High Risk Destination Ports"; sid:278670;)
```

###### Outbound HTTP HOST

This rule blocks outbound HTTP connections that have an IP address in the HTTP `HOST` header.

```
reject http $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"."; pcre:"/^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/"; msg:"IP in HTTP HOST Header (direct to IP, likely no DNS resolution first)"; flow:to_server; sid:1239847;)
```

###### Outbound TLS with IP in SNI

This rule blocks outbound TLS connections with an IP address in the SNI.

```
reject tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"."; pcre:"/^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/"; msg:"IP in TLS SNI (direct to IP, likely no DNS resolution first)"; flow:to_server; sid:1239848;)
```

###### Any IP protocols other than TCP, UDP, and ICMP

This rule silently blocks any IP protocols other than TCP, UDP, and ICMP.

```
drop ip any any-> any any (noalert; ip_proto:!TCP; ip_proto:!UDP; ip_proto:!ICMP; sid:21801620;)
```

###### SSH non-standard ports

This rule blocks the use of the SSH protocol on non-standard ports.

```
reject ssh $HOME_NET any -> $EXTERNAL_NET !22 (msg:"Block use of SSH protocol on non-standard port"; flow: to_server; sid:2171010;)
```

###### TCP/22 servers non-SSH

This rule blocks the use of TCP/22 servers that aren't using the SSH protocol.

```
reject tcp $HOME_NET any -> $EXTERNAL_NET 22 (msg:"Block TCP/22 servers that are not SSH protocol"; flow: to_server; app-layer-protocol:!ssh; sid:2171009;)
```

## Stateful rules examples: log traffic

###### Note

Before using any example rule, test and adapt it to your needs.

The examples in this section demonstrate ways to log traffic. To log traffic, you must configure logging for your firewall. For information about logging Network Firewall traffic, see [Logging and monitoring in AWS Network Firewall](logging-monitoring.md "logging-monitoring.md").

###### Log traffic direction in default-deny policy

Can be used at the end of a default-deny policy to accurately log the direction of denied traffic. These rules help you to make it clear in the logs who the client is and who the server is in the connection.

```
reject tcp $HOME_NET any -> $EXTERNAL_NET any (msg:"Default Egress TCP block to server"; flow:to_server; sid:202308171;)
drop udp $HOME_NET any -> $EXTERNAL_NET any (msg:"Default Egress UDP block";sid:202308172;)
drop icmp $HOME_NET any -> $EXTERNAL_NET any (msg:"Default Egress ICMP block";sid:202308177;)
drop tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Default Ingress block to server"; flow:to_server; sid:20230813;)
drop udp $EXTERNAL_NET any -> $HOME_NET any (msg:"Default Ingress UDP block"; sid:202308174;)
drop icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"Default Ingress ICMP block"; sid:202308179;)

```

###### Log traffic to an allowed SNI

The `alert` keyword can be used in the pass rule to generate alert logs for all matches. This rule logs all passed traffic to an allowed SNI.

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:".example.com"; dotprefix; endswith; nocase; alert; sid:202307052;)
```

## Stateful rules examples: rule variables

###### Note

Before using any example rule, test and adapt it to your needs.

The following JSON defines an example Suricata compatible rule
group that uses the variables `HTTP_SERVERS` and
`HTTP_PORTS`, with the variable
definitions provided in the rule group declaration.

```
{
"RuleVariables": {
    "IPSets": {
        "HTTP_SERVERS": {
            "Definition": [
                "10.0.2.0/24",
                "10.0.1.19"
            ]
        }
    },
    "PortSets": {
        "HTTP_PORTS": {
            "Definition": ["80", "8080"]
        }
    }
},
"RulesSource": {
    "RulesString": "alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (msg:\".htpasswd access attempt\"; flow:to_server,established; content:\".htpasswd\"; nocase; sid:210503; rev:1;)"
}
}
```

The variable `EXTERNAL_NET` is a Suricata standard variable that
represents the traffic destination. For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-7.0.8/ "https://docs.suricata.io/en/suricata-7.0.8/").

## Stateful rules examples: IP set reference

###### Note

Before using any example rule, test and adapt it to your needs.

To reference a prefix list in your rule group, specify a IP set variable name and associate it with the prefix list's Amazon Resource Name (ARN). Then, specify the variable in one or more of your rules, prefacing the variable with `@`, such as `@IP_Set_Variable`. The variable represents the IPv4 prefix list that you are referencing. For more information about using IP set references, see [Referencing Amazon VPC prefix lists](rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists "rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists").

The following example shows a Suricata compatible rule that uses an IP set reference variable `@BETA` as the source port in `RulesString`. To use an IP set reference in your rule, you must use an `@` in front of the IP set variable name, such as `@My_IP_set_variable_name`.

```
{
   "RuleVariables":{
      "IPSets":{
         "HTTP_SERVERS":{
            "Definition":[
               "10.0.2.0/24",
               "10.0.1.19"
            ]
         }
      },
      "PortSets":{
         "HTTP_PORTS":{
            "Definition":[
               "80",
               "8080"
            ]
         }
      }
   },
   "ReferenceSets":{
      "IPSetReferences":{
         "BETA":{
            "ReferenceArn":"arn:aws:ec2:us-east-1:555555555555:prefix-list/pl-1111111111111111111_beta"
         }
      }
   },
   "RulesSource":{
      "RulesString":"drop tcp @BETA any -> any any (sid:1;)"
   }
}
```

## Stateful rules examples: Geographic IP filter

###### Note

Before using any example rule, test and adapt it to your needs.

For information about Geographic IP filtering in Network Firewall, see [Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups](rule-groups-geo-ip-filtering.md "rule-groups-geo-ip-filtering.md").

The following shows an example Suricata rule string that generates an alert for traffic to or from Russia:

```
alert ip any any -> any any (msg:"Geographic IP is from RU, Russia"; geoip:any,RU; sid:55555555; rev:1;)
```

The following shows an example standard stateful rule group that drops traffic unless it originates from the United States or
the United Kingdom:

```

{
    "RulesSource": {
      "StatefulRules": [
        {
          "Action": "DROP",
          "Header": {
            "DestinationPort": "ANY",
            "Direction": "FORWARD",
            "Destination": "ANY",
            "Source": "ANY",
            "SourcePort": "ANY",
            "Protocol": "IP"
          },
          "RuleOptions": [
            {
              "Settings": [
                "1"
              ],
              "Keyword": "sid"
            },
            {
              "Settings": [
                "src,!US,UK"
              ],
              "Keyword": "geoip"
            }
          ]
        }
      ]
    },
    "StatefulRuleOptions": {
       "RuleOrder": "STRICT_ORDER"
     }
 }
```

## Stateful rules examples: manage rule evaluation order

###### Note

Before using any example rule, test and adapt it to your needs.

The examples in this section demonstrate ways to modify
evaluation behavior by modifying rule evaluation order in
Suricata compatible rules. Network Firewall recommends using strict order so that you can have control over the way your rules are processed for evaulation. For information about managing rule evaluation order, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md").

Allow HTTP traffic to specific domains:

**Default action order**

```
drop tcp $HOME_NET any -> $EXTERNAL_NET 80 (msg:"Drop established TCP:80"; flow: from_client,established; sid:172190; priority:5; rev:1;)
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; priority:10; sid:172191; rev:1;)
pass tcp $HOME_NET any -> $EXTERNAL_NET 22 (msg:"Allow TCP 22"; sid:172192; rev:1;)
drop tcp $HOME_NET any -> $EXTERNAL_NET !80 (msg:"Drop All non-TCP:80";  sid:172193; priority:2; rev:1;)

```

**Strict order**

```
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; sid:172191; rev:1;)
pass tcp $HOME_NET any -> $EXTERNAL_NET 22 (msg:"Allow TCP 22"; sid:172192; rev:1;)

```

Allow HTTP traffic to specific domains only:

**Default action order**

```
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; priority:1; sid:102120; rev:1;)
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".mydomain.test"; endswith; msg:"Allowed HTTP domain"; priority:1; sid:102121; rev:1;)
drop http $HOME_NET any -> $EXTERNAL_NET 80 (msg:"Drop HTTP traffic"; priority:1; sid:102122; rev:1;)

```

**Strict order**

```
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; sid:102120; rev:1;)
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".mydomain.test"; endswith; msg:"Allowed HTTP domain"; sid:102121; rev:1;)
```

Allow HTTP traffic to specific domains only and deny all other
IP traffic:

**Default action order**

```
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; priority:1; sid:892120; rev:1;)
drop tcp $HOME_NET any -> $EXTERNAL_NET 80 (msg:"Drop established non-HTTP to TCP:80"; flow: from_client,established; sid:892191; priority:5; rev:1;)
drop ip $HOME_NET any <> $EXTERNAL_NET any (msg: "Drop non-TCP traffic."; ip_proto:!TCP;sid:892192; rev:1;)
drop tcp $HOME_NET any -> $EXTERNAL_NET !80 (msg:"Drop All non-TCP:80"; sid:892193; priority:2; rev:1;)

```

**Strict order**

```
pass http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; dotprefix; content:".example.com"; endswith; msg:"Allowed HTTP domain"; sid:892120; rev:1;)
pass tcp $HOME_NET any <> $EXTERNAL_NET 80 (flow:not_established; sid:892191; rev:1;)
```

## Stateful rules examples: domain list rules

###### Note

Before using any example rule, test and adapt it to your needs.

###### Deny list example JSON, rule group creation, and

generated Suricata rules

The following JSON shows an example rule definition
for a Network Firewall domain list rule group that
specifies a deny list.

```
{
    "RulesSource": {
        "RulesSourceList": {
            "Targets": [
                "evil.com"
            ],
            "TargetTypes": [
                 "TLS_SNI",
                 "HTTP_HOST"
             ],
             "GeneratedRulesType": "DENYLIST"
        }
    }
}
```

To use the Network Firewall rule specification, we save the JSON to a
local file `domainblock.example.json`, and then
create the rule group in the following CLI command:

```
aws network-firewall create-rule-group --rule-group-name "RuleGroupName" --type STATEFUL --rule-group file://domainblock.example.json --capacity 1000
```

The following Suricata rules listing shows the rules that
Network Firewall creates for the above deny list
specification.

```
drop tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"evil.com"; startswith; nocase; endswith; msg:"matching TLS denylisted FQDNs"; priority:1; flow:to_server, established; sid:1; rev:1;)
drop http $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"evil.com"; startswith; endswith; msg:"matching HTTP denylisted FQDNs"; priority:1; flow:to_server, established; sid:2; rev:1;)
```

###### HTTP allow list example JSON and generated Suricata

rules

The following JSON shows an example rule definition
for a Network Firewall domain list rule group that
specifies an HTTP allow list. The `.`
before the domain name in `.amazon.com`
is the wildcard indicator in Suricata.

```
{
    "RulesSource": {
        "RulesSourceList": {
            "Targets": [
                ".amazon.com",
                "example.com"
            ],
            "TargetTypes": [
                "HTTP_HOST"
            ],
            "GeneratedRulesType": "ALLOWLIST"
        }
    }
}
```

The following Suricata rules listing shows the rules that
Network Firewall creates for the above allow list specification.

```
pass http $HOME_NET any -> $EXTERNAL_NET any (http.host; dotprefix; content:".amazon.com"; endswith; msg:"matching HTTP allowlisted FQDNs"; priority:1; flow:to_server, established; sid:1; rev:1;)
pass http $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"example.com"; startswith; endswith; msg:"matching HTTP allowlisted FQDNs"; priority:1; flow:to_server, established; sid:2; rev:1;)
drop http $HOME_NET any -> $EXTERNAL_NET any (http.header_names; content:"|0d 0a|"; startswith; msg:"not matching any HTTP allowlisted FQDNs"; priority:1; flow:to_server, established; sid:3; rev:1;)
```

###### TLS allow list example JSON and generated Suricata

rules

The following JSON shows an example rule definition
for a Network Firewall domain list rule group that
specifies a TLS allow list.

```
{
    "RulesSource": {
        "RulesSourceList": {
            "Targets": [
                ".amazon.com",
                "example.com"
            ],
            "TargetTypes": [
                "TLS_SNI"
            ],
            "GeneratedRulesType": "ALLOWLIST"
        }
    }
}
```

The following Suricata rules listing shows the rules that
Network Firewall creates for the above allow list specification.

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; dotprefix; content:".amazon.com"; nocase; endswith; msg:"matching TLS allowlisted FQDNs"; priority:1; flow:to_server, established; sid:1; rev:1;)
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"example.com"; startswith; nocase; endswith; msg:"matching TLS allowlisted FQDNs"; priority:1; flow:to_server, established; sid:2; rev:1;)
drop tls $HOME_NET any -> $EXTERNAL_NET any (msg:"not matching any TLS allowlisted FQDNs"; priority:1; ssl_state:client_hello; flow:to_server, established; sid:3; rev:1;)
```

###### Block traffic from `$EXTERNAL_NET` to `$HOME_NET`, allow outbound domain filtering

These rules block all unsolicited traffic from `$EXTERNAL_NET` to `$HOME_NET` while still allowing outbound domain filtering.

```
reject tls any any -> any any (msg:"Vulnerable versions of TLS"; ssl_version:tls1.0,tls1.1; sid:2023070518;)
```

## Stateful rules examples: standard stateful rule groups

###### Note

Before using any example rule, test and adapt it to your needs.

The following JSON shows an example rule definition for a
Network Firewall basic stateful rule group.

```
{
    "RulesSource": {
        "StatefulRules": [
          {
            "Action": "DROP",
            "Header": {
                "Protocol": "HTTP",
                "Source": "$HOME_NET",
                "SourcePort": "ANY",
                "Direction": "ANY",
                "Destination": "$EXTERNAL_NET",
                "DestinationPort": "ANY"
            },
            "RuleOptions": [ {
                    "Keyword": "msg",
                    "Settings": [ "\"this is a stateful drop rule\""
                    ]
                },
                {
                    "Keyword": "sid",
                    "Settings": [ "1234"
                    ]
                }
            ]
        }
      ]
    }
}
```

The following Suricata rules listing shows the rules that
Network Firewall generates for the above deny list specification.

```
drop http $HOME_NET ANY <> $EXTERNAL_NET ANY (msg:this is a stateful drop rule; sid:1234;)
```

## Stateful rules example: allow traffic to a domain using its SNI

###### Note

Before using any example rule, test and adapt it to your needs.

The following set of rules will allow traffic to a domain using its SNI, while blocking traffic to all other domains in a strict order action policy.

```

# Drop all established to_server traffic (even TLS) from $HOME_NET to $EXTERNAL_NET
drop tcp $HOME_NET any -> $EXTERNAL_NET any (flow: to_server, established; sid:1;)

# This rule does not allow the traffic because it is already dropped by sid:1, but it does keep the dropped traffic from touching any other rules in the ruleset
pass tcp $HOME_NET any -> $EXTERNAL_NET any (flow: to_server, established; sid:11;)

# Allow all TLS from anywhere to anywhere if it's SNI is example.com
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"example.com"; dotprefix; nocase; flow: to_server, established; sid:2;)

```

## Stateful rules example: filter domains on http2

###### Note

Before using any example rule, test and adapt it to your needs.

The following set of rules will allow http2 traffic to `https://example.com` and block all other http2 traffic.

```

# Pass the domain with an http2 based rule
pass http2 $HOME_NET any -> $EXTERNAL_NET any (http.request_header; content:"authority|3a 20|example.com"; sid:1; rev:1;)

# Reject traffic for non-allowed TCP except http2
reject tcp $HOME_NET any -> $EXTERNAL_NET any (app-layer-protocol:!http2; flow:to_server, established; sid:2; rev:1;)

# Drop all other http2 decrypted traffic
drop http2 $HOME_NET any -> $EXTERNAL_NET any (flow:established, to_server; http2.header_name; content:"authority"; sid:3; rev:1;)

```
