# Contents of a AWS Network Firewall log

The Network Firewall logs contain the following information:

- **firewall_name** – The name of the
  firewall that's associated with the log entry.
- **availability_zone** – The
  Availability Zone of the firewall endpoint that generated the log
  entry.
- **event_timestamp** – The time that
  the log was created, written in epoch seconds at Coordinated Universal Time
  (UTC).
- **aws_category** – For rules using URL or Domain Category filtering, contains the matched categories in JSON array format. For example, ["Search Engines and Portals"] or ["Technology and Internet"].
- **event** – Detailed information about
  the event. This information includes the event timestamp converted to human
  readable format, event type, network packet details, and, if applicable,
  details about the stateful rule that the packet matched against.

      + **Alert and flow events** –
       Alert and flow events are produced by Suricata, the open source
       threat detection engine that the stateful rules engine runs on.
       Suricata writes the event information in the Suricata EVE JSON
       output format, with the exception of the AWS managed
       `tls_inspected` attribute.




      	- Flow log events use the EVE output type
      	 `netflow`. The log type `netflow`
      	 logs uni-directional flows, so each event represents traffic
      	 going in a single direction.
      	- Alert log events using the EVE output type
      	 `alert`.
      	- If the firewall that's associated with the log uses TLS
      	 inspection and the firewall's traffic uses SSL/TLS,
      	 Network Firewall adds the custom field `"tls_inspected":
      	 true` to the log. If your firewall doesn't use TLS
      	 inspection, Network Firewall omits this field.
      For detailed information about these Suricata events, see [EVE JSON Output](https://docs.suricata.io/en/suricata-7.0.8/output/eve/eve-json-output.html?highlight=EVE "https://docs.suricata.io/en/suricata-7.0.8/output/eve/eve-json-output.html?highlight=EVE") in the [Suricata User Guide](https://docs.suricata.io/en/suricata-7.0.8/index.html "https://docs.suricata.io/en/suricata-7.0.8/index.html").
      + **TLS events** – TLS events are produced by a
       dedicated stateful TLS engine, which is separate from Suricata. TLS events
       have the output type `tls`. The
       logs have a JSON structure that's similar to the Suricata EVE
       output.


      These events require the firewall to be configured for TLS inspection. For information,
       see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").


      TLS logs report the following types of errors:




      	- TLS errors, with the custom field `"tls_error":` containing the error details. Currently, this category includes Server Name Indication (SNI) mismatches and SNI naming errors. Typically these
      	 errors are caused by problems with customer traffic or with the
      	 customer's client or server. For example, errors caused
      	 when the client hello SNI is NULL or doesn't match the subject name
      	 in the server certificate.
      	- Revocation check errors, with the custom field `"revocation_check":` containing the check failure details. These report outbound traffic that fails
      	 the server certificate revocation check
      	 during TLS inspection. This requires the firewall to be configured
      	 with TLS inspection for outbound traffic, and for the TLS inspection
      	 to be configured to check the certificate revocation status.
      	 The logs include the revocation check status, the action taken, and the
      	 SNI that the revocation check was for.
      	 For information about configuring certificate revocation checking, see
      	 [Using
      	 SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall](tls-inspection-certificate-requirements.md "tls-inspection-certificate-requirements.md").

  For detailed information about these Suricata events, see [EVE JSON Output](https://docs.suricata.io/en/suricata-7.0.8/output/eve/eve-json-output.html?highlight=EVE "https://docs.suricata.io/en/suricata-7.0.8/output/eve/eve-json-output.html?highlight=EVE") in the [Suricata User Guide](https://docs.suricata.io/en/suricata-7.0.8/index.html "https://docs.suricata.io/en/suricata-7.0.8/index.html").

###### Example alert log entry

The following listing shows an example alert log entry for Network Firewall.

```
{
      "firewall_name":"test-firewall",
      "availability_zone":"us-east-1b",
      "event_timestamp":"1602627001",
      "event":{
          "timestamp":"2020-10-13T22:10:01.006481+0000",
          "flow_id":1582438383425873,
          "event_type":"alert",
          "src_ip":"203.0.113.4",
          "src_port":55555,
          "dest_ip":"192.0.2.16",
          "dest_port":111,
          "proto":"TCP",
          "alert":{
              "action":"allowed",
              "signature_id":5,
              "rev":0,
              "signature":"test_tcp",
              "category":"",
              "severity":1
          }
      }
  }
```

###### Example alert log entry with URL and Domain Category enabled

```
{
    "firewall_name": "test-firewall",
    "availability_zone": "us-east-1b",
    "event_timestamp": "1762217722",
    "event": {
        "aws_category": "[\"Search Engines and Portals\"]",
        "tx_id": 2,
        "app_proto": "http2",
        "src_ip": "10.0.100.55",
        "src_port": 54878,
        "event_type": "alert",
        "alert": {
            "severity": 3,
            "signature_id": 6,
            "rev": 0,
            "signature": "",
            "action": "blocked",
            "category": ""
        },
        "flow_id": 643336554233439,
        "dest_ip": "64.233.180.147",
        "proto": "TCP",
        "verdict": {
            "action": "drop"
        },
        "http": {
            "version": "2",
            "request_headers": [{
                "name": ":method",
                "value": "GET"
            }, {
                "name": ":scheme",
                "value": "https"
            }, {
                "name": ":authority",
                "value": "www.google.com"
            }, {
                "name": ":path",
                "value": "/"
            }, {
                "name": "user-agent",
                "value": "curl/8.11.1"
            }, {
                "name": "accept",
                "value": "*/*"
            }],
            "http_user_agent": "curl/8.11.1",
            "url": "/",
            "http_method": "GET",
            "http2": {
                "stream_id": 1,
                "request": {},
                "response": {}
            }
        },
        "dest_port": 443,
        "timestamp": "2025-12-31T00:55:22.870721+0000",
        "direction": "to_server"
    }
}
```

###### Example TLS log entry

The following listing shows an example TLS log entry for a failed certificate revocation check.

```
{
    "firewall_name": "egress-fw",
    "availability_zone": "us-east-1d",
    "event_timestamp": 1708361189,
    "event": {
        "src_ip": "10.0.2.53",
        "src_port": "55930",
        "revocation_check": {
            "leaf_cert_fpr": "1234567890EXAMPLE0987654321",
            "status": "REVOKED",
            "action": "DROP"
        },
        "dest_ip": "54.92.160.72",
        "dest_port": "443",
        "timestamp": "2024-02-19T16:46:29.441824Z",
        "sni": "revoked-rsa-dv.ssl.com"
    }
}
```

###### Example TLS log entry with URL and Domain Category enabled

```
{
    "firewall_name": "test-firewall",
    "availability_zone": "us-east-1b",
    "event_timestamp": "1763508615",
    "event": {
        "aws_category": "[\"Technology and Internet\"]",
        "tx_id": 0,
        "app_proto": "tls",
        "src_ip": "10.0.100.55",
        "src_port": 44474,
        "event_type": "alert",
        "alert": {
            "severity": 3,
            "signature_id": 6,
            "rev": 0,
            "signature": "",
            "action": "blocked",
            "category": ""
        },
        "flow_id": 1972143099170468,
        "dest_ip": "192.178.155.113",
        "proto": "TCP",
        "verdict": {
            "action": "drop"
        },
        "tls": {
            "sni": "developers.google.com",
            "version": "UNDETERMINED"
        },
        "dest_port": 443,
        "pkt_src": "geneve encapsulation",
        "timestamp": "2025-11-18T23:30:15.006867+0000",
        "direction": "to_server"
    }
}
```
