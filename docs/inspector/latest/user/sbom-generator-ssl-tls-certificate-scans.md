# Amazon Inspector SBOM Generator SSL/TLS certificate scans

This section describes how to use the Amazon Inspector SBOM Generator to inventory SSL/TLS certificates.
The Sbomgen inventories SSL/TLS certificates by searching for certificates in predefined locations as well as directories provided by the user.
The feature is intended to enable users to inventory SSL/TLS certificates as well as identify expired certificates.
CA certificates will also appear in the output inventory.

## Using Sbomgen certificate scans

You can enable SSL/TLS certificate inventory collection using the `--scanners certificates` argument.
Certificate scans can be combined with any of the other scanners.
By default, certificate scans are not enabled.

The Sbomgen searches different locations for certificates depending on the artifact being scanned.
In all cases, the Sbomgen attempts to extract certificates in files with the following extensions.

```
.pem
.crt
.der
.p7b
.p7m
.p7s
.p12
.pfx
```

###### The localhost artifact type

If the certificate scanner is enabled and the artifact type is localhost, the Sbomgen recursively looks for certificates in `/etc/*/ssl`, `/opt/*/ssl/certs`, `/usr/local/*/ssl`, and `/var/lib/*/certs`, where `*` is not empty.
User-provided directories will be searched recursively, regardless of what directories are named.
Typically, CA/system certificates are not placed in these paths.
These certificates are often in folders named `pki`, `ca-certs`, or `CA`.
They also may appear in the default localhost scan paths.

###### Directory and container artifacts

When scanning directory or container artifacts, the Sbomgen searches for certificates located anywhere on the artifact.

###### Example certificate scan commands

The following contains example certificate scan commands.
One generates an SBOM that only contains certificates in a local directory.
Another generates an SBOM that contains certificates and Alpine, Debian, and Rhel packages in a local directory.
Another generates an SBOM that contains certificates found in common certificate locations.

```
# generate SBOM only containing certificates in a local directory
./inspector-sbomgen directory --path ./project/ --scanners certificates

# generate SBOM only containing certificates and Alpine, Debian, and Rhel OS packages in a local directory
./inspector-sbomgen directory --path ./project/ --scanners certificates,dpkg,alpine-apk,rhel-rpm

# generate SBOM only containing certificates, taken from common localhost certificate locations
./inspector-sbomgen localhost --scanners certificates
```

###### Example file component

The following contains two example certificate finding components.
When a certificate expires, you can view an extra property that identifies the expiration date.

```
{
      "bom-ref": "comp-2",
      "type": "file",
      "name": "certificate:expired.pem",
      "properties": [
            {
                "name": "amazon:inspector:sbom_generator:certificate_finding:IN-CERTIFICATE-001",
                "value": "expired:2015-06-06T11:59:59Z"
            },
            {
                "name": "amazon:inspector:sbom_generator:source_path",
                "value": "/etc/ssl/expired.pem"
            }
      ]
},
{
      "bom-ref": "comp-3",
      "type": "file",
      "name": "certificate:unexpired.pem",
      "properties": [
            {
                "name": "amazon:inspector:sbom_generator:source_path",
                "value": "/etc/ssl/unexpired.pem"
            }
      ]
}
```

###### Example vulnerability response component

Running the Amazon Inspector SBOM Generator with the `--scan-sbom` flag sends the resulting SBOM to Amazon Inspector for vulnerability scanning.
The following is an example of a certificate finding for a vulnerability response component.

```
{
    "advisories": [
        {
            "url": "https://aws.amazon.com/inspector/"
        },
        {
            "url": "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html"
        }
    ],
    "affects": [
        {
            "ref": "comp-2"
        }
    ],
    "analysis": {
        "state": "in_triage"
    },
    "bom-ref": "vuln-1",
    "created": "2025-04-17T18:48:20Z",
    "cwes": [
        324,
        298
    ],
    "description": "Expired Certificate: The associated certificate(s) are no longer valid. Replace certificate in order to reduce risk.",
    "id": "IN-CERTIFICATE-001",
    "properties": [
        {
            "name": "amazon:inspector:sbom_scanner:priority",
            "value": "standard"
        },
        {
            "name": "amazon:inspector:sbom_scanner:priority_intelligence",
            "value": "unverified"
        }
    ],
    "published": "2025-04-17T18:48:20Z",
    "ratings": [
        {
            "method": "other",
            "severity": "medium",
            "source": {
                "name": "AMAZON_INSPECTOR",
                "url": "https://aws.amazon.com/inspector/"
            }
        }
    ],
    "source": {
        "name": "AMAZON_INSPECTOR",
        "url": "https://aws.amazon.com/inspector/"
    },
    "updated": "2025-04-17T18:48:20Z"
}
```
