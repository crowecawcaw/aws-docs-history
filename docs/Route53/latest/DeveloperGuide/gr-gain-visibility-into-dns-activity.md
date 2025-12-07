# Gain visibility into DNS activity with

Route 53 Global Resolver

Route 53 Global Resolver provides comprehensive DNS query logging capabilities to monitor client device
activity and identify security threats. Enable DNS query logging in Route 53 Global Resolver to see what
websites client devices access, identify potential security threats, and analyze DNS
resolution patterns. Logs capture comprehensive information about each query, including which
security policies were applied.

## What information is captured in DNS logs

Each DNS query log entry provides detailed information about client device activity and
security policy enforcement:

- **Query information** - Domain name, query type, query
  class, and protocol used
- **Client device information** - Source IP address, DNS
  view, and authentication method
- **Response information** - Response code, answer
  records, and response time
- **Security actions** - Firewall rule matches, threat
  detection results, and actions taken
- **Metadata** - Timestamp, global resolver ID, Region,
  and trace information

## OCSF format for security integration

DNS query logs use the Open Cybersecurity Schema Framework (OCSF), which provides a
standardized format for security event data. This format enables:

- **Standardized analysis** - Consistent schema across
  different security tools
- **Improved interoperability** - Easy integration with
  SIEM and analytics platforms
- **Enhanced correlation** - Ability to correlate DNS
  events with other security data
- **Future compatibility** - Support for evolving
  security analysis requirements

### OCSF log format examples

Route 53 Global Resolver DNS query logs follow the OCSF schema structure, providing detailed
information about each DNS query, response, and security action. The following examples
show the log format for allowed and denied queries.

#### Route 53 Global Resolver DNS log - Access allowed example

This example shows a DNS query that was allowed through firewall rules. The log
includes query details, response information, and enrichment data with Route 53 Global Resolver-specific
identifiers.

```
{
    "action_id": 1,
    "action_name": "Allowed",
    "activity_id": 6,
    "activity_name": "Traffic",
    "category_name": "Network Activity",
    "category_uid": 4,
    "class_name": "DNS Activity",
    "class_uid": 4003,
    "cloud": {
        "provider": "AWS",
        "region": "us-east-1",
        "account": {
            "uid": "123456789012"
        }
    },
    "connection_info": {
        "direction": "Inbound",
        "direction_id": 1,
        "protocol_name": "udp",
        "protocol_num": 17,
        "protocol_ver": "",
        "uid": "db21d1739ddb423a"
    },
    "duration": 1,
    "end_time": 1761358379996,
    "answers": [{
        "rdata": "3.3.3.3",
        "type": "A",
        "class": "IN",
        "ttl": 300
    },
    {
        "rdata": "3.3.3.4",
        "type": "A",
        "class": "IN",
        "ttl": 300
    }],
    "src_endpoint": {
        "ip": "3.3.3.1",
        "port": 56576
    },
    "enrichments": [{
        "name": "global-resolver",
        "value": "gr-a1b2c3d4fexample",
        "data": {
            "dns_view_id": "dnsv-a1b2c3d4fexample",
            "firewall_rule_id": "fr-a1b2c3d4fexample",
            "token_id": "t-a1b2c3d4fexample",
            "token_name": "device-123456",
            "token_expiration": "1789419206",
        }
    }],
    "message": "",
    "metadata": {
        "version": "1.2.0",
        "product": {
            "name": "Global Resolver",
            "vendor_name": "AWS",
            "feature": {
                "name": "DNS"
            }
        }
    },
    "query": {
        "hostname": "example.com.",
        "class": "IN",
        "type": "A",
        "opcode": "Query",
        "opcode_id": 0
    },
    "query_time": 1761358379995,
    "rcode": "NOERROR",
    "rcode_id": 0,
    "response_time": 1761358379995,
    "severity": "Informational",
    "severity_id": 1,
    "src_endpoint": {
        "ip": "3.3.3.3",
        "port": 28276
    },
    "start_time": 1761358379995,
    "status": "Success",
    "status_id": 1,
    "time": 1761358379995,
    "type_name": "DNS Activity: Traffic",
    "type_uid": 400306
}
```

#### Route 53 Global Resolver DNS log - Access denied example

This example shows a DNS query that was blocked by firewall rules. The log includes
the denial action, empty answers array, and REFUSED response code indicating the query
was not processed.

```
{
    "action_id": 2,
    "action_name": "Denied",
    "activity_id": 6,
    "activity_name": "Traffic",
    "category_name": "Network Activity",
    "category_uid": 4,
    "class_name": "DNS Activity",
    "class_uid": 4003,
    "cloud": {
        "provider": "AWS",
        "region": "us-west-2",
        "account": {
            "uid": "123456789012"
        }
    },
    "connection_info": {
        "direction": "Inbound",
        "direction_id": 1,
        "protocol_name": "tcp",
        "protocol_num": 6,
        "protocol_ver_id": 4,
        "uid": "9fdc6fbc09794d5e"
    },
    "duration": 1,
    "end_time": 1761358379996,
    "answers": [],
    "src_endpoint": {
        "ip": "3.3.3.3",
        "port": 28276
    },
    "enrichments": [
        {
            "name": "global-resolver",
            "value": "gr-a1b2c3d4fexample",
            "data": {
                "dns_view_id": "dnsv-a1b2c3d4fexample",
                "firewall_rule_id": "fr-a1b2c3d4fexample",
                "token_id": "t-a1b2c3d4fexample",
                "token_name": "device-123456",
                "token_expiration": "1789419206",
            }
        }
    ],
    "message": "",
    "metadata": {
        "version": "1.2.0",
        "product": {
            "name": "Global Resolver",
            "vendor_name": "AWS",
            "feature": {
                "name": "DNS"
            }
        }
    },
    "query": {
        "hostname": "example.com.",
        "class": "IN",
        "type": "A",
        "opcode": "Query",
        "opcode_id": 0
    },
    "query_time": 1761358379995,
    "rcode": "REFUSED",
    "rcode_id": 5,
    "response_time": 1761358379995,
    "severity": "Informational",
    "severity_id": 1,
    "start_time": 1761358379995,
    "status": "Failure",
    "status_id": 1,
    "time": 1761358379995,
    "type_name": "DNS Activity: Traffic",
    "type_uid": 400306
}
```
