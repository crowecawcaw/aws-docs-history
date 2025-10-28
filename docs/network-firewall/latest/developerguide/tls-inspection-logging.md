# Logging for TLS inspection in AWS Network Firewall

You can enable TLS logging for your firewall's stateful engine, to log some categories of events related to TLS inspection.
TLS logs report TLS errors and certificate revocation check failures for outbound traffic.
For information about enabling logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").

###### Log entries for TLS errors

TLS errors currently report connection resets that are due to SNI mismatches and naming errors. These are typically caused by problems with customer traffic or with the
customer's client or server. For example, when the client hello SNI is NULL or doesn't match the subject name
in the server certificate.

For this type of error, the TLS logs include the source and destination IPs and ports, the SNI, and the TLS error message.

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

The following example TLS log entry indicates a server name mismatch.

```
{
    "firewall_name": "test-firewall",
    "availability_zone": "us-east-1d",
    "event_timestamp": 1721849698,
    "event": {
        "timestamp": "2024-07-24T19:34:58.337042Z",
        "src_ip": "10.0.2.22",
        "src_port": "44798",
        "dest_ip": "91.212.12.80",
        "dest_port": "444",
        "sni": "test.com",
        "tls_error": {
            "error_message": "SNI: test.com Match Failed to server certificate names: aaacertificateservices.comodoca.com/aaacertificateservices.comodoca.com/www.aaacertificateservices.comodoca.com "
        }
    }
}

```

###### Log entries for certificate revocation check failures

These entries report outbound traffic that fails the server certificate revocation check
during TLS inspection. This log type requires the firewall to be configured
with TLS inspection for outbound traffic, and for the TLS inspection
to be configured to check the certificate revocation status.
For information about configuring certificate revocation checking, see
[Using
SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall](tls-inspection-certificate-requirements.md "tls-inspection-certificate-requirements.md")
and
[Checking certificate revocation status](tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status "tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status").

For revocation checks, the TLS logs report when servers that you're sending traffic to are failing the checks.
The logs include the revocation check status, the action taken, source and destination IPs and ports, and the SNI that the revocation check was for.
You can use this information to pinpoint the traffic that's experiencing failures and take measures to manage the problem.

In the following example TLS log entry, the revocation check reports that the certificate has been revoked, either by an Online Certificate Status Protocol (OCSP) or a Certificate Revocation Lists (CRL) provider. The certificate is not valid anymore. For this case, the firewall acts according to the configuration that you've specified for these checks. For this example, the action is `DROP`.

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

In the following example, the revocation check status is `UNKNOWN`. This can happen for a number of reasons, such as when the check encounters an error retrieving the data from the provider, or the provider not having any record of the certificate. Whatever the reason, the firewall isn't sure whether the certificate is revoked. The firewall again acts according to the configuration that you've specified for these checks.

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
            "status": "UNKNOWN",
            "action": "DROP"
        },
        "dest_ip": "54.92.160.72",
        "dest_port": "443",
        "timestamp": "2024-02-19T16:46:29.441824Z",
        "sni": "revoked-rsa-dv.ssl.com"
    }
}

```
