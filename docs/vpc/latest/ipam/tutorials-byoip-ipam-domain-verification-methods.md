# Verify domain

control

Before you bring an IP address range to AWS, you have to use one of the options
described in this section to verify that you control the IP address space. Later, when
you bring the IP address range to AWS, AWS validates that you control the IP address
range. This validation ensures that customers cannot use IP ranges belonging to others,
preventing routing and security issues.

There are two methods that you can use to verify that you control the range:

- **X.509 certificate**: If your IP address
  range is registered with an Internet Registry that supports RDAP (such as ARIN,
  RIPE and APNIC), you can use an X.509 certificate to verify ownership of your
  domain.
- **DNS TXT record**: Regardless of whether
  your Internet Registry supports RDAP, you can use a verification token and a DNS
  TXT record to verify ownership of your domain.

###### Contents

- [Verify your domain with an X.509 certificate](#tutorials-byoip-ipam-domain-verification-cert "#tutorials-byoip-ipam-domain-verification-cert")
- [Verify your domain with a DNS TXT record](#tutorials-byoip-ipam-domain-verification-dns-txt "#tutorials-byoip-ipam-domain-verification-dns-txt")

## Verify your domain with an X.509 certificate

This section describes how to verify your domain with an X.509 certificate before you bring your IP address range to IPAM.

###### To verify your domain with an X.509 certificate

1. Complete the three steps in [Prerequisites for BYOIP in Amazon EC2](../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md "../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md") in the _Amazon EC2 User Guide_.

###### Note

When you create the ROAs, for IPv4 CIDRs
you must set the maximum length of an IP address prefix to `/24`. For IPv6 CIDRs,
if you are adding them to an advertisable pool, the maximum length of an IP address prefix must
be `/48`. This ensures that you have full flexibility to divide
your public IP address across AWS Regions. IPAM enforces the maximum length you set.
The maximum length is the smallest prefix length announcement you will allow for this
route. For example, if you bring a `/20` CIDR block to AWS, by setting the
maximum length to `/24`, you can divide the larger block any way you like
(such as with `/21`, `/22`, or `/24`) and distribute
those smaller CIDR blocks to any Region. If you were to set the maximum length to
`/23`, you would not be able to divide and advertise a `/24` from the larger
block. Also, note that `/24` is the smallest IPv4 block and `/48`
is the smallest IPv6 block you can advertise from a Region to the internet. 2. Complete steps 1 and 2 only under [Provision a
publicly advertisable address range in AWS](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-provision "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-provision") in the
_Amazon EC2 User Guide_, **and
don't provision the address range (step 3) yet**. Save the
`text_message` and `signed_message`. You'll need
them later in this process.

When you've completed these steps, continue with [Bring your own IP to IPAM using both the AWS Management Console and the AWS CLI](tutorials-byoip-ipam-console-intro.md "tutorials-byoip-ipam-console-intro.md") or [Bring your own IP CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-cli-only-intro.md "tutorials-byoip-ipam-cli-only-intro.md").

## Verify your domain with a DNS TXT record

Complete the steps in this section to verify your domain with a DNS TXT record
before you bring your IP address range to IPAM.

You can use DNS TXT records to validate that you control a public IP address
range. DNS TXT records are a type of DNS record that contain information about your
domain name. This feature enables you to bring IP addresses registered with any
internet registry (such as JPNIC, LACNIC, and AFRINIC), not just those that support
RDAP (Registration Data Access Protocol) record-based validations (such as ARIN,
RIPE and APNIC).

###### Important

Before you can continue, you must have already created an IPAM in the Free or Advanced Tier.
If you don’t have an IPAM, complete [Create an IPAM](create-ipam.md "create-ipam.md") first.

###### Contents

- [Step 1: Create a ROA if you don't have one](#tutorials-byoip-ipam-domain-verification-dns-txt-roa "#tutorials-byoip-ipam-domain-verification-dns-txt-roa")
- [Step 2. Create a verification token](#tutorials-byoip-ipam-domain-verification-dns-txt-token "#tutorials-byoip-ipam-domain-verification-dns-txt-token")
- [Step 3. Set up the DNS zone and TXT record](#tutorials-byoip-ipam-domain-verification-dns-txt-dns "#tutorials-byoip-ipam-domain-verification-dns-txt-dns")

### Step 1: Create a ROA if you don't have one

You must have a Route Origin Authorization (ROA) in your Regional Internet
Registry (RIR) for IP address ranges you wish to advertise. If you don’t have a
ROA in your RIR, complete [3.
Create a ROA object in your RIR](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-create-roa-object "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-create-roa-object") in the
_Amazon EC2 User Guide_. Ignore the other steps.

The most specific IPv4 address range that you can bring is /24. The most
specific IPv6 address range that you can bring is /48 for CIDRs that are
publicly advertisable and /60 for CIDRs that are not publicly
advertisable.

### Step 2. Create a verification token

A verification token is an AWS-generated random value that you can use to prove control of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to AWS (BYOIP).

Complete the steps in this section to create a verification token which you'll
need in a later step in this tutorial to bring your IP address range to IPAM. Use the instructions below
for either the AWS console or the AWS CLI.

AWS Management Console

###### To create a verification token

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the AWS Management Console, choose the AWS Region where you created your IPAM.
3. In the left navigation pane, choose **IPAMs**.
4. Choose your IPAM and then choose the **Verification tokens tab**.
5. Select **Create verification token**.
6. After you create the token, leave this browser tab open. You’ll need the **Token value**, **Token name** in the next step and the **Token ID** in a later step.

Note the following:

- Once you create a verification token, you can reuse the token for multiple BYOIP CIDRs that you provision from your IPAM within 72 hours. If you want to provision more CIDRs after 72 hours, you need a new token.
- You can create up to 100 tokens. If you reach the limit, delete expired tokens.

Command line

- Request that IPAM creates a verification token that you will use for the DNS configuration
  with [create-ipam-external-resource-verification-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-external-resource-verification-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-external-resource-verification-token.html"):

```
aws ec2 create-ipam-external-resource-verification-token --ipam-id ipam-id

```

This will return an IpamExternalResourceVerificationTokenId and token with `TokenName` and `TokenValue`, and the expiration time (`NotAfter`) of the token.

```
{
    "IpamExternalResourceVerificationToken": {
        "IpamExternalResourceVerificationTokenId": "ipam-ext-res-ver-token-0309ce7f67a768cf0",
        "IpamId": "ipam-0f9e8725ac3ae5754",
        "TokenValue": "a34597c3-5317-4238-9ce7-50da5b6e6dc8",
        "TokenName": "86950620",
        "NotAfter": "2024-05-19T14:28:15.927000+00:00",
        "Status": "valid",
        "Tags": [],
        "State": "create-in-progress" }
}
```

Note the following:

- Once you create a verification token, you can reuse the token for multiple BYOIP CIDRs that you provision from your IPAM within 72 hours. If you want to provision more CIDRs after 72 hours, you need a new token.
- You can view your tokens using [describe-ipam-external-resource-verification-tokens](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-external-resource-verification-tokens.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-external-resource-verification-tokens.html").
- You can create up to 100 tokens. If you reach the limit, you can delete expired tokens using [delete-ipam-external-resource-verification-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam-external-resource-verification-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam-external-resource-verification-token.html").

### Step 3. Set up the DNS zone and TXT record

Complete the steps in this section to set up the DNS zone and TXT record.
If you are not using Route53 as your DNS, then follow the documentation provided
by your DNS provider to set up a DNS Zone and add a TXT record.

If you are using Route53, note the following:

- To create a Reverse Lookup Zone in the AWS console, see [Creating a
  public hosted zone](../../../Route53/latest/DeveloperGuide/CreatingHostedZone.md "../../../Route53/latest/DeveloperGuide/CreatingHostedZone.md") in the _Amazon Route 53 Developer Guide_ or
  use the AWS CLI command [create-hosted-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-hosted-zone.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-hosted-zone.html").
- To create a record in the Reverse Lookup Zone in the AWS console, see [Creating records by using the Amazon Route 53 console](../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md") in the
  _Amazon Route 53 Developer Guide_ or use the AWS CLI command [change-resource-record-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/change-resource-record-sets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/change-resource-record-sets.html").
- After you are done creating your hosted zone, delegate the hosted zone from
  your RIR to the name servers provided by Route53 (such as for [LACNIC](https://www.lacnic.net/1017/2/lacnic/reverse-dns-resolution "https://www.lacnic.net/1017/2/lacnic/reverse-dns-resolution") or [APNIC](https://www.apnic.net/manage-ip/manage-resources/reverse-dns/ "https://www.apnic.net/manage-ip/manage-resources/reverse-dns/")).

Whether you are using another DNS provider or Route53, when
you set up the TXT record, note the following:

- Record name should be your token name.
- Record type should be TXT.
- ResourceRecord Value should be the token value.

Example:

- **Name**: `86950620.113.0.203.in-addr.arpa`
- **Type**: `TXT`
- **ResourceRecords Value**:
  `a34597c3-5317-4238-9ce7-50da5b6e6dc8`

Where:

- `86950620` is the verification token name.
- `113.0.203.in-addr.arpa` is the Reverse Lookup Zone name.
- `TXT` is the record type.
- `a34597c3-5317-4238-9ce7-50da5b6e6dc8` is the verification token value.

###### Note

Depending on the size of the prefix to be brought to IPAM with BYOIP, one or more
authentication records must be created in the DNS. These authentication
records are of the record type TXT and must be placed into the reverse zone
of the prefix itself or its parent prefix.

- For IPv4, authentication records need to align to ranges at an octet boundary that make up the prefix.
  - **Examples**
  - For 198.18.123.0/24, which is already aligned at an octet boundary, you would need to create a single authentication record at:
    - `*token-name*.123.18.198.in-addr.arpa. IN TXT
“*token-value*”`

  - For 198.18.12.0/22, which itself is not aligned to octet boundary, you would need to create four authentication records. These records must cover the subnets 198.18.12.0/24, 198.18.13.0/24, 198.18.14.0/24, and 198.18.15.0/24 which are aligned at an octet boundary. The corresponding DNS entries must be:
    - `*token-name*.12.18.198.in-addr.arpa.
IN TXT
“*token-value*”`
    - `*token-name*.13.18.198.in-addr.arpa.
IN TXT
“*token-value*”`
    - `*token-name*.14.18.198.in-addr.arpa.
IN TXT
“*token-value*”`
    - `*token-name*.15.18.198.in-addr.arpa.
IN TXT
“*token-value*”`

  - For 198.18.0.0/16, which is already aligned at an octet boundary, you need to create a single authentication record:
    - `*token-name*.18.198.in-addr.arpa. IN TXT “*token-value*”`

- For IPv6, authentication records need to align to
  ranges at nibble boundary that make up the prefix. Valid
  nibble values are e.g. 32, 36, 40, 44, 48, 52, 56, and

60. - **Examples**
      - For 2001:0db8::/40, which is already aligned at
        nibble boundary, you need to create a single
        authentication record:
        - `*token-name*.0.0.8.b.d.0.1.0.0.2.ip6.arpa
TXT
“*token-value*”`

      - For 2001:0db8:80::/42, which is itself not aligned
        at nibble boundary, you need to create four
        authentication records. These records must cover the
        subnets 2001:db8:80::/44, 2001:db8:90::/44,
        2001:db8:a0::/44, and 2001:db8:b0::/44 which are
        aligned at a nibble boundary. The corresponding DNS
        entries must be:
        - `*token-name*.8.0.0.8.b.d.0.1.0.0.2.ip6.arpa
TXT
“*token-value*”`
        - `*token-name*.9.0.0.8.b.d.0.1.0.0.2.ip6.arpa
TXT “*token-value*”`
        - `*token-name*.a.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`
        - `*token-name*.b.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`

      - For the non-advertised range 2001:db8:0:1000::/54,
        which is itself not aligned at a nibble boundary,
        you need to create four authentication records.
        These records must cover the subnets
        2001:db8:0:1000::/56, 2001:db8:0:1100::/56,
        2001:db8:0:1200::/56, and 2001:db8:0:1300::/56 which
        are aligned at a nibble boundary. The corresponding
        DNS entries must be:
        - `*token-name*.0.1.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`
        - `*token-name*.1.1.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`
        - `*token-name*.2.1.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`
        - `*token-name*.3.1.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
IN TXT “*token-value*”`

    - To validate the correct number of hexadecimal numbers
      between the _token-name_ and the
      "ip6.arpa" string, multiply the number by four. The result
      should match the prefix length. For example, for a /56
      prefix you should have 14 hexadecimal digits.

When you've completed these steps, continue with [Bring your own IP to IPAM using both the AWS Management Console and the AWS CLI](tutorials-byoip-ipam-console-intro.md "tutorials-byoip-ipam-console-intro.md") or [Bring your own IP CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-cli-only-intro.md "tutorials-byoip-ipam-cli-only-intro.md").
