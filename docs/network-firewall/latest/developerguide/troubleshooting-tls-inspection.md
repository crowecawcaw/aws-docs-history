# Troubleshooting TLS inspection in AWS Network Firewall

Use the information here to help you diagnose common issues that you might encounter when working with TLS inspection in Network Firewall.

## Outbound TLS - Blocked connections to servers with revoked certificates

If you've enabled the certificate revocation status check for your outbound TLS workflow,
and your client starts getting blocked connections to a specific target server, use
one of the following procedures to determine whether the firewall has blocked the
connection based on the certificate revocation check action. For more information
about actions, see [Checking certificate revocation status](tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status "tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status").

The check differs depending on whether you have TLS logging enabled.

###### Troubleshooting with TLS logging enabled

When you have TLS logging enabled, you can read the TLS logs to determine
which servers are experiencing failed revocation checks.

1. Look in your TLS logs for records reporting the action, the certificate
   revocation check status, and the Server Name Indication (SNI) of the server
   whose certificate failed the revocation check.
2. Use the SNI from the logs to determine which target servers are
   experiencing the failed revocation checks.

Example output for a certificate that's been revoked by the server:

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

###### Troubleshooting without TLS logging

If you don't have TLS logs to refer to, follow these steps to determine which
servers are experiencing failed revocation checks.

1. Run a `curl` command from the client to the target server that has the blocked connection Note the output of the commands.

Example output for **Drop** action:

```
[root@ip-10-0-2-230 ~]# curl -ikv https://revoked-rsa-dv.ssl.com
*   Trying 54.92.160.72:443...
* Connected to revoked-rsa-dv.ssl.com (54.92.160.72) port 443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
...
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* TLSv1.3 (IN), TLS alert, close notify (256):
* Empty reply from server
* Closing connection
* TLSv1.3 (OUT), TLS alert, close notify (256):
curl: (52) Empty reply from server

```

Example output for **Reject** action:

```
[root@ip-10-0-2-230 ~]# curl -ikv https://revoked-rsa-dv.ssl.com
*   Trying 54.92.160.72:443...
* Connected to revoked-rsa-dv.ssl.com (54.92.160.72) port 443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
...
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Recv failure: Connection reset by peer
* OpenSSL SSL_read: Connection reset by peer, errno 104
* Closing connection
* Send failure: Broken pipe
curl: (56) Recv failure: Connection reset by peer
```

2. Switch the action from **Drop** to **Reject**, or vice versa depending on the action you originally configured.
3. Run the `curl` command again on the client, and note the output.
4. Compare the outputs before and after you changed the configured action. If the curl output with a **Reject** action shows `connection reset by server` and the output with **Drop** action doesn't, it implies that the firewall has determined the certificate for that TLS server has a revoked status, and has blocked the connection based on the configured action.

## Outbound TLS - Passing traffic for specific target server with revoked certificates by adjusting scope

You can pass traffic to hosts with revoked certificate by updating the scope configuration in your TLS inspection configuration. Because a service endpoint hostname might resolve and be served using more than one IP address, it's important to ensure that the list of destinations contain all of the CIDRs corresponding to the service being investigated. In the following example, the server name with the revoked certificate is `revoked-rsa-dv.ssl.com` with IP address `54.92.160.72/32`, and is associated with the scope configuration on a TLS configuration as follows:

```
{
  ...
    "Scopes": [{
      "Sources": [{"AddressDefinition": "0.0.0.0/0"}],
      "Destinations": [{"AddressDefinition": "54.92.160.72/32"}],
      "SourcePorts": [{"FromPort": 0, "ToPort": 65535}],
      "DestinationPorts": [{"FromPort": 443, "ToPort": 443}],
      "Protocols": [6]
    },{
      "Sources": [{"AddressDefinition": "0.0.0.0/0"}],
      "Destinations": [{"AddressDefinition": "55.0.0.1/24"}],
      "SourcePorts": [{"FromPort": 0, "ToPort": 65535}],
      "DestinationPorts": [{"FromPort": 443, "ToPort": 443}],
      "Protocols": [6]
    }]
  ...
}
```

When you update the scope configuration to not send traffic for that target through TLS inspection, you can exclusively pass that traffic for the revoked target though the stateful engine without changing to a global **Pass** action for all revocation check failures. This keeps the traffic in the remaining scopes, flowing through the TLS inspection, without the existing **Drop** or **Reject** actions.

```
{
  ...
    "Scopes": [{
      "Sources": [{"AddressDefinition": "0.0.0.0/0"}],
      "Destinations": [{"AddressDefinition": "55.0.0.1/24"}],
      "SourcePorts": [{"FromPort": 0, "ToPort": 65535}],
      "DestinationPorts": [{"FromPort": 443, "ToPort": 443}],
      "Protocols": [6]
    }]
  ...
}
```

For information about scope configurations, see [TLS inspection configuration settings in AWS Network Firewall](tls-inspection-settings.md "tls-inspection-settings.md").

You can verify your scope configuration changes using the alert or TLS logs. For
information about logging, see [Logging and monitoring in AWS Network Firewall](logging-monitoring.md "logging-monitoring.md").

###### Verify with TLS logs

Review the TLS logs to verify that the servers you've removed from the scope
of TLS inspection are no longer showing up. TLS logging reports revocation
check failures for outbound traffic and SNI mismatches and naming errors.

###### Verify with alert logs

Add an alert rule to match the SNI of the revoked certificate, like in the following
example.

Example rule:

```
alert tls any any -> 54.92.160.72 443 (msg:"revoked cert rule match"; tls.sni; content:"revoked-rsa-dv.ssl.com"; ssl_state:client_hello; sid:1;)
```

Example alert log:

```
{
  "firewall_name": "test-network-firewall",
  ...
  "event": {
    "timestamp": "2023-10-25T15:14:11.010637+0000",
    "app_proto": "tls",
    "proto": "TCP",
    "src_ip": "10.0.2.230",
    "src_port": 55784,
    "dest_ip": "54.92.160.72",
    "dest_port": 443,
    "event_type": "alert",
    "alert": {
      "severity": 1,
      "signature_id": 1,
      "signature": "revoked cert rule match",
      ...
    },
    "tls": {
      "subject": "CN=revoked-rsa-dv.ssl.com",
      "issuerdn": "C = US, ST = Texas, L = Houston, O = SSL Corporation, CN = SSL.com Root Certification Authority RSA",
       ...
    },
    ...
  }
}
```

## Troubleshooting connection issues with AWS service endpoints (including the AWS Systems Manager agent)

When TLS outbound inspection is enabled, depending on the firewall's VPC architecture, instances behind a firewall
might be unable to connect to some public AWS service endpoints (including Systems Manager). This can occur for the following common reasons.

- Some AWS service clients (and some other applications) can use an internal set of trusted root certificates
  that is different from the host operating system default trusted root certificates. This can cause certificate verification
  errors on the client for the certificate provided by the firewall in the TLS connection. To fix this, set the
  `AWS_CA_BUNDLE` environment variable on the client device to the directory that has the root certificate for
  the CA certificate that has been configured on the firewall for outbound inspection. For more information about this
  environment variable, see [AWS CLI
  supported environment variables](../../../cli/latest/userguide/cli-configure-envvars.md#envvars-list "../../../cli/latest/userguide/cli-configure-envvars.md#envvars-list") in the _AWS CLI Version 2 User Guide_. Alternately, add the `--ca-bundle` parameter to
  your CLI calls to avoid the issue.
- Additionally, because the firewall decrypts TLS traffic before stateful inspection, be sure
  that your firewall has [appropriate stateful rules](rule-group-stateful-creating.md "rule-group-stateful-creating.md") to allow decrypted HTTP (not TLS or HTTPS) traffic to reach the
  endpoints to which clients connect.

## Troubleshooting TLS - Connections dropping or resetting

When TLS inspection is enabled, if you experience connection drops, it's possible that the cause is TLS errors. You can
use the TLS logs to determine if this is the case and to troubleshoot the problems that are logged. To do this, enable TLS logs and then check the logs for TLS error entries.

In the following example TLS log entry, the error is in the client hello.

```
{
    "firewall_name": "firewall-tls-test",
    "availability_zone": "us-east-1d",
    "event_timestamp": 1719943304,
    "event": {
        "timestamp": "2024-07-02T18:01:44.412778Z",
        "src_ip": "10.0.2.53",
        "src_port": "59844",
        "dest_ip": "10.0.1.27",
        "dest_port": "443",
        "sni": "-",
        "tls_error": {
            "error_message": "Server name is not found in client hello."
        }
    }
}
```

For information about enabling TLS logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").

For more information about the logs for this type of error, see [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md "tls-inspection-logging.md").
