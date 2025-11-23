# Onboard your address range for use in Amazon EC2

The onboarding process for BYOIP includes the following tasks, depending on your needs.

###### Tasks

- [Provision a publicly advertisable address range in AWS](#byoip-provision "#byoip-provision")
- [Provision an IPv6 address range that's
  not publicly advertisable](#byoip-provision-non-public "#byoip-provision-non-public")
- [Advertise the address range through AWS](#byoip-advertise "#byoip-advertise")
- [Deprovision the address range](#byoip-deprovision "#byoip-deprovision")
- [Validate your BYOIP](#byoip-validation "#byoip-validation")

## Provision a publicly advertisable address range in AWS

When you provision an address range for use with AWS, you are confirming that
you control the address range and are authorizing Amazon to advertise it. We also
verify that you control the address range through a signed authorization message.
This message is signed with the self-signed X.509 key pair that you used when
updating the RDAP record with the X.509 certificate. AWS requires a
cryptographically signed authorization message that it presents to the RIR. The RIR
authenticates the signature against the certificate that you added to RDAP, and
checks the authorization details against the ROA.

###### To provision the address range

1. ###### Compose message

Compose the plaintext authorization message. The format of the message is
as follows, where the date is the expiry date of the message:

```
1|aws|`account`|`cidr`|`YYYYMMDD`|SHA256|RSAPSS
```

Replace the account number, address range, and expiry date with your own
values to create a message resembling the following:

```
text_message="1|aws|0123456789AB|198.51.100.0/24|20211231|SHA256|RSAPSS"
```

This is not to be confused with a ROA message, which has a similar
appearance. 2. ###### Sign message

Sign the plaintext message using the private key that you created
previously. The signature returned by this command is a long string that you
need to use in the next step.

###### Important

We recommend that you copy and paste this command. Except for the
message content, do not modify or replace any of the values.

```
signed_message=$( echo -n $text_message | openssl dgst -sha256 -sigopt rsa_padding_mode:pss -sigopt rsa_pss_saltlen:-1 -sign private-key.pem -keyform PEM | openssl base64 | tr -- '+=/' '-_~' | tr -d "\n")
```

3. ###### Provision address

Use the AWS CLI [provision-byoip-cidr](../../../cli/latest/reference/ec2/provision-byoip-cidr.md "../../../cli/latest/reference/ec2/provision-byoip-cidr.md") command to provision the address range.
The `--cidr-authorization-context` option uses the message and
signature strings that you created previously.

###### Important

You must specify the AWS Region where the BYOIP range should be
provisioned if it differs from your [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md")
`Default region name`.

```
aws ec2 provision-byoip-cidr --cidr `address-range` --cidr-authorization-context Message="$text_message",Signature="$signed_message" --region `us-east-1`
```

Provisioning an address range is an asynchronous operation, so the call
returns immediately, but the address range is not ready to use until its
status changes from `pending-provision` to
`provisioned`. 4. ###### Monitor progress

While most provisioning will be completed within two hours, it might take
up to one week to complete the provisioning process for publicly
advertisable ranges. Use the [describe-byoip-cidrs](../../../cli/latest/reference/ec2/describe-byoip-cidrs.md "../../../cli/latest/reference/ec2/describe-byoip-cidrs.md") command to monitor progress, as in this
example:

```
aws ec2 describe-byoip-cidrs --max-results 5 --region `us-east-1`
```

If there are issues during provisioning and the status goes to
`failed-provision`, you must run the
`provision-byoip-cidr` command again after the issues have
been resolved.

## Provision an IPv6 address range that's

not publicly advertisable

By default, an address range is provisioned to be publicly advertisable to the
internet. You can provision an IPv6 address range that will not be publicly
advertisable. For routes that are not publicly advertisable, the provisioning
process generally completes within minutes. When you associate an IPv6 CIDR block
from a non-public address range with a VPC, the IPv6 CIDR can only be accessed
through hybrid connectivity options that support IPv6, such as [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"), [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md"), or [Amazon VPC Transit Gateways](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md").

A ROA is not required to provision a non-public address range.

###### Important

- You can only specify whether an address range is publicly advertisable
  during provisioning. You cannot change the advertisable status later
  on.
- Amazon VPC doesn't support [unique
  local address](https://en.wikipedia.org/wiki/Unique_local_address "https://en.wikipedia.org/wiki/Unique_local_address") (ULA) CIDRs. All VPCs must have unique IPv6
  CIDRs. Two VPCs can’t have the same IPv6 CIDR range.

To provision an IPv6 address range that will not be publicly advertisable, use the
following [provision-byoip-cidr](../../../cli/latest/reference/ec2/provision-byoip-cidr.md "../../../cli/latest/reference/ec2/provision-byoip-cidr.md") command.

```
aws ec2 provision-byoip-cidr --cidr `address-range` --cidr-authorization-context Message="$text_message",Signature="$signed_message" --no-publicly-advertisable --region `us-east-1`
```

## Advertise the address range through AWS

After the address range is provisioned, it is ready to be advertised. You must
advertise the exact address range that you provisioned. You can't advertise only a
portion of the provisioned address range.

If you provisioned an IPv6 address range that will not be publicly advertised, you
do not need to complete this step.

We recommend that you stop advertising the address range or any portion of the range from other locations
before you advertise it through AWS. If you keep advertising your IP address range or any portion of it from other locations, we can't reliably support it or troubleshoot issues.
Specifically, we can't guarantee that traffic to the address range or a portion of the range will enter our
network.

To minimize down time, you can configure your AWS resources to use an address
from your address pool before it is advertised, and then simultaneously stop
advertising it from the current location and start advertising it through AWS. For
more information about allocating an Elastic IP address from your address pool, see
[Allocate an Elastic IP address](working-with-eips.md#using-instance-addressing-eips-allocating "working-with-eips.md#using-instance-addressing-eips-allocating").

###### Limitations

- You can run the **advertise-byoip-cidr** command at most
  once every 10 seconds, even if you specify different address ranges each
  time.
- You can run the **withdraw-byoip-cidr** command at most
  once every 10 seconds, even if you specify different address ranges each
  time.

To advertise the address range, use the following [advertise-byoip-cidr](../../../cli/latest/reference/ec2/advertise-byoip-cidr.md "../../../cli/latest/reference/ec2/advertise-byoip-cidr.md")
command.

```
aws ec2 advertise-byoip-cidr --cidr `address-range` --region `us-east-1`
```

To stop advertising the address range, use the following [withdraw-byoip-cidr](../../../cli/latest/reference/ec2/withdraw-byoip-cidr.md "../../../cli/latest/reference/ec2/withdraw-byoip-cidr.md")
command.

```
aws ec2 withdraw-byoip-cidr --cidr `address-range` --region `us-east-1`
```

## Deprovision the address range

To stop using your address range with AWS, first release any Elastic IP
addresses and disassociate any IPv6 CIDR blocks that are still allocated from the
address pool. Then stop advertising the address range, and finally, deprovision the
address range.

You cannot deprovision a portion of the address range. If you want to use a more
specific address range with AWS, deprovision the entire address range and
provision a more specific address range.

(IPv4) To release each Elastic IP address, use the following [release-address](../../../cli/latest/reference/ec2/release-address.md "../../../cli/latest/reference/ec2/release-address.md")
command.

```
aws ec2 release-address --allocation-id `eipalloc-12345678abcabcabc` --region `us-east-1`
```

(IPv6) To disassociate an IPv6 CIDR block, use the following [disassociate-vpc-cidr-block](../../../cli/latest/reference/ec2/disassociate-vpc-cidr-block.md "../../../cli/latest/reference/ec2/disassociate-vpc-cidr-block.md") command.

```
aws ec2 disassociate-vpc-cidr-block --association-id `vpc-cidr-assoc-12345abcd1234abc1` --region `us-east-1`
```

To stop advertising the address range, use the following [withdraw-byoip-cidr](../../../cli/latest/reference/ec2/withdraw-byoip-cidr.md "../../../cli/latest/reference/ec2/withdraw-byoip-cidr.md")
command.

```
aws ec2 withdraw-byoip-cidr --cidr `address-range` --region `us-east-1`
```

To deprovision the address range, use the following [deprovision-byoip-cidr](../../../cli/latest/reference/ec2/deprovision-byoip-cidr.md "../../../cli/latest/reference/ec2/deprovision-byoip-cidr.md") command.

```
aws ec2 deprovision-byoip-cidr --cidr `address-range` --region `us-east-1`
```

It can take up to a day to deprovision an address range.

## Validate your BYOIP

1. Validate the self-signed x.509 key pair

Validate that the certificate has been uploaded and is valid via the whois
command.

For ARIN, use `whois -h whois.arin.net r +
 `2001:0DB8:6172::/48``to look up the
 RDAP record for your address range. Check the`Public Comments` section for the`NetRange`(network range) in the command output. The
 certificate should be added in the`Public Comments` section for the
address range.

You can inspect the `Public Comments` containing the certificate
using the following command:

```
whois -h whois.arin.net r + `2001:0DB8:6172::/48` | grep Comments | grep BEGIN
```

This returns output with the contents of the key, which should be similar to
the following:

```
Public Comments:
-----BEGIN CERTIFICATE-----
MIID1zCCAr+gAwIBAgIUBkRPNSLrPqbRAFP8RDAHSP+I1TowDQYJKoZIhvcNAQE
LBQAwezELMAkGA1UEBhMCTloxETAPBgNVBAgMCEF1Y2tsYW5kMREwDwYDVQQHDA
hBdWNrbGFuZDEcMBoGA1UECgwTQW1hem9uIFdlYiBTZXJ2aWNlczETMBEGA1UEC
wwKQllPSVAgRGVtbzETMBEGA1UEAwwKQllPSVAgRGVtbzAeFw0yMTEyMDcyMDI0
NTRaFw0yMjEyMDcyMDI0NTRaMHsxCzAJBgNVBAYTAk5aMREwDwYDVQQIDAhBdWN
rbGFuZDERMA8GA1UEBwwIQXVja2xhbmQxHDAaBgNVBAoME0FtYXpvbiBXZWIgU2
VydmljZXMxEzARBgNVBAsMCkJZT0lQIERlbW8xEzARBgNVBAMMCkJZT0lQIERlb
W8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCfmacvDp0wZ0ceiXXc
R/q27mHI/U5HKt7SST4X2eAqufR9wXkfNanAEskgAseyFypwEEQr4CJijI/5hp9
prh+jsWHWwkFRoBRR9FBtwcU/45XDXLga7D3stsI5QesHVRwOaXUdprAnndaTug
mDPkD0vrl475JWDSIm+PUxGWLy+60aBqiaZq35wU/x+wXlAqBXg4MZK2KoUu27k
Yt2zhmy0S7Ky+oRfRJ9QbAiSu/RwhQbh5Mkp1ZnVIc7NqnhdeIW48QaYjhMlUEf
xdaqYUinzz8KpjfADZ4Hvqj9jWZ/eXo/9b2rGlHWkJsbhr0VEUyAGu1bwkgcdww
3A7NjOxQbAgMBAAGjUzBRMB0GA1UdDgQWBBStFyujN6SYBr2glHpGt0XGF7GbGT
AfBgNVHSMEGDAWgBStFyujN6SYBr2glHpGt0XGF7GbGTAPBgNVHRMBAf8EBTADA
QH/MA0GCSqGSIb3DQEBCwUAA4IBAQBX6nn6YLhz521lfyVfxY0t6o3410bQAeAF
08ud+ICtmQ4IO4A4B7zV3zIVYr0clrOOaFyLxngwMYN0XY5tVhDQqk4/gmDNEKS
Zy2QkX4Eg0YUWVzOyt6fPzjOvJLcsqc1hcF9wySL507XQz76Uk5cFypBOzbnk35
UkWrzA9KK97cXckfIESgK/k1N4ecwxwG6VQ8mBGqVpPpey+dXpzzzv1iBKN/VY4
ydjgH/LBfdTsVarmmy2vtWBxwrqkFvpdhSGCvRDl/qdO/GIDJi77dmZWkh/ic90
MNk1f38gs1jrCj8lThoar17Uo9y/Q5qJIsoNPyQrJRzqFU9F3FBjiPJF
-----END CERTIFICATE-----
```

For RIPE, use `whois -r -h whois.ripe.net
 `2001:0DB8:7269::/48``to look up the
 RDAP record for your address range. Check the`descr`section for the
`inetnum`object (network range) in the command output. The
 certificate should be added as a new`descr` field for the address
range.

You can inspect the `descr` containing the certificate using the
following command:

```
whois -r -h whois.ripe.net `2001:0DB8:7269::/48` | grep descr | grep BEGIN
```

This returns output with the contents of the key, which should be similar to
the following:

```
descr:
-----BEGIN CERTIFICATE-----MIID1zCCAr+gAwIBAgIUBkRPNSLrPqbRAFP8
RDAHSP+I1TowDQYJKoZIhvcNAQELBQAwezELMAkGA1UEBhMCTloxETAPBgNVBAg
MCEF1Y2tsYW5kMREwDwYDVQQHDAhBdWNrbGFuZDEcMBoGA1UECgwTQW1hem9uIF
dlYiBTZXJ2aWNlczETMBEGA1UECwwKQllPSVAgRGVtbzETMBEGA1UEAwwKQllPS
VAgRGVtbzAeFw0yMTEyMDcyMDI0NTRaFw0yMjEyMDcyMDI0NTRaMHsxCzAJBgNV
BAYTAk5aMREwDwYDVQQIDAhBdWNrbGFuZDERMA8GA1UEBwwIQXVja2xhbmQxHDA
aBgNVBAoME0FtYXpvbiBXZWIgU2VydmljZXMxEzARBgNVBAsMCkJZT0lQIERlbW
8xEzARBgNVBAMMCkJZT0lQIERlbW8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwg
gEKAoIBAQCfmacvDp0wZ0ceiXXcR/q27mHI/U5HKt7SST4X2eAqufR9wXkfNanA
EskgAseyFypwEEQr4CJijI/5hp9prh+jsWHWwkFRoBRR9FBtwcU/45XDXLga7D3
stsI5QesHVRwOaXUdprAnndaTugmDPkD0vrl475JWDSIm+PUxGWLy+60aBqiaZq
35wU/x+wXlAqBXg4MZK2KoUu27kYt2zhmy0S7Ky+oRfRJ9QbAiSu/RwhQbh5Mkp
1ZnVIc7NqnhdeIW48QaYjhMlUEfxdaqYUinzz8KpjfADZ4Hvqj9jWZ/eXo/9b2r
GlHWkJsbhr0VEUyAGu1bwkgcdww3A7NjOxQbAgMBAAGjUzBRMB0GA1UdDgQWBBS
tFyujN6SYBr2glHpGt0XGF7GbGTAfBgNVHSMEGDAWgBStFyujN6SYBr2glHpGt0
XGF7GbGTAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBX6nn6Y
Lhz521lfyVfxY0t6o3410bQAeAF08ud+ICtmQ4IO4A4B7zV3zIVYr0clrOOaFyL
xngwMYN0XY5tVhDQqk4/gmDNEKSZy2QkX4Eg0YUWVzOyt6fPzjOvJLcsqc1hcF9
wySL507XQz76Uk5cFypBOzbnk35UkWrzA9KK97cXckfIESgK/k1N4ecwxwG6VQ8
mBGqVpPpey+dXpzzzv1iBKN/VY4ydjgH/LBfdTsVarmmy2vtWBxwrqkFvpdhSGC
vRDl/qdO/GIDJi77dmZWkh/ic90MNk1f38gs1jrCj8lThoar17Uo9y/Q5qJIsoN
PyQrJRzqFU9F3FBjiPJF
-----END CERTIFICATE-----
```

For APNIC, use `whois -h whois.apnic.net
 `2001:0DB8:6170::/48``to look up the
 RDAP record for your BYOIP address range. Check the`remarks`section
 for the`inetnum`object (network range) in the command output. The
 certificate should be added as a new`remarks` field for the address
range.

You can inspect the `remarks` containing the certificate using the
following command:

```
whois -h whois.apnic.net `2001:0DB8:6170::/48` | grep remarks | grep BEGIN
```

This returns output with the contents of the key, which should be similar to
the following:

```
remarks:
-----BEGIN CERTIFICATE-----
MIID1zCCAr+gAwIBAgIUBkRPNSLrPqbRAFP8RDAHSP+I1TowDQYJKoZIhvcNAQE
LBQAwezELMAkGA1UEBhMCTloxETAPBgNVBAgMCEF1Y2tsYW5kMREwDwYDVQQHDA
hBdWNrbGFuZDEcMBoGA1UECgwTQW1hem9uIFdlYiBTZXJ2aWNlczETMBEGA1UEC
wwKQllPSVAgRGVtbzETMBEGA1UEAwwKQllPSVAgRGVtbzAeFw0yMTEyMDcyMDI0
NTRaFw0yMjEyMDcyMDI0NTRaMHsxCzAJBgNVBAYTAk5aMREwDwYDVQQIDAhBdWN
rbGFuZDERMA8GA1UEBwwIQXVja2xhbmQxHDAaBgNVBAoME0FtYXpvbiBXZWIgU2
VydmljZXMxEzARBgNVBAsMCkJZT0lQIERlbW8xEzARBgNVBAMMCkJZT0lQIERlb
W8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCfmacvDp0wZ0ceiXXc
R/q27mHI/U5HKt7SST4X2eAqufR9wXkfNanAEskgAseyFypwEEQr4CJijI/5hp9
prh+jsWHWwkFRoBRR9FBtwcU/45XDXLga7D3stsI5QesHVRwOaXUdprAnndaTug
mDPkD0vrl475JWDSIm+PUxGWLy+60aBqiaZq35wU/x+wXlAqBXg4MZK2KoUu27k
Yt2zhmy0S7Ky+oRfRJ9QbAiSu/RwhQbh5Mkp1ZnVIc7NqnhdeIW48QaYjhMlUEf
xdaqYUinzz8KpjfADZ4Hvqj9jWZ/eXo/9b2rGlHWkJsbhr0VEUyAGu1bwkgcdww
3A7NjOxQbAgMBAAGjUzBRMB0GA1UdDgQWBBStFyujN6SYBr2glHpGt0XGF7GbGT
AfBgNVHSMEGDAWgBStFyujN6SYBr2glHpGt0XGF7GbGTAPBgNVHRMBAf8EBTADA
QH/MA0GCSqGSIb3DQEBCwUAA4IBAQBX6nn6YLhz521lfyVfxY0t6o3410bQAeAF
08ud+ICtmQ4IO4A4B7zV3zIVYr0clrOOaFyLxngwMYN0XY5tVhDQqk4/gmDNEKS
Zy2QkX4Eg0YUWVzOyt6fPzjOvJLcsqc1hcF9wySL507XQz76Uk5cFypBOzbnk35
UkWrzA9KK97cXckfIESgK/k1N4ecwxwG6VQ8mBGqVpPpey+dXpzzzv1iBKN/VY4
ydjgH/LBfdTsVarmmy2vtWBxwrqkFvpdhSGCvRDl/qdO/GIDJi77dmZWkh/ic90
MNk1f38gs1jrCj8lThoar17Uo9y/Q5qJIsoNPyQrJRzqFU9F3FBjiPJF
-----END CERTIFICATE-----
```

2. Validate the creation of a ROA object

Validate the successful creation of the ROA objects using the RIPEstat Data
API. Be sure to test your address range against the Amazon ASNs 16509 and 14618,
plus the ASNs that are currently authorized to advertise the address
range.

You can inspect the ROA objects from different Amazon ASNs with your address
range by using the following command:

```
curl --location --request GET "https://stat.ripe.net/data/rpki-validation/data.json?resource=`ASN`&prefix=`CIDR`
```

In this example output, the response has a result of `"status":
 "valid"` for the Amazon ASN 16509. This indicates the ROA object for
the address range was created successfully:

```
{
    "messages": [],
    "see_also": [],
    "version": "0.3",
    "data_call_name": "rpki-validation",
    "data_call_status": "supported",
    "cached": false,
    "data": {
        "validating_roas": [
            {
                "origin": "16509",
                "prefix": "2001:0DB8::/32",
                "max_length": 48,
                "validity": "valid"
            },
            {
                "origin": "14618",
                "prefix": "2001:0DB8::/32",
                "max_length": 48,
                "validity": "invalid_asn"
            },
            {
                "origin": "64496",
                "prefix": "2001:0DB8::/32",
                "max_length": 48,
                "validity": "invalid_asn"
            }
        ],
        "status": "valid",
        "validator": "routinator",
        "resource": "16509",
        "prefix": "2001:0DB8::/32"
    },
    "query_id": "20230224152430-81e6384e-21ba-4a86-852a-31850787105f",
    "process_time": 58,
    "server_id": "app116",
    "build_version": "live.2023.2.1.142",
    "status": "ok",
    "status_code": 200,
    "time": "2023-02-24T15:24:30.773654"
}

```

A status of `“unknown”` indicates the ROA object for the address range has
not been created. A status of `“invalid_asn”` indicates that the ROA object
for the address range was not created successfully.
